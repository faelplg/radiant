"""Validate the formats that describe dispatch: requirements, provides, units and routing.

Each validator returns a list of messages and never raises on bad content, so
the repository check can report every problem at once.
"""

import json
import re

CAPABILITIES = ["deep", "standard", "light"]


def load_requirements(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    terms = data.get("requirements") if isinstance(data, dict) else None
    if not isinstance(terms, dict) or not terms or set(data) != {"requirements"}:
        raise ValueError(f"{path.name}: expected {{\"requirements\": {{term: description}}}}")
    for term, description in terms.items():
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"{path.name}: {term!r} without a description")
    return set(terms)


def validate_provides(data, requirements):
    if not isinstance(data, dict) or set(data) != {"provides"} or not isinstance(data["provides"], list):
        return ["expected {\"provides\": [term, ...]}"]
    errors, seen = [], set()
    for term in data["provides"]:
        if not isinstance(term, str) or term not in requirements:
            errors.append(f"unknown requirement {term!r}")
            continue
        if term in seen:
            errors.append(f"repeated requirement {term!r}")
        seen.add(term)
    return errors


UNIT_ID = re.compile(r"TC-\d{4}\.[1-9]\d*$")
UNIT_KEYS = {"id", "role", "capability", "capability_reason", "requires", "objective",
             "writes", "depends_on", "done_when"}
UNIT_REQUIRED = ("id", "role", "objective", "writes", "done_when")
UNITS_FENCE = re.compile(r"(?m)^```yaml radiant-units[ \t]*\n(.*?)^```[ \t]*$", re.S)


def extract_units_block(markdown):
    blocks = UNITS_FENCE.findall(markdown)
    if len(blocks) > 1:
        raise ValueError("more than one radiant-units block")
    return blocks[0] if blocks else None


def text_list(value):
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


def overlaps(first, second):
    first, second = first.rstrip("/"), second.rstrip("/")
    return first == second or first.startswith(second + "/") or second.startswith(first + "/")


def reachable(graph, start):
    """Units that start depends on, directly or not; the visited set stops cycles."""
    seen, stack = set(), list(graph.get(start, ()))
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            stack.extend(graph.get(current, ()))
    return seen


def validate_unit(unit, agents, requirements):
    if not isinstance(unit, dict):
        return ["unit must be a mapping"]
    name = unit.get("id", "?")
    errors = [f"{name}: unknown key {key!r}" for key in sorted(set(unit) - UNIT_KEYS)]
    errors += [f"{name}: missing {key!r}" for key in UNIT_REQUIRED if key not in unit]
    if not isinstance(unit.get("id"), str) or not UNIT_ID.match(unit.get("id", "")):
        errors.append(f"{name}: id does not match TC-0000.N")
    if "role" in unit and (not isinstance(unit["role"], str) or unit["role"] not in agents):
        errors.append(f"{name}: unknown profile {unit['role']!r}")
    if "capability" in unit:
        if not isinstance(unit["capability"], str) or unit["capability"] not in CAPABILITIES:
            errors.append(f"{name}: unknown capability {unit['capability']!r}")
        reason = unit.get("capability_reason")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{name}: capability requires capability_reason")
    elif "capability_reason" in unit:
        errors.append(f"{name}: capability_reason without capability")
    requires = unit.get("requires", [])
    if not isinstance(requires, list):
        errors.append(f"{name}: requires must be a list")
    else:
        errors += [f"{name}: unknown requirement {term!r}" for term in requires
                   if not isinstance(term, str) or term not in requirements]
    writes = unit.get("writes")
    if "writes" in unit:
        if not text_list(writes) or not writes:
            errors.append(f"{name}: writes must be a non-empty list of paths")
        else:
            for path in writes:
                segments = (path[:-1] if path.endswith("/") else path).split("/")
                if path.startswith("/") or any(segment in ("", ".", "..") for segment in segments):
                    errors.append(f"{name}: path outside the project or not normalized {path!r}")
    if not text_list(unit.get("depends_on", [])):
        errors.append(f"{name}: depends_on must be a list of ids")
    for key in ("objective", "done_when"):
        if key in unit and (not isinstance(unit[key], str) or not unit[key].strip()):
            errors.append(f"{name}: {key} must be non-empty text")
    return errors


def validate_units(data, agents, requirements):
    if not isinstance(data, dict) or set(data) != {"units"} or not isinstance(data["units"], list) \
            or not data["units"]:
        return ["expected non-empty {units: [unit, ...]}"]
    units = data["units"]
    errors = []
    for unit in units:
        errors += validate_unit(unit, agents, requirements)
    if errors:
        return errors
    ids = [unit["id"] for unit in units]
    if len(set(ids)) != len(ids):
        errors.append("repeated unit id")
    if len({unit_id.split(".")[0] for unit_id in ids}) > 1:
        errors.append("all units must share the same contract prefix")
    graph = {unit["id"]: unit.get("depends_on", []) for unit in units}
    for unit_id, dependencies in graph.items():
        for dependency in dependencies:
            if dependency == unit_id or dependency not in graph:
                errors.append(f"{unit_id}: invalid dependency {dependency!r}")
    if errors:
        return errors
    closure = {unit_id: reachable(graph, unit_id) for unit_id in graph}
    for unit_id in graph:
        if unit_id in closure[unit_id]:
            errors.append(f"{unit_id}: cycle in depends_on")
    if errors:
        return errors
    for index, first in enumerate(units):
        for second in units[index + 1:]:
            if second["id"] in closure[first["id"]] or first["id"] in closure[second["id"]]:
                continue
            for path in first["writes"]:
                for other in second["writes"]:
                    if overlaps(path, other):
                        errors.append(f"{first['id']} and {second['id']}: writes overlap at {path!r} and {other!r}")
    return errors


RULE_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*$")
RULE_KEYS = {"id", "when", "use", "approval", "why"}
CANDIDATE_KEYS = {"harness", "capability", "effort"}


def validate_candidates(candidates, adapters, where):
    if not isinstance(candidates, list) or not candidates:
        return [f"{where}: a non-empty candidate list is required"]
    errors = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            errors.append(f"{where}: candidate must be an object")
            continue
        errors += [f"{where}: unknown key {key!r}" for key in sorted(set(candidate) - CANDIDATE_KEYS)]
        harness = candidate.get("harness")
        if not isinstance(harness, str) or harness not in adapters:
            errors.append(f"{where}: harness without an adapter {candidate.get('harness')!r}")
        if "capability" in candidate and (not isinstance(candidate["capability"], str)
                                          or candidate["capability"] not in CAPABILITIES):
            errors.append(f"{where}: unknown capability {candidate['capability']!r}")
        effort = candidate.get("effort", "x")
        if not isinstance(effort, str) or not effort.strip():
            errors.append(f"{where}: effort must be non-empty text")
    return errors


def validate_routing(data, adapters):
    if not isinstance(data, dict) or set(data) != {"schema", "rules", "default"}:
        return ["expected {schema, rules, default}"]
    errors = []
    if data["schema"] != 1:
        errors.append(f"unknown schema {data['schema']!r}")
    rules = data["rules"]
    if not isinstance(rules, list):
        return errors + ["rules must be a list"]
    seen = set()
    for rule in rules:
        if not isinstance(rule, dict):
            errors.append("rule must be an object")
            continue
        rule_id = rule.get("id")
        where = f"rule {rule_id!r}"
        errors += [f"{where}: unknown key {key!r}" for key in sorted(set(rule) - RULE_KEYS)]
        if not isinstance(rule_id, str) or not RULE_ID.match(rule_id):
            errors.append(f"{where}: id is not kebab-case")
        elif rule_id in seen:
            errors.append(f"{where}: repeated id")
        else:
            seen.add(rule_id)
        for key in ("when", "why"):
            if (key == "when" or key in rule) and (not isinstance(rule.get(key), str) or not rule[key].strip()):
                errors.append(f"{where}: {key} must be non-empty text")
        if "approval" in rule and rule["approval"] != "human":
            errors.append(f"{where}: approval only accepts 'human'")
        errors += validate_candidates(rule.get("use"), adapters, where)
    errors += validate_candidates(data["default"], adapters, "default")
    return errors

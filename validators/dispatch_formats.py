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
        raise ValueError(f"{path.name}: esperado {{\"requirements\": {{termo: descrição}}}}")
    for term, description in terms.items():
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"{path.name}: {term!r} sem descrição")
    return set(terms)


def validate_provides(data, requirements):
    if not isinstance(data, dict) or set(data) != {"provides"} or not isinstance(data["provides"], list):
        return ["esperado {\"provides\": [termo, ...]}"]
    errors, seen = [], set()
    for term in data["provides"]:
        if term not in requirements:
            errors.append(f"requisito desconhecido {term!r}")
        elif term in seen:
            errors.append(f"requisito repetido {term!r}")
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
        raise ValueError("mais de um bloco radiant-units")
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
        return ["unidade deve ser um mapeamento"]
    name = unit.get("id", "?")
    errors = [f"{name}: chave desconhecida {key!r}" for key in sorted(set(unit) - UNIT_KEYS)]
    errors += [f"{name}: falta {key!r}" for key in UNIT_REQUIRED if key not in unit]
    if not isinstance(unit.get("id"), str) or not UNIT_ID.match(unit.get("id", "")):
        errors.append(f"{name}: id fora do padrão TC-0000.N")
    if "role" in unit and unit["role"] not in agents:
        errors.append(f"{name}: perfil desconhecido {unit['role']!r}")
    if "capability" in unit:
        if unit["capability"] not in CAPABILITIES:
            errors.append(f"{name}: capacidade desconhecida {unit['capability']!r}")
        reason = unit.get("capability_reason")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{name}: capability exige capability_reason")
    elif "capability_reason" in unit:
        errors.append(f"{name}: capability_reason sem capability")
    requires = unit.get("requires", [])
    if not isinstance(requires, list):
        errors.append(f"{name}: requires deve ser lista")
    else:
        errors += [f"{name}: requisito desconhecido {term!r}" for term in requires if term not in requirements]
    writes = unit.get("writes")
    if "writes" in unit:
        if not text_list(writes) or not writes:
            errors.append(f"{name}: writes deve ser lista não vazia de paths")
        else:
            for path in writes:
                if path.startswith("/") or ".." in path.split("/"):
                    errors.append(f"{name}: path fora do projeto {path!r}")
    if not text_list(unit.get("depends_on", [])):
        errors.append(f"{name}: depends_on deve ser lista de ids")
    for key in ("objective", "done_when"):
        if key in unit and (not isinstance(unit[key], str) or not unit[key].strip()):
            errors.append(f"{name}: {key} deve ser texto não vazio")
    return errors


def validate_units(data, agents, requirements):
    if not isinstance(data, dict) or set(data) != {"units"} or not isinstance(data["units"], list) \
            or not data["units"]:
        return ["esperado {units: [unidade, ...]} não vazio"]
    units = data["units"]
    errors = []
    for unit in units:
        errors += validate_unit(unit, agents, requirements)
    if errors:
        return errors
    ids = [unit["id"] for unit in units]
    if len(set(ids)) != len(ids):
        errors.append("id de unidade repetido")
    if len({unit_id.split(".")[0] for unit_id in ids}) > 1:
        errors.append("todas as unidades devem ter o mesmo prefixo de contrato")
    graph = {unit["id"]: unit.get("depends_on", []) for unit in units}
    for unit_id, dependencies in graph.items():
        for dependency in dependencies:
            if dependency == unit_id or dependency not in graph:
                errors.append(f"{unit_id}: dependência inválida {dependency!r}")
    if errors:
        return errors
    closure = {unit_id: reachable(graph, unit_id) for unit_id in graph}
    for unit_id in graph:
        if unit_id in closure[unit_id]:
            errors.append(f"{unit_id}: ciclo em depends_on")
    if errors:
        return errors
    for index, first in enumerate(units):
        for second in units[index + 1:]:
            if second["id"] in closure[first["id"]] or first["id"] in closure[second["id"]]:
                continue
            for path in first["writes"]:
                for other in second["writes"]:
                    if overlaps(path, other):
                        errors.append(f"{first['id']} e {second['id']}: writes se sobrepõem em {path!r} e {other!r}")
    return errors


RULE_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*$")
RULE_KEYS = {"id", "when", "use", "approval", "why"}
CANDIDATE_KEYS = {"harness", "capability", "effort"}


def validate_candidates(candidates, adapters, where):
    if not isinstance(candidates, list) or not candidates:
        return [f"{where}: lista de candidatos não vazia é obrigatória"]
    errors = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            errors.append(f"{where}: candidato deve ser um objeto")
            continue
        errors += [f"{where}: chave desconhecida {key!r}" for key in sorted(set(candidate) - CANDIDATE_KEYS)]
        if candidate.get("harness") not in adapters:
            errors.append(f"{where}: harness sem adapter {candidate.get('harness')!r}")
        if "capability" in candidate and candidate["capability"] not in CAPABILITIES:
            errors.append(f"{where}: capacidade desconhecida {candidate['capability']!r}")
        effort = candidate.get("effort", "x")
        if not isinstance(effort, str) or not effort.strip():
            errors.append(f"{where}: effort deve ser texto não vazio")
    return errors


def validate_routing(data, adapters):
    if not isinstance(data, dict) or set(data) != {"schema", "rules", "default"}:
        return ["esperado {schema, rules, default}"]
    errors = []
    if data["schema"] != 1:
        errors.append(f"schema desconhecido {data['schema']!r}")
    rules = data["rules"]
    if not isinstance(rules, list):
        return errors + ["rules deve ser lista"]
    seen = set()
    for rule in rules:
        if not isinstance(rule, dict):
            errors.append("regra deve ser um objeto")
            continue
        rule_id = rule.get("id")
        where = f"regra {rule_id!r}"
        errors += [f"{where}: chave desconhecida {key!r}" for key in sorted(set(rule) - RULE_KEYS)]
        if not isinstance(rule_id, str) or not RULE_ID.match(rule_id):
            errors.append(f"{where}: id fora do padrão kebab-case")
        elif rule_id in seen:
            errors.append(f"{where}: id repetido")
        seen.add(rule_id)
        for key in ("when", "why"):
            if (key == "when" or key in rule) and (not isinstance(rule.get(key), str) or not rule[key].strip()):
                errors.append(f"{where}: {key} deve ser texto não vazio")
        if "approval" in rule and rule["approval"] != "human":
            errors.append(f"{where}: approval só aceita 'human'")
        errors += validate_candidates(rule.get("use"), adapters, where)
    errors += validate_candidates(data["default"], adapters, "default")
    return errors

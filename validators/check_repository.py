#!/usr/bin/env python3
"""Validate repository navigation, delegation consistency and portable source files."""

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import radiant_yaml
from dispatch_formats import (CAPABILITIES, extract_units_block, load_requirements,
                              validate_provides, validate_routing, validate_units)


ROOT = Path(__file__).resolve().parents[1]


def prose(text):
    """Ignore fenced examples and frontmatter, not actual document navigation."""
    if text.startswith("---\n"):
        text = text.split("---\n", 2)[-1]
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", text)


def anchors(text):
    result = set()
    counts = {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", prose(text)):
        slug = re.sub(r"[^\w\-\s]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def markdown_documents():
    """List tracked and untracked Markdown, honoring Git ignores such as harness worktrees."""
    if not any((directory / ".git").exists() for directory in (ROOT, *ROOT.parents)):
        return [path for path in ROOT.rglob("*.md")
                if not {".local", "__pycache__"}.intersection(path.relative_to(ROOT).parts)]
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.md"],
        cwd=ROOT, capture_output=True, text=True)
    if listing.returncode != 0:
        raise ValueError(f"git ls-files failed: {listing.stderr.strip()}")
    return sorted({ROOT / relative for relative in listing.stdout.split("\0")
                   if relative and (ROOT / relative).is_file()})


def check_delegation(errors):
    """Keep delegable profiles and every adapter's model map consistent with the core."""
    registry = "skills/radiant-delegation/agents.json"
    data = json.loads((ROOT / registry).read_text(encoding="utf-8"))
    if data.get("capabilities") != CAPABILITIES:
        errors.append(f"{registry}: capabilities must be exactly {CAPABILITIES}")
    roles = anchors((ROOT / "skills/radiant-delegation/SKILL.md").read_text(encoding="utf-8"))
    names = set()
    for agent in data.get("agents", []):
        name = agent.get("name", "")
        if not name.startswith("radiant-") or name in names:
            errors.append(f"{registry}: invalid or repeated agent name: {name!r}")
        names.add(name)
        if agent.get("capability") not in CAPABILITIES:
            errors.append(f"{registry}: {name}: unknown capability {agent.get('capability')!r}")
        if agent.get("access") not in ("read", "write"):
            errors.append(f"{registry}: {name}: unknown access {agent.get('access')!r}")
        if agent.get("role") not in roles:
            errors.append(f"{registry}: {name}: role without a section in the skill: {agent.get('role')!r}")
    bootstrap = (ROOT / "adapters/global.template.md").read_text(encoding="utf-8")
    for adapter in sorted(p for p in (ROOT / "adapters").iterdir() if p.is_dir()):
        if f"adapters/{adapter.name}/README.md" not in bootstrap:
            errors.append(f"adapters/global.template.md: does not point to adapters/{adapter.name}/README.md")
        mapping = adapter / "capabilities.json"
        relative = mapping.relative_to(ROOT).as_posix()
        if not mapping.is_file():
            errors.append(f"{relative}: adapter without a capability map")
            continue
        models = json.loads(mapping.read_text(encoding="utf-8"))
        if (not isinstance(models, dict) or set(models) != set(CAPABILITIES)
                or not all(isinstance(v, str) and v.strip() for v in models.values())):
            errors.append(f"{relative}: must map {CAPABILITIES} to non-empty model IDs")


def check_dispatch(errors):
    """Keep requirements, provides, the template units example and the routing example consistent."""
    example = "docs/routing.example.json"
    adapters = {p.name for p in (ROOT / "adapters").iterdir() if p.is_dir()}
    try:
        routing = json.loads((ROOT / example).read_text(encoding="utf-8"))
        errors.extend(f"{example}: {message}" for message in validate_routing(routing, adapters))
    except ValueError as error:
        errors.append(f"{example}: invalid JSON: {error}")
    requirements = load_requirements(ROOT / "skills/radiant-delegation/requirements.json")
    for adapter in sorted(p for p in (ROOT / "adapters").iterdir() if p.is_dir()):
        path = adapter / "provides.json"
        relative = path.relative_to(ROOT).as_posix()
        if not path.is_file():
            errors.append(f"{relative}: adapter without a declaration of provided requirements")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            errors.append(f"{relative}: invalid JSON: {error}")
            continue
        errors.extend(f"{relative}: {message}" for message in validate_provides(data, requirements))
    template = "templates/task-contract.md"
    try:
        block = extract_units_block((ROOT / template).read_text(encoding="utf-8"))
        if block is None:
            raise ValueError("no radiant-units example")
        units = radiant_yaml.load(block)
    except ValueError as error:
        errors.append(f"{template}: {error}")
        return
    registry = json.loads((ROOT / "skills/radiant-delegation/agents.json").read_text(encoding="utf-8"))
    agents = {agent.get("name"): agent.get("capability") for agent in registry.get("agents", [])}
    errors.extend(f"{template}: {message}" for message in validate_units(units, agents, requirements))


def check():
    errors = []
    check_delegation(errors)
    check_dispatch(errors)
    link_count = 0
    documents = markdown_documents()
    for source in documents:
        relative = source.relative_to(ROOT).as_posix()
        body = prose(source.read_text(encoding="utf-8"))
        if re.search(r"/(?:Users|home)/[^\s/]+/", body):
            errors.append(f"personal path in portable source: {relative}")
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            link_count += 1
            destination = (source.parent / unquote(target.path)).resolve() if target.path else source
            if not destination.is_relative_to(ROOT):
                errors.append(f"link outside the repository: {relative}: {raw}")
            elif not destination.exists():
                errors.append(f"broken link: {relative}: {raw}")
            elif target.fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(target.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"missing anchor: {relative}: {raw}")
    constitutions = [p for p in documents
                     if re.search(r"(?m)^# Radiant Constitution\s*$", p.read_text(encoding="utf-8"))]
    if constitutions != [ROOT / "constitution/CONSTITUTION.md"]:
        errors.append("the Constitution must have a single normative body")
    if errors:
        print("FAIL:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(documents)} documents; {link_count} local links.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(check())
    except (OSError, ValueError, KeyError) as error:
        sys.exit(f"FAIL: {error}")

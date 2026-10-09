#!/usr/bin/env python3
"""Validate repository navigation, migration custody and portable source files."""

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


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


CAPABILITIES = ["deep", "standard", "light"]


def check_delegation(errors):
    """Keep delegable profiles and every adapter's model map consistent with the core."""
    registry = "skills/radiant-delegation/agents.json"
    data = json.loads((ROOT / registry).read_text(encoding="utf-8"))
    if data.get("capabilities") != CAPABILITIES:
        errors.append(f"{registry}: capacidades devem ser exatamente {CAPABILITIES}")
    roles = anchors((ROOT / "skills/radiant-delegation/SKILL.md").read_text(encoding="utf-8"))
    names = set()
    for agent in data.get("agents", []):
        name = agent.get("name", "")
        if not name.startswith("radiant-") or name in names:
            errors.append(f"{registry}: nome de agente inválido ou repetido: {name!r}")
        names.add(name)
        if agent.get("capability") not in CAPABILITIES:
            errors.append(f"{registry}: {name}: capacidade desconhecida {agent.get('capability')!r}")
        if agent.get("role") not in roles:
            errors.append(f"{registry}: {name}: papel sem seção na skill: {agent.get('role')!r}")
    for adapter in sorted(p for p in (ROOT / "adapters").iterdir() if p.is_dir()):
        mapping = adapter / "capabilities.json"
        relative = mapping.relative_to(ROOT).as_posix()
        if not mapping.is_file():
            errors.append(f"{relative}: adapter sem mapa de capacidades")
            continue
        models = json.loads(mapping.read_text(encoding="utf-8"))
        if (not isinstance(models, dict) or set(models) != set(CAPABILITIES)
                or not all(isinstance(v, str) and v.strip() for v in models.values())):
            errors.append(f"{relative}: deve mapear {CAPABILITIES} para IDs de modelo não vazios")


def check():
    errors = []
    check_delegation(errors)
    inventory = json.loads((ROOT / "migration/inventory.json").read_text(encoding="utf-8"))
    historical = json.loads((ROOT / "migration/historical-links.json").read_text(encoding="utf-8"))
    exceptions = {(item["source"], item["target"]) for item in historical}
    observed = set()
    link_count = 0
    for item in inventory:
        destination = ROOT / item["destination"]
        if item.get("local_only") and not destination.exists():
            continue
        if not destination.is_file():
            errors.append(f"arquivo inventariado ausente: {item['destination']}")
        elif item["preserved"] and hashlib.sha256(destination.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"snapshot alterado: {item['destination']}")

    documents = [path for path in ROOT.rglob("*.md")
                 if not {".git", ".local", "__pycache__"}.intersection(path.relative_to(ROOT).parts)]
    for source in documents:
        relative = source.relative_to(ROOT).as_posix()
        body = prose(source.read_text(encoding="utf-8"))
        if not relative.startswith("migration/aikm/") and re.search(r"/(?:Users|home)/[^\s/]+/", body):
            errors.append(f"path pessoal em fonte portátil: {relative}")
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            if (relative, raw) in exceptions:
                observed.add((relative, raw))
                continue
            target = urlsplit(raw.strip("<>"))
            if target.scheme or target.netloc:
                continue
            link_count += 1
            destination = (source.parent / unquote(target.path)).resolve() if target.path else source
            if not destination.is_relative_to(ROOT):
                errors.append(f"link fora do repository: {relative}: {raw}")
            elif not destination.exists():
                errors.append(f"link quebrado: {relative}: {raw}")
            elif target.fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(target.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"anchor ausente: {relative}: {raw}")
    if exceptions != observed:
        errors.append(f"exceções históricas sem referência: {sorted(exceptions - observed)}")
    constitutions = [p for p in documents
                     if not p.relative_to(ROOT).as_posix().startswith("migration/")
                     and re.search(r"(?m)^# Radiant Constitution\s*$", p.read_text(encoding="utf-8"))]
    if constitutions != [ROOT / "constitution/CONSTITUTION.md"]:
        errors.append("a Constitution deve possuir um único corpo normativo")
    if errors:
        print("FAIL:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(documents)} documentos; {link_count} links locais; "
          f"{len(observed)} referências históricas explicitamente mapeadas; custódia íntegra.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(check())
    except (OSError, ValueError, KeyError) as error:
        sys.exit(f"FAIL: {error}")

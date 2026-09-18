#!/usr/bin/env python3
"""Check a consumer's Radiant pin and local pointers without changing files."""

import argparse
import json
import re
import subprocess
from pathlib import Path


FILES = ("frame", "spec", "plan", "workflow", "active_contract", "engineering_profile")
DIRECTORIES = ("contracts", "adrs", "verification", "learning")
FIELDS = {"radiant_revision", *FILES, *DIRECTORIES}


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True,
        text=True, capture_output=True,
    ).stdout.strip()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"campo repetido: {key}")
        result[key] = value
    return result


def validate(root, project):
    required = ("constitution/CONSTITUTION.md", "docs/integration.md",
                "skills/radiant-cycle/SKILL.md")
    if not all((root / path).is_file() for path in required):
        raise ValueError("checkout Radiant incompleto")
    if Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("a raiz Radiant não é a raiz do repositório Git")
    mapping = project / ".radiant.json"
    if not mapping.resolve().is_relative_to(project):
        raise ValueError(".radiant.json escapa do projeto")
    config = json.loads(mapping.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(config, dict) or set(config) != FIELDS:
        raise ValueError("campos do mapa diferem de templates/radiant-project.json")
    revision = config["radiant_revision"]
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
        raise ValueError("radiant_revision deve ser um commit completo, não branch/HEAD/template")
    if git(root, "rev-parse", "HEAD") != revision:
        raise ValueError("revisão do checkout difere do pin; não atualizar o pin automaticamente")
    if git(root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("checkout Radiant contém mudanças locais; use a revisão limpa registrada")
    for field in (*FILES, *DIRECTORIES):
        value = config[field]
        if value is None:
            continue
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field}: path relativo ou null esperado")
        path = Path(value)
        target = project / path
        if path.is_absolute() or ".." in path.parts or not target.resolve().is_relative_to(project):
            raise ValueError(f"{field}: path escapa do projeto")
        valid = target.is_file() if field in FILES else target.is_dir()
        if not valid:
            raise ValueError(f"{field}: destino ausente ou tipo incorreto")
    return revision


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="consumer repository root")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        revision = validate(root, args.project.resolve())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        parser.exit(1, f"HOLD: {detail}\n")
    print(f"PASS: Radiant {revision}; pin e paths conferidos. Autorização da tarefa é separada.")


if __name__ == "__main__":
    main()

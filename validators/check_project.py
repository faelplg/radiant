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
# Optional: may be absent from the map, and its directory may not exist yet.
OPTIONAL = ("maintenance",)


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True,
        text=True, capture_output=True,
    ).stdout.strip()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"repeated field: {key}")
        result[key] = value
    return result


def stack_pack(root, profile):
    declarations = []
    fence = None
    for line in profile.read_text(encoding="utf-8").splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if (marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence)
                    and not marker[2].strip()):
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        if re.match(r"^[ \t]*- Stack pack:", line):
            declarations.append(line.strip())
    if not declarations:
        return None
    if len(declarations) != 1:
        raise ValueError("engineering_profile: repeated Stack pack lines")
    match = re.fullmatch(r"- Stack pack: `([a-z0-9]+(?:-[a-z0-9]+)*)`", declarations[0])
    if match is None:
        raise ValueError("engineering_profile: expected - Stack pack: `<lowercase-kebab-id>`")
    pack = match[1]
    if pack == "none":
        return None
    known = {path.stem for path in (root / "engineering/stacks").glob("*.md")
             if path.name != "README.md"}
    if pack not in known:
        raise ValueError(f"engineering_profile: unknown Stack pack: {pack}")
    return pack


def validate(root, project):
    required = ("constitution/CONSTITUTION.md", "docs/integration.md",
                "skills/radiant-cycle/SKILL.md", "engineering/stacks/README.md")
    if not all((root / path).is_file() for path in required):
        raise ValueError("incomplete Radiant checkout")
    if Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("the Radiant root is not the Git repository root")
    mapping = project / ".radiant.json"
    if not mapping.resolve().is_relative_to(project):
        raise ValueError(".radiant.json escapes the project")
    config = json.loads(mapping.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(config, dict) or not FIELDS <= set(config) <= FIELDS | set(OPTIONAL):
        raise ValueError("map fields differ from templates/radiant-project.json")
    revision = config["radiant_revision"]
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
        raise ValueError("radiant_revision must be a full commit, not a branch, HEAD or template")
    if git(root, "rev-parse", "HEAD") != revision:
        raise ValueError("checkout revision differs from the pin; do not update the pin automatically")
    if git(root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("Radiant checkout has local changes; use the recorded clean revision")
    for field in (*FILES, *DIRECTORIES, *OPTIONAL):
        value = config.get(field)
        if value is None:
            continue
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field}: expected a relative path or null")
        path = Path(value)
        target = project / path
        if path.is_absolute() or ".." in path.parts or not target.resolve().is_relative_to(project):
            raise ValueError(f"{field}: path escapes the project")
        if field in OPTIONAL:
            if path == Path(".") or (target.exists() and not target.is_dir()):
                raise ValueError(f"{field}: expected its own directory inside the project")
            continue
        valid = target.is_file() if field in FILES else target.is_dir()
        if not valid:
            raise ValueError(f"{field}: target missing or of the wrong type")
    profile = config["engineering_profile"]
    pack = stack_pack(root, project / profile) if profile is not None else None
    return revision, pack


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="consumer repository root")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        revision, pack = validate(root, args.project.resolve())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        detail = error.stderr.strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        parser.exit(1, f"HOLD: {detail}\n")
    suffix = f" Stack pack: {pack}." if pack else ""
    print(f"PASS: Radiant {revision}; pin and paths checked. Task authorization is separate.{suffix}")


if __name__ == "__main__":
    main()

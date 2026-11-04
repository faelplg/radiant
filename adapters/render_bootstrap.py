#!/usr/bin/env python3
"""Render the Radiant bootstrap block or a harness's subagents; never modify global configuration."""

import argparse
import json
from pathlib import Path


ADAPTERS = {
    "codex": {"agent": "agent.template.toml", "ext": ".toml",
              "read": 'sandbox_mode = "read-only"\n'},
    "claude-code": {"agent": "agent.template.md", "ext": ".md",
                    "read": "tools: Read, Grep, Glob, WebFetch, WebSearch\n"},
}


def as_json(value):
    return json.dumps(value, ensure_ascii=False)


def render_global(root: Path) -> str:
    """One harness-neutral block, valid whether harnesses share an instructions file or not."""
    template = root / "adapters/global.template.md"
    return template.read_text(encoding="utf-8").replace("{{RADIANT_ROOT_JSON}}", as_json(str(root)))


def instructions(root: Path, agent: dict) -> str:
    skill = root / "skills/radiant-delegation/SKILL.md"
    return (
        f"You run the Radiant {agent['name']} profile. Read the `{agent['role']}` section "
        f"of {skill} and the delegation package you received; it defines inputs, boundary and output. "
        "Do not talk with the human, do not delegate to other agents and do not widen the scope. "
        "Return in the format of the Return section of the same skill."
    )


def render_agents(root: Path, adapter: str) -> dict:
    config = ADAPTERS[adapter]
    template = (root / "adapters" / adapter / config["agent"]).read_text(encoding="utf-8")
    models = json.loads((root / "adapters" / adapter / "capabilities.json").read_text(encoding="utf-8"))
    registry = json.loads((root / "skills/radiant-delegation/agents.json").read_text(encoding="utf-8"))
    files = {}
    for agent in registry["agents"]:
        text = instructions(root, agent)
        values = {
            "{{NAME_JSON}}": as_json(agent["name"]),
            "{{DESCRIPTION_JSON}}": as_json(agent["description"]),
            "{{MODEL_JSON}}": as_json(models[agent["capability"]]),
            "{{INSTRUCTIONS_JSON}}": as_json(text),
            "{{INSTRUCTIONS}}": text,
            "{{ACCESS}}": config["read"] if agent["access"] == "read" else "",
        }
        rendered = template
        for placeholder, value in values.items():
            rendered = rendered.replace(placeholder, value)
        files[agent["name"] + config["ext"]] = rendered
    return files


def write_exclusive(files: dict) -> None:
    """Refuse before writing anything if any destination exists or is a link."""
    taken = [path for path in files if path.exists() or path.is_symlink()]
    if taken:
        raise FileExistsError(", ".join(str(path) for path in taken))
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8") as output:
            output.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adapter", choices=sorted(ADAPTERS), help="harness for --agents-dir")
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--output", type=Path, help="create the global block in a new local file")
    target.add_argument("--agents-dir", type=Path, help="create the Radiant subagents in this directory")
    args = parser.parse_args()
    if args.agents_dir is not None and args.adapter is None:
        parser.error("--agents-dir requires --adapter")
    root = Path(__file__).resolve().parents[1]
    try:
        if args.agents_dir is not None:
            if args.agents_dir.is_symlink():
                raise FileExistsError(f"{args.agents_dir} is a link")
            agents = render_agents(root, args.adapter)
            write_exclusive({args.agents_dir / name: text for name, text in agents.items()})
            print("\n".join(str(args.agents_dir / name) for name in sorted(agents)))
        elif args.output is not None:
            write_exclusive({args.output: render_global(root)})
        else:
            print(render_global(root), end="")
    except OSError as error:
        parser.exit(1, f"Could not create the destination without overwriting: {error}\n")


if __name__ == "__main__":
    main()

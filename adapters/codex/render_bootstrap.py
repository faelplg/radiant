#!/usr/bin/env python3
"""Render the portable Codex pointer; never modify global configuration."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="create a new local file exclusively")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    template = root / "adapters/codex/global.AGENTS.template.md"
    rendered = template.read_text(encoding="utf-8").replace(
        "{{RADIANT_ROOT_JSON}}", json.dumps(str(root), ensure_ascii=False)
    )
    if args.output is None:
        print(rendered, end="")
        return
    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as output:
            output.write(rendered)
    except OSError as error:
        parser.exit(1, f"Não foi possível criar o destino sem sobrescrever: {error}\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate a contract's execution units or the user's routing rules for a dispatch operator.

Read-only. Success prints the parsed value as JSON and exits 0, so the operator
uses this checkout's reader instead of a second one. Invalid content prints
{"errors": [...]} and exits 1; a usage error exits 2.
"""

import argparse
import json
import os
from pathlib import Path
import sys

import radiant_yaml
from dispatch_formats import extract_units_block, load_requirements, validate_routing, validate_units


ROOT = Path(__file__).resolve().parents[1]


def read_text(source):
    return sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")


def default_routing():
    base = os.environ.get("XDG_CONFIG_HOME") or str(Path.home() / ".config")
    return str(Path(base) / "radiant" / "routing.json")


def check_units(source):
    block = extract_units_block(read_text(source))
    if block is None:
        raise ValueError("contrato sem bloco radiant-units")
    data = radiant_yaml.load(block)
    registry = json.loads((ROOT / "skills/radiant-delegation/agents.json").read_text(encoding="utf-8"))
    agents = {agent.get("name"): agent.get("capability") for agent in registry.get("agents", [])}
    requirements = load_requirements(ROOT / "skills/radiant-delegation/requirements.json")
    return data, validate_units(data, agents, requirements)


def check_routing(source):
    data = json.loads(read_text(source))
    adapters = {path.name for path in (ROOT / "adapters").iterdir() if path.is_dir()}
    return data, validate_routing(data, adapters)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    units = commands.add_parser("units", help="validar o bloco radiant-units de um contrato")
    units.add_argument("contract", help="path do contrato, ou - para ler da entrada padrão")
    routing = commands.add_parser("routing", help="validar as regras de roteamento do usuário")
    routing.add_argument("rules", nargs="?", default=None,
                         help="path do routing.json; padrão $XDG_CONFIG_HOME/radiant/routing.json")
    args = parser.parse_args()
    try:
        if args.command == "units":
            data, errors = check_units(args.contract)
        else:
            data, errors = check_routing(args.rules or default_routing())
    except (OSError, ValueError) as error:
        data, errors = None, [str(error)]
    if errors:
        print(json.dumps({"errors": errors}, ensure_ascii=False))
        return 1
    print(json.dumps(data, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

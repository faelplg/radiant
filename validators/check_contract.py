#!/usr/bin/env python3
"""Validate one Task Contract, with an optional explicit Engineering Profile.

Read-only. Success prints template_version and practices as JSON and exits 0;
invalid or unreadable input prints {"errors": [...]} and exits 1. Usage exits 2.
"""

import argparse
import json
from pathlib import Path
import sys

from practice_cards import baseline_ids
from task_contracts import unfenced, validate_contract, version_field

ROOT = Path(__file__).resolve().parents[1]


def read_text(source):
    try:
        return sys.stdin.read() if source == '-' else Path(source).read_text(encoding='utf-8')
    except (OSError, UnicodeError) as error:
        raise ValueError(f'{source}: {error}') from error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract', help='contract path, or - for standard input')
    parser.add_argument('--profile', help='explicit Engineering Profile path')
    args = parser.parse_args()
    try:
        text = read_text(args.contract)
        profile = read_text(args.profile) if args.profile is not None else None
        baseline = baseline_ids(read_text(ROOT / 'engineering/engineering-baseline.md'))
        catalog = {path.stem for path in (ROOT / 'engineering/practices').glob('*.md')
                   if path.name != 'README.md'}
        latest = version_field(unfenced(read_text(ROOT / 'templates/task-contract.md')), 'Version')
        data, errors = validate_contract(text, baseline, catalog, latest, profile)
    except (OSError, ValueError) as error:
        data, errors = None, [str(error)]
    if errors:
        print(json.dumps({'errors': errors}, ensure_ascii=False))
        return 1
    print(json.dumps(data, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())

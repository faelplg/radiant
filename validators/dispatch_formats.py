"""Validate the formats that describe dispatch: requirements, provides, units and routing.

Each validator returns a list of messages and never raises on bad content, so
the repository check can report every problem at once.
"""

import json


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

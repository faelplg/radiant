"""Read practice cards and citations, returning content errors without paths."""

import re
from typing import List, Set, Tuple

CARD_SECTIONS = ("Applies when", "Does not apply when", "Violation signals",
                 "Verification", "Source")
PRACTICE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _prose(text: str) -> str:
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$",
                  lambda match: "\n" * match.group().count("\n"), text)


def baseline_ids(text: str) -> Set[str]:
    return set(re.findall(r"(?m)^#{1,6} .*?\b(EB-\d{2})\b", _prose(text)))


def validate_sections(text: str) -> List[str]:
    text = _prose(text)
    headings = list(re.finditer(r"(?m)^## (.+?)\s*$", text))
    names = [heading.group(1) for heading in headings]
    errors = []
    for section in CARD_SECTIONS:
        if section not in names:
            errors.append(f"missing section: {section}")
    for section in dict.fromkeys(names):
        if section not in CARD_SECTIONS:
            errors.append(f"unknown section: {section}")
        if names.count(section) > 1:
            errors.append(f"repeated section: {section}")
    if not errors and names != list(CARD_SECTIONS):
        errors.append("sections out of order: found " + ", ".join(names)
                      + "; expected " + ", ".join(CARD_SECTIONS))
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        if not text[heading.end():end].strip():
            errors.append(f"section {heading.group(1)!r} must have a non-blank body")
    return errors


def validate_card(text: str, stem: str, baseline: Set[str]) -> List[str]:
    errors = validate_sections(text)
    text = _prose(text)
    if len(re.findall(r"(?m)^# [ \t]*\S.*$", text)) != 1:
        errors.append("card must have exactly one title")
    ids = re.findall(r"(?m)^- Id:[ \t]*(.*)$", text)
    match = re.fullmatch(r"`([^`]+)`", ids[0].strip()) if len(ids) == 1 else None
    if match is None:
        errors.append("Id must occur once with a backticked value")
    else:
        value = match.group(1)
        if not PRACTICE_ID.fullmatch(value):
            errors.append(f"invalid Id: {value!r}")
        if value != stem:
            errors.append(f"Id {value!r} must equal file stem {stem!r}")
    serves = re.findall(r"(?m)^- Serves:[ \t]*(.*)$", text)
    if len(serves) != 1:
        errors.append("Serves must occur once")
    else:
        terms = set(re.findall(r"\bEB-\d{2}\b", serves[0]))
        if not terms:
            errors.append("Serves must name at least one EB id")
        for term in sorted(terms - baseline):
            errors.append(f"Serves names unknown baseline id {term!r}")
    return errors


def table_rows(markdown: str):
    """Yield every data row with its original line number and all cells."""
    lines = _prose(markdown).splitlines()
    in_table = False
    for number, line in enumerate(lines, 1):
        if re.fullmatch(r"\s*\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)+\|?\s*", line):
            in_table = True
            continue
        if not line.strip() or re.match(r"^#{1,6} ", line):
            in_table = False
            continue
        if in_table:
            row = line.strip()
            if row.startswith("|"):
                row = row[1:]
            if row.endswith("|"):
                row = row[:-1]
            yield number, [cell.strip() for cell in row.split("|")]


def _table_rows(markdown: str):
    """Keep the first-cell reader used by card and index validation."""
    for number, cells in table_rows(markdown):
        yield number, cells[0]


def practice_cell(cell: str) -> str:
    """Read a practice id or preserve an invalid cell for diagnostics.

    Relative link targets are compared as text, never opened.
    """
    match = re.fullmatch(r"\[`([a-z0-9]+(?:-[a-z0-9]+)*)`\]\(([^\s()]+)\)", cell)
    if match:
        ident, target = match.groups()
        if (not target.startswith("/") and not re.search(r"[:?#\\]", target)
                and target.split("/")[-1] == ident + ".md"):
            return ident
        return cell
    return (cell[1:-1] if len(cell) >= 2 and cell.startswith("`")
            and cell.endswith("`") else cell)


def practice_ids(markdown: str) -> List[str]:
    text = _prose(markdown)
    section = re.search(r"(?m)^### Practices[ \t]*$", text)
    if section is None:
        return []
    body = text[section.end():]
    end = re.search(r"(?m)^#{1,3} ", body)
    if end:
        body = body[:end.start()]
    return [practice_cell(cell) for _, cell in _table_rows(body)]


def index_ids(markdown: str) -> Tuple[List[str], List[str]]:
    ids = []
    errors = []
    for number, cell in _table_rows(markdown):
        match = re.fullmatch(r"\[`([^`]+)`\]\(([a-z0-9]+(?:-[a-z0-9]+)*)\.md\)", cell)
        if match is None or match.group(1) != match.group(2):
            errors.append(f"line {number}: first cell must be one sibling card link: {cell!r}")
        else:
            ids.append(match.group(2))
    return ids, errors

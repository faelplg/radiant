"""Validate Task Contract text, returning all content errors without paths."""

import re

from practice_cards import PRACTICE_ID, practice_cell, table_rows

ENGINEERING = '8. Engineering Check'
ACCEPTANCE = '12. Acceptance criteria'
DECISIONS = '18. Owner decisions'
PRACTICES = ENGINEERING + ' / Practices'
GENERIC_ITEMS = {
    'all applicable checks in section 11 pass',
    'there was no change outside the Allowed scope',
    'relevant limitations are recorded',
    'the final evidence was read, not just presumed from the exit code',
}


def unfenced(text):
    """Remove fenced lines while preserving line boundaries, including open fences."""
    result = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            result.append('\n')
        elif match:
            fence = match[1]
            result.append('\n')
        else:
            result.append(line)
    return ''.join(result)


def sections(text, level):
    """Return heading names and bodies bounded at the requested heading depth."""
    headings = list(re.finditer(r'(?m)^#{1,' + str(level) + r'}[ \t]+([^\n]+?)[ \t]*$', text))
    return [(heading[1], text[heading.end():headings[index + 1].start()
                             if index + 1 < len(headings) else len(text)])
            for index, heading in enumerate(headings)]


def version_field(text, field):
    match = re.search(r'(?m)^\*\*' + re.escape(field) + r':\*\*[ \t]*(.*)$', text)
    if match is None:
        return None
    return match[1].rstrip().removesuffix('\\').strip().strip('`')


def numeric_version(value):
    return tuple(map(int, value.split('.')))


def project_practices(text, catalog):
    ids, errors = set(), []
    for name, body in sections(unfenced(text), 2):
        if name != 'Project practices':
            continue
        for _, cells in table_rows(body):
            ident = cells[0]
            if len(ident) >= 2 and ident.startswith('`') and ident.endswith('`'):
                ident = ident[1:-1]
            prefix = 'Profile / Project practices: '
            if not PRACTICE_ID.fullmatch(ident):
                errors.append(prefix + 'invalid practice id: ' + ident)
            elif ident in catalog:
                errors.append(prefix + 'catalog practice id: ' + ident)
            if ident in ids:
                errors.append(prefix + 'repeated practice id: ' + ident)
            ids.add(ident)
    return ids, errors


def engineering_check(body, baseline, known):
    errors, practices, seen = [], [], set()
    active = False
    baseline_body = re.split(r'(?m)^###[ \t]+', body, maxsplit=1)[0]
    for _, cells in table_rows(baseline_body):
        ident = cells[0].strip('`').split(' ', 1)[0]
        status = cells[1].strip('`') if len(cells) > 1 else ''
        if ident not in baseline:
            errors.append(ENGINEERING + ': unknown baseline id: ' + ident)
        if ident in seen:
            errors.append(ENGINEERING + ': repeated baseline id: ' + ident)
        seen.add(ident)
        if status not in ('REQUIRED', 'APPLICABLE', 'N/A'):
            errors.append(ENGINEERING + ': ' + ident + ': invalid status: ' + repr(status))
        if status in ('REQUIRED', 'APPLICABLE'):
            active = True
    if not active:
        errors.append(ENGINEERING + ': empty (requires a REQUIRED or APPLICABLE row)')
    bodies = [subbody for name, subbody in sections(body, 3) if name == 'Practices']
    if len(bodies) > 1:
        errors.append('repeated heading: ' + PRACTICES)
    seen = set()
    for subbody in bodies:
        rows = list(table_rows(subbody))
        if not rows:
            errors.append(PRACTICES + ': empty table')
        for _, cells in rows:
            cell = cells[0]
            ident = practice_cell(cell)
            if not PRACTICE_ID.fullmatch(ident):
                errors.append(PRACTICES + ': invalid practice cell: ' + repr(cell))
                continue
            if ident not in known:
                errors.append(PRACTICES + ': unknown practice id: ' + ident)
            if ident in seen:
                errors.append(PRACTICES + ': repeated practice id: ' + ident)
            seen.add(ident)
            practices.append(ident)
    return practices, errors


def concrete_item(item):
    item = item.strip().rstrip(';.,').strip()
    if len(item) >= 2 and item.startswith('`') and item.endswith('`'):
        item = item[1:-1].strip()
    return bool(item and not (item.startswith('[') and item.endswith(']'))
                and item not in GENERIC_ITEMS)


def validate_contract(text, baseline, catalog, latest_version, profile=None):
    """Return the command's success value and every error for the supplied text."""
    text = unfenced(text)
    version = version_field(text, 'Template version')
    errors, practices = [], []
    requires_decisions = False
    if version is not None:
        if not re.fullmatch(r'[0-9]+\.[0-9]+', version):
            errors.append('Template version: malformed: ' + repr(version))
        else:
            if numeric_version(version) > numeric_version(latest_version):
                errors.append('Template version: unsupported: ' + version + '; checkout supports ' + latest_version)
            requires_decisions = numeric_version(version) >= (0, 4)
    local, messages = project_practices(profile, catalog) if profile is not None else (set(), [])
    errors.extend(messages)
    headings = sections(text, 2)
    for title in (ENGINEERING, ACCEPTANCE, DECISIONS):
        bodies = [body for name, body in headings if name == title]
        required = title != DECISIONS or requires_decisions
        if not bodies and required:
            message = 'missing section: ' + title
            if title == DECISIONS:
                message += ' (required by template version ' + version + ')'
            errors.append(message)
        if len(bodies) > 1:
            errors.append('repeated heading: ' + title)
        for body in bodies:
            if title == ENGINEERING:
                found, messages = engineering_check(body, baseline, catalog | local)
                practices.extend(found)
                errors.extend(messages)
            elif title == ACCEPTANCE:
                items = re.findall(r'(?m)^- \[[ xX]\][ \t]+([^\n]+)$', body)
                if not any(concrete_item(item) for item in items):
                    errors.append(ACCEPTANCE + ': empty (requires a concrete checklist item)')
            elif requires_decisions and (not body.strip() or '[YYYY-MM-DD]' in body):
                errors.append(DECISIONS + ': non-blank body without [YYYY-MM-DD] required by template version ' + version)
    return {'template_version': version, 'practices': practices}, errors

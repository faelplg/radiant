# Task Contract convention

This is the shared convention. Instances, activation and evidence belong to
the consumer project. Origin: a convention tested in the first project,
identified in the [inventory](../docs/migration-plan.md). The copy that was in
custody was removed and exists only in Git history.

## Identity and location

Use stable sequential IDs per project, such as `TC-0001`, and filenames like
`TC-0001-short-slug.md`. The ID does not depend on the iteration number. Do
not include version or status in the filename or move contracts between
status folders. One iteration may require more than one contract.

Record the document revision and status in the metadata. Recommended
lifecycle states: `ready`, `active`, `done`, `held`, `failed`, `superseded`.
They do not replace the completion states of the
[Constitution](../constitution/CONSTITUTION.md).

## Activation

The local `ACTIVE.md` points to the contract that governs the work or
explicitly declares `none`. Read that pointer; do not select by timestamp or
filename. A ready proposal does not authorize execution. Record authorization
already granted and update the pointer, without requiring the same
authorization again.

## Integrity

Before execution, a proposal may be refined. Once it has started, do not
silently rewrite its goal, limits, outputs or criteria. Non-material
clarifications go into an explicit amendment. Material changes require HOLD
and a new or superseding contract; record `supersedes`/`supersededBy` when
useful.

The [template](../templates/task-contract.md) captures the delegation. Use the
[revision policy](../docs/integration.md) to pin which Radiant guides it.
Record the procedure actually applied in the evidence, with version and
commit/digest. Shared updates do not rewrite past execution.

Verification and learning reports point to the contract's ID/path, without
copying its body. Close the contract and update `ACTIVE.md` when the
completion is supported. Do not create retroactive contracts to fabricate
compliance.

## Execution units

A contract may split the work into units, in a ` ```yaml radiant-units ` block
of the [template](../templates/task-contract.md). The block uses restricted
YAML, read by `validators/radiant_yaml.py` without dependencies. Every block
valid in this subset is valid YAML with the same value, so readers with a full
parser, such as a dispatch operator, read the same content.

Accepted: block mappings and sequences, including `- key: value` with
continuation aligned to the key; bracketed lists of scalars, without nesting;
double-quoted values (escapes `\"`, `\\` and `\n`) or single-quoted ones
(`''` as a quote); `true`, `false`, `null` and integers; `#` comments on
their own line or after a quoted value or list; indentation with spaces only.

An unquoted value starts with a letter, `_`, `/` or `.` followed by a letter,
and cannot be read by YAML as another type. Use quotes when the text starts
with a digit, backtick or another symbol, is a word like `yes`, `on` or
`True`, or contains `: `, ` #`, a tab or a control character. Inside brackets,
also quote `,`, `[`, `]`, `{` and `}`.

Refused, with the line number: everything the rule above requires to be
quoted, tabs in indentation, a repeated key or one YAML reads as a boolean or
null, anchors (`&`, `*`), tags (`!`), `|` and `>` blocks, braced mappings,
document markers, a comment after an unquoted value and an unquoted value
spanning several lines.

Block rules:

- `id` follows `TC-0000.N`, with the same prefix in every unit, and is never
  renumbered. `role` is a profile from
  [agents.json](../skills/radiant-delegation/agents.json).
- A missing `capability` uses the profile's default; when present, it requires
  `capability_reason`. `requires` uses the terms from
  [requirements.json](../skills/radiant-delegation/requirements.json).
- `writes` is a subset of the contract's writable paths, without `..` or an
  absolute path, and normalized: no `.`, `./` or `//`. Units with no
  dependency between them do not overlap.
- `depends_on` cites only units of the same contract, without cycles.
- The sum of the units does not exceed the contract's goal, outputs and
  boundary. Changing the split after the start is an amendment when the
  boundary does not change and requires `HOLD` when it does.

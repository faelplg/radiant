# Maintenance report - [project] - [YYYY-MM-DD]

Form for the [maintenance skill](../skills/radiant-maintenance/SKILL.md).
The filled report lives in the consumer's `maintenance` directory, ignored by
Git.

## Run

- Radiant revision: `[full commit]`
- Consumer commit: `[commit]`
- Previous report: `[path | none]`
- Mode: `[manual | scheduled, with the mechanism]`
- Main session: `[requested capability, effective model ID, deviation | no deviation]`
- Delegations, one per round: `[profile, capability, model ID, state, adapter usage metric | absent]`

## Sources

| Source | Status | Detail |
| --- | --- | --- |
| `[source]` | `consulted / skipped by policy / failed` | `[command, reason or error]` |

## Candidates

| ID | Category | Evidence | Risk | Value | Reversibility | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `M-1` | `[cycle / gate / drift / dependency / forge / pin]` | `[output, path:line]` | `[low/medium/high]` | `[low/medium/high]` | `[high/medium/low]` | `new / recurring / resolved` |

## Contract drafts

Up to three candidates at the top. They are not contracts and have no ID.

### `[M-1]` - [title]

- Goal: `[observable change]`
- Outputs: `[files or behavior]`
- Verification: `[command or criterion]`

## Omissions and limitations

- `[what was not observed and why]`

## State

`DONE | HOLD | FAIL` - `[one-sentence conclusion, including "nothing material" when that is the case]`

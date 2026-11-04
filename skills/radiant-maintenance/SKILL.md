---
name: radiant-maintenance
description:
  Run maintenance triage of a Radiant consumer project and produce a report
  with prioritized proposals and contract drafts, without changing the
  project. Use in a manual run or a locally scheduled one.
metadata:
  version: "0.1.4"
---

# Radiant maintenance

Maintenance observes a consumer and feeds the
[cycle](../radiant-cycle/SKILL.md) with proposals. It only proposes: nothing
changes in the project until the human selects a candidate and the
orchestrator creates and activates a contract. Roles, capabilities and return
follow the [delegation skill](../radiant-delegation/SKILL.md); the report
format follows the [template](../../templates/maintenance-report.md).

## Entry

1. Read `.radiant.json` and run the adapter's gate. Without a `maintenance`
   field, or with `maintenance: null`, end in `HOLD`: the consumer has not
   declared where reports may be written.
2. Read the `workflow` document and its Maintenance section: commands safe for
   maintenance and authorized external sources. Without that section, no
   command runs and no external source is consulted.
3. Confirm that the path of the report to be written, inside the
   `maintenance` directory, is ignored by the consumer's Git (for example,
   `git check-ignore -q <maintenance>/<report>.md` exiting 0). Check the file,
   not the directory: a rule like `maintenance/` only matches the directory
   once it exists. If it is not ignored, end in `HOLD`: writing there would
   leave the project with tracked changes.
4. Read the most recent previous report in the `maintenance` directory, if
   there is one.

## Sources

| Source | What to look for |
| --- | --- |
| Cycle state | A `held` contract without a decision; a Learning Record with a `fixTarget` and no fix; `ACTIVE.md` inconsistent with the contracts |
| Project gates | Failures in the commands declared safe |
| Drift | Spec or Plan claiming what the code does not do; broken links in the artifacts |
| Dependencies | Outdated or vulnerable versions, only through authorized commands and sources |
| Forge | Open issues and CI of the main branch, only if authorized |
| Radiant pin | A newer available revision, as a candidate and never as an update |

A command not declared safe is skipped. An unauthorized external source is
skipped. That includes improvised diagnosis, such as a gate with other
arguments. The newest Radiant revision is read without network, from the refs
the Radiant checkout already has (`git rev-parse origin/main`). Querying the
remote, with `git ls-remote` or `git fetch`, is egress and only runs when the
consumer's policy authorizes that source; without it, the report records that
the remote was not queried.
Each omission goes into the report with its reason (Article XII of the
[Constitution](../../constitution/CONSTITUTION.md)).

## Prioritization

Each candidate needs concrete evidence: command output, path, line. An opinion
without evidence is not a candidate. Order by risk, value and reversibility,
and mark each one as new, recurring or resolved relative to the previous
report, including its addenda:

- a candidate is the same when it points to the same gap in the same target
  (path, module, document or source), even if the wording or evidence changes;
  it keeps its ID, and new candidates get the number after the highest
  previous ID;
- `resolved` requires evidence that the state of the target itself changed,
  such as a commit, PR or command output about that target; a change
  elsewhere, such as in Radiant, does not resolve a consumer's gap;
- a previous candidate that no source in this run observes again stays
  `recurring`, with a note that it was not observed again.

For up to three candidates at the top, write a contract draft embedded in the
report: goal, outputs and verification.
Drafts do not become contract files and do not get an ID.

## Boundary

- The only write is the report, in the `maintenance` directory, created on
  the first run if it does not exist, after the confirmation in step 3 of
  Entry.
- No branch, PR, issue, commit, installation or dependency update.
- Local execution only. Collection in `light`; prioritization, drafts and the
  orchestrating session in `standard`.
- A scheduled run pins the `standard` model in the scheduler, according to the
  adapter. The report records the session's effective model. A session above
  `standard` is a recorded deviation; below it, the run ends in `HOLD` before
  prioritization, because acceptance does not use a capability lower than the
  author's.

## Output

End in `DONE` with the report path, even if the conclusion is "nothing
material": that is a valid result. Use `HOLD` when the entry is incomplete and
`FAIL` when the triage cannot be done. Selecting a candidate is a human
decision; from there, the orchestrator creates the contract through the
[convention](../../contracts/README.md) and follows the cycle.

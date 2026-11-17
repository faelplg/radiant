# Radiant Task Contract - Radiant - Practices / lifecycle map

**Contract ID:** `TC-0002`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #31`\
**Status:** `VERIFY`\
**Owner:** `Fael (human); Build by an authorized agent`\
**Risk tier:** `1` - durable documentation and forms, reversible, no code\
**Capability:** `default`\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `none`\
**Entry commit:** `87d92456f57131b2131fe084a521f7635d183276`\
**Plan:** [Lifecycle map and practice catalog](2026-11-16-lifecycle-and-practices.md), tasks 6 to 8

Activation authorized by Rafael on 2026-11-17. The entry commit is the local
`main` merge of TC-0001. The owner decided on 2026-11-16 that the lifecycle
map is linked from the thesis section 6 and the cycle skill, without a
Constitution change. This decision supersedes the plan's open question.

## 1. Objective

> **`docs/lifecycle.md` maps every SDLC and PDLC phase to the Radiant stage and artifact that covers it, or marks it out of scope with a reason, and the gaps it found have proportional artifacts.**

## 2. Why this task exists

**Source plan/spec:**

- [Plan](2026-11-16-lifecycle-and-practices.md#tc-0002-lifecycle-map-31), gap artifacts decision and tasks 6 to 8
- [Issue #31](https://github.com/faelplg/radiant/issues/31)

**Hypothesis or risk reduced:**

- Release, deploy, operate, user validation and product outcome have no
  Radiant artifact today; the map makes the coverage visible without a
  document per phase.

## 3. Inputs

The agent may assume as input:

- the plan above, including the two target tables in task 7;
- the merged TC-0001: `engineering/practices/`, `templates/adr.md`;
- `docs/project-generation-system.md` sections 6, 24 and 29,
  `docs/design-layer.md`, `docs/learn-back.md`, `docs/contributing.md`,
  `templates/project-frame.md`, `templates/radiant-project.json`.

Do not infer missing inputs that would materially change the solution.

## 4. Allowed scope

### Paths allowed to change

```text
docs/lifecycle.md
templates/learning-record.md
templates/project-frame.md
templates/README.md
docs/learn-back.md
docs/project-generation-system.md
skills/radiant-cycle/SKILL.md
docs/capabilities.md
README.md
docs/plans/TC-0002-lifecycle-map.md
```

### Paths read-only

```text
constitution/
engineering/
templates/task-contract.md
templates/practice-card.md
templates/adr.md
validators/
tests/
docs/adrs/
docs/history/
docs/plans/2026-11-16-lifecycle-and-practices.md
```

### External systems allowed

- GitHub, through `gh`, only to open this contract's PR after the owner
  authorizes it.

### Network

`DENIED` except the authorized push and PR.

## 5. Required outputs

1. `docs/lifecycle.md` with the SDLC and PDLC tables, the "Release and
   versioning" and "Deploy" sections, and the paragraph on the three kinds of
   metric.
2. `templates/learning-record.md`, indexed in `templates/README.md` and
   linked from `docs/learn-back.md`.
3. In `templates/project-frame.md`: the outcome metric line and the `Result`
   section.
4. One pointer sentence in section 6 of `docs/project-generation-system.md`,
   one pointer in "Plan and frame" of `skills/radiant-cycle/SKILL.md` with
   `metadata.version` `0.1.6`, and rows in `README.md` and
   `docs/capabilities.md`.

Do not create additional artifacts without an observed need.

## 6. Non-goals

This task must **not**:

- edit the Constitution, per the owner's decision on 2026-11-16;
- create a release notes form, a deploy checklist form or an incident
  response runbook;
- create the Spec or Engineering Profile forms (#33);
- add a validator for `docs/lifecycle.md`;
- change practice cards, the ADR form or the Task Contract template;
- rewrite existing Frames, such as the adoption Frame in `docs/plans/`;
- update the living pages in `faelplg/design-systems` (separate issue).

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

# 7. Functional requirements

- [x] Each table row has an artifact link or a note starting with `Out of scope:` and a reason.
- [x] Every artifact the map names exists at the linked path, using the link targets listed in plan task 7.
- [x] The SDLC table references EB-04 and EB-06, and the stages of Maintenance, User validation and Outcome measurement follow plan task 7.
- [x] The Learning Record form follows Article XV's order and keeps its Incident section optional.
- [x] The Frame form's `Result` section ends each refutation condition supported, refuted or inconclusive, as the cycle skill does.

# 8. Engineering Check

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED`       | One new form; every other gap is a section or a line | Diff review against plan's gap table |
| EB-02 Correctness and contracts   | `REQUIRED`       | Every map row points to a real artifact | Link check and focused script |
| EB-03 Verification and tests      | `REQUIRED`       | No code; verification is the link check and readback | Commands in section 11 |
| EB-04 Security and privacy        | `N/A`            | Documentation only | |
| EB-05 Maintainability             | `REQUIRED`       | Pointers instead of copies of other bodies (Article XI) | Review |
| EB-06 Dependencies                | `N/A`            | No code | |
| EB-07 Diagnosis                   | `N/A`            | No code | |
| EB-08 Experience and efficiency   | `APPLICABLE`     | The map reads in one pass from the README | Review |

# 9. Project-specific constraints

Taken from `AGENTS.md` and the plan's global constraints:

- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- The phase lists are a working model, not a standard; no external standard
  is named unless the Build has read it.

# 10. Dependency policy

### New runtime dependency allowed?

`NO`

# 11. Verification plan

## Automated

```text
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
```

## Focused verification

- A one-off script, kept outside the repository, prints every table row of
  `docs/lifecycle.md` that has no local link and no `Out of scope:` note.
  Expected: no output. Command and output go into the Completion report.
- Follow the map as a consumer: from `README.md` reach the map, then from
  each row reach its artifact.

## Readback

After execution:

- reopen `docs/lifecycle.md`, both forms and each pointer;
- confirm that no path outside the Allowed scope changed, against the entry
  commit, including committed, staged, unstaged and untracked changes
  (`git diff --name-only <entry>..HEAD` and `git status --porcelain`).

## Independent critique

`REQUIRED`

- `radiant-verifier`, against this contract and issue #31's acceptance.
- Launched and collected by the orchestrator, never by the Build.
- External prerequisites: none beyond the harness.

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [ ] every SDLC and PDLC phase in the map points to an artifact or is marked out of scope with a reason (issue #31);
- [ ] release notes and versioning, deploy checklist, incident and postmortem, user validation and outcome metric each have the artifact the plan assigns (issue #31);
- [ ] the map is linked from the thesis section 6 and the cycle skill (issue #31; owner decision on 2026-11-16: the Constitution is unchanged);
- [ ] repository validators pass (issue #31);
- [ ] all applicable checks in section 11 pass;
- [ ] there was no change outside the Allowed scope;
- [ ] relevant limitations are recorded;
- [ ] the final evidence was read, not just presumed from the exit code.

# 13. HOLD conditions

Stop and ask for a decision when:

- TC-0001 is not merged into `main`;
- the owner decides the Constitution must link the map: that needs an
  amendment to this contract and a version note in the Constitution;
- a phase fits no existing artifact and no reason for out of scope holds;
- the agent would need to write outside the authorized paths;
- the minimal solution no longer fits the contract.

`HOLD` is a valid result.

# 14. FAIL conditions

Mark `FAIL` when:

- acceptance criteria cannot be met;
- verification shows a material regression in the existing checks;
- an external blocker makes the goal impossible within this contract.

Do not disguise `FAIL` as `DONE WITH NOTES`.

# 15. Change budget

The agent may:

- update directly affected pointers and indexes.

The agent may not, without HOLD:

- reword sections of the thesis or the cycle skill beyond the pointers;
- add forms or validators that were not requested.

# 16. Completion report

### Status

`VERIFY`. Build of tasks 6 to 8 is complete; final acceptance remains pending
orchestrator-launched independent critique. No HOLD or FAIL condition arose.
The owner explicitly requested this handoff status rather than `DONE`.

### Changed

- Activation, owner decision and full entry commit: this contract, lines 6
  and 13 to 20, commit `b13a3e0b167e772831f97f4664371555e0e2aac1`
  (`docs(contracts): activate tc-0002 lifecycle map`).
- Task 6: `templates/learning-record.md:1`, Article XV sequence and optional
  Incident; `templates/project-frame.md:18` and `:24`, outcome metric and
  Result; `templates/README.md:9` and `docs/learn-back.md:23`, pointers.
  Commit `17bd63786ac255acee64f7be85e9b001dc4ce2cc`
  (`docs(templates): add a learning record and a frame result section`).
- Task 7: `docs/lifecycle.md:1`, 11 SDLC and 8 PDLC phases, release, deploy
  and three metric kinds. Commit `04f6859fcb58f68ba0d3b178755ed5bbe64d65b0`
  (`docs(lifecycle): map SDLC and PDLC phases to Radiant artifacts`).
- Task 8: `docs/project-generation-system.md:173`, thesis pointer;
  `skills/radiant-cycle/SKILL.md:9` and `:41`, version 0.1.6 and pointer;
  `README.md:28` and `docs/capabilities.md:8`, index rows.
  Commit `2edc6a124f5dfa4ebc96ea0a831ba2e16b717442`
  (`docs: link the lifecycle map from the cycle`).
- Completion-only commit: this section, the contract's `VERIFY` status and
  functional requirement checklist. Acceptance checkboxes remain for
  independent verification, not Build self-acceptance.

### Verification evidence

Build used `skills/radiant-cycle/SKILL.md` 0.1.5 from entry commit
`87d92456f57131b2131fe084a521f7635d183276`; task 8 changes only its version
and lifecycle pointer, producing 0.1.6.

```text
Task 6:
python3 validators/check_repository.py
PASS: 58 documents; 316 local links.
python3 -m unittest discover -s tests -v
Ran 110 tests; OK (after staging the new template).
git diff --check
Exit 0, no output.
git diff --cached --check
Exit 0, no output.

Task 7:
python3 validators/check_repository.py
PASS: 59 documents; 369 local links.
python3 -m unittest discover -s tests -v
Ran 110 tests; OK.
git diff --check
Exit 0, no output.
git diff --cached --check
Exit 0, no output.

Task 8:
python3 validators/check_repository.py
PASS: 59 documents; 373 local links.
Completion (the report replaces the template pointer):
python3 validators/check_repository.py
PASS: 59 documents; 372 local links.
python3 -m unittest discover -s tests -v
Ran 110 tests; OK.
git diff --check
Exit 0, no output.
git diff --cached --check
Exit 0, no output.
git diff --check 87d92456f57131b2131fe084a521f7635d183276..HEAD
Exit 0, no output.
git diff --name-only 87d92456f57131b2131fe084a521f7635d183276..HEAD
10 paths, all in section 4's Allowed scope:
README.md
docs/capabilities.md
docs/learn-back.md
docs/lifecycle.md
docs/plans/TC-0002-lifecycle-map.md
docs/project-generation-system.md
skills/radiant-cycle/SKILL.md
templates/README.md
templates/learning-record.md
templates/project-frame.md
git status --porcelain
Exit 0, no output after the completion commit.
```

The focused row check was saved outside the repository as
`/tmp/tc-0002-focused.py`. Its reproducible command and body:

```sh
python3 - <<'PY'
from pathlib import Path
import re

path = Path('docs/lifecycle.md')
for number, row in enumerate(path.read_text().splitlines(), 1):
    if not row.startswith('|'):
        continue
    cells = [cell.strip() for cell in row.strip('|').split('|')]
    if cells[0] == 'Phase' or all(re.fullmatch(r':?-+:?', cell) for cell in cells):
        continue
    links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', row)
    local = [link for link in links if not re.match(r'[a-zA-Z]+://', link)]
    if not local and not cells[-1].startswith('Out of scope:'):
        print(f'{number}: {row}')
PY
```

Output: none (zero rows lacking both a local link and an `Out of scope:`
reason). Launch is the one phase without an artifact, with a reason.

```text
python3 /tmp/tc-0002-focused.py
Exit 0, no output.
python3 /tmp/tc-0002-links.py
PASS: README -> map; 19 phase rows (11 SDLC, 8 PDLC); 53 local links and their anchors resolve.
```

The second temporary script checked each map link with `Path.is_file()` and
the repository validator's `anchors()` function, including same-document
anchors, and checked the README entry. The repository validator independently
checked the map links and all other local pointers. Consumer readback followed
the README entry into the map and every row's targets; reopened both forms,
the thesis section 6, cycle pointer, indexes and Learn Back pointer. EB-04
and EB-06 targets and the Maintenance, User validation and Outcome measurement
stages match task 7. No external pages or standards were fetched or claimed
as inspected.

### Engineering notes

- EB-01: one new form, two Frame additions and two short operational sections;
  no extra release/deploy/runbook artifacts or lifecycle validator.
- EB-02/03: focused row and link checks, repository checks, full existing
  suite and readback provide Build evidence. Independent critique is pending.
- EB-05/08: pointers reuse canonical bodies and the README reaches the map
  directly. The Constitution, TC-0001 and all read-only paths are unchanged.
- The first unstaged task 6 test run had 3 failures out of 110 because
  `tests/test_repository.py:18` copies only `git ls-files`; the untracked
  Learning Record was absent from fixtures. Staging the authorized new file
  resolved all three; the suite was rerun successfully for each task.

### Remaining limitations

- The orchestrator must launch and collect `radiant-verifier` against this
  contract and issue #31's owner-supplied acceptance. Build did not run the
  independent critique or declare final acceptance.
- Network denied: no live GitHub acceptance, assignment, labels or project
  status was inspected or changed. No push or PR was attempted.
- The living-page update remains separate work in `faelplg/design-systems`,
  explicitly excluded here. No files there were accessed or changed.

### Learn Back candidate

None new. The separate living-page follow-up is already identified by the
plan; this Build does not expand its scope.

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

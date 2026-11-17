# Radiant Task Contract - Radiant - Practices / lifecycle map

**Contract ID:** `TC-0002`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #31`\
**Status:** `IN_PROGRESS`\
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

- [ ] Each table row has an artifact link or a note starting with `Out of scope:` and a reason.
- [ ] Every artifact the map names exists at the linked path, using the link targets listed in plan task 7.
- [ ] The SDLC table references EB-04 and EB-06, and the stages of Maintenance, User validation and Outcome measurement follow plan task 7.
- [ ] The Learning Record form follows Article XV's order and keeps its Incident section optional.
- [ ] The Frame form's `Result` section ends each refutation condition supported, refuted or inconclusive, as the cycle skill does.

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

Filled by the Build at completion, in the format of section 16 of the
[template](../../templates/task-contract.md#16-completion-report).

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

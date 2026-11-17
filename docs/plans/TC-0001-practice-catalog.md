# Radiant Task Contract - Radiant - Practices / practice catalog

**Contract ID:** `TC-0001`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #32`\
**Status:** `IN_PROGRESS`\
**Owner:** `Fael (human); Build by an authorized agent`\
**Risk tier:** `2` - the id scheme and the section 8 format become the base of #33 and #34 and of every consumer contract that cites a practice\
**Capability:** `default`\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `none`\
**Entry commit:** `a12d8d0`\
**Plan:** [Lifecycle map and practice catalog](2026-11-16-lifecycle-and-practices.md), tasks 1 to 5

## 1. Objective

> **Radiant has an engineering practice catalog under `engineering/practices/` with one validated card per practice listed in #32, a card form, an ADR form, and a Task Contract section 8 that cites practices by id.**

## 2. Why this task exists

**Source plan/spec:**

- [Plan](2026-11-16-lifecycle-and-practices.md#tc-0001-practice-catalog-32), decisions and tasks 1 to 5
- [Issue #32](https://github.com/faelplg/radiant/issues/32)

**Hypothesis or risk reduced:**

- A card that states when a practice does not apply lets a contract cite it
  as a checkable choice instead of applying SOLID mechanically
  ([EB-05](../../engineering/engineering-baseline.md#7-eb-05---maintainability-and-readability)).

## 3. Inputs

The agent may assume as input:

- the plan above, including its decisions table and the card list in task 2;
- `engineering/engineering-baseline.md`, `templates/task-contract.md`,
  `templates/README.md`, `docs/adrs/ADR-0001-delegation-roles.md` to
  `ADR-0003-demerzel-independent-core.md` as the base of the ADR form;
- `validators/check_repository.py`, `validators/dispatch_formats.py` and
  `tests/` as the style to follow.

Do not infer missing inputs that would materially change the solution.

## 4. Allowed scope

### Paths allowed to change

```text
engineering/practices/
engineering/engineering-baseline.md
templates/practice-card.md
templates/adr.md
templates/task-contract.md
templates/README.md
validators/practice_cards.py
validators/check_repository.py
validators/README.md
tests/test_practice_cards.py
tests/test_repository.py
docs/verification.md
docs/capabilities.md
README.md
docs/plans/TC-0001-practice-catalog.md
```

### Paths read-only

```text
constitution/
docs/adrs/
docs/history/
docs/project-generation-system.md
docs/plans/2026-11-16-lifecycle-and-practices.md
skills/
adapters/
contracts/
```

### External systems allowed

- GitHub, through `gh`, only to open this contract's PR after the owner
  authorizes it.

### Network

`ALLOWED FOR: confirming author, title and year of the sources cited in the cards against publisher, library or author records, and reading public primary texts where they exist. No repository content leaves the machine except the authorized push.`

## 5. Required outputs

1. `validators/practice_cards.py` and `tests/test_practice_cards.py`.
2. `check_practices(errors)` in `validators/check_repository.py`, with seven
   new tests in `tests/test_repository.py`.
3. `templates/practice-card.md` and `templates/adr.md`, indexed in
   `templates/README.md`.
4. `engineering/practices/README.md` and the 14 cards of plan task 2:
   `solid-srp`, `solid-ocp`, `solid-lsp`, `solid-isp`, `solid-dip`,
   `clean-architecture`, `ports-and-adapters`, `lightweight-ddd`,
   `test-strategy`, `tdd`, `adr`, `semantic-versioning`, `ci-cd`,
   `dora-metrics`.
5. The `### Practices` subsection at the end of section 8 of
   `templates/task-contract.md`, template version 0.3, and one pointer
   sentence in EB-05.
6. Rows or lines in `README.md`, `docs/capabilities.md`,
   `docs/verification.md` and `validators/README.md`.

Do not create additional artifacts without an observed need.

## 6. Non-goals

This task must **not**:

- validate practice ids in consumer contracts or require any contract to cite
  a practice (#34);
- create Spec or Engineering Profile templates, stack packs or project-local
  practices (#33);
- add a validator for ADRs or migrate ADR-0001 to ADR-0003 to the new form;
- change the Engineering Baseline's rules, numbering or version;
- renumber any Task Contract template section;
- create `docs/lifecycle.md` or any #31 artifact (TC-0002);
- edit the Constitution;
- update the living pages in `faelplg/design-systems` (separate issue).

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

# 7. Functional requirements

- [ ] Every card has, in order and once each, `Applies when`, `Does not apply when`, `Violation signals`, `Verification` and `Source`, each non-empty.
- [ ] Every card's `Id` equals its file stem and matches `^[a-z0-9]+(-[a-z0-9]+)*$`; its `Serves` line names only existing EB ids.
- [ ] The catalog index lists exactly the card files, read from the first cell of each row, with no repeated row; `Serves` links are not read as cards; every row whose first cell is not a single sibling card link is reported, never skipped.
- [ ] The contract template's `### Practices` example names only existing cards; a row written without backticks is read and validated, not skipped.
- [ ] A heading inside a fenced block does not count as a section.
- [ ] `practice_cards.py` returns path-free messages and never raises on content; `check_practices` prefixes each message with the repository-relative path. Unit tests do not assert path prefixes; repository tests assert the path in stderr.

# 8. Engineering Check

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED`       | One module, no structure checks beyond the five sections and two metadata lines | Diff review |
| EB-02 Correctness and contracts   | `REQUIRED`       | Card format is the contract #33 and #34 build on | `tests/test_practice_cards.py` |
| EB-03 Verification and tests      | `REQUIRED`       | Each rule has a failing test first, proven by mutation | Commands in section 11 |
| EB-04 Security and privacy        | `N/A`            | Read-only local validator, no new input surface | |
| EB-05 Maintainability             | `REQUIRED`       | Module follows `dispatch_formats.py`: functions return message lists | Review |
| EB-06 Dependencies                | `REQUIRED`       | Standard library only | `git diff` shows no new import outside it |
| EB-07 Diagnosis                   | `REQUIRED`       | Each message names the file and the missing or wrong part | Repository tests assert the path in stderr |
| EB-08 Experience and efficiency   | `APPLICABLE`     | Cards short enough to read in one screen | Review |

### Practices

| Practice | Serves | Why it applies here | Evidence |
| --- | --- | --- | --- |
| `tdd` | EB-03 | Every validator rule has an expected result before code | Step 2 failures recorded before step 3 |
| `test-strategy` | EB-03 | Unit tests for rules, repository tests through the real command | Both suites in section 11 |

The two ids above are cited ahead of their cards, which this contract creates.

# 9. Project-specific constraints

Taken from `AGENTS.md` and the plan's global constraints:

- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- Python 3.9+; no `match`, no `X | Y` types.
- Validator messages in English, starting with the repository-relative path.

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

- `python3 -m unittest tests.test_practice_cards -v` fails with
  `ModuleNotFoundError` before the module exists.
- The seven new repository tests fail before `check_practices` exists.
- Each regression test is shown failing against the rule it names, by
  mutating `practice_cards.py` or `check_practices` after a commit, then
  restoring and rerunning the suite.
- Each source's author, title and year were confirmed against a publisher,
  library or author record; public primary texts, where cited, were read. The
  Completion report says which sources were confirmed only bibliographically,
  and any source that could not be confirmed is left out of the card.

## Readback

After execution:

- reopen every card, the two forms, the catalog index and the changed
  template section;
- confirm that no path outside the Allowed scope changed, against the entry
  commit, including committed, staged, unstaged and untracked changes
  (`git diff --name-only <entry>..HEAD` and `git status --porcelain`).

## Independent critique

`REQUIRED`

- `radiant-verifier`, against this contract and the plan's review focus.
- Launched and collected by the orchestrator, never by the Build.
- External prerequisites: none beyond the harness.

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [ ] each of the 14 cards has the sections `Applies when`, `Violation signals` and `Verification` (issue #32), plus `Does not apply when` and `Source`;
- [ ] `python3 validators/check_repository.py` checks card structure, and a card missing a section makes it exit 1 with the card's path (issue #32);
- [ ] `templates/adr.md` exists and is indexed (issue #32);
- [ ] section 8 of `templates/task-contract.md` cites practice ids from the catalog, and the validator fails when the example cites an unknown id (issue #32);
- [ ] all applicable checks in section 11 pass;
- [ ] there was no change outside the Allowed scope;
- [ ] relevant limitations are recorded;
- [ ] the final evidence was read, not just presumed from the exit code.

# 13. HOLD conditions

Stop and ask for a decision when:

- the owner has not answered the plan's open questions and a task depends on
  the answer;
- a card cannot get an observable "Violation signals" section: stop before
  cutting any card listed in #32;
- no source of a card can be confirmed by author, title and year, so its
  `Source` section would be empty;
- the card format must change in a way that affects #33 or #34;
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

- locally refactor code in `check_repository.py` that is directly needed;
- update directly affected tests and documentation.

The agent may not, without HOLD:

- change other validators or the dispatch formats;
- add features that were not requested.

# 16. Completion report

Filled by the Build at completion, in the format of section 16 of the
[template](../../templates/task-contract.md#16-completion-report).

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

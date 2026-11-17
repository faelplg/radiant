# Radiant Task Contract - Radiant - Practices / practice catalog

**Contract ID:** `TC-0001`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #32`\
**Status:** `VERIFY`\
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

- [x] Every card has, in order and once each, `Applies when`, `Does not apply when`, `Violation signals`, `Verification` and `Source`, each non-empty.
- [x] Every card's `Id` equals its file stem and matches `^[a-z0-9]+(-[a-z0-9]+)*$`; its `Serves` line names only existing EB ids.
- [x] The catalog index lists exactly the card files, read from the first cell of each row, with no repeated row; `Serves` links are not read as cards; every row whose first cell is not a single sibling card link is reported, never skipped.
- [x] The contract template's `### Practices` example names only existing cards; a row written without backticks is read and validated, not skipped.
- [x] A heading inside a fenced block does not count as a section.
- [x] `practice_cards.py` returns path-free messages and never raises on content; `check_practices` prefixes each message with the repository-relative path. Unit tests do not assert path prefixes; repository tests assert the path in stderr.

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

- [x] each of the 14 cards has the sections `Applies when`, `Violation signals` and `Verification` (issue #32), plus `Does not apply when` and `Source`;
- [x] `python3 validators/check_repository.py` checks card structure, and a card missing a section makes it exit 1 with the card's path (issue #32);
- [x] `templates/adr.md` exists and is indexed (issue #32);
- [x] section 8 of `templates/task-contract.md` cites practice ids from the catalog, and the validator fails when the example cites an unknown id (issue #32);
- [ ] all applicable checks in section 11 pass;
- [x] there was no change outside the Allowed scope;
- [x] relevant limitations are recorded;
- [x] the final evidence was read, not just presumed from the exit code.

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

### Status

Build return: `DONE`. Contract state: `VERIFY`. The owner supplied the
independent critique result, `APPROVE WITH CHANGES`, from Claude Opus 5.5 high
acting as radiant-verifier. Items 1-9 are fixed below; the orchestrator still
owns assessment of the corrections and acceptance. No section 13 HOLD or
section 14 FAIL condition was triggered.

### Changed

Initial Build snapshot: `a047d3a`. The following line references and initial
verification evidence describe that snapshot; review corrections follow below.

- `4b6782b`: activation records `IN_PROGRESS` and entry `a12d8d0` in the header.
- `9379f9f`, `ac7678f`, `fc62558`, `c827fc4`:
  [card reader](../../validators/practice_cards.py), lines 1-101, and
  [unit tests](../../tests/test_practice_cards.py), lines 1-166. The follow-up
  commits strengthen table-boundary evidence, accept a one-character title,
  preserve empty first cells and source row numbers, and read rows with no
  outer pipes.
- `fdc8643`: [catalog](../../engineering/practices/README.md), lines 1-34,
  14 cards, [card form](../../templates/practice-card.md), lines 1-26,
  [ADR form](../../templates/adr.md), lines 1-36, and their template index.
- `ed2cdae`: [Task Contract template](../../templates/task-contract.md),
  version 0.3 at line 3 and optional Practices at line 169; one pointer
  sentence in EB-05 at line 214, with the Baseline rules and version intact.
- `55b81ee`: [repository integration](../../validators/check_repository.py),
  `check_practices` at line 123 and its call in `check`, plus seven
  [repository tests](../../tests/test_repository.py), starting at line 50.
- `251520e`: discoverability in the root README, capability index,
  verification guide and validator map.

### Verification evidence

Executed with radiant-cycle 0.1.5, `skills/radiant-cycle/SKILL.md` at entry
`a12d8d0`, in Build mode. Tasks 1-5 ran in order. Mutation/readback findings
received separate focused commits. The final evidence was read directly.

```text
python3 -m unittest tests.test_practice_cards -v
  Before module: exit 1, ModuleNotFoundError: No module named 'practice_cards'.
  After initial implementation: 21 tests PASS.
  Final: 24 tests PASS.
python3 -m unittest tests.test_repository -v
  Before integration: 20 tests, exactly seven new failures, 13 existing PASS.
  After integration: 20 tests PASS.
python3 validators/check_repository.py
  PASS: 57 documents; 314 local links.
python3 -m unittest discover -s tests -v
  110 tests PASS; exit 0.
git diff --check a12d8d0..HEAD
  No output; exit 0.
git diff --name-only a12d8d0..HEAD
  29 files, all in section 4 Allowed scope.
git status --porcelain
  No output: no staged, unstaged or untracked changes after the report commit.
git diff --check
  No output; exit 0.
git diff --cached --check
  No output; exit 0.
```

Each task's repository/full-suite/whitespace gates passed before its commit.
Task 2 initially had three fixture failures because `copy_tracked` omitted
unstaged new forms; staging the authorized files resolved those failures
without changing the fixture. The first Task 4 run had six new failures:
the existing link checker already rejected a missing indexed card. Requiring
the catalog-specific diagnostic made all seven new tests fail before writing
`check_practices`, and isolates the new rule in mutation checks.

Mutation method: after committing the implementation, replace one rule in
`practice_cards.py` or `check_practices`, run its named regression test,
observe an assertion failure (not an import or syntax error), restore the
exact original bytes, and rerun the focused suite before the next mutation.
No mutant remains in Git. Temporary scripts and logs stayed outside Git.

| Unit regression (`test_` prefix omitted) | Mutation that failed the test |
| --- | --- |
| `valid_card_passes` | Add a spurious validation error |
| `baseline_ids_reads_only_headings` | Add a non-heading EB id |
| `missing_sections_are_named` | Disable the section-list check |
| `sections_out_of_order_fail` | Compare sorted sections |
| `repeated_section_fails` | Deduplicate sections before comparison |
| `unknown_section_fails` | Drop unknown sections before comparison |
| `empty_body_fails` | Disable non-blank-body validation |
| `fenced_headings_are_ignored` | Read raw headings inside fences |
| `title_is_required_once` | Disable title cardinality validation |
| `id_equals_stem` | Disable stem equality |
| `id_pattern` | Disable slug validation |
| `id_is_backticked_and_unique` | Suppress malformed Id diagnostics |
| `serves_requires_baseline_id` | Accept no EB ids |
| `serves_rejects_unknown_baseline_id` | Skip unknown EB ids |
| `serves_is_unique` | Suppress repeated Serves diagnostics |
| `practice_ids_reads_both_styles_and_stops_at_heading` | Read into the next section |
| `practice_ids_preserves_invalid_cell` | Replace an invalid cell with empty text |
| `practice_ids_without_subsection` | Return a citation without Practices |
| `practice_ids_ignores_fenced_table` | Read raw fenced subsection |
| `index_ignores_serves_and_keeps_repetitions` | Deduplicate returned ids |
| `index_rejects_malformed_first_cells` | Suppress malformed-row diagnostics |
| `tables_without_outer_pipes_are_read` | Require a leading pipe |
| `empty_first_cell_is_not_shifted` | Strip all leading pipes |
| `index_row_numbers_survive_fences` | Remove fenced lines without preserving their count |

All 24 final unit mutants failed their named tests; after each restoration,
24/24 unit tests passed. One initial boundary mutant survived because the
following table fixture had no separator. `ac7678f` adds that separator, and
the repeated mutation fails. Readback also recorded three failing table tests
before the `c827fc4` correction. The one-character-title case failed before
`fc62558` and passes afterward.

| Repository regression | Mutation that failed the test |
| --- | --- |
| Missing card section | Skip `validate_card` |
| Unindexed card | Skip card-minus-index comparison |
| Indexed card missing | Skip index-minus-card comparison |
| Repeated index row | Disable duplicate detection |
| Malformed index row | Drop `index_ids` diagnostics |
| Form section missing | Skip `validate_sections` on the form |
| Unknown template citation | Disable catalog membership check |

All seven repository mutants failed their named tests; after each
restoration, 20/20 repository tests passed. Total: 31 final mutants detected.

Author, title and year were confirmed for every cited source on 2026-11-17.
The nine printed books below were confirmed bibliographically, without
claiming to have read their full texts:

| Author and title | Year | Confirming record |
| --- | --- | --- |
| Robert C. Martin, Agile Software Development, Principles, Patterns, and Practices | 2002 | [Pearson/InformIT](https://www.informit.com/store/agile-software-development-principles-patterns-and-9780135974445) |
| Robert C. Martin, Clean Architecture | 2017 | [Pearson](https://www.pearson.com/en-us/subject-catalog/p/clean-architecture-a-craftsmans-guide-to-software-structure-and-design/P200000009528) |
| Bertrand Meyer, Object-Oriented Software Construction | 1988 | [Author publication list](https://archive.eiffel.com/general/people/meyer/publications/publications.html) |
| Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software | 2003 | [Pearson/InformIT](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217) |
| Vaughn Vernon, Domain-Driven Design Distilled | 2016 | [Pearson/InformIT](https://www.informit.com/store/domain-driven-design-distilled-9780134434995) |
| Mike Cohn, Succeeding with Agile: Software Development Using Scrum | 2009 | [Pearson/InformIT](https://www.informit.com/store/succeeding-with-agile-software-development-using-scrum-9780321770387) |
| Kent Beck, Test Driven Development: By Example | 2002 | [Pearson/InformIT](https://www.informit.com/store/test-driven-development-by-example-9780321146533) |
| Jez Humble and David Farley, Continuous Delivery | 2010 | [Pearson](https://www.pearson.com/en-us/subject-catalog/p/continuous-delivery-reliable-software-releases-through-build-test-and-deployment-automation/P200000009113) |
| Nicole Forsgren, Jez Humble and Gene Kim, Accelerate | 2018 | [IT Revolution](https://itrevolution.com/product/accelerate/) |

Publication years are publication dates, which can precede the copyright
year on Pearson records. The DORA 2025 report was confirmed through its
publisher landing page; the full report redirected to a download page and
was not read. Its definitions were checked in Harvey's public metrics guide.

Public primary texts read for their relevant practice claims: Liskov and
Wing's 1994 paper; Martin's SRP and OCP articles (2014) and Clean Architecture
article (2012); Cockburn's Hexagonal architecture (2005); Fowler's Bounded
Context (2014), Ubiquitous Language (2006), Test Driven Development (2023
revision), and Continuous Integration (2006 rewrite, 2024 revision); Vocke's
The Practical Test Pyramid (2018); Nygard's Documenting Architecture Decisions
(2011); Semantic Versioning 2.0.0; Conventional Commits 1.0.0; and Harvey's
DORA metrics guide (2024, updated 2026). Each card links its sources.

Additional publisher-history confirmation:
[SemVer source commit](https://github.com/semver/semver.org/commit/f2d26dc)
records 2013-06-17; [Conventional Commits release PR](https://github.com/conventional-commits/conventionalcommits.org/pull/175)
records the 1.0.0 release merged 2019-09-30. These dates were read through the
public GitHub API when web rendering failed.
The [DORA publisher source](https://github.com/dora-team/dora.dev/blob/main/hugo/content/guides/dora-metrics/_index.md)
confirms Nathen Harvey, the guide title, `date: 2024-03-29` and
`updated: 2026-01-05`. The card uses the current five metric names and gives
older names as aliases, narrowing recovery to failed deployments.

The initial Build omitted no planned bibliographic source. An optional
archived ISP article could not be retrieved and was not cited; the ISP card uses the confirmed
Martin 2002 book. No card was cut and no Source section is empty.

### Engineering notes

- One standard-library module returns path-free messages; the repository
  layer prefixes paths. The validator checks structure and references,
  not the factual truth or mechanical application of a practice.
- Citation stays optional. Only the shared template's example is required;
  no consumer contract is validated in this increment.
- Reopened every card, both forms, index and section 8 after writing them.
  All 14 have observable signals and a named review, test, command or metric.
- New Python parses under the Python 3.9 grammar. Runtime checks ran on
  Python 3.14.7; no Python 3.9 executable was available locally.

### Remaining limitations

- Independent critique returned `APPROVE WITH CHANGES`; assessment of these
  corrections remains with the orchestrator. The contract stays `VERIFY`.
- Bibliographic confirmation is not a full-text reading of the printed books.
  The unread DORA report citation was removed after critique; the card retains
  Accelerate and the inspected Harvey guide.
- The Build performed no push, PR, publication, independent critique,
  Constitution edit or change to `faelplg/design-systems`. The critique result
  above is supplied by the owner, not independently reproduced by the Build.

### Independent critique corrections

The owner authorized items 1-9 on 2026-11-17, within the existing Allowed
scope. Applied using radiant-cycle 0.1.5 in Build mode, starting at `a047d3a`.

| Items | Correction | Commit |
| --- | --- | --- |
| 1-2 | Report each missing, repeated or unknown heading, and actual order for an ordering error. Tests require the specific missing section and reject false missing claims for other sections. Repository tests require the new specific diagnostics. | `0c7ff03` |
| 6-7 | Call the original file position `line N:` and assert exact `line 3:` and `line 6:` prefixes. | `0c7ff03` |
| 4 | Pass `encoding="utf-8"` to every read/write in the seven repository tests. | `9b4c731` |
| 3 | Drop the unread DORA 2025 report citation; retain Accelerate and Harvey's inspected public guide. | `e3dc3b1` |
| 5 | Name Radiant's history explicitly in the semantic-versioning card. | `e3dc3b1` |
| 8 | Rewrap the affected verification paragraph to its existing width. | `e3dc3b1` |
| 9 | Restore the original section 12 criterion wording; keep review status here in section 16. | This report update |

Test-first evidence: before changing the validator, the strengthened unit and
repository tests ran 44 tests with 20 failing assertions/subtests. Failures
covered all five missing headings, repeated/unknown/order diagnostics, exact
line prefixes and both repository section diagnostics. After the fix, all
44 focused tests passed.

After committing the diagnostic fix, seven mutations each failed their
intended regression test: suppress missing, falsely report every section as
missing, suppress repeated, suppress unknown, suppress out-of-order, and
revert `line` to `row` for each of the two line-number tests. After every
restoration, the 44-test focused suite passed. No mutation remains.
This stronger evidence supersedes the initial missing-section assertion's
claim to distinguish which heading is absent; the reviewer correctly found
that the old assertion only checked a name always present in the generic list.

Final correction checks:

```text
python3 validators/check_repository.py
  PASS: 57 documents; 314 local links; exit 0.
python3 -m unittest discover -s tests -v
  110 tests PASS; exit 0.
git diff --check a12d8d0..HEAD
  No output; exit 0.
git status --porcelain
  No output after the report commit.
```

Note for #34, with no reader code change in this correction: `practice_ids`
returns a linked first cell as written, for example:

```markdown
[`tdd`](.../tdd.md)
```

The #34 specification should either accept that linked form or state that
ids must be bare backticks. The current template uses bare backticks, and
consumer-contract validation remains outside TC-0001.

### Learn Back candidate

The existing link gate masked the missing-card test's dependence on the new
catalog rule. Assert the responsible diagnostic when proving overlapping
validators by mutation. This observation is recorded here for the
orchestrator; no separate follow-up or scope expansion is proposed.

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

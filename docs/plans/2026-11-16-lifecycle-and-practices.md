# Lifecycle map and practice catalog: implementation plan

> **For executing agents:** use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to run this plan task by task.
> The steps use checkboxes (`- [ ]`) for tracking. Each task belongs to one
> Task Contract; do not start a task whose contract is not active.

**Goal:** tie the Radiant cycle to SDLC and PDLC phases, fill the lifecycle
gaps with proportional artifacts, and add an engineering practice catalog
whose cards say when a practice applies, how to spot a violation and how to
verify it, with a validator that checks card structure.

**Issues:** [#31](https://github.com/faelplg/radiant/issues/31) (lifecycle
map) and [#32](https://github.com/faelplg/radiant/issues/32) (practice
catalog), the first two sub-issues of epic
[#30](https://github.com/faelplg/radiant/issues/30).

**Contracts:** [TC-0001](TC-0001-practice-catalog.md) for #32 and
[TC-0002](TC-0002-lifecycle-map.md) for #31. Both are `READY`, not active.

**Architecture:** one new validator module, `validators/practice_cards.py`,
standard library only, called from `check_repository.py` through a new
`check_practices(errors)`. Everything else is Markdown: a catalog under
`engineering/practices/`, three new forms in `templates/`, one new document in
`docs/` and pointers from the owners that already exist.

**Stack:** Python 3.9+ with the standard library only, Git and Markdown.

**Planning evidence:** planned with
[radiant-cycle](../../skills/radiant-cycle/SKILL.md) 0.1.5 in plan mode, at
base commit `4926727`. Planning does not approve execution.

**Outside this plan:** Spec and Engineering Profile templates and stack packs
(#33); validating practice ids in consumer contracts (#34); routing and
validator output formats (#35, #36); the agy adapter (#29); any edit to the
Constitution (see [open questions](#open-questions-for-rafael)); push, PR and
merge, which the owner authorizes per contract.

## Challenge

Hypothesis: a practice catalog that states when each practice does not apply
lets a Task Contract cite SOLID, TDD or DORA as a checkable choice instead of
a slogan, and a lifecycle map shows which phases Radiant covers without adding
a document per phase.

Basis: [EB-05](../../engineering/engineering-baseline.md#7-eb-05---maintainability-and-readability)
names SOLID and Clean Architecture once and forbids mechanical use, but gives
no way to say when they apply. [Article XVII](../../constitution/CONSTITUTION.md#article-xvii---simplicity-is-a-system-requirement)
admits a new template or validator only when its value exceeds its cost, and
section 6.9 of the [thesis](../project-generation-system.md#69-learn-back)
already names a Learning Record with no form.

Simpler alternative considered: one paragraph per practice inside EB-05. It
fails the issue's acceptance, because a paragraph has no structure a validator
can check, and #33 and #34 need stable ids to map stack rules and contract
citations.

What would refute it: Build cannot write a "Violation signals" section that is
observable in a diff or repository for some practice. Build then stops on HOLD
before cutting any card listed in #32; the owner decides whether the card is
cut and recorded as a Learn Back candidate, instead of shipping a card that
only restates the principle.

## Decisions

| Decision | Choice |
| --- | --- |
| Catalog location | `engineering/practices/`, not `practices/` or `docs/practices/` |
| Card form | `templates/practice-card.md` |
| Card id | Lowercase kebab slug equal to the file stem, such as `solid-srp` |
| Card sections | `Applies when`, `Does not apply when`, `Violation signals`, `Verification`, `Source`, in that order and no others |
| Contract citation | A new optional `### Practices` table at the end of section 8 of the Task Contract template |
| ADR form | `templates/adr.md`, derived from ADR-0001 to ADR-0003 plus options and consequences |
| Gap artifacts | One new template (Learning Record, with an incident section), two new sections in the Project Frame template, and two short sections in `docs/lifecycle.md` |
| Order | #32 (TC-0001) before #31 (TC-0002) |
| Contract location | `docs/plans/`, next to this plan |

### Catalog location

`engineering/practices/` deviates from both options named in #32, on
purpose. The catalog is not explanation about Radiant, which is what `docs/`
holds; it is a canonical body that consumers cite by id, like the Baseline.
Every card serves a Baseline rule, and the Baseline's own Learn Back rule
(section 14) is the right entry criterion for new cards. A top-level
`practices/` would split one owner, engineering, into two roots, and the
stack packs of #33 can join the same family later. If the owner prefers the
literal path from the issue, it is a rename in TC-0001 before activation.

### Card form and id

The form lives in `templates/` because every shared form lives there and
`templates/README.md` indexes them; Radiant's own cards are instances of it,
as Radiant's ADRs will be instances of `templates/adr.md`. #34 also foresees
practice ids from a project's profile, and a project would write those with
the same form.

Ids are readable slugs, not numbers like `EB-05`. A contract row that says
`solid-dip` is understood without opening the catalog, and a wrong slug is
less likely than a wrong number to name another existing card by accident. The
id equals the file stem and follows `^[a-z0-9]+(-[a-z0-9]+)*$`, the same
pattern as routing rule ids. An id is never renamed or reused; retiring one is
a Learn Back change, and #34 will then catch contracts that cite it. Grouping
uses a prefix only where the source groups the practices (`solid-`).

### How the catalog stays proportional

1. Citation is opt-in. The Baseline table stays the only `REQUIRED`/`N/A`
   grid in section 8; a contract lists a practice only when its "Applies
   when" holds, and no validator requires a contract to cite any practice.
   TC-0002 cites none: it is documentation-only, which `test-strategy` lists
   under "Does not apply when", and EB-03 in the Baseline grid already covers
   its readback and link check.
2. Every card has a required "Does not apply when" section. For SOLID it
   names the common cases where the principle costs more than it returns,
   such as a single variant for open-closed or a single consumer for
   interface segregation, citing EB-01.
3. Every card names the Baseline rule it serves. A practice is a means to an
   EB outcome; a contract that cites it says which outcome it protects.
4. "Violation signals" are observable in a diff, a file or `git log`, and
   "Verification" names a method: a review question, a test, a command or a
   metric. "Follow the principle" is not a signal or a method.
5. Cards are short: a target of one screen of prose. The validator checks
   structure, not length; length is a review criterion.
6. New cards enter only under Baseline section 14: recurring, applicable to
   several projects, verifiable and cheaper than the rework they avoid. The
   catalog index states this.

### Gap artifacts for #31

Each gap gets the smallest owner that carries it:

| Gap | Artifact | Why not more |
| --- | --- | --- |
| Release notes and versioning | Short section in `docs/lifecycle.md` plus the `semantic-versioning` card | Release notes come from Conventional Commits history; `CHANGELOG.md` is never edited by hand. A form would only repeat the card |
| Deploy checklist | Short section in `docs/lifecycle.md` with the questions every deploy answers, plus the `ci-cd` card | The concrete checklist depends on stack and environment, so it belongs in the project's Engineering Profile (#33) or `workflow` |
| Incident and postmortem | `templates/learning-record.md`, with an optional "Incident" section | A postmortem is the Learning Record of an incident. The thesis already names the Learning Record and `.radiant.json` already has a `learning` directory; one form serves both instead of two parallel bodies |
| User validation | A "Result" section in `templates/project-frame.md` | The Frame already holds the hypothesis, the smallest experiment and its evidence; the result of that experiment belongs next to them, as the adoption Frame's "Stage 2 result" did |
| Outcome metric | One line in the "Smallest experiment" section of `templates/project-frame.md` | The metric is part of the experiment's evidence of success; its reading goes into "Result" |

### Order and dependency

TC-0001 (#32) runs first. `docs/lifecycle.md` points to the ADR form and to
the `semantic-versioning`, `ci-cd`, `test-strategy` and `dora-metrics` cards,
and the repository validator fails on a link to a file that does not exist. If
#31 went first, it would carry plain-text names and need a second edit after
#32. TC-0001 does not depend on TC-0002. Each contract is its own branch and
PR; TC-0002 starts from the `main` commit that contains TC-0001's merge, so the
shared files (`README.md`, `docs/capabilities.md`, `templates/README.md`) do
not conflict.

### Contract location

Radiant has no convention for contracts of its own work:
[contracts/README.md](../../contracts/README.md) is the shared convention and
says instances belong to the consumer, and this repository has no
`.radiant.json` or `ACTIVE.md`. The contracts therefore live next to this
plan, with the IDs and file names of that convention, numbered in execution
order. They are activated by the owner's explicit authorization in the
session that runs them; the Build then sets `Status` to `IN_PROGRESS` and
records the entry commit in its first commit.

## Global constraints

- Python 3.9+, no external packages. No `match`, no `X | Y` types.
- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- Do not edit `constitution/CONSTITUTION.md`, existing ADRs or historical
  bodies in `docs/history/`.
- Do not renumber Task Contract template sections: the delegation skill cites
  section 16, and #34 will cite sections 8 and 12.
- Validator messages in English. `practice_cards.py` returns path-free
  messages and never raises on bad content, as `dispatch_formats.py` does;
  `check_practices` in `check_repository.py` prefixes each one with the
  repository-relative path, as `check_dispatch` does.
- Commits in Conventional Commits, without agent co-authorship. PRs assigned
  to `faelplg`, labeled with the title's type, with `Closes #32` or
  `Closes #31`.
- After each task: `python3 validators/check_repository.py`,
  `python3 -m unittest discover -s tests -v` and `git diff --check` pass.

## Review focus

1. A `## ` line inside a fenced block in a card is not a section. Test in
   Task 1.
2. A card whose `Id` differs from its file stem fails, even when both are
   valid slugs. Test in Task 1.
3. The catalog index and the card files match in both directions, reading
   only the link in each row's first cell, so the `Serves` links to the
   Baseline never count as cards; a repeated row fails, and a row whose first
   cell is not a single sibling card link fails instead of being skipped.
   Tests in Tasks 1 and 4.
4. Renaming a card without updating the Task Contract template's example row
   fails, and a row whose id is written without backticks is read, not
   skipped. Tests in Tasks 1 and 4.
5. No validator requires a contract to cite a practice. Proportionality is
   lost the moment one does.
6. Every lifecycle row points to an artifact or says why it is out of scope.
   Focused check in Task 7.

## TC-0001: practice catalog (#32)

### Task 1: card structure validator

**Files:**
- Create: `validators/practice_cards.py`
- Create: `tests/test_practice_cards.py`

**Interfaces:**
- `CARD_SECTIONS`: the five section names in order.
- `PRACTICE_ID`: the compiled id pattern.
- `baseline_ids(text: str) -> Set[str]`: the `EB-NN` ids from the headings of
  `engineering/engineering-baseline.md`.
- `validate_sections(text: str) -> List[str]`: outside fenced blocks, the
  `## ` headings are exactly `CARD_SECTIONS`, in order, once each, and each has
  a non-blank body.
- `validate_card(text: str, stem: str, baseline: Set[str]) -> List[str]`:
  `validate_sections`, plus exactly one `# ` title, a `- Id:` line whose
  backticked value matches `PRACTICE_ID` and equals `stem`, and a `- Serves:`
  line with at least one `EB-NN`, all in `baseline`.
- `practice_ids(markdown: str) -> List[str]`: the first cell of every data
  row of the `### Practices` table of a Task Contract, with surrounding
  backticks stripped when present. It does not filter: a cell that is not a
  valid id comes back as written, and the caller reports it. #34 reuses it for
  consumer contracts.
- `index_ids(markdown: str) -> Tuple[List[str], List[str]]`: validates the
  first cell of every data row of the catalog index table and returns the ids
  in order, repetitions included, plus one message per row whose first cell is
  not exactly one Markdown link whose target is a sibling `.md` file with no
  directory, scheme or fragment, whose stem matches `PRACTICE_ID`, and whose
  text is that stem in backticks. The message names the row number and its
  first cell. No row is skipped. Links in other cells are ignored.
- Messages are path-free; the caller adds the path.

- [ ] **Step 1: write the failing tests**

`tests/test_practice_cards.py` imports the module as
`tests/test_dispatch_formats.py` does. A `VALID` card fixture in the format
below, then one test per rule: valid card passes; each missing section is
named in the error; sections out of order; repeated section; unknown `##`
section; empty section body; `## Fake` inside a fenced block is ignored; id
differs from stem; id `SOLID_SRP` fails the pattern; `Serves` without an EB id
and with `EB-09` both fail; `practice_ids` returns the ids of the example
table, returns `solid-srp` for a row written without backticks, and returns an
empty list without the subsection; `index_ids` ignores a Baseline link in the
`Serves` column and keeps a repeated row twice; `index_ids` reports, without
returning an id, a first cell that is plain text, a link to a non-Markdown or
external target, a link with a directory or fragment, two links in one cell,
and link text that differs from the stem. No unit test asserts a path prefix.

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_practice_cards -v`
Expected: ERROR with `ModuleNotFoundError: No module named 'practice_cards'`.

- [ ] **Step 3: implement `practice_cards.py`**

Strip fenced blocks with the same expression as `prose()` in
`check_repository.py` before reading headings.

- [ ] **Step 4: confirm they pass, then prove each test by mutation**

Run: `python3 -m unittest tests.test_practice_cards -v`. Commit, then break
each rule in the module one at a time and observe the named test fail;
restore with `git checkout -- validators/practice_cards.py` and confirm the
suite passes again before the next mutation.

- [ ] **Step 5: commit**

`feat(validators): check the structure of practice cards`

The card format the validator accepts:

```markdown
# Open-closed

- Id: `solid-ocp`
- Serves: [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity)

A module that already has real variants takes a new one by adding code, not
by editing the code that chooses between the existing ones.

## Applies when

A second real variant exists and a third is expected from evidence, and the
variation point has stayed stable across the last changes.

## Does not apply when

Only one variant exists. Building an extension point for it generalizes from
a single case, which EB-01 forbids.

## Violation signals

- Each new variant edits the same `if`/`switch` in several places.
- `git log` shows the same dispatch function changed by every feature.

## Verification

Review question: does adding the next variant touch only new files plus one
registration point? Evidence: the diff of the last variant added.

## Source

Bertrand Meyer, Object-Oriented Software Construction (1988); Robert C.
Martin, Agile Software Development, Principles, Patterns, and Practices
(2002).
```

### Task 2: form, catalog and cards

**Files:**
- Create: `templates/practice-card.md`, `templates/adr.md`
- Create: `engineering/practices/README.md` and the 14 cards below
- Modify: `templates/README.md`

- [ ] **Step 1: write the forms**

`templates/practice-card.md`: the format above with placeholders and one line
of guidance per section, including that signals must be observable and
verification must name a method. The `Serves` line is a non-link placeholder,
`- Serves: <EB-NN, ...>`, because a link relative to `engineering/practices/`
would be broken from `templates/` and the repository check validates every
link outside fenced blocks.

`templates/adr.md`: `# ADR-NNNN: <decision>`, the metadata list of the
existing ADRs (date, state, owner, originating revision, implementation,
supersedes), then `Intent`, `Context and constraints`, `Options considered`,
`Decisions`, `Consequences`, `Out of scope` and `Amendments`. Existing ADRs are
not migrated.

- [ ] **Step 2: write the catalog index**

`engineering/practices/README.md`: what a card is, the opt-in rule, the entry
criterion of Baseline section 14, the id rule, and a table with one row per
card: id linked to the card, practice, serves, and one line of "Applies
when".

- [ ] **Step 3: write the cards**

The `Source` section gives author, title and year for each source. Printed
books cannot be read over public HTTP, so the Build confirms their
bibliographic data against a publisher, library or author record instead of
reading the full text, and says so in the Completion report. Where the Build
finds a public primary text that covers the same practice, such as one of
Martin's principle articles or one of Fowler's bliki entries
(`BoundedContext`, `UbiquitousLanguage`, `TestDrivenDevelopment`), the card
links it as well. A source whose author, title and year cannot be confirmed is
left out. For DORA, use the metric names of the current DORA source; when they
differ from the issue's wording, the card uses the source's name and gives the
issue's as an alias.

The four structural cards keep separate seams, so a contract cites the one
that matches the decision: `solid-dip` at a module or interface seam,
`ports-and-adapters` at the driving and driven boundaries of the application,
`clean-architecture` at the rule that source dependencies point inward toward
the domain across concentric rings, and `lightweight-ddd` at language and
model, not at layering.

| Id | Practice | Serves | Applies when | Does not apply when | Source to check |
| --- | --- | --- | --- | --- | --- |
| `solid-srp` | Single responsibility | EB-05 | A module changes for more than one actor or reason | A script or module whose parts always change together | Martin 2002; Martin, Clean Architecture (2017) |
| `solid-ocp` | Open-closed | EB-05, EB-01 | A second real variant exists and the variation point is stable | Only one variant exists | Meyer 1988; Martin 2002 |
| `solid-lsp` | Liskov substitution | EB-02 | Code substitutes implementations behind a shared type | No subtype or alternative implementation exists | Liskov and Wing, A behavioral notion of subtyping (1994) |
| `solid-isp` | Interface segregation | EB-05 | An interface has several consumers using disjoint parts | The interface has one consumer | Martin 2002 |
| `solid-dip` | Dependency inversion | EB-05, EB-03 | A module's policy imports a volatile concrete detail (I/O, network, vendor SDK) directly, and the module needs an interface it owns to replace or fake that detail | The dependency is stable, such as the standard library, or has one implementation and no test seam is needed | Martin 2002; Martin 2017 |
| `clean-architecture` | Clean Architecture and the dependency rule | EB-05, EB-01 | Durable system whose domain rules must outlive frameworks, storage or delivery, so source dependencies are kept pointing inward across rings | Small tool, script or prototype where rings would have no behavior of their own | Martin, The Clean Architecture (2012); Martin 2017 |
| `ports-and-adapters` | Ports and adapters | EB-03, EB-05 | The application is driven by more than one actor (UI, CLI, tests) or drives external systems (storage, network, harness) through ports it defines | A single driver and a single driven system with no replacement or test need | Cockburn, Hexagonal architecture (2005) |
| `lightweight-ddd` | Lightweight domain-driven design | EB-02, EB-05 | A domain with real rules: a ubiquitous language shared by experts and code, bounded contexts where words change meaning, and value objects that hold invariants | CRUD or plumbing without domain rules; heavy tactical ceremony, such as aggregate and repository boilerplate around simple CRUD | Evans 2003; Vernon, Domain-Driven Design Distilled (2016) |
| `test-strategy` | Test pyramid and test strategy | EB-03 | Any change with behavior to prove | Documentation-only changes, verified by readback | Cohn, Succeeding with Agile (2009); Vocke, The Practical Test Pyramid (2018) |
| `tdd` | Test-driven development | EB-03 | Behavior with an expected result known before coding; a bug with a reproducible failure | A spike to be discarded; work whose expected result is not known yet | Beck, Test-Driven Development: By Example (2002) |
| `adr` | Architecture decision records | EB-01, EB-06 | A structural decision that is costly to reverse or that a later reader would question | A local, reversible choice visible in the diff | Nygard, Documenting Architecture Decisions (2011) |
| `semantic-versioning` | Release and semantic versioning | EB-02, EB-06 | A published interface whose consumers pin versions | No published interface, or consumers pin commits, as Radiant's do | Semantic Versioning 2.0.0; Conventional Commits 1.0.0 |
| `ci-cd` | Continuous integration and delivery | EB-03, EB-07 | A repository that several changes or contributors integrate into, or anything deployed | A personal throwaway | Fowler, Continuous Integration (2006); Humble and Farley, Continuous Delivery (2010) |
| `dora-metrics` | DORA metrics | EB-07 | A system deployed repeatedly, where delivery performance informs decisions | Libraries and CLIs without deployment, or too few deploys to read a trend | Forsgren, Humble and Kim, Accelerate (2018); current DORA report |

- [ ] **Step 4: index the forms**

`templates/README.md`: one line each for `practice-card.md` and `adr.md`.

- [ ] **Step 5: verify and commit**

Run the three checks. Commit:
`docs(practices): add the practice catalog, card form and ADR form`

### Task 3: cite practices from the Task Contract

**Files:**
- Modify: `templates/task-contract.md`,
  `engineering/engineering-baseline.md`

- [ ] **Step 1: add the subsection**

At the end of section 8, after "N/A justification", without renumbering:

```markdown
### Practices

Optional. List only practices from the
[practice catalog](../engineering/practices/README.md) whose "Applies when"
holds for this task. Leave the subsection out when none applies.

| Practice | Serves | Why it applies here | Evidence |
| --- | --- | --- | --- |
| `test-strategy` | EB-03 | `[boundary that needs proof]` | `[command / review]` |
```

Template version 0.2 becomes 0.3, and the `Base` line names the catalog.

- [ ] **Step 2: point EB-05 to the catalog**

One sentence after "None of them is to be applied mechanically": the practice
catalog says, per practice, when it applies and when it does not. The rule
text and the Baseline version do not change.

- [ ] **Step 3: verify and commit**

Run the three checks. Commit: `docs(contracts): cite catalog practices in the engineering check`

### Task 4: wire the validator into the repository check

Runs after Task 3, so the `### Practices` example it requires already exists.

**Files:**
- Modify: `validators/check_repository.py`, `tests/test_repository.py`

- [ ] **Step 1: write the failing repository tests**

In `RepositoryCheckTests`, each on the copied tree and expecting exit 1 with
the named path in stderr:

- `test_practice_card_missing_section_fails`: remove `## Verification` from
  `engineering/practices/tdd.md`.
- `test_practice_card_not_indexed_fails`: copy a card to
  `engineering/practices/new-practice.md` with its id changed to
  `new-practice`; stderr names `engineering/practices/README.md`.
- `test_indexed_practice_without_card_fails`: delete
  `engineering/practices/adr.md`.
- `test_repeated_index_row_fails`: duplicate the `tdd` row of the index
  table; stderr names `engineering/practices/README.md`.
- `test_malformed_index_row_fails`: replace the first cell of the `tdd` row
  with plain text `tdd`, so the card file still exists and the row has no
  link; stderr names `engineering/practices/README.md`.
- `test_practice_template_missing_section_fails`: remove `## Source` from
  `templates/practice-card.md`.
- `test_contract_template_cites_unknown_practice_fails`: replace the example
  id in the `### Practices` table of `templates/task-contract.md` with
  `no-such-practice`.

- [ ] **Step 2: confirm they fail**

Run: `python3 -m unittest tests.test_repository -v`
Expected: the seven new tests FAIL; the others pass.

- [ ] **Step 3: implement `check_practices(errors)`**

Called in `check()` after `check_dispatch`. It reads the Baseline ids, runs
`validate_card` on every `engineering/practices/*.md` except `README.md`,
reports every message from `index_ids` of the index, compares the card stems
with the ids it returns and reports a repeated id, runs `validate_sections` on
`templates/practice-card.md`, and checks that `practice_ids` of
`templates/task-contract.md` is non-empty and that each id matches
`PRACTICE_ID` and names an existing card. Each message from
`practice_cards.py` gets the repository-relative path as prefix.

- [ ] **Step 4: confirm they pass, prove by mutation and commit**

Run all three checks; mutate `check_practices` once per new test as in
Task 1. Commit: `feat(validators): check the practice catalog in the repository`

### Task 5: discoverability

**Files:**
- Modify: `README.md`, `docs/capabilities.md`, `docs/verification.md`,
  `validators/README.md`

- [ ] **Step 1:** `README.md` table: a row for `engineering/practices/`.
  `docs/capabilities.md`: rows "Choose an engineering practice" and "Record a
  structural decision". `docs/verification.md` and `validators/README.md`: the
  repository check also validates practice cards, the catalog index and the
  practice ids in the contract template.
- [ ] **Step 2:** run the three checks and commit:
  `docs: point to the practice catalog and its check`

## TC-0002: lifecycle map (#31)

Starts only after TC-0001 is merged into `main`.

### Task 6: gap forms

**Files:**
- Create: `templates/learning-record.md`
- Modify: `templates/project-frame.md`, `templates/README.md`,
  `docs/learn-back.md`

- [ ] **Step 1: Learning Record form**

Header: record id, date, project, Radiant revision, related contract or ADR.
Sections in the order of Article XV: `Outcome`, `Evidence`, `Diagnosis`,
`Fix target`, `Change`, `Verification`, `Reuse`. An optional `Incident`
section, used when the outcome is a production incident: detection, impact,
timeline in UTC, time to restore (the input of `dora-metrics`) and
contributing factors written without blame.

- [ ] **Step 2: Project Frame form**

In "Smallest experiment", one placeholder line for the outcome metric: what is
measured, baseline, target and when it is read. A new last section, `Result`,
filled after the experiment: each refutation condition ends supported, refuted
or inconclusive, with its evidence and the human decision that follows.

- [ ] **Step 3: index and point**

`templates/README.md`: one line for `learning-record.md`.
`docs/learn-back.md`: the "selective record" links to the form.

- [ ] **Step 4:** run the three checks and commit:
  `docs(templates): add a learning record and a frame result section`

### Task 7: the map

**Files:**
- Create: `docs/lifecycle.md`

- [ ] **Step 1: write the map**

An opening paragraph: the phase lists are a working model for this map, not a
standard, and the Radiant cycle is the process; the map only shows where each
phase's evidence lives. Then two tables with the columns `Phase`, `Radiant
stage`, `Artifact` and `Note`. Every artifact cell is a link; every row
without an artifact starts its note with `Out of scope:` and a reason.

SDLC:

| Phase | Radiant stage | Artifact | Note |
| --- | --- | --- | --- |
| Planning | Frame, Plan | Project Frame, Implementation Plan | |
| Requirements | Spec | Spec (thesis section 6.3) | The Spec form comes with #33 |
| Design | Design | ADR form, Design Frame, Design Spec, EB-04, EB-06 | System and experience tracks; security boundaries and structural dependencies are decided here and recorded in an ADR |
| Implementation | Contract, Build | Task Contract (sections 4 and 10), Engineering Baseline, practice catalog | Section 4 bounds paths, external systems and network (EB-04); section 10 governs new dependencies (EB-06) |
| Testing | Verify | Task Contract sections 11 and 16, `test-strategy`, EB-04 | Security verification when the change touches the surfaces EB-04 lists |
| Release | Build, Verify | "Release and versioning" section, `semantic-versioning` | New section |
| Deployment | Build, Verify | "Deploy" section, `ci-cd` | New section; the concrete checklist lives in the project's Profile |
| Operations | Verify, Learn Back | EB-07, `dora-metrics` | Monitoring tooling is stack-specific and belongs to the Profile |
| Incident and postmortem | Learn Back | Learning Record with its Incident section | New form. Out of scope: live incident response runbooks, which depend on the environment |
| Maintenance | Outside the cycle (feeds the Frame), Learn Back | radiant-maintenance, maintenance report | As the Maintenance role in radiant-delegation defines it |
| Retirement | Plan, Contract | Plan, ADR form, Task Contract HOLD conditions | Irreversible, so Article III applies |

PDLC:

| Phase | Radiant stage | Artifact | Note |
| --- | --- | --- | --- |
| Discovery | Frame | Project Frame, radiant-research | |
| Definition | Frame, Challenge | Project Frame, radiant-grill | |
| Solution design and prototyping | Design | Design Frame, Design Spec, design layer prototyping | |
| User validation | Frame, Design, Verify | Project Frame "Smallest experiment" and "Result", design layer prototyping | New section; the experiment is framed in the Frame, run through prototyping or real use, and read in Verify |
| Development | Spec to Verify | The SDLC table | |
| Launch | None | None | Out of scope: go-to-market, pricing and communication are business functions, and Radiant is a development operating system; release mechanics are in the SDLC table |
| Outcome measurement | Frame, Verify, Learn Back | Project Frame outcome metric and "Result" | New line in the form; declared in the Frame, read in Verify, acted on in Learn Back |
| Iterate or sunset | Learn Back, Frame | Learning Record, Frame revision, ADR form | Sunset is a human decision (Article XIII) |

Link targets for artifacts that are not a whole file, relative to `docs/`:

| Artifact | Target |
| --- | --- |
| Project Frame | `../templates/project-frame.md`, with `#intent-and-participant` for Discovery, `#hypothesis-and-challenge` for Definition and `#smallest-experiment` for validation and outcome |
| Implementation Plan | `project-generation-system.md#65-plan` |
| Spec | `project-generation-system.md#63-spec` |
| radiant-research and radiant-grill | `../skills/radiant-delegation/SKILL.md#ideation` |
| Maintenance role | `../skills/radiant-delegation/SKILL.md#maintenance` |
| Design Frame, Design Spec, prototyping | `design-layer.md#design-frame`, `#design-spec`, `#prototyping-and-review` |
| Task Contract sections | `../templates/task-contract.md#4-allowed-scope`, `#10-dependency-policy`, `#11-verification-plan`, `#13-hold-conditions`, `#16-completion-report` |
| EB-04, EB-06, EB-07 | `../engineering/engineering-baseline.md#6-eb-04---security-privacy-and-data-control`, `#8-eb-06---dependencies-and-supply-chain`, `#9-eb-07---operability-diagnosis-and-observability` |
| Radiant's own metrics | `project-generation-system.md#29-metrics` |

Every anchor above exists at the plan's base commit; the repository check
confirms them once the links are written.

Then the two short sections. "Release and versioning": commits follow
Conventional Commits; release notes are generated from history and
`CHANGELOG.md` is never edited by hand; version per `semantic-versioning` when
there are consumers of a published interface; Radiant itself is identified by
commit, as in [contributing](../contributing.md#initial-identity). "Deploy":
the questions every deploy answers (what exact commit or artifact, who
approves, how it is reversed, in which order data migrations run and whether
they reverse, which smoke check runs after and who watches it), the Task
Contract HOLD condition for an unplanned irreversible action, and that the
concrete checklist lives in the project's Engineering Profile or `workflow`.

A last short paragraph separates the three kinds of metric: the product
outcome metric in the Frame, delivery performance in `dora-metrics`, and
Radiant's own metrics in thesis section 29.

- [ ] **Step 2: focused check of the acceptance**

Run a one-off script over `docs/lifecycle.md` (kept outside the repository)
that prints every table row without a local link and without `Out of scope:`.
Expected: no output. Paste the command and output into the Completion report.

- [ ] **Step 3:** run the three checks and commit:
  `docs(lifecycle): map SDLC and PDLC phases to Radiant artifacts`

### Task 8: link the map from the cycle

**Files:**
- Modify: `docs/project-generation-system.md` (one sentence after the cycle
  line in section 6), `skills/radiant-cycle/SKILL.md` (one pointer in "Plan
  and frame", `metadata.version` from `0.1.5` to `0.1.6`), `README.md`,
  `docs/capabilities.md`

- [ ] **Step 1:** add the pointers; no other wording changes.
- [ ] **Step 2:** run the three checks and commit:
  `docs: link the lifecycle map from the cycle`

## After the merges

AGENTS.md asks for the living pages (map, glossary, use cases) to follow
changes to the thesis, a skill or a template. Both contracts change templates,
and TC-0002 changes the thesis and the cycle skill. That update happens in
`faelplg/design-systems`, needs the owner's approval to publish, and gets its
own issue in the `lab.fael.tech` project before TC-0001 is activated.

## Open questions for Rafael

1. **Link from the Constitution.** #31 asks to link the map from the
   Constitution. The Constitution has no outbound links today, and section 7
   keeps volatile material out of it; a link would also need a 0.1.2 version
   note. Recommendation: link from the thesis, the cycle skill, the README and
   the capability index only, and drop the Constitution from #31's scope.
   TC-0002 is written that way and holds if you want the link.

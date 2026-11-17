# Radiant Task Contract - Radiant - Practices / practice validator

**Contract ID:** `TC-0004`\
**Template version:** `0.4`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #34`\
**Status:** `DONE` - accepted after independent critique and orchestrator readback on 2026-11-17\
**Owner:** `Fael (human); Build by an authorized agent`\
**Risk tier:** `2` - the check joins `check_repository.py`, the CI gate of every Radiant change, and adds a command that consumers reach through their pin\
**Capability:** `default`\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `none`\
**Entry commit:** `92bcf449ee538476748770edaac8757835650451`\
**Tracking:** [issue #34](https://github.com/faelplg/radiant/issues/34), sub-issue of epic [#30](https://github.com/faelplg/radiant/issues/30); [#61](https://github.com/faelplg/radiant/issues/61), which blocked it, is closed

Routing: the Build runs as `radiant-dev` at `standard`, the build tier, on
the Codex harness. The independent critique runs as `radiant-verifier` at
`deep`, by a reviewer independent of the author, as section 11 defines. Model
IDs go only in the provenance lines of the Completion report, as
[radiant-delegation](../../skills/radiant-delegation/SKILL.md#provenance)
requires.

Activation: the owner authorized Build on 2026-11-17 at 15:04 BRT: "Merge
feito, pode seguir." ("Merged, you may proceed."). No active-contract pointer
is present in this repository; this activation records the governing contract.

## 1. Objective

> **A Radiant command refuses a Task Contract whose `8. Engineering Check` is empty, whose `12. Acceptance criteria` has no criterion, or whose cited practice ids are in neither the catalog nor the project's Profile, with an error that names the section; from `Template version` `0.4` it also requires `18. Owner decisions`. `check_repository.py` applies the same rules to Radiant's own contracts, and every existing one passes.**

## 2. Why this task exists

**Source plan/spec:**

- [Issue #34](https://github.com/faelplg/radiant/issues/34): scope and
  acceptance. Its section numbers, 8 for the Engineering Check and 12 for the
  acceptance criteria, match [template](../../templates/task-contract.md)
  version 0.4; this contract uses the template's numbers and titles.
- The owner's comment on #34, from the TC-0001 critique on PR #44:
  `practice_ids` returns a linked cell as written, so this contract either
  accepts the linked form or states that ids are bare backticks;
  [owner decision 1](#18-owner-decisions) accepts the linked form.
- [Issue #61](https://github.com/faelplg/radiant/issues/61): `# 18. Owner decisions`
  exists so that #34 can treat it as required. The template keeps the section
  "so a validator can require it", and the
  [convention](../../contracts/README.md#integrity) exempts contracts without
  a `Template version` field or at `0.3` or earlier.
- [Epic #30](https://github.com/faelplg/radiant/issues/30), track 1: "check
  practices with a validator"; track 2 asks for structured validator output.
- [Practice catalog](../../engineering/practices/README.md): citation is
  opt-in, and the Baseline table remains the required engineering check.
- [TC-0001](TC-0001-practice-catalog.md#6-non-goals) and
  [TC-0003](TC-0003-engineering-profile.md#6-non-goals) deferred contract
  citations and project practice ids to #34.

**Hypothesis or risk reduced:**

- Today no validator checks any practice, so a contract can ship with an
  undecided Engineering Check, no observable criterion or a misspelled
  practice id, and only a human reader notices. Three deterministic rules at
  the contract boundary move those failures from review to the gate.
- What would refute it: the rules cannot accept every existing Radiant
  contract without rewriting a historical body. The Build then stops on HOLD
  instead of loosening a rule silently or editing a `DONE` contract.

## 3. Inputs

Consumer probe revisions fixed at activation:

- `faelplg/demerzel`: `8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0`.
- `faelplg/aikm`: `a2cfd1bf6f415521567d0e48d8eebcc79a3e611d`.

The agent may assume as input:

- the documents in section 2, the [Baseline section 2](../../engineering/engineering-baseline.md#2-proportionality-rule)
  status vocabulary (`REQUIRED`, `APPLICABLE`, `N/A`), the
  [Profile form](../../templates/engineering-profile.md) `Project practices`
  table and the [contract convention](../../contracts/README.md);
- `validators/practice_cards.py` (`practice_ids`, `PRACTICE_ID`,
  `baseline_ids`, `_prose`), `validators/check_dispatch.py`,
  `validators/check_repository.py` and their tests, as the code, output and
  test style to follow;
- the existing contracts `docs/plans/TC-0001-practice-catalog.md`,
  `TC-0002-lifecycle-map.md` and `TC-0003-engineering-profile.md`. None has a
  `Template version` field. A planning probe, kept outside the repository,
  applied the rules of section 7 to all three and reported no error; the
  template itself fails them, as a form with placeholders should;
- under owner decision 7, consumer contracts, read-only, from the
  owner's local checkouts of `faelplg/demerzel` and `faelplg/aikm`. The
  activation commit records here the full commit of each consumer, as
  TC-0003 did before its Build. The Build request supplies each checkout's
  absolute root and grants the sandbox read access to it. The Build reads
  only at the recorded commits, with `git -C <checkout> show <commit>:<path>`
  and `git -C <checkout> ls-tree -r --name-only <commit>`, never from the
  working tree, and reports the results in section 16. The Build opens no
  issue; the orchestrator opens any consumer pointer issue, with the owner's
  authorization. The contract does not carry the paths: the repository check
  refuses personal paths.

[Issue #52](https://github.com/faelplg/radiant/issues/52) also edits
`check_repository.py`. If it merges first, the Build rebases onto it; the two
checks stay separate functions.

Do not infer missing inputs that would materially change the solution.

## 4. Allowed scope

### Paths allowed to change

```text
validators/task_contracts.py
validators/check_contract.py
validators/check_repository.py
validators/practice_cards.py
validators/README.md
tests/test_task_contracts.py
tests/test_check_contract.py
tests/test_repository.py
tests/test_practice_cards.py
docs/verification.md
docs/integration.md
contracts/README.md
engineering/practices/README.md
docs/plans/TC-0004-practice-validator.md
```

`validators/practice_cards.py` and `tests/test_practice_cards.py` change only
for two shared pieces and their tests: a table-row reader that returns every
cell of a row, on which `_table_rows` keeps its current behavior, and the
practice cell reading of `practice_ids`. Every existing test in
`tests/test_practice_cards.py` stays unchanged and passes.
`docs/integration.md`, `contracts/README.md` and
`engineering/practices/README.md` take pointer sentences only.

### Paths read-only

```text
constitution/
engineering/engineering-baseline.md
engineering/practices/*.md except README.md
engineering/stacks/
templates/
skills/
adapters/
validators/check_dispatch.py
validators/check_project.py
validators/dispatch_formats.py
validators/radiant_yaml.py
tests/test_check_dispatch.py
tests/test_dispatch_formats.py
tests/test_integration.py
tests/test_radiant_yaml.py
docs/adrs/
docs/history/
docs/plans/ (every file except this contract)
the consumer checkouts listed in section 3
```

### External systems allowed

- None for the Build. GitHub, through `gh`, only to open this contract's PR
  after the owner authorizes it.

### Network

`DENIED` except the authorized push and PR.

## 5. Required outputs

1. `validators/task_contracts.py`: the contract rules of section 7, as
   functions that take text and return messages without paths, like
   `practice_cards.py`.
2. `validators/check_contract.py`: the command
   `check_contract.py <contract|-> [--profile <path>]`, with tests in
   `tests/test_check_contract.py` and unit tests in
   `tests/test_task_contracts.py`.
3. `validators/check_repository.py`: the same rules over
   `docs/plans/TC-[0-9][0-9][0-9][0-9]-*.md`, against the catalog only, with
   tests in `tests/test_repository.py`.
4. `validators/practice_cards.py`: the shared table-row reader of section 4,
   and `practice_ids` reading the linked cell form, as owner decision 1
   requires.
5. Pointers: `validators/README.md` (the command and its output),
   `docs/verification.md` (the repository check now validates Radiant's
   contracts, replacing the sentence that says it does not),
   `docs/integration.md` (how a consumer runs the check from its pinned
   checkout), `contracts/README.md` (validation of a contract) and
   `engineering/practices/README.md` (citations are checked when present).

Do not create additional artifacts without an observed need.

### Decisions

| Decision | Choice |
| --- | --- |
| Entry point | A new command, `validators/check_contract.py`, over a new rule module, `validators/task_contracts.py`; `check_dispatch.py` is unchanged |
| Output | Same convention as `check_dispatch.py`: success prints JSON and exits 0; invalid content prints `{"errors": [...]}` and exits 1; a usage error exits 2 |
| Section lookup | A heading of level 1 or 2 whose text is exactly the template's number and title, such as `8. Engineering Check`, outside fenced blocks; it runs until the next heading of level 1 or 2. Inside section 8, the Baseline table is read before the first level 3 heading, and `### Practices` is a level 3 subsection that runs until the next heading of level 1 to 3 |
| `18. Owner decisions` | Required when `Template version` is `0.4` or later; exempt when the field is absent or `0.3` or earlier |
| Known practice ids | Card stems in the checkout's `engineering/practices/`, plus the ids in the `Project practices` table of the Profile given with `--profile` |
| Radiant's own contracts | `check_repository.py` checks `docs/plans/TC-[0-9][0-9][0-9][0-9]-*.md` against the catalog; the template is a form and is not checked as a contract |
| Practice cells | Bare `tdd`, backticked `` `tdd` `` and, by owner decision 1, a link whose text is `` `tdd` ``; bare ids stay accepted because `practice_ids` and `tests/test_practice_cards.py` already accept them and TC-0001 relies on that |
| Consumer gates | `check_project.py` and `check_dispatch.py` keep their behavior and output byte for byte |

Each decision stands unless the owner overturns it in review.

#### Why a new command instead of extending `check_dispatch.py`

`check_dispatch.py` is the dispatch gate: Demerzel's integration calls it,
from the pinned checkout, to validate `radiant-units` and routing before a
launch ([Demerzel boundary](../integration.md#demerzel-boundary)), and its
success output is the parsed value that the operator consumes. A contract
check has a different audience, every contract author and reviewer, whether
or not the contract is dispatched, and a different success value. Adding it
as a subcommand would give one file two reasons to change, the case the
[`solid-srp`](../../engineering/practices/solid-srp.md) card names, and would
make every change to contract rules a change to the dispatch gate's file.
Folding it into `units` would be worse: a consumer's pin bump would start
refusing dispatch of contracts that dispatched before.

The cost is one more entry point. It is documented next to the others in
`validators/README.md`, keeps the same output convention, so a caller parses
both the same way, and shares code through modules, as `check_repository.py`
already shares `practice_cards.py` and `dispatch_formats.py`.

#### Why `18. Owner decisions` becomes required from `0.4`

The template reserves the section for a validator, and the convention
already defines the exemption. Gating on the contract's own declared version,
not on a date or a path, keeps historical contracts valid without rewriting
them ([integrity](../../contracts/README.md#integrity)): TC-0001 to TC-0003
and every consumer contract written before 0.4 have no field and stay exempt.
The version is compared numerically by major and minor, so `0.10` is later
than `0.4`. A version later than the checkout's own template, read from its
`**Version:**` line, is refused: the contract was written against rules this
checkout does not know.

#### How consumers are affected through the pin

Consumers run the validators of the Radiant revision they pin
([no silent update](../integration.md#no-silent-update)). Before a pin bump,
nothing changes. After one:

- `check_project.py` and `check_dispatch.py` behave as before, so the pin gate
  and Demerzel's dispatch gate keep passing;
- `check_contract.py` exists in the checkout but runs only when the consumer
  or its tooling calls it. Making it a gate is a consumer decision, taken in
  that consumer's repository (owner decision 5);
- a consumer contract without `Template version` is exempt from section 18
  but not from sections 8 and 12. A consumer that adopts the command and has
  a contract that fails those rules fixes it through its own
  [integrity](../../contracts/README.md#integrity) rules, as an explicit
  amendment, never by a Radiant change.

### Questions decided by the owner

The owner decided all seven questions on 2026-11-17, choosing option (a),
the recommended one, for each; the second-opinion review of this contract had
agreed with every recommended option. The decisions and their contract impact
are recorded in [section 18](#18-owner-decisions). The options below are kept
as the record of what was weighed.

1. **Linked practice cells.** TC-0001 and TC-0003 cite backticked ids, and
   `tests/test_practice_cards.py` also accepts a bare id; the catalog index
   uses links. Bare and backticked ids stay accepted under both options.
   - (a) Also accept a Markdown link whose text is `` `id` `` and whose target
     is a relative `.md` path ending in `id.md`; the target is compared,
     never opened.
     Consequence: authors may link cards for readers; `practice_ids` and
     `check_repository.py` change together.
   - (b) Accept no link; refuse it with a message that says so.
     Consequence: no change to `practice_ids`; readers lose the link.
2. **Where the Profile comes from.**
   - (a) `--profile <path>`, explicit. Consequence: simple and testable; a
     consumer that forgets it sees its own ids refused, a safe failure.
   - (b) `--project <root>`, reading `engineering_profile` from
     `.radiant.json`. Consequence: one argument for consumers, but the
     command duplicates the map and path rules of `check_project.py` or
     couples to it.
   - (c) Both. Consequence: two paths to test and document.
3. **What counts as an empty Engineering Check.**
   - (a) Refuse when no row is `REQUIRED` or `APPLICABLE`; rows may be any
     subset of EB-01 to EB-08. Consequence: matches the template's "apply only
     what is relevant"; an all-`N/A` table is refused.
   - (b) Also require all eight rows. Consequence: stricter, and consumer
     contracts that drop irrelevant rows fail.
   - (c) Refuse only when no row has a decided status. Consequence: an
     all-`N/A` table passes, although every task has something to verify.
4. **Minimum acceptance criteria.**
   - (a) At least one checklist item that is neither a template placeholder
     such as `` `[observable criterion]` `` nor one of the template's four
     generic items. Consequence: a contract must state at least one observable
     criterion of its own; every existing Radiant contract has one.
   - (b) Any checklist item. Consequence: a contract with only the generic
     items passes, which the issue's "no acceptance criteria" does not reach.
5. **Gate adoption.**
   - (a) Opt-in command only; no existing gate calls it outside Radiant.
     Consequence: no consumer breaks on a pin bump; adoption is a follow-up
     per consumer.
   - (b) `check_dispatch.py units` also runs the contract rules. Consequence:
     Demerzel refuses to dispatch contracts that fail, including old ones,
     on its next pin bump.
   - (c) `check_project.py` checks the contract that `ACTIVE.md` points to.
     Consequence: the pin gate reads contracts and fails a project whose
     active contract fails, a change to the map gate's meaning.
6. **Shape of an owner decision entry.**
   - (a) Require the section with a non-blank body, `None.` or entries, and
     refuse the template's unedited `[YYYY-MM-DD]` entry placeholder.
     Consequence: the issue's need is met; entry format stays a review
     concern.
   - (b) Also check each entry's date and `Contract impact`. Consequence:
     stronger provenance, more rules and more failing contracts to amend.
7. **Consumer probe.**
   - (a) The Build runs `check_contract.py`, read-only, over the contracts of
     Demerzel and AIKM at the commits recorded in section 3 at activation,
     and reports the results in section 16. The orchestrator, not the Build,
     opens one pointer issue in each consumer with failures, with the
     owner's authorization.
     Consequence: the effect on consumers is measured before any adopts the
     command; the sandbox needs read access to both checkouts, and the
     Build's network boundary does not change.
   - (b) No probe. Consequence: no consumer access; the effect is learned at
     adoption.

### Build order

Each task is one commit; after each, all the automated checks of section 11
pass. New files are staged before the full test run:
`tests/test_repository.py` copies only `git ls-files` into its fixtures.

1. **Rules, test-first.** `tests/test_task_contracts.py` and the new tests in
   `tests/test_practice_cards.py`; run them and see them fail as section 11
   describes; implement `validators/task_contracts.py` and the shared pieces
   in `practice_cards.py`; run them and see them pass; commit; then prove
   each rule by mutation. Commit:
   `feat(validators): add Task Contract rules for practices and acceptance`.
2. **Command, test-first.** `tests/test_check_contract.py`, then
   `validators/check_contract.py`, same order. Commit:
   `feat(validators): add the check_contract command`.
3. **Repository gate, test-first.** `tests/test_repository.py`, then
   `check_repository.py`, same order. Commit:
   `feat(validators): check Radiant's own Task Contracts`.
4. **Pointers.** The files of output 5. Commit:
   `docs: point to the Task Contract check`.

## 6. Non-goals

This task must **not**:

- change `check_project.py`, `check_dispatch.py`, their output or their
  tests; a gate that calls the new command is a separate decision
  (owner decision 5);
- change the Task Contract template, its version or any other template;
- edit TC-0001, TC-0002 or TC-0003, or any consumer contract;
- change any consumer repository, its `.radiant.json` or its pin;
- validate other contract sections, the `N/A justification`, the Practices
  table's `Serves` column against the cited card, or Profile sections other
  than the `Project practices` ids;
- validate the structure of stack packs (#52);
- update the living pages in `faelplg/design-systems`.

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

# 7. Functional requirements

- [ ] Fenced blocks are ignored: a heading, row or line inside a fence never counts.
- [ ] Sections `8. Engineering Check`, `12. Acceptance criteria` and `18. Owner decisions` are found and bounded as the section lookup decision in section 5 says; a heading of level 3 such as `### Practices` never ends a numbered section.
- [ ] A contract without a `8. Engineering Check` heading produces `missing section: 8. Engineering Check`; the same holds for `12. Acceptance criteria`, and for `18. Owner decisions` when its version requires it.
- [ ] A numbered section heading that appears more than once, and a second `### Practices` inside section 8, are each refused as a repeated heading, naming the section.
- [ ] Section 8's Baseline rows are the data rows of its table before the first level 3 heading. Each row starts with an EB id that exists in the Baseline and has status `REQUIRED`, `APPLICABLE` or `N/A`, with or without backticks; an unknown id, an undecided status such as `REQUIRED / N/A` and a repeated id are each refused, naming section 8 and the id.
- [ ] Section 8 with no `REQUIRED` or `APPLICABLE` row is refused as empty, naming section 8.
- [ ] Without a `### Practices` heading inside section 8, the contract cites no practice and passes this rule. A `### Practices` heading whose table has no data row is refused, naming the subsection; that is how an empty subsection differs from an absent one.
- [ ] A practice cell is read as an id in three forms: bare `tdd`, backticked `` `tdd` `` and, by owner decision 1, a link whose text is `` `tdd` `` and whose target is a relative path with no URL scheme, query or fragment, not starting with `/`, ending in `tdd.md`. The link target is never opened. Any other cell, including a link that breaks those rules, is refused as an invalid practice cell, naming the cell.
- [ ] Each id read from `### Practices` is a catalog card stem or a Profile project id; otherwise `unknown practice id` names section 8, the Practices subsection and the id. A repeated id is refused, naming it.
- [ ] A Profile's `Project practices` ids, bare or in backticks, are read from its table; an id outside the practice id pattern, equal to a catalog id or repeated is refused, naming the Profile and the id. A Profile without the section contributes no id.
- [ ] Section 12's checklist items are the lines `- [ ] `, `- [x] ` or `- [X] ` followed by text. A placeholder is an item whose text, after removing trailing `;`, `.` or `,`, surrounding whitespace and one pair of surrounding backticks, starts with `[` and ends with `]`. A generic item is one of the template's four fixed items, compared with the same trailing punctuation removed. With no item that is neither a placeholder nor generic, section 12 is refused, naming section 12.
- [ ] A contract without `Template version`, or at `0.3` or earlier, passes without `18. Owner decisions`.
- [ ] A contract at `0.4` or later is refused, naming section 18 and the template version that requires it, when the heading is missing, its body is blank, or its body still holds the template's unedited entry placeholder `[YYYY-MM-DD]`. `None.` is accepted.
- [ ] A malformed `Template version`, one that is not `MAJOR.MINOR` digits, or one later than the checkout's template, is refused, naming the field.
- [ ] `check_contract.py` reads a path or `-` for standard input. Success prints `{"template_version": "0.4", "practices": [...]}` and exits 0; `template_version` is the field's value as written, or JSON `null` when the field is absent, and `practices` lists the ids in table order. Failure prints every error in `{"errors": [...]}` and exits 1; a missing or unreadable contract or Profile exits 1 with an error naming it; a usage error exits 2.
- [ ] `check_repository.py` checks every `docs/plans/TC-[0-9][0-9][0-9][0-9]-*.md` against the catalog, prefixes each error with the contract's path and exits 1 on any; the current tree passes, including this contract.
- [ ] `check_project.py` and `check_dispatch.py` outputs are unchanged.

# 8. Engineering Check

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED`       | Three rules and the section 18 requirement; one module, one command, no new format | Diff review against section 5 decisions |
| EB-02 Correctness and contracts   | `REQUIRED`       | Exact section titles from template 0.4; numeric version comparison; historical contracts stay exempt | Tests in section 11 |
| EB-03 Verification and tests      | `REQUIRED`       | Test-first, pass and fail cases, mutation proof | Commands in section 11 |
| EB-04 Security and privacy        | `REQUIRED`       | Contract and Profile are read-only text; a practice id or link target never becomes a path that is opened | Tests with `../` link targets and path-like ids |
| EB-05 Maintainability             | `REQUIRED`       | Rules in a module that returns messages; the command and the repository check share it | Review |
| EB-06 Dependencies                | `REQUIRED`       | Standard library only | Diff review |
| EB-07 Diagnosis                   | `REQUIRED`       | Each error names the section, and the id or field when there is one; every error is reported at once | Assertions on the error text |
| EB-08 Experience and efficiency   | `APPLICABLE`     | A contract author fixes a refusal from the message alone | Readback of each message |

### Practices

| Practice | Serves | Why it applies here | Evidence |
| --- | --- | --- | --- |
| `tdd` | EB-03 | Every rule's accept and refuse result is known before coding | Failing runs before each implementation, in the Completion report |
| `test-strategy` | EB-03 | Rules are unit tested; the command and the repository check are proven at their CLI boundary | `tests/test_task_contracts.py`, `tests/test_check_contract.py`, `tests/test_repository.py` |
| `solid-srp` | EB-05 | The dispatch gate and the contract check serve different actors, so they stay in different commands | Section 5 decision; `check_dispatch.py` unchanged in the diff |

# 9. Project-specific constraints

Taken from `AGENTS.md` and the earlier contracts:

- Python 3.9+, standard library only; no `match`, no `X | Y` types.
- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- Validators stay read-only.
- No absolute personal path in any Markdown file; the repository check
  refuses them.

# 10. Dependency policy

### New runtime dependency allowed?

`NO`

# 11. Verification plan

## Automated

```text
PYTHONDONTWRITEBYTECODE=1 python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
```

## Focused verification

- Every item of section 7 has a test. Rule tests run on text; command and
  repository tests run the real command in a temporary directory, as
  `tests/test_check_dispatch.py` and `tests/test_repository.py` do.
- Fixture contracts are built in the tests from a minimal valid contract, not
  from the template, so a template edit cannot silently change them.
- Before each implementation, the new tests are run and seen to fail, and
  the Completion report shows each run. For the new files,
  `validators/task_contracts.py` and `validators/check_contract.py`, every
  new test fails because the module or script does not exist yet
  (`ModuleNotFoundError` or a missing file); that run proves the tests reach
  the new code, not each rule, so each rule's own proof is its mutation
  below. For the existing files, `practice_cards.py` and
  `check_repository.py`, the new tests fail on the missing behavior while
  every existing test, including those of `tests/test_practice_cards.py`,
  passes.
- After each validator commit, mutate one rule at a time: each refusal, the
  version comparison (string instead of numeric), the exemption, fence
  stripping, the linked cell and the path prefix in `check_repository.py`.
  Commit before mutating; observe the named test fail; restore with
  `git checkout -- <file>` and confirm the suite passes before the next
  mutation. Gate each step on the command's exit code.
- Run `check_contract.py` on TC-0001, TC-0002, TC-0003 and this contract, and
  record the output of each.
- Run `check_dispatch.py units` and `routing` on the template and the routing
  example, and `check_project.py` through its existing tests, at the entry
  commit and at the end; the outputs match.
- Under owner decision 7: run `check_contract.py` on each consumer contract,
  read from the commit recorded in section 3 through standard input, and
  report per file the result and errors in section 16. Record
  `git -C <checkout> rev-parse HEAD` and `git -C <checkout> status --porcelain`
  before and after; the records match. The Build opens no issue and makes no
  network call for the probe.

## Readback

After execution:

- reopen the module, the command, each pointer and every error message;
- confirm that no path outside the Allowed scope changed, against the entry
  commit, including committed, staged, unstaged and untracked changes
  (`git diff --name-only <entry>..HEAD` and `git status --porcelain`).

## Independent critique

`REQUIRED`

- `radiant-verifier` at `deep`, independent of the author as
  [Article VIII](../../constitution/CONSTITUTION.md#article-viii---creation-and-critique-must-be-separated-when-that-increases-confidence)
  requires: neither the Build session nor the session that wrote this
  contract. The harness follows the [routing rules](../routing.md); a
  different vendor is a routing choice, not a Core rule
  ([delivery flow](../delivery-flow.md#5-independent-critique)). It checks
  the result against this contract, issue #34's acceptance and section 18.
- Launched and collected by the orchestrator, never by the Build. The
  orchestrator records the role, capability, harness, full model ID and
  command in the Completion report's provenance.
- External prerequisites: the chosen harness installed and authenticated on
  the owner's machine.

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [x] `check_contract.py` refuses a contract with an empty Engineering Check, one with no acceptance criteria and one citing a practice id outside the catalog and the Profile, each with an error naming the section (issue #34);
- [x] tests cover the pass and fail case of every rule in section 7 (issue #34);
- [x] TC-0001, TC-0002, TC-0003 and this contract pass `check_repository.py` and `check_contract.py` unchanged, or the Build stopped on HOLD with the failure documented (issue #34);
- [x] a contract at `Template version` `0.4` without `18. Owner decisions` is refused, and one without the field is not (issue #61);
- [x] `check_project.py` and `check_dispatch.py` outputs are unchanged at the end;
- [x] all applicable checks in section 11 pass;
- [x] there was no change outside the Allowed scope;
- [x] relevant limitations are recorded;
- [x] the final evidence was read, not just presumed from the exit code.

# 13. HOLD conditions

Stop and ask for a decision when:

- a Build finding contradicts an [owner decision](#18-owner-decisions);
- an existing Radiant contract fails a rule and passing would require editing
  it or loosening the rule;
- a rule needs a change to the Task Contract template or its version;
- the check needs a dependency, a `.radiant.json` field or a change to
  `check_project.py` or `check_dispatch.py`;
- the agent would need to write outside the authorized paths, including any
  consumer checkout;
- the minimal solution no longer fits the contract.

`HOLD` is a valid result.

# 14. FAIL conditions

Mark `FAIL` when:

- acceptance criteria cannot be met;
- verification shows a material regression in the existing checks;
- `check_project.py` or `check_dispatch.py` output changes;
- an external blocker makes the goal impossible within this contract.

Do not disguise `FAIL` as `DONE WITH NOTES`.

# 15. Change budget

The agent may:

- add the two shared pieces of `practice_cards.py` that section 4 allows,
  keeping every existing test unchanged and passing;
- update directly affected tests and pointers.

The agent may not, without HOLD:

- refactor `check_repository.py` beyond adding the contract check;
- add rules, commands or output fields that were not requested.

# 16. Completion report

### Status

`DONE`. The owner reported the completed independent critique and
orchestrator readback on 2026-11-17 and authorized acceptance and closure.
The Build returned with the contract `ACTIVE`; this acceptance closes it.
No active-contract pointer exists in this repository, so none needs clearing.
No HOLD condition triggered. No network, push, PR, issue creation or consumer
edit was performed.

### Changed

Line references below refer to the indicated commit's files:

| Commit | Paths and evidence |
| --- | --- |
| `e7a2780` | `docs/plans/TC-0004-practice-validator.md:7`: activation, entry commit, authorization and pinned consumer revisions; no active pointer exists in this repository |
| `2adaba3` | `validators/task_contracts.py:19`: fence and section readers; `:76`: Engineering Check and practices; `:125`: version, acceptance and owner decisions; `tests/test_task_contracts.py:47`: rule tests; `validators/practice_cards.py:70`: shared all-cell reader preserving `_table_rows`; `:96`: practice cells; `tests/test_practice_cards.py:133`: new shared-reader tests, with all existing tests unchanged |
| `dd6803a` | `validators/check_contract.py:19`: read-only input and CLI; `tests/test_check_contract.py:32`: real command tests |
| `1ec1295` | `validators/check_repository.py:160`: separate contract gate and path-prefixed errors; `tests/test_repository.py:95`: real repository command tests |
| `be333ed` | `validators/practice_cards.py:104`, `tests/test_practice_cards.py:139`, `tests/test_task_contracts.py:85`: distinguish a URL scheme from a colon inside a relative link path |
| `b6f2af4` | `validators/README.md:34`, `docs/verification.md:34`, `docs/integration.md:183`, `contracts/README.md:56`, `engineering/practices/README.md:9`: command, rules, output and opt-in pointers |

The separate `be333ed` increment corrects an over-restriction found during
readback: `../cards:local/tdd.md` has no URL scheme and is allowed by owner
decision 1. It adds no rule or output field and changes only authorized shared
code and tests. This is the one extra implementation commit beyond section 5's
four-step sequence.

### Verification evidence

All commands ran locally with no network. Ephemeral detailed logs were kept
under `/tmp/tc-0004-evidence`; the evidence needed for handoff is recorded here.

Test-first runs, before each implementation:

| Command (`PYTHONDONTWRITEBYTECODE=1` prefix) | Observed failing-before result |
| --- | --- |
| `python3 -m unittest discover -s tests -p test_task_contracts.py` | Exit 1, `ModuleNotFoundError: No module named 'task_contracts'`; this proves the import boundary, not each rule |
| `python3 -m unittest discover -s tests -p test_practice_cards.py` | Exit 1, 26 tests: linked-cell assertion failed and `table_rows` import failed; the 24 existing tests passed |
| `python3 -m unittest discover -s tests -p test_check_contract.py` | Exit 1, all 7 tests failed because the command file did not exist; the usage test also requires argparse's usage text |
| `python3 -m unittest discover -s tests -p test_repository.py` | Exit 1, 23 tests: two new refusal tests failed because invalid contracts returned PASS; 21 other tests passed |
| `python3 -m unittest discover -s tests -p test_practice_cards.py` (relative-colon increment) | Exit 1, 27 tests: `test_relative_link_colon_outside_scheme_is_accepted` failed because the link cell stayed unread; 26 other tests passed |

After staging each increment, `check_repository.py`, the full unittest suite,
`git diff --check` and `git diff --cached --check` passed before committing:
143 tests for rules, 150 for the command, 153 for the repository gate, and
154 for the relative-link correction and pointers.

Mutation proofs ran only after committing the target file. Each successful
mutation produced exit 1 and a named assertion failure. Each target was
restored with `git checkout -- <file>`, then the rule and shared-reader suites
passed before the next mutation (40 tests initially, 41 after the extra link
case). No mutation remains in the delivery.

| Disabled or regressed rule | Named test in `ContractRuleTests`, unless qualified |
| --- | --- |
| Missing required section | `test_missing_sections` |
| Repeated section or Practices heading | `test_repeated_sections_and_practices` |
| Unknown EB id, repeated EB id, invalid status (three separate mutations) | `test_baseline_rows` |
| No active Engineering Check row | `test_empty_engineering_and_subsection_boundary` |
| Present but empty Practices table | `test_practices_optional_but_not_empty` |
| Invalid practice cell | `test_practice_cells` |
| Unknown practice id, repeated practice id (two separate mutations) | `test_unknown_repeated_and_ordered_practices` |
| Invalid, catalog-colliding or repeated Profile id (three separate mutations) | `test_profile_ids` |
| No concrete acceptance criterion | `test_acceptance_checklists_and_normalization` |
| Empty or placeholder owner decisions | `test_owner_decisions_and_exemption` |
| Malformed version, unsupported version (two separate mutations) | `test_numeric_versions_and_value_as_written` |
| String comparison replacing numeric comparison | `test_numeric_versions_and_value_as_written` |
| Absent-version exemption, old-version exemption (two separate mutations) | `test_owner_decisions_and_exemption` |
| Fence stripping | `test_fences_ignore_headings_rows_items_and_metadata` |
| Linked practice cell | `PracticeCardTests.test_practice_ids_reads_linked_cells` |
| Command content refusal | `ContractCommandTests.test_all_content_errors_exit_1` |
| Hardcoded supported version instead of the checkout template | `ContractCommandTests.test_checkout_template_controls_supported_version` |
| Repository contract gate, repository path prefix (two separate mutations) | `RepositoryCheckTests.test_contract_rules_fail_with_each_contract_path` |
| Rejecting a colon outside a URL scheme | `PracticeCardTests.test_relative_link_colon_outside_scheme_is_accepted` |

There were 27 successful assertion-producing mutation proofs. An initial
absent-version mutant instead raised `TypeError` while formatting a missing
version; it was restored and excluded from that count. A replacement mutant
that incorrectly refuses the absent version produced the required assertion
failure. The successful absent-version and old-version proofs were then run
separately.

Direct command runs, all exit 0:

```text
python3 validators/check_contract.py docs/plans/TC-0001-practice-catalog.md
{"template_version": null, "practices": ["tdd", "test-strategy"]}
python3 validators/check_contract.py docs/plans/TC-0002-lifecycle-map.md
{"template_version": null, "practices": []}
python3 validators/check_contract.py docs/plans/TC-0003-engineering-profile.md
{"template_version": null, "practices": ["tdd", "test-strategy"]}
python3 validators/check_contract.py docs/plans/TC-0004-practice-validator.md
{"template_version": "0.4", "practices": ["tdd", "test-strategy", "solid-srp"]}
```

Compatibility: before implementation and at the end,
`check_dispatch.py units templates/task-contract.md` and
`check_dispatch.py routing docs/routing.example.json` exited 0. Their saved
stdout files compared byte for byte with `cmp`, both exit 0.
`python3 -m unittest discover -s tests -p test_integration.py` passed all 32
existing pin/project-gate tests at entry and at the end. The two gate files
and their existing tests have no diff against the entry commit.

Final checks:

```text
PYTHONDONTWRITEBYTECODE=1 python3 validators/check_repository.py
PASS: 67 documents; 496 local links. Exit 0.
python3 -m unittest discover -s tests
154 tests, OK. Exit 0.
git diff --check
Exit 0.
git diff --cached --check
Exit 0.
```

Readback covered the module, command, all changed pointers and error messages.
The committed path list against the entry, staged/unstaged diff and untracked
status were checked against section 4. Only the 14 allowed paths changed.
TC-0001 to TC-0003, templates, adapters, skills and consumer checkouts are
unchanged.

### Consumer probe

Each consumer's `.radiant.json`, contract listing and contract bodies were
read exclusively with `git -C <checkout> show <recorded-commit>:<path>` and
`git -C <checkout> ls-tree -r --name-only <recorded-commit>`. All TC Markdown
files in those listings were checked through `check_contract.py -` with their
body on stdin. Both recorded maps have a null Engineering Profile, so no
`--profile` was supplied. Every result is listed below; no consumer gate was
changed or adopted.

| Consumer | Recorded commit, also HEAD before and after | `status --porcelain` before and after |
| --- | --- | --- |
| `faelplg/demerzel` | `8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0` | Empty, identical |
| `faelplg/aikm` | `a2cfd1bf6f415521567d0e48d8eebcc79a3e611d` | Empty, identical |

All paths below are under each consumer's `docs/project/contracts/`.

| Consumer file | Exit | Exact JSON stdout |
| --- | --- | --- |
| Demerzel `TC-0001-core.md` | 0 | `{"template_version": null, "practices": []}` |
| Demerzel `TC-0002-herdr-backend.md` | 0 | `{"template_version": null, "practices": []}` |
| Demerzel `TC-0003-radiant-integration.md` | 0 | `{"template_version": null, "practices": []}` |
| Demerzel `TC-0004-project-preparation.md` | 0 | `{"template_version": null, "practices": []}` |
| AIKM `TC-0023-pipeline-skills-three-harnesses.md` | 1 | `{"errors": ["missing section: 8. Engineering Check", "missing section: 12. Acceptance criteria"]}` |
| AIKM `TC-0024-skills-antigravity.md` | 1 | `{"errors": ["missing section: 8. Engineering Check", "missing section: 12. Acceptance criteria"]}` |
| AIKM `TC-0025-external-sources.md` | 1 | `{"errors": ["missing section: 8. Engineering Check", "missing section: 12. Acceptance criteria"]}` |

These AIKM results are measured adoption concerns, not a Radiant HOLD:
owner decisions 5 and 7 keep adoption opt-in and assign any pointer issue to
the orchestrator. The Build opened no issue.

### Independent critique and orchestrator acceptance

Source: the owner's acceptance instruction of 2026-11-17. The following
critique and orchestrator results were supplied by the owner; this closing
session records them without claiming to have launched the critique.

- Independent critique: `VERDICT approve`, no Must-fix and no Should-fix.
  The critic reran the checks, probed the command with its own contracts,
  confirmed `check_dispatch.py` and `check_project.py` are unchanged, and
  reproduced the consumer probe output.
- Orchestrator readback: `check_repository.py` PASS (67 documents), all
  154 tests OK, `git diff --check` clean, and `check_contract.py` accepts
  TC-0001 through TC-0004. The orchestrator accepted the delivery following
  the independent approval; the owner authorized setting the contract to
  `DONE` and committing this closure.
- Closure verification: the three requested checks were rerun for this
  documentation change: `PYTHONDONTWRITEBYTECODE=1 python3 validators/check_repository.py`
  PASS (67 documents), `python3 -m unittest discover -s tests` 154 tests OK,
  and `git diff --check` clean. No implementation file changed in closure.

### Engineering notes

- Standard library only, Python 3.9-compatible syntax and APIs. Text rules
  have no filesystem access; the CLI reads only explicit inputs and checkout
  catalog/Baseline/template sources. Link targets never become opened paths.
- Section lookup and practice parsing are shared between the standalone
  command and repository gate. The dispatch gate remains independent.
- Existing shared-reader tests remain unchanged. New fixtures are minimal
  contracts in tests, independent of the template.

### Remaining limitations

- Independent critique and orchestrator acceptance are complete, as reported
  by the owner above. The critique transcript and exact invocation were not
  supplied to this closing session; no invocation or usage metric is invented.
- Execution used Python 3.14; Python 3.9 was not run in this session. No
  dependency installation or network access was attempted.
- Structural checks do not establish whether a criterion is truly observable
  or a practice is appropriate. Profile card contents and links are not read.
- AIKM would need its own integrity-preserving adoption decision for the
  three refusals above. No consumer amendment is authorized by this Build.

### Learn Back candidate

Consumer gate adoption should begin with a pinned read-only probe: these
results show that historical section numbering can prevent adoption even
when the existing pin and dispatch gates pass. The consumer owns any amendment;
the orchestrator owns its pointer issue under decision 7. No shared procedure
or consumer document was changed for this candidate.

### Provenance

- Build round: `radiant-dev`, `standard`, Codex; adapter-resolved full model
  ID `gpt-6.1-sol` at entry `92bcf449ee538476748770edaac8757835650451`;
  Build return `DONE`, contract `ACTIVE`. Effective runtime model confirmation,
  context/round-volume counters and task duration are not exposed by this
  session's tool results, so those metrics are absent rather than inferred.
- First critique attempt: `radiant-verifier`, `deep`, Antigravity CLI,
  `claude-opus-5-5-high`; stopped on a quota limit before any verdict.
- Completed critique: `radiant-verifier`, `deep`, Antigravity CLI,
  `gemini-4-argon-high`; `VERDICT approve`, no Must-fix and no Should-fix.
  Provenance supplied by the owner. Exact CLI invocation, dispatch identifier,
  usage counters and duration were not supplied for either critique attempt.
- Orchestrator readback and acceptance: completed and reported by the owner
  on 2026-11-17; the orchestrator's harness, model and usage were not supplied.
- Applied bodies: `radiant-cycle` version `0.1.6` and `radiant-delegation`
  version `0.2.2`, both read from the entry revision; Conventional Commits
  skill applied to each commit. No subagent delegation occurred.

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

# 18. Owner decisions

Source of entries 1 to 7: the owner's message of 2026-11-17 at 14:56 BRT,
answering the seven questions of section 5: "Aceito recomendações." ("I
accept the recommendations"). Each entry is the recommended option (a) of the
question with the same number.

1. **`2026-11-17`:** Linked practice cells: option (a). Bare and backticked
   ids stay accepted, and a Markdown link whose text is the backticked id and
   whose target is a relative `.md` path ending in `<id>.md` is also
   accepted; the target is compared, never opened. **Contract impact:**
   section 7's practice cell rule, output 4 (`practice_ids` reads the linked
   form) and the `Practice cells` row of the section 5 decisions.
2. **`2026-11-17`:** Where the Profile comes from: option (a), an explicit
   `--profile <path>`; there is no `--project` option. **Contract impact:**
   output 2's command signature and section 7's Profile rule.
3. **`2026-11-17`:** Empty Engineering Check: option (a). Section 8 is
   refused when no row is `REQUIRED` or `APPLICABLE`; rows may be any subset
   of EB-01 to EB-08, so an all-`N/A` table is refused. **Contract impact:**
   section 7's empty Engineering Check rule.
4. **`2026-11-17`:** Minimum acceptance criteria: option (a). Section 12
   needs at least one checklist item that is neither a placeholder nor one of
   the template's four generic items. **Contract impact:** section 7's
   acceptance criteria rule.
5. **`2026-11-17`:** Gate adoption: option (a). Outside Radiant the command
   is opt-in; `check_repository.py` applies it only to Radiant's own
   contracts, and `check_project.py` and `check_dispatch.py` are unchanged.
   **Contract impact:** confirms the section 6 non-goal on those two
   validators, the `Consumer gates` row of the section 5 decisions and the
   section 14 FAIL condition on their output.
6. **`2026-11-17`:** Shape of an owner decision entry: option (a). From
   `Template version` `0.4`, section 18 must exist with a non-blank body,
   `None.` or entries, and the template's unedited entry with its bracketed
   date placeholder is refused; entry format is not validated. **Contract
   impact:** section 7's section 18 rule; checking entry format stays out of
   scope.
7. **`2026-11-17`:** Consumer probe: option (a). The Build runs
   `check_contract.py` read-only over Demerzel and AIKM contracts at the
   commits recorded in section 3 at activation and reports in section 16; the
   orchestrator, not the Build, opens any consumer pointer issue, with the
   owner's authorization. **Contract impact:** section 3's consumer input,
   section 11's consumer probe step, and the activation commit, which must
   record both consumer commits.

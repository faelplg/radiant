# Radiant Task Contract - Radiant - Practices / Spec and Engineering Profile

**Contract ID:** `TC-0003`\
**Project:** `radiant`\
**Iteration:** `Practices milestone, issue #33`\
**Status:** `READY` - the owner answered the planning questions on 2026-11-17; activation is a separate owner go\
**Owner:** `Fael (human); Build by an authorized agent`\
**Risk tier:** `2` - the pack declaration and the `check_project.py` change become part of the pin gate that every consumer, and Demerzel's dispatch, runs on its next pin bump\
**Capability:** `default`\
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`\
**Engineering Profile:** `none`\
**Entry commit:** `1a3595997df6d226300ecc324592d4254532cc36`\
**Tracking:** [issue #50](https://github.com/faelplg/radiant/issues/50), sub-issue of epic [#30](https://github.com/faelplg/radiant/issues/30)

The contract is ready, not active: the owner answered the planning questions
on 2026-11-17, as recorded in [Owner decisions](#owner-decisions-2026-11-17).
Activation is a separate go from the owner after this contract merges. A Build that starts from a later `main`
commit, such as the merge of this contract, records that commit as the entry
commit at activation; the Allowed scope does not change.

Routing: the Build runs as `radiant-dev` on the Codex harness at medium
effort; the independent critique runs on the agy harness, from a vendor
different from the Build's. Model IDs go only in the provenance lines of the
Completion report, as
[radiant-delegation](../../skills/radiant-delegation/SKILL.md#provenance)
requires.

## 1. Objective

> **Radiant has a Spec form, an Engineering Profile form and one stack pack (`typescript-bun`) under `engineering/stacks/`; a Profile declares at most one pack by id, `check_project.py` accepts a known id and refuses an unknown one, and a Demerzel example Profile kept in Radiant passes that check.**

## 2. Why this task exists

**Source plan/spec:**

- [Issue #33](https://github.com/faelplg/radiant/issues/33): scope and
  acceptance.
- [Plan](2026-11-16-lifecycle-and-practices.md#catalog-location): stack packs
  join the `engineering/` family next to the practice catalog; the
  [gap table](2026-11-16-lifecycle-and-practices.md#gap-artifacts-for-31)
  sends the concrete deploy checklist to the Engineering Profile.
- [Baseline section 11](../../engineering/engineering-baseline.md#11-engineering-profile-per-project):
  what a Profile may define, and that it must not copy the Baseline.
- [Thesis section 6.3](../project-generation-system.md#63-spec) and
  [section 24](../project-generation-system.md#engineering-profile): the Spec
  and the Profile are named artifacts without a form.
- [Lifecycle map](../lifecycle.md#deploy): the Requirements, Deployment and
  Operations rows point to forms this contract creates.

**Hypothesis or risk reduced:**

- The `engineering_profile` slot is `null` in Demerzel and AIKM because a
  project has to write every stack rule from scratch. A pack carries the
  rules shared by projects on the same stack, mapped to practice ids, so a
  Profile records only the project's own decisions and overrides.
- What would refute it: the Demerzel example Profile cannot stay shorter than
  the pack it selects without copying pack or Baseline text. The Build then
  stops on HOLD instead of shipping a Profile that duplicates them.

## 3. Inputs

The agent may assume as input:

- the documents in section 2, `docs/integration.md` (project map and
  revision policy), `templates/project-agents.md`, `templates/README.md`,
  `engineering/practices/` (the ids a pack may cite) and the
  [Constitution's order of precedence](../../constitution/CONSTITUTION.md#3-order-of-precedence);
- `validators/check_project.py` and `tests/test_integration.py` as the code
  and test style to follow;
- consumer evidence, read-only, from the owner's local checkouts of the
  consumer repositories. The contract does not carry their paths: the
  repository check refuses personal paths, and relative paths such as
  `../demerzel` do not resolve inside harness worktrees
  ([delegation package](../../skills/radiant-delegation/SKILL.md#delegation-package)).
  The Build request supplies the absolute root of each checkout and grants
  the sandbox read access to it. The Build reads each file at its commit with
  `git -C <checkout> show <commit>:<path>` and the layout with
  `git -C <checkout> ls-tree -r --name-only <commit>`, never from the working
  tree. The commits are:
  - `faelplg/demerzel` `8edd3b9d4028dc8fb8ad8a9e6ad9718e75bdaac0`:
    `package.json`, `tsconfig.json`, `.github/workflows/check.yml`,
    `AGENTS.md`, `src/` and `test/` layout, `docs/project/SPEC.md`, and
    `src/radiant/validators.ts`, whose pin gate parses the `PASS` line of
    `check_project.py`;
  - `faelplg/aikm` `a2cfd1bf6f415521567d0e48d8eebcc79a3e611d`:
    `package.json`, `biome.json`, `.github/workflows/check.yml`,
    `docs/project/SPEC.md`;

Planning found that AIKM is TypeScript on Bun at that commit (`package.json`,
`bun.lock`, `biome.json`, no `.py` file), although #33 lists it under Python.
Owner decision 1 records the consequence: AIKM is a `typescript-bun`
consumer, and no Python pack ships here.

Do not infer missing inputs that would materially change the solution.

## 4. Allowed scope

### Paths allowed to change

```text
engineering/stacks/
engineering/engineering-baseline.md
templates/spec.md
templates/engineering-profile.md
templates/README.md
templates/project-agents.md
docs/engineering-profile.example.md
docs/integration.md
docs/lifecycle.md
docs/project-generation-system.md
docs/capabilities.md
validators/check_project.py
validators/README.md
tests/test_integration.py
README.md
docs/plans/TC-0003-engineering-profile.md
```

`engineering/engineering-baseline.md` and `docs/project-generation-system.md`
take pointer sentences only; rule text and versions do not change.

### Paths read-only

```text
constitution/
engineering/practices/
templates/task-contract.md
templates/radiant-project.json
validators/check_repository.py
validators/practice_cards.py
validators/check_dispatch.py
validators/dispatch_formats.py
validators/radiant_yaml.py
tests/test_repository.py
tests/test_practice_cards.py
skills/
adapters/
contracts/
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

1. `engineering/stacks/README.md`: what a pack is, the id rule, how a Profile
   selects one, how it overrides a pack section, precedence, and an index
   table with one row per pack.
2. `engineering/stacks/typescript-bun.md`, in the pack format of the
   decisions below.
3. `templates/spec.md` and `templates/engineering-profile.md`, indexed in
   `templates/README.md`.
4. `docs/engineering-profile.example.md`: the Demerzel example Profile,
   selecting `typescript-bun`, with at least one real override.
5. `validators/check_project.py`: the pack check; tests in
   `tests/test_integration.py`.
6. Pointers: `docs/integration.md` (the `engineering_profile` field and the
   pack check), `docs/lifecycle.md` (the Requirements, Deployment and
   Operations rows and the "Deploy" section's checklist sentence), thesis
   sections 6.3 and 24, Baseline section 11, `templates/project-agents.md`
   (read the pack with the Profile), `validators/README.md`, `README.md`, and
   `docs/capabilities.md` (an index row and the paragraph after the table
   that names the Spec), plus the cross-links between packs, forms and the
   example that earlier tasks could not write.

Do not create additional artifacts without an observed need.

### Decisions

| Decision | Choice |
| --- | --- |
| Pack location | `engineering/stacks/`, next to `engineering/practices/` |
| Pack id | Lowercase kebab slug equal to the file stem, same pattern as practice ids; never renamed or reused |
| First pack | `typescript-bun` only, for Demerzel and AIKM |
| Pack sections | `Layering and dependency rule`, `Test layout and commands`, `Lint and format`, `Error handling`, `CI and release`, in that order and no others |
| Mapping to practices | Each section opens with a `- Serves:` line of at least one Markdown link, each to a practice card or a Baseline anchor; `Lint and format` and `Error handling` have no card today and may cite Baseline rules only |
| Declaration | Decided by the owner: one line in the Profile file: ``- Stack pack: `<id>` `` or ``- Stack pack: `none` ``; `.radiant.json` is unchanged |
| Number of packs | At most one per Profile |
| Override | A `Pack overrides` table in the Profile, one row per changed pack section, with the reason |
| Pack version | The Radiant pin; a pack has no version of its own |
| Project practices | A Profile section lists the project's own practice cards, written with the card form and kept in the consumer; their ids never reuse a catalog id |
| Pack structure check | None in this contract; a tracked follow-up issue adds it (owner decision 3) |
| Demerzel example | `docs/engineering-profile.example.md`, after the `docs/routing.example.json` precedent |

#### Where pack ids live

A pack is a shared body that consumers cite by id, like a practice card, so
it lives in `engineering/` and its id is its file stem. `check_project.py`
already runs from the Radiant checkout at the consumer's pin, so "known id"
means a pack file present at the pinned revision; no registry is needed. The
match is exact against the stems listed in `engineering/stacks/` except
`README.md`, never a path lookup: on a case-insensitive filesystem,
`readme.md` would otherwise resolve to the index.

`typescript-bun` names the runtime and package manager because a pack fixes
commands, and commands depend on them: `bun install --frozen-lockfile`,
`bun run check`. A TypeScript project on another runtime needs another pack,
not overrides of every command.

#### How a consumer declares a pack

Owner decision 2 settles it. The `engineering_profile` slot keeps its
meaning: a file path or `null`. The Profile file it points to carries the
pack line, and `.radiant.json` is unchanged. Reasons:

- the map stays a map of pointers and the pin, as
  [integration](../integration.md#project-map) defines it, and
  `templates/radiant-project.json` does not change, so a consumer's map stays
  valid across a pin bump;
- the stack is a Profile concern
  ([Baseline section 11](../../engineering/engineering-baseline.md#11-engineering-profile-per-project):
  "stack and conventions"), and the overrides sit next to the selection they
  modify;
- a project that wants only the pack writes a short Profile with the pack
  line and no overrides.

`check_project.py` reads the Profile only when `engineering_profile` is set
and the existing path checks pass. Outside fenced blocks:

- no `- Stack pack:` line, or the value `none`: no pack; accepted, so every
  existing Profile keeps passing;
- exactly one line, of the form ``- Stack pack: `<id>` ``, whose `<id>` is a
  pack stem: accepted, and the `PASS` line on stdout names the pack;
- anything else is `HOLD` on stderr naming `engineering_profile`: an unknown
  id, an id outside the pattern, empty backticks, a value without backticks,
  or a repeated line.

`none` is reserved and is never a pack id. The `PASS` output is unchanged
when no pack is declared. When a pack is declared, its name goes after the
existing text, and the line keeps its `PASS: Radiant <commit>;` prefix:
Demerzel's pin gate parses that prefix (`src/radiant/validators.ts`, the
`PASS` expression, at the commit in section 3).

`check_project.py` adds `engineering/stacks/README.md` to the files that make
a complete Radiant checkout, so a checkout without the packs fails as
incomplete instead of reporting every pack as unknown. A consumer pinned to an
earlier revision runs that revision's validator and is unaffected.

#### How a Profile overrides a pack

The `Pack overrides` table has the columns `Pack section`, `Override` and
`Reason`. A section without a row keeps the pack's rule. Precedence follows
the [Constitution](../../constitution/CONSTITUTION.md#3-order-of-precedence):
the Profile is a canonical project artifact and wins over the pack, a shared
body. Neither may lower a Baseline minimum; that needs the explicit human
decision of [Constitution section 2](../../constitution/CONSTITUTION.md#2-normative-language),
recorded with its reason. No validator reads the overrides in this contract.

#### Pack content

Every pack rule is grounded in the consumer evidence of section 3 or in a
practice card: commands are the consumers' real commands, such as
`bun run check` and `bun test`, not invented ones. When consumers
differ, the pack states the default and the reason, and the difference
becomes an override in that consumer's Profile. Demerzel has no linter while
AIKM uses Biome; if the pack defaults to Biome, the Demerzel example records
the override. Each pack header lists the consumers and commits it was
grounded in. Deploy and operations stay out of packs: they depend on the
environment, so the Profile form carries them, after the
[Deploy](../lifecycle.md#deploy) questions.

#### Forms

`templates/spec.md` follows thesis section 6.3 and the shape the Demerzel and
AIKM Specs share: concepts, behavior by area (rules, states, events,
invariants), interfaces, refusals and errors, security and egress,
non-functional requirements, acceptance and verification, out of scope, and
decisions. Engineering constraints point to the Profile instead of living in
the Spec.

`templates/engineering-profile.md` has a header with project, Radiant
revision, Baseline version and the `- Stack pack:` line, then the sections of
Baseline section 11 that a project fills: default risk, minimum quality per
kind of change, pack overrides, commands, test strategy beyond the pack,
dependency policy, security boundaries, UX requirements, compatibility and
performance, project practices, deploy checklist and operations. It states
that the Profile copies neither the Baseline nor the pack, and that a section
with nothing project-specific is removed.

The project practices section closes what
[TC-0001](TC-0001-practice-catalog.md#6-non-goals) deferred to #33: it lists
the project's own practice cards by id and link, written with
`templates/practice-card.md` and kept in the consumer. #34 validates contract
citations against the catalog and these ids; this contract does not.

### Build order

Each task is one commit; after each, all the automated checks of section 11
pass. A task links only to files that exist at its commit: a link from an
earlier file to a later one, such as from `engineering/stacks/README.md` to
the Profile form or the example, waits for task 5.

1. **Pack.** `engineering/stacks/README.md` and `typescript-bun.md`.
   Commit: `docs(stacks): add the TypeScript on Bun stack pack`.
2. **Validator, test-first.** In `tests/test_integration.py`, add
   `engineering` to the directories copied into the fixture, then the tests of
   section 11; run them and see the new ones fail; implement the check in
   `check_project.py`, standard library only; run them and see them pass;
   commit, then prove each refusal test by mutation. Commit:
   `feat(validators): check the stack pack an engineering profile declares`.
3. **Forms.** `templates/spec.md`, `templates/engineering-profile.md`,
   `templates/README.md`. Commit: `docs(templates): add Spec and Engineering Profile forms`.
4. **Demerzel example.** `docs/engineering-profile.example.md` and its
   integration test. Commit: `docs(profile): add the Demerzel example engineering profile`.
5. **Pointers.** The files of output 6. Commit:
   `docs: point to the profile forms and stack packs`.

New files are staged before the full test run: `tests/test_repository.py`
copies only `git ls-files` into its fixtures (learned in TC-0002).

## 6. Non-goals

This task must **not**:

- change any consumer repository, its `.radiant.json`, its pin (`9612a8c` in
  Demerzel and AIKM) or its `engineering_profile`; bumping a pin and adopting
  a Profile are separate human decisions;
- change the `.radiant.json` schema or `templates/radiant-project.json`;
- add a pack structure validator to `check_repository.py`. Follow-up, to be
  tracked in its own issue: `check_repository.py` checks each pack's id,
  sections and `Serves` links and matches the pack files with the index rows
  in both directions, as it does for practice cards;
- validate Profile sections, override rows or Spec content;
- validate practice ids in consumer contracts or project practice ids (#34);
- add a Python pack. Follow-up, for when a Python project, for example
  omr-ingestor, adopts Radiant: a pack grounded in that project's evidence;
- add packs for other stacks, or allow several packs per Profile;
- edit the Constitution, the Task Contract template, practice cards, skills
  or adapters;
- update the living pages in `faelplg/design-systems` (separate issue).

Finding an improvement outside this scope does not authorize implementing it.

Record it as an observation or a Learn Back candidate.

# 7. Functional requirements

- [ ] A Profile with ``- Stack pack: `typescript-bun` `` passes `check_project.py`, and the `PASS` line on stdout keeps its `PASS: Radiant <commit>;` prefix and names the pack.
- [ ] A Profile without the line, or with `none`, passes with the current output.
- [ ] `no-such-pack`, `README`, `readme`, `../templates/spec`, empty backticks, a value without backticks and two `Stack pack` lines each produce `HOLD` on stderr naming `engineering_profile`, with exit 1.
- [ ] A `- Stack pack:` line inside a fenced block is ignored.
- [ ] `engineering_profile: null` never reads a pack.
- [ ] A Radiant checkout without `engineering/stacks/README.md` produces `HOLD: incomplete Radiant checkout`.
- [ ] The Demerzel example Profile, copied into a fixture project, passes `check_project.py`.
- [ ] Each pack has the five sections in order, each opening with a `- Serves:` line of at least one link, each resolving to a practice card or a Baseline anchor.

# 8. Engineering Check

| Baseline                          | Status           | Application in this task | Evidence          |
| --------------------------------- | ---------------- | ------------------------ | ----------------- |
| EB-01 Deliberate complexity       | `REQUIRED`       | One line in the Profile, no schema change, no registry, one pack per Profile; one pack, for the only stack with Radiant consumers | Diff review against section 5 decisions |
| EB-02 Correctness and contracts   | `REQUIRED`       | Exact stem match; backward compatible with Profiles without a pack | Tests in `tests/test_integration.py` |
| EB-03 Verification and tests      | `REQUIRED`       | Test-first, accept and reject cases, mutation proof | Commands in section 11 |
| EB-04 Security and privacy        | `REQUIRED`       | The id never becomes a path; no read outside the Radiant root and the Profile | Refusal tests for `../templates/spec` and `readme` |
| EB-05 Maintainability             | `REQUIRED`       | Packs and Profile point to the Baseline and cards instead of copying them | Review and focused script |
| EB-06 Dependencies                | `REQUIRED`       | Standard library only | Diff review |
| EB-07 Diagnosis                   | `REQUIRED`       | Each `HOLD` names `engineering_profile` and the reason; `PASS` names the pack | stderr assertions for `HOLD`, stdout assertions for `PASS` |
| EB-08 Experience and efficiency   | `APPLICABLE`     | A consumer reaches the pack, the form and the example from `README.md` in one pass | Readback |

### Practices

| Practice | Serves | Why it applies here | Evidence |
| --- | --- | --- | --- |
| `tdd` | EB-03 | The accept and reject results are known before coding | Failing run before the check exists, in the Completion report |
| `test-strategy` | EB-03 | The check is proven at the CLI boundary, as the existing `check_project.py` tests do | `tests/test_integration.py` |

# 9. Project-specific constraints

Taken from `AGENTS.md` and the plan's global constraints:

- Python 3.9+, standard library only; no `match`, no `X | Y` types.
- English, plain hyphen, no em or en dash, no horizontal dividers in new text.
- `check_project.py` stays read-only and keeps its `HOLD` and exit 1 contract.
- No absolute personal path in any Markdown file; the repository check
  refuses them.

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

- The new tests in `tests/test_integration.py` cover every item of section 7
  that names `check_project.py`, through the CLI as the existing tests do.
- The accept-with-pack test asserts exit 0 and that stdout has a line
  starting `PASS: Radiant <commit>;` that names the pack id. The fenced-block
  test puts ``- Stack pack: `no-such-pack` `` inside a fence and a valid line
  outside it, so reading the fence would refuse the Profile.
- Before the check exists, the accept-with-pack test and the refusal tests
  fail; the tests that expect today's behavior (no line, `none`, `null`,
  fenced line) pass. The Completion report shows that run.
- After the validator commit, mutate `check_project.py` one rule at a time:
  each refusal rule, the pack name in `PASS`, the fence stripping and the new
  required file. Observe the named test fail, restore with
  `git checkout -- validators/check_project.py` and confirm the suite passes
  before the next mutation. Gate each step on the command's exit code.
- A one-off script, kept outside the repository, prints every pack whose `##`
  sections differ from the five of section 5 and every section without a
  `- Serves:` line linking a practice card or a Baseline anchor, every pack
  file without an index row in `engineering/stacks/README.md` and every row
  without a pack file; it also prints every `Pack overrides` row of the
  Demerzel example whose section is not a pack section. Expected: no output.
  Until the follow-up issue of section 6 lands, this script is the only
  structural check of packs. Command, body and output go into
  the Completion report.
- Each command a pack names is found in the cited consumer file at the cited
  commit; the Completion report lists command, file and line.

## Readback

After execution:

- reopen both packs, both forms, the example and each pointer;
- confirm that the example Profile copies no Baseline or pack paragraph;
- confirm that no path outside the Allowed scope changed, against the entry
  commit, including committed, staged, unstaged and untracked changes
  (`git diff --name-only <entry>..HEAD` and `git status --porcelain`);
- confirm that the consumer checkouts are unchanged: record
  `git -C <checkout> rev-parse HEAD` and `git -C <checkout> status --porcelain`
  for each before the first task and again at the end, and report both. The
  two records must match; neither is assumed to be empty.

## Independent critique

`REQUIRED`

- `radiant-verifier` at `deep`, from a vendor different from the Build's,
  against this contract, issue #33's acceptance and the consumer evidence of
  section 3.
- Launched and collected by the orchestrator, never by the Build. The
  orchestrator records the harness, the full model ID and the command in the
  Completion report's provenance.
- External prerequisites: the agy harness installed and authenticated on the
  owner's machine. Radiant has no agy adapter yet (#29), so the orchestrator
  resolves the `deep` model for it.

# 12. Acceptance criteria

The task can only be declared `DONE` when:

- [ ] `check_project.py` accepts a project whose Profile declares a pack and refuses an unknown pack id (issue #33);
- [ ] the Demerzel example Profile passes `check_project.py` (issue #33);
- [ ] the Spec form and the Engineering Profile form exist and are indexed in `templates/README.md`, and the Profile form covers the sections listed in section 5 (issue #33; Baseline section 11);
- [ ] `typescript-bun` covers layering and dependency rule, test layout and commands, lint and format, error handling, and CI and release, each section mapped to practice ids or Baseline rules (issue #33; the Python pack is deferred by owner decision 1);
- [ ] `engineering/stacks/README.md` says how a project selects and overrides a pack (issue #33);
- [ ] no consumer repository and no `.radiant.json` schema changed;
- [ ] all applicable checks in section 11 pass;
- [ ] there was no change outside the Allowed scope;
- [ ] relevant limitations are recorded;
- [ ] the final evidence was read, not just presumed from the exit code.

# 13. HOLD conditions

Stop and ask for a decision when:

- a Build finding contradicts an [owner decision](#owner-decisions-2026-11-17);
- a pack rule can be grounded neither in the consumer evidence of section 3
  nor in a practice card;
- the Demerzel example cannot avoid copying pack or Baseline text;
- the check needs a `.radiant.json` field, a change to
  `templates/radiant-project.json` or a dependency;
- the agent would need to write outside the authorized paths, including any
  consumer checkout;
- the minimal solution no longer fits the contract.

`HOLD` is a valid result.

# 14. FAIL conditions

Mark `FAIL` when:

- acceptance criteria cannot be met;
- verification shows a material regression in the existing checks;
- an existing Profile without a pack line would stop passing
  `check_project.py`;
- an external blocker makes the goal impossible within this contract.

Do not disguise `FAIL` as `DONE WITH NOTES`.

# 15. Change budget

The agent may:

- update directly affected pointers, indexes and the fixture setup in
  `tests/test_integration.py`.

The agent may not, without HOLD:

- refactor `check_project.py` beyond the pack check;
- reword sections of the thesis, the Baseline or the lifecycle map beyond the
  pointers;
- add forms, packs or validators that were not requested.

# 16. Completion report

Filled by the Build in the format of
[the template](../../templates/task-contract.md#16-completion-report).

# 17. Completion rule

> **Do not declare DONE because the code looks right. Declare DONE only when the observable criteria, the applicable engineering and the verification evidence converge.**

## Owner decisions (2026-11-17)

The owner answered the three planning questions on 2026-11-17:

1. **Python pack.** Not in this contract. Only `typescript-bun` ships, for
   Demerzel and AIKM; a Python pack is a follow-up for when a Python project
   adopts Radiant (section 6).
2. **Where the declaration lives.** A `- Stack pack:` line in the Profile
   file; `.radiant.json` and `templates/radiant-project.json` are unchanged.
3. **Pack structure validator.** Not in this contract; the follow-up issue
   described in section 6 adds the `check_repository.py` rule.

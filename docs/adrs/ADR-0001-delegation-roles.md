# ADR-0001: roles, capabilities and delegation

- Date: 2026-10-08
- State: `accepted` on 2026-10-09
- Owner: Fael
- Originating Radiant revision: `160ef8edddd5893169e5c9d9d5375dd25be802b3`
- Implementation: PR #2, merge `6074810e6d3ca3cc8f591b78d62272b26b6428a9`

The operational rules live in
[radiant-delegation](../../skills/radiant-delegation/SKILL.md),
[radiant-maintenance](../../skills/radiant-maintenance/SKILL.md) and the
adapters. When they diverge, those bodies prevail; this ADR remains as the
record of the decision and of the design that guided the implementation.

## Intent

Allow projects carried out with Radiant to be handled by specialized roles
(Ideation, Design, Dev, Verifier and Maintenance) coordinated by an
orchestrator, with human approval between phases, without tying Radiant to a
harness or model.

Two outcomes are expected:

1. Radiant explicitly harness-agnostic: the same core is consumed by two
   adapters that actually delegate (Codex and Claude Code).
2. Cost proportional to the work: the orchestrator uses the highest capability
   and bounded work is delegated to cheaper capabilities, without weakening
   critique and verification.

## Context and constraints

- The cycle Frame → Challenge → Spec → Design → Plan → Contract → Build →
  Verify → Learn Back already covers Ideation, Design and Dev. Continuous
  maintenance has no corresponding stage.
- The [Constitution](../../constitution/CONSTITUTION.md) requires: a
  tool-independent core (Article XIV), one canonical body (Article XI),
  autonomy proportional to reversibility (Article IV), independent
  verification and critique (Articles VII and VIII), human agency
  (Article XIII), default deny for egress (Article XII), provenance
  (Article X) and simplicity (Article XVII). Model names do not belong in the
  core (section 7).
- Only the [Codex adapter](../../adapters/codex/README.md) exists. The
  consumer template and AIKM's `AGENTS.md` point directly to it.
- External skills (for example superpowers and design-superpowers) produce
  artifacts at their own paths, competing with Radiant's.
- Harness facts checked in the official documentation on 2026-10-09:
  - Claude Code: subagents in Markdown with frontmatter in `~/.claude/agents/`;
    the frontmatter `model` accepts a full ID. The invocation's `model`
    parameter wins over the frontmatter, but only accepts family aliases
    (`sonnet`, `opus`, `haiku`, `fable`), which do not identify the effective
    model. Subagents can create subagents up to three layers below the main
    session; creation is blocked per agent with `disallowedTools: Agent`.
  - Codex: subagents in TOML in `~/.codex/agents/`, with `name`,
    `description` and `developer_instructions` required and `model` optional.
    The `model` declared in the agent's file wins over the value passed at
    creation. There is no documented depth limit.
- The [Task Contract template](../../templates/task-contract.md) already has
  `Risk tier`, `Independent critique` and `Completion report`, reused by this
  decision.

## Decisions

| Decision | Choice |
| --- | --- |
| Where the roles live | Agnostic core; adapters translate for each harness |
| Name of the concept | Capability (`deep`, `standard`, `light`); `Capability` field in the contract |
| Choosing the capability | Default per role, with a justified override in the Task Contract |
| Independent acceptance | Once per contract in `deep`; brought forward when `Risk tier` ≥ 2 or `Independent critique: REQUIRED` |
| Model provenance | Adapters map capability to a full model ID, not an alias |
| External skills | Radiant is canonical; external skills are optional procedures the adapter points to |
| Maintenance autonomy | Only proposes; the only write is the report, in a directory ignored by Git |
| Maintenance execution | Local only; cloud routines out of scope |
| Maintenance policy | Safe commands and authorized egress declared in the consumer's workflow |
| Structure in the core | Skills `radiant-delegation` and `radiant-maintenance`; `radiant-cycle` only gets pointers |
| Adapters | New Claude Code and complete Codex, both generating the six subagents |
| Pilot | AIKM: adoption as TC-0019; cycle of the Maintenance candidate as TC-0020 |

Discarded alternatives:

- Roles only in the adapter: ties roles to a harness.
- Roles outside Radiant: no Learn Back or pin.
- Fixed capability per role: rigid for hard tasks.
- Capability decided case by case by the orchestrator: unpredictable and
  without provenance.
- Everything inside `radiant-cycle`: the skill everyone loads grows without
  need.
- One skill per team: duplicates the cycle procedure.
- `deep` acceptance per task: cancels the savings of delegating Build.
- Model aliases: the evidence stops identifying the effective model.
- Maintenance report versioned or published to the forge: conflicts with work
  in progress or requires external writes and egress.
- Maintenance policy in `.radiant.json` fields: turns the path map into a
  policy file.
- Minimal Codex adapter: leaves the core/adapter separation without a real
  test.
- The term `tier`: collides with the `Risk tier` of existing contracts.

## 1. Roles and capabilities

### Capabilities

The core defines abstract capabilities. Each adapter maps capabilities to full
model IDs.

| Capability | Use |
| --- | --- |
| `deep` | Judgment, critique, expensive decisions and acceptance |
| `standard` | Execution bounded by an approved artifact |
| `light` | Search, collection, mechanical checks and summaries |

### Roles

| Role | Stages | Default capability | Produces |
| --- | --- | --- | --- |
| Orchestrator | Coordination of all | `deep` | Delegation packages, gate decisions, final acceptance |
| Ideation | Frame, Challenge | `deep` for Grill; `light` for research | Recorded Frame and Challenge |
| Design | Spec, Design | `deep` for System Design and ADR; `standard` for a Design Spec derived from an approved Frame | Spec, Design Frame, Design Spec, ADRs |
| Dev | Plan, Contract, Build | `standard`; `light` for mechanical tasks | Plan, proposed contracts, diff |
| Verifier | Verify | `deep` for acceptance; `light` for deterministic checks | Verification report |
| Maintenance | Outside the cycle; feeds the Frame | `light` for collection; `standard` for prioritization | Maintenance report with proposals |

### Rules

1. Human interaction belongs to the orchestrator. Delegated roles do not talk
   with the human; framing questions, Challenge and approvals go through the
   main session.
2. Acceptance never uses a capability lower than the author's. Per task,
   deterministic checks and the `deep` orchestrator's readback apply. The
   dedicated `deep` Verifier accepts the contract once, at the end, and is
   brought forward when `Risk tier` ≥ 2 or `Independent critique: REQUIRED`.
3. Capability override only through the Task Contract, in an optional
   `Capability` field with a one-line justification, recorded in the
   execution evidence.
4. Not delegated: scope changes, contract activation, irreversible actions and
   acceptance of canonical knowledge.
5. Delegating is optional. Without harness support, or in a small task, the
   orchestrator runs the role in its own session with the same inputs and
   outputs. The same applies when the harness does not allow the requested
   override.
6. Orchestrator exception: in a Maintenance run, which only proposes, the
   orchestrator may operate in `standard`.
7. Delegated roles do not delegate. Every delegation starts from the
   orchestrator, so each one is recorded in the cost provenance and respects
   the acceptance rule.

## 2. Handoff and return

### Delegation package

Holds pointers, not copies:

- role and effective capability;
- goal in one or two sentences;
- inputs: artifact paths and the Radiant revision;
- boundary: writable paths, read-only paths and non-goals;
- expected output and return format;
- `HOLD` conditions.

For Build, the Task Contract is the package; the handoff points to it. For
small jobs (research, Grill, collection), the package goes in the request
itself and does not become a file.

### Return

For Build, the return is the Task Contract's `Completion report`. For the
other roles, the return holds:

- state: `DONE`, `HOLD` or `FAIL`;
- outputs: paths created or changed;
- evidence: commands and results actually obtained, including blockers;
- deviations: ambiguities and what stayed outside the boundary;
- findings that are candidates for Learn Back.

The return is a summary, not a content dump.

### Handling by the orchestrator

1. It does not accept `DONE` on the account alone. It reads back the diff,
   runs checks and compares with the contract.
2. `HOLD` is resolved within the current authorization or taken to the human.
3. `FAIL` preserves evidence and goes to Learn Back.

### Parallelism

Only between independent tasks with disjoint write paths. When in doubt, run
sequentially.

### Cost provenance

The contract's verification report records each delegation: role, capability,
full model ID resolved by the adapter and state. Model IDs appear only in the
consumer's evidence and in the adapters.

## 3. Maintenance

### Observed sources

| Source | Typical candidates |
| --- | --- |
| Cycle state | A forgotten `held` contract; a Learning Record with a `fixTarget` and no fix |
| Project gates | Failures in the commands declared safe for maintenance |
| Drift | Spec or Plan in disagreement with the code; broken links in the artifacts |
| Dependencies | Outdated or vulnerable versions |
| Forge | Open issues; CI failures on the main branch |
| Radiant pin | A newer available revision, as a candidate and never as an automatic update |

### Policy declared by the consumer

The consumer's `workflow` document holds a Maintenance section with:

- commands safe for maintenance: only these run; the others are skipped and
  recorded as omitted;
- authorized external sources (package registry, forge): without
  authorization, the source is skipped and the omission is recorded.

### Report

A run produces a report, following `templates/maintenance-report.md`, with:

- candidates prioritized by risk, value and reversibility, each with concrete
  evidence (command output, path, line);
- comparison with the previous report: new, recurring, resolved;
- an embedded contract draft for up to three candidates at the top (goal,
  outputs, verification).

Drafts do not become `TC-xxxx` files. The contract with an ID is created by
the orchestrator only when the human selects a candidate. A run that
concludes "nothing material" is a valid result.

### Location and boundary

- New optional `maintenance` field in `.radiant.json`: a relative directory or
  `null`. A missing field is the same as `null`.
- The directory is ignored by Git in the consumer. The validator only requires
  a relative path inside the project and accepts that it does not exist; the
  skill creates it on the first run. The exception applies only to this field.
- The only write allowed is the report. No branch, PR, issue or commit.
- Local execution only, manual or scheduled on the user's machine.

## 4. Adapters

### Common to the adapters

- A single generator: the current script starts accepting
  `--adapter codex|claude-code`, with templates per adapter. The existing
  Codex output stays compatible.
- Six thin subagents, generated in the user's agents directory, outside Git,
  regenerable and without overwriting existing files: `radiant-research`
  (`light`), `radiant-grill` (`deep`), `radiant-design` (`standard`),
  `radiant-dev` (`standard`), `radiant-verifier` (`deep`) and
  `radiant-maintenance` (`standard`). The body holds only harness metadata and
  a pointer to the role's section in `radiant-delegation`.
- A single capability → full model ID map in each adapter's
  `capabilities.json`, referenced by the README.
- An optional role → suggested external procedure table. Explicit rule: the
  output goes to the paths in `.radiant.json`, never to the external skill's
  default paths.

### Claude Code (new, `adapters/claude-code/`)

- Global bootstrap: a `radiant:begin/end` block for the user's global
  instructions file, preserving the rest and removable on its own.
- Subagents in Markdown with frontmatter, in the user's agents directory, with
  `disallowedTools: Agent` to enforce rule 7.
- Capability override does not use the invocation's `model` parameter, which
  only accepts aliases: the role with a changed capability runs in the
  orchestrator's session (rule 5), as in Codex.

### Codex (`adapters/codex/`)

- Keeps the current bootstrap.
- Subagents in TOML in the user's agents directory. Rule 7 lives in the
  agent's instructions, because Codex does not document per-agent blocking.
- Since the file's `model` wins, capability override is not possible at
  creation: the role with a changed capability runs in the orchestrator's
  session (rule 5).

### Consumers

- The consumer's `AGENTS.md` template leaves `adapters/codex/` and becomes a
  neutral harness map in `templates/`, which says to read the adapter of the
  harness in use.
- Consumers that use Claude Code have a one-line `CLAUDE.md` with
  `@AGENTS.md`, keeping a single body.
- Radiant itself gets the same one-line `CLAUDE.md`.

## 5. Verification and pilot

### Deterministic verification in Radiant

- Generator tests with each adapter: global block, six subagents, refusal to
  overwrite and a path with spaces.
- Regression: the Codex global block equal to the current one, except for
  intentional changes.
- `check_project.py`: `maintenance` with `null`, an existing directory, a
  nonexistent directory (accepted), a path that escapes the project (rejected)
  and a missing field (accepted).
- `check_repository.py`: every adapter maps the three capabilities defined in
  `radiant-delegation`.
- [Verification](../verification.md): simulation D (entry through Claude Code)
  and the harness agnosticism criterion in the structural review.

### Pilot in AIKM

| Stage | Action | Evidence |
| --- | --- | --- |
| 0. Adoption (TC-0019) | Pin at the merge commit, neutral `AGENTS.md`, one-line `CLAUDE.md`, `maintenance` field, `.gitignore` and a Maintenance section in the workflow | `check_project.py` passes |
| 1. New session | A new Claude Code session identifies the pointer, validates the pin and loads the Constitution and map without help | Transcript |
| 2. Maintenance | Manual run, then one scheduled locally | Report with evidence; `git status` without tracked changes |
| 3. Cycle (TC-0020) | The human selects a candidate from the report or, without a material candidate, an item from the Plan's horizon; TC-0020 goes through the roles to `DONE` | Verification report with recorded delegations |
| 4. Learn Back | Findings about Radiant routed to the owner | Learning Record and a change or open item |
| 5. Codex regression | The human confirms that a Codex session in AIKM still validates and delegates to a Radiant subagent | Recorded confirmation |

### Success criteria

- Stages 1 to 5 completed without intervention outside the planned gates.
- No acceptance with a capability lower than the author's.
- Usage split by capability recorded as a baseline. There is no numeric target
  in this pilot; per-subagent measurement limitations are recorded.

### Delivery order

1. PR in Radiant: core, adapters, validators and this ADR.
2. Merge into `main`; the ADR becomes `accepted` with a reference to the
   commit.
3. PR in AIKM: TC-0019 with the pin at the merge commit, followed by the
   TC-0020 cycle.

## Limitation recorded in the PR review

Delegable profiles declare `access` (`read` or `write`). Read profiles get the
harness's least privilege (restricted `tools` in Claude Code,
`sandbox_mode = "read-only"` in Codex). Each contract's specific boundaries on
`write` profiles are not enforced by the harness: they depend on the package
and on the orchestrator's readback, according to the "Access and boundaries"
section of the delegation skill. Per-contract enforcement is a candidate for
evolution with evidence from the pilot.

## Amendments

- 2026-10-09: the global block becomes a single neutral template,
  `adapters/global.template.md`, that names each harness's adapter. Reason: in
  the first real use, the global instructions of Claude Code and Codex were
  the same file (dotfiles), and one block per adapter made one harness read
  the other's adapter. The generator prints the block without `--adapter`,
  which becomes required only with `--agents-dir`.
- 2026-10-10: the pilot's Learn Back changed operational rules in the skills
  and adapters, which prevail over this record
  ([PR #5](https://github.com/faelplg/radiant/pull/5) and
  [PR #6](https://github.com/faelplg/radiant/pull/6)). The Build return
  follows section 16 of the template even when the contract does not
  reproduce it. The readback checks each reported change and each reported
  result against the working tree. The package carries the absolute Radiant
  root. The provenance records one line per round with the usage metric
  defined by the adapter, or its absence. So the "Cost provenance" section
  above holds with these additions.
- 2026-10-13: resolves the first open item of the pilot result. The pilot's
  task was created by a scheduling tool, which sets no model, and ran on the
  default model. A scheduled run now pins the `standard` model in the
  scheduler and records the session's effective model in the report; below
  `standard`, it ends in `HOLD`. The rule is in the
  [maintenance skill](../../skills/radiant-maintenance/SKILL.md) 0.1.2 and the
  [template](../../templates/maintenance-report.md), and the scheduling
  mechanisms, in the
  [Claude Code adapter](../../adapters/claude-code/README.md#maintenance).
  Usage evidence: AIKM's maintenance on 2026-10-13, run on demand by the app's
  task with AIKM at `6800f5a591793d82f573ae061008a670236c05d4` and Radiant
  pinned at `9581aa988cf5b6483bc0a3d276f5451275cffef2`, recorded the session
  on `claude-sonnet-5-5`, without deviation.
- 2026-10-13: closes the other two open items with AIKM's TC-0024
  ([AIKM PR #29](https://github.com/faelplg/aikm/pull/29), merge
  `c113e53215f8dfebf902c25ed7d6121509ca2003`; contract closed at
  `0218852d94539ab6ac51cf23334bb4bdac453bd5`), run by Codex with the main
  session in `deep` and Radiant pinned at
  `9581aa988cf5b6483bc0a3d276f5451275cffef2`.
  - Build by Codex: three `radiant-dev` rounds in `standard`, plus one
    `radiant-verifier` round in `deep`, each with the Codex adapter's metric.
  - Per-contract boundaries: the four rounds recorded zero writes outside the
    writable paths, checked by readback of the diff, staged and untracked
    files and temporary directories. This evidence does not justify
    enforcement in the harness; the readback remains the mechanism, and
    enforcement becomes a candidate again if a round records a violation.
  - The contract's C3 required proof of native discovery that Antigravity does
    not show. The owner approved a criterion amendment in the contract itself,
    the third intervention outside the gates after the pilot's two. The
    [contract template](../../templates/task-contract.md) now asks that each
    criterion's evidence be confirmed as observable before activation.
  - The Codex adapter now says that the main session runs in `deep` and that a
    round's model is checked in the turns after `thread_settings_applied`. The
    [maintenance skill](../../skills/radiant-maintenance/SKILL.md) 0.1.3 now
    reads the new Radiant revision from the local refs, querying the remote
    only with authorized egress, and skips improvised diagnosis, findings from
    the same maintenance.

## Pilot result

Recorded on 2026-10-10, with AIKM at
`31266c690e5b5cf84d2e576a0c73ee93caaa286e` and Radiant pinned at
`6ad7ad260ab4464023a7eea798530ad85d284faf`.

| Stage | Evidence | Status |
| --- | --- | --- |
| 0. Adoption | TC-0019, [AIKM PR #13](https://github.com/faelplg/aikm/pull/13) | Completed |
| 1. New session | Claude Code and Codex sessions opened by the owner located and validated the core without help (TC-0019 report) | Completed |
| 2. Maintenance | Manual run on 2026-10-09 and a locally scheduled run on 2026-10-10, with `radiant-maintenance` 0.1.1 ([PR #8](https://github.com/faelplg/radiant/pull/8)); reports with evidence and a clean `git status` | Completed, with a deviation: the scheduled session ran in `deep`, not `standard` |
| 3. Cycle | TC-0020, [AIKM PR #14](https://github.com/faelplg/aikm/pull/14), with Build, verification and research delegated; TC-0021 and TC-0022 repeated the cycle | Completed |
| 4. Learn Back | AIKM's LR-0002, [AIKM PR #17](https://github.com/faelplg/aikm/pull/17), and [PR #5](https://github.com/faelplg/radiant/pull/5) | Completed |
| 5. Codex regression | AIKM's VR-0006, [AIKM PR #18](https://github.com/faelplg/aikm/pull/18): gate and one read-only delegation; metric in [PR #6](https://github.com/faelplg/radiant/pull/6) | Completed, without a Build by Codex |

Success criteria: partially met. The stages were completed, but not without
intervention outside the planned gates, and the scheduled Maintenance session
ran on a capability different from the one requested.

- Intervention outside the gates: not met. There were two, both owner
  decisions recorded in the consumer. One clarified the reach of "error
  messages" in TC-0020, after closing. The other waived an infeasible
  criterion in TC-0022 (amendment A3). Both motivated the referent rule for
  criteria in the template.
- Acceptance with a capability lower than the author's: none. `standard`
  Builds were accepted by a `deep` verifier or by the `deep` orchestrator with
  the owner.
- Usage baseline: recorded per round in the consumer's reports. In Claude
  Code, `standard` Build rounds were between 87 thousand and 112 thousand
  tokens of context, and `deep` verification rounds between 122 thousand and
  165 thousand; the `light` research was about 46 thousand. In Codex, the
  `light` round had 72 thousand of context and 303 thousand accumulated. The
  two harnesses' metrics are not directly comparable, and neither is billed
  cost.

In the scheduled run, the comparison with the previous report kept the IDs of
the pending candidates, including those from addenda, and did not mark as
resolved a candidate whose target did not change. The session's model comes
from the scheduled task, not from the adapter; the run recorded the effective
model and the deviation.

Open items recorded in this result: define how a scheduled run uses the
`standard` capability; a Build delegated by Codex; and the evidence for
per-contract boundary enforcement, foreseen in the limitation recorded above,
which the pilot did not produce. All three were closed on 2026-10-13,
according to the [Amendments](#amendments). Per-contract enforcement only
becomes a candidate again if a round records a write outside the writable
paths.

## Out of scope

- Automatic execution of fixes by Maintenance.
- Maintenance routines in the cloud.
- External board (GitHub Projects, Notion); the state stays in the consumer's
  artifacts and in `ACTIVE.md`.
- Adapters for harnesses other than Claude Code and Codex.
- Numeric cost targets.
- Changes to the Constitution. If the pilot shows a new invariant, it follows
  the constitutional proposal flow.

## Planned files

| Action | Path |
| --- | --- |
| Create | `skills/radiant-delegation/SKILL.md` |
| Create | `skills/radiant-maintenance/SKILL.md` |
| Create | `templates/maintenance-report.md` |
| Create | `adapters/claude-code/README.md`, global template and subagent template |
| Create | TOML subagent template in `adapters/codex/` |
| Create | `CLAUDE.md` at the Radiant root |
| Change | `skills/radiant-cycle/SKILL.md` (pointers) |
| Change | `adapters/codex/README.md` and generator (`--adapter`, subagents, capabilities) |
| Change | `templates/task-contract.md` (`Capability` field), `templates/radiant-project.json` (`maintenance`) |
| Move | `adapters/codex/project.AGENTS.template.md` to `templates/project-agents.md`, as a neutral harness map |
| Change | `docs/capabilities.md`, `docs/integration.md`, `docs/verification.md`, `docs/learn-back.md`, `README.md`, `AGENTS.md` |
| Change | `validators/check_project.py`, `validators/check_repository.py`, `tests/test_integration.py` |

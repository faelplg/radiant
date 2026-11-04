---
name: radiant-delegation
description:
  Coordinate the roles of a Radiant cycle and delegate bounded work to
  subagents with the right capability. Use when orchestrating Ideation,
  Design, Dev, Verification or Maintenance, when assembling a delegation
  package or when evaluating the return of a delegated role.
metadata:
  version: "0.2.2"
---

# Radiant delegation and roles

This skill defines how the orchestrator distributes the
[cycle](../radiant-cycle/SKILL.md) across roles. The
[Constitution](../../constitution/CONSTITUTION.md) remains higher; contracts
follow the [template](../../templates/task-contract.md) and the
[convention](../../contracts/README.md). The delegable profiles, machine
readable, are in [agents.json](agents.json). Concrete models belong to the
adapters; this skill only talks about capabilities. The decision that gave
rise to this skill is in [ADR-0001](../../docs/adrs/ADR-0001-delegation-roles.md).

## Capabilities

| Capability | Use |
| --- | --- |
| `deep` | Judgment, critique, expensive decisions and acceptance |
| `standard` | Execution bounded by an approved artifact |
| `light` | Search, collection, mechanical checks and summaries |

Each adapter maps the three capabilities to full model IDs and declares how
its harness delegates.

## Roles

### Orchestrator

Main session, in `deep`. Talks with the human, frames the request through the
cycle, chooses what to delegate, assembles packages, applies gates and makes
the final acceptance. Keeps for itself: scope changes, contract activation,
irreversible actions and acceptance of canonical knowledge.

### Ideation

Frame and Challenge stages. Framing is carried out by the orchestrator with
the human, because it requires conversation. Delegable: research in `light`
(`radiant-research`), which returns inspected sources and what each one
supports, and adversarial critique in `deep` (`radiant-grill`), which attacks
the assumptions, scope and irreversibility of an existing Frame or Spec and
returns objections with evidence. Neither decides intent or scope.

### Design

Spec and Design stages, in both tracks of the
[Design Layer](../../docs/design-layer.md). System Design and ADRs in `deep`;
a Design Spec derived from an approved Frame and Design Frame in `standard`
(`radiant-design`). Produces Spec, Design Frame, Design Spec and ADRs as
proposals; approval is human, mediated by the orchestrator.

### Dev

Plan, Contract and Build stages. The orchestrator proposes the Plan and
contracts; the Build of an active contract is delegated in `standard`
(`radiant-dev`), and mechanical tasks may use `light`. The contract is the
package and its `Completion report` is the return.

### Verifier

Verify stage, in `deep` (`radiant-verifier`). Checks outputs against the
contract, Spec and criteria, runs the gates and inspects the result as a
consumer. Deterministic checks may run in `light`. It does not fix what it
verifies: it returns findings with evidence. In a round after fixes, the
package points to the previous round's return, and the verifier confirms each
fix before looking for new findings. If the verifier's harness becomes
unavailable, the human chooses another one, different from the one that did
the Build.

### Maintenance

Outside the delivery cycle; feeds the Frame with proposals. Collection in
`light`, prioritization and drafts in `standard` (`radiant-maintenance`). It
only proposes. The procedure is in the
[maintenance skill](../radiant-maintenance/SKILL.md).

## Rules

1. Human interaction belongs to the orchestrator. Delegated roles do not talk
   with the human.
2. Acceptance never uses a capability lower than the author's. Per task,
   deterministic checks and the orchestrator's readback apply. The Verifier
   accepts the contract once, at the end, and is brought forward when
   `Risk tier` ≥ 2 or `Independent critique: REQUIRED`.
3. A role's default capability only changes through the Task Contract's
   `Capability` field, with a one-line justification recorded in the evidence.
4. Not delegated: scope changes, contract activation, irreversible actions and
   acceptance of canonical knowledge.
5. Delegating is optional. Without harness support, in a small task or when
   the harness does not allow the requested capability, the orchestrator runs
   the role in its own session with the same inputs and outputs.
6. In a Maintenance run, which only proposes, the orchestrator may operate in
   `standard`.
7. Delegated roles do not delegate. Every delegation starts from the
   orchestrator.

## Delegation package

Pointers, not copies:

- role and effective capability;
- goal in one or two sentences;
- inputs: artifact paths, the Radiant revision and the absolute root of the
  checkout resolved by the bootstrap; relative paths such as `../radiant` do
  not resolve inside harness worktrees;
- boundary: writable paths, read-only paths and non-goals;
- expected output and return format;
- `HOLD` conditions.

For Build, the Task Contract is the package; the request points to it and adds
the Radiant revision and absolute root, which the contract does not carry. For
research, critique and collection, the package goes in the request itself and
does not become a file.

## Return

For Build, the return follows the `Completion report` in section 16 of the
[template](../../templates/task-contract.md), even when the consumer's contract
does not reproduce that section. The other roles return:

- state: `DONE`, `HOLD` or `FAIL`;
- outputs: paths created or changed;
- evidence: commands and results actually obtained, including blockers;
- coverage: what the request included and was not inspected or run, with the
  reason;
- deviations: ambiguities and what stayed outside the boundary;
- findings that are candidates for Learn Back.

The return is a summary. The orchestrator does not accept `DONE` on the
account alone. In the readback, it:

- checks each reported change in the diff and confirms that the full state of
  the working tree, including untracked files, has no unreported change;
- confirms each claimed verification result from the command output or by
  running it again;
- checks the cited line references against the indicated revision;
- runs the checks and compares the result with the contract.

`HOLD` is resolved within the current authorization or taken to the human.
`FAIL` preserves the evidence and goes to [Learn Back](../../docs/learn-back.md).

## Access and boundaries

Each profile in [agents.json](agents.json) declares `access`: `read` for
profiles that do not change files (research and critique) and `write` for the
others. The adapters translate `read` into the harness's least-privilege
mechanism.

A contract's specific boundaries (writable paths, network, external systems)
are not enforced by the harness on `write` profiles: they hold as package
instructions and are checked by the orchestrator in the readback, which
compares the diff with the allowed paths before accepting. When the
contract's risk requires real enforcement (`Risk tier` ≥ 2 with network denied
or sensitive paths), run the Build in an isolated environment offered by the
harness or keep the role in the orchestrator's session under its permissions.

## Parallelism

Only between independent tasks with disjoint write paths. When in doubt, run
sequentially.

## Backend dispatch

An external operator may replace the native subagent: each execution unit of
the contract runs in its own session of the chosen harness, with its own
worktree, and the orchestrator remains the session with the human.

- The package is the contract path and the unit ID, as a pointer, plus the
  Radiant revision and absolute root. The split and its rules are in
  [execution units](../../contracts/README.md#execution-units).
- The orchestrator chooses the [routing rule](../../docs/routing.md); the
  operator resolves harness and model. Requirements come from
  [requirements.json](requirements.json), and what each harness offers, from
  `adapters/<harness>/provides.json`.
- The Build return is still the `Completion report`, written to
  `.radiant/reports/<id>.md` in the worktree. The consumer ignores that path
  in Git.
- Acceptance, readback and rules 1 to 7 do not change. The operator does not
  accept, does not merge or push and does not change scope.

## Provenance

The contract's verification report, or the maintenance report in a
Maintenance run, records each delegation, one line per round: role,
capability, full model ID resolved by the adapter, state and the usage metric
defined by the adapter. In backend dispatch, the line also includes the
harness and the dispatch identifier. Without a defined metric, the report
records its absence. Model IDs appear only in these reports and in the
adapters.

---
id: TC-0001
version: "0.2"
status: done
acceptance: approved
accepted_on: 2026-09-15
accepted_by: Project owner (Fael)
verification: docs/project/verification/VR-0002-bootstrap-acceptance.md
canonical_path: docs/project/contracts/TC-0001-iteration-00-bootstrap.md
project: AI Knowledge Manager (AIKM)
iteration: "00"
title: Technical Bootstrap
system: Radiant - Project Generation System
risk: Durable / local / reversible
---

# Radiant Task Contract - AIKM - Iteration 00

## 1. Revision and purpose

Amendment 0.2 (2026-09-15), requested by the project owner: align this contract with the corrected [Implementation Plan](../PLAN.md), section 5, Iteration 00 - Technical Bootstrap. The previous Plan duplicated the Spec and did not contain the iteration referenced by version 0.1 of this contract.

This revision preserves the contract ID, filename, bootstrap objective, delegated authority, write boundary, non-goals, and verification gates. It clarifies traceability without retroactively approving any implementation or declaring an earlier execution complete. Any previous execution evidence remains associated with the version under which it was produced.

Create the smallest justified, reproducible technical foundation needed to begin AIKM implementation. The observable result is a local CLI that responds to `aikm --help`, supported by tests, lint, format verification, and a short stack ADR.

This is technical bootstrap, not AIKM product development. A working help command makes the increment observable; unused infrastructure for later iterations does not.

## 2. Canonical inputs

Read before implementation:

1. [Radiant Constitution](../../radiant/CONSTITUTION.md).
2. [Project Frame](../FRAME.md), especially intent, product hypothesis, and scope boundaries.
3. [Implementation Spec](../SPEC.md), especially sections 5-7, 54, 65-67, and 73: implementation principles, scope, core independence, CLI, optional AI, canonical storage, Git, and deferred decisions.
4. [Implementation Plan](../PLAN.md), section 5 for the delegated increment; sections 3, 25-28, and 32 for execution, contracts, completion, tests, and ADRs; section 6 only to identify the next iteration's boundary.
5. [Task Contract convention](README.md) and [active contract pointer](ACTIVE.md).
6. this Task Contract
7. [Repository harness guidance](../../../AGENTS.md).

Use the corrected Plan as the increment source, not the earlier duplicated document. This contract already fulfills the Plan's instruction to create the Iteration 00 contract; do not create a duplicate under an iteration-only filename. Contract identity and activation follow the contract convention and active pointer.

Higher-precedence sources must not be silently reinterpreted. If an applicable ADR already exists, inspect it before making structural choices; this contract does not authorize silently replacing an established decision.

## 3. Plan traceability

| Iteration 00 requirement              | Contract output                                             | Verification                                       |
| ------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| Repository and initial code structure | Runnable project in the existing AIKM source repository     | Setup instructions and source readback             |
| Justified technical choices           | Short `ADR-0001-technical-bootstrap.md`                     | Decision coverage and trade-off review             |
| Minimum CLI                           | `aikm --help` or its documented repository-local invocation | Successful exit, visible help, AIKM identification |
| Test suite                            | Executable tests with one repository-local command          | Complete current suite passes                      |
| Lint and format                       | Configuration and documented commands                       | Lint and format check pass                         |
| No premature product features         | Bootstrap-only implementation                               | Diff and dependency readback against section 6     |

The Plan's repository deliverable refers to this existing source repository. It does not authorize creating a nested repository or a remote.

## 4. Delegated technical decisions

The implementing agent may choose the bootstrap stack without additional approval, within the canonical constraints and any existing decisions.

Decide and justify:

| Area                 | Required decision                                                  |
| -------------------- | ------------------------------------------------------------------ |
| Language and runtime | Local execution and distribution approach                          |
| Dependencies         | Package manager and reproducible dependency handling               |
| CLI                  | Library or runtime-native command-line mechanism                   |
| Markdown/frontmatter | Safe parsing approach for future record work                       |
| Schema validation    | Validation approach, without defining the AIKM domain schema       |
| Filesystem           | Local file access strategy                                         |
| Tests                | Test runner and CLI execution test approach                        |
| Lint and format      | Tools and repository-local verification commands                   |
| IDs                  | Generation strategy, without implementing record identity behavior |
| Git                  | Optional development/history support, never a runtime dependency   |
| Layout               | Minimal source, test, and configuration structure                  |

Evaluate choices against the Plan's criteria: simple local distribution, strong filesystem handling, fast CLI execution, safe YAML/frontmatter parsing, fast tests, few operational dependencies, and reasonable multiplatform support. Multiplatform verification is not an MVP requirement.

Do not select a stack solely because it is familiar, fashionable, or theoretically scalable. Record important alternatives and actual trade-offs.

Selecting a parser, validator, filesystem approach, or ID strategy does not require installing unused packages, creating wrappers, or implementing future semantics. Distinguish decisions recorded now from code needed now.

## 5. Scope and deliverables

Create or adjust only the technical foundation needed for:

1. project/package manifests and a lockfile when normal for the ecosystem;
2. minimal source structure and runnable CLI entry point;
3. the repository-supported invocation of `aikm --help`;
4. initial CLI tests and a command to run the complete test suite;
5. lint configuration and a local lint command;
6. format configuration and local format/format-check commands;
7. necessary build/runtime configuration;
8. ignore rules for generated, cache, and build artifacts where applicable;
9. minimal setup and developer instructions with exact commands;
10. `docs/project/adrs/ADR-0001-technical-bootstrap.md`.

The CLI must display AIKM help and exit successfully. No global installation, package publication, database, daemon, remote service, or AI provider is required to use it.

If bootstrap artifacts already exist, inspect and verify them before changing them. Reuse conforming work; neither recreate it automatically nor treat its existence as proof of completion.

## 6. Explicit non-goals

Do **not** implement Iteration 01 or later behavior.

Specifically, do not implement:

- `aikm init`;
- AIKM workspace creation, discovery, or manifest handling;
- AIKM Record persistence;
- `knowledgeRole` or `artifactKind` behavior;
- provenance/lifecycle/trust behavior;
- capture/inbox;
- routing/promotion;
- search/retrieve;
- execution evidence;
- Experience/Finding/Learn Back product behavior;
- reuse events or `doctor`;
- AIKM-to-harness adapters;
- databases of any kind;
- embeddings or vector search;
- sync/cloud/authentication;
- telemetry/analytics;
- LLM integration;
- speculative abstractions for future iterations.

Do not advertise unavailable commands as implemented capabilities. Fixtures containing AIKM records and product workflows belong to later increments, not this bootstrap.

## 7. Repository and write boundary

The execution root is the **AIKM source repository**, not an AIKM knowledge workspace.

Do not create a knowledge workspace during this task.

Implementation writes are limited to:

- source/test/config files necessary for the chosen bootstrap stack;
- dependency manifests and lockfiles;
- `.gitignore` entries required by that stack;
- minimal bootstrap developer documentation;
- `docs/project/adrs/ADR-0001-technical-bootstrap.md`.

Treat canonical inputs as read-only during implementation:

```text
AGENTS.md
docs/radiant/CONSTITUTION.md
docs/project/FRAME.md
docs/project/SPEC.md
docs/project/PLAN.md
docs/project/contracts/README.md
docs/project/contracts/ACTIVE.md
docs/project/contracts/TC-0001-iteration-00-bootstrap.md
```

The owner-requested amendment in section 1 is a documentation revision, not permission for an implementing agent to rewrite this contract to fit its result. A material contradiction or necessary change outside these boundaries requires `HOLD`.

Preserve unrelated work. Do not create a nested repository, configure remotes, publish packages, push changes, or provision external services. Do not use credentials, paid services, telemetry, or external transmission of project content.

Git may be used normally when already available, but AIKM runtime behavior must not depend on Git.

## 8. Required ADR

Create or complete the short stack ADR at:

```text
docs/project/adrs/ADR-0001-technical-bootstrap.md
```

Record context, every decision in section 4, important alternatives, why the selected stack fits the Plan's criteria, trade-offs, and intentionally deferred work.

Clearly separate approaches selected for later implementation from functionality actually delivered now. Do not duplicate the Spec, redefine established product principles, or use the ADR to decide later product architecture without a bootstrap need.

## 9. Implementation constraints

Keep the foundation minimal, runnable, and local:

- `aikm --help`, tests, lint, and format verification run locally without a remote service.
- No database, container, daemon, cloud infrastructure, or AI integration is needed.
- The core remains independent of a model, provider, or coding harness; repository agent guidance is not runtime architecture.
- No unused domain layer or fake implementation of future AIKM capabilities is introduced.
- Setup prerequisites and commands are documented so the environment can be reproduced from repository files.

## 10. Verification and readback

Use the narrowest deterministic checks first, then run all bootstrap gates below. Record exact commands and outcomes; naming a tool or adding a script is not execution evidence.

### CLI behavior

Run the documented repository-local equivalent of:

```bash
aikm --help
```

Confirm a successful exit, visible help text, and clear AIKM identification. Tests must exercise the actual CLI entry point and assert that behavior; independently run the command as an end user would.

### Tests and tooling

Run:

1. the necessary build/typecheck command, if the selected stack requires one;
2. the complete current test suite;
3. the configured lint/static-quality command;
4. the configured non-mutating format check or equivalent verification.

Expected: all required commands succeed, all tests pass, and in-scope files conform without blocking findings. Do not claim a gate passed if it was not run or was blocked.

### Reproducibility and ADR

Confirm the documented prerequisites, dependency manifests, lockfile where applicable, and build/run commands reproduce the foundation without relying on undocumented local state.

Read the ADR against section 4 and the Plan's stack criteria. Confirm all required decisions are justified and deferred product work remains deferred.

### Scope readback

Inspect the resulting diff, source, dependencies, configuration, and developer documentation. Confirm:

- the delivered behavior is limited to the bootstrap;
- no Iteration 01+ capability, product workspace, database, AI integration, or product adapter was added;
- generated/cache/build artifacts are ignored appropriately;
- writes remained inside the delegated boundary and unrelated work was preserved;
- canonical inputs were not changed by implementation.

The prior Plan finding is resolved only after readback confirms the corrected Plan contains Iteration 00 and agrees with this contract. That documentary check does not substitute for bootstrap verification.

Tests created in this task are supporting evidence, not the only evidence. The final product experiment and AC-01 through AC-22 are not bootstrap acceptance gates.

## 11. Completion state

### `DONE`

Use only when all section 5 deliverables exist and section 10 verification supports them:

- stack choices are justified in the ADR;
- `aikm --help` works;
- required build/typecheck, tests, lint, and format verification pass;
- bootstrap is reproducible from repository files;
- scope remained bounded and final readback confirms no premature product capability.

Passing this contract prepares the repository for Iteration 01. It does not authorize implementing that iteration without its applicable contract.

### `HOLD`

Use when continuing requires an undelegated decision, authorization, or external dependency, including:

- unresolved contradiction between canonical sources;
- a material scope change or necessary edit outside the write boundary;
- replacement of an established architectural decision without authorization;
- external credentials, paid services, remote publication, or other undelegated side effect;
- blocked verification with no adequate local alternative.

Report blocker, evidence, why it exceeds authority, and the smallest decision/action needed.

### `FAIL`

Use when the objective cannot be achieved within the agreed boundary or final verification demonstrates non-conformance. Known failures that invalidate the outcome must not be reported as `DONE`.

## 12. Learn Back

Report only reusable findings with evidence and the smallest responsible `fixTarget`: Contract, Spec, Plan, Procedure/Skill, Adapter, or Constitution only for a truly cross-project invariant.

The incorrect Plan that motivated revision 0.2 is a planning/traceability finding, not permission to redesign the bootstrap. Report any remaining mismatch explicitly.

Do not create permanent process artifacts for trivial observations. A finding does not authorize editing its target outside the write boundary. Reporting development findings is not implementation of the AIKM Learn Back product feature.

## 13. Required completion report

The implementing agent must finish with:

**State:** `DONE`, `HOLD`, or `FAIL`  
**Implemented:** concise description  
**Decisions:** selected stack + ADR path  
**Verification:** commands executed + outcomes  
**Scope integrity:** confirmation or disclosed deviation  
**Findings:** only reusable Learn Back findings/blockers

Reference `TC-0001` version 0.2. The report must distinguish implementation verified in this execution from any earlier evidence; contract metadata alone is not evidence of completion.

## 14. Success statement

> **AIKM has a justified and reproducible technical foundation from which the first real product capability can be built, while no product capability has yet been prematurely implemented.**

## 15. Acceptance record

On 2026-09-15, the project owner explicitly requested approval and documentary
closure of the delivered contract before proceeding to the next one. TC-0001
v0.2 is accepted as `DONE`, supported by the fresh verification recorded in
[VR-0002](../verification/VR-0002-bootstrap-acceptance.md).

This entry records acceptance only. Version 0.2, its objective, scope, write
boundary, and verification criteria remain unchanged. The bootstrap code is
identified by commit `cbcbc732a639f09fc7609261ca760460927e14fc`.

The accompanying workflow preparation has its own documentary authority and
[verification record](../verification/VR-0001-workflow-setup.md); it is not
retroactively included in this implementation contract. Approval closes the
bootstrap and does not activate TC-0002 or establish product utility.

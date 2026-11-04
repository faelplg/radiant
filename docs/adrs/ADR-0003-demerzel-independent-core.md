# ADR-0003: Demerzel core independent of Radiant

- Date: 2026-10-17
- State: `accepted` on 2026-10-17
- Owner: Fael
- Originating Radiant revision: `c5cf46774fe567b49d7f5af1e22056286a14f1db`
- Implementation: PR #22, merge `cc398b624af872152d8242cf2b28a1ab515ec277`
- Partly supersedes: [ADR-0002](ADR-0002-backend-dispatch-demerzel.md)

This ADR records a decision the owner made in conversation on 2026-10-17,
during Demerzel's Frame: Demerzel's internal boundary separates a core without
Radiant from a Radiant integration, but the scope remains that of ADR-0002.
ADR-0002 holds where this one does not supersede it.

## Intent

ADR-0002 made Demerzel a Radiant consumer at runtime, without saying where
that dependency lives inside it. This ADR confines it to an integration
module, so the dispatch core does not carry Radiant.

Two dependencies are kept apart:

1. Radiant as the process for developing Demerzel: `.radiant.json`, Frame,
   Spec and contracts in the Demerzel repository. This continues.
2. Radiant as a runtime dependency of the product: it stays only in the
   Radiant integration.

## Context and constraints

- AIKM already follows this pattern: it is a Radiant consumer for development,
  and its code does not depend on Radiant. Its
  [Frame](https://github.com/faelplg/aikm/blob/main/docs/project/FRAME.md)
  records that shared formats are welcome, and a shared executor is not.
- The [Constitution](../../constitution/CONSTITUTION.md) keeps the core
  tool-independent (Article XIV) and asks for evidence before expansion
  (Article II). ADR-0002 already asks, from eve, for dependencies wrapped in
  surfaces of their own.
- Every planned use of Demerzel today is in a Radiant project. There is no
  recorded case of dispatch outside one.
- Harness knowledge already lives in Radiant's adapters (capability to model,
  `provides.json`) and in AIKM's adapters (native files). A catalog of
  Demerzel's own would be a third place for the same fact.
- A Radiant unit needs the Radiant bootstrap in the session that executes it,
  which requires a Radiant adapter ([ADR-0001](ADR-0001-delegation-roles.md)).

## Decisions

| Decision | Choice |
| --- | --- |
| Demerzel's identity | Dispatch mechanics, without judgment about the split, rule choice or acceptance, as in ADR-0002 |
| Internal boundary | Core without a dependency on Radiant; reading `radiant-units`, the pin gate, filtering by adapter, resolving model and requirements through the adapter and the Completion report live in a Radiant integration module |
| Public entry in the first increment | Only the Radiant integration |
| Routing format, requirements vocabulary, `provides.json`, `capabilities.json` | Stay in Radiant, as in ADR-0002 |
| Proof of the boundary | Demerzel's suite runs the core flow with a fake backend, without a Radiant checkout in the environment |
| Constitution | No change |

Deferred, with a condition for reopening:

| Piece | Reopen when |
| --- | --- |
| Generic core entry and Demerzel's own harness catalog | There is a real dispatch in a project without `.radiant.json` |
| Demerzel's routing format | Routing needs a fact Radiant should not know, such as a usage quota per harness |

Discarded alternatives:

- Keeping ADR-0002 without an internal boundary: the dependency on Radiant
  spreads through the core, and separating it later costs more.
- A full generic core now, with its own task format, catalog and routing (the
  first version of this proposal): a surface without a user, a third place for
  model by capability and rework on the routing format just delivered in
  PR #20.
- Demerzel as an orchestrator with judgment: trades mechanics for judgment and
  reopens automatic rule choice. The owner kept Demerzel as mechanics.

## 1. Boundaries

Supersedes the Demerzel row of the table in section 1 of ADR-0002. The others
remain.

| Piece | Question it answers | Contains | Does not contain |
| --- | --- | --- | --- |
| Demerzel, core | How does a task become a running session, and what state is it in? | Internal task model, request builder, backend, dispatch log, supervision | Knowledge of Radiant, work split, acceptance, merge, scope |
| Demerzel, Radiant integration | How does a unit of a Task Contract become a core task? | Contract reader, pin gate, router over Radiant's rules and adapters, return in `.radiant/reports/` | Changes to the contract or to Radiant bodies |

Rules 1 to 4 of section 1 of ADR-0002 still hold.

## 2. Components

Complements the table in section 3 of ADR-0002, which still holds for stack,
CLI, exit codes, herdr backend, log and the
`dispatch`/`status`/`wait`/`collect` flow.

| ADR-0002 component | Where it lives |
| --- | --- |
| Request builder, backend, dispatch log | Core |
| Contract reader, pin gate, router | Radiant integration |

The router stays in the integration while the rules and adapters belong to
Radiant. The core's internal task model is defined in Demerzel's Spec and
receives from the integration the harness, model, effort, paths and request
already resolved.

All the refusals in section 4 of ADR-0002 still hold. A divergent pin, an
invalid `radiant-units` block, a harness without a Radiant adapter and
`.radiant/reports/` not ignored by Git are checked by the integration.

## 3. Egress correction

Supersedes, in section 4 of ADR-0002, the sentence "The request carries only
paths, and the contract's content does not leave the machine (Article XII)".
Demerzel does not control what the launched harness sends: it reads the
contract and sends it to its model provider, as it would in a session opened
by hand. The possible guarantee is smaller.

- Demerzel does not embed contract content or secrets in the request; the
  request carries only paths.
- Routing a unit to a harness is also an egress decision (Article XII). It
  follows the same rules that would apply to opening that harness by hand in
  the project.

The 2026-10-17 revision of Demerzel's Frame already records this correction.

## 4. Verification

The smallest experiment in section 5 of ADR-0002 continues. One refutation
condition for the boundary is added: the hypothesis falls if the core needs a
Radiant checkout to dispatch an already resolved task.

## Out of scope

- Everything ADR-0002 already left out of scope.
- The deferred pieces above, until their conditions are met.
- Demerzel as an orchestrator with judgment.

## Planned files in Radiant

| Action | Path |
| --- | --- |
| Change | `docs/integration.md` ("Demerzel boundary": core and integration) |
| Change | `docs/adrs/ADR-0002-backend-dispatch-demerzel.md` (pointer to this ADR, including in the egress sentence of section 4) |

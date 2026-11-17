# Spec: [project]

- Revision: [revision and date]
- Frame: [consumer Frame path and revision]
- Engineering Profile: [consumer Profile path and revision]

Define observable behavior before implementation details. Keep engineering
constraints in the [Engineering Profile form](engineering-profile.md), not in
this Spec. Remove areas that do not apply; retain explicit exclusions and
unresolved decisions that affect acceptance.

## Concepts

| Concept | Meaning and identity |
| --- | --- |
| [domain term] | [definition and ownership] |

## Behavior by area

Repeat this subsection for each independently testable area.

### [Area]

- Inputs and preconditions: [valid data, caller and authorization].
- Rules: [observable outcomes and side effects].
- States: [valid states and transitions, including interrupted operations].
- Events: [triggers, ordering and delivery guarantees].
- Invariants: [what must always hold, including concurrent or retried use].

## Interfaces

| Interface | Input | Output | Compatibility contract |
| --- | --- | --- | --- |
| [CLI, API, file or event] | [shape and limits] | [shape and side effects] | [stable behavior] |

## Refusals and errors

| Trigger | Error or refusal | Observable effects | Recovery |
| --- | --- | --- | --- |
| [invalid input or failed operation] | [code, exit and diagnostic] | [what changed or stayed intact] | [safe next action] |

## Security and egress

- Trust boundaries: [actors, inputs and resources].
- Data classification: [what can be read, stored and sent, and to whom].
- Authorization: [required decision before privileged or external effects].
- Refusals: [how prohibited access or egress is demonstrated].

## Non-functional requirements

State measurable product limits and refer to the Profile for implementation
conventions: [latency, capacity, compatibility, accessibility or availability,
with workload and measurement conditions].

## Acceptance and verification

| Criterion | Evidence and command or procedure | Owning increment |
| --- | --- | --- |
| [observable behavior] | [real path, boundary, failure and recovery evidence] | [Plan issue or contract] |

Distinguish implementation evidence, user outcome and unverified assumptions.

## Out of scope

- [explicit exclusion and the boundary it protects].

## Decisions

| Decision | Chosen behavior and reason | Rejected alternative | Status or owner |
| --- | --- | --- | --- |
| [question] | [choice and evidence] | [alternative and consequence] | [settled or pending] |

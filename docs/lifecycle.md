# Lifecycle coverage

The SDLC (software development lifecycle) and PDLC (product development
lifecycle) phase lists below are a working model for this map, not a
standard. The Radiant cycle is the process; this map shows where each
phase's evidence lives, without requiring a document per phase.

## SDLC

| Phase | Radiant stage | Artifact | Note |
| --- | --- | --- | --- |
| Planning | Frame, Plan | [Project Frame](../templates/project-frame.md), [Implementation Plan](project-generation-system.md#65-plan) | |
| Requirements | Spec | [Spec form](../templates/spec.md) | Behavior, interfaces and observable acceptance; engineering constraints point to the Profile. |
| Design | Design | [ADR form](../templates/adr.md), [Design Frame](design-layer.md#design-frame), [Design Spec](design-layer.md#design-spec), [EB-04](../engineering/engineering-baseline.md#6-eb-04---security-privacy-and-data-control), [EB-06](../engineering/engineering-baseline.md#8-eb-06---dependencies-and-supply-chain) | System and experience tracks; security boundaries and structural dependencies are decided here and recorded in an ADR. |
| Implementation | Contract, Build | [Task Contract section 4](../templates/task-contract.md#4-allowed-scope) and [section 10](../templates/task-contract.md#10-dependency-policy), [Engineering Baseline](../engineering/engineering-baseline.md), [practice catalog](../engineering/practices/README.md) | Section 4 bounds paths, external systems and network (EB-04); section 10 governs new dependencies (EB-06). |
| Testing | Verify | [Task Contract section 11](../templates/task-contract.md#11-verification-plan) and [section 16](../templates/task-contract.md#16-completion-report), [test-strategy](../engineering/practices/test-strategy.md), [EB-04](../engineering/engineering-baseline.md#6-eb-04---security-privacy-and-data-control) | Security verification when the change touches the surfaces EB-04 lists. |
| Release | Build, Verify | [Release and versioning](#release-and-versioning), [semantic-versioning](../engineering/practices/semantic-versioning.md) | |
| Deployment | Build, Verify | [Deploy](#deploy), [ci-cd](../engineering/practices/ci-cd.md) | The concrete checklist lives in the project's [Engineering Profile](../templates/engineering-profile.md#deploy-checklist) or [`workflow`](integration.md). |
| Operations | Verify, Learn Back | [EB-07](../engineering/engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability), [dora-metrics](../engineering/practices/dora-metrics.md) | Environment-specific tooling and runbooks belong in the [Profile operations section](../templates/engineering-profile.md#operations). |
| Incident and postmortem | Learn Back | [Learning Record with its Incident section](../templates/learning-record.md#incident-optional) | Live incident response runbooks are out of scope because they depend on the environment. |
| Maintenance | Outside the cycle (feeds the Frame), Learn Back | [radiant-maintenance](../skills/radiant-maintenance/SKILL.md), [maintenance report](../templates/maintenance-report.md) | As the [Maintenance role](../skills/radiant-delegation/SKILL.md#maintenance) defines it. |
| Retirement | Plan, Contract | [Plan](project-generation-system.md#65-plan), [ADR form](../templates/adr.md), [Task Contract HOLD conditions](../templates/task-contract.md#13-hold-conditions) | Irreversible, so [Article III](../constitution/CONSTITUTION.md#article-iii---rigor-proportional-to-irreversibility) applies. |

## PDLC

| Phase | Radiant stage | Artifact | Note |
| --- | --- | --- | --- |
| Discovery | Frame | [Project Frame](../templates/project-frame.md#intent-and-participant), [radiant-research](../skills/radiant-delegation/SKILL.md#ideation) | |
| Definition | Frame, Challenge | [Project Frame](../templates/project-frame.md#hypothesis-and-challenge), [radiant-grill](../skills/radiant-delegation/SKILL.md#ideation) | |
| Solution design and prototyping | Design | [Design Frame](design-layer.md#design-frame), [Design Spec](design-layer.md#design-spec), [design layer prototyping](design-layer.md#prototyping-and-review) | |
| User validation | Frame, Design, Verify | Project Frame [Smallest experiment](../templates/project-frame.md#smallest-experiment) and [Result](../templates/project-frame.md#result), [design layer prototyping](design-layer.md#prototyping-and-review) | The experiment is framed in the Frame, run through prototyping or real use, and read in Verify. |
| Development | Spec to Verify | [The SDLC table](#sdlc) | |
| Launch | None | None | Out of scope: go-to-market, pricing and communication are business functions, and Radiant is a development operating system; release mechanics are in the SDLC table. |
| Outcome measurement | Frame, Verify, Learn Back | Project Frame [outcome metric](../templates/project-frame.md#smallest-experiment) and [Result](../templates/project-frame.md#result) | Declared in the Frame, read in Verify, acted on in Learn Back. |
| Iterate or sunset | Learn Back, Frame | [Learning Record](../templates/learning-record.md), [Frame revision](../templates/project-frame.md), [ADR form](../templates/adr.md) | Sunset is a human decision ([Article XIII](../constitution/CONSTITUTION.md#article-xiii---humans-keep-agency-over-relevant-decisions)). |

## Release and versioning

Commits follow Conventional Commits. Release notes are generated from that
history; never edit `CHANGELOG.md` by hand. Use the
[semantic-versioning practice](../engineering/practices/semantic-versioning.md)
when there are consumers of a published interface. Radiant itself is
identified by a full Git commit, as defined in
[contributing](contributing.md#initial-identity).

## Deploy

Every deploy answers: which exact commit or artifact is deployed, who
approves it, how it is reversed, in which order data migrations run and
whether they reverse, which smoke check runs afterward and who watches it.
The concrete checklist lives in the project's
[Engineering Profile deploy checklist](../templates/engineering-profile.md#deploy-checklist) or
[`workflow`](integration.md), with the [ci-cd practice](../engineering/practices/ci-cd.md) as a
reference. An unplanned destructive action, such as an irreversible migration, triggers the
[Task Contract HOLD condition](../templates/task-contract.md#13-hold-conditions).

## Metrics

The product outcome metric belongs in the Project Frame's
[Smallest experiment](../templates/project-frame.md#smallest-experiment) and
[Result](../templates/project-frame.md#result). Delivery performance belongs
to [dora-metrics](../engineering/practices/dora-metrics.md). Radiant's own
metrics are defined in [thesis section 29](project-generation-system.md#29-metrics).

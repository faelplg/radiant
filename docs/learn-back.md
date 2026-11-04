# Learn Back for Radiant

Article XV and section 8 of the [Constitution](../constitution/CONSTITUTION.md)
govern learning and constitutional promotion. The procedure is in the
[cycle skill](../skills/radiant-cycle/SKILL.md). This map identifies the real
destinations in the repository.

| Supported finding | First destination to assess |
| --- | --- |
| Misunderstood intent or specific requirement | The consumer's Frame/Spec/context |
| Reusable ambiguity in framing | `templates/project-frame.md` |
| Ambiguous delegation | `templates/task-contract.md` or `contracts/README.md` |
| Inadequate recurring step | `skills/radiant-cycle/SKILL.md` |
| Insufficient structural verification | `validators/` or `docs/verification.md` |
| Harness does not find the right body | `adapters/<harness>/` |
| Inadequate role, capability or handoff | `skills/radiant-delegation/` |
| Inadequate model for a capability | `adapters/<harness>/capabilities.json` |
| Noisy or blind maintenance triage | `skills/radiant-maintenance/` or the consumer's workflow |
| Applied revision cannot be identified | `docs/integration.md` and its validator |
| Demonstrated cross-cutting invariant | Candidate for a constitutional amendment |

The originating project keeps evidence and diagnosis. To propose a change in
Radiant, record in the diff/commit or in a selective record: authorized
origin, Radiant commit used, finding, evidence, reusable reach, `fixTarget`,
change and verification. Do not bring unnecessary private data into the Core.

A specific problem stays in the consumer. When the cause affects several
projects or is structural, the proposal may change the shared owner, with
justification and verification. Recurrence helps ground the promotion; an
isolated finding does not automatically become a universal rule.

A verified fix does not demonstrate later reuse. The project only consumes the
fixed revision after explicitly adopting the pin. When it is used, record the
evidence of application in the consumer and reference the Radiant change. That
link lives in Git and in the consumer's artifacts.

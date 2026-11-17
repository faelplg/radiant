# Templates

A template is the shared form. The filled document is project state, with its
own identity, decisions and history. Do not keep a copy of the template in the
consumer for distribution to other projects.

- [practice-card.md](practice-card.md): applicability, observable signals and verification of an engineering practice.
- [adr.md](adr.md): context, options and consequences of a structural decision.
- [learning-record.md](learning-record.md): outcome, evidence, diagnosis, fix target, change, verification and reuse, with an optional incident section.
- [project-frame.md](project-frame.md): intent and smallest experiment.
- [design-frame.md](design-frame.md): framing of the experience before
  implementation.
- [design-spec.md](design-spec.md): structure of the experience, states, flows,
  accessibility and verification criteria.
- [task-contract.md](task-contract.md): bounded delegation; use the
  [convention](../contracts/README.md). Historical gap in `docs/plans/`:
  [TC-0001-practice-catalog.md](../docs/plans/TC-0001-practice-catalog.md)
  and [TC-0002-lifecycle-map.md](../docs/plans/TC-0002-lifecycle-map.md)
  predate `# 18. Owner decisions` and remain without that section as
  historical contracts;
  [TC-0003-engineering-profile.md](../docs/plans/TC-0003-engineering-profile.md)
  records its owner decisions under `## Owner decisions (2026-11-17)`.
- [spec.md](spec.md): concepts, behavior, interfaces and observable acceptance.
- [engineering-profile.md](engineering-profile.md): project-specific engineering
  decisions and stack pack overrides; the filled Profile stays in the consumer.
- [radiant-project.json](radiant-project.json): local map and pin, according to
  [integration](../docs/integration.md). Replace `RADIANT_COMMIT` with a real
  full commit; `null` means the artifact does not exist yet.

- [maintenance-report.md](maintenance-report.md): maintenance triage report,
  written outside Git in the consumer.
- [project-agents.md](project-agents.md): neutral harness map, the delimited
  Radiant section in the consumer's `AGENTS.md`.

Harness configuration templates live in the
[Codex](../adapters/codex/README.md) and
[Claude Code](../adapters/claude-code/README.md) adapters. Full rules stay
with their owners and are not copied into the forms.

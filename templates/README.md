# Templates

A template is the shared form. The filled document is project state, with its
own identity, decisions and history. Do not keep a copy of the template in the
consumer for distribution to other projects.

- [project-frame.md](project-frame.md): intent and smallest experiment.
- [design-frame.md](design-frame.md): framing of the experience before
  implementation.
- [design-spec.md](design-spec.md): structure of the experience, states, flows,
  accessibility and verification criteria.
- [task-contract.md](task-contract.md): bounded delegation; use the
  [convention](../contracts/README.md).
- The Engineering Profile is a consumer artifact; the Baseline stays in
  [engineering/engineering-baseline.md](../engineering/engineering-baseline.md).
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

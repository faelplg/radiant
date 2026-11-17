# Radiant

Radiant organizes the transformation of intent into verifiable systems and
makes learning correct the process used in the following cycles. It reduces
lost context, implicit scope and rules duplicated across agents.

It is a development operating system, not a consumer product, agent framework
or knowledge base. It works without AIKM.

The [cycle and thesis](docs/project-generation-system.md) explain the system.
The [Constitution](constitution/CONSTITUTION.md) is its only constitutional
normative source.

## Status

Radiant has a cycle skill, templates, validators, Codex and Claude Code
adapters, and a CI job named `check`. The Antigravity CLI (`agy`) adapter is
planned in [#29](https://github.com/faelplg/radiant/issues/29).

## Find what you need

| Location                                                                   | Responsibility                                           |
| -------------------------------------------------------------------------- | -------------------------------------------------------- |
| [AGENTS.md](AGENTS.md)                                                     | Map for working on Radiant itself                        |
| [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md)               | Invariants and precedence                                |
| [engineering/engineering-baseline.md](engineering/engineering-baseline.md) | Proportional engineering baseline                        |
| [engineering/practices/](engineering/practices/README.md) | Opt-in engineering practices and verification methods |
| [docs/capabilities.md](docs/capabilities.md)                               | Index of available capabilities                          |
| [docs/design-layer.md](docs/design-layer.md)                               | Radiant's canonical design layer                         |
| [skills/radiant-cycle/SKILL.md](skills/radiant-cycle/SKILL.md)             | Reusable cycle procedure                                 |
| [skills/radiant-delegation/SKILL.md](skills/radiant-delegation/SKILL.md)   | Roles, capabilities and delegation                       |
| [skills/radiant-maintenance/SKILL.md](skills/radiant-maintenance/SKILL.md) | Maintenance triage that only proposes                    |
| [templates/](templates/README.md)                                          | Forms for Frame, Contract, Design and the project map    |
| [contracts/README.md](contracts/README.md)                                 | Shared contract convention                               |
| [adapters/codex/](adapters/codex/README.md)                                | Codex bootstrap and subagents                            |
| [adapters/claude-code/](adapters/claude-code/README.md)                    | Claude Code bootstrap and subagents                      |
| [validators/](validators/README.md)                                        | Local integrity and review checks                        |
| [docs/contributing.md](docs/contributing.md)                               | Evolution and versioning                                 |
| [docs/integration.md](docs/integration.md)                                 | Consumer adoption, pin policy and tool boundaries         |
| [docs/verification.md](docs/verification.md)                               | Verifying changes to this system                         |
| [docs/learn-back.md](docs/learn-back.md)                                   | Routing learning to the right owner                      |
| [docs/routing.md](docs/routing.md)                                         | Rules for routing units to harnesses                     |
| [docs/adrs/](docs/adrs/ADR-0001-delegation-roles.md)                       | Structural decisions of Radiant itself                   |

## Use it in another project

1. Choose a Radiant commit and a clean checkout of that revision.
2. Generate the global block according to your harness's adapter:
   [Codex](adapters/codex/README.md) or [Claude Code](adapters/claude-code/README.md).
3. In the consumer, follow [Adopt in a project](docs/integration.md#adopt-in-a-project):
   declare the revision and the local paths and add the Radiant section to
   `AGENTS.md`.
4. Create Frame, Spec, Plan, Engineering Profile and Contracts in the
   consumer, in proportion to the task. The Profile is recommended when there
   is a specific stack, security, integration or risk; the Baseline stays in
   Radiant. Read skills and templates directly in Radiant.

The global configuration holds only a path and an adapter entry. It can be
rebuilt; it holds no Constitution, skills or project state. A new Radiant
revision does not update consumers automatically.

Demerzel dispatches a contract's execution units into harness sessions. Its
Radiant integration validates units, pins and routing through the chosen
Radiant revision. It does not accept deliveries or change scope; both systems
work independently. See the [Demerzel boundary](docs/integration.md#demerzel-boundary).

## Run the checks

At the repository root, with Python 3.9+ and Git:

```sh
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
```

See [verification](docs/verification.md) for check coverage and review criteria.

## Evolve

Change the canonical owner, run the [checks](docs/verification.md) and record
motivation and evidence in Git. A project finding can improve a template,
skill, validator or adapter through [Learn Back](docs/learn-back.md). Only
cross-cutting invariants justify constitutional proposals.

There is a real cycle skill, artifact forms, a design layer and an integration
map. There are no engines, package manager or dependency on a specific tool;
each adapter translates the same Core for one harness. The workflow procedure
lives in the skill; no empty directory duplicates it.

History: the September 2026 reorganization is recorded in the
[migration plan](docs/history/migration-plan.md) and
[reorganization report](docs/history/repository-report.md).

## License

Radiant is released under the [MIT license](LICENSE).

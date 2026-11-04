# Available capabilities

This index does not implement behavior. Read only the applicable body.

| Need                                     | Canonical body                                                                   | Local result in the consumer        |
| ---------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------- |
| Plan, execute, verify and learn          | [radiant-cycle](../skills/radiant-cycle/SKILL.md)                                | Bounded increment and evidence      |
| Orchestrate roles and delegate           | [radiant-delegation](../skills/radiant-delegation/SKILL.md)                      | Delegations with evidence and acceptance |
| Triage maintenance of a consumer         | [radiant-maintenance](../skills/radiant-maintenance/SKILL.md), [report](../templates/maintenance-report.md) | Report with proposals               |
| Set up the harness                       | [Codex](../adapters/codex/README.md), [Claude Code](../adapters/claude-code/README.md) | User bootstrap and subagents        |
| Frame intent                             | [Project Frame](../templates/project-frame.md)                                   | Filled Frame                        |
| Frame the experience                     | [Design Frame](../templates/design-frame.md)                                     | Filled Design Frame                 |
| Define the experience in detail          | [Design Spec](../templates/design-spec.md)                                       | Implementable Design Spec           |
| Contract an increment                    | [Convention](../contracts/README.md), [form](../templates/task-contract.md)      | Contract and local pointer          |
| Map consumer state                       | [Integration](integration.md), [form](../templates/radiant-project.json)         | Paths and Radiant revision          |
| Verify Radiant                           | [Verification](verification.md), [validators](../validators/README.md)           | Evidence about the change           |
| Route learning                           | [Learn Back](learn-back.md)                                                      | Fix in the responsible owner        |
| Dispatch units through a backend         | [radiant-delegation](../skills/radiant-delegation/SKILL.md#backend-dispatch), [routing](routing.md) | Units running on chosen harnesses   |
| Operate the design layer                 | [Design Layer](design-layer.md)                                                  | Design system inside Radiant        |

Spec and Plan are guided by the skill and by sections 6.3 and 6.5 of the
[thesis](project-generation-system.md). The design layer now has its own
canonical body and specific templates, keeping the separation between System
Design and Experience Design. Future capabilities may come in as skills,
templates, validators or workflows of their own when there is a distinct body
and a proven need.

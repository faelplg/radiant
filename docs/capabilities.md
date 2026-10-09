# Capacidades disponíveis

Este índice não implementa comportamento. Leia somente o corpo aplicável.

| Necessidade                              | Corpo canônico                                                                   | Resultado local do consumidor       |
| ---------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------- |
| Planejar, executar, verificar e aprender | [radiant-cycle](../skills/radiant-cycle/SKILL.md)                                | Incremento delimitado e evidência   |
| Orquestrar papéis e delegar              | [radiant-delegation](../skills/radiant-delegation/SKILL.md)                      | Delegações com evidência e aceite   |
| Triar manutenção de um consumidor        | [radiant-maintenance](../skills/radiant-maintenance/SKILL.md), [relatório](../templates/maintenance-report.md) | Relatório com propostas             |
| Configurar o harness                     | [Codex](../adapters/codex/README.md), [Claude Code](../adapters/claude-code/README.md) | Bootstrap e subagentes do usuário   |
| Enquadrar intenção                       | [Project Frame](../templates/project-frame.md)                                   | Frame preenchido                    |
| Enquadrar a experiência                  | [Design Frame](../templates/design-frame.md)                                     | Design Frame preenchido             |
| Definir a experiência detalhadamente     | [Design Spec](../templates/design-spec.md)                                       | Design Spec implementável           |
| Contratar um incremento                  | [Convenção](../contracts/README.md), [formulário](../templates/task-contract.md) | Contract e ponteiro local           |
| Mapear estado do consumidor              | [Integração](integration.md), [formulário](../templates/radiant-project.json)    | Paths e revisão do Radiant          |
| Verificar o Radiant                      | [Verification](verification.md), [validators](../validators/README.md)           | Evidência sobre a alteração         |
| Encaminhar aprendizado                   | [Learn Back](learn-back.md)                                                      | Correção no owner responsável       |
| Operar a camada de design                | [Design Layer](design-layer.md)                                                  | Sistema de design dentro do Radiant |

Spec e Plan são orientados pela skill e pelas seções 6.3 e 6.5 da
[tese](project-generation-system.md). A camada de design agora possui corpo
canônico próprio e templates específicos, mantendo a separação entre System
Design e Experience Design. Capabilities futuras podem entrar como skills,
templates, validators ou workflows próprios quando houver corpo distinto e
necessidade comprovada.

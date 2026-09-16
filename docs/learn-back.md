# Learn Back para o Radiant

O Artigo XV e a seção 8 da [Constitution](../constitution/CONSTITUTION.md)
governam aprendizado e promoção constitucional. O procedimento está na
[skill de ciclo](../skills/radiant-cycle/SKILL.md). Este mapa identifica os
destinos reais do repositório.

| Finding sustentado | Primeiro destino a avaliar |
| --- | --- |
| Intenção ou requisito específico mal compreendido | Frame/Spec/contexto do consumidor |
| Ambiguidade reutilizável no enquadramento | `templates/project-frame.md` |
| Delegação ambígua | `templates/task-contract.md` ou `contracts/README.md` |
| Passo recorrente inadequado | `skills/radiant-cycle/SKILL.md` |
| Verificação estrutural insuficiente | `validators/` ou `docs/verification.md` |
| Harness não encontra o corpo correto | `adapters/codex/` |
| Revisão aplicada não identificável | `docs/integration.md` e seu validador |
| Invariante transversal demonstrado | Candidato a amendment constitucional |

O projeto de origem guarda evidência e diagnóstico. Para propor mudança no
Radiant, registrar no diff/commit ou em registro seletivo: origem autorizada,
commit do Radiant usado, finding, evidência, alcance reutilizável, `fixTarget`,
mudança e verificação. Não trazer dados privados desnecessários para o Core.

Um problema específico continua no consumidor. Quando a causa afeta vários
projetos ou é estrutural, a proposta pode alterar o owner compartilhado, com
justificativa e verificação. Recorrência ajuda a fundamentar a promoção; um
finding isolado não vira regra universal automaticamente.

Uma correção verificada não demonstra reutilização posterior. O projeto só
consome a revisão corrigida após adoção explícita do pin. Quando ela for usada,
registre a evidência de aplicação no consumidor e referencie a mudança Radiant.
AIKM poderá recuperar esse vínculo, mas não é necessário para fechar o ciclo.

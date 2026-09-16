---
id: LR-0001
date: 2026-09-15
status: Correção documental verificada; reutilização posterior pendente
fixTarget: Procedure/Skill e adapter do projeto
reuse: Não demonstrado em entrega posterior
---

# Tornar o workflow acionável antes da próxima entrega

## Finding e evidência

O responsável apontou que a implementação já havia começado sem clareza sobre o
uso de skills e a execução do processo Radiant. A inspeção do repositório
encontrou Constituição, Frame, Spec, Plan, contrato, ADR e testes de bootstrap,
mas nenhum procedimento de ciclo ou skill Radiant com entrada pelo adapter. O
Plan também citava "Tier 2 / Deep" sem definição operacional disponível.

Isso não invalida a verificação técnica do bootstrap. Revela uma lacuna entre
ter artefatos de projeto e um processo reutilizável que oriente sua produção,
aplicação e revisão. A
[verificação desta preparação](../verification/VR-0001-workflow-setup.md)
preserva o limite da evidência atual.

## Diagnóstico e correção

O procedimento recorrente dependia da interpretação do agente e das intervenções
na conversa. Faltavam um ponto de entrada explícito e o vínculo entre execução,
versão do procedimento e evidência.

O menor destino de correção foi uma
[skill de ciclo](../../radiant/skills/radiant-cycle/SKILL.md), ligada pelo
[adapter do repositório](../../../AGENTS.md) ao
[mapa do projeto](../WORKFLOW.md). O Plan agora remete a esse fluxo; TC-0002,
ainda proposto, identifica o workflow e os dados de proveniência a preservar. O
rigor de verificação passa a ser expresso pelos checks concretos, sem afirmar um
nível indefinido.

A Constituição e TC-0001 permanecem intactos. Não atribuir uso desta skill às
execuções anteriores. Usar skills para desenvolver o AIKM também não implica que
o produto já as armazene ou recupere.

## Verificar na próxima aplicação

Na próxima entrega autorizada, observar se uma sessão entra pelo mapa, aplica o
modo correto, respeita o contrato, verifica o resultado e preserva evidência sem
reconstruir o procedimento na conversa. Registrar intervenções necessárias.

Se a skill exigir detalhes específicos de produto ou ferramenta para funcionar,
avaliar primeiro uma correção no mapa/adapter consumidor. Alterar o procedimento
compartilhado somente quando o finding justificar. Reutilização em outro produto
e ganho de utilidade via AIKM continuam pendentes de observação real.

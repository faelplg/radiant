---
name: radiant-cycle
description:
  Conduzir planejamento, execução ou verificação de um ciclo de desenvolvimento
  sob Radiant, ligando intenção, contrato, evidência e aprendizado. Usar ao
  iniciar ou retomar uma entrega Radiant; uma consulta pontual não exige
  executar o ciclo inteiro.
metadata:
  version: "0.1.3"
---

# Ciclo operacional Radiant

Esta skill contém o procedimento reutilizável. A
[Constitution](../../constitution/CONSTITUTION.md) define as regras superiores. Os artefatos
do projeto definem o produto e a delegação; a skill não os substitui. Comandos,
paths, contrato ativo e estado de implementação vêm do mapa operacional do
projeto consumidor.

## Entrada e retomada

1. Identifique a solicitação atual: analisar/planejar, alterar documentação,
   implementar ou verificar. Preserve decisões já autorizadas na sessão.
2. Leia o mapa do projeto e os inputs necessários. Confira o contrato pelo
   ponteiro ativo, o estado real dos arquivos e evidências anteriores; não
   deduza execução ou conclusão apenas de metadados ou da existência de um
   plano.
3. Escolha o modo abaixo. Uma solicitação de análise não autoriza mudanças;
   documentação explicitamente solicitada pode ser revisada sem inventar um
   contrato de implementação. Código exige a delegação aplicável do projeto.
4. Informe de forma curta: objetivo, modo, contrato ou autorização documental,
   versão desta skill, evidência esperada e próxima ação. Reutilize contexto já
   carregado; não recomece etapas concluídas sem nova razão.
5. Para coordenar papéis ou delegar trabalho a subagentes, leia a
   [skill radiant-delegation](../radiant-delegation/SKILL.md). Para triagem
   contínua de um consumidor, use a
   [skill radiant-maintenance](../radiant-maintenance/SKILL.md).

## Planejar e enquadrar

- Relacione a necessidade real ao Frame e procure conhecimento/procedimentos
  existentes antes de produzir outro corpo. Separe processo compartilhado de
  contexto específico do produto e configuração de ferramenta.
- Faça o Challenge na própria decisão: qual hipótese este incremento testa, qual
  evidência motivou seu escopo e qual alternativa mais simples o atende?
  Registre a resposta no artefato responsável quando material; não crie um
  documento por etapa apenas para preencher um fluxo.
- Compare Spec, Plan e realidade. Encaminhe divergências à camada responsável,
  respeitando a autorização atual. Defina o percurso observável de uso e a
  evidência que distingue implementação técnica de utilidade do produto.
- Prepare ou refine o contrato antes de sua execução, com inputs, outputs,
  paths, non-goals e verificações executáveis. Use a convenção do projeto para
  identidade e ativação. Não reformule um contrato já executado para acomodar um
  resultado diferente.
- Saída: proposta concreta ou artefatos autorizados atualizados, pendências
  materiais e próximo passo. Planejar uma entrega não a aprova para execução.

## Executar uma entrega

- Confirme que o contrato ativo cobre a tarefa e que a autorização já existente
  permite o próximo passo. Não peça de novo uma decisão já concedida. Um
  contrato proposto diferente do ativo não é selecionado por conveniência.
- Comece pelo percurso que o usuário observará. Em correções de bugs, reproduza
  a falha nesse percurso antes de editar. Em uma capacidade nova, registre o
  comportamento ausente sem tratar a ausência como bug.
- Implemente dentro da fronteira delegada e preserve trabalho existente. Use
  procedimentos especializados quando a tarefa efetivamente precisar deles; esta
  skill não substitui conhecimentos de domínio, design ou segurança.
- Verifique a menor parcela relevante ao longo do trabalho. Se aparecer uma
  divergência material ou necessidade fora da delegação, preserve a evidência e
  aplique o estado constitucional adequado; não alargue o contrato sozinho.
- Saída: alteração inspecionável e evidências prontas para o modo seguinte.
  Código produzido ainda não é uma conclusão de verificação.

## Verificar e aprender

- Releia critérios e outputs a partir do contrato e da Spec. Inspecione o diff e
  o resultado como consumidor; confronte a afirmação de conclusão com esses
  inputs, não apenas com o relato de quem implementou.
- Quando uma revisão posterior encontrar lacuna em um aceite anterior, preserve
  o contrato e a evidência histórica. Registre o que a nova evidência limita,
  qual correção cabe ao ciclo atual e qual critério ainda precisa de prova;
  não transforme o `DONE` da revisão em novo aceite da entrega examinada.
- Execute o percurso real aplicável e os gates do projeto. Para documentação,
  confira referências, coerência das instruções e consequências de segui-las em
  cenários reais. Registre comandos e resultados efetivos, incluindo bloqueios;
  não transforme um teste planejado em evidência obtida.
- Escolha independência proporcional ao risco: verificadores determinísticos,
  inspeção do consumidor, outra execução ou revisão humana. Só use delegação
  quando disponível e autorizada. Diga qual método foi usado e suas limitações;
  uma releitura própria não equivale a uma revisão independente. Com papéis
  delegados, siga a regra de aceite da
  [skill de delegação](../radiant-delegation/SKILL.md#regras).
- Relacione achado material, evidência, diagnóstico e menor `fixTarget`. Corrija
  dentro da autorização vigente; caso contrário registre a pendência. Distingua
  correção feita, correção verificada e reutilização posterior demonstrada.
  Nenhuma delas implica automaticamente as demais.
- Encerre em `DONE`, `HOLD` ou `FAIL` conforme a Constitution. Registre no local
  permitido pelo contrato os dados de execução abaixo; para uma consulta
  simples, uma resposta curta basta. Não crie um registro permanente para cada
  interação.

## Evidência mínima de um ciclo relevante

O relatório autorizado, existente ou novo, deve permitir recuperar:

- objetivo, contrato e versão, ou solicitação documental que autorizou o ciclo;
- path e versão da skill utilizada, mais revisão Git ou digest do corpo exato
  quando ele ainda não estiver commitado;
- resultado, comandos/checks e limitações de verificação;
- achados materiais, `fixTarget` e referência da correção quando houver;
- estado final e próximo passo, distinguindo produto, processo e reutilização.

Não duplique a skill nos relatórios ou em memórias de ferramentas. Ao reutilizar
em outro produto, aponte para este corpo canônico e forneça o mapa/contexto
desse produto. Mudanças compartilhadas não reescrevem contratos ou evidências
anteriores; registre a versão realmente usada e avalie a aplicabilidade da
revisão seguinte.

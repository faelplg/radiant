---
version: "0.1"
status: Procedimento disponível; aplicação em entrega de produto pendente
project: AIKM
---

# Como desenvolver o AIKM com Radiant

## Ponto de entrada

Leia a [skill radiant-cycle](../radiant/skills/radiant-cycle/SKILL.md) e aplique
o modo correspondente à solicitação. Ela é a fonte do procedimento; este arquivo
contém seu mapeamento para o AIKM. O [AGENTS.md](../../AGENTS.md) encaminha o
agente para ambos antes de um ciclo relevante.

A skill já pode orientar o desenvolvimento por leitura direta do arquivo. Não
depende de captura, busca ou instalação global do AIKM. Ela não foi registrada
em um catálogo global de skills; sua disponibilidade aqui vem do ponteiro no
adapter do repositório. Não presumir que uma sessão exibirá `$radiant-cycle`
como comando ou que o agente leu a skill sem verificar sua entrada no ciclo.

## Mapa dos inputs e das saídas

| Necessidade                        | Fonte no AIKM                                                                             |
| ---------------------------------- | ----------------------------------------------------------------------------------------- |
| Intenção, participante e hipótese  | [Frame](FRAME.md)                                                                         |
| Comportamento e critérios          | [Spec](SPEC.md)                                                                           |
| Marco de uso e incremento          | [Plan](PLAN.md), seção 4                                                                  |
| Delegação aplicável                | [ACTIVE.md](contracts/ACTIVE.md) e contrato apontado                                      |
| Identidade e ativação de contratos | [Convenção](contracts/README.md)                                                          |
| Stack e trade-offs vigentes        | [ADR-0001](adrs/ADR-0001-technical-bootstrap.md)                                          |
| Procedimento reutilizável          | [radiant-cycle](../radiant/skills/radiant-cycle/SKILL.md)                                 |
| Evidência de execução              | Path permitido pelo contrato em `docs/project/verification/`                              |
| Aprendizado material               | Relatório da execução ou registro seletivo em `docs/project/learning/`, quando autorizado |

Estado ativo vem do ponteiro; este guia não é uma segunda lista de contratos
ativos. Evidência técnica não substitui evidência de utilidade ou de adoção.

## Como iniciar e retomar

Pedidos úteis, adaptáveis à tarefa:

- "Leia `docs/project/WORKFLOW.md` e a skill indicada. Revise o próximo contrato
  no modo planejar, sem iniciar implementação."
- "Execute o contrato ativo aplicável usando o workflow Radiant e registre a
  verificação da entrega."
- "Verifique a entrega contra o contrato e registre achados, evidências e o
  menor destino de correção."

O agente começa informando objetivo, modo, skill/versão, contrato ou autorização
documental e evidência de saída. Na retomada, consulta arquivos e evidências
atuais para identificar o que falta. Não precisa produzir novamente Frame, Spec
e Plan a cada sessão.

Para uma decisão concreta de produto, o Challenge cabe na justificativa do
incremento: necessidade real, alternativa mais simples e evidência de sucesso.
Design e skills especializadas entram quando houver decisões de interface,
arquitetura ou domínio que precisem delas; não são etapas vazias obrigatórias.

## Verificar a entrega neste repositório

Os comandos de setup e qualidade estão no [README](../../README.md#development).
O gate atual é `npm run check`. Também executar o percurso da CLI definido no
contrato e inspecionar os arquivos resultantes. Para mudanças somente
documentais, verificar links, instruções e diff; os testes do bootstrap não
demonstram o comportamento de uma skill.

O formatador padrão exclui documentos canônicos. Para um arquivo novo desta
camada, verificar sua formatação explicitamente; não reformatar toda a árvore
para validar uma mudança localizada.

Registrar a versão da skill (`metadata.version`) e a revisão ou SHA-256 do
arquivo lido. Assim, mudanças futuras no processo não apagam qual procedimento
orientou uma entrega. Relatórios históricos não devem atribuir uso dessa skill
ao bootstrap anterior à sua criação.

## Próxima aplicação e limites atuais

O bootstrap foi verificado e aprovado pelo responsável em 2026-09-15. O
[aceite do TC-0001](verification/VR-0002-bootstrap-acceptance.md) registra
`DONE` e as evidências de encerramento. Não há contrato de implementação ativo
até a próxima ativação, conforme [ACTIVE.md](contracts/ACTIVE.md). A
[proposta TC-0002](contracts/TC-0002-capture-search.md) prepara a parcela
técnica de M1, ainda com aprovação de execução pendente. O próximo passo é
revisá-la usando a skill, resolver decisões materiais e obter autorização de
execução. Quando ela for concedida, registrar a aprovação e atualizar o ponteiro
pela convenção; não exigir uma segunda aprovação idêntica.

Depois, executar e verificar TC-0002 pelo mesmo workflow, registrando
separadamente:

- resultado técnico de captura/busca;
- se o procedimento orientou a entrega e quais intervenções adicionais foram
  necessárias;
- utilidade real no Projeto B, que depende de uma tarefa e acervo autorizados.

A criação desta camada de instruções não ativa TC-0002 nem implementa suas
capacidades. A
[verificação desta preparação](verification/VR-0001-workflow-setup.md) registra
o que foi conferido e o que ainda precisa de uma execução posterior.

## Reaproveitar em outro produto

O primeiro caso de uso priorizado é reaproveitar o workflow de desenvolvimento
entre produtos. Manter o procedimento neste corpo canônico por enquanto; um novo
projeto recebe seu próprio mapa, contexto, Spec, Plan e contratos, além de um
ponteiro acessível para a skill e sua Constituição. Não copiar regras do AIKM
como se fossem requisitos do novo produto.

O nome da ferramenta, os comandos, caminhos locais e políticas do consumidor
ficam no mapa/adapter desse produto. Se o outro ambiente não alcançar a fonte,
resolver sua distribuição no escopo autorizado e preservar origem/versão; não
substituir o ponteiro por uma cópia divergente silenciosa.

Atualizações na skill compartilhada devem nascer de findings concretos e ser
verificadas antes de orientar uma nova entrega. Reutilização por leitura direta
prova uso do procedimento; só uma recuperação e aplicação via AIKM poderá
sustentar a hipótese de utilidade do produto. Nenhum outro projeto é alterado
como parte desta preparação.

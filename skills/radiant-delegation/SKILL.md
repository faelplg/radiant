---
name: radiant-delegation
description:
  Coordenar papéis de um ciclo Radiant e delegar trabalho delimitado a
  subagentes com a capacidade adequada. Usar ao orquestrar Ideação, Design,
  Dev, Verificação ou Manutenção, ao montar um pacote de delegação ou ao
  avaliar o retorno de um papel delegado.
metadata:
  version: "0.2.0"
---

# Delegação e papéis Radiant

Esta skill define como o orquestrador distribui o
[ciclo](../radiant-cycle/SKILL.md) entre papéis. A
[Constitution](../../constitution/CONSTITUTION.md) continua superior; contratos
seguem o [template](../../templates/task-contract.md) e a
[convenção](../../contracts/README.md). Os perfis delegáveis, legíveis por
máquina, estão em [agents.json](agents.json). Modelos concretos pertencem aos
adapters; esta skill fala apenas em capacidades. A decisão que originou esta
skill está no [ADR-0001](../../docs/adrs/ADR-0001-delegation-roles.md).

## Capacidades

| Capacidade | Uso |
| --- | --- |
| `deep` | Julgamento, crítica, decisões caras e aceite |
| `standard` | Execução delimitada por artefato aprovado |
| `light` | Busca, coleta, checks mecânicos e resumo |

Cada adapter mapeia as três capacidades para IDs completos de modelo e declara
como seu harness delega.

## Papéis

### Orquestrador

Sessão principal, em `deep`. Conversa com o humano, enquadra a solicitação
pelo ciclo, escolhe o que delegar, monta pacotes, aplica gates e faz o aceite
final. Mantém para si: mudança de escopo, ativação de contrato, ações
irreversíveis e aceitação de conhecimento canônico.

### Ideação

Etapas Frame e Challenge. O enquadramento é conduzido pelo orquestrador com o
humano, porque exige conversa. Delegáveis: pesquisa em `light`
(`radiant-research`), que devolve fontes inspecionadas e o que cada uma
sustenta, e crítica adversarial em `deep` (`radiant-grill`), que ataca
premissas, escopo e irreversibilidade de um Frame ou Spec existente e devolve
objeções com evidência. Nenhum dos dois decide intenção ou escopo.

### Design

Etapas Spec e Design, nas duas trilhas da
[Design Layer](../../docs/design-layer.md). System Design e ADRs em `deep`;
Design Spec derivado de Frame e Design Frame aprovados em `standard`
(`radiant-design`). Produz Spec, Design Frame, Design Spec e ADRs como
propostas; a aprovação é humana, mediada pelo orquestrador.

### Dev

Etapas Plan, Contract e Build. O orquestrador propõe Plan e contratos; o Build
de um contrato ativo é delegado em `standard` (`radiant-dev`), e tarefas
mecânicas podem usar `light`. O contrato é o pacote e seu `Completion report`
é o retorno.

### Verificador

Etapa Verify, em `deep` (`radiant-verifier`). Confronta outputs com contrato,
Spec e critérios, executa os gates e inspeciona o resultado como consumidor.
Checks determinísticos podem rodar em `light`. Não corrige o que verifica:
devolve achados com evidência.

### Manutenção

Fora do ciclo de entrega; alimenta Frame com propostas. Coleta em `light`,
priorização e rascunhos em `standard` (`radiant-maintenance`). Só propõe. O
procedimento está na [skill de manutenção](../radiant-maintenance/SKILL.md).

## Regras

1. Interação humana pertence ao orquestrador. Papéis delegados não conversam
   com o humano.
2. Aceite nunca usa capacidade inferior à do autor. Por tarefa, valem checks
   determinísticos e o readback do orquestrador. O Verificador faz o aceite do
   contrato uma vez, ao final, e é antecipado quando `Risk tier` ≥ 2 ou
   `Independent critique: REQUIRED`.
3. A capacidade padrão do papel só muda pelo campo `Capability` do Task
   Contract, com justificativa de uma linha, registrada na evidência.
4. Não são delegadas: mudança de escopo, ativação de contrato, ações
   irreversíveis e aceitação de conhecimento canônico.
5. Delegar é opcional. Sem suporte do harness, em tarefa pequena ou quando o
   harness não permite a capacidade pedida, o orquestrador executa o papel na
   própria sessão com as mesmas entradas e saídas.
6. Em execução de Manutenção, que apenas propõe, o orquestrador pode operar em
   `standard`.
7. Papéis delegados não delegam. Toda delegação parte do orquestrador.

## Pacote de delegação

Ponteiros, não cópias:

- papel e capacidade efetiva;
- objetivo em uma ou duas frases;
- entradas: paths de artefatos, revisão do Radiant e raiz absoluta do
  checkout resolvida pelo bootstrap; paths relativos como `../radiant` não
  resolvem dentro de worktrees do harness;
- fronteira: paths graváveis, paths somente leitura e non-goals;
- saída esperada e formato do retorno;
- condições de `HOLD`.

Para Build, o Task Contract é o pacote; o pedido aponta para ele e acrescenta
a revisão e a raiz absoluta do Radiant, que o contrato não carrega. Para
pesquisa, crítica e coleta, o pacote vai no próprio pedido e não vira arquivo.

## Retorno

Para Build, o retorno segue o `Completion report` da seção 16 do
[template](../../templates/task-contract.md), mesmo quando o contrato do
consumidor não reproduz essa seção. Os demais papéis retornam:

- estado: `DONE`, `HOLD` ou `FAIL`;
- outputs: paths criados ou alterados;
- evidência: comandos e resultados efetivos, incluindo bloqueios;
- cobertura: o que o pedido incluía e não foi inspecionado ou executado, com
  o motivo;
- desvios: ambiguidades e o que ficou fora da fronteira;
- findings candidatos a Learn Back.

O retorno é um resumo. O orquestrador não aceita `DONE` apenas pelo relato. No
readback, ele:

- confere cada mudança relatada no diff e confirma que o estado completo do
  working tree, incluindo arquivos não rastreados, não traz mudança não
  relatada;
- confirma cada resultado de verificação alegado pela saída do comando ou
  reexecutando-o;
- confere as referências de linha citadas contra a revisão indicada;
- executa os checks e confronta o resultado com o contrato.

`HOLD` é resolvido dentro da autorização vigente ou levado ao humano. `FAIL`
preserva a evidência e segue para [Learn Back](../../docs/learn-back.md).

## Acesso e fronteiras

Cada perfil em [agents.json](agents.json) declara `access`: `read` para
perfis que não alteram arquivos (pesquisa e crítica) e `write` para os demais.
Os adapters traduzem `read` no mecanismo de menor privilégio do harness.

As fronteiras específicas de um contrato (paths graváveis, rede, sistemas
externos) não são impostas pelo harness nos perfis `write`: valem como
instrução do pacote e são conferidas pelo orquestrador no readback, que
compara o diff com os paths permitidos antes de aceitar. Quando o risco do
contrato exigir enforcement real (`Risk tier` ≥ 2 com rede negada ou paths
sensíveis), execute o Build em ambiente isolado oferecido pelo harness ou
mantenha o papel na sessão do orquestrador sob as permissões dela.

## Paralelismo

Somente entre tarefas independentes com paths de escrita disjuntos. Na dúvida,
execução sequencial.

## Despacho por backend

Um operador externo pode substituir o subagente nativo: cada unidade de
execução do contrato roda numa sessão própria do harness escolhido, com
worktree próprio, e o orquestrador continua sendo a sessão com o humano.

- O pacote é o caminho do contrato e o ID da unidade, como ponteiro, mais a
  revisão e a raiz absoluta do Radiant. A divisão e suas regras estão em
  [unidades de execução](../../contracts/README.md#unidades-de-execução).
- O orquestrador escolhe a [regra de roteamento](../../docs/routing.md); o
  operador resolve harness e modelo. Requisitos vêm de
  [requirements.json](requirements.json), e o que cada harness oferece, de
  `adapters/<harness>/provides.json`.
- O retorno de Build continua sendo o `Completion report`, gravado em
  `.radiant/reports/<id>.md` no worktree. O consumidor ignora esse path no Git.
- O aceite, o readback e as regras 1 a 7 não mudam. O operador não aceita,
  não faz merge nem push e não muda escopo.

## Proveniência

O relatório de verificação do contrato, ou o relatório de manutenção numa
execução de Manutenção, registra cada delegação, uma linha por rodada: papel,
capacidade, ID completo do modelo resolvido pelo adapter, estado e a métrica de
uso definida pelo adapter. No despacho por backend, a linha inclui também o
harness e o identificador do despacho. Sem métrica definida, o relatório registra a
ausência. IDs de modelo aparecem apenas nesses relatórios e nos adapters.

# ADR-0003: núcleo do Demerzel independente do Radiant

- Data: 2026-10-17
- Estado: `accepted` em 2026-10-17
- Owner: Fael
- Revisão de origem do Radiant: `c5cf46774fe567b49d7f5af1e22056286a14f1db`
- Implementação: PR #22, merge `cc398b624af872152d8242cf2b28a1ab515ec277`
- Substitui em parte: [ADR-0002](ADR-0002-backend-dispatch-demerzel.md)

Este ADR registra uma decisão do owner tomada em conversa em 2026-10-17,
durante o Frame do Demerzel: a fronteira interna do Demerzel separa um núcleo
sem Radiant de uma integração Radiant, mas o escopo continua o do ADR-0002. O
ADR-0002 vale onde este não o substitui.

## Intenção

O ADR-0002 fez do Demerzel um consumidor do Radiant em tempo de execução, sem
dizer onde essa dependência mora dentro dele. Este ADR a confina num módulo de
integração, para que o núcleo de despacho não carregue o Radiant.

Duas dependências ficam separadas:

1. Radiant como processo para desenvolver o Demerzel: `.radiant.json`, Frame,
   Spec e contratos no repositório do Demerzel. Continua.
2. Radiant como dependência do produto em tempo de execução: fica só na
   integração Radiant.

## Contexto e restrições

- O AIKM já segue esse molde: é consumidor do Radiant para desenvolver, e seu
  código não depende do Radiant. Seu
  [Frame](https://github.com/faelplg/aikm/blob/main/docs/project/FRAME.md)
  registra que formatos compartilhados são bem-vindos, e um executor
  compartilhado não.
- A [Constitution](../../constitution/CONSTITUTION.md) mantém o core
  independente de ferramenta (Artigo XIV) e pede evidência antes de expansão
  (Artigo II). O ADR-0002 já pede, do eve, dependências embrulhadas em
  superfícies próprias.
- Todo uso previsto do Demerzel hoje é em projeto Radiant. Não há caso
  registrado de despacho fora dele.
- O conhecimento de harness já vive nos adapters do Radiant (capacidade para
  modelo, `provides.json`) e nos adapters do AIKM (arquivos nativos). Um
  catálogo próprio do Demerzel seria um terceiro lugar para o mesmo fato.
- Uma unidade Radiant precisa do bootstrap do Radiant na sessão que a executa,
  o que exige adapter Radiant
  ([ADR-0001](ADR-0001-delegation-roles.md)).

## Decisões

| Decisão | Escolha |
| --- | --- |
| Identidade do Demerzel | Mecânica de despacho, sem julgamento sobre divisão, escolha de regra ou aceite, como no ADR-0002 |
| Fronteira interna | Núcleo sem dependência do Radiant; leitura de `radiant-units`, gate de pin, filtro por adapter, resolução de modelo e requisitos pelo adapter e Completion report ficam num módulo de integração Radiant |
| Entrada pública no primeiro incremento | Só a integração Radiant |
| Formato de roteamento, vocabulário de requisitos, `provides.json`, `capabilities.json` | Continuam no Radiant, como no ADR-0002 |
| Prova da fronteira | A suíte do Demerzel roda o fluxo do núcleo com backend falso, sem checkout Radiant no ambiente |
| Constitution | Sem alteração |

Adiado, com condição para reabrir:

| Peça | Reabrir quando |
| --- | --- |
| Entrada genérica do núcleo e catálogo próprio de harnesses | Houver um despacho real num projeto sem `.radiant.json` |
| Formato de roteamento do Demerzel | O roteamento precisar de um fato que o Radiant não deve conhecer, como cota de uso por harness |

Alternativas descartadas:

- Manter o ADR-0002 sem fronteira interna: a dependência do Radiant se
  espalha pelo núcleo, e separá-la depois custa mais.
- Núcleo genérico completo agora, com formato de tarefa, catálogo e roteamento
  próprios (primeira versão desta proposta): superfície sem usuário, um
  terceiro lugar para modelo por capacidade e retrabalho no formato de
  roteamento recém-entregue no PR #20.
- Demerzel como orquestrador com julgamento: troca mecânica por julgamento e
  reabre a escolha automática de regra. O owner manteve o Demerzel como
  mecânica.

## 1. Fronteiras

Substitui a linha Demerzel da tabela da seção 1 do ADR-0002. As demais
permanecem.

| Peça | Pergunta que responde | Contém | Não contém |
| --- | --- | --- | --- |
| Demerzel, núcleo | Como uma tarefa vira uma sessão rodando, e em que estado ela está? | Modelo interno de tarefa, montador do pedido, backend, registro de despachos, supervisão | Conhecimento de Radiant, divisão do trabalho, aceite, merge, escopo |
| Demerzel, integração Radiant | Como uma unidade de um Task Contract vira uma tarefa do núcleo? | Leitor de contrato, gate de pin, roteador sobre as regras e os adapters do Radiant, retorno em `.radiant/reports/` | Alteração de contrato ou de corpos do Radiant |

As regras 1 a 4 da seção 1 do ADR-0002 continuam valendo.

## 2. Componentes

Complementa a tabela da seção 3 do ADR-0002, que continua valendo para stack,
CLI, códigos de saída, backend herdr, registro e fluxo
`dispatch`/`status`/`wait`/`collect`.

| Componente do ADR-0002 | Onde fica |
| --- | --- |
| Montador do pedido, backend, registro de despachos | Núcleo |
| Leitor de contrato, gate de pin, roteador | Integração Radiant |

O roteador fica na integração enquanto as regras e os adapters forem do
Radiant. O modelo interno de tarefa do núcleo é definido na Spec do Demerzel e
recebe da integração harness, modelo, esforço, paths e pedido já resolvidos.

As recusas da seção 4 do ADR-0002 continuam todas valendo. Pin divergente,
bloco `radiant-units` inválido, harness sem adapter Radiant e
`.radiant/reports/` não ignorado pelo Git são verificados pela integração.

## 3. Correção de egress

Substitui, na seção 4 do ADR-0002, a frase "O pedido leva só paths, e o
conteúdo do contrato não sai da máquina (Artigo XII)". O Demerzel não controla
o que o harness lançado envia: ele lê o contrato e o manda ao seu provedor de
modelo, como faria numa sessão aberta à mão. A garantia possível é menor.

- O Demerzel não embute conteúdo do contrato nem secrets no pedido; o pedido
  leva só paths.
- Rotear uma unidade para um harness é também uma decisão de egress
  (Artigo XII). Ela segue as mesmas regras que valeriam para abrir aquele
  harness à mão no projeto.

A revisão de 2026-10-17 do Frame do Demerzel já registra essa correção.

## 4. Verificação

O menor experimento da seção 5 do ADR-0002 continua. Acrescenta-se uma
condição de refutação da fronteira: a hipótese cai se o núcleo precisar de um
checkout Radiant para despachar uma tarefa já resolvida.

## Fora de escopo

- Tudo o que o ADR-0002 já deixou fora de escopo.
- As peças adiadas acima, até suas condições se cumprirem.
- Demerzel como orquestrador com julgamento.

## Arquivos previstos no Radiant

| Ação | Path |
| --- | --- |
| Alterar | `docs/integration.md` ("Fronteira Demerzel": núcleo e integração) |
| Alterar | `docs/adrs/ADR-0002-backend-dispatch-demerzel.md` (ponteiro para este ADR, inclusive na frase de egress da seção 4) |

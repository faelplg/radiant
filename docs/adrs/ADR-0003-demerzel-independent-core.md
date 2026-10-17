# ADR-0003: Demerzel com núcleo próprio e integração Radiant opcional

- Data: 2026-10-17
- Estado: `proposed`
- Owner: Fael
- Revisão de origem do Radiant: `c5cf46774fe567b49d7f5af1e22056286a14f1db`
- Implementação: pendente
- Substitui em parte: [ADR-0002](ADR-0002-backend-dispatch-demerzel.md)

Este ADR registra uma decisão do owner tomada em conversa em 2026-10-17,
durante o Frame do Demerzel: o Demerzel continua sendo mecânica, mas genérico,
com núcleo próprio e o Radiant como integração opcional. O ADR-0002 continua
valendo onde este não o substitui.

## Intenção

O ADR-0002 fez do Demerzel um consumidor do Radiant em tempo de execução: só
despacha unidades `radiant-units`, passa por um gate de pin, só roteia para
harnesses com adapter Radiant e lê regras de roteamento cujo formato o Radiant
define. Isso prende uma ferramenta de despacho a um processo de
desenvolvimento.

Resultado esperado: o Demerzel despacha trabalho para sessões de harnesses
diferentes em qualquer projeto, com ou sem Radiant. Quando o projeto usa
Radiant, uma integração opcional preserva as garantias do ADR-0002 para as
unidades de um Task Contract.

Duas dependências ficam separadas:

1. Radiant como processo para desenvolver o Demerzel: o `.radiant.json`, o
   Frame, a Spec e os contratos no repositório do Demerzel. Continua.
2. Radiant como dependência do produto em tempo de execução: passa a existir
   só na integração Radiant.

## Contexto e restrições

- A [Constitution](../../constitution/CONSTITUTION.md) mantém o core
  independente de ferramenta (Artigo XIV) e a autonomia proporcional à
  reversibilidade (Artigo IV). Nada aqui a altera.
- Uma unidade Radiant precisa do bootstrap do Radiant na sessão que a executa,
  e o mapeamento de capacidade para modelo das funções Radiant vive nos
  adapters ([ADR-0001](ADR-0001-delegation-roles.md)). Por isso a restrição a
  harnesses com adapter vale para unidades Radiant, não para trabalho genérico.
- As regras de roteamento só importam para quem despacha para outro harness. A
  delegação por subagente nativo roda no harness da própria sessão e não as
  usa.
- O PR #20 já implementou no Radiant o formato de roteamento,
  `docs/routing.example.json` e sua validação em
  `validators/dispatch_formats.py`.

## Decisões

| Decisão | Escolha |
| --- | --- |
| Identidade do Demerzel | Operador de despacho genérico: transforma uma tarefa delimitada numa sessão de harness e acompanha seu estado. Continua sem julgamento sobre divisão, escolha de regra ou aceite |
| Dependência do Radiant | Só na integração Radiant, ativada quando o projeto tem `.radiant.json` |
| Formato de entrada do núcleo | Próprio do Demerzel, definido na Spec dele |
| Catálogo de harnesses | Do Demerzel, no nível do usuário: como lançar cada harness, o que cada um oferece, modelo por capacidade |
| Regras de roteamento | Arquivo e formato do Demerzel. O Radiant mantém as regras de conduta que qualquer operador cumpre ao despachar unidades Radiant |
| Unidades Radiant | A integração lê `radiant-units`, roda o gate de pin, aceita só harness com adapter Radiant, resolve modelo e requisitos pelos arquivos do adapter e espera o Completion report |
| Formato `radiant-units`, vocabulário de requisitos, `provides.json`, `capabilities.json` | Continuam no Radiant, sem mudança |
| Constitution | Sem alteração |

Alternativas descartadas:

- Manter o ADR-0002 como está: o Demerzel só serve a projetos Radiant e
  carrega o Radiant em toda execução.
- Demerzel como orquestrador agêntico que decide divisão e roteamento: troca
  mecânica por julgamento e reabre a escolha automática de regra, que o
  ADR-0002 deixou fora de escopo. O owner manteve o Demerzel como mecânica.
- Formato de roteamento no Radiant, lido pelo Demerzel nas unidades Radiant, e
  outro formato do Demerzel no trabalho genérico: o usuário manteria dois
  arquivos para a mesma decisão, e eles divergiriam.
- Catálogo do Demerzel como fonte de modelo também para unidades Radiant: a
  mesma função Radiant resolveria modelos diferentes conforme fosse delegada
  pelo subagente nativo ou pelo Demerzel.

## 1. Fronteiras

Substitui as linhas Radiant, Usuário e Demerzel da tabela da seção 1 do
ADR-0002. As demais permanecem.

| Peça | Pergunta que responde | Contém | Não contém |
| --- | --- | --- | --- |
| Radiant | Como o trabalho é dividido, roteado e aceito? | Template de contrato com divisão, vocabulário de requisitos, regras de conduta do despacho, skill de delegação, adapters | Código de despacho, formato de roteamento, catálogo de harnesses, estado de execução |
| Usuário | Com quais harnesses e preferências eu trabalho? | Bootstrap do Radiant, catálogo, regras de roteamento e configuração do Demerzel | Corpos do Radiant |
| Demerzel, núcleo | Como uma tarefa vira uma sessão rodando, e em que estado ela está? | Formato de tarefa, catálogo, roteamento, backend, registro de despachos, supervisão | Conhecimento de Radiant, divisão do trabalho, aceite, merge, escopo |
| Demerzel, integração Radiant | Como uma unidade de um Task Contract vira uma tarefa do núcleo sem perder as garantias do Radiant? | Leitura de `radiant-units`, gate de pin, filtro por adapter, resolução de modelo e requisitos pelo adapter, Completion report | Alteração de contrato ou de corpos do Radiant |

As regras 1 a 3 da seção 1 do ADR-0002 valem para o núcleo e para a
integração. A regra 4 (pin divergente impede o despacho) vale só para a
integração Radiant.

## 2. Regras de conduta no Radiant

Substitui, na seção 2 do ADR-0002, "Formato das regras de roteamento". Ao
despachar unidades Radiant, qualquer operador:

1. Executa a regra escolhida pelo orquestrador, sem escolher outra.
2. Só usa harness com adapter Radiant cujo `provides.json` cobre os `requires`
   da unidade.
3. Resolve o modelo pelo `capabilities.json` do adapter e nunca usa capacidade
   abaixo da pedida pela unidade. Sem candidato viável, a unidade fica em
   `HOLD`.
4. Registra a decisão antes do lançamento e não a relê depois.
5. Não despacha sem confirmação explícita do humano quando a regra a exige.
6. Recusa sem efeito quando o pin diverge.

O formato do arquivo, o nome dos campos e o lugar da instância passam ao
Demerzel. O Radiant deixa de manter `docs/routing.example.json` e sua
validação.

## 3. Mudanças no Demerzel

Substitui, na seção 3 do ADR-0002, a tabela de componentes. Stack, CLI,
códigos de saída, backend herdr, registro de despachos e fluxo
`dispatch`/`status`/`wait`/`collect` continuam como no ADR-0002.

| Componente | Onde fica |
| --- | --- |
| Formato de tarefa, catálogo, roteador, montador do pedido, backend, registro | Núcleo |
| Leitor de contrato, gate de pin, filtro por adapter, retorno em `.radiant/reports/` | Integração Radiant |

As recusas da seção 4 do ADR-0002 valem para o núcleo, exceto pin
divergente, bloco `radiant-units` inválido, harness sem adapter Radiant e
`.radiant/reports/` não ignorado pelo Git, que valem só para a integração.

## 4. Verificação e primeiro incremento

O menor experimento da seção 5 do ADR-0002 continua, rodado pela integração
Radiant. Acrescenta-se uma condição de refutação da independência: a hipótese
cai se o núcleo precisar de um checkout Radiant para despachar uma tarefa sem
`.radiant.json`. A suíte do Demerzel prova isso rodando o fluxo do núcleo com
backend falso, sem Radiant no ambiente.

## Fora de escopo

- Tudo o que o ADR-0002 já deixou fora de escopo.
- O formato de tarefa do núcleo e o formato do catálogo, que pertencem à Spec
  do Demerzel.
- Demerzel como orquestrador com julgamento.

## Arquivos previstos no Radiant

| Ação | Path |
| --- | --- |
| Alterar | `docs/routing.md` (regras de conduta; formato passa ao Demerzel) |
| Remover | `docs/routing.example.json` |
| Alterar | `validators/dispatch_formats.py`, `validators/check_repository.py`, `tests/test_dispatch_formats.py`, `tests/test_repository.py` (remover a validação de roteamento) |
| Alterar | `docs/integration.md` ("Fronteira Demerzel") |
| Alterar | `skills/radiant-delegation/SKILL.md` ("Despacho por backend") |
| Alterar | `docs/project-generation-system.md` (nota de estado na seção 30) |
| Alterar | `docs/adrs/ADR-0002-backend-dispatch-demerzel.md` (estado e ponteiro para este ADR) |

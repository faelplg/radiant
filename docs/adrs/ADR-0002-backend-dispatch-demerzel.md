# ADR-0002: despacho por backend e o operador Demerzel

- Data: 2026-10-16
- Estado: `proposed`
- Owner: Fael
- Revisão de origem do Radiant: `604c2a0b5103005e54b6a6089433f42d10d31320`
- Implementação: pendente

Este ADR registra o desenho aprovado em conversa com o owner. Quando
implementado, as regras operacionais passam a viver no template de contrato,
na [skill de delegação](../../skills/radiant-delegation/SKILL.md), nos
adapters e no repositório do Demerzel; em caso de divergência, esses corpos
prevalecem.

## Intenção

Fazer o Radiant orquestrar os orquestradores de desenvolvimento sem se tornar
o runtime. Hoje, montar uma subtarefa exige criar worktree e branch, abrir uma
aba, escolher harness e modelo, iniciar o harness e colar contexto e contrato à
mão. O mecanismo de subagente de cada harness evita parte disso, mas prende a
subtarefa ao harness da sessão principal e não deixa a divisão registrada.

Resultados esperados:

1. O Task Contract declara a divisão do trabalho em unidades, e cada unidade
   já diz o necessário para configurar o subagente adequado.
2. Um operador externo, o Demerzel, transforma cada unidade numa sessão do
   harness escolhido, numa aba própria do herdr, e acompanha seu estado.
3. Monitorar e gerenciar os fluxos fica possível por uma interface, num
   incremento posterior.

## Contexto e restrições

- A [Constitution](../../constitution/CONSTITUTION.md) exige core independente
  de ferramenta (Artigo XIV), um corpo canônico (Artigo XI), autonomia
  proporcional à reversibilidade (Artigo IV), agência humana (Artigo XIII),
  default deny para egress (Artigo XII) e simplicidade (Artigo XVII). Nomes de
  modelo e ferramenta não pertencem ao core (seção 7).
- A tese declara que o Radiant não é framework de agentes
  ([seção 30](../project-generation-system.md#30-o-que-radiant-não-é)), e o
  README declara que não há engines.
- Pela [skill de delegação](../../skills/radiant-delegation/SKILL.md) 0.1.1,
  um contrato inteiro é o pacote de um único `radiant-dev`. Papéis delegados
  não delegam (regra 7), e paralelismo exige paths de escrita disjuntos.
- Só existem adapters para Claude Code e Codex. O `capabilities.json` de cada
  um mapeia exatamente as três capacidades, e o `check_repository.py` rejeita
  chaves extras.
- Herdr 0.9.0, instalado na máquina do owner e conferido em 2026-10-16:
  `worktree create` aceita `--branch`, `--base` e `--trust-repository`;
  `agent start --kind` aceita `claude`, `codex`, `copilot`, `agy`, `opencode` e
  outros, num pane já aberto; `agent prompt` envia o pedido; `agent wait`
  reconhece `idle`, `working`, `blocked`, `done` e `unknown`;
  `api snapshot` expõe o estado vivo da sessão.
- Referências inspecionadas em 2026-10-16:
  - firstmate em `5f2b81bca96abc6a7702a2187232ca1c0c767493`: um agent distro
    que despacha tarefas em worktrees e abas de tmux ou herdr. Dele vêm as
    regras de roteamento em linguagem natural escolhidas com julgamento
    (`docs/configuration.md`, "Crew dispatch profiles"), a recusa de lançar
    sem harness resolvido, a decisão registrada na intake e não relida, o
    estado reconciliado do disco depois de restart, a proibição de rebaixar
    modelo sem permissão explícita e o princípio "scripts own the mechanics,
    agents own the judgment" (`VISION.md`).
  - eve em `5666d2f0d8b78690d01a40ce93cac5e472799901`: dependências de
    terceiros embrulhadas em superfícies próprias (`AGENTS.md`, princípio 5),
    CLIs prontos para agentes, com saída de máquina e erros que dizem o que
    fazer, e o gate de autoria de testes do `test-audit`.
- O AIKM rejeitou geradores de terceiros no caminho central para manter os
  formatos sob controle do owner ([Frame](https://github.com/faelplg/aikm/blob/main/docs/project/FRAME.md)).

## Decisões

| Decisão | Escolha |
| --- | --- |
| Identidade | O Radiant define como fluxos agênticos são divididos, roteados e aceitos; a execução continua nos harnesses |
| Quem executa a mecânica | Produto separado, o Demerzel, consumidor do Radiant pelo mesmo pin de qualquer projeto |
| Unidade de despacho | Unidade declarada dentro do Task Contract, menor que o contrato |
| O que a unidade declara sobre onde rodar | Papel, capacidade e requisitos; nunca harness ou modelo |
| Onde ficam as regras de roteamento | Nível do usuário, geradas pelo dotfiles; o Radiant define o formato |
| Quem escolhe a regra | O orquestrador, com julgamento; o Demerzel valida e executa |
| Primeiro backend | Herdr, atrás de uma interface própria do Demerzel |
| Stack do Demerzel | Bun e TypeScript |
| Formato das unidades | Bloco YAML cercado `radiant-units` no contrato |
| Retorno da unidade | Arquivo em path fixo e ignorado pelo Git dentro do worktree |
| Registro de despachos | Diretório de estado do usuário, por projeto |
| Constitution | Sem alteração |

Alternativas descartadas:

- Radiant como runtime de agentes: contradiz o Artigo XIV e cria outro produto.
- Camada de operação dentro do repositório Radiant: põe código no Core e em
  todo consumidor, inclusive nos que não despacham.
- Adotar o firstmate como camada de execução: põe um projeto de terceiro no
  caminho central, com modelo de autoridade e vocabulário próprios que
  competem com a Constitution.
- Contrato inteiro como unidade de despacho: força contratos minúsculos ou
  deixa a divisão sem registro.
- Subtarefa como artefato separado do contrato: cria uma segunda fronteira
  para manter coerente.
- Harness e modelo nomeados no contrato: exige emenda constitucional e
  envelhece o contrato quando um modelo sai de linha.
- Regras de roteamento no Core ou no projeto: o Core passaria a conhecer
  harnesses, e o projeto repetiria fatos da máquina do usuário.
- Tabela Markdown para as unidades: leitura por máquina ambígua.
- Retorno lido da saída do terminal: frágil diante de redesenho de tela e
  truncamento.

## 1. Fronteiras

| Peça | Pergunta que responde | Contém | Não contém |
| --- | --- | --- | --- |
| Radiant | Como o trabalho é dividido, roteado e aceito? | Template de contrato com divisão, vocabulário de requisitos, formato das regras de roteamento, skill de delegação | Código de despacho, nomes de harness no Core, estado de execução |
| Projeto consumidor | O que fazer neste incremento? | Contratos com unidades, `ACTIVE.md`, evidência | Regras de roteamento, estado do Demerzel |
| Usuário | Com quais harnesses e preferências eu trabalho? | Regras de roteamento, bootstrap do Radiant, configuração do Demerzel | Corpos do Radiant |
| Demerzel | Como cada unidade vira uma sessão rodando, e em que estado ela está? | Leitura do contrato, roteamento, backend, registro de despachos, supervisão | Divisão do trabalho, aceite, merge, escopo |
| Herdr | Onde a sessão roda? | Abas, panes, worktrees, estado do agente | Conhecimento de Radiant |
| Harness | Quem executa a unidade? | Sessão com papel e unidade recebidos | Delegação adicional (regra 7) |
| AIKM | Que skills, contexto e MCP o projeto tem? | Arquivos nativos por harness | Despacho ou estado de execução |

1. O orquestrador continua sendo a sessão principal com o humano. O Demerzel é
   uma ferramenta que ele chama no lugar da ferramenta nativa de subagente, e
   que o humano também pode chamar.
2. O Demerzel lê o contrato e nunca o altera. Grava apenas seu registro de
   despachos. O retorno continua sendo o Completion report, e o aceite
   continua com o orquestrador e o verificador.
3. Merge, push, descarte de worktree e mudança de escopo permanecem com o
   humano (Artigos IV e XIII).
4. O Demerzel consome o Radiant por `radiant_revision` e `check_project.py`.
   Pin divergente impede o despacho.

## 2. Mudanças no Radiant

### Divisão de execução no contrato

O [template](../../templates/task-contract.md) ganha uma seção opcional depois
de "Allowed scope". Sem ela, o contrato é uma unidade só, como hoje.

```yaml radiant-units
units:
  - id: TC-0025.1
    role: radiant-dev
    requires: []
    objective: Buscar fontes externas por rev para o cache.
    writes: [src/sources/, tests/sources/]
    depends_on: []
    done_when: Os testes de tests/sources passam e o cache recusa digest divergente.
  - id: TC-0025.2
    role: radiant-dev
    capability: deep
    capability_reason: A recusa de digest exige julgamento de segurança.
    requires: []
    objective: Integrar a verificação de digest ao sync.
    writes: [src/sync/]
    depends_on: [TC-0025.1]
    done_when: bun run check passa e o sync recusa conteúdo sem digest correspondente.
```

Regras:

- `id` é estável e nunca renumerado. `role` vem de
  [agents.json](../../skills/radiant-delegation/agents.json). `capability`
  ausente usa o padrão do papel; presente, exige `capability_reason`.
- `writes` é subconjunto dos paths graváveis do contrato. Unidades sem
  dependência entre si não se sobrepõem.
- A soma das unidades não ultrapassa objetivo, outputs e fronteira do
  contrato.
- Mudar a divisão depois do início segue a
  [integridade de contratos](../../contracts/README.md): amendment quando a
  fronteira não muda, HOLD quando muda.

### Vocabulário de requisitos

Arquivo legível por máquina em `skills/radiant-delegation/`, ao lado de
`agents.json`. Começa com `browser`, `ios-simulator` e `computer-use` e cresce
por Learn Back. Só entram propriedades estáticas do harness. Crítica por modelo
de outro fornecedor depende de quem foi o autor, então fica no `when` de uma
regra até existir evidência para um requisito próprio.

### O que cada adapter oferece

Cada adapter ganha `provides.json`, com os requisitos que seu harness atende
quando lançado num terminal por um backend, não no app desktop. Cada item
precisa de evidência de smoke registrada. O `capabilities.json` mantém o
schema atual. Só se roteia para harnesses que têm
adapter Radiant, porque sem adapter não há mapeamento de capacidade para
modelo nem bootstrap do Radiant naquela sessão.

### Formato das regras de roteamento

O Radiant define o formato e um exemplo. A instância fica em
`$XDG_CONFIG_HOME/radiant/routing.json`, gerada pelo dotfiles.

```json
{
  "schema": 1,
  "rules": [
    {
      "id": "ui-browser",
      "when": "Unidades de interface que precisam abrir e inspecionar páginas",
      "use": [{ "harness": "claude-code" }, { "harness": "codex" }],
      "why": "Preferência do owner para inspeção visual"
    },
    {
      "id": "independent-critique",
      "when": "Crítica de um Build feito por modelo de outro fornecedor",
      "use": [{ "harness": "codex", "capability": "deep" }],
      "approval": "human"
    }
  ],
  "default": [{ "harness": "claude-code" }]
}
```

- `harness` é o nome do diretório do adapter.
- `use` é uma lista em ordem de preferência. Cada candidato pode trazer
  `capability`, nunca abaixo da pedida pela unidade, e `effort`. Um `effort`
  que o harness não aceita é registrado e omitido do lançamento.
- `approval: human` impede despacho sem confirmação explícita do humano.

### Skill de delegação

Ganha a seção "Despacho por backend", alternativa ao subagente nativo. O
pacote é o caminho do contrato mais o ID da unidade, como ponteiro. A linha de
proveniência registra também harness e identificador do despacho. As regras 1
a 7 não mudam.

### Registros

- `docs/integration.md` ganha "Fronteira Demerzel", no molde da
  "Fronteira AIKM".
- A seção 30 da tese ganha nota de estado, sem reescrever o registro 0.2.
- As páginas vivas de mapa, glossário e casos de uso são atualizadas.

## 3. Demerzel

Bun e TypeScript. A interface principal é um CLI não interativo, com saída
`--json`, códigos `0` (ok), `1` (achados ou estado pendente) e `2` (recusa sem
efeito), e erros que dizem o que fazer em seguida.

| Componente | Responsabilidade |
| --- | --- |
| Leitor de contrato | Acha o projeto pelo `.radiant.json`, lê o contrato e extrai `radiant-units` |
| Gate de pin | Executa o `check_project.py` do Radiant e recusa em divergência |
| Roteador | Aplica a regra escolhida: descarta candidatos sem adapter ou sem os requisitos da unidade, pega o primeiro viável e resolve o modelo pelo `capabilities.json` |
| Montador do pedido | Prompt curto com ponteiros: papel, raiz absoluta e revisão do Radiant, contrato, ID da unidade e path do retorno |
| Backend | Interface com criar worktree, abrir aba, iniciar agente, enviar pedido, ler estado e encerrar; herdr é a primeira implementação e traduz o nome do adapter no `--kind` |
| Registro de despachos | Estado em `$XDG_STATE_HOME/demerzel/`, por projeto: unidade, harness, modelo, esforço, IDs no herdr, worktree, branch, base, revisão do Radiant, estado e horários |

Fluxo de `demerzel dispatch TC-0025.1 --rule <id>`:

1. Resolve o projeto e passa pelo gate de pin.
2. Lê a unidade, confere dependências concluídas e ausência de sobreposição
   com unidades em andamento.
3. Roteia e grava a decisão no registro antes de lançar. A decisão não é
   relida depois. O prefixo `radiant/` é o padrão e pode mudar na
   configuração do Demerzel; a base é a branch atual do orquestrador, salvo
   `--base`.
4. No herdr: cria o worktree com branch `radiant/TC-0025.1` sobre a base,
   abre a aba, inicia o agente e envia o pedido.
5. `demerzel status` combina registro e estado do herdr. `demerzel wait` volta
   quando a unidade termina ou trava.
6. `demerzel collect` lê o retorno em `.radiant/reports/TC-0025.1.md` no
   worktree e o entrega ao orquestrador, que faz readback e aceite.

## 4. Erros, HOLD e segurança

Todas as verificações rodam antes do primeiro efeito. Recusas saem com `2`,
sem criar nada. O Demerzel recusa quando:

- o pin diverge;
- a unidade não existe ou o bloco `radiant-units` é inválido;
- uma dependência não terminou;
- os paths graváveis se sobrepõem a uma unidade em andamento;
- nenhum candidato da regra é viável;
- o harness não tem adapter Radiant;
- o herdr não está rodando ou está abaixo da versão mínima;
- o branch ou o path do worktree já existe;
- `.radiant/reports/` não é ignorado pelo Git no consumidor;
- a regra exige `approval: human` e a chamada não traz a confirmação.

Demais regras:

- Falha depois do primeiro efeito marca `launch-failed` e lista o que foi
  criado. Worktree e branch nunca são apagados sem flag explícita de descarte
  dada pelo humano.
- Em `blocked`, o Demerzel reporta ao orquestrador, que leva ao humano. Nunca
  responde prompts de permissão. Só envia o pedido inicial e seguimentos que o
  orquestrador pedir, todos registrados.
- Se só houver candidato com capacidade menor que a pedida, a unidade fica em
  HOLD. Não há rebaixamento silencioso.
- O Demerzel nunca faz merge, push, abertura de PR, remoção de branch ou
  mudança de escopo, nem passa secrets no pedido. O pedido leva só paths, e o
  conteúdo do contrato não sai da máquina (Artigo XII).
- `--trust-repository` só é usado quando o usuário liga a opção na
  configuração do Demerzel. Sem isso, um prompt de confiança aparece como
  `blocked`.
- Ao iniciar, o registro é reconciliado com `herdr api snapshot`. Aba sumida
  vira `lost` e não é relançada sozinha.
- Um lock por projeto serializa despachos.

## 5. Verificação e primeiro incremento

### Ordem de entrega

1. PR no Radiant com as mudanças da seção 2, extensões do
   `check_repository.py` (cada `provides` usa o vocabulário; o exemplo de
   regras e o bloco de exemplo do template passam no schema), testes pelos
   comandos reais e este ADR. Merge, e o ADR passa a `accepted`.
2. Repositório do Demerzel criado pelo owner, com `.radiant.json` no commit de
   merge, `AGENTS.md` do template, Frame, Spec e Plan.
3. Primeiro contrato do Demerzel: `dispatch`, `status`, `wait`, `collect` e
   `close`, com registro, gate de pin, recusas da seção 4 e backend herdr para
   Claude Code e Codex. A interface de observação é um incremento posterior.

### Menor experimento

Um contrato real com duas unidades independentes num consumidor real, uma
roteada para Claude Code e outra para Codex, ambas em abas do herdr, com
`collect` devolvendo os dois Completion reports e o orquestrador fazendo o
aceite. Evidência: registro de despachos, snapshot do herdr, os relatórios e os
diffs.

A hipótese é refutada quando:

- despachar custa mais tempo ou atenção do owner do que montar à mão;
- a maioria dos contratos precisa de amendment na divisão;
- o lançamento trava com frequência em prompts de confiança ou autenticação;
- o orquestrador ainda precisa colar contexto no pedido.

### Testes do Demerzel

Cada teste nomeia o comportamento que protege e a regressão que o faria
falhar, conforme o gate do `test-audit` do eve.

- Unidade: leitor de contrato, roteador, montador do pedido e transições do
  registro.
- Integração: fluxo completo com backend falso em memória, incluindo cada
  recusa sem efeito.
- Cenário local: backend herdr contra o herdr real numa sessão isolada.
- Smoke com harness real: Claude Code e Codex, registrado na verificação do
  contrato.

## Fora de escopo

- Interface de observação e gestão, que terá desenho próprio.
- Adapters Radiant para outros harnesses.
- Backends além do herdr.
- Execução em nuvem ou em host remoto.
- Escolha automática de regra sem o orquestrador.
- Alterações na Constitution.

## Arquivos previstos no Radiant

| Ação | Path |
| --- | --- |
| Alterar | `templates/task-contract.md` (seção de divisão) |
| Criar | `skills/radiant-delegation/requirements.json` |
| Criar | `adapters/claude-code/provides.json`, `adapters/codex/provides.json` |
| Criar | `docs/routing.md` e `docs/routing.example.json` |
| Alterar | `skills/radiant-delegation/SKILL.md` (despacho por backend, proveniência) |
| Alterar | `docs/integration.md`, `docs/project-generation-system.md` (nota na seção 30), `docs/capabilities.md`, `README.md` |
| Alterar | `validators/check_repository.py`, `tests/test_repository.py` |

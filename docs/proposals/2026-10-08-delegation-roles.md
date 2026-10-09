# Proposta: papéis, níveis de capacidade e delegação

- Data: 2026-10-08
- Estado: proposta aprovada em conversa; aguardando revisão do texto escrito
- Owner: Fael
- Revisão de origem do Radiant: `160ef8edddd5893169e5c9d9d5375dd25be802b3`

## Intenção

Permitir que projetos conduzidos pelo Radiant sejam tocados por papéis
especializados (Ideação, Design, Dev, Verificador e Manutenção) coordenados por
um orquestrador, com aprovação humana entre fases, sem amarrar o Radiant a um
harness ou modelo.

Dois resultados são esperados:

1. Radiant explicitamente agnóstico a harness: o mesmo core é consumido por
   pelo menos dois adapters (Codex e Claude Code).
2. Custo proporcional ao trabalho: o orquestrador usa o nível mais capaz e o
   trabalho delimitado é delegado a níveis mais baratos, sem enfraquecer
   crítica e verificação.

## Contexto e restrições

- O ciclo Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify
  → Learn Back já cobre Ideação, Design e Dev. Manutenção contínua não tem
  etapa correspondente.
- A [Constitution](../../constitution/CONSTITUTION.md) exige: core independente
  de ferramenta (Artigo XIV), um corpo canônico (Artigo XI), autonomia
  proporcional à reversibilidade (Artigo IV), verificação e crítica
  independentes (Artigos VII e VIII), agência humana (Artigo XIII), default
  deny para egress (Artigo XII) e simplicidade (Artigo XVII). Nomes de modelo
  não pertencem ao core (seção 7).
- Só existe o [adapter Codex](../../adapters/codex/README.md). O template de
  consumidor e o `AGENTS.md` do AIKM apontam diretamente para ele.
- Skills externas (por exemplo superpowers e design-superpowers) produzem
  artefatos em paths próprios, concorrentes com os do Radiant.

## Decisões

| Decisão | Escolha |
| --- | --- |
| Onde vivem os papéis | Core agnóstico; adapters traduzem para cada harness |
| Escolha de nível | Padrão por papel, com override justificado no Task Contract |
| Skills externas | Radiant canônico; skills externas são procedimentos opcionais apontados pelo adapter |
| Autonomia da Manutenção | Só propõe; a única escrita é o próprio relatório |
| Piloto | AIKM, começando por uma execução de Manutenção |
| Estrutura no core | Skill `radiant-delegation` e skill `radiant-maintenance`; `radiant-cycle` recebe apenas ponteiros |

Alternativas descartadas: papéis somente no adapter (prende papéis a um
harness), papéis fora do Radiant (sem Learn Back nem pin), nível fixo por papel
(rígido), nível decidido caso a caso pelo orquestrador (imprevisível e sem
proveniência), tudo dentro de `radiant-cycle` (skill carregada por todos cresce
sem necessidade) e uma skill por time (duplica o procedimento do ciclo).

## 1. Papéis e níveis

### Níveis de capacidade

O core define níveis abstratos. Cada adapter mapeia níveis para modelos.

| Nível | Uso |
| --- | --- |
| `deep` | Julgamento, crítica, decisões caras e aceite |
| `standard` | Execução delimitada por artefato aprovado |
| `light` | Busca, coleta, checks mecânicos e resumo |

### Papéis

| Papel | Etapas | Nível padrão | Produz |
| --- | --- | --- | --- |
| Orquestrador | Coordenação de todas | `deep` | Pacotes de delegação, decisões de gate, aceite final |
| Ideação | Frame, Challenge | `deep` para Grill; `light` para pesquisa | Frame e Challenge registrados |
| Design | Spec, Design | `deep` para System Design e ADR; `standard` para Design Spec derivado de Frame aprovado | Spec, Design Frame, Design Spec, ADRs |
| Dev | Plan, Contract, Build | `standard`; `light` para tarefas mecânicas | Plano, contratos propostos, diff |
| Verificador | Verify | `deep` para aceite; `light` para checks determinísticos | Relatório de verificação |
| Manutenção | Fora do ciclo; alimenta Frame | `light` para coleta; `standard` para priorização | Relatório de manutenção com propostas |

### Regras

1. Interação humana pertence ao orquestrador. Papéis delegados não conversam
   com o humano; perguntas de enquadramento, Challenge e aprovações passam pela
   sessão principal.
2. Quem verifica não fica abaixo do nível de quem produziu. Um aceite usa nível
   igual ou superior ao do autor, ou um verificador determinístico.
3. Override de nível somente pelo Task Contract, em campo opcional `tier` com
   justificativa de uma linha, registrado na evidência de execução.
4. Não são delegadas: mudança de escopo, ativação de contrato, ações
   irreversíveis e aceitação de conhecimento canônico.
5. Delegar é opcional. Sem suporte do harness a subagentes, ou em tarefa
   pequena, o orquestrador executa o papel na própria sessão com as mesmas
   entradas e saídas.
6. Exceção do orquestrador: em execução agendada de Manutenção, que apenas
   propõe, o orquestrador pode operar em `standard`.

## 2. Handoff e retorno

### Pacote de delegação

Contém ponteiros, não cópias:

- papel e nível efetivo;
- objetivo em uma ou duas frases;
- entradas: paths de artefatos e revisão do Radiant;
- fronteira: paths graváveis, paths somente leitura e non-goals;
- saída esperada e formato do retorno;
- condições de `HOLD`.

Para Build, o Task Contract é o pacote; o handoff aponta para ele. Para
trabalhos pequenos (pesquisa, Grill, coleta), o pacote vai no próprio pedido e
não vira arquivo.

### Retorno

- estado: `DONE`, `HOLD` ou `FAIL`;
- outputs: paths criados ou alterados;
- evidência: comandos e resultados efetivos, incluindo bloqueios;
- desvios: ambiguidades e o que ficou fora da fronteira;
- findings candidatos a Learn Back.

O retorno é um resumo, não um despejo de conteúdo.

### Tratamento pelo orquestrador

1. Não aceita `DONE` apenas pelo relato. Faz readback do diff, executa checks e
   confronta com o contrato; encaminha ao Verificador quando o risco pedir.
2. `HOLD` é resolvido dentro da autorização vigente ou levado ao humano.
3. `FAIL` preserva evidência e segue para Learn Back.

### Paralelismo

Somente entre tarefas independentes com paths de escrita disjuntos. Na dúvida,
execução sequencial.

### Proveniência de custo

O relatório de verificação do contrato registra cada delegação: papel, nível,
modelo efetivo resolvido pelo adapter e estado. Nomes de modelo aparecem apenas
na evidência do consumidor.

## 3. Manutenção

### Fontes observadas (somente leitura)

| Fonte | Candidatos típicos |
| --- | --- |
| Estado do ciclo | Contrato `held` esquecido; Learning Record com `fixTarget` sem correção |
| Gates do projeto | Falhas nos comandos de verificação do workflow ou Engineering Profile |
| Drift | Spec ou Plan em desacordo com o código; links quebrados nos artefatos |
| Dependências | Versões desatualizadas ou vulneráveis |
| Forge | Issues abertas; falhas de CI na branch principal |
| Pin do Radiant | Revisão mais nova disponível, como candidato e nunca como atualização automática |

Fontes que enviam informação para fora (registry de pacotes, forge) só são
consultadas quando o workflow do consumidor autoriza explicitamente. Sem
autorização, a fonte é pulada e o relatório registra a omissão.

### Relatório

Uma execução produz um relatório com:

- candidatos priorizados por risco, valor e reversibilidade, cada um com
  evidência concreta (saída de comando, path, linha);
- comparação com o relatório anterior: novo, recorrente, resolvido;
- rascunho de contrato embutido para até três candidatos do topo (objetivo,
  outputs, verificação).

Rascunhos não viram arquivos `TC-xxxx`. O contrato com ID é criado pelo
orquestrador somente quando o humano seleciona um candidato.

### Localização e fronteira

- Novo campo opcional `maintenance` em `.radiant.json`: diretório relativo ou
  `null`. Campo ausente equivale a `null`, para não exigir mudança em
  consumidores existentes.
- A única escrita permitida é o relatório. Sem branch, PR, issue ou commit.
- Agendamento e frequência pertencem ao adapter e ao workflow do consumidor.

## 4. Adapters

### Claude Code (novo, `adapters/claude-code/`)

- Bootstrap global: bloco `radiant:begin/end` gerado a partir do checkout para
  o arquivo de instruções globais do usuário, preservando o restante e
  removível isoladamente.
- Gerador único: o script atual passa a aceitar `--adapter codex|claude-code`,
  com um template por adapter. A saída Codex permanece compatível.
- Subagentes finos gerados no diretório de agentes do usuário, fora do Git,
  regeneráveis e sem sobrescrever arquivos existentes: `radiant-research`
  (`light`), `radiant-grill` (`deep`), `radiant-design` (`standard`),
  `radiant-dev` (`standard`), `radiant-verifier` (`deep`) e
  `radiant-maintenance` (`standard`). O corpo contém apenas frontmatter e
  ponteiro para a seção do papel em `radiant-delegation`.
- Override de nível usa o parâmetro de modelo da delegação do harness, sem um
  arquivo por combinação.
- Tabela única de mapeamento nível → modelo no README do adapter.
- Rotinas de Manutenção: execução local agendada (código não sai da máquina) ou
  rotina em nuvem (decisão de egress que o workflow precisa autorizar).
- Tabela opcional papel → procedimento externo sugerido. Regra explícita: a
  saída vai para os paths do `.radiant.json`, nunca para paths padrão da skill
  externa.

### Codex (ajuste mínimo)

- Recebe a tabela de níveis e a declaração de como delega.
- Suporte a subagentes e modelos disponíveis são confirmados na documentação
  oficial durante a implementação. Sem suporte, delegação é execução
  sequencial na sessão.

### Consumidores

- `project.AGENTS.template.md` passa a ser um mapa neutro de harness, que manda
  ler o adapter do harness em uso.
- Consumidores que usam Claude Code têm um `CLAUDE.md` de uma linha com
  `@AGENTS.md`, mantendo um único corpo.
- O próprio Radiant recebe o mesmo `CLAUDE.md` de uma linha.

## 5. Verificação e piloto

### Verificação determinística no Radiant

- Testes do gerador com `--adapter claude-code`: bloco global, seis
  subagentes, recusa de sobrescrita e path com espaços.
- Regressão: saída de `--adapter codex` igual à atual, exceto mudanças
  intencionais.
- `check_project.py`: `maintenance` com `null`, diretório válido, path que
  escapa do projeto (rejeitado) e campo ausente (aceito).
- `check_repository.py`: todo adapter mapeia os três níveis definidos em
  `radiant-delegation`.
- [Verification](../verification.md): simulação D (entrada pelo Claude Code) e
  critério de agnosticismo de harness na revisão estrutural.

### Piloto no AIKM

| Etapa | Ação | Evidência |
| --- | --- | --- |
| 0. Adoção | Pin atualizado para o commit de merge, `AGENTS.md` neutro, `CLAUDE.md` de uma linha, campo `maintenance` | `check_project.py` aprovado |
| 1. Sessão nova | Sessão Claude Code nova identifica pointer, valida pin e carrega Constitution e mapa sem ajuda | Transcrição |
| 2. Manutenção | Execução manual, depois uma agendada | Relatório com evidência; `git status` mostra apenas o relatório |
| 3. Ciclo | Humano seleciona candidato; TC-0019 percorre os papéis até `DONE` | Relatório de verificação com delegações registradas |
| 4. Learn Back | Findings sobre o Radiant roteados ao owner | Learning Record e mudança ou pendência |
| 5. Regressão Codex | Humano confirma que uma sessão Codex no AIKM continua validando | Confirmação registrada |

### Critérios de sucesso

- Etapas 1 a 5 concluídas sem intervenção fora dos gates previstos.
- Nenhum aceite feito por nível inferior ao do autor.
- Divisão de uso por nível registrada como linha de base. Não há meta numérica
  neste piloto; limitações de medição por subagente são registradas.

### Ordem de entrega

1. PR no Radiant: core, adapters e validators.
2. Merge na `main`.
3. PR no AIKM: adoção com pin no commit de merge, seguida do ciclo TC-0019.

## Fora de escopo

- Execução automática de correções pela Manutenção.
- Board externo (GitHub Projects, Notion); o estado continua nos artefatos do
  consumidor e em `ACTIVE.md`.
- Adapters para outros harnesses além de Claude Code e Codex.
- Metas numéricas de custo.
- Alterações na Constitution. Se o piloto mostrar um invariante novo, ele segue
  o fluxo constitucional de proposta.

## Arquivos previstos

| Ação | Path |
| --- | --- |
| Criar | `skills/radiant-delegation/SKILL.md` |
| Criar | `skills/radiant-maintenance/SKILL.md` |
| Criar | `templates/maintenance-report.md` |
| Criar | `adapters/claude-code/README.md`, templates global e de subagente |
| Criar | `CLAUDE.md` na raiz do Radiant |
| Alterar | `skills/radiant-cycle/SKILL.md` (ponteiros) |
| Alterar | `adapters/codex/` (níveis, delegação, gerador) |
| Alterar | `templates/task-contract.md` (campo `tier`), `templates/radiant-project.json` (`maintenance`) |
| Alterar | `docs/capabilities.md`, `docs/integration.md`, `docs/verification.md`, `docs/learn-back.md`, `README.md`, `AGENTS.md` |
| Alterar | `validators/check_project.py`, `validators/check_repository.py`, `tests/test_integration.py` |

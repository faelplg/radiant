# ADR-0001: papéis, capacidades e delegação

- Data: 2026-10-08
- Estado: `accepted` em 2026-10-09
- Owner: Fael
- Revisão de origem do Radiant: `160ef8edddd5893169e5c9d9d5375dd25be802b3`
- Implementação: PR #2, merge `6074810e6d3ca3cc8f591b78d62272b26b6428a9`

As regras operacionais vivem em
[radiant-delegation](../../skills/radiant-delegation/SKILL.md),
[radiant-maintenance](../../skills/radiant-maintenance/SKILL.md) e nos
adapters. Em caso de divergência, esses corpos prevalecem; este ADR permanece
como registro da decisão e do design que orientou a implementação.

## Intenção

Permitir que projetos conduzidos pelo Radiant sejam tocados por papéis
especializados (Ideação, Design, Dev, Verificador e Manutenção) coordenados por
um orquestrador, com aprovação humana entre fases, sem amarrar o Radiant a um
harness ou modelo.

Dois resultados são esperados:

1. Radiant explicitamente agnóstico a harness: o mesmo core é consumido por
   dois adapters que delegam de fato (Codex e Claude Code).
2. Custo proporcional ao trabalho: o orquestrador usa a capacidade mais alta e
   o trabalho delimitado é delegado a capacidades mais baratas, sem enfraquecer
   crítica e verificação.

## Contexto e restrições

- O ciclo Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify
  → Learn Back já cobre Ideação, Design e Dev. Manutenção contínua não tem
  etapa correspondente.
- A [Constitution](../../constitution/CONSTITUTION.md) exige: core independente
  de ferramenta (Artigo XIV), um corpo canônico (Artigo XI), autonomia
  proporcional à reversibilidade (Artigo IV), verificação e crítica
  independentes (Artigos VII e VIII), agência humana (Artigo XIII), default
  deny para egress (Artigo XII), proveniência (Artigo X) e simplicidade
  (Artigo XVII). Nomes de modelo não pertencem ao core (seção 7).
- Só existe o [adapter Codex](../../adapters/codex/README.md). O template de
  consumidor e o `AGENTS.md` do AIKM apontam diretamente para ele.
- Skills externas (por exemplo superpowers e design-superpowers) produzem
  artefatos em paths próprios, concorrentes com os do Radiant.
- Fatos de harness conferidos na documentação oficial em 2026-10-09:
  - Claude Code: subagentes em Markdown com frontmatter em `~/.claude/agents/`;
    `model` do frontmatter aceita ID completo. O parâmetro `model` da
    invocação prevalece sobre o frontmatter, mas aceita apenas aliases de
    família (`sonnet`, `opus`, `haiku`, `fable`), que não identificam o
    modelo efetivo. Subagentes podem criar subagentes até três camadas
    abaixo da sessão principal; a criação é bloqueada por agente com
    `disallowedTools: Agent`.
  - Codex: subagentes em TOML em `~/.codex/agents/`, com `name`,
    `description` e `developer_instructions` obrigatórios e `model` opcional.
    O `model` declarado no arquivo do agente prevalece sobre o valor passado na
    criação. Não há limite de profundidade documentado.
- O [template de Task Contract](../../templates/task-contract.md) já possui
  `Risk tier`, `Independent critique` e `Completion report`, reutilizados por
  esta decisão.

## Decisões

| Decisão | Escolha |
| --- | --- |
| Onde vivem os papéis | Core agnóstico; adapters traduzem para cada harness |
| Nome do conceito | Capacidade (`deep`, `standard`, `light`); campo `Capability` no contrato |
| Escolha da capacidade | Padrão por papel, com override justificado no Task Contract |
| Aceite independente | Uma vez por contrato em `deep`; antecipado quando `Risk tier` ≥ 2 ou `Independent critique: REQUIRED` |
| Proveniência de modelo | Adapters mapeiam capacidade para ID completo de modelo, não alias |
| Skills externas | Radiant canônico; skills externas são procedimentos opcionais apontados pelo adapter |
| Autonomia da Manutenção | Só propõe; a única escrita é o relatório, em diretório ignorado pelo Git |
| Execução da Manutenção | Somente local; rotinas em nuvem fora de escopo |
| Política da Manutenção | Comandos seguros e egress autorizados declarados no workflow do consumidor |
| Estrutura no core | Skills `radiant-delegation` e `radiant-maintenance`; `radiant-cycle` recebe apenas ponteiros |
| Adapters | Claude Code novo e Codex completo, ambos gerando os seis subagentes |
| Piloto | AIKM: adoção como TC-0019; ciclo do candidato da Manutenção como TC-0020 |

Alternativas descartadas:

- Papéis somente no adapter: prende papéis a um harness.
- Papéis fora do Radiant: sem Learn Back nem pin.
- Capacidade fixa por papel: rígida para tarefas difíceis.
- Capacidade decidida caso a caso pelo orquestrador: imprevisível e sem
  proveniência.
- Tudo dentro de `radiant-cycle`: a skill carregada por todos cresce sem
  necessidade.
- Uma skill por time: duplica o procedimento do ciclo.
- Aceite `deep` por tarefa: anula a economia de delegar Build.
- Aliases de modelo: a evidência deixa de identificar o modelo efetivo.
- Relatório de Manutenção versionado ou publicado no forge: conflita com
  trabalho em andamento ou exige escrita e egress externos.
- Política de Manutenção em campos do `.radiant.json`: transforma o mapa de
  paths em arquivo de política.
- Adapter Codex mínimo: deixa a separação core/adapter sem teste real.
- Termo `tier`: colide com `Risk tier` dos contratos existentes.

## 1. Papéis e capacidades

### Capacidades

O core define capacidades abstratas. Cada adapter mapeia capacidades para IDs
completos de modelo.

| Capacidade | Uso |
| --- | --- |
| `deep` | Julgamento, crítica, decisões caras e aceite |
| `standard` | Execução delimitada por artefato aprovado |
| `light` | Busca, coleta, checks mecânicos e resumo |

### Papéis

| Papel | Etapas | Capacidade padrão | Produz |
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
2. Aceite nunca usa capacidade inferior à do autor. Por tarefa, valem checks
   determinísticos e o readback do orquestrador `deep`. O Verificador `deep`
   dedicado faz o aceite do contrato uma vez, ao final, e é antecipado quando
   `Risk tier` ≥ 2 ou `Independent critique: REQUIRED`.
3. Override de capacidade somente pelo Task Contract, em campo opcional
   `Capability` com justificativa de uma linha, registrado na evidência de
   execução.
4. Não são delegadas: mudança de escopo, ativação de contrato, ações
   irreversíveis e aceitação de conhecimento canônico.
5. Delegar é opcional. Sem suporte do harness, ou em tarefa pequena, o
   orquestrador executa o papel na própria sessão com as mesmas entradas e
   saídas. O mesmo vale quando o harness não permite o override pedido.
6. Exceção do orquestrador: em execução de Manutenção, que apenas propõe, o
   orquestrador pode operar em `standard`.
7. Papéis delegados não delegam. Toda delegação parte do orquestrador, para
   que cada uma fique registrada na proveniência de custo e respeite a regra
   de aceite.

## 2. Handoff e retorno

### Pacote de delegação

Contém ponteiros, não cópias:

- papel e capacidade efetiva;
- objetivo em uma ou duas frases;
- entradas: paths de artefatos e revisão do Radiant;
- fronteira: paths graváveis, paths somente leitura e non-goals;
- saída esperada e formato do retorno;
- condições de `HOLD`.

Para Build, o Task Contract é o pacote; o handoff aponta para ele. Para
trabalhos pequenos (pesquisa, Grill, coleta), o pacote vai no próprio pedido e
não vira arquivo.

### Retorno

Para Build, o retorno é o `Completion report` do Task Contract. Para os demais
papéis, o retorno contém:

- estado: `DONE`, `HOLD` ou `FAIL`;
- outputs: paths criados ou alterados;
- evidência: comandos e resultados efetivos, incluindo bloqueios;
- desvios: ambiguidades e o que ficou fora da fronteira;
- findings candidatos a Learn Back.

O retorno é um resumo, não um despejo de conteúdo.

### Tratamento pelo orquestrador

1. Não aceita `DONE` apenas pelo relato. Faz readback do diff, executa checks e
   confronta com o contrato.
2. `HOLD` é resolvido dentro da autorização vigente ou levado ao humano.
3. `FAIL` preserva evidência e segue para Learn Back.

### Paralelismo

Somente entre tarefas independentes com paths de escrita disjuntos. Na dúvida,
execução sequencial.

### Proveniência de custo

O relatório de verificação do contrato registra cada delegação: papel,
capacidade, ID completo do modelo resolvido pelo adapter e estado. IDs de
modelo aparecem apenas na evidência do consumidor e nos adapters.

## 3. Manutenção

### Fontes observadas

| Fonte | Candidatos típicos |
| --- | --- |
| Estado do ciclo | Contrato `held` esquecido; Learning Record com `fixTarget` sem correção |
| Gates do projeto | Falhas nos comandos declarados seguros para manutenção |
| Drift | Spec ou Plan em desacordo com o código; links quebrados nos artefatos |
| Dependências | Versões desatualizadas ou vulneráveis |
| Forge | Issues abertas; falhas de CI na branch principal |
| Pin do Radiant | Revisão mais nova disponível, como candidato e nunca como atualização automática |

### Política declarada pelo consumidor

O documento de `workflow` do consumidor contém uma seção de Manutenção com:

- comandos seguros para manutenção: somente estes são executados; os demais
  são pulados e registrados como omitidos;
- fontes externas autorizadas (registry de pacotes, forge): sem autorização,
  a fonte é pulada e a omissão é registrada.

### Relatório

Uma execução produz um relatório, conforme `templates/maintenance-report.md`,
com:

- candidatos priorizados por risco, valor e reversibilidade, cada um com
  evidência concreta (saída de comando, path, linha);
- comparação com o relatório anterior: novo, recorrente, resolvido;
- rascunho de contrato embutido para até três candidatos do topo (objetivo,
  outputs, verificação).

Rascunhos não viram arquivos `TC-xxxx`. O contrato com ID é criado pelo
orquestrador somente quando o humano seleciona um candidato. Uma execução que
conclui "nada material" é resultado válido.

### Localização e fronteira

- Novo campo opcional `maintenance` em `.radiant.json`: diretório relativo ou
  `null`. Campo ausente equivale a `null`.
- O diretório é ignorado pelo Git no consumidor. O validator exige apenas path
  relativo dentro do projeto e aceita que ele não exista; a skill o cria na
  primeira execução. A exceção vale somente para este campo.
- A única escrita permitida é o relatório. Sem branch, PR, issue ou commit.
- Execução somente local, manual ou agendada na máquina do usuário.

## 4. Adapters

### Comum aos adapters

- Gerador único: o script atual passa a aceitar `--adapter codex|claude-code`,
  com templates por adapter. A saída Codex existente permanece compatível.
- Seis subagentes finos, gerados no diretório de agentes do usuário, fora do
  Git, regeneráveis e sem sobrescrever arquivos existentes: `radiant-research`
  (`light`), `radiant-grill` (`deep`), `radiant-design` (`standard`),
  `radiant-dev` (`standard`), `radiant-verifier` (`deep`) e
  `radiant-maintenance` (`standard`). O corpo contém apenas metadados do
  harness e ponteiro para a seção do papel em `radiant-delegation`.
- Mapa único capacidade → ID completo de modelo em `capabilities.json` de
  cada adapter, referenciado pelo README.
- Tabela opcional papel → procedimento externo sugerido. Regra explícita: a
  saída vai para os paths do `.radiant.json`, nunca para paths padrão da skill
  externa.

### Claude Code (novo, `adapters/claude-code/`)

- Bootstrap global: bloco `radiant:begin/end` para o arquivo de instruções
  globais do usuário, preservando o restante e removível isoladamente.
- Subagentes em Markdown com frontmatter, no diretório de agentes do usuário,
  com `disallowedTools: Agent` para aplicar a regra 7.
- Override de capacidade não usa o parâmetro `model` da invocação, que só
  aceita aliases: o papel com capacidade alterada roda na sessão do
  orquestrador (regra 5), como no Codex.

### Codex (`adapters/codex/`)

- Mantém o bootstrap atual.
- Subagentes em TOML no diretório de agentes do usuário. A regra 7 fica nas
  instruções do agente, porque o Codex não documenta bloqueio por agente.
- Como o `model` do arquivo prevalece, o override de capacidade não é
  possível na criação: o papel com capacidade alterada roda na sessão do
  orquestrador (regra 5).

### Consumidores

- O template de `AGENTS.md` do consumidor sai de `adapters/codex/` e passa a
  ser um mapa neutro de harness em `templates/`, que manda ler o adapter do
  harness em uso.
- Consumidores que usam Claude Code têm um `CLAUDE.md` de uma linha com
  `@AGENTS.md`, mantendo um único corpo.
- O próprio Radiant recebe o mesmo `CLAUDE.md` de uma linha.

## 5. Verificação e piloto

### Verificação determinística no Radiant

- Testes do gerador com cada adapter: bloco global, seis subagentes, recusa de
  sobrescrita e path com espaços.
- Regressão: bloco global Codex igual ao atual, exceto mudanças intencionais.
- `check_project.py`: `maintenance` com `null`, diretório existente, diretório
  inexistente (aceito), path que escapa do projeto (rejeitado) e campo ausente
  (aceito).
- `check_repository.py`: todo adapter mapeia as três capacidades definidas em
  `radiant-delegation`.
- [Verification](../verification.md): simulação D (entrada pelo Claude Code) e
  critério de agnosticismo de harness na revisão estrutural.

### Piloto no AIKM

| Etapa | Ação | Evidência |
| --- | --- | --- |
| 0. Adoção (TC-0019) | Pin no commit de merge, `AGENTS.md` neutro, `CLAUDE.md` de uma linha, campo `maintenance`, `.gitignore` e seção de Manutenção no workflow | `check_project.py` aprovado |
| 1. Sessão nova | Sessão Claude Code nova identifica pointer, valida pin e carrega Constitution e mapa sem ajuda | Transcrição |
| 2. Manutenção | Execução manual, depois uma agendada localmente | Relatório com evidência; `git status` sem mudanças rastreadas |
| 3. Ciclo (TC-0020) | Humano seleciona candidato do relatório ou, sem candidato material, item do horizonte do Plan; TC-0020 percorre os papéis até `DONE` | Relatório de verificação com delegações registradas |
| 4. Learn Back | Findings sobre o Radiant roteados ao owner | Learning Record e mudança ou pendência |
| 5. Regressão Codex | Humano confirma que uma sessão Codex no AIKM continua validando e delega a um subagente Radiant | Confirmação registrada |

### Critérios de sucesso

- Etapas 1 a 5 concluídas sem intervenção fora dos gates previstos.
- Nenhum aceite com capacidade inferior à do autor.
- Divisão de uso por capacidade registrada como linha de base. Não há meta
  numérica neste piloto; limitações de medição por subagente são registradas.

### Ordem de entrega

1. PR no Radiant: core, adapters, validators e este ADR.
2. Merge na `main`; ADR passa a `accepted` com referência ao commit.
3. PR no AIKM: TC-0019 com pin no commit de merge, seguido do ciclo TC-0020.

## Limitação registrada na revisão do PR

Perfis delegáveis declaram `access` (`read` ou `write`). Perfis de leitura
recebem menor privilégio do harness (`tools` restritas no Claude Code,
`sandbox_mode = "read-only"` no Codex). Fronteiras específicas de cada
contrato nos perfis `write` não são impostas pelo harness: dependem do pacote
e do readback do orquestrador, conforme a seção "Acesso e fronteiras" da skill
de delegação. Enforcement por contrato é candidato a evolução com evidência do
piloto.

## Emendas

- 2026-10-09: o bloco global passa a ser um template único e neutro,
  `adapters/global.template.md`, que indica o adapter de cada harness. Motivo:
  no primeiro uso real, as instruções globais do Claude Code e do Codex eram o
  mesmo arquivo (dotfiles), e um bloco por adapter fazia um harness ler o
  adapter do outro. O gerador imprime o bloco sem `--adapter`, que passa a ser
  exigido só com `--agents-dir`.
- 2026-10-10: o Learn Back do piloto alterou regras operacionais nas skills e
  nos adapters, que prevalecem sobre este registro
  ([PR #5](https://github.com/faelplg/radiant/pull/5) e
  [PR #6](https://github.com/faelplg/radiant/pull/6)). O retorno de Build segue
  a seção 16 do template mesmo quando o contrato não a reproduz. O readback
  confere cada mudança e cada resultado relatados contra o working tree. O
  pacote leva a raiz absoluta do Radiant. A proveniência registra uma linha
  por rodada com a métrica de uso definida pelo adapter, ou a ausência dela.
  Assim, a seção "Proveniência de custo" acima vale com esses acréscimos.

## Resultado do piloto

Registrado em 2026-10-10, com o AIKM em
`31266c690e5b5cf84d2e576a0c73ee93caaa286e` e o Radiant fixado em
`6ad7ad260ab4464023a7eea798530ad85d284faf`.

| Etapa | Evidência | Situação |
| --- | --- | --- |
| 0. Adoção | TC-0019, [AIKM PR #13](https://github.com/faelplg/aikm/pull/13) | Concluída |
| 1. Sessão nova | Sessões Claude Code e Codex abertas pelo owner localizaram e validaram o core sem ajuda (relatório do TC-0019) | Concluída |
| 2. Manutenção | Execução manual em 2026-10-09 e execução agendada localmente em 2026-10-10, com `radiant-maintenance` 0.1.1 ([PR #8](https://github.com/faelplg/radiant/pull/8)); relatórios com evidência e `git status` limpo | Concluída, com desvio: a sessão agendada rodou em `deep`, não em `standard` |
| 3. Ciclo | TC-0020, [AIKM PR #14](https://github.com/faelplg/aikm/pull/14), com Build, verificação e pesquisa delegados; TC-0021 e TC-0022 repetiram o ciclo | Concluída |
| 4. Learn Back | LR-0002 do AIKM, [AIKM PR #17](https://github.com/faelplg/aikm/pull/17), e [PR #5](https://github.com/faelplg/radiant/pull/5) | Concluída |
| 5. Regressão Codex | VR-0006 do AIKM, [AIKM PR #18](https://github.com/faelplg/aikm/pull/18): gate e uma delegação somente leitura; métrica no [PR #6](https://github.com/faelplg/radiant/pull/6) | Concluída, sem Build pelo Codex |

Critérios de sucesso: atendidos parcialmente. As etapas foram concluídas, mas
não sem intervenção fora dos gates previstos, e a sessão agendada da Manutenção
rodou em capacidade diferente da pedida.

- Intervenção fora dos gates: não atendido. Houve duas, ambas decisões do owner e
  registradas no consumidor. Uma esclareceu o alcance de "error messages" no
  TC-0020, depois do fechamento. A outra dispensou um critério inviável no
  TC-0022 (emenda A3). As duas motivaram a regra de referente dos critérios no
  template.
- Aceite com capacidade inferior à do autor: nenhum. Builds `standard` foram
  aceitos por verificador `deep` ou pelo orquestrador `deep` com o owner.
- Linha de base de uso: registrada por rodada nos relatórios do consumidor. No
  Claude Code, rodadas de Build `standard` ficaram entre 87 mil e 112 mil
  tokens de contexto, e de verificação `deep`, entre 122 mil e 165 mil; a
  pesquisa `light` ficou em cerca de 46 mil. No Codex, a rodada `light` teve
  72 mil de contexto e 303 mil acumulados. As métricas dos dois harnesses não
  são diretamente comparáveis, e nenhuma delas é custo cobrado.

Na execução agendada, a comparação com o relatório anterior manteve os IDs dos
candidatos pendentes, inclusive os vindos de adendos, e não marcou como
resolvido um candidato cujo alvo não mudou. O modelo da sessão vem da tarefa
agendada, não do adapter; a execução registrou o modelo efetivo e o desvio.

Pendências: definir como uma execução agendada usa a capacidade `standard`; um
Build delegado pelo Codex; e a evidência para enforcement de fronteiras por
contrato, prevista na limitação registrada acima, que o piloto não produziu.

## Fora de escopo

- Execução automática de correções pela Manutenção.
- Rotinas de Manutenção em nuvem.
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
| Criar | `adapters/claude-code/README.md`, template global e template de subagente |
| Criar | Template de subagente TOML em `adapters/codex/` |
| Criar | `CLAUDE.md` na raiz do Radiant |
| Alterar | `skills/radiant-cycle/SKILL.md` (ponteiros) |
| Alterar | `adapters/codex/README.md` e gerador (`--adapter`, subagentes, capacidades) |
| Alterar | `templates/task-contract.md` (campo `Capability`), `templates/radiant-project.json` (`maintenance`) |
| Mover | `adapters/codex/project.AGENTS.template.md` para `templates/project-agents.md`, como mapa neutro de harness |
| Alterar | `docs/capabilities.md`, `docs/integration.md`, `docs/verification.md`, `docs/learn-back.md`, `README.md`, `AGENTS.md` |
| Alterar | `validators/check_project.py`, `validators/check_repository.py`, `tests/test_integration.py` |

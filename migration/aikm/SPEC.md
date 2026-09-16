---
version: "0.3.1"
status: Especificação revisada para prova antecipada de utilidade
origem: Radiant Project Frame - AI Knowledge Manager (AIKM) v0.2.1
projeto: AI Knowledge Manager
acronimo_interno: AIKM
enquadramento: fael.tech
sistema_de_desenvolvimento: Radiant — Project Generation System v0.2
natureza: Infraestrutura local-first de conhecimento operacional para humanos e agentes
---

# Implementation Spec — AI Knowledge Manager (AIKM)

## 1. Objetivo desta especificação

Esta especificação define o menor sistema implementável capaz de testar as duas hipóteses centrais do AIKM:

> **Conhecimento produzido em um projeto consegue permanecer útil e ser reutilizado em outro sem precisar ser reconstruído?**

e:

> **O resultado de uma execução consegue voltar ao sistema e melhorar uma execução futura?**

A versão 0.2 substitui a visão inicial de um catálogo de artefatos por uma arquitetura de **conhecimento operacional**.

A revisão 0.3, aprovada pelo responsável pelo projeto em 2026-09-15, antecipa a prova de utilidade, distingue entrada de promoção e torna explícita a fronteira de saída de dados. Preserva a hipótese do Frame v0.2 e as decisões do bootstrap. As capacidades abaixo descrevem o comportamento pretendido, não funcionalidades já implementadas.

O sistema continua deliberadamente pequeno.

Ele não pretende implementar uma plataforma completa de knowledge management, memória autônoma ou RAG.

Seu objetivo é construir uma base canônica, legível e utilizável por humanos e agentes para provar:

```text
Projeto A
  ↓
Conhecimento preservado
  ↓
Projeto B
  ↓
Conhecimento recuperado e reutilizado
  ↓
Execução verificada
  ↓
Learn Back
  ↓
Sistema melhor para o próximo ciclo
```

# 2. Principais mudanças em relação à v0.1

A v0.2 altera algumas premissas importantes.

## 2.1. `artifactKind` e `knowledgeRole` são eixos diferentes

Na v0.1, `prompt`, `context`, `skill` e `agent` eram tratados como tipos centrais.

Agora:

- `artifactKind` descreve **que forma técnica o recurso possui**;
- `knowledgeRole` descreve **qual função o conteúdo exerce no sistema**.

Exemplo:

```yaml
artifactKind: skill
knowledgeRole: procedure
```

## 2.2. Captura não exige classificação perfeita

A entrada pode começar em `inbox/`.

Depois passa por routing.

Fluxo:

```text
capture → classify → promote | discard
```

## 2.3. Source e synthesis são separados

Originais devem permanecer distinguíveis do conhecimento derivado deles.

Síntese não substitui proveniência.

## 2.4. Experience passa a possuir evidência

Aprendizados podem apontar para:

- projeto;
- artefato;
- execução;
- verificação;
- fonte.

## 2.5. Learn Back passa a ser explícito

Um aprendizado relevante deve conseguir registrar:

- finding;
- evidência;
- diagnóstico;
- `fixTarget`;
- alteração realizada;
- verificação posterior.

## 2.6. Core e adapters são separados

AIKM não pertence ao Codex, Claude Code ou qualquer harness.

O core é compartilhado.

Cada ferramenta possui apenas um adapter fino.

## 2.7. SQLite deixa de ser requisito da primeira versão

A primeira implementação deve tentar provar valor utilizando:

- filesystem;
- Markdown;
- frontmatter;
- links;
- busca textual;
- scripts leves.

Banco derivado só entra quando uma necessidade observada justificar.

## 2.8. Versionamento próprio deixa de ser obrigatório

A v0.1 exigia:

```text
versions/001/
versions/002/
```

Essa estrutura é retirada do MVP.

A primeira versão utiliza:

- Git quando disponível;
- timestamps;
- provenance;
- lifecycle;
- `supersedes` / `replaces`.

Versionamento explícito poderá existir em artefatos que realmente precisem dele.

## 2.9. Visibility e egress são separados

Conteúdo disponível localmente não está automaticamente autorizado a ser enviado para um provider externo.

# 3. Hipótese de produto testada

> **Se conhecimento operacional de IA for preservado em uma estrutura local, legível, classificável, rastreável e independente de ferramentas específicas, então conhecimento produzido em um projeto poderá melhorar decisões e execuções posteriores sem precisar ser reconstruído.**

A hipótese possui três dimensões.

### Continuidade

O conhecimento sobrevive ao projeto em que nasceu.

### Operabilidade

O sistema diferencia knowledge, context, procedures, memory, execution evidence e evaluation.

### Aprendizado

Resultados e falhas conseguem alterar a camada responsável pelo comportamento futuro.

# 4. Critério experimental principal

A implementação não é considerada validada apenas porque os comandos funcionam.

A primeira evidência de produto é:

> **Um conhecimento produzido ou consolidado no Projeto A é recuperado no Projeto B e utilizado de forma suficientemente relevante para evitar reconstrução.**

Evidência complementar:

> **Uma descoberta produzida no Projeto B gera Learn Back e altera uma camada que será utilizada em uma execução posterior.**

## 4.1. Primeiro percurso completo

Antes de automatizar todo o ciclo, demonstrar:

1. preservar um conteúdo real do Projeto A, sem exigir classificação na entrada;
2. organizar e inspecionar somente o item que merece reutilização;
3. iniciar uma tarefa real do Projeto B sem indicar previamente o arquivo que deve ser encontrado;
4. recuperar conteúdo por uma necessidade, abrir a fonte e avaliar sua aplicabilidade;
5. aplicar o conhecimento, verificar o resultado e registrar o trabalho ou erro evitado;
6. quando houver descoberta material, corrigir a camada responsável e verificar a correção.

Busca lexical pode atender à recuperação inicial. Classificação, promoção, contexto dos projetos, registro de reutilização e aprendizado podem começar por edição explícita de arquivos legíveis, com validação dos campos aplicáveis. Não é necessário implementar todos os comandos antes dessa prova.

O primeiro uso pode ser local e humano. A integração mínima com um único harness deve ser testada logo depois, usando o mesmo percurso e a filtragem da seção 50. Uma sessão nova deve descobrir o acervo a partir de configuração persistente e receber a necessidade da tarefa, sem receber o ID, título ou caminho da resposta esperada.

Na revisão 0.3.1, o caso priorizado desse percurso é reutilizar procedimentos do workflow de desenvolvimento em outro produto. Preservar a referência e a versão do procedimento efetivamente aplicado, o contexto adaptado e a evidência de resultado, usando proveniência e notas já previstas. Não criar um motor de execução de workflows no AIKM. A skill usada para construir o produto e seu acionamento pertencem ao [mapa operacional do projeto](WORKFLOW.md), não ao runtime do AIKM.

## 4.2. Possibilidade e utilidade recorrente

Um evento real demonstra possibilidade de reutilização. A utilidade recorrente exige observações em tarefas posteriores, considerando também captura, manutenção, recuperação malsucedida e uso espontâneo. O protocolo de comparação está nas seções 70-71; nenhum desses resultados pode ser inferido apenas de testes automatizados.

# 5. Princípios de implementação

## 5.1. Filesystem canônico

O patrimônio vive em arquivos locais.

Caches, índices, embeddings e bancos são derivados.

## 5.2. Human-readable

O workspace precisa permanecer compreensível sem executar o AIKM.

## 5.3. Local-first

A operação central não depende de serviço remoto.

## 5.4. Portable-by-design

O workspace pode ser:

- copiado;
- versionado;
- arquivado;
- migrado;
- aberto por ferramentas genéricas.

## 5.5. Model-agnostic

Nenhum provider ou modelo define o formato canônico.

## 5.6. Harness-agnostic

Codex, Claude Code ou outro agent são consumidores do AIKM, não proprietários dele.

## 5.7. One body, pointers elsewhere

Conhecimento compartilhado possui uma fonte canônica.

Outros ambientes recebem referências.

## 5.8. Capture cheap, promotion deliberate

Capturar deve ser barato.

Promover algo a conhecimento durável exige mais intenção.

## 5.9. Generated is not canonical

Conteúdo gerado por IA começa como candidato ou conteúdo não verificado.

## 5.10. Retrieval is not verification

Encontrar um item não prova que ele está correto ou que sustenta uma conclusão.

## 5.11. Learn Back closes the loop

Aprendizado relevante deve possuir um destino de correção.

## 5.12. Store selectively

Não armazenar dados apenas porque é possível.

Persistir aquilo que modifica:

- futura recuperação;
- decisão;
- execução;
- verificação;
- capacidade de reutilização.

# 6. Escopo da primeira implementação

## 6.1. Incluir

As capacidades a seguir compõem o horizonte do ciclo. O Plan define a parcela necessária para a primeira prova e condiciona as demais à evidência observada. A prova inicial não exige implementar toda esta lista; capacidades ainda não entregues permanecem explicitamente pendentes.

- workspace local;
- manifest do workspace;
- diretórios semânticos;
- inbox;
- records em Markdown/frontmatter;
- suporte a originais opacos através de sidecar metadata;
- `artifactKind`;
- `knowledgeRole`;
- provenance;
- lifecycle;
- trust;
- visibility;
- egress policy;
- projetos como context;
- relações entre records;
- procedures;
- operational memory baseada em ponteiros;
- execution records seletivos;
- experiences;
- evaluation/findings;
- Learn Back;
- reuse events;
- busca textual;
- retrieval básico;
- adapters finos;
- validação estrutural;
- verificação de secrets;
- `doctor`;
- CLI mínima;
- funcionamento sem IA.

## 6.2. Não incluir

- interface gráfica;
- SaaS;
- contas;
- multi-user;
- equipes;
- colaboração em tempo real;
- sync obrigatório;
- cloud obrigatório;
- marketplace;
- graph database;
- vector database;
- embeddings obrigatórios;
- chat genérico com o vault;
- execução universal de agents;
- memória automática irrestrita;
- ingestão total de históricos;
- observabilidade empresarial;
- billing;
- ACL organizacional completa;
- protocolo público;
- ranking por LLM obrigatório;
- promoção automática de conhecimento gerado.

# 7. Arquitetura conceitual

```text
                    ┌────────────────────────────┐
                    │         AIKM Core          │
                    │                            │
                    │ routing · records · links  │
                    │ retrieval · lifecycle      │
                    │ learn back · security      │
                    └─────────────┬──────────────┘
                                  │
                     canonical filesystem
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
      Human use              CLI / scripts             Adapters
                                                          │
                                     ┌────────────────────┼───────────────────┐
                                     │                    │                   │
                                   Codex              Claude Code           Other
```

O core não deve depender de nenhum adapter.

# 8. Estrutura inicial do workspace

Estrutura proposta:

```text
workspace/
  aikm.yaml
  README.md

  inbox/
  sources/
  knowledge/
  context/
    projects/
  memory/
  procedures/
  actions/
  evaluation/
  outputs/
  archive/

  system/
    INDEX.md
    ROUTER.md
    SECURITY.md

  adapters/

  .aikm/
    cache/
```

## Regras

- os diretórios semânticos representam `knowledgeRole`;
- `archive/` contém records encerrados ou substituídos quando movê-los fizer sentido;
- `system/` contém regras do workspace;
- `adapters/` contém somente integração específica de harness;
- `.aikm/` contém estado derivado ou descartável;
- apagar `.aikm/` não pode apagar conhecimento;
- `README.md` explica como o workspace é utilizado;
- `system/INDEX.md` funciona como mapa curto para humanos e agents.

A estrutura pode evoluir durante o primeiro ciclo.

A semântica é mais importante que a numeração ou o nome exato dos folders.

# 9. Workspace manifest

Arquivo:

```text
aikm.yaml
```

Exemplo:

```yaml
schemaVersion: "0.3"

workspace:
  id: aikm-workspace:fael
  name: Fael AI Knowledge
  createdAt: 2026-09-14T18:00:00-03:00
  defaultLanguage: pt-BR

defaults:
  visibility: private
  egressAllowed: false

features:
  aiAssistance: false
  semanticSearch: false
  derivedDatabase: false
```

## Campos obrigatórios

```text
schemaVersion
workspace.id
workspace.name
workspace.createdAt
defaults.visibility
defaults.egressAllowed
```

# 10. Unidade canônica: AIKM Record

A unidade comum do sistema é chamada nesta versão de **AIKM Record**.

Um record representa algo que merece identidade, metadata, proveniência e possibilidade de relação.

Ele pode representar:

- um prompt;
- uma skill;
- uma source;
- um conceito;
- um contexto de projeto;
- uma decisão;
- um run;
- uma experience;
- uma avaliação;
- um output.

A unidade lógica é comum.

O conteúdo físico pode ser:

- um arquivo Markdown;
- um arquivo opaco acompanhado de sidecar;
- um diretório composto acompanhado de manifest.

# 11. Modelo em dois eixos

## 11.1. `knowledgeRole`

Valores iniciais:

```text
source
knowledge
context
operational-memory
procedure
action
evaluation
output
```

## 11.2. `artifactKind`

Valores iniciais não exaustivos:

```text
document
reference
prompt
context-bundle
skill
agent
workflow
checklist
playbook
configuration
project
decision
run
handoff
experience
finding
rubric
verification
reuse-event
pointer
output
```

A arquitetura deve aceitar novos `artifactKind` sem exigir novos `knowledgeRole`.

# 12. Mapeamento inicial de roles

| Knowledge Role       | Função                                          | Kinds comuns                              |
| -------------------- | ----------------------------------------------- | ----------------------------------------- |
| `source`             | preservar material de origem                    | document, reference                       |
| `knowledge`          | conhecimento sintetizado reutilizável           | document, reference, pattern              |
| `context`            | informação específica de pessoa/projeto/domínio | project, context-bundle, configuration    |
| `operational-memory` | ponteiro curto necessário antes de agir         | pointer                                   |
| `procedure`          | como executar algo repetível                    | skill, workflow, checklist, playbook      |
| `action`             | execução/decisão necessária como evidência      | run, decision, handoff, reuse-event       |
| `evaluation`         | falhas, critérios, verificações e aprendizados  | experience, finding, rubric, verification |
| `output`             | entregável destinado a consumo externo          | output, document                          |

Esse mapa é inicial.

O primeiro ciclo deve testar se todos esses papéis merecem permanecer distintos.

# 13. Representação Markdown

Um record Markdown utiliza frontmatter.

Exemplo:

```yaml
aikmSchema: "0.3"
id: aikm:01K5A7W8QF8Z2Q2R3M8E4XK9TW
title: Code Review Procedure
description: Procedure for reviewing code changes with a bounded verification pass.

knowledgeRole: procedure
artifactKind: skill

lifecycle: active
trust: reviewed

createdAt: 2026-09-14T18:00:00-03:00
modifiedAt: 2026-09-14T18:00:00-03:00

visibility: private
egressAllowed: false

projects:
  - aikm:project:radiant

tags:
  - engineering
  - code-review

origin:
  type: project
  ref: aikm:project:radiant

links: []
# Code Review Procedure
...
```

# 14. Campos mínimos do record

## Obrigatórios na entrada

Um item ainda não classificado é um record em `inbox/` com `lifecycle: candidate`. Ele possui:

```text
aikmSchema
id
title
lifecycle
trust
createdAt
modifiedAt
visibility
egressAllowed
origin.type
```

Captura gera schema, ID, datas, título inicial editável, lifecycle, trust e política restritiva. O título pode vir do nome do arquivo ou da primeira linha não vazia do texto. A origem registra o modo de entrada e a referência disponível, sem inventar autor, ferramenta ou procedência externa. Importar um arquivo não prova que seu conteúdo foi revisado.

`description`, `knowledgeRole` e `artifactKind` podem estar ausentes enquanto o item permanecer candidato no inbox. Ausência significa classificação pendente; não criar um role artificial nem preencher campos com valores fictícios. Campos fornecidos explicitamente devem ser validados mesmo nessa fase.

## Obrigatórios ao organizar ou promover

Além dos campos de entrada, um record fora do inbox ou com `lifecycle: active` exige:

```text
description
knowledgeRole
artifactKind
```

A exceção de entrada acompanha um candidato não classificado quando arquivado; isso não o torna ativo ou classificado. Organização e promoção preservam ID, origem e data de criação e atualizam `modifiedAt`. Operações do AIKM validam a transição antes de persistir. Edições manuais exigem validação posterior antes de consumir o record; operações de leitura devem rejeitar records inválidos com diagnóstico acionável.

## Opcionais em ambas as fases

```text
projects
tags
origin.ref
origin.uri
origin.tool
origin.model
origin.actor
derivedFrom
supersedes
supersededBy
links
verification
```

Campos opcionais não devem ser preenchidos apenas para satisfazer aparência de completude.

O usuário precisa fornecer o conteúdo ou sua localização para capturar. Classificação ambígua, revisão de confiança, promoção e mudança de política podem exigir decisão posterior. A captura simples não abre um questionário de metadata.

# 15. Identificadores

IDs devem ser:

- estáveis;
- independentes do nome do arquivo;
- independentes do título;
- adequados para referências entre records.

Formato sugerido:

```text
aikm:<ulid>
```

Exemplo:

```text
aikm:01K5A7W8QF8Z2Q2R3M8E4XK9TW
```

Records de projeto podem possuir aliases legíveis:

```yaml
aliases:
  - project:radiant
```

O ID canônico não muda quando o arquivo for renomeado.

# 16. Nomes de arquivos

Regra inicial:

```text
kebab-case.md
```

Exemplos:

```text
code-review-procedure.md
radiant-project.md
filesystem-as-canonical-store.md
```

Identidade não depende do filename.

# 17. Arquivos e artefatos opacos

Alguns originais ou artefatos não devem ser modificados para receber frontmatter.

Exemplos:

- PDF;
- imagem;
- JSON externo;
- arquivo de configuração original;
- pacote de arquivos;
- repositório externo.

Nesses casos usar sidecar:

```text
sources/
  paper.pdf
  paper.pdf.aikm.yaml
```

ou:

```text
procedures/
  my-skill/
    AIKM.yaml
    SKILL.md
    examples/
    scripts/
```

O sidecar contém metadata AIKM.

O conteúdo original permanece intacto.

# 18. Source

`source` preserva material original.

Regras:

1. originals não são silenciosamente reescritos;
2. origem deve ser registrada;
3. uma síntese deve apontar para a source;
4. excluir a síntese não deve excluir a source;
5. atualizar a source não deve alterar silenciosamente uma síntese existente.

Exemplo:

```yaml
knowledgeRole: source
artifactKind: document
trust: raw

origin:
  type: external
  uri: https://example.com/article
```

# 19. Derivação e síntese

Conhecimento derivado deve registrar:

```yaml
derivedFrom:
  - aikm:01K...
```

Exemplo:

```text
source/article.md
        ↓
knowledge/agent-memory-patterns.md
```

O record derivado pode estar errado mesmo quando a source está correta.

Por isso os estados de confiança são independentes.

# 20. Lifecycle

Valores iniciais:

```text
candidate
active
superseded
archived
```

## `candidate`

Conteúdo capturado ou produzido que ainda não foi aceito como parte ativa do repertório.

## `active`

Disponível para uso normal.

## `superseded`

Substituído por outro record, porém preservado para histórico.

## `archived`

Fora do fluxo operacional normal.

# 21. Trust

Valores iniciais:

```text
raw
unverified
reviewed
canonical
deprecated
```

## `raw`

Material original ainda não interpretado.

## `unverified`

Conteúdo derivado ou gerado que não passou por revisão suficiente.

## `reviewed`

Conteúdo inspecionado por humano ou procedimento adequado.

## `canonical`

Referência preferencial atual dentro de determinado escopo.

## `deprecated`

Não deve orientar novos trabalhos sem justificativa explícita.

# 22. Lifecycle e trust são diferentes

Exemplo:

```yaml
lifecycle: active
trust: raw
```

é válido para uma source original.

Outro exemplo:

```yaml
lifecycle: candidate
trust: unverified
```

é adequado para uma síntese recém-gerada.

Outro:

```yaml
lifecycle: superseded
trust: reviewed
```

preserva conhecimento historicamente válido que foi substituído.

# 23. Promotion

A transição:

```text
candidate → active
```

deve ser explícita.

Na primeira versão pode acontecer através de:

```bash
aikm promote <record>
```

ou por uma operação equivalente de routing.

A promoção não exige aprovação humana em todos os casos.

O processo depende do tipo de conteúdo.

Antes da transição, aplicar os requisitos de record organizado da seção 14. Routing pode classificar mantendo `candidate`; classificação não é revisão de confiança. Na primeira prova, edição explícita seguida de validação pode substituir o comando, sem promover implicitamente conteúdo para `canonical`.

Entretanto:

> conteúdo gerado automaticamente nunca deve chegar a `canonical` sem um gate explícito.

# 24. Intake

Todo conteúdo novo que ainda não possui destino claro pode entrar em:

```text
inbox/
```

Exemplos:

```bash
aikm capture ./new-skill.md
aikm capture "Remember: this procedure fails without a clean working tree"
```

O item recebe metadata mínima:

```yaml
lifecycle: candidate
trust: unverified
```

ou `raw` quando for original externo.

Os demais campos e defaults seguem a seção 14. Arquivos importados não têm o original alterado. O pre-check acontece antes de qualquer persistência de conteúdo no workspace, inclusive arquivos temporários, e uma entrada recusada não deve reaparecer em logs ou mensagens de erro.

O item não classificado já deve ser encontrável por busca local, com indicação de classificação pendente, `candidate` e trust. A busca não deve exigir promoção apenas para localizar algo recém-capturado.

Inbox é staging.

Não é armazenamento permanente.

# 25. Router

O Router decide o destino semântico.

Fluxo inicial:

```text
Input
 │
 ├─ Is it an original external source?
 │      └─ source
 │
 ├─ Is it a failure, verification rule or quality criterion?
 │      └─ evaluation
 │
 ├─ Is it a repeatable way to execute?
 │      └─ procedure
 │
 ├─ Is it specific to a project/person/domain?
 │      └─ context
 │
 ├─ Is it a short stable rule needed before acting?
 │      └─ operational-memory
 │
 ├─ Is it reusable synthesized knowledge?
 │      └─ knowledge
 │
 ├─ Is it execution evidence needed for reproduction,
 │  verification, recovery or handoff?
 │      └─ action
 │
 ├─ Is it an external deliverable?
 │      └─ output
 │
 └─ Otherwise
        └─ discard or keep temporarily in inbox
```

O Router deve ser representado em:

```text
system/ROUTER.md
```

A primeira implementação pode ser determinística/manual.

IA pode sugerir classificação futuramente.

# 26. Regra de descarte

O Router precisa permitir explicitamente:

```text
DO_NOT_STORE
```

Exemplos típicos:

- logs triviais de sucesso;
- outputs intermediários sem valor futuro;
- duplicações;
- estado transitório;
- informação sem relevância operacional.

Isso é uma feature.

Não uma falha de captura.

# 27. Context

`context` contém informação que só é verdadeira dentro de determinado escopo.

Exemplos:

- projeto;
- usuário;
- domínio;
- restrição;
- preferência;
- ambiente.

Projetos são representados como records:

```yaml
knowledgeRole: context
artifactKind: project
```

Exemplo:

```yaml
id: aikm:01K...
title: Radiant
knowledgeRole: context
artifactKind: project
lifecycle: active
trust: reviewed
```

# 28. Operational Memory

Operational Memory é propositalmente pequena.

Ela contém ponteiros curtos.

Exemplo:

```markdown
knowledgeRole: operational-memory
artifactKind: pointer
...

- Before agentic implementation, use [[radiant-task-contract]].
- Shared procedures live in [[code-review-procedure]], not in harness memory.
```

Regras:

- não armazenar longos corpos de conhecimento;
- não duplicar procedures;
- não duplicar context completo;
- carregar apenas o que realmente precisa estar disponível antes de agir.

# 29. Procedure

Procedures descrevem execução repetível.

Kinds iniciais:

```text
skill
workflow
checklist
playbook
```

Uma procedure deve idealmente possuir:

- objetivo;
- quando usar;
- inputs;
- passos;
- failure points conhecidos;
- método de verificação;
- links para conhecimento necessário.

Knowledge reutilizável por várias procedures deve permanecer em `knowledge/`.

# 30. Action / Execution Evidence

A camada `action` registra apenas execução relevante.

Kinds iniciais:

```text
run
decision
handoff
reuse-event
```

Um run deve ser persistido apenas quando necessário para:

- reproduzir resultado;
- verificar;
- diagnosticar falha;
- recuperar;
- suportar um aprendizado;
- fazer handoff.

Não criar diário completo de todas as execuções.

# 31. Execution Record

Exemplo:

```yaml
knowledgeRole: action
artifactKind: run

project: aikm:project-b
procedure:
  - aikm:procedure-code-review

startedAt: ...
completedAt: ...

outcome: failed

evidence:
  - path: tests/output.txt

produced:
  - aikm:...
```

O corpo deve registrar apenas aquilo que muda reprodução, verificação ou Learn Back.

# 32. Experience

Experience representa um aprendizado explícito.

Exemplo:

```yaml
knowledgeRole: evaluation
artifactKind: experience

statement: >
  The procedure becomes unreliable when the project context is not
  loaded before execution.

confidence: medium

evidenceRefs:
  - aikm:run:...

projects:
  - aikm:project-b
```

Valores iniciais de confidence:

```text
low
medium
high
```

Experience não precisa permanecer para sempre como Experience.

Ela pode originar:

- knowledge;
- context;
- procedure update;
- operational-memory pointer;
- evaluation rule.

# 33. Finding

Um finding registra algo identificado durante verificação.

Exemplo:

```yaml
knowledgeRole: evaluation
artifactKind: finding

findingType: recurring-failure
severity: medium

evidenceRefs:
  - aikm:...
```

Findings fornecem entrada para Learn Back.

# 34. Learn Back Record

Learn Back precisa tornar explícita a correção.

Schema conceitual:

```yaml
knowledgeRole: evaluation
artifactKind: experience

learning:
  finding: >
    The procedure did not define how to validate generated migrations.

  evidenceRefs:
    - aikm:run:...

  diagnosis: >
    Verification responsibility was absent from the procedure.

  fixTarget:
    role: procedure
    ref: aikm:procedure:database-migration

  changeRef:
    ref: aikm:decision:...

  verificationRef:
    ref: aikm:verification:...
```

O `fixTarget` é central.

Uma retrospectiva sem destino de correção não fecha o ciclo.

# 35. Learn Back routing

Mapa inicial:

| Finding                           | Fix target preferencial |
| --------------------------------- | ----------------------- |
| conhecimento incorreto            | `knowledge`             |
| informação específica ausente     | `context`               |
| procedimento falho                | `procedure`             |
| regra necessária em toda sessão   | `operational-memory`    |
| ausência de critério de qualidade | `evaluation`            |
| má classificação                  | `system/ROUTER.md`      |
| adapter duplicando conteúdo       | adapter                 |
| problema na regra global do AIKM  | `system/`               |

O sistema deve permitir exceções.

# 36. Relations

Relações ficam inicialmente dentro dos records.

Formato:

```yaml
links:
  - type: uses
    ref: aikm:01K...
  - type: derived-from
    ref: aikm:01K...
```

Tipos iniciais:

```text
uses
depends-on
derived-from
related-to
supersedes
replaces
supports
evaluates
produces
used-by
```

Não criar banco de grafo na primeira versão.

Quando uma relação precisar de metadata própria significativa, poderá virar um record separado futuramente.

# 37. Reuse Event

Reuse continua sendo evidência central.

Representação:

```yaml
knowledgeRole: action
artifactKind: reuse-event

sourceProject: aikm:...
targetProject: aikm:...

reused:
  - aikm:...

reconstructionAvoided: "yes"

outcome: useful

note: >
  Existing procedure was reused in the new project without recreation.
```

O evento deve preservar:

- origem;
- destino;
- record reutilizado;
- resultado;
- percepção sobre reconstrução evitada.

`reconstructionAvoided` usa `yes`, `partial`, `no` ou `unknown`, como na seção 71. Na prova inicial, uma nota manual pode registrar esses fatos, a necessidade original e a evidência do resultado. Isso não equivale à entrega do comando `aikm reuse`.

# 38. Search

Comando conceitual:

```bash
aikm search "<query>"
```

Filtros iniciais:

```text
--role
--kind
--project
--trust
--lifecycle
--tag
```

A busca inicial pode utilizar:

- scan do filesystem;
- metadata;
- conteúdo Markdown;
- ferramentas locais de busca textual.

Não exige banco.

A primeira parcela busca título e conteúdo de records textuais, retorna ID, path, trecho pertinente, lifecycle, trust e role/kind quando presentes. Indica classificação pendente quando ausentes. Candidatos no inbox são encontráveis; `archived` fica fora por padrão e `superseded`/`deprecated` aparecem com aviso. A ordenação deve ser determinística. Descrição e filtros entram conforme o Plan e os contratos, sem exigir uma taxonomia completa para o primeiro uso.

Busca local pode acessar conteúdo privado. Sua saída não é automaticamente autorizada para um consumidor externo: aplicar a seção 50 antes de entregar resultados ou corpos ao adapter.

# 39. Retrieve

Comando:

```bash
aikm retrieve "<need>"
```

Objetivo:

> **quais elementos do repertório parecem úteis para esta necessidade?**

Sinais iniciais:

1. correspondência no título;
2. descrição;
3. conteúdo;
4. tags;
5. projeto;
6. knowledge role;
7. links;
8. trust;
9. lifecycle.

Regras:

- `archived` não aparece por padrão;
- `deprecated` deve ser claramente identificado ou penalizado;
- `candidate` não deve ser tratado como equivalente a `active`;
- resultado deve mostrar `knowledgeRole` ou classificação pendente;
- resultado deve mostrar trust;
- resultado deve explicar minimamente por que apareceu.

# 40. Retrieval result

Exemplo:

```text
1. Code Review
   role: procedure
   kind: skill
   trust: reviewed
   projects: radiant, seed

   reason:
   - title matches "review"
   - used in engineering projects
   - related evaluation exists

2. Code Review Failure Pattern
   role: evaluation
   kind: experience
   trust: reviewed

   reason:
   - linked to Code Review
```

O resultado não deve esconder que itens exercem funções diferentes.

# 41. Retrieval não implica claim support

Este ciclo não implementará um evidence packet completo.

Entretanto, o sistema deve preservar espaço para distinguir futuramente:

```text
retrieved
directly-inspected
supports-claim
conflicted
stale
```

Por enquanto:

- retrieval retorna candidates;
- consumers são responsáveis por inspecionar conteúdo relevante;
- Radiant Verify decide o rigor necessário.

# 42. Índice e persistência derivada

Nesta versão:

> **nenhum banco é obrigatório.**

A implementação deve primeiro funcionar via filesystem.

`.aikm/` poderá conter:

```text
cache/
search-index/
```

se isso melhorar performance.

Qualquer estado derivado deve ser:

- descartável;
- reconstruível;
- subordinado aos arquivos canônicos.

# 43. Quando SQLite pode entrar

SQLite só deve ser introduzido se o experimento demonstrar pelo menos uma destas necessidades:

- scan do filesystem se torna lento;
- filtros estruturados ficam complexos;
- relações precisam de consulta mais eficiente;
- métricas de reuse precisam de agregação frequente;
- adapters precisam de leitura estruturada rápida.

Se entrar:

> **continua sendo projection, nunca authority.**

# 44. Versionamento

Este ciclo não cria infraestrutura própria de versões para todos os records.

Estratégia inicial:

### Git disponível

Usar histórico Git para mudanças de arquivo.

### Mudança semântica de substituição

Registrar:

```yaml
supersedes:
  - aikm:...
```

e no record anterior:

```yaml
supersededBy: aikm:...
lifecycle: superseded
```

### Artefato que possui versão própria

Pode declarar:

```yaml
artifactVersion: "1.2.0"
```

Version directories podem ser introduzidos apenas quando um caso de uso concreto exigir.

# 45. Adapter Contract

Todo adapter deve responder pelo menos:

1. Onde está o AIKM root?
2. O que o agent carrega no início da sessão?
3. Como o agent recupera knowledge/context/procedures?
4. Como conteúdo novo é enviado para intake/routing?
5. Como findings são enviados para Learn Back?
6. Como o adapter aplica visibility/egress?

# 46. Session bootstrap

Um adapter não deve carregar todo o vault.

Depois de uma configuração local explícita da raiz, uma sessão nova deve conseguir descobrir o acervo sem intervenção repetida. Para consumidores externos, o bootstrap passa primeiro pela filtragem local da seção 50; o agent não recebe acesso bruto aos arquivos como mecanismo dessa integração.

Conteúdo candidato ao bootstrap, somente após a filtragem:

```text
system/INDEX.md
memory/*
adapter-specific pointer
```

Depois:

```text
need
 ↓
search / retrieve
 ↓
knowledge / context / procedure
```

Isso evita carregar conhecimento longo em toda sessão.

Um ponteiro para conteúdo restrito não autoriza sua leitura. O adapter deve consultar novamente a mesma fronteira para recuperar o corpo ou seguir relações. Se não houver conteúdo permitido ou a raiz não estiver acessível, informar a limitação sem revelar conteúdo protegido.

# 47. Harness-native memory

Se um harness possui memória própria:

### Pode permanecer lá

- detalhes específicos da própria ferramenta;
- ponteiro para AIKM;
- configurações exclusivas do harness.

### Deve preferencialmente permanecer no AIKM

- conhecimento reutilizável;
- project context compartilhado;
- procedures compartilhadas;
- findings;
- avaliações;
- regras comuns.

Pergunta de divisão:

> **Outro harness precisaria disso?**

Se sim, AIKM é o candidato canônico.

# 48. Adapter de Codex

A primeira implementação pode começar pelo harness realmente utilizado no experimento.

O adapter deve ser mínimo.

Exemplo conceitual:

```text
AIKM root: /path/to/workspace

At session start:
- request locally filtered bootstrap from the configured AIKM root

When knowledge is needed:
- request locally filtered search/retrieve and record content

Before persisting shared knowledge:
- use AIKM Router

On material failure:
- create finding
- route Learn Back
```

Não duplicar Router, Security ou procedures no adapter.

O adapter mínimo pode encaminhar classificação e Learn Back para uma operação manual local; não depende de comandos especializados ainda não implementados. A superfície concreta de integração e a configuração do harness serão delimitadas no contrato correspondente.

# 49. Visibility

Valores iniciais:

```text
public
non-sensitive
private
restricted
```

`visibility` descreve sensibilidade/disponibilidade.

Não decide sozinho transmissão externa.

# 50. Egress

Campo:

```yaml
egressAllowed: true | false
```

Regras:

- `private` → egress deve ser `false`;
- `restricted` → egress deve ser `false`;
- `public` ou `non-sensitive` só saem da máquina quando `egressAllowed: true`;
- ausência de política deve falhar para o lado mais restritivo.

Adapters devem aplicar essa regra antes de enviar contexto a serviços externos.

## Fronteira local obrigatória

O processo local que prepara a resposta do adapter deve ler e validar a política antes de liberar qualquer conteúdo. Instruções textuais para o agent não substituem esse controle. Uma chamada de ferramenta que devolve conteúdo a um modelo externo já cruza essa fronteira.

A regra cobre bootstrap, índice, memory, resultados de busca, títulos, trechos, caminhos, corpos, relações, mensagens de erro e exports. Material sem metadata própria, inclusive `system/`, recebe os defaults do workspace; ausência ou invalidez de política resulta em negação. A permissão de um índice ou ponteiro não libera os records referenciados nem seus metadados.

Quando uma resposta ou síntese combina múltiplas fontes, todas precisam permitir a saída; a combinação não pode tornar menos restritiva a política de uma delas. Novas capturas continuam com defaults restritivos. Autorizar saída exige uma operação explícita, separada da captura e da promoção.

O adapter externo deve consumir apenas essa interface filtrada. Se a configuração do harness permite contornar a interface e ler o workspace diretamente, a integração não pode alegar isolamento nem passar AC-21. O contrato do adapter deve demonstrar uma configuração sem esse acesso ou limitar o experimento ao uso local até resolver a fronteira.

Verificar a fronteira com um consumidor simulado e marcadores sintéticos, sem credenciais ou envio real: cobrir conteúdo permitido, privado, restrito, política ausente/inválida e combinações de fontes. O marcador negado não pode aparecer em nenhuma saída destinada ao consumidor, mesmo quando encontrado por busca local.

# 51. Secrets

Secrets não podem ser persistidos como conhecimento.

Proibidos como conteúdo comum:

- API keys;
- passwords;
- OAuth tokens;
- cookies;
- private keys;
- session tokens.

Representação permitida:

```yaml
secretRef:
  provider: macos-keychain
  name: openai-personal
```

O AIKM armazena a referência.

Não o valor.

# 52. Security pre-check

Security precede routing.

Fluxo:

```text
capture
  ↓
security pre-check
  ↓
route
```

Se a entrada contém secret evidente:

- recusar antes de gravar no workspace, inclusive inbox e temporários;
- alertar sem reproduzir o valor;
- permitir armazenar apenas referência segura.

Detecção de padrões conhecidos é uma proteção parcial, não prova de ausência de secrets. Ela não substitui a política de saída nem a revisão de conteúdo destinado a sair da máquina.

# 53. Outputs como superfície de vazamento

Conteúdo em `outputs/` pode ser destinado a deixar o ambiente local.

Antes de exportar ou entregar:

- verificar secrets;
- verificar dados pessoais;
- verificar caminhos privados;
- verificar referências internas;
- verificar conteúdo `private` ou `restricted`.

Esse check pertence ao Verify.

# 54. CLI conceitual

Nome:

```text
aikm
```

Comandos centrais:

```bash
aikm init
aikm capture
aikm route
aikm promote
aikm search
aikm retrieve
aikm reuse
aikm learn
aikm doctor
```

Comandos adicionais podem aparecer se o Implementation Plan demonstrar necessidade.

Para M1, `aikm validate` oferece a verificação local de manifest e records necessária após edições manuais, conforme Plan seção 30. Não corrige arquivos nem substitui o horizonte completo de `doctor`. A seleção explícita `--workspace <path>` permite operar o acervo a partir de outro diretório de projeto.

# 55. `aikm init`

```bash
aikm init [path]
```

Cria:

- `aikm.yaml`;
- diretórios;
- arquivos básicos de `system/`;
- `.aikm/`.

Não cria database obrigatório.

# 56. `aikm capture`

```bash
aikm capture <path|text>
```

Responsabilidades:

- executar security pre-check;
- criar record mínimo em `inbox/`;
- preservar origem;
- gerar ID;
- marcar lifecycle/trust apropriados.

# 57. `aikm route`

```bash
aikm route <id>
```

Responsabilidades:

- aplicar ou auxiliar árvore de classificação;
- escolher `knowledgeRole`;
- sugerir `artifactKind`;
- mover para destino canônico;
- ou retornar `DO_NOT_STORE`.

A primeira versão pode solicitar decisão humana quando houver ambiguidade.

# 58. `aikm promote`

```bash
aikm promote <id>
```

Responsabilidades:

- alterar `candidate → active`;
- registrar actor/reason quando relevante;
- impedir promoção inválida;
- não definir automaticamente `canonical`.

# 59. `aikm search`

Busca lexical e metadata.

Precisa funcionar sem IA.

# 60. `aikm retrieve`

Recupera candidatos ordenados para uma necessidade.

Precisa funcionar sem IA.

# 61. `aikm reuse`

```bash
aikm reuse <record> --from <project-a> --to <project-b>
```

Cria `reuse-event`.

# 62. `aikm learn`

Ajuda a registrar:

- finding;
- experience;
- evidence refs;
- fix target;
- change ref.

Pode ser interativo na primeira versão.

# 63. `aikm doctor`

`doctor` verifica integridade.

Checks iniciais:

- manifest válido;
- frontmatter válido;
- IDs duplicados;
- references quebradas;
- roles inválidos;
- kinds inválidos quando controlados;
- lifecycle inválido;
- trust inválido;
- private/restricted com egress permitido;
- secrets comuns;
- operational memory excessivamente longa;
- arquivos em inbox envelhecidos;
- links para records inexistentes;
- sidecars sem target;
- targets opacos sem sidecar quando gerenciados.

Resultado:

```text
PASS
PASS_WITH_NOTE
FAIL
```

`doctor` não deve corrigir automaticamente conhecimento sem autorização.

# 64. Lint vs Doctor

Pode haver um único executável inicialmente.

Conceitualmente:

### Lint

Verifica estrutura determinística.

### Doctor

Verifica consistência do workspace e políticas.

Não confundir esses checks com verificação semântica de verdade factual.

# 65. IA opcional

Todas as capacidades obrigatórias precisam funcionar com:

```yaml
features:
  aiAssistance: false
```

IA futura pode ajudar em:

- classification suggestion;
- duplicate detection;
- semantic retrieval;
- relation suggestion;
- experience synthesis;
- Learn Back diagnosis.

Quando fizer isso:

- gera candidate;
- preserva origem;
- não promove silenciosamente;
- respeita egress.

# 66. Source of truth e derived state

Regra fundamental:

```text
Canonical filesystem > derived state
```

Se um cache contradiz o filesystem:

> filesystem vence.

Se estado derivado for apagado:

> o conhecimento continua utilizável.

# 67. Git

Git é recomendado, não obrigatório.

Quando presente, pode fornecer:

- histórico;
- diff;
- rollback;
- autoria;
- experimentação em branches.

O AIKM não deve reinventar Git sem evidência de necessidade.

`.aikm/` deve poder ser ignorado.

# 68. Acceptance Criteria

## AC-01 — Workspace legível

Dado um diretório vazio, `aikm init` cria um workspace cuja estrutura principal pode ser compreendida sem banco ou aplicação gráfica.

## AC-02 — Capture

Um novo item pode ser capturado no inbox com ID e provenance mínimos.

Captura simples não exige classificação nem preenchimento manual de metadata técnica. Um candidato sem role/kind é válido no inbox e encontrável por busca local; promoção incompleta é rejeitada.

## AC-03 — Security before storage

Uma secret de padrão conhecido é recusada antes de persistência no workspace e não é reproduzida nos diagnósticos. O teste inspeciona também inbox e temporários; promoção não pode contornar a mesma regra.

## AC-04 — Routing

Um item pode ser classificado para um `knowledgeRole` ou descartado.

## AC-05 — Two-axis model

Um record consegue representar separadamente `artifactKind` e `knowledgeRole`.

## AC-06 — Source preservation

Um original pode ser preservado sem ser modificado para receber metadata.

## AC-07 — Derived knowledge provenance

Uma síntese consegue apontar para sua source.

## AC-08 — Lifecycle

Um record pode passar de candidate para active sem perder provenance.

## AC-09 — Trust

Records de diferentes níveis de confiança permanecem distinguíveis durante retrieval.

## AC-10 — Projects as context

Um record pode ser relacionado a pelo menos um projeto.

## AC-11 — Operational memory pointer

Uma memory entry consegue apontar para conhecimento completo sem duplicá-lo.

## AC-12 — Procedure

Uma skill ou workflow pode ser representado como `artifactKind` técnico e `knowledgeRole: procedure`.

## AC-13 — Execution evidence

Uma execução relevante pode ser preservada e ligada ao projeto/procedure que a produziu.

## AC-14 — Experience with evidence

Uma Experience pode apontar para evidência de execução.

## AC-15 — Learn Back

Um finding pode registrar `fixTarget` e apontar para uma alteração realizada.

## AC-16 — Search without AI

Busca lexical funciona com IA desabilitada.

## AC-17 — Retrieve without AI

Retrieve retorna candidatos ordenados e informa role/trust.

## AC-18 — Reuse Event

É possível registrar reutilização do Projeto A no Projeto B.

## AC-19 — No database dependency

Apagar todo estado derivado não impede leitura manual nem operação essencial.

## AC-20 — Harness separation

Um adapter consegue utilizar o AIKM sem duplicar o core.

Após configuração local única, uma sessão nova descobre e consulta o acervo a partir da necessidade da tarefa, sem receber o arquivo esperado. A ausência de conteúdo aplicável também é um resultado válido.

## AC-21 — Egress protection

Conteúdo private/restricted não é enviado por adapter externo.

Aplicar a fronteira local da seção 50, inclusive no bootstrap e em metadados. Testes com consumidor simulado demonstram a negação antes da entrega e a liberação de conteúdo explicitamente permitido, sem depender de obediência textual do agent.

## AC-22 — Doctor

`aikm doctor` detecta ao menos referências quebradas, metadata inválida, política de egress inválida e padrões comuns de secrets.

# 69. Experimento Projeto A → Projeto B

Executar uma primeira passagem assim que captura e busca local estiverem utilizáveis, com organização e evidência manuais quando necessário. Repetir com a integração mínima protegida antes de expandir capacidades. As etapas abaixo descrevem fatos a demonstrar, não uma obrigação de implementar um comando para cada etapa.

## Projeto A

1. registrar projeto;
2. capturar material real;
3. classificar;
4. consolidar pelo menos um procedure/knowledge record;
5. utilizar o record;
6. registrar execution evidence quando material;
7. registrar Experience ou Finding;
8. manter provenance.

## Projeto B

1. criar novo context de projeto;
2. formular necessidade real;
3. executar `search` ou `retrieve`;
4. encontrar record do Projeto A;
5. inspecioná-lo;
6. reutilizá-lo;
7. executar trabalho;
8. registrar `reuse-event`;
9. responder `reconstructionAvoided`;
10. verificar o resultado.

## Learn Back

Depois do Projeto B:

1. identificar uma descoberta real;
2. registrar evidence;
3. definir `fixTarget`;
4. alterar a camada responsável;
5. utilizar essa alteração em uma execução posterior.

# 70. Critério de sucesso do experimento

### Evidência primária

```text
Knowledge Reuse Event >= 1
```

com:

```text
reconstructionAvoided = yes
```

e justificativa concreta.

Esse resultado prova possibilidade. Não basta para declarar adoção recorrente, ganho líquido ou conclusão de capacidades ainda pendentes.

### Evidência secundária

```text
Learn Back Event >= 1
```

com alteração recuperável posteriormente.

### Utilidade recorrente

Observar novas necessidades reais em sessões ou tarefas distintas e comparar com a forma anterior de trabalhar. Antes de usar o AIKM em cada observação, registrar a necessidade, o procedimento habitual de procura/reconstrução e o que caracterizaria uma resposta aplicável. Não fornecer ao consumidor a resposta esperada nem selecionar apenas sucessos.

Registrar tentativas bem-sucedidas, falhas, manutenção necessária e se o uso foi espontâneo ou solicitado pelo experimento. Evidência favorável exige benefício repetido que compense o esforço de captura, manutenção e recuperação; um erro relevante evitado também pode justificar esse esforço quando a evidência for concreta. Se houver apenas uma oportunidade ou a comparação não for confiável, registrar resultado inconclusivo para recorrência.

# 71. Métricas

## Knowledge Reuse Events

Quantidade de reutilizações reais.

## Reconstruction Avoided

Avaliação:

```text
yes
partial
no
unknown
```

## Retrieval Usefulness

```text
useful
partially-useful
not-useful
```

## Capture Cost

Tempo/esforço aproximado de captura de todos os itens do recorte observado, inclusive os não reutilizados.

## Maintenance Cost

Esforço de classificação, promoção, correção, descarte e atualização do acervo no mesmo recorte.

## Time to Useful Application

Tempo entre formular a necessidade e encontrar, inspecionar e decidir aplicar conteúdo útil. Registrar também buscas abandonadas ou sem resultado; latência do comando é apenas uma parcela.

## Benefício líquido observado

Comparar esforço de captura, manutenção e recuperação com reconstrução/retrabalho evitados e melhorias verificáveis no resultado. Usar o modo habitual de trabalhar como referência, distinguir tempo observado de estimativas e não repetir artificialmente a mesma tarefa como se não houvesse aprendizado anterior.

## Retorno espontâneo

Registrar se novas consultas aconteceram por iniciativa de uso cotidiano ou por solicitação do experimento. Não exige telemetria: notas locais curtas bastam.

## Learn Back Rate

Proporção de findings materiais que resultam em correção explícita.

## Duplication Avoided

Casos em que um harness usa referência ao conteúdo canônico em vez de manter cópia.

## Provenance Recovery

É possível chegar da reutilização até a origem ou evidência relevante?

# 72. Requisitos não funcionais

## Simplicidade

Primeiro uso não deve exigir infraestrutura externa.

## Portabilidade

Copiar o workspace deve preservar o patrimônio.

## Legibilidade

Conteúdo principal deve permanecer acessível com editor de texto e filesystem.

## Performance

Para um workspace pessoal inicial, busca deve permanecer interativa.

Não estabelecer otimização prematura.

## Integridade

Operações de movimentação/promoção não devem deixar references quebradas silenciosamente.

## Observabilidade

Erros devem indicar:

- record;
- path;
- regra violada;
- ação recomendada quando conhecida.

# 73. Decisões técnicas deliberadamente adiadas

Não decidir ainda:

- linguagem final do produto;
- framework de UI;
- SQLite;
- graph database;
- vector database;
- embedding model;
- desktop app;
- web app;
- sync;
- cloud;
- multi-user;
- public protocol;
- full semantic evidence packet;
- automatic memory extraction;
- global agent prompt injection;
- automatic canonical promotion.

Essas decisões dependem de evidência posterior.

# 74. Referência externa e limite de adoção

A revisão desta spec incorpora padrões observados no projeto público:

**DECK6/akm — Agent Knowledge Management**  
https://github.com/DECK6/akm

Foram considerados especialmente:

- separation of stores;
- source vs synthesized knowledge;
- routing;
- operational memory como ponteiros;
- core–adapter separation;
- selective action logging;
- verification;
- Learn Back;
- derived state descartável;
- security before classification;
- visibility vs egress.

O AIKM não pretende reproduzir esse projeto.

Nossa hipótese experimental continua sendo própria:

> **provar continuidade e reutilização de conhecimento operacional entre projetos pessoais de IA, integrando progressivamente esse patrimônio ao Radiant.**

# 75. Riscos técnicos principais

## Taxonomia rígida cedo demais

Mitigação:

- `knowledgeRole` pequeno e estável;
- `artifactKind` extensível.

## Inbox virar cemitério

Mitigação:

- doctor aponta itens antigos;
- routing simples;
- discard explícito.

## Metadata burocrática

Mitigação:

- poucos campos obrigatórios;
- promotion completa metadata apenas quando necessário.

## Operational Memory inflada

Mitigação:

- ponteiros curtos;
- doctor pode alertar tamanho excessivo.

## Duplicação entre adapters

Mitigação:

- adapters apontam para core;
- one body, pointers elsewhere.

## Conteúdo gerado ganhar autoridade cedo

Mitigação:

- candidate + unverified;
- promoção explícita.

## Busca ruim causar adoção prematura de RAG

Mitigação:

- testar lexical + roles + links antes de embeddings.

## Egress acidental

Mitigação:

- default deny;
- adapter enforcement;
- doctor.

## Registro excessivo de execuções

Mitigação:

- persistir apenas quando necessário para reprodução, verification, handoff ou learning.

# 76. Verification do primeiro ciclo

O estágio Verify do Radiant deverá testar:

### Estrutura

- schemas;
- IDs;
- links;
- lifecycle;
- trust;
- sidecars.

### Segurança

- secrets;
- visibility;
- egress.

### Portabilidade

- copiar workspace;
- apagar `.aikm/`;
- repetir busca básica.

### Harness

- session bootstrap;
- retrieval;
- ausência de duplicação de core.

### Produto

- Reuse Event real.

### Aprendizado

- Learn Back real.

Resultado:

> **Verification Report - AI Knowledge Manager (AIKM) v0.3**

A primeira prova verifica as capacidades e fronteiras já entregues. O relatório distingue critérios demonstrados, falhos e ainda não implementados; não declara todos os AC atendidos porque um percurso funcionou. A revisão completa do ciclo aplica todos os AC vigentes, com pendências explícitas.

# 77. Learning Record esperado

O primeiro Learning Record deve responder:

- A separação por knowledgeRole ajudou?
- `artifactKind × knowledgeRole` ficou claro na prática?
- Inbox reduziu atrito?
- Router reduziu ou aumentou burocracia?
- O que foi descartado corretamente?
- Source e synthesis precisaram realmente ser separados?
- Operational Memory por ponteiros funcionou?
- O adapter conseguiu evitar duplicação?
- Search lexical foi suficiente?
- Retrieve produziu resultado útil?
- SQLite fez falta?
- Git foi suficiente para histórico?
- Execution Record foi útil ou excessivo?
- Experience conseguiu apontar para evidência?
- Learn Back gerou uma melhoria real?
- Visibility/egress foi compreensível?
- Qual metadata nunca foi usada?
- Qual metadata fez falta?
- O segundo projeto começou melhor por causa do primeiro?
- O benefício compensou captura, manutenção e buscas sem resultado?
- Houve retorno espontâneo em tarefas posteriores?
- Quais limitações observadas justificam o próximo incremento?

# 78. Próximo artefato

Esta especificação deve alimentar:

# Implementation Plan - AI Knowledge Manager (AIKM) v0.3

O Plan v0.3 organiza a execução por marcos de uso. As identificações das capacidades permanecem estáveis, mas sua numeração não exige execução linear.

A sequência de uso é:

```text
Bootstrap verificado
  ↓
Workspace + entrada mínima + segurança + busca local
  ↓
Primeira reutilização real + verificação + evidência manual
  ↓
Adapter mínimo com fronteira local + nova sessão real
  ↓
Uso recorrente + comparação com o trabalho habitual
  ↓
Expansão justificada por limitações + Verify + Learn
```

O Implementation Plan deve evitar reintroduzir SQLite, version directories ou infraestrutura agêntica complexa antes de aparecer evidência de necessidade.

# 79. Síntese

> **AIKM v0.3 especifica uma infraestrutura pessoal local-first de conhecimento operacional em que filesystem e arquivos legíveis permanecem canônicos; conteúdos podem ser classificados por função, preservam proveniência e confiança, podem ser utilizados por diferentes agents através de adapters finos e retornam aprendizados ao sistema através de Learn Back.**

Seu primeiro objetivo continua simples:

> **fazer conhecimento do Projeto A melhorar concretamente o Projeto B.**

Seu segundo objetivo começa onde o primeiro termina:

> **fazer aquilo que aprendemos no Projeto B melhorar a próxima execução.**

Tudo que não ajuda a provar esses dois fenômenos continua sendo secundário.

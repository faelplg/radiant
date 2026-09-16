---
version: "0.3.1"
status: Plano revisado para prova antecipada de utilidade
origem: Radiant Project Frame - AI Knowledge Manager (AIKM) v0.2.1 + Implementation Spec - AI Knowledge Manager (AIKM) v0.3.1
projeto: AI Knowledge Manager
acronimo_interno: AIKM
enquadramento: fael.tech
sistema_de_desenvolvimento: Radiant — Project Generation System v0.2
objetivo_do_ciclo: Provar continuidade, reutilização e Learn Back entre projetos reais
---

# Implementation Plan — AI Knowledge Manager (AIKM)

## 1. Objetivo do plano

Este plano transforma a especificação v0.3.1 do AIKM em incrementos pequenos, verificáveis e orientados por evidência.

Revisão aprovada pelo responsável pelo projeto em 2026-09-15: antecipar captura, busca, integração mínima e experiência real, antes da automação completa de organização e aprendizado. O bootstrap permanece registrado em TC-0001 v0.2 e ADR-0001; esta revisão não altera retroativamente sua delegação.

A revisão 0.3.1 torna o procedimento Radiant acionável antes da próxima implementação. Seguir o [mapa operacional](WORKFLOW.md), que aponta para a skill reutilizável e para as evidências do ciclo. Essa preparação documental não é uma nova capacidade de produto nem uma execução do TC-0002.

A implementação não busca construir um knowledge management system completo.

Ela busca provar dois fenômenos:

> **Conhecimento produzido ou consolidado no Projeto A consegue melhorar concretamente o Projeto B sem precisar ser reconstruído.**

e:

> **Uma descoberta produzida durante uma execução consegue retornar ao AIKM, corrigir a camada responsável e melhorar uma execução posterior.**

O plano deve preservar a principal mudança introduzida pela revisão:

> **AIKM é uma infraestrutura de conhecimento operacional, não apenas um catálogo de artefatos.**

---

# 2. Resultado esperado ao final do ciclo

O horizonte de capacidades do ciclo é:

1. criar um workspace local legível;
2. capturar material com baixo atrito;
3. impedir que secrets sejam persistidos como conhecimento comum;
4. classificar conteúdo por `knowledgeRole`;
5. representar separadamente `artifactKind` e `knowledgeRole`;
6. preservar fontes e proveniência;
7. distinguir lifecycle de trust;
8. representar projetos, procedures e operational memory;
9. pesquisar o repertório sem IA;
10. preservar evidência seletiva de execução;
11. registrar Experience e Finding apoiados por evidência;
12. realizar Learn Back com `fixTarget`;
13. recuperar conteúdo relevante através de `retrieve`;
14. conectar pelo menos um harness através de adapter fino;
15. registrar um `ReuseEvent`;
16. executar um experimento real Projeto A → Projeto B;
17. verificar integridade, segurança e utilidade;
18. produzir um Learning Record que oriente a próxima versão.

A primeira prova cobre somente a parcela definida no marco M1 da seção 4. Capacidades restantes não são pré-requisitos para observar utilidade e continuam pendentes até terem contrato, implementação e verificação. Após os marcos iniciais, escolher expansão por limitação observada; encerrar ou pausar o experimento não equivale a concluir todas as capacidades desta lista.

---

# 3. Princípios de execução

## 3.1. Filesystem antes de infraestrutura derivada

O filesystem é a fonte canônica.

Não introduzir SQLite, graph database, vector database ou outro store derivado sem evidência de necessidade.

---

## 3.2. Build apenas após contrato

O Radiant v0.2 estabelece:

```text
Plan → Contract → Build
```

Antes de delegar uma iteração relevante a um agente, criar um **Radiant Task Contract** pequeno e delimitado.

Cada contrato deve especificar:

- objetivo;
- inputs;
- outputs;
- paths permitidos;
- non-goals;
- critérios de conclusão;
- testes;
- readback;
- segurança;
- condições de HOLD/FAIL.

---

## 3.3. Incrementos observáveis

Cada iteração precisa terminar com um comportamento demonstrável.

Não aceitar como incremento apenas:

- scaffolding sem uso;
- abstração sem consumidor;
- infraestrutura para uma feature futura;
- documentação sem impacto operacional.

---

## 3.4. Evidência antes de expansão

Nenhuma capacidade futura entra porque “provavelmente será necessária”.

Ela entra quando:

- uma limitação foi observada;
- a limitação impede o experimento;
- a nova capacidade é a menor resposta possível.

---

## 3.5. Capture barato, promoção deliberada

Entrada deve ser simples.

Conhecimento durável recebe mais estrutura apenas quando necessário.

---

## 3.6. Store selectively

O sistema deve possuir uma saída legítima:

```text
DO_NOT_STORE
```

Não registrar tudo é parte da arquitetura.

---

## 3.7. Gerado não é canônico

Conteúdo criado por IA começa como candidato ou não verificado.

Nenhuma automação deve elevá-lo silenciosamente a `canonical`.

---

## 3.8. Retrieval não é verificação

Search e retrieve produzem candidatos.

Quando o conteúdo sustentar uma decisão importante, o consumidor precisa inspecioná-lo conforme o rigor exigido pelo Radiant.

---

## 3.9. Learn Back precisa modificar o sistema

Uma retrospectiva sem `fixTarget` não fecha o ciclo.

---

## 3.10. One body, pointers elsewhere

Conhecimento compartilhado possui um corpo canônico.

Adapters e memórias nativas carregam ponteiros sempre que possível.

---

# 4. Estratégia geral do ciclo

## Capacidades com identidade estável

Os IDs 00-14 e as seções existentes permanecem estáveis para rastreabilidade. A numeração identifica capacidades; a ordem de execução vigente é a dos marcos abaixo. Um contrato pode entregar uma parcela explícita de várias capacidades sem declarar cada uma concluída integralmente.

```text
00  Bootstrap técnico
01  Canonical Workspace
02  AIKM Record + Provenance
03  Inbox + Security Pre-check
04  Router + Promotion
05  Context + Procedure + Memory + Relations
06  Search
07  Execution Evidence
08  Evaluation + Experience + Learn Back
09  Retrieve
10  Adapter
11  Reuse Event
12  Experimento Projeto A → Projeto B
13  Verify
14  Learn
```

## Marcos de uso e dependências

| Marco | Parcela de implementação | Comportamento e evidência de saída |
| --- | --- | --- |
| M0 - Base técnica | 00, entregue e aprovada sob TC-0001 v0.2 | CLI de ajuda e gates do bootstrap verificados; aceite registrado em [VR-0002](verification/VR-0002-bootstrap-acceptance.md); não representa validação do produto. |
| M1 - Capturar e reencontrar em outra tarefa | 01; entrada textual e validação mínima de 02-03; busca básica de 06; primeira passagem de 12-14 | Capturar texto/Markdown sem classificação obrigatória, organizar manualmente um item, buscar por uma necessidade real, inspecionar e aplicar no Projeto B, registrar resultado e custo. |
| M2 - Consultar no ambiente de trabalho | Parcela mínima de 10 e fronteira de saída, usando a busca de M1; nova passagem de 12-14 | Uma sessão nova descobre o acervo configurado e encontra conteúdo permitido sem indicação do arquivo esperado. Testes locais demonstram a negação de conteúdo protegido antes da entrega. |
| M3 - Verificar recorrência | Repetições reais de 12-14 e comparação da seção 36 | Observar benefício, custo de manutenção, falhas e retorno espontâneo em tarefas posteriores; decidir continuar, ajustar, pausar ou parar. |
| M4 - Responder às limitações observadas | Parcelas restantes de 02-11 e doctor, somente quando justificadas | Cada contrato liga uma limitação dos marcos anteriores à menor capacidade que a resolve, com verificação e nova observação de uso. |

Em M1, projetos podem ser identificados em notas locais; classificação e promoção podem ser edições explícitas validadas. Reutilização, evidência de execução e Learn Back podem ser notas com origem, destino, record, resultado, custo e referências de verificação. Isso não exige comandos `route`, `promote`, `reuse` ou `learn`, nem implementações completas de Context, Relations ou Retrieve.

M1 começa com texto e Markdown. Sidecars opacos, diretórios compostos, relações avançadas e filtros adicionais permanecem no horizonte, sem bloquear a primeira prova. A busca deve aceitar tanto candidatos não classificados quanto records organizados válidos.

Falhas de captura, busca, segurança ou ergonomia devem ser corrigidas no marco em que aparecerem, dentro do contrato aplicável. M4 organiza a expansão; não exige esperar pela recorrência para resolver um problema que impeça o uso.

Segurança, integridade e verificação não ficam adiadas: validar a entrada antes de gravar, preservar originais, impedir sobrescrita e aplicar os gates das operações entregues. A interface filtrada e a configuração sem acesso bruto são pré-requisitos de M2, nunca tarefas posteriores ao teste com um consumidor externo.

Antes da observação real, escolher uma necessidade recorrente, um acervo pequeno de conteúdo existente e projetos com trabalho efetivo. A implementação usa fixtures sintéticas; acesso a acervos pessoais e execução de tarefas em outros projetos dependem de seu escopo autorizado. Falta de oportunidade real deixa a validação de produto pendente, sem impedir a verificação técnica local.

Priorizar o reaproveitamento do workflow de desenvolvimento descrito no Frame seção 27: recuperar um procedimento aplicado no AIKM, adaptar o contexto para outro produto e verificar o benefício. Usar a skill diretamente no desenvolvimento atual demonstra aplicação do processo; não contar isso como recuperação via AIKM nem como evidência antecipada de M1-M3.

O primeiro contrato após o bootstrap entrega a parcela técnica de M1. A observação real e o adapter possuem limites explícitos próprios; não inferir autorização para operar outros projetos, configurar contas ou enviar conteúdo a partir deste plano.

---

# 5. Iteração 00 — Bootstrap técnico

Estado: `DONE`, com aceite do responsável em 2026-09-15 no
[TC-0001 v0.2](contracts/TC-0001-iteration-00-bootstrap.md#15-acceptance-record).
A [verificação de encerramento](verification/VR-0002-bootstrap-acceptance.md)
confirma CLI, gates, reprodução do setup e integridade do escopo. As decisões
estão no [ADR-0001](adrs/ADR-0001-technical-bootstrap.md). Os critérios abaixo
permanecem como referência do incremento concluído; não exigem recriar o
contrato ou escolher novamente a stack. TC-0002 continua proposto e não ativo.

## Objetivo

Criar a menor base de implementação necessária para executar o plano.

A stack ainda não deve ser escolhida por preferência abstrata.

Ela deve servir ao problema atual.

---

## Decisões necessárias

Escolher:

- linguagem/runtime;
- biblioteca ou mecanismo de CLI;
- parser de Markdown/frontmatter;
- validação de schema;
- estratégia de filesystem;
- estratégia de testes;
- lint/format;
- geração de IDs;
- suporte a Git sem torná-lo obrigatório.

---

## Critérios para a stack

Priorizar:

- distribuição local simples;
- boa manipulação de arquivos;
- execução rápida de CLI;
- parsing seguro de YAML/frontmatter;
- testes rápidos;
- poucas dependências operacionais;
- bom suporte multiplataforma, sem transformar isso em requisito de MVP.

---

## Entregáveis

- repositório;
- estrutura inicial de código;
- suíte de testes;
- lint/format;
- comando mínimo:

```bash
aikm --help
```

- ADR curto da stack.

---

## Task Contract

Antes do build, criar:

```text
Radiant Task Contract — AIKM — Iteration 00
```

---

## Critério de saída

- `aikm --help` funciona;
- testes executam;
- ADR registra as decisões estruturais;
- nenhuma feature de produto foi implementada prematuramente.

---

# 6. Iteração 01 — Canonical Workspace

## Objetivo

Provar que o AIKM pode existir como um sistema legível no filesystem antes de qualquer indexação sofisticada.

---

## Capacidade entregue

```bash
aikm init [path]
```

---

## Implementar

Estrutura inicial:

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

Implementar também:

- descoberta da raiz;
- leitura de `aikm.yaml`;
- defaults de visibility/egress;
- criação idempotente;
- proteção contra sobrescrita acidental.

---

## Não implementar

- banco;
- semantic search;
- graph;
- adapter real;
- auto-routing.

---

## Testes

- criar workspace vazio;
- reabrir workspace;
- recusar init destrutivo;
- detectar manifest inválido;
- apagar `.aikm/` sem afetar conteúdo canônico.

---

## Evidência

Abrir o workspace apenas com editor de texto e conseguir compreender sua estrutura.

---

## Critérios relacionados

- AC-01;
- AC-19 parcialmente.

---

# 7. Iteração 02 — AIKM Record + Provenance

## Objetivo

Definir a unidade canônica que permitirá representar conhecimento sem acoplar arquitetura a prompts, skills ou agents.

Em M1, entregar records textuais com schema de entrada e validação de records organizados. O suporte opaco e demais capacidades desta seção ficam para contratos posteriores, conforme evidência, sem declarar Iteração 02 integralmente concluída.

---

## Implementar

Schema de entrada de `AIKM Record`, conforme Spec seção 14, com:

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

`description`, `knowledgeRole` e `artifactKind` são opcionais para candidatos no inbox e obrigatórios ao organizar fora dele ou promover. Candidato não classificado arquivado conserva a exceção prevista na Spec. Gerar campos técnicos e defaults restritivos automaticamente; validar campos opcionais quando fornecidos.

Suportar também:

- tags;
- project refs;
- links;
- `derivedFrom`;
- `supersedes`;
- `supersededBy`.

---

## Modelo obrigatório

Separar:

```text
artifactKind
```

de:

```text
knowledgeRole
```

Exemplo:

```yaml
artifactKind: skill
knowledgeRole: procedure
```

---

## Suporte a conteúdo opaco

Implementar pelo menos um caso de sidecar:

```text
paper.pdf
paper.pdf.aikm.yaml
```

ou diretório composto:

```text
my-skill/
  AIKM.yaml
  SKILL.md
```

---

## Source e derivação

Demonstrar:

```text
Source original
    ↓ derivedFrom
Knowledge sintetizado
```

sem alterar o original.

---

## Lifecycle inicial

```text
candidate
active
superseded
archived
```

---

## Trust inicial

```text
raw
unverified
reviewed
canonical
deprecated
```

---

## Testes

- criar record Markdown;
- validar campos;
- rejeitar `knowledgeRole` inválido;
- aceitar novo `artifactKind` permitido pela estratégia adotada;
- preservar source opaca;
- criar síntese ligada por `derivedFrom`;
- alterar filename sem alterar ID;
- distinguir lifecycle e trust.
- aceitar captura sem role/kind/description;
- rejeitar organização ou promoção incompleta;
- manter classificação pendente visível na busca;
- preservar ID e origem durante organização manual validada.

---

## Evidência

Criar records reais a partir dos próprios documentos do Radiant/AIKM.

---

## Critérios relacionados

- AC-05;
- AC-06;
- AC-07;
- AC-08;
- AC-09.

---

# 8. Iteração 03 — Inbox + Security Pre-check

## Objetivo

Permitir captura de baixo atrito sem sacrificar segurança.

M1 entrega texto e arquivos Markdown/textuais. Outros formatos seguem contratos posteriores. Segurança precede toda gravação no workspace, inclusive inbox e temporários.

---

## Capacidades entregues

```bash
aikm capture <path|text>
```

---

## Fluxo

```text
capture
   ↓
security pre-check
   ↓
inbox
```

---

## Implementar

- captura de texto;
- captura de arquivo;
- criação de ID;
- provenance mínima;
- lifecycle inicial;
- trust inicial;
- detecção básica de padrões de secrets;
- default deny para egress;
- possibilidade de armazenar `secretRef`, nunca o secret.

Para a captura simples, o usuário fornece somente conteúdo ou localização. Schema, ID, título inicial editável, datas, modo de origem e defaults são automáticos. Classificação, promoção, confiança superior e autorização de saída não são perguntas obrigatórias dessa operação.

---

## Regras

Conteúdo capturado:

- não é automaticamente knowledge;
- não é automaticamente active;
- não é automaticamente confiável.

---

## Casos de segurança

Rejeitar antes de persistir conteúdo no workspace quando houver padrões conhecidos de:

- API key conhecida;
- token;
- password;
- private key;
- cookie/session token.

Não reproduzir o valor em stdout, stderr, logs ou temporários. A detecção é parcial e não autoriza saída de dados. Verificar o conteúdo efetivamente gravado, não apenas o status de saída do comando.

Permitir referência como:

```yaml
secretRef:
  provider: macos-keychain
  name: openai-personal
```

---

## Testes

- capturar texto simples;
- capturar arquivo;
- manter provenance;
- detectar secret;
- garantir `egressAllowed: false` por default;
- garantir que conteúdo rejeitado não vá para role final.

---

## Critérios relacionados

- AC-02;
- AC-03.

---

# 9. Checkpoint A — A captura é sustentável?

Antes de implementar Router completo, responder:

- capturar ficou simples?
- metadata mínima está excessiva?
- provenance é suficiente?
- security pre-check gera muitos falsos positivos?
- inbox é compreensível?

Se captura já estiver burocrática:

> simplificar antes de continuar.

Esse checkpoint existe para impedir que o AIKM resolva reconstrução criando uma nova obrigação de catalogação pesada.

---

# 10. Iteração 04 — Router + Promotion + Discard

Em M1, usar organização/promoção manual explícita com validação da Spec seção 14. Os comandos desta capacidade entram quando a prática observada justificar automatizar a operação; não são pré-requisitos de busca ou do experimento.

## Objetivo

Transformar intake em conhecimento organizado sem exigir classificação perfeita no momento da captura.

---

## Capacidades entregues

```bash
aikm route <id>
aikm promote <id>
```

---

## Implementar

Router inicial para:

```text
source
knowledge
context
operational-memory
procedure
action
evaluation
output
DO_NOT_STORE
```

O Router pode ser:

- determinístico;
- interativo;
- baseado em árvore de decisão.

Não usar IA como requisito.

---

## Promotion

Implementar:

```text
candidate → active
```

com registro mínimo de:

- timestamp;
- actor, quando disponível;
- razão opcional.

Não promover automaticamente para `canonical`.

---

## Discard

Permitir descartar conscientemente:

- duplicação;
- log trivial;
- estado transitório;
- conteúdo sem utilidade futura.

---

## Inbox hygiene

Adicionar verificação de itens antigos no `doctor` posteriormente.

Não é necessário criar daemon ou job recorrente nesta fase.

---

## Testes

- route para cada role principal;
- `DO_NOT_STORE`;
- candidate → active com campos completos; edição manual incompleta é recusada pela validação;
- source permanece `raw` quando apropriado;
- conteúdo gerado permanece `unverified` até revisão;
- routing não elimina provenance.

---

## Critérios relacionados

- AC-04;
- AC-08.

---

# 11. Iteração 05 — Context + Procedure + Memory + Relations

## Objetivo

Provar que o AIKM consegue diferenciar o que sabemos, o contexto em que algo vale, como executar e o que deve estar disponível antes de agir.

---

## Implementar

### Project como Context

Representar projeto:

```yaml
knowledgeRole: context
artifactKind: project
```

### Procedure

Suportar:

```text
skill
workflow
checklist
playbook
```

### Operational Memory

Representar ponteiros curtos para conteúdo canônico.

### Relations

Inicialmente através de:

```yaml
links:
  - type: uses
    ref: aikm:...
```

Tipos mínimos:

```text
uses
depends-on
derived-from
related-to
supersedes
supports
evaluates
produces
```

---

## Regra crítica

Operational Memory não pode virar cópia de procedures ou knowledge.

A demonstração desta iteração precisa possuir:

```text
memory pointer
   ↓
procedure canonical
   ↓
knowledge/context necessário
```

---

## Testes

- associar record a projeto;
- criar procedure;
- criar memory pointer;
- navegar relação;
- detectar link quebrado;
- demonstrar que memory não duplica body completo.

---

## Critérios relacionados

- AC-10;
- AC-11;
- AC-12.

---

# 12. Iteração 06 — Search

Antecipar em M1 a busca por título e conteúdo de records textuais, incluindo candidatos no inbox, com ordem determinística e indicação de classificação pendente. A parcela restante desta seção não bloqueia a primeira reutilização.

## Objetivo

Provar que a estrutura já criada é recuperável sem banco, embeddings ou IA.

---

## Capacidade entregue

```bash
aikm search "<query>"
```

---

## Filtros

```text
--role
--kind
--project
--trust
--lifecycle
--tag
```

---

## Estratégia inicial

Utilizar o menor mecanismo suficiente:

- scan de arquivos;
- índice leve descartável, se necessário;
- ferramenta textual local;
- metadata parseada.

Não introduzir SQLite apenas por conveniência.

---

## Saída mínima

Cada resultado deve mostrar:

- título;
- id;
- `knowledgeRole`;
- `artifactKind`;
- trust;
- lifecycle;
- path;
- projeto quando relevante.

Incluir trecho pertinente para permitir avaliar o resultado. Role/kind ausentes no inbox aparecem como classificação pendente. Não exigir os filtros adicionais antes de evidência de necessidade. Saídas destinadas a um consumidor externo passam pela fronteira local da Spec seção 50 antes de qualquer entrega.

---

## Testes

- título;
- descrição;
- conteúdo;
- filtros;
- `archived` fora do padrão;
- `deprecated` visível como tal;
- `candidate` distinto de `active`;
- source e procedure retornadas com papéis distintos.

---

## Critérios relacionados

- AC-16.

---

# 13. Checkpoint B — Precisamos de banco?

Depois de Search, medir:

- latência;
- complexidade do código;
- dificuldade dos filtros;
- volume real;
- ergonomia.

SQLite só entra agora se houver uma limitação observável que afete o experimento.

Se Search estiver adequada:

> continuar sem banco.

A ausência de SQLite não é dívida técnica nesta fase.

É decisão experimental.

---

# 14. Iteração 07 — Execution Evidence

Notas locais de execução e links de verificação bastam nos marcos iniciais. Implementar esta capacidade estruturada somente quando o registro manual revelar uma limitação relevante.

## Objetivo

Criar a ponte entre “artefato existente” e “aprendizado derivado de uso real”.

---

## Implementar

`action` com kinds:

```text
run
decision
handoff
```

Um Execution Record deve ser opcional e seletivo.

---

## Persistir somente quando necessário para

- reprodução;
- verificação;
- diagnóstico;
- recuperação;
- handoff;
- suporte a aprendizado.

---

## Campos conceituais

```text
project
procedures
startedAt
completedAt
outcome
evidence
produced
```

---

## Regra de contenção

Execuções triviais bem-sucedidas não precisam virar records.

O sistema deve continuar permitindo não armazenar.

---

## Testes

- run ligado a projeto;
- run ligado a procedure;
- evidência referenciada;
- output produzido referenciado;
- run trivial pode ser omitido sem quebrar fluxo.

---

## Critérios relacionados

- AC-13.

---

# 15. Iteração 08 — Evaluation + Experience + Learn Back

Nos marcos iniciais, registrar manualmente finding, evidência, `fixTarget`, alteração e verificação. A correção real continua obrigatória quando aplicável; o comando especializado depende de necessidade observada.

## Objetivo

Transformar execução em aprendizado operacional.

---

## Implementar

Kinds mínimos de `evaluation`:

```text
experience
finding
verification
```

Opcionalmente:

```text
rubric
```

se já houver caso real.

---

## Experience

Deve suportar:

- statement;
- confidence;
- evidence refs;
- project refs.

---

## Finding

Deve suportar:

- finding type;
- severity;
- evidence refs.

---

## Learn Back

Deve registrar:

```text
finding
evidenceRefs
diagnosis
fixTarget
changeRef
verificationRef
```

---

## Capacidade entregue

```bash
aikm learn
```

Pode ser interativa.

---

## Fluxo obrigatório

```text
Run / Verification
      ↓
Finding
      ↓
Diagnosis
      ↓
Fix Target
      ↓
Change
```

---

## Testes

- Experience com evidence;
- Finding com execution evidence;
- `fixTarget` para procedure;
- `fixTarget` para context;
- `fixTarget` para memory;
- mudança preserva referência ao finding;
- Learn Back sem `fixTarget` é incompleto quando a correção é conhecida.

---

## Critérios relacionados

- AC-14;
- AC-15.

---

# 16. Checkpoint C — Estamos realmente aprendendo?

Antes de implementar retrieval mais sofisticado, verificar a experiência dos marcos M1-M3, inclusive quando as evidências são manuais:

- Execution Record ajudou ou virou log?
- Experience possui evidência real?
- `fixTarget` é compreensível?
- alguma procedure/context/memory realmente foi corrigida?

Se o Learn Back estiver apenas gerando documentos:

> interromper e simplificar.

O objetivo é alterar comportamento futuro.

---

# 17. Iteração 09 — Retrieve

Busca lexical de M1 atende à primeira recuperação. Implementar ranking adicional e este comando quando observações reais mostrarem o que a busca inicial deixa de resolver; o adapter mínimo não depende desta capacidade completa.

## Objetivo

Responder à principal pergunta de uso:

> **O que do meu repertório parece útil para esta necessidade?**

---

## Capacidade entregue

```bash
aikm retrieve "<need>"
```

---

## Sinais iniciais

Combinar de forma simples:

1. título;
2. descrição;
3. conteúdo;
4. tags;
5. projeto;
6. role;
7. links;
8. trust;
9. lifecycle.

---

## Regras

- IA não é necessária;
- `archived` fora do padrão;
- `deprecated` penalizado ou marcado;
- `candidate` não equivale a `active`;
- resultados mostram role/trust;
- a razão do resultado deve ser compreensível;
- source bruta e procedure canônica não são apresentadas como equivalentes.

---

## Saída exemplo

```text
1. Code Review Procedure
   role: procedure
   kind: skill
   trust: reviewed

   reason:
   - matches "review"
   - used by current project type
   - linked evaluation exists
```

---

## Testes

- correspondência direta;
- correspondência por descrição;
- role influence;
- trust influence;
- related evaluation;
- candidate vs active;
- resultado sem IA.

---

## Critérios relacionados

- AC-17.

---

# 18. Checkpoint D — Retrieval lexical é suficiente?

Medir em necessidades reais:

- encontrou o que deveria?
- ranking ficou aceitável?
- roles melhoraram interpretação?
- relações ajudaram?
- search + retrieve resolvem o caso sem embeddings?

Somente considerar semantic search se houver falha concreta de recall relevante.

---

# 19. Iteração 10 — Adapter inicial

Entregar a parcela mínima no marco M2, logo após a primeira passagem local de M1. Usar busca existente e encaminhamento manual de organização/aprendizado; não esperar comandos `retrieve`, `reuse` ou `learn`.

## Objetivo

Provar que um agent consegue utilizar o AIKM sem duplicar seu core.

---

## Escolha do harness

Usar primeiro o harness realmente empregado no desenvolvimento do experimento.

Não criar adapters para várias ferramentas apenas para demonstrar generalidade.

---

## Adapter Contract

Responder:

1. onde está o AIKM root?
2. o que carregar ao iniciar sessão?
3. como buscar knowledge/context/procedures?
4. como enviar novo material para intake?
5. como encaminhar findings para Learn Back?
6. como aplicar visibility/egress?

---

## Session bootstrap

Após configuração local única da raiz, uma sessão nova deve descobrir o acervo sem receber o arquivo esperado. Para consumidores externos, obter pela interface local filtrada somente o conteúdo permitido de:

```text
system/INDEX.md
memory/*
adapter-specific pointer
```

O restante é recuperado sob demanda.

Cada recuperação de corpo ou relação passa pela mesma fronteira. Ausência de conteúdo permitido produz uma resposta compreensível sem revelar o item negado. Não carregar diretamente o workspace no contexto do consumidor externo.

---

## Egress enforcement

Antes de entregar conteúdo a provider externo:

- verificar `visibility`;
- verificar `egressAllowed`;
- negar `private`;
- negar `restricted`;
- default deny em caso de ambiguidade.

Aplicar a Spec seção 50 em processo local antes de responder à ferramenta do adapter. Cobrir bootstrap, índice, memory, títulos, trechos, caminhos, relações e erros; fontes combinadas preservam a restrição de cada origem. Política do ponteiro não libera o destino.

O contrato de M2 deve demonstrar configuração sem acesso bruto do consumidor externo ao workspace. Se não for possível, manter o experimento local e reportar a limitação. Instruções textuais ao agent não são prova de enforcement.

---

## Teste de duplicação

A procedure compartilhada deve existir somente no AIKM.

O adapter aponta para ela.

Não copiar o body para a memória do harness.

---

## Testes

- fresh session encontra AIKM;
- bootstrap permanece pequeno;
- busca de M1 acessível, sem depender do comando `retrieve`;
- novo conhecimento vai para intake;
- failure pode originar Learn Back;
- conteúdo private/restricted não sai;
- core não está duplicado.
- consulta formulada pela necessidade, sem ID/título/path da resposta esperada;
- consumidor simulado recebe conteúdo permitido e nunca recebe marcadores sintéticos negados;
- negação cobre bootstrap, corpo, metadados, links e fontes combinadas;
- configuração de integração não oferece caminho de leitura bruta que contorne a filtragem.

---

## Critérios relacionados

- AC-20;
- AC-21.

---

# 20. Iteração 11 — Reuse Event

Notas manuais com os fatos da Spec seção 37 sustentam a primeira prova. O comando entra quando houver necessidade observada de automatizar esse registro; sua ausência não impede observar reutilização.

## Objetivo

Criar a evidência explícita do fenômeno central do produto.

---

## Capacidade entregue

```bash
aikm reuse <record> --from <project-a> --to <project-b>
```

---

## Implementar

Record com:

```yaml
knowledgeRole: action
artifactKind: reuse-event
```

Campos principais:

- source project;
- target project;
- record reutilizado;
- outcome;
- `reconstructionAvoided`;
- nota;
- timestamp.

---

## Valores sugeridos

```text
outcome:
  useful
  partially-useful
  not-useful

reconstructionAvoided:
  yes
  partial
  no
  unknown
```

---

## Testes

- references válidas;
- source/target diferentes;
- reutilização recuperável;
- reuse aparece em search;
- evento sobrevive à remoção de `.aikm/`.

---

## Critérios relacionados

- AC-18;
- AC-19.

---

# 21. Iteração 12 — Experimento real Projeto A → Projeto B

Iniciar no marco M1 e repetir em M2-M3. O ID 12 identifica o experimento, não sua posição após todas as capacidades anteriores.

## Objetivo

Testar a hipótese assim que captura e busca local estiverem utilizáveis, mantendo a verificação técnica das capacidades entregues.

Esta é a iteração mais importante.

As etapas abaixo podem utilizar notas e edições manuais validadas. Registrar quais operações foram manuais e seu custo; não apresentar essas operações como funcionalidades implementadas.

---

## Escolha dos projetos

O Projeto A precisa produzir conhecimento real.

O Projeto B precisa possuir uma necessidade real relacionada.

Não construir um cenário artificial apenas para fazer a hipótese passar.

Antes de cada observação, registrar a necessidade, a forma habitual de resolver/procurar e o resultado que tornaria o conteúdo aplicável. Usar notas locais curtas; incluir falhas e comparações incertas. Não pré-carregar no Projeto B a solução, o ID ou o arquivo esperado.

---

## Projeto A — Produção

Executar:

1. registrar projeto como context;
2. capturar material real;
3. route;
4. promover somente o que merece permanecer;
5. produzir ou consolidar ao menos uma procedure/knowledge record;
6. utilizar o record;
7. registrar execution evidence se material;
8. registrar Experience ou Finding quando houver;
9. preservar provenance.

---

## Intervalo

Evitar preparar manualmente o Projeto B com conhecimento do teste.

O objetivo é observar recuperação real.

---

## Projeto B — Reutilização

Executar:

1. registrar Projeto B;
2. formular uma necessidade real;
3. usar `search` ou `retrieve`;
4. encontrar conhecimento de A;
5. inspecioná-lo;
6. reutilizá-lo;
7. executar o trabalho;
8. verificar resultado;
9. registrar `ReuseEvent`;
10. avaliar `reconstructionAvoided`.

---

## Learn Back após reutilização

Executar:

1. identificar uma descoberta do uso;
2. registrar evidence;
3. criar Finding/Experience;
4. definir `fixTarget`;
5. alterar a camada responsável;
6. utilizar a mudança em execução posterior quando possível.

---

## Evidência primária

```text
Knowledge Reuse Event >= 1
```

e:

```text
reconstructionAvoided = yes
```

ou evidência qualitativa forte equivalente.

Isso demonstra possibilidade, não adoção recorrente. A verificação de M3 exige necessidades posteriores em sessões ou tarefas distintas, com esforço de manutenção, tentativas malsucedidas e uso espontâneo registrados conforme a seção 36. Sem oportunidades suficientes, declarar recorrência inconclusiva.

---

## Evidência secundária

```text
Learn Back Event >= 1
```

com mudança efetivamente reutilizável.

---

# 22. Resultados possíveis do experimento

## Sucesso forte

Conhecimento é encontrado, reutilizado e evita reconstrução; Learn Back melhora ciclo posterior.

---

## Sucesso parcial

Conhecimento é reutilizado, porém o ganho é pequeno ou Learn Back não se demonstra.

---

## Falha de captura

O conhecimento útil nunca foi preservado adequadamente.

---

## Falha de classificação

O conteúdo existe, porém foi colocado em papel que prejudicou sua recuperação ou uso.

---

## Falha de retrieval

Conhecimento adequado existe, porém não é encontrado.

---

## Falha de confiança

Conteúdo é encontrado, porém não existe confiança suficiente para utilizá-lo.

---

## Falha de ergonomia

O custo de captura/manutenção supera o benefício.

---

## Falha de hipótese

Mesmo com captura e retrieval adequados, reutilização não produz valor relevante.

Todos os resultados são aprendizados válidos.

---

# 23. Iteração 13 — Verify

## Objetivo

Verificar produto, implementação e comportamento experimental de maneira independente do Build.

Aplicar nos marcos M1-M3 aos comportamentos efetivamente entregues; repetir apenas quando novas capacidades ou riscos justificarem. Não esperar a capacidade 13 para verificar segurança, integridade ou benefício.

---

## Rigor e independência

Como se trata de infraestrutura durável utilizada por agents e potencialmente contendo conteúdo sensível, exigir verificação estrutural, segurança, portabilidade e inspeção do percurso real conforme as parcelas entregues e o contrato. Os checks concretos abaixo e a evidência executada definem a cobertura.

O rótulo anterior "Tier 2 / Deep" não possui definição operacional nos artefatos canônicos disponíveis. Não declarar conformidade com esse rótulo. Registrar o método de revisão, o que foi independente da implementação e suas limitações, conforme a Constitution e a skill de ciclo, elevando checks de segurança quando o risco exigir.

---

## Verificação estrutural

Confirmar:

- workspace manifest;
- record schema;
- IDs;
- links;
- sidecars;
- lifecycle;
- trust;
- provenance;
- role/kind.

---

## Verificação de segurança

Confirmar:

- secret detection;
- `secretRef`;
- visibility;
- egress;
- outputs;
- default deny;
- adapter enforcement.

---

## Verificação de portabilidade

Executar:

1. copiar workspace;
2. remover `.aikm/`;
3. abrir estrutura;
4. executar search;
5. resolver links;
6. encontrar reuse events.

---

## Verificação do adapter

Confirmar:

- bootstrap limitado;
- core não duplicado;
- pointers funcionam;
- egress policy funciona.

---

## Verificação de produto

Confirmar:

- houve Reuse Event real;
- houve ou não reconstrução evitada;
- retrieval foi útil;
- capture cost foi aceitável.
- custo de manutenção e buscas malsucedidas entrou na comparação;
- benefício foi comparado ao modo habitual de trabalhar;
- primeira reutilização foi distinguida de utilidade recorrente;
- consultas espontâneas foram distinguidas das solicitadas pelo experimento.

---

## Verificação de aprendizado

Confirmar:

- Finding possui evidence;
- `fixTarget` é explícito;
- a mudança ocorreu;
- a mudança pode ser recuperada posteriormente.

---

## Acceptance Criteria

Mapear AC-01 a AC-22 da Implementation Spec v0.3.1 aos outputs de cada contrato. Em marcos parciais, verificar a parcela entregue e marcar o restante como pendente/não implementado. A verificação completa do horizonte exige todos os AC aplicáveis; sucesso de M1 não substitui essa cobertura.

---

## Artefato produzido

# Verification Report - AI Knowledge Manager (AIKM) v0.3

Registrar:

- PASS;
- PASS_WITH_NOTE;
- HOLD;
- FAIL;

para cada área relevante.

---

# 24. Iteração 14 — Learn

## Objetivo

Transformar o primeiro ciclo em decisão e capacidade.

---

## Artefato produzido

# Learning Record - AI Knowledge Manager (AIKM) v0.3

Nos marcos iniciais, preservar somente evidência e findings que orientem o próximo incremento. O relatório completo consolida o ciclo; não exigir sua automação ou um documento abrangente por tentativa.

---

## Perguntas obrigatórias

### Arquitetura

- filesystem funcionou como authority?
- `.aikm/` permaneceu realmente descartável?
- SQLite fez falta?
- Git foi suficiente para histórico?
- folders semânticos fizeram sentido?

### Modelo

- `artifactKind × knowledgeRole` ficou claro?
- quais roles foram úteis?
- algum role foi artificial?
- lifecycle e trust ficaram compreensíveis?
- provenance teve custo aceitável?

### Intake

- capture foi barato?
- inbox ajudou?
- Router reduziu ou aumentou esforço?
- `DO_NOT_STORE` foi usado?
- quais dados foram capturados desnecessariamente?

### Operação

- Operational Memory ficou curta?
- procedures foram reutilizáveis?
- Execution Records ficaram seletivos?
- Experience teve evidência útil?

### Retrieval

- Search bastou?
- Retrieve melhorou uso?
- semantic search fez falta?
- ranking por trust/role ajudou?

### Agents

- adapter foi realmente fino?
- houve duplicação?
- bootstrap ficou pequeno?
- one body/pointers funcionou?

### Segurança

- egress policy foi compreensível?
- default deny atrapalhou?
- secret detection funcionou?
- outputs exigiram nova política?

### Hipótese

- o Projeto B começou melhor por causa do Projeto A?
- houve reconstrução evitada?
- qual conhecimento foi reutilizado?
- quanto trabalho foi evitado?
- o benefício compensou captura, manutenção e recuperação?
- houve retorno espontâneo em tarefas posteriores?
- quais observações justificam expandir, ajustar ou parar?

### Learn Back

- houve um finding material?
- `fixTarget` apontou para a camada correta?
- a correção modificou comportamento posterior?
- o Learn Back virou prática ou documentação?

---

## Decisão de ciclo

Escolher:

```text
continue
adjust
pause
stop
```

com evidência.

---

# 25. Task Contracts durante o plano

Cada incremento que produzir alterações materiais deve ter um contrato delimitado antes do Build. Quando abranger parcelas de várias capacidades, listar o que entrega e o que permanece pendente.

Identidade, filename estável, status e ativação seguem [a convenção de contratos](contracts/README.md). O ponteiro [ACTIVE.md](contracts/ACTIVE.md) é a única fonte de ativação; a ordem dos marcos ou a existência de uma proposta não ativa um contrato.

Não criar contratos retroativamente apenas para satisfazer o processo.

O contrato existe quando há delegação ou execução bounded que se beneficia de um agreement explícito.

---

# 26. Conteúdo mínimo de um Task Contract

Cada contrato deve responder:

```text
Task
Purpose
Inputs
Outputs
Allowed paths
Non-goals
Acceptance criteria
Verification commands
Readback
Security restrictions
Blockers
```

Quando uma tarefa não puder ser concluída dentro do contrato:

> HOLD e retornar ao Plan.

Não expandir silenciosamente.

---

# 27. Definition of Done por iteração

Uma iteração está concluída somente quando:

1. comportamento previsto funciona;
2. testes relevantes passam;
3. critérios do incremento foram demonstrados;
4. readback confirma os artefatos gerados;
5. documentação operacional mínima está atualizada;
6. nenhum dado canônico depende de `.aikm/`;
7. nenhuma feature futura entrou sem necessidade;
8. findings materiais receberam destino;
9. Task Contract, quando utilizado, foi respeitado.

---

# 28. Estratégia de testes

## Unit tests

Cobrir:

- schema;
- IDs;
- role/kind;
- lifecycle;
- trust;
- egress;
- routing;
- ranking;
- secret patterns.

---

## Integration tests

Cobrir:

- CLI + filesystem;
- capture;
- route;
- promote;
- links;
- search;
- retrieve;
- learn;
- reuse;
- adapter boundaries.

---

## End-to-end

Em M1, executar init, captura, busca a partir de outro diretório e organização manual seguida de validação. Os fluxos abaixo descrevem o horizonte; comandos ainda não implementados permanecem pendentes e não impedem a primeira prova manual equivalente.

Fluxo 1:

```text
init
  ↓
capture
  ↓
route
  ↓
promote
  ↓
search
```

Fluxo 2:

```text
project
  ↓
procedure
  ↓
run
  ↓
finding
  ↓
learn back
```

Fluxo 3:

```text
Project A
  ↓
retrieve in Project B
  ↓
reuse
  ↓
verify
  ↓
learn back
```

---

# 29. Fixture / Golden Workspace

Criar um workspace pequeno e explícito para testes automatizados, ampliado somente com as capacidades entregues. M1 começa com candidatos textuais, um record organizado, um arquivado e entradas inválidas/secrets sintéticas; os demais casos entram nos contratos correspondentes.

Conforme as capacidades forem entregues, o fixture passa a incluir:

- source;
- knowledge;
- project context;
- procedure;
- memory pointer;
- run;
- experience;
- finding;
- reuse event;
- archived record.

O fixture serve para:

- schema;
- links;
- search;
- doctor;
- portabilidade.

Ele não substitui o experimento real.

---

# 30. `aikm doctor`

As verificações de integridade e segurança entram junto com cada operação. M1 exige validação de manifest, entrada, records lidos e organização manual, com diagnóstico acionável; M2 exige a fronteira de saída verificada. Essas verificações podem existir nos comandos e testes locais, sem exigir o comando `doctor` completo antes da primeira experiência A → B. A interface concreta para validar edições manuais deve constar do contrato de M1.

Consolidar os checks em `doctor` quando o uso justificar, sem adiar controles necessários às operações já entregues.

Checks mínimos finais:

- manifest;
- frontmatter;
- IDs duplicados;
- refs quebradas;
- role/kind inválido;
- lifecycle/trust inválidos;
- source sidecars;
- private/restricted com egress permitido;
- secrets comuns;
- memory excessivamente longa;
- inbox envelhecido;
- records não encontráveis pelo INDEX quando aplicável.

Resultado:

```text
PASS
PASS_WITH_NOTE
FAIL
```

Doctor não corrige automaticamente conhecimento sem autorização.

---

# 31. Estratégia de commits

Commits devem refletir capacidades.

Exemplos:

```text
feat(workspace): initialize canonical AIKM workspace
feat(records): add two-axis AIKM record model
feat(intake): add secure inbox capture
feat(router): classify and promote knowledge records
feat(knowledge): add context procedures and memory pointers
feat(search): add local lexical search
feat(actions): persist selective execution evidence
feat(learning): add experience findings and learn back
feat(retrieve): rank reusable knowledge without AI
feat(adapter): connect first agent harness
feat(reuse): record cross-project reuse events
```

Evitar commits gigantes que misturem várias iterações.

---

# 32. ADRs necessários

Criar ADR apenas para decisões estruturais relevantes.

Candidatos iniciais:

- linguagem/runtime;
- formato de frontmatter/schema;
- estratégia de ID;
- filesystem como authority;
- política de lifecycle/trust;
- primeira estratégia de search;
- eventual introdução de SQLite;
- eventual introdução de semantic retrieval.

Não criar ADR para toda decisão de implementação.

---

# 33. Gates de complexidade

Antes de introduzir as capacidades abaixo, exigir evidência.

## SQLite

Só se filesystem search/filter for insuficiente.

## Embeddings

Só se lexical retrieval falhar em casos reais importantes.

## Graph database

Só se links explícitos se tornarem insuficientes para consultas relevantes.

## UI

Só se CLI/filesystem criarem fricção que afete adoção ou hipótese.

## Cloud

Só se existir necessidade real de sincronização ou disponibilidade remota.

## Automatic ingestion

Só se captura manual for gargalo demonstrado.

## Automatic promotion

Não introduzir no primeiro ciclo.

---

# 34. Critérios de interrupção

Parar e reavaliar se:

- capture for demasiadamente caro;
- Router exigir demasiada manutenção;
- roles não forem compreensíveis;
- metadata superar valor;
- Operational Memory virar duplicação;
- adapters copiarem o core;
- logs começarem a dominar o workspace;
- retrieval depender de IA para funcionar minimamente;
- SQLite surgir apenas como preferência técnica;
- o experimento A → B estiver sendo artificialmente preparado;
- Learn Back não modificar nenhuma camada real.

Parar também é um resultado válido do Radiant.

---

# 35. O que explicitamente não entra neste ciclo

Mesmo se parecer interessante durante o build:

- aplicação desktop;
- aplicação web;
- sync;
- cloud;
- contas;
- teams;
- colaboração;
- marketplace;
- embeddings;
- vector DB;
- graph DB;
- RAG completo;
- chat com o vault;
- multi-agent orchestration;
- ingestão automática de chats;
- memory extraction irrestrita;
- full evidence packet;
- global prompt injection;
- automatic canonical promotion;
- sistema público de plugins;
- OKF compatibility;
- migrations complexas;
- analytics sofisticado.

Tudo isso precisa esperar evidência.

---

# 36. Métricas do ciclo

## Principal

### Knowledge Reuse Event

Meta inicial:

```text
>= 1 evento real
```

Esse limiar demonstra possibilidade. Para utilidade recorrente, observar necessidades reais posteriores em sessões ou tarefas distintas; uma única oportunidade não prova adoção.

---

## Principal qualitativa

### Reconstruction Avoided

```text
yes
partial
no
unknown
```

---

## Aprendizado

### Learn Back Event

Meta inicial:

```text
>= 1 finding material
→ fixTarget
→ mudança realizada
```

---

## Auxiliares

- Capture Cost;
- Maintenance Cost;
- tempo até encontrar, inspecionar e decidir aplicar conteúdo útil;
- buscas abandonadas/sem resultado;
- trabalho ou erro evitado com evidência;
- consultas espontâneas versus solicitadas;
- Retrieval Usefulness;
- Duplication Avoided;
- Provenance Recovery;
- quantidade de records descartados;
- tempo de search;
- findings sem fix target;
- inbox aging;
- false secret warnings.

As métricas não devem virar objetivo em si.

## Comparação com o modo habitual de trabalhar

Usar o protocolo das seções 70-71 da Spec. Antes da consulta, anotar a necessidade e como ela seria atendida sem AIKM. Depois, registrar resultado, verificação e esforço de captura, manutenção e recuperação do recorte, inclusive de itens não reutilizados. Separar medições de estimativas; não alegar comparação controlada ao repetir uma tarefa cuja solução já ficou conhecida.

Benefício repetido que compense o esforço e retorno espontâneo sustentam continuidade. Resultado negativo pede ajuste ou parada; poucas oportunidades ou referência incerta deixam a recorrência inconclusiva. Não impor tempo universal nem inventar economia. Notas manuais bastam, sem telemetria ou novo sistema de analytics.

Antes de contratar uma capacidade de M4, identificar a limitação observada e a evidência que permitirá saber se o incremento a resolveu.

---

# 37. Backlog pós-validação

Somente depois do Learning Record considerar:

- semantic retrieval;
- embeddings locais;
- SQLite derivado;
- relation suggestions;
- duplicate detection;
- context assembly;
- additional adapters;
- automated intake;
- IDE integration;
- file watchers;
- UI;
- sync;
- richer evidence model;
- runtime memory;
- interoperabilidade externa.

Prioridade futura deve vir dos problemas observados.

---

# 38. Integração com Radiant

O AIKM é simultaneamente:

- um projeto sendo conduzido pelo Radiant;
- uma futura infraestrutura de memória operacional para o próprio Radiant.

Fluxo desejado:

```text
Radiant Project
    ↓
Build / Verify
    ↓
Knowledge / Procedure / Finding
    ↓
AIKM
    ↓
Future Radiant Project
    ↓
Retrieve / Reuse
```

Não automatizar a integração completa neste ciclo.

Primeiro provar o fluxo manual e explícito.

O procedimento de desenvolvimento já é utilizável por leitura da skill indicada em [WORKFLOW.md](WORKFLOW.md). Ele orienta planejar, executar e verificar/aprender antes de existir suporte do AIKM para skills. Cada ciclo relevante registra versão do procedimento e evidência no local autorizado, sem duplicar seu corpo.

---

# 39. O que este ciclo valida sobre Radiant

Além do AIKM, observar se:

```text
Frame
  ↓
Challenge
  ↓
Spec
  ↓
Plan
  ↓
Contract
  ↓
Build
  ↓
Verify
  ↓
Learn Back
```

produziu:

- melhor enquadramento;
- menos expansão de escopo;
- decisões mais rastreáveis;
- agentes com fronteiras melhores;
- verificação independente;
- aprendizado incorporado.

Se Frame, Spec, Plan e Contracts não influenciarem o Build:

> o Radiant também precisa de Learn Back.

Na próxima entrega, verificar se o agente iniciou pelo mapa/skill, selecionou o contrato correto, executou as verificações aplicáveis e registrou um finding material quando existente. Distinguir revisão própria, verificador determinístico e revisão independente; registrar intervenções necessárias do usuário. A preparação do workflow não prova ainda sua eficácia em uma entrega completa ou em outro produto.

---

# 40. Próximo passo operacional

Com Project Frame v0.2.1, Implementation Spec v0.3.1 e este Implementation Plan v0.3.1, a documentação ampla necessária para o próximo incremento está suficiente. Iniciar pelo [mapa operacional](WORKFLOW.md) e aplicar o modo planejar da skill à proposta de contrato antes de sua ativação.

O bootstrap foi entregue sob TC-0001 v0.2. A próxima proposta é [TC-0002 - Captura e busca local](contracts/TC-0002-capture-search.md), que delimita a parcela técnica de M1: workspace, entrada textual segura, validação e busca. Sua aprovação para execução deve anteceder a atualização de ACTIVE.md; a proposta não autoriza iniciar implementação por si só.

Depois da entrega técnica, observar reutilização em uma necessidade real dentro do escopo autorizado. A integração protegida de M2 recebe contrato próprio, usando as evidências de M1.

Além da preparação operacional explicitamente solicitada, não criar novos documentos abrangentes antes da execução. Procedimentos reutilizáveis ficam na skill e contexto de uso no mapa; não produzir manuais paralelos do mesmo processo.

Novos documentos surgem apenas quando uma decisão concreta exigir:

- ADR;
- Task Contract;
- Verification Report;
- Learning Record.

---

# 41. Síntese do plano

O ciclo atualizado fica:

> **Bootstrap verificado → Captura e busca local → Primeira reutilização real verificada → Adapter mínimo protegido → Uso recorrente e comparação → Expansão por evidência**

A direção permanece:

> **Não estamos construindo uma plataforma completa de knowledge management. Estamos construindo o menor sistema capaz de provar que conhecimento operacional pode atravessar projetos e que o aprendizado produzido por uma execução pode melhorar a próxima.**

O primeiro sinal de sucesso não será a quantidade de records.

Será:

> **Projeto B começar melhor porque o Projeto A existiu.**

E o segundo:

> **o próximo ciclo começar melhor porque o AIKM aprendeu com o Projeto B.**

---
version: "0.2.1"
status: Primeiro experimento Radiant — revisão após pesquisa externa
projeto: AI Knowledge Manager
acronimo_interno: AIKM
enquadramento: fael.tech
sistema_de_desenvolvimento: Radiant — Project Generation System v0.2
natureza: Infraestrutura pessoal local-first de conhecimento operacional para humanos e agentes
---

# Radiant Project Frame — AI Knowledge Manager (AIKM)

## 1. Intenção

Construir uma infraestrutura pessoal capaz de preservar, organizar, recuperar e evoluir o know-how acumulado sobre como trabalhar com inteligência artificial entre diferentes projetos, ferramentas e agentes.

O AIKM não deve ser apenas um repositório de prompts, skills ou agentes.

Também não deve ser apenas uma interface de busca sobre arquivos.

A intenção é criar uma camada de continuidade operacional em que diferentes formas de conhecimento possam permanecer úteis ao longo do tempo:

- fontes;
- conhecimento sintetizado;
- contexto;
- procedimentos;
- memória operacional;
- decisões;
- execuções relevantes;
- avaliações;
- falhas;
- aprendizados.

A pergunta central permanece:

> **Como evitar reconstruir conhecimento de IA que já foi produzido, testado e utilizado anteriormente?**

E ganha uma segunda dimensão:

> **Como fazer com que o resultado de uma execução melhore a qualidade das próximas?**

## 2. Problema

O trabalho contínuo com IA produz um repertório crescente de:

- prompts;
- contexts;
- skills;
- agents;
- workflows;
- harnesses;
- configurações;
- fontes;
- referências;
- decisões;
- procedimentos;
- integrações;
- experiências;
- critérios de avaliação;
- padrões de falha;
- práticas de segurança;
- aprendizados.

Hoje, esse repertório tende a ficar fragmentado entre:

- projetos;
- repositórios;
- chats;
- arquivos locais;
- IDEs;
- coding agents;
- serviços de IA;
- memórias nativas de ferramentas;
- documentação isolada.

Como consequência:

- soluções semelhantes são recriadas;
- conhecimento útil fica preso ao projeto em que nasceu;
- diferentes agentes mantêm cópias divergentes da mesma regra;
- fontes se misturam com sínteses;
- contexto se perde;
- decisões deixam de ter proveniência;
- execuções produzem experiência que não retorna ao sistema;
- erros recorrentes voltam a acontecer;
- conhecimento gerado por IA pode ganhar autoridade sem revisão;
- memória operacional se transforma em depósito de conteúdo;
- informações locais podem ser enviadas a serviços externos sem uma política explícita.

## 3. Transformação desejada

> **Sair de um repertório de IA fragmentado entre ferramentas e projetos para uma infraestrutura local de conhecimento operacional em que humanos e agentes conseguem encontrar, compreender, executar, verificar e evoluir o que já foi aprendido.**

A mudança desejada não é apenas:

> “encontrar aquele prompt antigo”.

É sair de:

> “onde está aquilo que fiz?”

para:

> **“o que já sabemos sobre este problema, qual contexto se aplica, como costumamos resolvê-lo, o que já falhou e o que devo reutilizar agora?”**

## 4. Participante estrutural

O primeiro participante continua sendo uma única pessoa trabalhando continuamente com IA em diferentes projetos.

O AIKM precisa gerar valor integral nesse cenário.

Colaboração, equipes, compartilhamento público e comunidade não fazem parte da hipótese central atual.

Essa restrição permanece intencional.

O projeto continua pertencendo à **fael.tech** e não deve receber uma camada coletiva artificial apenas para se aproximar da Longward.

## 5. Hipótese central

> **Se conhecimento operacional de IA for preservado em uma estrutura local, legível, classificável, recuperável e independente de ferramentas específicas, então conhecimento produzido em um projeto poderá melhorar decisões e execuções posteriores sem precisar ser reconstruído.**

A hipótese agora possui três níveis:

### Continuidade

Conhecimento não desaparece entre projetos.

### Operabilidade

O sistema distingue o que precisa ser conhecido, aplicado, carregado ou verificado.

### Aprendizado

Resultados e falhas podem corrigir o conhecimento, contexto, procedimento ou regra que influenciará o próximo ciclo.

## 6. Desafio Radiant

A revisão reforça que o projeto não deve começar assumindo um aplicativo completo.

A pergunta de Challenge passa a ser:

> **Qual é a menor infraestrutura de conhecimento capaz de melhorar uma execução futura sem criar outro silo ou uma nova burocracia de catalogação?**

Questões que devem permanecer sob pressão:

- Precisamos de um gerenciador de artefatos ou de um sistema de conhecimento operacional?
- Quais informações realmente precisam ser armazenadas?
- O que pode permanecer apenas como referência?
- O que merece virar conhecimento reutilizável?
- O que precisa ser procedimento?
- O que deve ser carregado por um agente em toda sessão?
- O que deve permanecer como evidência de execução?
- O que não merece ser armazenado?
- A captura está custando mais do que o valor da reutilização?
- Estamos duplicando conhecimento entre AIKM e memórias nativas de agentes?
- Precisamos de um banco de dados já na primeira versão?
- O sistema continua útil sem IA?
- Um agente consegue utilizá-lo sem conhecer uma aplicação proprietária?

## 7. Insight estrutural: formato não é papel

A primeira versão do Project Frame tratava `prompt`, `context`, `skill` e `agent` como as principais unidades do sistema.

A revisão mostra que isso é insuficiente.

Um artefato possui pelo menos dois eixos independentes.

### Artifact Kind

O formato ou tipo técnico do recurso.

Exemplos:

- prompt;
- context bundle;
- skill;
- agent;
- workflow;
- checklist;
- reference;
- configuration;
- document.

### Knowledge Role

O papel que aquele conteúdo exerce no sistema.

Exemplos:

- source;
- knowledge;
- context;
- operational-memory;
- procedure;
- action;
- evaluation;
- output.

Exemplo:

> Uma `skill` pode ter `artifactKind: skill` e `knowledgeRole: procedure`.

Essa separação evita transformar a taxonomia atual de ferramentas de IA na arquitetura fundamental do produto.

## 8. Papéis de conhecimento

O AIKM deve explorar uma separação conceitual entre diferentes formas de conhecimento.

### Source

Original externo ou material bruto cuja origem precisa ser preservada.

### Knowledge

Conhecimento sintetizado e reutilizável.

### Context

Informação verdadeira para determinada pessoa, projeto, domínio ou situação.

### Operational Memory

Ponteiros curtos e estáveis que precisam estar disponíveis antes de agir.

### Procedure

Como executar algo repetível.

Pode assumir formas como:

- skill;
- workflow;
- checklist;
- playbook.

### Action / Execution Evidence

Registros seletivos de decisões ou execuções importantes para:

- reprodução;
- verificação;
- handoff;
- diagnóstico.

### Evaluation

Falhas recorrentes, critérios, verificações, rubricas e auditorias.

### Output

Artefatos produzidos para consumo externo ou entrega.

Esses papéis ainda são hipóteses de modelagem.

O experimento deve testar se essa separação realmente melhora recuperação e execução.

## 9. Regra contra armazenamento indiscriminado

O AIKM não deve tentar registrar tudo.

Mais informação armazenada pode reduzir, em vez de aumentar, a qualidade da recuperação.

A pergunta deve ser:

> **Isso muda uma futura decisão, recuperação, execução, verificação ou capacidade de reutilização?**

Se não, provavelmente não precisa permanecer.

Especialmente:

- logs triviais;
- outputs intermediários descartáveis;
- histórico sem valor de reprodução;
- duplicações;
- cópias de conhecimento já canônico.

devem poder ser descartados.

## 10. Intake antes de classificação definitiva

A captura não deve exigir que o usuário saiba imediatamente onde cada informação pertence.

A primeira versão deve explorar:

> **capturar → classificar → promover**

Um item novo pode entrar em uma área de intake temporária.

Depois, uma regra ou processo de routing decide se ele deve se tornar:

- source;
- knowledge;
- context;
- memory;
- procedure;
- action;
- evaluation;
- output;
- ou ser descartado.

Isso reduz o custo de captura sem transformar o inbox em armazenamento permanente.

## 11. Router

O AIKM precisa de um mecanismo explícito de classificação.

O Router deve responder perguntas como:

- É um original que precisamos preservar?
- É conhecimento reutilizável?
- É contexto específico?
- É uma regra curta necessária antes de agir?
- É um procedimento repetível?
- É evidência de uma execução?
- É uma falha ou critério de qualidade?
- É um output?
- Não merece ser armazenado?

O Router não precisa ser inicialmente inteligente.

Pode começar como:

- convenção;
- checklist;
- árvore de decisão;
- skill.

A automação só deve vir depois que o modelo provar utilidade.

## 12. Separação entre fonte e síntese

Uma fonte e o conhecimento derivado dela não são a mesma coisa.

O AIKM deve preservar a possibilidade de responder:

- qual era o original;
- qual interpretação foi criada;
- quem ou o que produziu a síntese;
- quando ela foi produzida;
- qual nível de confiança possui;
- se ainda está atual.

Princípio:

> **síntese não deve apagar origem.**

Isso também se aplica a conteúdo gerado por IA.

## 13. Lifecycle e confiança

Conteúdo novo não deve adquirir autoridade automaticamente.

Um lifecycle conceitual inicial:

```text
candidate
    ↓ review / approval
active
    ↓ replacement
superseded
    ↓ end of life
deprecated / archived
```

Outros estados podem surgir no experimento.

Também deve existir alguma forma de representar confiança ou status epistemológico, por exemplo:

- raw;
- unverified;
- reviewed;
- canonical;
- deprecated.

O objetivo não é criar burocracia de aprovação.

É evitar que:

> **gerado = verdadeiro**

ou:

> **recuperado = confiável**

## 14. Memória não é conhecimento

O AIKM deve evitar tratar “memory” como sinônimo de todo o repertório.

Memória operacional deve conter apenas aquilo que precisa ser conhecido rapidamente antes de agir.

O conhecimento completo continua em sua fonte canônica.

Princípio:

> **memory contains pointers; knowledge contains bodies.**

Isso reduz contexto carregado desnecessariamente e facilita uso por diferentes agents.

## 15. One body, everywhere else pointers

O AIKM deve favorecer:

> **uma representação canônica; referências nos demais lugares.**

Quando Codex, Claude Code ou outro harness já possui memória própria:

- aquilo que só interessa a esse harness pode permanecer lá;
- conhecimento compartilhado deve permanecer no AIKM;
- a memória nativa deve apontar para o AIKM quando possível.

O projeto deve evitar manter a mesma regra ou skill copiada em vários ambientes.

## 16. Core e adapters

O AIKM deve permanecer independente de harness.

A arquitetura conceitual é:

```text
AIKM Core
    ↓
Knowledge + Routing + Retrieval
    ↓
Adapters
    ↓
Codex / Claude Code / outros agents
```

Um adapter deve ser fino.

Sua função é ensinar um agent a:

- encontrar o AIKM;
- saber o que carregar inicialmente;
- recuperar knowledge/context/procedures;
- encaminhar novo conhecimento para o Router;
- registrar ou encaminhar Learn Back.

Adapters não devem duplicar o core.

## 17. Execução como evidência seletiva

A primeira versão possuía `Experience`, porém faltava uma camada clara entre artefato e aprendizado.

Nem toda execução deve ser registrada.

Entretanto, quando necessário para:

- reprodução;
- verificação;
- diagnóstico;
- handoff;
- origem de um aprendizado;

o AIKM deve conseguir preservar um **Execution Record** ou equivalente.

Esse registro permite responder:

> **Em qual execução aprendemos isso?**

E torna `Experience` sustentada por evidência em vez de uma nota isolada.

## 18. Experience

`Experience` continua sendo parte central do projeto.

Representa um aprendizado explícito derivado do uso.

Exemplos:

- “esta skill funciona melhor quando o contexto de arquitetura é separado”;
- “este workflow falha quando não há testes automatizados”;
- “esta abordagem reduziu retrabalho em projetos desse tipo”.

Agora, uma Experience deve poder apontar para:

- projeto;
- artefato;
- execução;
- decisão;
- evidência.

Ela também deve poder ser:

- revisada;
- substituída;
- promovida a procedimento;
- transformada em memória operacional;
- arquivada.

## 19. Learn Back

O AIKM não deve apenas armazenar Experience.

Ele deve ajudar a fechar o ciclo de aprendizado do Radiant.

Fluxo conceitual:

```text
Execute
  ↓
Verify
  ↓
Finding
  ↓
Experience / Evaluation
  ↓
Fix Target
  ↓
Knowledge / Context / Procedure / Memory
```

Exemplos:

- conhecimento estava errado → corrigir knowledge;
- contexto estava incompleto → corrigir context;
- procedimento produziu erro → corrigir procedure;
- erro recorrente deve ser lembrado sempre → criar pointer em memory;
- critério de qualidade estava ausente → criar evaluation/rubric.

O AIKM deve preservar esse vínculo entre descoberta e correção.

## 20. Recuperação

A primeira versão de recuperação precisa responder:

> **O que do meu repertório parece útil para esta necessidade?**

Porém os resultados não devem ser tratados todos da mesma forma.

O sistema deve poder considerar:

- papel do conhecimento;
- projeto;
- origem;
- confiança;
- status;
- uso anterior;
- relações;
- experiências;
- procedimentos;
- avaliação.

Uma fonte bruta e uma procedure canônica podem ambas corresponder a uma query, porém possuem funções diferentes.

## 21. Retrieval não é verificação

Encontrar algo não significa que aquilo sustenta uma decisão.

O projeto deve preservar conceitualmente a diferença entre:

- candidato recuperado;
- conteúdo realmente lido;
- evidência utilizada;
- conclusão sustentada;
- conteúdo em conflito;
- conteúdo desatualizado.

Essa distinção pode permanecer leve no primeiro experimento.

Ela deve, porém, orientar a arquitetura futura.

## 22. Visibilidade e egress

O sistema precisa separar duas perguntas:

### Posso utilizar isso localmente?

e:

### Posso enviar isso para um provider externo?

As respostas podem ser diferentes.

Uma classificação conceitual futura pode incluir:

- public;
- non-sensitive;
- private;
- restricted.

E uma política separada:

```text
egress_allowed: true | false
```

Princípio:

> **visibilidade não implica permissão de egress.**

Isso é estrutural para um produto cujo propósito é centralizar contexto de IA.

## 23. Secrets

Secrets nunca devem entrar como conhecimento comum.

Não armazenar diretamente:

- API keys;
- access tokens;
- passwords;
- private keys;
- cookies;
- session tokens.

Armazenar apenas quando necessário:

- nome;
- função;
- localização segura;
- referência para o mecanismo que realmente guarda o segredo.

## 24. Representação canônica

O filesystem continua sendo a principal hipótese para a fonte de verdade.

Princípio:

> **O patrimônio deve continuar compreensível mesmo sem o AIKM.**

Os formatos devem favorecer:

- Markdown;
- frontmatter;
- YAML/JSON quando necessário;
- arquivos nativos;
- links;
- diretórios compreensíveis;
- Git quando útil.

Índices devem ser derivados.

## 25. Reavaliação de SQLite

A pesquisa externa reforça uma hipótese mais simples.

O AIKM talvez não precise de SQLite para seu primeiro experimento.

Portanto:

> **SQLite deixa de ser uma premissa da v0.1 e passa a ser uma opção de índice derivado quando o volume ou as consultas justificarem.**

O experimento deve primeiro verificar se:

- filesystem;
- metadata;
- links;
- busca textual simples;
- convenções de routing;

já são suficientes para produzir valor.

Se não forem, um índice estruturado pode ser introduzido.

## 26. Reavaliação de versionamento

Também não devemos exigir uma árvore explícita de versões para todo conteúdo desde o início.

O primeiro experimento pode aproveitar:

- Git;
- metadata de origem;
- timestamps;
- lifecycle;
- relações `supersedes` / `replaces`;

antes de criar uma infraestrutura própria de `versions/001`.

Versionamento explícito deve ser obrigatório apenas onde o uso demonstrar necessidade semântica real.

## 27. Menor experimento relevante

O primeiro experimento continua local e sem interface gráfica.

O caso de uso priorizado pelo responsável pelo projeto em 2026-09-15 é reaproveitar o workflow de desenvolvimento entre produtos digitais, como o AIKM, uma rede social de receitas e sites pessoais ou da Longward. A hipótese e o participante permanecem os mesmos; o Projeto B concreto será escolhido a partir de uma necessidade real autorizada.

Reutilizar significa recuperar procedimentos aplicáveis, adaptar o contexto do produto e aproveitar correções anteriores. O processo compartilhado, os procedimentos especializados e o contexto de cada produto permanecem distinguíveis. Um site e uma rede social não precisam executar todas as atividades com o mesmo peso.

Ele deve permitir:

1. criar um workspace legível;
2. capturar um item novo em intake;
3. classificá-lo por `knowledgeRole`;
4. preservar sua origem;
5. registrar pelo menos um artefato técnico reutilizável;
6. relacioná-lo a um projeto;
7. registrar uma execução relevante quando necessário;
8. registrar um aprendizado;
9. recuperar conhecimento ao iniciar outro projeto;
10. reutilizar esse conhecimento;
11. registrar o evento de reutilização;
12. executar Learn Back quando a reutilização produzir uma nova descoberta.

Não é necessário que todas essas operações possuam uma CLI sofisticada na primeira prova.

O importante é validar o ciclo.

## 28. Fluxo experimental

### Projeto A

```text
Work
  ↓
Capture
  ↓
Classify
  ↓
Store
  ↓
Execute
  ↓
Verify
  ↓
Learn
```

### Projeto B

```text
Need
  ↓
Retrieve
  ↓
Inspect
  ↓
Reuse
  ↓
Execute
  ↓
Verify
  ↓
Learn Back
```

O experimento é bem-sucedido quando o Projeto B começa em uma posição melhor por causa do Projeto A.

## 29. Evidência mínima de sucesso

A evidência mínima continua sendo:

> **Um conhecimento produzido ou consolidado no Projeto A é recuperado no Projeto B e utilizado de forma relevante sem precisar ser reconstruído.**

A revisão adiciona uma evidência secundária desejável:

> **O uso no Projeto B gera um novo aprendizado que corrige ou melhora uma camada do AIKM para futuras execuções.**

A primeira prova valida continuidade.

A segunda começa a validar aprendizado operacional.

## 30. Métrica principal

### Knowledge Reuse Event

Um evento em que conhecimento anterior é reutilizado de forma útil em um novo projeto.

## 31. Métricas secundárias

### Reconstruction Avoided

O usuário teria reconstruído aquilo sem o AIKM?

### Retrieval Usefulness

O resultado recuperado realmente alterou a execução?

### Capture Cost

Quanto esforço foi necessário para preservar o conhecimento?

### Learn Back Event

Uma descoberta ou falha gerou uma alteração explícita em knowledge, context, procedure, memory ou evaluation?

### Duplication Avoided

Um agent reutilizou uma fonte canônica em vez de manter outra cópia?

### Provenance Recovery

Conseguimos encontrar a origem de um conhecimento reutilizado?

## 32. Interfaces iniciais possíveis

A CLI continua sendo uma possibilidade forte, porém deixa de ser o próprio experimento.

O primeiro produto pode combinar:

- filesystem;
- convenções;
- Markdown;
- scripts;
- CLI;
- skills;
- adapters.

O critério de escolha é:

> **qual é a menor interface que permite provar continuidade e Learn Back?**

Uma futura CLI pode usar o nome:

```text
aikm
```

evitando o acrônimo `akm`, já utilizado por outro projeto semanticamente próximo.

## 33. Não objetivos

A primeira versão não precisa construir:

- aplicação web;
- aplicação desktop;
- SaaS;
- cloud obrigatório;
- sync multi-device;
- colaboração em tempo real;
- equipes;
- marketplace;
- graph database;
- vector database;
- embeddings obrigatórios;
- memória automática irrestrita;
- execução universal de agentes;
- chat genérico com o repertório;
- integração profunda com dezenas de providers;
- sistema completo de reputação;
- protocolo público.

Também não precisa reproduzir integralmente sistemas externos de knowledge management.

## 34. Riscos principais

### Criar outro silo

Se o repertório só puder ser utilizado através do AIKM, o projeto falha em sua própria tese.

### Criar burocracia de classificação

O Router deve reduzir ambiguidade sem aumentar demais o custo da captura.

### Armazenar demais

Um sistema cheio de logs e outputs triviais pode tornar a recuperação pior.

### Confundir memória com conhecimento

Carregar tudo sempre aumenta custo e ruído.

### Confundir retrieval com verdade

Conteúdo recuperado pode estar errado, antigo ou fora de contexto.

### Duplicação entre harnesses

Memórias nativas não devem virar cópias independentes do AIKM.

### Learn Back passivo

Registrar retrospectivas sem corrigir uma camada responsável não representa aprendizado operacional.

### Modelar cedo demais

A taxonomia não pode ficar presa aos formatos atuais de agentes e skills.

### Segurança de egress

Centralizar conhecimento aumenta o impacto de enviar contexto inadequadamente a providers externos.

## 35. Restrições de projeto

O AIKM deve buscar ser:

- local-first;
- human-readable;
- portable-by-design;
- model-agnostic;
- harness-agnostic;
- source-aware;
- provenance-aware;
- security-aware;
- reconstruível;
- utilizável sem IA;
- compatível com Git;
- fácil de integrar por adapters;
- simples o suficiente para uso cotidiano.

## 36. Relação com Radiant

AIKM é o primeiro produto construído pelo Radiant e, ao mesmo tempo, uma futura infraestrutura para ele.

A relação desejada é:

```text
Radiant Project
    ↓
produces
    ↓
Knowledge / Context / Procedure / Evidence / Learning
    ↓
AIKM
    ↓
retrieve
    ↓
Future Radiant Project
```

O AIKM não deve incorporar a lógica completa de geração de projetos.

Radiant não deve possuir sua própria base duplicada de conhecimento.

A fronteira é:

> **Radiant coordena o trabalho. AIKM preserva o que o trabalho ensina.**

Skills usadas para desenvolver o AIKM podem existir antes de o produto conseguir gerenciá-las. Seu uso direto em arquivos valida o procedimento Radiant; a utilidade do AIKM exige demonstrar que sua captura/recuperação melhora uma execução real. Registrar esses resultados separadamente, sem atribuir ao produto um reaproveitamento que aconteceu somente por leitura manual.

## 37. Duplo experimento

Este projeto testa duas hipóteses simultaneamente.

### Hipótese de produto

> **Uma infraestrutura local de conhecimento operacional reduz reconstrução e melhora reutilização entre projetos?**

### Hipótese de processo

> **O Radiant consegue transformar intenção em experimento, execução verificável e Learn Back sem criar documentação desconectada do trabalho?**

Os dois resultados precisam ser registrados separadamente.

## 38. Questões em aberto

- Qual é a menor estrutura de folders que torna os papéis de conhecimento compreensíveis?
- O sistema deve usar folders como papel semântico, frontmatter, ou ambos?
- Um inbox temporário melhora captura ou apenas adia classificação?
- Quais `knowledgeRoles` são realmente necessários na primeira versão?
- `operational-memory` precisa ser uma camada própria ou pode ser uma view?
- Qual diferença prática deve existir entre `knowledge` e `context`?
- Quando uma Experience vira Procedure?
- Quando uma falha merece virar Evaluation?
- Qual execução merece ser persistida?
- Como um adapter deve descobrir e carregar conhecimento?
- Quais informações específicas pertencem à memória nativa de cada harness?
- Como representar provenance sem burocracia?
- Precisamos de SQLite antes do primeiro Reuse Event?
- Git é suficiente para versionamento inicial?
- Como representar trust/lifecycle sem exigir revisão manual excessiva?
- Qual política mínima de visibility/egress deve existir desde o início?
- Como medir Learn Back sem transformar o sistema em um tracker de processos?
- Quais aprendizados do projeto DECK6/akm são princípios gerais e quais são específicos ao problema que ele resolve?

## 39. Próximo artefato

Este Project Frame atualizado deve alimentar:

# Implementation Spec - AI Knowledge Manager (AIKM)

A [Spec vigente](SPEC.md) deve manter coerência especialmente com:

- modelo `artifactKind × knowledgeRole`;
- intake;
- Router;
- fonte vs síntese;
- lifecycle e trust;
- execution evidence;
- Experience;
- Learn Back;
- adapters;
- one body / pointers;
- retrieval;
- egress;
- secrets;
- persistência canônica;
- necessidade real de SQLite;
- estratégia de versionamento;
- critérios do experimento A → B.

A spec deve continuar orientada por simplicidade.

## 40. Síntese

> **AIKM é uma infraestrutura pessoal local-first de conhecimento operacional para humanos e agentes. Ela preserva fontes, conhecimento, contexto, procedimentos, evidência de execução e aprendizado de forma legível e portável, permitindo que conhecimento produzido em um projeto melhore o trabalho realizado nos projetos seguintes.**

O primeiro experimento não precisa provar que construímos um knowledge management system completo.

Precisa responder duas perguntas:

> **Ao começar um novo projeto, o AIKM me ajuda concretamente a reutilizar algo que eu provavelmente teria reconstruído?**

e:

> **Quando uma execução ensina algo novo, conseguimos fazer esse aprendizado melhorar o sistema para a próxima vez?**

Até que essas duas perguntas tenham evidência, tudo que não contribui para respondê-las é secundário.

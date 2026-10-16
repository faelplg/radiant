---
versão: 0.2
status: Tese operacional revisada
natureza: Sistema interno de geração, desenvolvimento, verificação e aprendizado de projetos
contexto: fael.tech / Longward
codename: Radiant
---

# Radiant — Project Generation System

## 1. Definição

**Radiant é o sistema de geração e desenvolvimento de projetos utilizado para transformar intenção em sistemas reais, verificáveis e capazes de aumentar a capacidade dos ciclos seguintes.**

Radiant não é um produto final.

Radiant não é um único agente.

Radiant não é apenas uma metodologia de documentação.

Radiant é uma camada operacional que organiza como uma intenção é:

- questionada;
- enquadrada;
- especificada;
- planejada;
- delegada;
- construída;
- verificada;
- transformada em aprendizado;
- reincorporada ao próprio sistema.

Sua pergunta principal é:

> **Como transformamos uma intenção em um sistema real sem perder clareza, contexto, evidência e aprendizado no caminho?**

---

## 2. Papel no ecossistema

Radiant possui uma função distinta de fael.tech, Longward e Foundation.

### fael.tech

Pergunta:

> **O que vale a pena explorar, construir ou aprender?**

É o laboratório pessoal onde ideias podem nascer, ser investigadas e transformadas em experimentos.

### Longward

Pergunta:

> **O que merece se tornar uma infraestrutura de continuidade coletiva?**

É a organização institucional orientada por Collective Continuity.

### Foundation

Pergunta:

> **A Longward deveria existir para construir algo como isso?**

É o sistema de validação institucional da Longward.

### Radiant

Pergunta:

> **Como levamos esta intenção até uma implementação verificável e fazemos o sistema aprender com o resultado?**

Radiant não decide o destino institucional de uma ideia.

Ele recebe uma intenção suficientemente clara e conduz sua materialização.

---

## 3. O problema que Radiant resolve

A capacidade de produzir software com inteligência artificial cresce rapidamente.

Isso reduz o custo de:

- escrever código;
- gerar documentos;
- pesquisar alternativas;
- criar testes;
- produzir protótipos;
- executar tarefas repetitivas;
- coordenar múltiplos agentes.

Ao mesmo tempo, cria novos riscos:

- construir antes de entender;
- aceitar a primeira solução plausível;
- transformar prompts temporários em processo permanente;
- gerar código sem uma hipótese clara;
- produzir documentação desconectada da implementação;
- perder contexto entre agentes, ferramentas e sessões;
- repetir decisões já tomadas;
- validar o próprio trabalho sem crítica independente;
- registrar aprendizados sem corrigir o sistema que falhou;
- confundir memória com conhecimento;
- confundir execução com evidência;
- duplicar regras em diferentes agentes;
- depender excessivamente de um único modelo, IDE ou fornecedor.

Radiant parte de uma hipótese diferente:

> **A principal vantagem de um sistema agêntico de desenvolvimento não é gerar mais código. É reduzir incerteza de forma disciplinada e aumentar capacidade entre ciclos.**

---

## 4. Tese central

A tese do Radiant é:

> **Projetos melhores emergem quando intenção, especificação, execução, verificação e Learn Back fazem parte de um mesmo sistema contínuo.**

Radiant não busca automatizar tudo.

Busca organizar conscientemente:

- o que precisa ser entendido;
- o que precisa ser questionado;
- o que precisa ser especificado;
- o que pode ser delegado;
- o que precisa ser verificado;
- qual evidência sustenta uma conclusão;
- onde um erro precisa ser corrigido;
- o que deve permanecer disponível para o próximo projeto.

O resultado esperado de um ciclo não é apenas software.

É:

> **sistema entregue + evidência + aprendizado incorporado + capacidade acumulada.**

---

## 5. Intenção antes de geração

Radiant não começa por código.

Começa por intenção.

Antes de construir, o sistema precisa conseguir responder:

- O que estamos tentando mudar?
- Para quem?
- Qual problema ou oportunidade existe?
- Qual é a hipótese central?
- Qual é o menor fenômeno que precisamos provar?
- O que não precisamos construir ainda?
- O que faria esta hipótese estar errada?

Uma ideia mal enquadrada continua sendo mal enquadrada mesmo quando implementada rapidamente.

Por isso:

> **velocidade de geração não substitui clareza de intenção.**

---

## 6. O ciclo Radiant

O ciclo operacional inicial do Radiant é:

> **Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify → Learn Back**

Cada estágio reduz um tipo diferente de incerteza.

---

### 6.1. Frame

Transforma uma intenção ampla em um contrato inicial de entendimento.

Artefato principal:

**Radiant Project Frame**

Deve registrar:

- intenção;
- problema;
- transformação desejada;
- participante ou usuário;
- hipótese central;
- restrições;
- hipóteses críticas;
- menor experimento relevante;
- evidência mínima de sucesso;
- não objetivos;
- questões em aberto.

---

### 6.2. Challenge

Questiona premissas antes que elas se transformem em arquitetura.

Perguntas típicas:

- Precisamos mesmo de um produto?
- Precisamos mesmo desta interface?
- Existe uma solução menor?
- Estamos resolvendo o problema ou implementando a primeira forma imaginada?
- Qual premissa pode invalidar boa parte do projeto?
- O que estamos adicionando apenas porque a tecnologia permite?

Radiant pode implementar esta função através de uma skill ou agente chamado provisoriamente de **Grill**.

Seu objetivo não é bloquear.

É impedir que velocidade seja confundida com convicção.

---

### 6.3. Spec

Descreve o comportamento esperado antes de decidir todos os detalhes de implementação.

Pode produzir:

- Implementation Spec;
- Domain Spec;
- Workspace Spec;
- Interface Contract;
- invariantes;
- estados;
- eventos;
- acceptance criteria;
- requisitos não funcionais;
- limites de segurança.

A especificação funciona como contrato intermediário entre intenção e código.

---

### 6.4. Design

Define como o sistema será estruturado e como a experiência será percebida, compreendida e usada.

Radiant reconhece duas trilhas conceitualmente distintas, que podem coexistir no mesmo projeto:

#### 6.4.1. System Design

Relaciona-se à estrutura interna do sistema:

- arquitetura;
- modelo de domínio;
- componentes;
- contratos;
- persistência;
- integrações;
- decisões técnicas;
- trade-offs;
- ADRs.

#### 6.4.2. Experience Design

Relaciona-se à forma como pessoas percebem, entendem e usam o sistema:

- intenção da experiência;
- arquitetura de informação;
- jornadas e fluxos;
- estados e interações;
- responsividade;
- acessibilidade;
- expressão visual;
- comportamento e feedback;
- coerência entre intenção e implementação.

A Design Layer do Radiant formaliza essa separação sem criar um processo paralelo. A etapa Design deve preservar a diferença entre estrutura do sistema e experiência do usuário. O corpo canônico especializado está em [Radiant Design Layer](design-layer.md).

Radiant deve favorecer decisões reversíveis enquanto a incerteza for alta e manter a formalidade proporcional ao risco.

---

### 6.5. Plan

Transforma a spec em incrementos executáveis.

Artefato principal:

**Implementation Plan**

Um bom plano não é uma lista extensa de tarefas.

É uma sequência de incrementos capazes de:

- reduzir risco;
- produzir comportamento observável;
- gerar evidência;
- permitir interrupção antecipada quando a hipótese se mostra fraca.

---

### 6.6. Contract

Antes de delegar trabalho agêntico relevante, Radiant pode gerar um **Task Contract**.

O contrato existe para impedir que agentes interpretem livremente uma intenção ampla.

Um Task Contract deve declarar, proporcionalmente à tarefa:

- identidade da tarefa;
- objetivo;
- inputs;
- outputs exatos;
- caminhos canônicos;
- owner;
- restrições;
- non-goals;
- critérios de conclusão;
- método de verificação;
- condições de HOLD ou FAIL;
- limites de segurança;
- blockers externos;
- limite de execução quando aplicável.

O contrato deve ser pequeno.

Sua função é tornar delegação verificável.

---

### 6.7. Build

Executa os incrementos.

Agentes podem:

- implementar;
- gerar testes;
- refatorar;
- pesquisar APIs;
- atualizar documentação;
- preparar migrações;
- revisar alterações;
- executar checklists.

Construção nunca deve se desconectar de Frame, Spec e Contract.

---

### 6.8. Verify

Radiant trata verificação como etapa própria.

Não como consequência automática do Build.

Pode envolver:

- testes automatizados;
- análise estática;
- acceptance criteria;
- revisão arquitetural;
- execução manual;
- segurança;
- performance;
- acessibilidade;
- readback de artefatos;
- revisão por outro agente;
- avaliação humana;
- comparação entre intenção, spec e implementação.

O princípio é:

> **quem cria não deve ser a única entidade responsável por declarar que está correto.**

---

### 6.9. Learn Back

Radiant não deve apenas registrar aprendizado.

Deve determinar:

> **qual parte do sistema precisa ser corrigida para que a próxima execução seja melhor?**

Exemplos:

- problema de intenção → corrigir Frame;
- premissa mal testada → corrigir Challenge;
- ambiguidade → corrigir Spec;
- decisão arquitetural ruim → corrigir Design ou ADR;
- decomposição inadequada → corrigir Plan;
- instrução insuficiente → corrigir Task Contract ou Skill;
- falha recorrente de execução → corrigir Procedure;
- verificação inadequada → corrigir Verification Rule;
- conhecimento errado ou obsoleto → corrigir Knowledge;
- contexto mal compreendido → corrigir Context;
- regra necessária em toda execução → promover um ponteiro para Operational Memory.

O ciclo só fecha quando o aprendizado altera o sistema responsável.

---

## 7. Learn Back como princípio estrutural

Um sistema que apenas armazena retrospectivas não necessariamente aprende.

Radiant considera aprendizado real quando uma observação produz uma mudança em uma camada responsável.

Fluxo:

> **Outcome → Evidence → Diagnosis → Fix Target → Change → Reuse**

Toda falha relevante deve conseguir responder:

1. O que aconteceu?
2. Qual evidência temos?
3. Por que acreditamos que aconteceu?
4. Qual camada poderia ter evitado isso?
5. O que precisa mudar?
6. Como verificaremos que a mudança funcionou?

Essa lógica evita uma memória passiva de erros.

---

## 8. Radiant Project Frame

O **Radiant Project Frame** é o contrato inicial entre intenção e construção.

Ele não é um PRD completo.

Sua função é impedir que um projeto comece diretamente por features.

Deve ser pequeno o suficiente para ser usado.

E explícito o suficiente para permitir que outra pessoa ou agente compreenda:

- por que o projeto existe;
- o que precisa ser provado;
- o que está deliberadamente fora.

---

## 9. Radiant Constitution

A [Radiant Constitution](../constitution/CONSTITUTION.md) é a fonte normativa
canônica dos princípios operacionais. Esta tese explica o sistema; não mantém
uma segunda lista de regras. Consulte a Constitution para precedência, artigos,
estados operacionais e alterações constitucionais.

### Engenharia como restrição explícita

Radiant não substitui práticas de engenharia pelo uso de agentes. Projetos
podem adotar um [Radiant Engineering Baseline](../engineering/engineering-baseline.md)
com expectativas mínimas e um Engineering Profile com adaptações específicas.
O Baseline não impõe arquitetura ou stack universal; sua aplicação é
proporcional ao risco, impacto e reversibilidade.

Task Contracts referenciam essas regras, Verify produz evidência de conformidade
e Learn Back corrige a camada responsável quando a regra se mostra insuficiente.

## 10. Core e adapters

Radiant deve separar:

```text
Radiant Core
    ↓
Capabilities / Skills
    ↓
Adapters
    ↓
Agent Runtime / Harness
    ↓
Model / Tool
```

### Core

Contém:

- Constitution;
- ciclo;
- artefatos;
- regras de verificação;
- contratos;
- Learn Back;
- convenções de memória;
- princípios de segurança.

### Adapters

Conectam Radiant a ambientes como:

- Codex;
- Claude Code;
- IDE agents;
- CLI agents;
- runtimes locais;
- futuros harnesses.

Adapters não devem duplicar regras do core.

Devem apontar para elas.

---

## 11. One body, everywhere else pointers

Radiant adota a regra:

> **um conteúdo canônico; nos demais sistemas, apenas referências quando possível.**

Exemplo:

- uma skill compartilhada vive no repositório canônico;
- o Codex recebe um ponteiro;
- Claude Code recebe um ponteiro;
- uma memória nativa pode conter apenas a localização e instrução de uso;
- o AIKM preserva origem, versão, uso e aprendizado.

Isso reduz:

- drift;
- duplicação;
- regras conflitantes;
- manutenção repetida.

---

## 12. Skills como unidades de capacidade

Uma **skill** encapsula uma competência reutilizável.

Exemplos:

- `grill-project-hypothesis`
- `write-implementation-spec`
- `model-domain`
- `create-implementation-plan`
- `create-task-contract`
- `review-security`
- `verify-acceptance-criteria`
- `extract-project-learning`
- `route-learn-back`

Uma skill ideal define:

- objetivo;
- entradas;
- contexto necessário;
- processo;
- restrições;
- formato de saída;
- critérios de qualidade;
- método de verificação;
- falhas conhecidas;
- Learn Back target quando relevante.

Skills transformam experiência operacional em infraestrutura.

---

## 13. Grill como mecanismo de pressão

Radiant deve possuir uma capacidade explícita de crítica adversarial.

**Grill** desafia:

- premissas;
- necessidade da solução;
- escopo;
- complexidade;
- arquitetura;
- dependências;
- métricas;
- evidência;
- irreversibilidade.

Grill deve acontecer antes de decisões caras.

Também pode ser reaplicado quando o projeto começa a acumular complexidade não prevista.

---

## 14. Spec-Driven Development

Radiant incorpora Spec-Driven Development como mecanismo, não como identidade completa.

Fluxo:

> **Intent → Spec → Contract → Implementation → Verification → Learn Back**

A spec não é documentação congelada.

Quando a realidade contradiz a especificação, Radiant deve registrar:

- o que mudou;
- por que mudou;
- qual evidência justificou a mudança;
- se Frame, Spec ou Design precisam ser atualizados.

O objetivo é impedir que implementação e intenção se afastem silenciosamente.

---

## 15. Criação e crítica separadas

Sempre que possível, Radiant separa funções de geração e avaliação.

Exemplos:

- um agente implementa e outro revisa;
- um agente escreve a spec e outro busca ambiguidades;
- um agente propõe arquitetura e outro procura riscos;
- um agente produz uma resposta e outro verifica evidência;
- um agente gera testes e outro verifica se os testes cobrem os critérios;
- um agente sintetiza aprendizado e outro identifica a camada correta de Learn Back.

Isso reduz auto-confirmação.

---

## 16. Verificação proporcional ao risco

Nem toda tarefa precisa do mesmo rigor.

Radiant deve selecionar a profundidade de verificação com base em:

- durabilidade;
- reversibilidade;
- exposição externa;
- impacto;
- segurança;
- importância factual.

Um modelo inicial pode utilizar quatro níveis:

### Tier 0 — Quick

Tarefa descartável e de baixo risco.

Verificar apenas o necessário para não reportar algo materialmente incorreto.

### Tier 1 — Durable

Artefato que será reutilizado.

Verificar:

- aderência ao pedido;
- estrutura;
- integridade;
- proveniência;
- legibilidade;
- discoverability.

### Tier 2 — Deep

Arquitetura, pesquisa, proposta, spec importante ou publicação.

Adicionar:

- critérios específicos;
- análise de riscos;
- claims críticos;
- segunda leitura.

### Tier 3 — High Impact

Segurança, produção, dados sensíveis, decisões irreversíveis ou outputs públicos de alta consequência.

Adicionar:

- evidência explícita;
- revisão independente;
- gates de aprovação;
- plano de rollback quando aplicável.

O rigor deve acompanhar o risco, não o tamanho do texto.

---

## 17. Evidência

Radiant deve distinguir:

- algo recuperado;
- algo efetivamente inspecionado;
- algo que sustenta uma conclusão;
- algo em conflito;
- algo desatualizado.

Especialmente em pesquisa e decisão técnica:

> **retrieval não equivale a verificação.**

Uma fonte encontrada não sustenta automaticamente uma decisão.

Radiant pode futuramente estruturar evidence packets, porém essa capacidade deve nascer apenas quando o uso justificar.

---

## 18. Task Contracts

Task Contracts são a unidade operacional entre planejamento e execução agêntica.

Um contrato existe para responder:

> **O agente sabe exatamente o que deve produzir, onde, sob quais limites e como a conclusão será verificada?**

Um bom contrato deve evitar:

- escopo implícito;
- outputs vagos;
- “done” sem readback;
- mudanças não autorizadas;
- expansão silenciosa;
- execução indefinida.

Task Contracts não devem se transformar em um novo PRD.

Devem permanecer bounded.

Além dos limites funcionais, um contrato pode declarar Baseline e Profile,
Engineering Check, política de dependências, comandos de verificação e
condições de HOLD específicas de engenharia. O contrato referencia esses
documentos; não copia seus corpos.

---

## 19. Memória operacional

Radiant precisa acumular:

- decisões;
- padrões;
- falhas;
- experiências;
- soluções;
- trade-offs;
- componentes;
- skills;
- contexts;
- avaliações;
- resultados de experimentos;
- regras de prevenção.

Essa memória deve ser organizada de acordo com sua função.

Nem tudo precisa ser carregado sempre.

Radiant deve distinguir ao menos conceitualmente:

### Knowledge

O que sabemos.

### Context

O que é verdadeiro para um projeto, pessoa ou situação específica.

### Procedure

Como executar algo repetidamente.

### Operational Memory

Ponteiros curtos e estáveis que precisam ser conhecidos antes de agir.

### Action / Execution Evidence

O que aconteceu em uma execução relevante.

### Evaluation

Falhas, critérios e verificações.

Essa separação evita transformar “memória” em um depósito indiferenciado.

---

## 20. Relação com AIKM

> **Nota de estado (2026-10-15):** as menções ao AIKM nas seções 11, 20, 21, 32, 33, 37 e 42 descrevem o AIKM v1, uma camada de preservação e recuperação de conhecimento. Desde a revisão 2 do Frame AIKM (2026-10-12), o AIKM gerencia skills, contexto e servidores MCP por projeto, e essa camada de conhecimento é non-goal. A fronteira vigente está em [integração](integration.md#fronteira-aikm); o texto abaixo permanece como registro da tese 0.2.

O **AI Knowledge Manager**, abreviado internamente como **AIKM**, é a infraestrutura candidata para preservar e recuperar o patrimônio operacional produzido pelo Radiant.

As funções permanecem distintas:

### Radiant

Orquestra como projetos são transformados de intenção em sistema.

### AIKM

Preserva e recupera o conhecimento operacional acumulado ao longo desses projetos.

A relação desejada é:

> **Radiant executa → produz evidência e aprendizado → AIKM preserva → Radiant recupera → próximo ciclo começa com mais capacidade.**

Essa relação não deve criar duplicação.

Radiant é processo.

AIKM é infraestrutura de conhecimento.

---

## 21. Intake e classificação

Radiant deve evitar exigir classificação perfeita no momento da captura.

Uma arquitetura saudável permite:

> **capturar primeiro → classificar depois → promover quando houver evidência suficiente.**

Isso reduz atrito.

Também permite distinguir:

- material bruto;
- conhecimento sintetizado;
- contexto;
- procedimento;
- execução;
- avaliação;
- aprendizado promovido.

O AIKM pode implementar essa função de intake e roteamento.

---

## 22. Conhecimento e lifecycle

Conteúdo produzido por IA não deve se tornar canônico automaticamente.

Um lifecycle conceitual útil é:

```text
candidate
    ↓ explicit review
active / reviewed
    ↓ replacement
superseded
    ↓ end of life
deprecated / archived
```

O estado exato pode variar por tipo de artefato.

O princípio permanece:

> **gerado não significa confiável; recuperado não significa verdadeiro; utilizado não significa canônico.**

---

## 23. Segurança e egress

Radiant deve distinguir:

- possibilidade de leitura local;
- permissão de envio para uma ferramenta externa.

Algo pode ser útil no contexto local e ainda assim não poder sair da máquina.

Portanto:

> **visibility não implica egress permission.**

Especial atenção para:

- secrets;
- código privado;
- dados pessoais;
- dados empresariais;
- credenciais;
- conversas privadas;
- artefatos de clientes;
- documentos internos.

Adapters e agentes precisam respeitar esta fronteira.

---

## 24. Artefatos do Radiant

Radiant deve produzir apenas artefatos que tenham função operacional.

### Radiant Project Frame

Define intenção e experimento.

### Implementation Spec

Define comportamento, regras e critérios.

### Domain / Technical Spec

Aprofunda áreas que exigem precisão.

### Implementation Plan

Organiza incrementos.

### Task Contract

Transforma um incremento em trabalho agêntico delimitado.

### ADR

Registra decisões estruturais.

### Verification Report

Registra o que foi efetivamente verificado.

### Learning Record

Registra resultado, evidência, diagnóstico e Learn Back.

### Engineering Baseline

Define o padrão mínimo de engenharia reutilizável entre projetos.

### Engineering Profile

Contextualiza o Baseline para um projeto sem duplicá-lo.

Nem todo projeto precisa de todos os artefatos.

Formalidade é proporcional a risco e complexidade.

---

## 25. Artefatos como estado do sistema

Os documentos não são apenas relatórios.

Eles são parte do estado operacional do projeto.

Fluxo:

```text
Project Frame
    ↓
Implementation Spec
    ↓
Implementation Plan
    ↓
Task Contracts
    ↓
Build
    ↓
Verification Report
    ↓
Learning Record
    ↓
Learn Back
    ↓
Knowledge / Skill / Context / Rule
```

Cada estágio deve poder apontar para o anterior quando isso aumentar rastreabilidade.

---

## 26. Human-in-the-loop

Radiant não pressupõe autonomia total.

### Pode ser altamente automatizado

- scaffolding;
- geração de testes;
- refatorações locais;
- documentação derivada;
- lint;
- busca;
- tarefas mecânicas;
- execução de checklists;
- validações estruturais.

### Requer participação humana maior

- intenção;
- propósito;
- priorização;
- escolhas econômicas;
- mudanças de escopo;
- decisões éticas;
- dados sensíveis;
- produção;
- trade-offs irreversíveis;
- aprovação de conhecimento canônico.

A função do sistema não é remover o humano.

É ampliar sua capacidade sem eliminar responsabilidade.

---

## 27. Model-agnostic e tool-agnostic

Radiant deve funcionar com diferentes:

- modelos;
- IDEs;
- CLIs;
- coding agents;
- runtimes;
- provedores;
- sistemas de versionamento;
- ferramentas de documentação.

O processo pertence ao Radiant.

A execução pertence ao runtime escolhido.

---

## 28. Segurança e limites de execução

Um sistema agêntico precisa operar dentro de fronteiras explícitas.

Radiant deve considerar:

- permissões mínimas;
- ambientes isolados;
- secrets fora de prompts;
- política de egress;
- revisão de comandos destrutivos;
- acesso restrito a produção;
- limites de rede;
- provenance de mudanças;
- logs seletivos;
- approval gates;
- rollback quando relevante.

Autonomia deve ser proporcional à reversibilidade.

---

## 29. Métricas

Radiant não deve ser avaliado apenas por velocidade.

### Intention-to-Working-System

Tempo entre intenção clara e primeiro sistema funcional.

### Spec Drift

Diferença material entre intenção/spec e implementação.

### Verification Escape Rate

Problemas que deveriam ter sido detectados antes da conclusão.

### Rework Rate

Retrabalho causado por enquadramento ou especificação inadequados.

### Knowledge Reuse Rate

Percentual de projetos que reutilizam conhecimento anterior.

### Learn Back Rate

Percentual de falhas relevantes que geram uma correção explícita na camada responsável.

### Learning Yield

Quantidade e qualidade de conhecimento reutilizável produzido por ciclo.

### Task Contract Compliance

Percentual de execuções que permanecem dentro de outputs e limites acordados.

### Human Intervention Quality

Pontos em que a participação humana altera materialmente a qualidade ou direção.

A métrica principal continua sendo:

> **convergência entre intenção, sistema entregue, evidência e capacidade acumulada.**

---

## 30. O que Radiant não é

> **Nota de estado (2026-10-16):** o Radiant define como fluxos agênticos são divididos em unidades, roteados para harnesses e aceitos. A execução e a observação ficam com os harnesses e com um operador externo, o Demerzel, conforme o [ADR-0002](adrs/ADR-0002-backend-dispatch-demerzel.md) e a [integração](integration.md#fronteira-demerzel). O texto abaixo permanece como registro da tese 0.2.

Radiant não é:

- framework de agentes;
- IDE;
- coding agent;
- coleção de prompts;
- substituto para engenharia;
- gerador automático de startups;
- metodologia rígida;
- sistema de documentação pesada;
- desculpa para automatizar decisões humanas relevantes;
- base de conhecimento isolada.

Radiant é uma camada operacional sobre essas capacidades.

---

## 31. Princípio de proporcionalidade

Projetos pequenos devem gerar pouca burocracia.

Projetos maiores ou mais arriscados devem gerar mais estrutura.

### Pequeno experimento

Pode exigir:

- Project Frame;
- spec curta;
- plan curto;
- Task Contract opcional;
- build;
- verify;
- learning record.

### Produto de maior risco

Pode exigir:

- domain spec;
- threat model;
- ADRs;
- task contracts;
- security review;
- observabilidade;
- rollback strategy;
- evidência mais rigorosa;
- revisão humana adicional.

Radiant aumenta rigor conforme aumenta o custo do erro.

Para pequenos experimentos, o Baseline pode ser aplicado diretamente e o
Profile pode ser omitido. Para produtos com múltiplas iterações, integrações,
dados sensíveis ou risco operacional, o Profile e a evidência de engenharia
passam a ser recomendados.

---

## 32. Primeira implementação do Radiant

A primeira implementação do Radiant não precisa ser uma plataforma.

Pode existir como um repositório com:

```text
radiant/
  constitution/
  templates/
  skills/
  adapters/
  workflows/
  contracts/
  validators/
  projects/
  knowledge/
```

Componentes iniciais recomendados:

1. Radiant Constitution;
2. template de Project Frame;
3. skill de Grill;
4. skill de Implementation Spec;
5. skill de Implementation Plan;
6. template de Task Contract;
7. skill de Verification;
8. skill de Learn Back;
9. adapters iniciais para harnesses usados;
10. integração gradual com AIKM.
11. Radiant Engineering Baseline e template de Profile.

A infraestrutura deve crescer a partir do uso real.

---

## 33. Primeiro teste: AI Knowledge Manager

O primeiro projeto conduzido pelo Radiant é o **AI Knowledge Manager — AIKM**, incubado pela fael.tech.

Esse teste é adequado porque:

- resolve uma dor real;
- possui escopo controlável;
- tem reflexão conceitual prévia;
- pode ser usado pelo próprio Radiant;
- permite observar reutilização entre projetos;
- permite testar core–adapter separation;
- permite testar Learn Back.

O ciclo inicial deve produzir:

### Project Frame

Define intenção e hipótese.

### Implementation Spec

Define o menor sistema necessário.

### Implementation Plan

Divide em incrementos.

### Task Contracts

Delimitam trabalho agêntico relevante.

### Build

Implementa.

### Verify

Confirma comportamento e hipótese.

### Learn Back

Atualiza AIKM e Radiant com o que foi descoberto.

---

## 34. Critério de sucesso do primeiro teste

Radiant não será considerado validado porque gerou código.

O primeiro teste será promissor quando observarmos:

> Uma intenção é enquadrada.  
> Premissas são questionadas.  
> A spec orienta a implementação.  
> O plano reduz o trabalho a incrementos.  
> Agentes recebem contratos delimitados.  
> A implementação é verificada por critérios externos à própria geração.  
> O uso produz evidência real.  
> Uma falha ou descoberta gera Learn Back.  
> Conhecimento produzido é reutilizado em um ciclo posterior.

O ponto decisivo é:

> **o segundo ciclo deve começar melhor por causa do primeiro.**

---

## 35. Evolução do sistema

Radiant deve evoluir através dos próprios projetos.

Uma capacidade só entra no core quando:

- aparece repetidamente;
- possui valor em mais de um projeto;
- pode ser abstraída sem apagar contexto;
- possui método de verificação;
- seu custo operacional é menor que o retrabalho que evita.

Isso pode produzir novas:

- skills;
- validators;
- templates;
- adapters;
- contracts;
- rubrics;
- regras da Constitution.

O sistema deve crescer de dentro para fora.

---

## 36. Relação com publicação

Radiant é um projeto interno.

Não precisa ser apresentado publicamente como produto.

Aprendizados reais podem gerar publicações pela fael.tech sobre:

- agentic development;
- Spec-Driven Development;
- core–adapter architectures;
- human-in-the-loop;
- verification;
- task contracts;
- Learn Back;
- operational memory;
- AI-assisted engineering.

A publicação deve nascer da evidência produzida pelo trabalho.

Não de uma metodologia apresentada como universal antes de ser testada.

---

## 37. Referências operacionais e limites de adoção

Radiant pode aprender com sistemas externos de engenharia agêntica e gestão de conhecimento.

Um exemplo relevante é o projeto **DECK6/akm**, que demonstra práticas como:

- separação entre knowledge, context, procedure, action e evaluation;
- core–adapter separation;
- Learn Back;
- verificação proporcional ao risco;
- task contracts;
- conhecimento canônico separado de índices derivados;
- ponteiros em vez de duplicação;
- lifecycle explícito;
- distinção entre disponibilidade local e egress.

Radiant não deve copiar sua arquitetura integralmente.

O problema do Radiant é diferente:

> **orquestrar a geração de projetos.**

O problema do AIKM é:

> **preservar e recuperar conhecimento operacional.**

Referências externas devem melhorar nossos princípios sem apagar a natureza específica dos nossos sistemas.

---

## 38. Hipótese de longo prazo

Se Radiant funcionar, cada novo projeto deve começar com mais capacidade do que o anterior.

Não apenas porque os modelos melhoraram.

E sim porque o sistema acumulou:

- melhores perguntas;
- melhores specs;
- melhores contracts;
- melhores procedures;
- melhores critérios de verificação;
- melhores padrões;
- melhores contextos;
- melhores mecanismos de recuperação;
- conhecimento sobre falhas anteriores.

Radiant passa a funcionar como uma infraestrutura de aprendizagem para construção de software e produtos.

---

## 39. Missão operacional

> **Transformar intenção em sistemas verificáveis e transformar cada ciclo em capacidade para o próximo.**

---

## 40. Visão

Criar um ambiente em que humanos e agentes consigam desenvolver projetos sem depender de conversas descartáveis, contexto perdido ou geração improvisada.

Um sistema em que:

- intenção permanece visível;
- agentes recebem fronteiras claras;
- especificações orientam construção;
- contratos tornam delegação verificável;
- decisões preservam contexto;
- resultados são avaliados proporcionalmente ao risco;
- erros corrigem a camada responsável;
- aprendizado é preservado;
- novos projetos reutilizam capacidade anterior.

Radiant não deve apenas ajudar a construir mais rápido.

Deve ajudar a:

> **construir com continuidade e aprender operacionalmente.**

---

## 41. Questão fundamental

Toda evolução do Radiant deve responder:

> **Esta capacidade reduz incerteza, melhora verificação, reduz duplicação ou transforma experiência em capacidade reutilizável?**

Se não fizer nenhuma dessas coisas, provavelmente não pertence ao sistema.

---

## 42. Estado atual

Radiant possui uma tese operacional revisada.

O primeiro experimento continua sendo o **AI Knowledge Manager — AIKM**.

O próximo estágio é atualizar os documentos do AIKM para refletir:

- intake e routing;
- separação entre tipo e papel do conhecimento;
- execution evidence;
- Learn Back;
- lifecycle;
- core–adapter separation;
- verificação;
- segurança de egress;
- simplificação do MVP quando possível.

Depois disso:

> **Frame → Spec → Plan → Contract → Build → Verify → Learn Back**

A tese agora pode ser resumida assim:

> **Radiant transforma intenção em construção, construção em evidência e evidência em capacidade acumulada.**

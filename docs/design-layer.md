# Radiant Design Layer v0.1

## Papel

A camada de design do Radiant define como a intenção de um projeto se converte em uma experiência coerente, compreensível e verificável antes de ela se tornar implementação final.

A Design Layer não substitui a tese do Radiant nem cria um processo paralelo. Ela organiza a parte da incerteza que fala sobre estrutura da experiência e sobre como o sistema transmite significado, comportamento e responsabilidade a quem o usa.

Seu papel é responder:

> Como a intenção se torna uma experiência legível, coerente e verificável sem perder a hipótese do projeto?

## Sistema e experiência

A camada de design reconhece duas trilhas conceitualmente distintas:

### System Design

Relaciona-se com a estrutura interna do sistema:

- arquitetura;
- domínio e regras;
- componentes e interfaces;
- dados e contratos;
- integrações;
- trade-offs;
- restrições de implementação;
- ADRs e decisões técnicas.

### Experience Design

Relaciona-se com a forma como pessoas percebem, entendem e usam o sistema:

- intenção da experiência;
- arquitetura de informação;
- jornadas e fluxos;
- estados e interações;
- acessibilidade;
- feedback e clareza;
- expressão visual;
- cooperação entre comportamento e linguagem;
- consistência sem homogeneização artificial.

Essas trilhas se influenciam, mas não são sinônimos. A estrutura do sistema não decide toda a experiência e a experiência não substitui a arquitetura.

## Quando o design é necessário

O design deve ser aplicado com proporcionalidade ao risco, à reversibilidade e à relevância da experiência.

### Projetos sem experiência relevante

Podem usar apenas System Design, com foco em domínio, fluxo de dados, arquitetura e critérios de entrega.

### Pequenos projetos e mudanças reversíveis

Podem usar apenas Design Frame e critérios no Contract, sem um Design Spec detalhado.

### Produtos públicos, fluxos críticos ou experiências complexas

Podem exigir:

- Design Frame;
- Design Spec;
- revisão de acessibilidade;
- prototipagem ou readback de fluxo;
- validação com usuários ou com critérios de uso real.

A exigência procedural deve crescer com a relevância do produto e o custo do erro.

## Relação com o ciclo Radiant

A Design Layer se encaixa no ciclo macro do Radiant:

> Frame → Challenge → Spec → Design → Plan → Contract → Build → Verify → Learn Back

A diferença é que a etapa Design passa a ser explicitamente compreendida como duas trilhas complementares:

- System Design: estrutura e viabilidade do sistema;
- Experience Design: comportamento, legibilidade e resultado percebido.

A Design Layer não substitui a Spec. Ela torna a intenção da experiência operacionalmente legível antes da implementação.

## Artefatos da camada

### Design Frame

Usado para enquadrar a experiência antes de detalhar a solução. Deve responder:

- o que a experiência precisa permitir;
- quem a usa e em qual contexto;
- qual percepção ou relação desejamos produzir;
- quais jornadas e estados são críticos;
- quais restrições existem;
- onde há maior risco de fricção ou confusão;
- quais decisões devem permanecer simples;
- o que ainda não será desenhado.

O Design Frame não é um mockup nem uma lista de telas. É um contrato mínimo de intenção experiencial.

### Design Spec

Usado quando a experiência exige maior precisão. Pode descrever:

- arquitetura de informação;
- navegação e fluxos;
- estados e transições;
- feedback e erros;
- regras de interação;
- padrões de responsividade;
- acessibilidade;
- visual direction;
- indicadores de coerência com o produto;
- critérios de aceitação de experiência.

O Design Spec deve ser implementável e verificável, não uma coleção de screenshots sem semântica.

## Princípios de design

A Design Layer opera com princípios que reduzem incerteza antes da implementação:

- intenção antes da interface;
- estrutura antes de estilo;
- experiência antes de componentes;
- interação como comportamento do sistema;
- acessibilidade como restrição de projeto;
- estados como parte do design;
- consistência sem homogeneização artificial;
- implementação deve preservar intenção;
- design proporcional ao risco.

Esses princípios podem ser herdados por projetos ou organizações sem serem duplicados em cada instância. O Radiant preserva a regra de que há um corpo canônico e os demais ambientes recebem ponteiros.

## Prototipação e revisão

A Design Layer aceita prototipação quando ela reduz incerteza. Porém ela não exige protótipo em todo projeto. A prototipagem serve para validar:

- intenção da jornada;
- clareza de fluxo;
- estados críticos;
- percepção da hierarquia;
- rótulos, feedback e ações.

A revisão de design deve observar o sistema como experiência real, e não apenas como conjunto de componentes ou layout. Ela avalia:

- intenção;
- clareza de estrutura;
- coerência de interação;
- acessibilidade;
- consistência;
- implementação e preservação da intenção original;
- complexidade desnecessária.

## Verificação e Learn Back

A verificação de design deve incluir evidência relevante:

- contraste e legibilidade;
- clareza de fluxo;
- acessibilidade;
- estados e erros;
- coerência com a Spec;
- preservação da intenção frente à implementação.

Se a experiência falhar, o problema deve retornar à camada responsável:

- problema de intenção → Frame ou Design Frame;
- problema de estrutura → Design Frame ou Design Spec;
- problema de fluxo → Design Spec;
- problema de padrão → princípio organizacional ou design system;
- problema de implementação → Build e Verification;
- problema recorrente em acessibilidade ou clareza → Design Principle, Verification Rule ou processo.

Esse mapeamento preserva a regra central do Radiant: aprendizado relevante deve corrigir a camada responsável.

## Ferramentas

A Design Layer é tool-agnostic. Ela não exige Figma, Penpot, Storybook, prototipação com IA ou um framework específico. Ferramentas podem ser escolhidas como procedimento do projeto, mas não definem a identidade do processo.

## Limites

A Design Layer não transforma o Radiant em uma metodologia de UX isolada. Ela continua sendo parte do sistema de geração de projetos, ao lado de Frame, Spec, Contract, Verify e Learn Back.

Ela também não exige uma camada de documentação visual pesada para todo projeto. O rigor segue risco, reversibilidade e impacto.

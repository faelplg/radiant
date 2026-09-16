# Evolução e versionamento

Mudanças seguem a [Constitution](../constitution/CONSTITUTION.md) e o
[ciclo operacional](../skills/radiant-cycle/SKILL.md). Preserve uma relação
revisável entre intenção, diff, evidência e, quando houver, finding de origem.

Antes de criar um corpo novo, consulte o [índice](capabilities.md). Corrija o
owner mais específico. Um adapter só recebe tradução para seu harness; regras
compartilhadas ficam no Core. Não duplicar procedures em documentação global.

Use alterações pequenas o suficiente para distinguir moves, ajustes editoriais
e mudanças de comportamento. Verifique os [critérios do repository](verification.md).
Mensagens de commit seguem Conventional Commits, sem coautoria automática de
agente. Registre motivação e referência de Learn Back no corpo quando relevante.

## Identidade inicial

O estado do Radiant é identificado por commit Git completo. Não existe release
formal ou contrato de compatibilidade de API que justifique SemVer do sistema
nesta etapa. Não adicionar `VERSION` apenas para repetir a tese.

A tese mantém sua versão 0.2. A Constitution mantém sua versão 0.1 e a política
da seção 9, aplicável àquele documento. Skills podem ter versão editorial própria;
ela é metadado auxiliar, não substitui a revisão do conjunto.

Tags e releases poderão nomear commits revisados quando houver consumidores e
critérios claros. Por enquanto, Git fornece autoria, estado anterior, diff e
motivação. Não editar CHANGELOG.md manualmente; geração futura pode usar esse
histórico. Não há automação de releases ou publicação nesta tarefa.

Consumidores adotam mudanças pela [política de pin](integration.md). Um commit
no Radiant não muda silenciosamente um projeto antigo. Não reescrever contratos
ou relatórios históricos para afirmar que usaram uma revisão nova.

## Learn Back como mudança

Use o [roteamento](learn-back.md) para justificar mudanças compartilhadas.
Compare a verificação anterior com a posterior. Constituições evoluem pelo
processo constitucional existente; não promover automaticamente uma preferência
ou um erro local para princípio universal.

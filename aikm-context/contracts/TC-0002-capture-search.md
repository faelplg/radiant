---
id: TC-0002
version: "0.2"
status: ready
execution_approval: pending
canonical_path: docs/project/contracts/TC-0002-capture-search.md
project: AI Knowledge Manager (AIKM)
milestone: M1 - parcela técnica
capabilities: ["01", "02 parcial", "03 parcial", "06 parcial"]
title: Captura e busca local
risk: Persistência local / reversível com proteção de dados
workflow: radiant-cycle@0.1.0
---

# Radiant Task Contract - AIKM - Captura e busca local

## 1. Proposta e ativação

Proposta produzida após a revisão aprovada da Spec e do Plan em 2026-09-15. Está
pronta para revisão, com aprovação de execução pendente. Não substitui nem
altera TC-0001. Sua existência não a torna ativa: a implementação só começa
depois da validação do responsável e da atualização de [ACTIVE.md](ACTIVE.md),
conforme a [convenção](README.md).

Revisão 0.2, ainda antes da execução: vincular o workflow operacional solicitado
pelo responsável e registrar a proveniência do procedimento no relatório da
entrega. Objetivo, capacidades delegadas e aprovação pendente permanecem iguais.

## 2. Objetivo

Entregar a parcela técnica de M1 que permite preservar um texto e reencontrá-lo
por uma necessidade em outro diretório de projeto, usando somente arquivos
locais. O usuário deve conseguir capturar sem classificar e inspecionar o
conteúdo encontrado antes de aplicá-lo.

Esta entrega prepara uma experiência real. Testes com fixtures não demonstram
reutilização real, ganho líquido ou adoção recorrente.

## 3. Inputs canônicos

- [Constitution](../../radiant/CONSTITUTION.md), já carregada na sessão ou lida
  antes da execução.
- [Frame v0.2.1](../FRAME.md), seções 5-6 e 27-32.
- [Spec v0.3.1](../SPEC.md), seções 4, 8-24, 38, 49-56, 68-71.
- [Plan v0.3.1](../PLAN.md), marco M1 da seção 4 e parcelas aplicáveis das
  capacidades 01-03 e 06, validação da seção 30 e comparação da seção 36.
- [ADR-0001](../adrs/ADR-0001-technical-bootstrap.md), implementação existente e
  instruções AGENTS.md aplicáveis.
- [Mapa operacional](../WORKFLOW.md) e
  [skill radiant-cycle](../../radiant/skills/radiant-cycle/SKILL.md) versão
  0.1.0: usar os modos executar e verificar/aprender nesta entrega, depois de
  revisar a proposta no modo planejar e obter sua ativação.

Preservar stack e convenções existentes. Só introduzir as dependências
selecionadas no ADR quando efetivamente utilizadas. Não reinterpretar restrições
canônicas para fazer a implementação passar.

## 4. Outputs e limites de capacidade

| Parcela         | Entrega                                                                                  | Continua pendente                                                 |
| --------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 01              | `init`, manifest, descoberta da raiz, estrutura legível e proteção contra sobrescrita    | Nenhuma parcela adicional desta capacidade                        |
| 02 parcial      | Records textuais, ID estável, provenance, schemas de entrada e de organização            | Sidecars opacos, diretórios compostos, relações avançadas         |
| 03 parcial      | Captura explícita de texto ou arquivo textual/Markdown, pre-check e defaults restritivos | Outros formatos, classificação automática, ingestão de históricos |
| 06 parcial      | Busca lexical em título/conteúdo, incluindo inbox e records organizados                  | Filtros adicionais, ranking composto, comando `retrieve`          |
| Validação de M1 | `validate` local para manifest e records, inclusive após edição manual                   | Doctor completo, verificação factual do conteúdo                  |

Documentar comandos executáveis no README e ajuda da CLI. Não anunciar comandos
ou parcelas pendentes como implementados.

## 5. Comportamento requerido

### Workspace

- `init [path]` cria a estrutura da Spec seção 8, manifest e mapa curto de uso.
  Defaults: `private`, `egressAllowed: false`, assistência de IA desabilitada.
- Redescobrir a raiz por diretório ancestral e permitir seleção explícita por
  `--workspace <path>` nos comandos que operam um workspace. A seleção explícita
  permite executar a busca a partir do diretório do Projeto B.
- Reabrir ou repetir init em workspace válido não sobrescreve conteúdo nem
  redefine políticas. Recusar colisões com conteúdo existente, manifest inválido
  ou destino inseguro, com erro acionável.
- Não seguir caminhos ou symlinks que escapem da raiz nas operações gerenciadas.
  Uma fonte externa explicitamente selecionada para captura pode ser lida, mas
  nunca modificada.

### Captura

- Oferecer `capture --text <text>` e `capture --file <path>` como entradas
  mutuamente exclusivas; arquivo inexistente não pode virar texto
  silenciosamente. Esses modos tornam explícito o `<path|text>` conceitual da
  Spec.
- Aceitar texto UTF-8 e Markdown. Rejeitar formato não suportado ou entrada
  vazia com diagnóstico acionável. Documentar limites de tamanho/parsing e
  verificá-los.
- Gerar metadata de entrada conforme Spec seção 14, sem perguntas de
  classificação. Começar como `candidate` e `unverified`, usando `raw` somente
  quando a origem externa estiver explicitamente estabelecida.
- Preservar o conteúdo textual e a referência da origem; não confiar em
  frontmatter da fonte para conceder trust, ativação ou egress. ID não depende
  do filename e não muda durante organização posterior.
- Recusar padrões conhecidos de secrets antes de qualquer gravação de conteúdo
  no workspace. Nenhum valor recusado deve aparecer em mensagens, logs ou
  temporários. Usar somente secrets sintéticas nos testes.
- Validar antes de publicar arquivos e não sobrescrever records existentes.
  Falhas não deixam records parciais; proteger colisões de nomes e IDs.

### Busca, inspeção e organização manual

- `search <query>` percorre records textuais canônicos sem IA ou índice
  obrigatório. Busca por título e conteúdo, sem distinção de caixa, com ordem
  determinística documentada.
- Cada resultado inclui ID, título, path, trecho pertinente, lifecycle, trust e
  role/kind ou classificação pendente. Candidatos no inbox aparecem; arquivados
  ficam fora por padrão. Identificar `superseded` e `deprecated` como
  inadequados para uso normal sem inspeção.
- Nenhuma correspondência é um resultado válido, distinguível de falha de
  leitura/validação. Metadata inválida deve gerar diagnóstico local com
  path/regra/ação, sem expor corpos ou secrets.
- O usuário pode abrir o arquivo retornado, organizar um item por edição
  explícita e executar `validate`. Exigir os campos de organização/promoção da
  Spec; não atribuir confiança superior automaticamente.
- `validate` retorna sucesso somente se manifest e todos os records no escopo
  textual forem válidos. Detectar IDs duplicados, metadata/política inválida e
  padrões conhecidos de secrets sem imprimir seus valores. Não reescrever
  arquivos.
- Busca e validação funcionam após copiar o workspace ou remover seu estado
  derivado. Não exigir registros formais de projetos para pesquisar a partir de
  outro diretório.

## 6. Paths permitidos

- `src/**`, `tests/**` e fixtures sintéticas de teste;
- manifests e lockfile gerado pelo gerenciador, quando houver dependência
  realmente utilizada;
- configuração de desenvolvimento necessária à entrega;
- `README.md`, ajuda da CLI e ignore rules necessárias;
- `docs/project/verification/TC-0002-capture-search.md`, evidência concisa desta
  entrega.

Workspaces de teste devem ficar em diretórios temporários criados para o teste e
ser limpos com alvo exato. Não criar um acervo pessoal permanente neste
repositório nem importar arquivos pessoais para fixtures.

Frame, Spec, Plan, Constitution, AGENTS, ADR-0001 e contratos são inputs somente
de leitura durante a implementação. Alterações materiais nesses limites exigem
HOLD e nova decisão. A presente proposta pode ser refinada antes de começar a
execução conforme a convenção.

## 7. Non-goals e segurança

Não implementar adapter, integração com provider, saída para serviços externos,
UI, sincronização, banco, embeddings, telemetria, processamento de formatos
opacos, comandos de routing/promoção, Learn Back ou Reuse Event.

A saída local de busca pode conter conteúdo privado; ela não é uma interface
autorizada para consumidores externos. O adapter protegido pertence a M2 e a
contrato próprio. Não enviar conteúdos reais, configurar ferramentas externas,
modificar outros projetos, publicar, fazer push ou instalar globalmente sob este
contrato.

Não mudar a stack nem criar abstrações para funcionalidades pendentes. Não
modificar originais importados, apagar conteúdo existente ou realizar migrações
destrutivas.

## 8. Verification

Começar pelo percurso real da CLI em workspace temporário, usando a sintaxe
documentada:

1. executar `init`, reabrir o workspace e repetir a operação sem alterar
   arquivos existentes;
2. capturar texto e arquivo Markdown sem fornecer role/kind/description;
3. em outro diretório vazio, usar `--workspace` e buscar por palavras do
   conteúdo, inspecionando o arquivo retornado;
4. organizar manualmente um candidato, preservando ID e origem, e validar;
   confirmar que organização incompleta é rejeitada;
5. copiar o workspace, remover apenas `.aikm/` dessa cópia temporária e repetir
   busca/validação;
6. executar casos adversos: secret sintética, manifest inválido, ID duplicado,
   origem inexistente, colisão, symlink de escape e falha de gravação;
   inspecionar o filesystem e os diagnósticos;
7. executar `npm run check`, preservando a cobertura aplicável do bootstrap e
   atualizando casos tornados obsoletos pela entrega, como a rejeição de `init`;
8. ler o diff e os arquivos resultantes contra este contrato, Spec e Plan.

Testes devem lançar a CLI real e cobrir operações válidas e recusadas, além da
chamada manual independente. O teste de falha de gravação deve funcionar no
ambiente de execução sem depender de uma suposição falsa de permissões. Não
basta afirmar que o comando retornou erro: inspecionar preservação dos dados e
ausência de conteúdo parcial ou recusado.

Registrar comandos exatos, resultados e limitações no relatório de verificação.
Registrar também path, versão e revisão/digest da skill efetivamente utilizada,
método de revisão, intervenções necessárias e findings materiais com
`fixTarget`. Uma mudança posterior na skill não altera retroativamente este
registro. Avaliar divergência material antes de substituir a versão indicada
neste contrato. Mapear AC-01, AC-02, AC-03 e AC-19, mais as parcelas textuais
aplicáveis de AC-05/06/08/09/16. A detecção de padrões é parcial. AC-20/21 e os
demais comportamentos pendentes não são demonstrados por esta entrega.

## 9. Estado final e próximo uso

- `DONE`: outputs técnicos existem, percurso da CLI e gates passam, dados são
  preservados e readback confirma o escopo. Isso conclui somente a parcela
  técnica de M1.
- `HOLD`: execução ainda não aprovada/ativada, input conflitante, limite de
  escrita insuficiente, dependência externa indisponível ou decisão material não
  delegada impede continuar.
- `FAIL`: verificação demonstra não conformidade que não pode ser resolvida
  dentro dos limites.

Relatar estado, funcionalidades entregues, comandos verificados, capacidades
pendentes e findings reutilizáveis com o menor `fixTarget`. Não alterar
documentos canônicos para ocultar divergências.

Após a entrega técnica, o próximo passo é observar uma necessidade real do
Projeto B no escopo autorizado, usando o protocolo do Plan seção 36. A
inexistência dessa oportunidade não invalida os testes técnicos, mas deixa a
hipótese de produto pendente. A observação orienta o contrato de M2 e as
próximas capacidades.

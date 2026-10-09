# Adapter Codex

Este é o mapa do harness, não o sistema. Os três níveis e a política de revisão
pertencem à [integração](../../docs/integration.md).

## Entrada do agente

1. Resolva a raiz indicada pelo bootstrap global e a raiz do consumidor.
2. Leia `.radiant.json` local e execute
   `python3 <radiant-root>/validators/check_project.py <project-root>`.
   Siga o resultado antes de carregar instruções compartilhadas.
3. Com o gate satisfeito, leia a
   [Constitution](../../constitution/CONSTITUTION.md) dessa revisão, o
   [Engineering Baseline](../../engineering/engineering-baseline.md), o
   [índice de capabilities](../../docs/capabilities.md) e a skill aplicável.
4. Leia os paths do mapa do consumidor conforme a tarefa; comandos são locais
   ao consumidor. O [Learn Back](../../docs/learn-back.md) aponta para os owners.

No próprio Radiant, use seu [AGENTS.md](../../AGENTS.md). Um pedido explícito de
primeiro bootstrap permite preparar o mapa do novo projeto, sem inventar um
pin ou iniciar uma implementação sem inputs. Conhecer a localização de uma
skill não significa que ela foi lida: carregue seu arquivo quando aplicável.
Não é necessária instalação em catálogo nativo para usar a skill por leitura.

## Configurar o usuário

Requisitos: Python 3.9+, Git e checkout acessível ao harness. Na raiz do Radiant:

```sh
python3 adapters/render_bootstrap.py
```

O comando imprime o [bloco global](../global.template.md) com o path absoluto
deste checkout. O bloco é o mesmo para todos os harnesses e indica o adapter de
cada um, então serve também quando Codex e outro harness leem o mesmo arquivo
de instruções. Para criar um arquivo local inspecionável, ignorado no Git:

```sh
python3 adapters/render_bootstrap.py --output .local/global.md
```

O gerador recusa sobrescrever arquivos e symlinks. Para regenerar, use outro
destino ou a saída padrão. Ele não instala regras, altera preferências nem
substitui o `AGENTS.md` do usuário.

Inclua apenas o bloco gerado, uma única vez, na fonte das instruções globais
do perfil usado.
No Codex, o local padrão é `~/.codex/AGENTS.md`; com `CODEX_HOME`, use o diretório
desse perfil. Um `AGENTS.override.md` não vazio tem prioridade. São mecanismos
do harness, não mecanismos de descoberta adicionais do Radiant.
Esses comportamentos seguem a
[documentação oficial de AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
consultada em 2026-09-15.

Preserve preferências existentes. Se o arquivo for gerado por Nix/dotfiles,
altere sua fonte e regenere pelo mecanismo proprietário. A configuração local
inspecionada nesta migração é desse tipo; a instalação externa não foi executada.

Abra uma sessão nova no consumidor e peça que identifique pointer, commit
validado, Constitution e mapa local. Confirme o carregamento das fontes; o
texto em Markdown é instrução para leitura, não import automático de arquivos.
Não alegar validação de sessão nova com base só no gerador.

Para desfazer, remova somente o bloco delimitado `radiant:begin/end` da fonte
das instruções globais e regenere quando aplicável. Não apague preferências
restantes. Para relocação, regenere o bloco com o novo checkout. Nenhum arquivo
do Core precisa mudar.

## Capacidades

O mapeamento capacidade → ID completo de modelo está em
[capabilities.json](capabilities.json), única fonte deste adapter. Trocar de
modelo é editar esse arquivo, verificar e regenerar os subagentes.

## Subagentes

Os perfis de [agents.json](../../skills/radiant-delegation/agents.json) viram
agentes customizados do Codex:

```sh
python3 adapters/render_bootstrap.py --adapter codex --agents-dir ~/.codex/agents
```

Cada TOML contém `name`, `description`, `model`, `developer_instructions` e,
nos perfis de leitura, `sandbox_mode`. O campo `developer_instructions` traz
apenas o ponteiro para a seção do papel na
[skill de delegação](../../skills/radiant-delegation/SKILL.md). O gerador
recusa a execução inteira se qualquer `radiant-*.toml` já existir.

- O `model` declarado no arquivo prevalece sobre o modelo pedido na criação do
  subagente. Um override de capacidade pelo contrato, portanto, roda na sessão
  do orquestrador, conforme a regra 5 da skill.
- O Codex não documenta bloqueio de delegação por agente; a regra de que
  papéis delegados não delegam está nas instruções do agente.
- Perfis com `access: read` recebem `sandbox_mode = "read-only"`. Perfis
  `write` herdam o sandbox da sessão; as fronteiras do contrato valem pela
  seção "Acesso e fronteiras" da skill de delegação.

Comportamentos conforme a
[documentação oficial de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents),
consultada em 2026-10-09. Para desfazer, remova os seis arquivos
`radiant-*.toml` de `~/.codex/agents/`.

## Configurar o consumidor

Use o [mapa neutro](../../templates/project-agents.md) como `AGENTS.md` e
[radiant-project.json](../../templates/radiant-project.json) como `.radiant.json`.
Preencha o commit e os paths conforme a [convenção](../../docs/integration.md),
incluindo `engineering_profile` quando o projeto possuir um Profile.
Um `AGENTS.md` já existente recebe só os ponteiros necessários, não substituição
integral. Constituição, templates compartilhados e skills permanecem no Radiant.

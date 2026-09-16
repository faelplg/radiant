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
python3 adapters/codex/render_bootstrap.py
```

O comando imprime o [template global](global.AGENTS.template.md) com o path
absoluto deste checkout. Para criar um arquivo local inspecionável, ignorado no Git:

```sh
python3 adapters/codex/render_bootstrap.py --output .local/codex-global.md
```

O gerador recusa sobrescrever arquivos e symlinks. Para regenerar, use outro
destino ou a saída padrão. Ele não instala regras, altera preferências nem
substitui o `AGENTS.md` do usuário.

Inclua apenas o bloco gerado na fonte das instruções globais do perfil usado.
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

## Configurar o consumidor

Use [project.AGENTS.template.md](project.AGENTS.template.md) como mapa local e
[radiant-project.json](../../templates/radiant-project.json) como `.radiant.json`.
Preencha o commit e os paths conforme a [convenção](../../docs/integration.md).
Um `AGENTS.md` já existente recebe só os ponteiros necessários, não substituição
integral. Constituição, templates compartilhados e skills permanecem no Radiant.

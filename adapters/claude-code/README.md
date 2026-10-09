# Adapter Claude Code

Este é o mapa do harness, não o sistema. Os três níveis e a política de revisão
pertencem à [integração](../../docs/integration.md); papéis e delegação, à
[skill radiant-delegation](../../skills/radiant-delegation/SKILL.md).

## Entrada do agente

1. Resolva a raiz indicada pelo bootstrap global e a raiz do consumidor.
2. Leia `.radiant.json` local e execute
   `python3 <radiant-root>/validators/check_project.py <project-root>`.
   Siga o resultado antes de carregar instruções compartilhadas.
3. Com o gate satisfeito, leia a
   [Constitution](../../constitution/CONSTITUTION.md) dessa revisão, o
   [Engineering Baseline](../../engineering/engineering-baseline.md), o
   [índice de capabilities](../../docs/capabilities.md) e a skill aplicável.
4. Ao coordenar papéis, a sessão principal é o orquestrador: leia a skill de
   delegação e use os subagentes `radiant-*` descritos abaixo.

No próprio Radiant, o [CLAUDE.md](../../CLAUDE.md) importa o
[AGENTS.md](../../AGENTS.md). Skills do Radiant são lidas pelo path; não é
necessária instalação em catálogo nativo.

## Configurar o usuário

Requisitos: Python 3.9+, Git e checkout acessível ao harness. Na raiz do Radiant:

```sh
python3 adapters/render_bootstrap.py --adapter claude-code
```

O comando imprime o [template global](global.CLAUDE.template.md) com o path
absoluto deste checkout. Para criar um arquivo local inspecionável, ignorado no Git:

```sh
python3 adapters/render_bootstrap.py --adapter claude-code --output .local/claude-global.md
```

Inclua apenas o bloco gerado no `~/.claude/CLAUDE.md`, preservando as
instruções existentes. O gerador recusa sobrescrever arquivos e symlinks e não
altera configuração global sozinho.

## Capacidades

O mapeamento capacidade → ID completo de modelo está em
[capabilities.json](capabilities.json). Ele é a única fonte deste adapter;
trocar de modelo é editar esse arquivo, verificar e regenerar os subagentes.
Aliases não são usados, para que a evidência identifique o modelo efetivo.

## Subagentes

Os perfis de [agents.json](../../skills/radiant-delegation/agents.json) viram
subagentes de usuário:

```sh
python3 adapters/render_bootstrap.py --adapter claude-code --agents-dir ~/.claude/agents
```

Cada arquivo contém só frontmatter e um ponteiro para a seção do papel na
skill de delegação, com o path absoluto deste checkout. O gerador recusa a
execução inteira se qualquer `radiant-*.md` já existir; para regenerar, remova
os seis arquivos e execute de novo.

- `disallowedTools: Agent` aplica a regra de que papéis delegados não delegam.
- Override de capacidade pelo contrato: o orquestrador passa o parâmetro
  `model` da invocação com o ID correspondente em `capabilities.json`; esse
  parâmetro prevalece sobre o frontmatter.
- A sessão principal deve rodar no modelo de `deep`.

Comportamentos de subagentes conforme a
[documentação oficial](https://code.claude.com/docs/en/sub-agents),
consultada em 2026-10-09.

## Manutenção

Execute a [skill de manutenção](../../skills/radiant-maintenance/SKILL.md)
localmente, manualmente ou por tarefa agendada na própria máquina, com a
sessão principal em `standard`. Rotinas em nuvem estão fora de escopo: o
relatório não pode ser persistido sem escrita externa.

## Procedimentos externos opcionais

Quando instalados, podem servir como "como fazer" de um papel. A saída sempre
vai para os paths do `.radiant.json`, nunca para os paths padrão da skill
externa. Sem eles, o papel segue apenas o Radiant.

| Papel | Procedimento sugerido |
| --- | --- |
| Ideação | `grilling` para Challenge |
| Design | `design-superpowers:design`, `design-superpowers:design-review` |
| Dev | `superpowers:test-driven-development`, `superpowers:systematic-debugging` |
| Verificador | `code-review`, `superpowers:verification-before-completion` |

## Configurar o consumidor

Use o [mapa neutro](../../templates/project-agents.md) como `AGENTS.md` e crie
um `CLAUDE.md` com a única linha `@AGENTS.md`. Use
[radiant-project.json](../../templates/radiant-project.json) como
`.radiant.json`, conforme a [convenção](../../docs/integration.md).

## Desfazer

Remova somente o bloco `radiant:begin/end` do `~/.claude/CLAUDE.md` e os seis
arquivos `radiant-*.md` de `~/.claude/agents/`. Nenhum arquivo do Core muda.

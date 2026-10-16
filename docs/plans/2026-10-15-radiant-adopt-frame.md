# Project Frame: adoção do Radiant

Revisão do Frame: 2 (2026-10-15), aguardando aprovação humana
Referência Radiant: 604c2a0b5103005e54b6a6089433f42d10d31320

## Intenção e participante

Adotar o Radiant num projeto hoje exige juntar passos de três lugares: a
[integração](../integration.md#mapa-do-projeto), a seção "Configurar o
consumidor" dos adapters e os templates. Nenhum desses lugares trata o caso do
projeto que já existe, com comandos, CI e convenções próprios. A
[entrada do adapter](../../adapters/claude-code/README.md#entrada-do-agente)
supõe um `.radiant.json` presente.

Participantes: o humano que decide adotar e o orquestrador que conduz a adoção.

Transformação: a partir do pedido "adote o Radiant aqui", o orquestrador
diagnostica o projeto, propõe o setup e escreve só depois da aprovação. O
projeto termina com mapa válido, comandos reais no `AGENTS.md` e as lacunas de
intenção listadas para o ciclo.

O Radiant define sozinho os arquivos que escreve e não depende de nenhuma
outra ferramenta. Uma ferramenta que gerencie skills ou contexto no mesmo
projeto convive com ele preservando o que está fora da seção do Radiant.

## Hipótese e Challenge

Hipótese: um checklist de adoção, seguido pelo orquestrador, leva um projeto
existente a um setup correto sem que fatos sejam inventados.

A [tese](../project-generation-system.md) só aceita uma capacidade nova
quando ela se repete e vale em mais de um projeto. Ainda não há dor registrada,
porque o único consumidor foi adotado à mão. Por isso, o trabalho avança em
etapas e cada uma só começa com a evidência da anterior.

| Etapa | Entrega | Avança se |
| --- | --- | --- |
| 1. Documentação | Seção "Adotar" na integração e ramo do adapter para projeto sem `.radiant.json` | Validador e testes passam; merge em `main` |
| 2. Adoção medida | Adoção de um projeto existente seguindo a etapa 1 | O resultado mostra erro, omissão ou atrito repetível |
| 3. Skill | `radiant-adopt`, só com o que a etapa 2 mostrou faltar | Repetir a etapa 2 em outro projeto melhora o resultado |

O Frame é refutado se a etapa 2 acertar sem atrito. Nesse caso, a documentação
basta e a skill não é criada.

## Menor experimento

Etapa 2 no projeto `faelplg/lab-ai-usage-quota`. Ele tem testes, typecheck e
CI, não publica o repositório como site e ainda não tem `AGENTS.md`.

1. Antes de começar, o humano escreve um gabarito com os comandos, as regras e
   as decisões que espera ver no setup.
2. O pin é o commit de `main` que contém a etapa 1, com o checkout principal
   limpo nesse commit. Nada muda no bootstrap global.
3. O orquestrador faz o diagnóstico só lendo, e propõe a lista exata de
   arquivos e o conteúdo de cada um.
4. Depois da aprovação, ele escreve num branch local, sem push.
5. O humano compara o resultado com o gabarito.

Evidência:

- itens do gabarito encontrados e itens omitidos;
- fatos inventados, com meta zero;
- arquivos tocados fora da lista aprovada, com meta zero, conferidos pelo diff
  e pelo `git status --ignored`;
- `check_project.py` saindo com 0, sem mudar o pin para passar;
- atritos anotados durante a adoção.

O `check_project.py` sozinho não prova a adoção, porque aceita um mapa todo
`null`. Ele só confirma a estrutura.

## Fronteiras

Arquivos que a adoção escreve:

- `.radiant.json`, com `null` em todo artefato que ainda não existe;
- uma seção `<!-- radiant:begin/end -->` no `AGENTS.md`, criando o arquivo se
  ele faltar e preservando todo o resto;
- `CLAUDE.md` com `@AGENTS.md`, só se não houver um `CLAUDE.md`;
- opcionalmente, `maintenance` e uma entrada no `.gitignore`, se o humano
  aprovar.

Restrições:

- Nada é escrito antes da aprovação, e nada fora da lista aprovada.
- O pin é decisão humana e precisa ser alcançável a partir de `main`.
- Configuração global continua manual, pelos comandos do adapter.
- Um comando só é seguro se for local, sem rede e sem escrita fora do projeto.

Non-goals:

- Escrever Frame, Spec, Plan ou Engineering Profile do produto. Esses itens
  ficam na lista de lacunas para o `radiant-cycle`.
- Atualizar o pin de quem já adotou.
- Adapter Codex. Ele entra depois da etapa 2, pelo mesmo texto.
- Qualquer integração com outra ferramenta de gestão de skills ou contexto.

Em aberto:

- O que a etapa 2 revelar decide se a etapa 3 existe e qual é o seu escopo.

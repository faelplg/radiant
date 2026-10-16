# Project Frame: adoção do Radiant

Revisão do Frame: 4 (2026-10-16), encerrado na etapa 2; a skill não será criada
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

1. O pin é o commit de `main` que contém a etapa 1, com o checkout principal
   limpo nesse commit. Nada muda no bootstrap global.
2. O orquestrador faz o diagnóstico só lendo, e propõe a lista exata de
   arquivos e o conteúdo de cada um.
3. O humano revisa a proposta direto, marcando o que está errado, o que sobra
   e o que falta.
4. Depois da aprovação, o orquestrador escreve num branch local, sem push.

Evidência:

- correções do humano na revisão: erros, sobras e omissões;
- fatos inventados, com meta zero;
- arquivos tocados fora da lista aprovada, com meta zero, conferidos pelo diff
  e pelo `git status --ignored`;
- `check_project.py` saindo com 0, sem mudar o pin para passar;
- atritos anotados durante a adoção.

A revisão 3 tirou o gabarito escrito antes da proposta. Para um projeto pequeno
e local, o custo não compensava (Artigo XVII). A perda aceita é que uma
omissão pode passar sem ser vista na revisão.

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

## Resultado da etapa 2

Adoção do `lab-ai-usage-quota` em 2026-10-16, no commit local `63576da` do
branch `chore/radiant-adoption`, sem push. Pin
`238190aa4918c74a7f1de99907e8215c7e96a443`.

| Evidência | Resultado |
| --- | --- |
| Correções do humano na revisão | 0 |
| Fatos inventados | 0 |
| Arquivos fora da lista aprovada | 0: só `.radiant.json`, `AGENTS.md`, `CLAUDE.md` e `.gitignore` |
| `check_project.py` | Saída 0, pin intacto |

Atritos, todos corrigidos na [integração](../integration.md#adotar-num-projeto)
e no [mapa neutro](../../templates/project-agents.md):

1. O checkout estava atrás do pin. O passo 1 agora diz quando fazer
   fast-forward.
2. O repositório é público. A proposta agora avisa que a seção vale para todo
   contribuidor, e o mapa diz o que segue quem não usa o Radiant.
3. O projeto é em inglês e o mapa em português. A seção fica em português.
4. Não havia lugar para a evidência. Ela vai no corpo do commit de adoção.
5. Classificar comando seguro exigiu ler os testes. O passo 2 agora diz isso e
   manda tratar a dúvida como não seguro.

Decisão humana: não houve erro nem invenção, e os atritos se resolveram no
checklist. A etapa 3 não acontece e a `radiant-adopt` não será criada.

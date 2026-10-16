# Integração e referência de revisão

## Três níveis

| Nível        | Owner e conteúdo                                                     | Não contém                                     |
| ------------ | -------------------------------------------------------------------- | ---------------------------------------------- |
| Radiant Core | Este repositório: Constitution, definição, capabilities e convenções | Estado de produtos                             |
| Usuário      | Localização do checkout e entrada do adapter do harness              | Corpos do Core ou conhecimento de projetos     |
| Projeto      | Opt-in, revisão, paths, restrições e comandos próprios               | Constitution ou skills compartilhadas copiadas |

O repository é a autoridade. O Core é lógico, distribuído pelos diretórios
listados no [README](../README.md); não exige uma pasta `core/` adicional.
Configuração global é reconstruível. Os adapters
[Codex](../adapters/codex/README.md) e
[Claude Code](../adapters/claude-code/README.md) implementam a descoberta em
cada harness. Outros harnesses poderão localizar os mesmos corpos com adapters
próprios.

## Descoberta mínima

O mecanismo escolhido é **um path local explícito no bootstrap do usuário**.
Um template portátil gera esse texto a partir do checkout. A configuração
gerada fica fora do conteúdo versionado. Não há fallback implícito por diretório
vizinho, registry, variável de ambiente ou symlink exigido pelo Radiant.

Esse mecanismo funciona também em um aplicativo aberto fora de um shell com
variáveis exportadas. É suficiente para um checkout compartilhado local e não
exige um instalador que reescreva preferências globais.

O projeto não declara o path pessoal da máquina. Seu adapter descobre a raiz
pela configuração do usuário. Em outra máquina, gere novamente o bootstrap.
Em caso de path inacessível, resolva a localização antes de executar sob Radiant;
não use uma cópia antiga encontrada por acaso.

## Mapa do projeto

Na raiz do consumidor, `.radiant.json` declara o uso do sistema. Comece pelo
[formulário](../templates/radiant-project.json). Seu schema inicial é:

- `radiant_revision`: commit Git completo, 40 ou 64 dígitos hexadecimais.
- `frame`, `spec`, `plan`, `workflow`, `active_contract`: arquivo relativo à
  raiz do consumidor ou `null` enquanto não existir.
- `engineering_profile`: arquivo relativo ao consumidor ou `null` quando o
  Baseline for suficiente e não houver decisões específicas do projeto.
- `contracts`, `adrs`, `verification`, `learning`: diretório relativo ou `null`.
- `maintenance`: opcional; diretório relativo ignorado pelo Git onde a
  Manutenção grava seus relatórios, ou `null`. Pode ainda não existir: a skill
  de [manutenção](../skills/radiant-maintenance/SKILL.md) o cria na primeira
  execução. Campo ausente equivale a `null`.

Todos os campos estão presentes, exceto o opcional `maintenance`; não inserir
paths absolutos, `..` ou symlinks que escapem do projeto. Quando um artefato for criado, atualize seu ponteiro.
`null` não dispensa um input necessário à tarefa: a skill identifica a lacuna
e orienta seu enquadramento. O validador estrutural não concede autorização.

O `AGENTS.md` do consumidor aponta para esse mapa e para a entrada do harness.
O Baseline de engenharia vive no Radiant; o Profile, quando existir, vive no
consumidor e não deve copiar o corpo do Baseline.
Restrições, comandos e referências a ADRs locais podem ficar nele ou em
`workflow`, conforme o volume. A lista de contratos ativos existe somente no
`ACTIVE.md` apontado, nunca no mapa e no adapter simultaneamente.

Para começar, siga [Adotar num projeto](#adotar-num-projeto). O formulário
preenchido vira instância; o corpo da skill continua no Radiant.

## Adotar num projeto

O orquestrador conduz a adoção quando o humano pede e o projeto ainda não tem
`.radiant.json`. Os passos valem para projeto novo e existente.

1. **Conferir o Radiant.** O bootstrap global aponta para um checkout limpo,
   num commit alcançável a partir de `main`. Se o checkout estiver limpo em
   `main` e só atrás do remoto, faça fast-forward até o commit escolhido; com
   trabalho em andamento, não troque a branch. Se o bootstrap não apontar
   para um checkout, pare em `HOLD` e indique o setup do adapter. A
   configuração global é feita pelo humano.
2. **Diagnosticar, só lendo.** Levante, com path e linha, os comandos de
   build, teste, lint e typecheck (manifests, scripts e CI), as instruções que
   já existem (`AGENTS.md`, arquivo do harness, README) e as decisões
   registradas. Não execute comandos nesta etapa. Para classificar um comando
   como seguro, leia o script e os testes que ele roda; na dúvida, ele não é
   seguro.
3. **Propor.** Apresente a lista exata de arquivos e o conteúdo de cada um:
   - `.radiant.json` com o pin proposto e `null` em todo artefato que ainda
     não existe;
   - no `AGENTS.md`, uma seção entre `<!-- radiant:begin -->` e
     `<!-- radiant:end -->` a partir do [mapa neutro](../templates/project-agents.md),
     com os comandos encontrados. Crie o arquivo se faltar e preserve todo o
     resto;
   - o arquivo de instruções do harness, só se ele não existir, conforme o
     adapter. Se existir sem apontar para o `AGENTS.md`, registre como lacuna;
   - opcionais: `maintenance` e sua entrada no `.gitignore`;
   - lacunas: Frame, Spec, Plan e Engineering Profile ausentes, encaminhados
     à [skill de ciclo](../skills/radiant-cycle/SKILL.md). Nada é inventado
     para preenchê-los.

   Em repositório público ou compartilhado, diga na proposta que a seção e o
   arquivo do harness valem para todo contribuidor, inclusive quem não usa o
   Radiant. O humano decide se a adoção entra no repositório.
4. **Escrever o aprovado.** Antes, guarde `git status --porcelain --ignored`.
   Escreva só os arquivos aprovados, num branch, sem push. O corpo do commit
   de adoção registra o diagnóstico resumido e a lista aprovada; essa é a
   evidência da adoção.
5. **Verificar.** `check_project.py` sai com 0 sem mudar o pin. Compare
   `git status --porcelain --ignored` com o estado guardado: a diferença,
   incluindo arquivos não rastreados e ignorados, contém só a lista aprovada,
   e o conteúdo de cada arquivo novo confere com a proposta. O check confirma
   a estrutura, não a qualidade do diagnóstico.

O pin é decisão humana. Um comando proposto como seguro roda localmente, sem
rede e sem escrita fora do projeto. A seção e os comentários que a adoção
escreve ficam em português, como o mapa neutro, mesmo num projeto em outro
idioma. O Radiant escreve só os arquivos acima;
outra ferramenta no mesmo projeto convive com ele porque o conteúdo fora da
seção do Radiant é preservado.

## Sem atualização silenciosa

Antes de carregar Constitution e capabilities para um consumidor, verificar:

1. O checkout descoberto é um repositório Radiant completo.
2. Seu `HEAD` corresponde exatamente a `radiant_revision`.
3. Não há modificações tracked, staged ou arquivos não rastreados relevantes
   nesse checkout. Arquivos ignorados como `.local/` não compõem o Core.
4. Os paths declarados do consumidor existem e permanecem dentro dele.

`python3 <radiant-root>/validators/check_project.py <project-root>` verifica
essas condições. Qualquer divergência deixa o consumo em HOLD, antes de ler
novas regras. O bootstrap do adapter é apenas o mecanismo de localização e
checagem, não uma autorização para aplicar a revisão encontrada.

Um pin registrado sem conferir o checkout não basta. Não alterar o pin para
fazer a validação passar. Para projetos em revisões diferentes, pode-se preparar
um checkout/worktree Git limpo da revisão requerida e regenerar o pointer
global para ele. Checkouts são materializações do mesmo histórico canônico,
não corpos independentes mantidos em cada produto. Não trocar automaticamente
a branch de um checkout que contém trabalho em andamento.

Uma atualização é uma decisão explícita de ciclo: comparar revisões, avaliar
Constitution/capabilities/adapter afetados, registrar razão, alterar o pin e
verificar o novo ciclo. Contrato em execução mantém a referência com que começou;
mudanças materiais seguem [integridade de contratos](../contracts/README.md).
Relatórios guardam o commit aplicado, mesmo após o projeto atualizar seu pin.

Tags futuras podem ser nomes de conveniência, resolvidos para commit completo.
Branch, `HEAD`, versão isolada da Constitution ou da tese não são pins válidos.

## Fonte e configuração gerada

O template e seu gerador pertencem ao adapter versionado. O texto gerado contém
o path local e pode ser incluído na fonte da configuração global. Se esta for
gerenciada por dotfiles/Nix, regenere através desse gerenciador; não edite a
saída gerada. O setup detalhado e o rollback estão no adapter.

## Fronteira AIKM

Radiant funciona com Git e arquivos sem instalar AIKM. Desde a revisão 2 do
Frame AIKM (2026-10-12), AIKM é um consumidor do Radiant e uma ferramenta que
gera, por projeto, os arquivos nativos de skills, contexto e servidores MCP de
cada harness. Ele não preserva nem recupera evidência ou aprendizado do ciclo:
essa camada de conhecimento da v1 é non-goal. Evidência e Learn Back ficam nos
artefatos do consumidor e no histórico Git do Radiant. O corpo das capabilities
Radiant continua neste repositório; distribuir um pointer ou uma cópia gerada
não transfere ownership nem autoriza egress de seu destino.

Os documentos de projeto do AIKM vivem no repositório AIKM. A custódia que
existia aqui foi encerrada conforme o
[plano de migração](migration-plan.md#encerramento-da-custódia).

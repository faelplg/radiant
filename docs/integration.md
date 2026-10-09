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

Para começar: selecionar a revisão, configurar o mapa e o adapter local,
enquadrar a intenção com o template de Frame, escrever Spec e Plan locais
orientados pela skill e criar Contracts locais quando aplicáveis. O formulário
preenchido vira instância; o corpo da skill continua no Radiant.

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

Radiant funciona com Git e arquivos sem instalar AIKM. AIKM pode preservar
referências, proveniência, evidência e aprendizado do ciclo. O corpo das
capabilities Radiant continua neste repositório; conhecimento operacional de
outros domínios pode pertencer ao AIKM. Capturar ou recuperar um pointer não
transfere ownership nem autoriza egress de seu destino.

Os snapshots atuais seguem o [plano de separação](../migration/README.md).

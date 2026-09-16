# Relatório da reorganização canônica

Estado: **DONE** para organização, integração projetada e verificação local.
Conclusão em 2026-09-16. Instalação global efetiva e adoção do novo adapter pelo
AIKM não fazem parte da execução externa desta entrega.

Autoridade: solicitação do responsável para transformar esta pasta em repository
Radiant independente, seguida da autorização para dois commits locais. A
[análise anterior aos moves](migration-plan.md) preserva inventário, ownership,
decisões e riscos. Não houve push, remoto ou escrita em outro projeto.

## Estrutura anterior

Uma pasta sem Git, `AGENTS.md` vazio, tese 0.2 e Constitution 0.1 na raiz, mais
12 documentos AIKM em `aikm-context/` e um `.DS_Store`. Frame era 0.2.1;
Spec/Plan, 0.3.1. O contexto continha TC-0001 encerrado e TC-0002 proposto.
Faltavam os corpos da skill e do adapter referenciados nesses documentos.

A consulta delimitada ao AIKM existente recuperou o adapter original e a skill
0.1.0 com digest compatível com os relatórios. A Constitution externa só diferia
editorialmente; a fonte fornecida nesta pasta foi preservada como owner.

## Estrutura final

```text
radiant/
  README.md
  AGENTS.md
  .gitignore
  constitution/CONSTITUTION.md
  docs/
    project-generation-system.md
    capabilities.md
    integration.md
    contributing.md
    verification.md
    learn-back.md
    migration-plan.md
    repository-report.md
  skills/radiant-cycle/SKILL.md
  templates/
    README.md
    project-frame.md
    task-contract.md
    radiant-project.json
  contracts/README.md
  adapters/codex/
    README.md
    global.AGENTS.template.md
    project.AGENTS.template.md
    render_bootstrap.py
  validators/
    README.md
    check_repository.py
    check_project.py
  tests/test_integration.py
  migration/
    README.md
    AGENTS.md
    inventory.json
    historical-links.json
    aikm/  (snapshot recebido, sem alterações)
  .local/codex-global.md  (gerado, ignorado no Git)
```

Não há `projects/`, `knowledge/`, `workflows/` ou pastas de adapters futuros sem
função presente. O workflow é a skill real; `docs/capabilities.md` apenas a
indexa. A futura Design Layer pode acrescentar capabilities sem mudar owners.

## Arquivos movidos

| From | To |
| --- | --- |
| `constitution.md` | `constitution/CONSTITUTION.md` |
| `project-generation-system.md` | `docs/project-generation-system.md` |
| `aikm-context/FRAME.md` | `migration/aikm/FRAME.md` |
| `aikm-context/SPEC.md` | `migration/aikm/SPEC.md` |
| `aikm-context/PLAN.md` | `migration/aikm/PLAN.md` |
| `aikm-context/WORKFLOW.md` | `migration/aikm/WORKFLOW.md` |
| `aikm-context/adrs/ADR-0001-technical-bootstrap.md` | `migration/aikm/adrs/ADR-0001-technical-bootstrap.md` |
| `aikm-context/contracts/README.md` | `migration/aikm/contracts/README.md` |
| `aikm-context/contracts/ACTIVE.md` | `migration/aikm/contracts/ACTIVE.md` |
| `aikm-context/contracts/TC-0001-iteration-00-bootstrap.md` | `migration/aikm/contracts/TC-0001-iteration-00-bootstrap.md` |
| `aikm-context/contracts/TC-0002-capture-search.md` | `migration/aikm/contracts/TC-0002-capture-search.md` |
| `aikm-context/learning/LR-0001-workflow-activation.md` | `migration/aikm/learning/LR-0001-workflow-activation.md` |
| `aikm-context/verification/VR-0001-workflow-setup.md` | `migration/aikm/verification/VR-0001-workflow-setup.md` |
| `aikm-context/verification/VR-0002-bootstrap-acceptance.md` | `migration/aikm/verification/VR-0002-bootstrap-acceptance.md` |
| `aikm-context/.DS_Store` | `migration/aikm/.DS_Store` (somente local, ignorado) |

## Criados, preservados e ajustados

| Arquivo(s) criado(s) | Função |
| --- | --- |
| `README.md` | Entrada humana e índice da árvore |
| `.gitignore` | Excluir metadata Finder, cache Python e saída local |
| `docs/capabilities.md` | Descoberta de corpos disponíveis |
| `docs/integration.md` | Três níveis, mapa local e pin |
| `docs/contributing.md` | Evolução e identidade Git |
| `docs/verification.md` | Gates e critérios estruturais |
| `docs/learn-back.md` | Destinos reais de correção |
| `docs/migration-plan.md` | Inventário e decisões antes dos moves |
| `docs/repository-report.md` | Este relatório |
| `skills/radiant-cycle/SKILL.md` | Skill incorporada do primeiro experimento |
| `templates/README.md` | Uso e ownership dos formulários |
| `templates/project-frame.md` | Formulário mínimo de intenção |
| `templates/task-contract.md` | Formulário de delegação |
| `templates/radiant-project.json` | Configuração portátil do consumidor |
| `contracts/README.md` | Convenção genérica extraída do experimento |
| `adapters/codex/README.md` | Entrada e bootstrap do harness |
| `adapters/codex/global.AGENTS.template.md` | Fonte portátil do bloco global |
| `adapters/codex/project.AGENTS.template.md` | Ponteiros do consumidor |
| `adapters/codex/render_bootstrap.py` | Geração local sem sobrescrita |
| `validators/README.md` | Comandos e limites dos validators |
| `validators/check_repository.py` | Links, custódia e portabilidade |
| `validators/check_project.py` | Pin, checkout limpo e paths do consumidor |
| `tests/test_integration.py` | Percursos reais dos scripts em ambiente isolado |
| `migration/README.md`, `migration/AGENTS.md` | Ownership e proteção da custódia |
| `migration/inventory.json` | SHA-256 dos originais e destinos |
| `migration/historical-links.json` | Exceções exatas de navegação histórica |
| `.local/codex-global.md` | Configuração local gerada, não fonte versionada |

O `AGENTS.md` existente foi preenchido. Constitution, 12 documentos AIKM e
metadata Finder foram preservados byte a byte. A tese só perdeu a duplicação
normativa da seção 9, substituída por link; seu texto conceitual restante e
versão foram preservados. A skill só mudou versão editorial e link para a
Constitution. Nenhum conteúdo foi eliminado sem permanecer no histórico.

Os 12 links históricos únicos que escapam do snapshot AIKM possuem resolução
no [mapa de custódia](../migration/README.md). Não foram falsamente consertados
para abrir arquivos de outro projeto. Todos os links operacionais novos são
diretos e verificados; os corpos históricos não foram reescritos.

## Fontes canônicas

- Tese: [docs/project-generation-system.md](project-generation-system.md).
- Constituição: [constitution/CONSTITUTION.md](../constitution/CONSTITUTION.md).
- Procedure/capability de ciclo: [radiant-cycle](../skills/radiant-cycle/SKILL.md).
- Templates: [templates/](../templates/README.md).
- Contract system: [contracts/README.md](../contracts/README.md).
- Integração compartilhada: [integration.md](integration.md).
- Harness: [adapters/codex/](../adapters/codex/README.md).
- Verification e Learn Back: seus [checks](verification.md) e
  [mapa de destinos](learn-back.md), subordinados à Constitution e à skill.

## Configuração global, projeto e AGENTS

O mecanismo escolhido é um path configurado pelo usuário. O gerador preenche um
template pequeno com o checkout descoberto pelo próprio script. Não exige
variável adicional, symlink, registry ou instalação do Core em outro lugar.
Mudar de máquina ou path exige regenerar somente o bloco.

O bloco fica nas instruções globais efetivas do perfil Codex, por inclusão na
configuração fonte do usuário. A documentação oficial, consultada pela skill
OpenAI Docs, determinou o tratamento do perfil e do override; veja
[adapter](../adapters/codex/README.md). A configuração atual é gerenciada por
Nix: foi gerado apenas `.local/codex-global.md`, sem modificar sua fonte ou saída.

Global AGENTS localiza o checkout e o adapter. O AGENTS do Radiant orienta
trabalho neste repository. O AGENTS consumidor aponta para o adapter e seu
`.radiant.json`, além de comandos/restrições específicos. Nenhum recebe a tese,
a Constitution ou a skill como cópia.

## Versionamento

O commit `471c65085ff5e9271c27e8fa24b62d37bd80ba0f` preserva o estado recebido.
O segundo commit introduz esta reorganização e este relatório. Sua identidade
é recuperável por `git log`, sem autorreferência impossível no próprio arquivo.

Um consumidor registra o SHA completo em `radiant_revision`; relatórios de
ciclo preservam a revisão realmente usada. O gate recusa divergência de HEAD e
checkout alterado. Atualização é adoção explícita, nunca efeito silencioso de
`git pull`. Não há SemVer do repository; versões existentes da tese,
Constitution e skill conservam seus escopos próprios.

## Revisão e simulações

Houve uma passagem de revisão após o Build contra os critérios do pedido e de
[Verification](verification.md). A evidência independente da narrativa inclui
Git, SHA-256 dos inputs anteriores e o validador preexistente da skill, além de
execução dos scripts em subprocessos. Não houve outro agente/revisor; o readback
arquitetural próprio não é apresentado como uma revisão humana independente.

| Critério | Resultado observado |
| --- | --- |
| Canonicality | Constitution única; tese aponta para ela; snapshots rotulados históricos |
| Core/adapter | Regras de revisão no Core; tradução de descoberta no Codex |
| Global | Bloco inferior a 1 KiB; regenerável; sem cópia de corpos |
| Portabilidade | Bootstrap e gate passam em checkout temporário com espaços/acentos |
| Projeto independente | Estado próprio no consumidor; nenhum Core copiado |
| AIKM independente | Testes de consumo funcionam sem a pasta de custódia |
| One body/pointers | Skill e convenção vivas únicas; exceções históricas explícitas |
| Discoverability | Percursos A/B/C abaixo inspecionados |
| Versionabilidade | Baseline recuperável, renames verificáveis, pin obrigatório |
| Minimalismo | Nenhum diretório vazio ou adapter especulativo |
| Extensibilidade | Novas capabilities podem usar os mesmos owners/diretórios |

**A - Trabalhar no Radiant.** O AGENTS leva à Constitution, tese e índice; este
leva à skill. O modo de revisão leva aos checks do repository e ao roteamento
de Learn Back. O checkout de desenvolvimento não é bloqueado por um pin de
consumidor; alterações são justamente o objeto dessa sessão.

**B - Novo projeto.** O bootstrap global localiza Radiant; o AGENTS consumidor
lê o adapter e seu mapa. O commit é conferido antes de carregar regras. O projeto
cria seu Frame, Spec e Plan e registra os paths; cria contratos e `ACTIVE.md`
localmente. A skill continua no checkout compartilhado. Testes exercitaram mapa
inicial, criação de estado, relocação, gate e atualização explícita de revisão.

**C - AIKM.** A comparação read-only confirmou que seus 12 documentos já existem
no repository AIKM com conteúdo igual aos snapshots. A adoção futura pode
referenciar Radiant e manter esses documentos no lugar; não precisa mover o
produto para este repository. Evidência e aprendizado ficam no AIKM; uma
correção reutilizável pode apontar para um arquivo Radiant. O AIKM não vira owner
do sistema nem requisito do bootstrap.

## Evidência executada e limites

- `python3 validators/check_repository.py`: passou; links locais, anchors,
  exceções históricas explícitas e digests preservados.
- `python3 -m unittest discover -s tests -v`: sete testes passaram. Cobrem
  novo consumidor, paths inválidos e escape por symlink, JSON inválido/duplicado,
  pin divergente/simbólico, mudanças tracked/staged/untracked, adoção explícita
  após novo commit, geração portátil e recusa de sobrescrita.
- `render_bootstrap.py --output .local/codex-global.md`: criou saída local;
  leitura confirmou pointer para este checkout e ausência de corpos do Core.
- `quick_validate.py skills/radiant-cycle`: `Skill is valid!`. A primeira
  tentativa encontrou PyYAML ausente. PyYAML 6.0.3 foi instalado somente em
  diretório temporário para executar o verificador, sem dependência no Radiant.
- `git diff --check` e revisão do índice/diff: integridade da alteração
  conferida; conteúdo anterior preservado no baseline. Hard breaks Markdown dos
  originais não foram reformados para satisfazer whitespace de importação.
- Ambiente executado: macOS, Python 3.14.7 e Git 2.55.0. Compatibilidade declarada
  com Python 3.9+ usa somente APIs dessa base; outras versões não foram executadas.

A skill 0.1.0 recuperada orientou o planejamento. A 0.1.1 incorporada foi lida
para a revisão, SHA-256
`daaf24af79f42aad54a3e66f4854f586c7504758086507b1d7e87ace61af3f25`.
Skill Creator orientou a validação da incorporação mínima; Conventional Commits
orientou os dois registros de histórico.

Não foi iniciada uma sessão nova real do Codex nem instalado o bloco global.
Os cenários A/B/C são simulações conceituais acompanhadas de execução real dos
scripts, não prova de comportamento futuro do modelo ou de utilidade AIKM.

## Learn Back desta reorganização

Finding: referências ao Core dentro do AIKM tornavam sua localização dependente
do primeiro consumidor. Evidência: links originais quebrados nesta pasta, skill
ausente e adapter recuperado no AIKM. Fix targets: repository, integração e
adapter. Correção: corpos com owner Radiant e pointers de consumo com revisão
explícita. Verificação: navegação, preservação e testes de consumidor realocado.
Reutilização em uma futura entrega de produto permanece por demonstrar.

Findings futuros ficam locais quando específicos; os reutilizáveis podem
originar alteração no arquivo Radiant responsável, com razão, evidência e
verificação. Uma Constitution amendment exige a justificativa transversal
prevista na própria Constitution, nunca promoção automática.

## Questões abertas e trabalho adiado

Nenhuma decisão material impede a organização entregue. Permanecem para a
adoção externa: o ciclo/revisão que o AIKM escolherá, a inclusão do bloco na fonte
Nix do usuário e a retirada posterior da custódia depois de conferir o destino.

Não implementados: Experience Design, System Design, Design Layer e seus
artefatos; outros adapters; publicação; releases/tags e changelog automatizado;
package management; registro automático de skills no harness; integração de
captura/retrieval com AIKM; alterações no produto ou ativação de TC-0002.

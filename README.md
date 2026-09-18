# Radiant

Radiant organiza a transformação de intenção em sistemas verificáveis e faz o
aprendizado corrigir o processo usado nos ciclos seguintes. Reduz contexto
perdido, escopo implícito e regras duplicadas entre agentes.

É um sistema operacional de desenvolvimento, não um produto consumidor,
framework de agentes ou base de conhecimento. Funciona sem AIKM.

O [ciclo e a tese](docs/project-generation-system.md) explicam o sistema.
A [Constitution](constitution/CONSTITUTION.md) é sua única fonte normativa
constitucional. A tese 0.2 é uma definição conceitual; sua seção de estado atual
registra o momento em que foi escrita, não o status desta reorganização.

## Encontrar o que precisa

| Local                                                                      | Responsabilidade                                         |
| -------------------------------------------------------------------------- | -------------------------------------------------------- |
| [AGENTS.md](AGENTS.md)                                                     | Mapa para trabalhar no próprio Radiant                   |
| [constitution/CONSTITUTION.md](constitution/CONSTITUTION.md)               | Invariantes e precedência                                |
| [engineering/engineering-baseline.md](engineering/engineering-baseline.md) | Baseline de engenharia proporcional                      |
| [docs/capabilities.md](docs/capabilities.md)                               | Índice das capacidades disponíveis                       |
| [docs/design-layer.md](docs/design-layer.md)                               | Camada canônica de design do Radiant                     |
| [skills/radiant-cycle/SKILL.md](skills/radiant-cycle/SKILL.md)             | Procedimento reutilizável do ciclo                       |
| [templates/](templates/README.md)                                          | Formulários de Frame, Contract, Design e mapa do projeto |
| [contracts/README.md](contracts/README.md)                                 | Convenção compartilhada de contratos                     |
| [adapters/codex/](adapters/codex/README.md)                                | Bootstrap específico do harness atual                    |
| [validators/](validators/README.md)                                        | Checks locais de integridade e revisão                   |
| [docs/contributing.md](docs/contributing.md)                               | Evolução e versionamento                                 |
| [docs/verification.md](docs/verification.md)                               | Verificar mudanças neste sistema                         |
| [docs/learn-back.md](docs/learn-back.md)                                   | Encaminhar aprendizado ao owner correto                  |
| [migration/](migration/README.md)                                          | Custódia temporária dos documentos AIKM                  |

## Usar em outro projeto

1. Escolha um commit do Radiant e um checkout limpo dessa revisão.
2. Gere o bloco global conforme o [adapter Codex](adapters/codex/README.md).
3. No consumidor, use o template de `AGENTS.md` do adapter e declare a revisão
   e os paths locais conforme a [convenção de integração](docs/integration.md).
4. Crie Frame, Spec, Plan, Engineering Profile e Contracts no consumidor,
   proporcionalmente à tarefa. O Profile é recomendado quando houver stack,
   segurança, integração ou risco específico; o Baseline permanece no Radiant.
   Leia skills e templates diretamente no Radiant.

A configuração global contém somente um path e uma entrada do adapter. Pode
ser reconstruída; não contém Constitution, skills ou estado de projetos.
Uma nova revisão do Radiant não atualiza consumidores automaticamente.

## Evoluir

Modifique o owner canônico, execute os [checks](docs/verification.md) e registre
motivação e evidência em Git. Um finding de projeto pode melhorar um template,
skill, validator ou adapter pelo [Learn Back](docs/learn-back.md). Só invariantes
transversais justificam propostas constitucionais.

Há uma skill de ciclo real, formulários de artefatos, uma camada de design e um mapa de integração.
Não há engines, package manager, adapters futuros ou dependência de ferramenta específica.
O procedimento de workflow vive na skill; nenhum diretório vazio o duplica.

Veja o [relatório da reorganização](docs/repository-report.md) para inventário,
moves, decisões, simulações, evidências e limites desta entrega.

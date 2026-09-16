# Trabalhar no Radiant

Este arquivo é o mapa do próprio repositório. Comece pela
[Constitution](constitution/CONSTITUTION.md) e pela
[definição do sistema](docs/project-generation-system.md). O índice de
[capabilities](docs/capabilities.md) aponta para os corpos reutilizáveis.

Em planejamento, execução ou revisão relevante, leia a
[skill radiant-cycle](skills/radiant-cycle/SKILL.md) e aplique o modo pertinente
à autorização atual. O pedido que governa esta reorganização e seu escopo estão
registrados no [plano de migração](docs/migration-plan.md).

Para mudanças no sistema, siga [contribuição e versionamento](docs/contributing.md),
[verificação](docs/verification.md) e [Learn Back](docs/learn-back.md).
Comandos locais: `python3 validators/check_repository.py` e
`python3 -m unittest discover -s tests -v`. Use Python 3.9+ e Git.

Integração com consumidores está em [integração](docs/integration.md) e no
[adapter Codex](adapters/codex/README.md). O Core compartilhado não depende do
adapter. Trabalhando neste repositório, a árvore local é o alvo de edição;
o pin de um consumidor não impede desenvolver uma nova revisão do Radiant.

`migration/aikm/` guarda snapshots externos, não contratos ativos deste
repositório. Consulte o [mapa de custódia](migration/README.md) antes de mexer
nesses arquivos. Não aplicar comandos AIKM como gates do Radiant.

Preserve corpos históricos, evite reformatação em massa e não edite arquivos
gerados ou CHANGELOG.md manualmente. Novos textos usam hífen simples e não
adicionam divisores horizontais. Não implementar a futura Design Layer nesta
reorganização.

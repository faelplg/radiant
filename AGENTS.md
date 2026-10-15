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

Integração com consumidores está em [integração](docs/integration.md) e nos
adapters [Codex](adapters/codex/README.md) e
[Claude Code](adapters/claude-code/README.md). O Core compartilhado não depende
de adapter. Para coordenar papéis e delegar, leia a
[skill radiant-delegation](skills/radiant-delegation/SKILL.md); decisões
estruturais do Radiant ficam em [docs/adrs/](docs/adrs/ADR-0001-delegation-roles.md). Trabalhando neste repositório, a árvore local é o alvo de edição;
o pin de um consumidor não impede desenvolver uma nova revisão do Radiant.

Para contexto rápido, três páginas privadas no claude.ai resumem o sistema: o
[mapa](https://claude.ai/artifact/7QZWWNTBv5NSxrePFBiaWg) em arc42 e C4, o
[glossário](https://claude.ai/artifact/7aaAD9YCE2nkVTkm4EDa3L) e os
[casos de uso](https://claude.ai/artifact/PEKb9oaxypnxxsQ1FTtoAQ). São visões
derivadas: o texto deste repositório vence quando divergem. Ao mudar a
Constitution, a tese, uma skill, um adapter, um template ou um ADR, atualize a
página afetada; as fontes e os passos estão em `source/README.md` do mapa.
Proponha evoluções citando sua base: documento canônico, código, evidência ou
método nomeado.

Os documentos AIKM que ficaram sob custódia aqui pertencem ao repositório AIKM;
o encerramento está no [plano de migração](docs/migration-plan.md#encerramento-da-custódia).
Não aplicar comandos AIKM como gates do Radiant.

Preserve corpos históricos, evite reformatação em massa e não edite arquivos
gerados ou CHANGELOG.md manualmente. Novos textos usam hífen simples e não
adicionam divisores horizontais. Não implementar a futura Design Layer nesta
reorganização.

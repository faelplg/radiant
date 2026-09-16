# Inventário e plano de migração

Análise realizada antes dos moves em 2026-09-15. A pasta não tinha `.git`;
`AGENTS.md` tinha zero bytes. Todos os 15 documentos Markdown foram lidos
integralmente. `.DS_Store` é metadata binária do Finder, sem papel operacional.

## Inventário completo e ownership

| Current path | Responsabilidade / classificação | Owner canônico | Destino proposto | Ação | Razão |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | Radiant adapter, vazio | Radiant | `AGENTS.md` | Preencher | Entrada do agente no próprio sistema |
| `constitution.md` | Radiant normative | Radiant | `constitution/CONSTITUTION.md` | Mover sem editar | Fonte normativa inequívoca |
| `project-generation-system.md` | Radiant Core, tese 0.2 | Radiant | `docs/project-generation-system.md` | Mover; deduplicar seção 9 | Explicação distinta da norma |
| `aikm-context/FRAME.md` | AIKM project state, 0.2.1 | AIKM | `migration/aikm/FRAME.md` | Mover sem editar | Intenção do consumidor |
| `aikm-context/SPEC.md` | AIKM project state, 0.3.1 | AIKM | `migration/aikm/SPEC.md` | Mover sem editar | Comportamento do consumidor |
| `aikm-context/PLAN.md` | AIKM project state, 0.3.1 | AIKM | `migration/aikm/PLAN.md` | Mover sem editar | Incrementos do consumidor |
| `aikm-context/WORKFLOW.md` | AIKM project state / adapter local | AIKM | `migration/aikm/WORKFLOW.md` | Mover sem editar | Mapa local, não procedure compartilhada |
| `aikm-context/adrs/ADR-0001-technical-bootstrap.md` | AIKM project state | AIKM | `migration/aikm/adrs/ADR-0001-technical-bootstrap.md` | Mover sem editar | Stack AIKM não é stack Radiant |
| `aikm-context/contracts/README.md` | Convenção genérica + contexto AIKM | AIKM (snapshot); Radiant (convenção extraída) | `migration/aikm/contracts/README.md` | Preservar; extrair convenção | Não converter instância histórica em norma viva |
| `aikm-context/contracts/ACTIVE.md` | AIKM project state | AIKM | `migration/aikm/contracts/ACTIVE.md` | Mover sem editar | Nenhum contrato ativo; TC-0002 não autorizado |
| `aikm-context/contracts/TC-0001-iteration-00-bootstrap.md` | AIKM project state, contrato encerrado | AIKM | `migration/aikm/contracts/TC-0001-iteration-00-bootstrap.md` | Mover sem editar | Preservar delegação e aceite históricos |
| `aikm-context/contracts/TC-0002-capture-search.md` | AIKM project state, proposta | AIKM | `migration/aikm/contracts/TC-0002-capture-search.md` | Mover sem editar | Não ativar nem reescrever proposta |
| `aikm-context/learning/LR-0001-workflow-activation.md` | AIKM project state, evidência | AIKM | `migration/aikm/learning/LR-0001-workflow-activation.md` | Mover sem editar | Proveniência de Learn Back |
| `aikm-context/verification/VR-0001-workflow-setup.md` | AIKM project state, evidência | AIKM | `migration/aikm/verification/VR-0001-workflow-setup.md` | Mover sem editar | Não atribuir uso retroativo |
| `aikm-context/verification/VR-0002-bootstrap-acceptance.md` | AIKM project state, evidência | AIKM | `migration/aikm/verification/VR-0002-bootstrap-acceptance.md` | Mover sem editar | Aceite de implementação externa |
| `aikm-context/.DS_Store` | Historical/transitional, metadata Finder | Máquina | `migration/aikm/.DS_Store` | Mover; ignorar no Git | Preservar sem poluir histórico |

Diretórios anteriores: raiz, `aikm-context/` e seus filhos `adrs/`,
`contracts/`, `learning/`, `verification/`. Não havia templates, capabilities,
skills, validators, workflows ou exemplos independentes na pasta. Nenhum
artefato textual ficou com classificação unknown; nenhum foi classificado como
exemplo permanente.

## Evidência complementar inspecionada

O repositório AIKM vizinho já existe. Somente seus artefatos relacionados ao
Radiant foram consultados; nenhuma escrita externa faz parte desta migração.

| Fonte externa | Responsabilidade | Decisão |
| --- | --- | --- |
| AIKM `AGENTS.md` | Primeiro adapter Codex 0.2 | Evidência de navegação; novo adapter não copia suas regras |
| AIKM `docs/radiant/CONSTITUTION.md` | Cópia transitória | Difere apenas em frontmatter e divisores; a fonte fornecida nesta pasta vence |
| AIKM `docs/radiant/skills/radiant-cycle/SKILL.md` | Radiant capability 0.1.0 | Incorporar em `skills/radiant-cycle/SKILL.md`, corrigindo link e versão editorial |

Origem da skill: AIKM commit `3e896d441a7ce3563531f923861ad1f109f809ce`,
SHA-256 `5b7c61260188afab1e7f9b561130829b655412b20aff6bd8bbb26660b8401c06`,
igual ao registrado em VR-0001/VR-0002. O adapter externo e as cópias externas
permanecem transitórios até adoção explícita pelo AIKM.

## Canonicality e decisões

- Constitution: um corpo em `constitution/CONSTITUTION.md`. A lista normativa
  repetida na seção 9 da tese passa a ser referência; demais ideias permanecem.
- Ciclo: reutilizar a skill existente. `docs/capabilities.md` será só índice;
  não criar um workflow paralelo com o mesmo corpo.
- Contracts: convenção genérica em `contracts/README.md`, formulário em
  `templates/task-contract.md`; contratos e ativação pertencem ao consumidor.
- Frame: formulário mínimo baseado na tese, sem copiar o Frame AIKM.
- Verification e Learn Back: procedimentos da skill e critérios específicos
  em `docs/verification.md` e `docs/learn-back.md`, subordinados à Constitution.
- Integração: um path configurado no bootstrap global gerado a partir de
  template; nenhum registry, variável adicional obrigatória ou package manager.
- Revisão: commit Git completo por projeto e por ciclo. Versões de documentos
  não identificam todo o sistema. Não adotar SemVer do repositório agora.

## Riscos e contenções antes da execução

Moves internos são reversíveis. O índice Git guarda o estado original antes
das mudanças; hashes verificam a preservação. Não apagar documentos nem editar
artefatos gerados. Não sobrescrever destinos existentes.

Referências históricas AIKM pressupõem `docs/project/` e `docs/radiant/` no
repositório original, já ausentes nesta pasta. Serão inventariadas em
`migration/README.md` com resolução explícita, sem mudar corpos de contratos ou
evidências. O validador distinguirá links operacionais de referências históricas
conhecidas, detectando novos links quebrados em ambos.

O `AGENTS.md` global observado é um symlink gerenciado por Nix. Gerar um bloco
local para inspeção e documentar inclusão na configuração fonte; não alterar o
symlink nem o store. Instalação real não é condição da arquitetura solicitada.

Transferência definitiva de documentos AIKM e substituição de suas cópias do
Core ficam fora desta execução. Exigem comparar com o estado do repositório
destino e autorizar a mudança nele. Havendo conflito material nessa futura
transferência, usar HOLD; não sobrescrever nem inferir qual versão prevalece.

Não implementar Experience Design, System Design ou qualquer artefato da futura
Design Layer. Diretórios só serão criados com conteúdo operacional real.

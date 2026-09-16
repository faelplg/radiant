# Templates

Um template é o formulário compartilhado. O documento preenchido é estado do
projeto, com identidade, decisões e histórico próprios. Não manter no consumidor
uma cópia do template para distribuição a outros projetos.

- [project-frame.md](project-frame.md): intenção e menor experimento.
- [task-contract.md](task-contract.md): delegação delimitada; usar a
  [convenção](../contracts/README.md).
- [radiant-project.json](radiant-project.json): mapa local e pin, conforme
  [integração](../docs/integration.md). Substituir `RADIANT_COMMIT` por commit
  completo real; `null` significa que o artefato ainda não existe.

Templates de configuração do harness vivem no
[adapter](../adapters/codex/README.md). Regras completas permanecem nos owners,
não são copiadas para os formulários.

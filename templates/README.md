# Templates

Um template é o formulário compartilhado. O documento preenchido é estado do
projeto, com identidade, decisões e histórico próprios. Não manter no consumidor
uma cópia do template para distribuição a outros projetos.

- [project-frame.md](project-frame.md): intenção e menor experimento.
- [design-frame.md](design-frame.md): enquadramento da experiência antes da
  implementação.
- [design-spec.md](design-spec.md): estrutura da experiência, estados, fluxos,
  acessibilidade e critérios de verificação.
- [task-contract.md](task-contract.md): delegação delimitada; usar a
  [convenção](../contracts/README.md).
- O Engineering Profile é um artefato do consumidor; o Baseline permanece em
  [engineering/engineering-baseline.md](../engineering/engineering-baseline.md).
- [radiant-project.json](radiant-project.json): mapa local e pin, conforme
  [integração](../docs/integration.md). Substituir `RADIANT_COMMIT` por commit
  completo real; `null` significa que o artefato ainda não existe.

Templates de configuração do harness vivem no
[adapter](../adapters/codex/README.md). Regras completas permanecem nos owners,
não são copiadas para os formulários.

# Validators

Requisitos: Python 3.9+ e Git. Sem pacotes externos.

- `python3 validators/check_repository.py`: integridade dos documentos,
  links/anchors locais, snapshots preservados e portabilidade do Core. Read-only.
- `python3 <radiant-root>/validators/check_project.py <project-root>`: valida
  `.radiant.json`, pin, checkout limpo e paths locais. Read-only; divergências
  produzem `HOLD` e saída 1. Sucesso estrutural não ativa contratos.

Os limites semânticos e a revisão dos percursos estão em
[Verification](../docs/verification.md). Os checks não validam verdade factual,
política de egress de AIKM, execução de produto nem obediência de um modelo.

# Validators

Requisitos: Python 3.9+ e Git. Sem pacotes externos.

- `python3 validators/check_repository.py`: integridade dos documentos,
  links/anchors locais, Constitution única, portabilidade do Core e
  coerência entre perfis delegáveis e o mapa de capacidades de cada adapter,
  requisitos e `provides.json` dos adapters, o exemplo de unidades do template
  e o exemplo de roteamento. Read-only.
- `radiant_yaml.py` lê o YAML restrito dos blocos `radiant-units`, e
  `dispatch_formats.py` valida unidades, `provides` e regras de roteamento.
- `python3 <radiant-root>/validators/check_project.py <project-root>`: valida
  `.radiant.json`, pin, checkout limpo e paths locais. Read-only; divergências
  produzem `HOLD` e saída 1. Sucesso estrutural não ativa contratos.

Os limites semânticos e a revisão dos percursos estão em
[Verification](../docs/verification.md). Os checks não validam verdade factual,
política de egress de AIKM, execução de produto nem obediência de um modelo.

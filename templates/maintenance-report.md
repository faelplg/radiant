# Relatório de manutenção - [projeto] - [AAAA-MM-DD]

Formulário da [skill de manutenção](../skills/radiant-maintenance/SKILL.md).
O relatório preenchido fica no diretório `maintenance` do consumidor, ignorado
pelo Git.

## Execução

- Revisão do Radiant: `[commit completo]`
- Commit do consumidor: `[commit]`
- Relatório anterior: `[path | nenhum]`
- Delegações, uma por rodada: `[perfil, capacidade, ID do modelo, estado, métrica de uso do adapter | ausente]`

## Fontes

| Fonte | Situação | Detalhe |
| --- | --- | --- |
| `[fonte]` | `consultada / pulada por política / falhou` | `[comando, motivo ou erro]` |

## Candidatos

| ID | Categoria | Evidência | Risco | Valor | Reversibilidade | Situação |
| --- | --- | --- | --- | --- | --- | --- |
| `M-1` | `[ciclo / gate / drift / dependência / forge / pin]` | `[saída, path:linha]` | `[baixo/médio/alto]` | `[baixo/médio/alto]` | `[alta/média/baixa]` | `novo / recorrente / resolvido` |

## Rascunhos de contrato

Até três candidatos do topo. Não são contratos e não possuem ID.

### `[M-1]` - [título]

- Objetivo: `[mudança observável]`
- Outputs: `[arquivos ou comportamento]`
- Verificação: `[comando ou critério]`

## Omissões e limitações

- `[o que não foi observado e por quê]`

## Estado

`DONE | HOLD | FAIL` - `[conclusão em uma frase, incluindo "nada material" quando for o caso]`

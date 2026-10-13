---
name: radiant-maintenance
description:
  Fazer a triagem de manutenção de um projeto consumidor do Radiant e
  produzir um relatório com propostas priorizadas e rascunhos de contrato,
  sem alterar o projeto. Usar em execução manual ou agendada localmente.
metadata:
  version: "0.1.2"
---

# Manutenção Radiant

A Manutenção observa um consumidor e alimenta o
[ciclo](../radiant-cycle/SKILL.md) com propostas. Ela só propõe: nada muda no
projeto sem que o humano selecione um candidato e o orquestrador crie e ative
um contrato. Papéis, capacidades e retorno seguem a
[skill de delegação](../radiant-delegation/SKILL.md); o formato do relatório,
o [template](../../templates/maintenance-report.md).

## Entrada

1. Leia `.radiant.json` e execute o gate do adapter. Sem campo
   `maintenance`, ou com `maintenance: null`, termine em `HOLD`: o consumidor
   não declarou onde relatórios podem ser gravados.
2. Leia o documento de `workflow` e sua seção de Manutenção: comandos seguros
   para manutenção e fontes externas autorizadas. Sem essa seção, nenhum
   comando é executado e nenhuma fonte externa é consultada.
3. Confirme que o path do relatório a gravar, dentro do diretório
   `maintenance`, é ignorado pelo Git do consumidor (por exemplo,
   `git check-ignore -q <maintenance>/<relatório>.md` com saída 0). Verifique
   o arquivo, não o diretório: uma regra como `maintenance/` só casa com o
   diretório depois que ele existe. Se não for ignorado, termine em `HOLD`:
   gravar ali deixaria o projeto com mudanças rastreadas.
4. Leia o relatório anterior mais recente no diretório `maintenance`, se
   existir.

## Fontes

| Fonte | O que procurar |
| --- | --- |
| Estado do ciclo | Contrato `held` sem decisão; Learning Record com `fixTarget` sem correção; `ACTIVE.md` incoerente com os contratos |
| Gates do projeto | Falhas nos comandos declarados seguros |
| Drift | Spec ou Plan afirmando o que o código não faz; links quebrados nos artefatos |
| Dependências | Versões desatualizadas ou vulneráveis, somente via comandos e fontes autorizados |
| Forge | Issues abertas e CI da branch principal, somente se autorizado |
| Pin do Radiant | Revisão mais nova disponível, como candidato e nunca como atualização |

Comando não declarado seguro é pulado. Fonte externa não autorizada é pulada.
Cada omissão entra no relatório com o motivo (Artigo XII da
[Constitution](../../constitution/CONSTITUTION.md)).

## Priorização

Cada candidato precisa de evidência concreta: saída de comando, path, linha.
Opinião sem evidência não é candidato. Ordene por risco, valor e
reversibilidade, e marque cada um como novo, recorrente ou resolvido em
relação ao relatório anterior, incluindo seus adendos:

- um candidato é o mesmo quando aponta a mesma lacuna no mesmo alvo (path,
  módulo, documento ou fonte), mesmo que a redação ou a evidência mudem; ele
  mantém o ID, e candidatos novos recebem o número seguinte ao maior ID
  anterior;
- `resolvido` exige evidência de que o estado do próprio alvo mudou, como
  commit, PR ou saída de comando sobre esse alvo; mudança em outro lugar, como
  no Radiant, não resolve uma lacuna do consumidor;
- um candidato anterior que nenhuma fonte desta execução reobserva continua
  `recorrente`, com a nota de que não foi reobservado.

Para até três candidatos do topo, escreva um rascunho de contrato embutido no
relatório: objetivo, outputs e verificação.
Rascunhos não viram arquivos de contrato nem recebem ID.

## Fronteira

- A única escrita é o relatório, no diretório `maintenance`, criado na
  primeira execução se não existir, depois da confirmação do passo 3 da
  Entrada.
- Sem branch, PR, issue, commit, instalação ou atualização de dependência.
- Execução somente local. Coleta em `light`; priorização, rascunhos e a sessão
  orquestradora em `standard`.
- Uma execução agendada fixa o modelo de `standard` na própria sessão quando o
  agendador permite. Quando não permite, a sessão se limita a gate, pacote e
  readback, e delega priorização e rascunhos ao perfil `radiant-maintenance`,
  cujo modelo o adapter fixa. O relatório registra o modelo efetivo da sessão
  e de cada rodada; sessão fora de `standard` sem essa delegação é desvio.

## Saída

Termine em `DONE` com o path do relatório, mesmo que a conclusão seja "nada
material": é um resultado válido. Use `HOLD` quando a entrada estiver
incompleta e `FAIL` quando a triagem não puder ser feita. A seleção de um
candidato é humana; a partir dela, o orquestrador cria o contrato pela
[convenção](../../contracts/README.md) e segue o ciclo.

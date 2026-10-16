# Convenção de Task Contracts

Esta é a convenção compartilhada. Instâncias, ativação e evidência pertencem ao
projeto consumidor. Origem: convenção testada no primeiro projeto, identificada
no [inventário](../docs/migration-plan.md). A cópia que ficou sob custódia foi
retirada e só existe no histórico Git.

## Identidade e localização

Use IDs sequenciais estáveis por projeto, como `TC-0001`, e filenames
`TC-0001-short-slug.md`. O ID não depende do número da iteração. Não incluir
versão ou status no filename nem mover contratos entre pastas de status.
Uma iteração pode exigir mais de um contrato.

Registre a revisão do documento e o status nos metadados. Estados de lifecycle
recomendados: `ready`, `active`, `done`, `held`, `failed`, `superseded`.
Eles não substituem os estados de conclusão da
[Constitution](../constitution/CONSTITUTION.md).

## Ativação

O `ACTIVE.md` local aponta para o contrato que governa o trabalho ou declara
explicitamente `none`. Leia esse ponteiro; não selecione pelo timestamp ou
filename. Proposta pronta não autoriza execução. Registre autorização já
concedida e atualize o ponteiro, sem exigir a mesma autorização novamente.

## Integridade

Antes de executar, uma proposta pode ser refinada. Depois de começar, não
reescreva silenciosamente objetivo, limites, outputs ou critérios. Esclarecimentos
não materiais ficam em amendment explícito. Mudanças materiais exigem HOLD e
contrato novo ou superseding; registre `supersedes`/`supersededBy` quando útil.

O [template](../templates/task-contract.md) captura a delegação. Use a
[política de revisão](../docs/integration.md) para fixar qual Radiant a orienta.
Registre o procedimento realmente aplicado na evidência, com versão e
commit/digest. Atualizações compartilhadas não reescrevem execução passada.

Relatórios de verificação e aprendizado apontam para ID/path do contrato, sem
copiar seu corpo. Feche o contrato e atualize `ACTIVE.md` quando a conclusão
estiver sustentada. Não crie contratos retroativos para fabricar conformidade.

## Unidades de execução

Um contrato pode dividir o trabalho em unidades, num bloco ` ```yaml radiant-units `
do [template](../templates/task-contract.md). O bloco usa YAML restrito, lido
por `validators/radiant_yaml.py` sem dependências. Todo bloco válido nesse
subconjunto é YAML válido com o mesmo valor, então leitores com parser
completo, como um operador de despacho, leem o mesmo conteúdo.

Aceito: mapeamentos e sequências em bloco, inclusive `- chave: valor` com
continuação alinhada à chave; listas de escalares entre colchetes, sem
aninhamento; escalares simples, entre aspas duplas (escapes `\"`, `\\` e `\n`)
ou simples (`''` como aspa); `true`, `false`, `null` e inteiros; comentários
`#` no início da linha ou depois de espaço; indentação só com espaços.

Recusado, com o número da linha: tab na indentação, chave repetida, âncoras
(`&`, `*`), tags (`!`), blocos `|` e `>`, mapeamentos entre chaves, marcadores
de documento, valor simples com `: ` ou terminado em `:` (use aspas) e valor
simples em várias linhas.

Regras do bloco:

- `id` segue `TC-0000.N`, com o mesmo prefixo em todas as unidades, e nunca é
  renumerado. `role` é um perfil de
  [agents.json](../skills/radiant-delegation/agents.json).
- `capability` ausente usa o padrão do perfil; presente, exige
  `capability_reason`. `requires` usa os termos de
  [requirements.json](../skills/radiant-delegation/requirements.json).
- `writes` é subconjunto dos paths graváveis do contrato, sem `..` nem path
  absoluto. Unidades sem dependência entre si não se sobrepõem.
- `depends_on` cita só unidades do mesmo contrato, sem ciclo.
- A soma das unidades não ultrapassa objetivo, outputs e fronteira do
  contrato. Mudar a divisão depois do início é amendment quando a fronteira não
  muda e exige `HOLD` quando muda.

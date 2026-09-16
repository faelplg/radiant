# Convenção de Task Contracts

Esta é a convenção compartilhada. Instâncias, ativação e evidência pertencem ao
projeto consumidor. Origem: convenção testada no primeiro projeto, identificada
no [inventário](../docs/migration-plan.md); a cópia em migração é histórica.

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

# Custódia temporária do AIKM

Os arquivos em `aikm/` foram recebidos junto ao Radiant e pertencem ao projeto
AIKM. Permanecem aqui para evitar perda de contexto enquanto a transferência
definitiva não é executada. Não são exemplos, capabilities nem estado ativo do
Radiant. Consulte o [inventário anterior](../docs/migration-plan.md).

O destino conceitual é `docs/project/` do repositório AIKM. Esse repositório já
existe e foi inspecionado somente para localizar o adapter e a skill mencionados
pelos documentos. Nenhum arquivo externo foi escrito. Não copiar por cima do
estado atual desse projeto: comparar revisões e conteúdo antes da transferência.
Na conferência final, os 12 documentos já existiam em `docs/project/` do AIKM
com conteúdo idêntico; somente `.DS_Store` era exclusivo desta custódia. Portanto
não há corpo documental ausente a repor hoje. O trabalho futuro é adotar os
pointers no AIKM e encerrar a custódia após conferir novamente sua integridade.

## Referências históricas e resolução

Os corpos foram preservados byte a byte. Links entre os documentos AIKM continuam
locais; links que escapavam do pacote já dependiam do repositório original e
podem coincidir acidentalmente com arquivos do Radiant após o move. Eles não são
entradas operacionais. A resolução correta é esta:

| Referência no contexto AIKM original | Resolução / ação |
| --- | --- |
| `docs/radiant/CONSTITUTION.md` | Origem histórica: Constitution AIKM 0.1. Owner atual: [Constitution Radiant](../constitution/CONSTITUTION.md). Diferenças originais somente editoriais; não inferir pin retroativo. |
| `docs/radiant/skills/radiant-cycle/SKILL.md` | Origem histórica: skill 0.1.0, digest no relatório. Owner atual: [skill Radiant](../skills/radiant-cycle/SKILL.md) 0.1.1. O link novo não muda qual corpo foi usado no passado. |
| `AGENTS.md` da raiz AIKM | Adapter AIKM 0.2 existente no repositório AIKM. Não é o AGENTS desta raiz. Adoção futura usa o [template consumidor](../templates/project-agents.md). |
| `README.md#development` da raiz AIKM | Comandos de desenvolvimento do AIKM, não do Radiant. Consultar o repository AIKM ao retomar seu desenvolvimento. |
| Literais `docs/project/...`, `src/**`, `npm run check` | Paths e comandos de execução no repository AIKM original. Não rebasear fronteiras de contratos encerrados para esta pasta. |

[inventory.json](inventory.json) registra cada arquivo preservado e seu SHA-256.
[historical-links.json](historical-links.json) enumera cada link externo ao
snapshot com sua referência original. O validador confere essas exceções
individualmente, inclusive quando um link acabaria abrindo um arquivo errado
existente nesta árvore; novos links quebrados não são ignorados.

Essa custódia constitui uma exceção transitória e explícita à ausência de corpos
históricos duplicados. Somente os paths operacionais fora de `migration/` são
fontes compartilhadas vivas. O snapshot da convenção de contratos não evolui em
paralelo com [a convenção canônica](../contracts/README.md).

## Finalizar a separação

1. Validar o destino AIKM e comparar seus documentos vigentes com os snapshots.
2. Resolver conflitos com o owner AIKM; preservar evidência histórica em Git.
3. No AIKM, adotar `.radiant.json`, pin revisado e adapter consumidor; trocar
   cópias vivas de Constitution/skills por pointers ao Radiant.
4. Atualizar navegação operacional do AIKM, sem reatribuir versões em relatórios.
5. Verificar o percurso do AIKM e registrar aceite da transferência.
6. Somente então retirar esta custódia do working tree por mudança revisada;
   o histórico Git continuará preservando o estado recebido.

Esta tarefa não executa essa transferência, não ativa TC-0002 e não demonstra
capacidades de produto AIKM. O Core Radiant funciona sem acessar esta pasta.

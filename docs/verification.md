# Verificar alterações no Radiant

A [Constitution](../constitution/CONSTITUTION.md) define o significado de
conclusão. A [skill](../skills/radiant-cycle/SKILL.md), modo verificar e aprender,
define o procedimento. Aqui ficam os checks concretos deste repositório.

Execute na raiz com Python 3.9+ e Git, sem dependências de runtime adicionais:

```sh
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
git diff --cached --check
```

O primeiro comando verifica links Markdown locais e anchors, unicidade da
Constitution, ausência de paths pessoais nos documentos e coerência entre `agents.json`, as seções da skill de
delegação e o `capabilities.json` de cada adapter. Os testes exercitam o
gerador de bootstrap e subagentes, o gate de pin e o validator do repository
através dos seus comandos reais em diretórios temporários, incluindo
divergência, sujeira no checkout, paths inválidos e recusa de sobrescrita.

## Revisão estrutural separada do Build

Confronte os arquivos finais com estes critérios, depois dos checks:

| Critério | Evidência a inspecionar |
| --- | --- |
| Canonicality | Constitution única; índices e adapters apontam para owners |
| Core/adapter | Nenhuma regra geral exclusiva do harness |
| Global | Bloco pequeno, regenerável, sem corpos ou estado local de produto |
| Portabilidade | Repetir bootstrap em outro path, inclusive com espaços |
| Independência do projeto | Frame/Spec/Plan/Contracts no consumidor; pin conferido |
| Independência AIKM | Checks operacionais não dependem de executar o produto |
| Discoverability | Percursos abaixo alcançam fontes reais a partir da raiz |
| Versionabilidade | Diff e referência Git permitem saber o estado aplicado |
| Minimalismo | Cada arquivo tem função; nenhuma pasta vazia antecipatória |
| Extensibilidade | Novas capabilities cabem na estrutura sem introduzi-las agora |
| Agnosticismo de harness | Papéis e capacidades no Core; modelos e mecanismos só nos adapters; todo adapter mapeia as três capacidades |

Simule A: entrar pelo AGENTS do Radiant, encontrar Constitution, tese, capability
e verificação. Simule B: consumidor vazio, pin, bootstrap, Frame e estado local,
contrato e leitura compartilhada. Simule C: AIKM independente com seus documentos,
Learn Back e nenhum ownership sobre o Core. Simule D: sessão nova no Claude Code
encontra o bloco global, o adapter, o gate de pin, a Constitution e a skill de
delegação, e os subagentes gerados apontam para essa mesma revisão.

Use verificadores determinísticos como evidência independente da redação e
inspecione os percursos do consumidor. Declare se houve outro revisor ou apenas
readback próprio. Testes estruturais não demonstram que um modelo obedecerá ao
adapter em uma nova sessão; simulação conceitual não é E2E real do harness.

O validador não ignora links quebrados nem reescreve qualquer documento.

Registre resultados e limites no relatório autorizado. Se houver falha material,
corrija dentro do escopo e repita a verificação afetada. Não declarar DONE por
passagem de testes apenas.

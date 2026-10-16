# Despacho por backend: plano de implementação

> **Para agentes executores:** use superpowers:subagent-driven-development
> (recomendado) ou superpowers:executing-plans para executar este plano tarefa
> por tarefa. Os passos usam checkbox (`- [ ]`) para acompanhamento.

**Objetivo:** implementar no Radiant a parte do ADR-0002 que é processo:
divisão de execução no contrato, vocabulário de requisitos, `provides` dos
adapters, formato das regras de roteamento, despacho por backend na skill de
delegação e os registros de fronteira, com validators que leem YAML restrito.

**Arquitetura:** dois módulos novos em `validators/`, só com biblioteca
padrão: `radiant_yaml.py` lê um subconjunto estrito de YAML, e
`dispatch_formats.py` valida unidades, `provides` e regras de roteamento.
`check_repository.py` os usa para conferir o vocabulário, os adapters, o
exemplo do template e o exemplo de roteamento. O resto é texto e dados.

**Stack:** Python 3.9+ somente com biblioteca padrão, Git, Markdown, JSON e o
YAML restrito definido na Tarefa 1.

**Spec:** [ADR-0002](../adrs/ADR-0002-backend-dispatch-demerzel.md)

**Fora deste plano:** repositório, Frame, Spec, Plan e código do Demerzel
(ganham plano no próprio repositório, depois do merge); push e PR; a tabela
"Onde cada informação fica" já presente em `docs/integration.md`, que vai em
commit e PR próprios antes da Tarefa 1.

## Restrições globais

- Python 3.9+, sem pacotes externos. Nada de `match`, nem tipos com `|`; use
  `typing.Optional` e `typing.List` quando anotar.
- Textos novos em português, hífen simples, sem travessão e sem divisores
  horizontais.
- Capacidades exatamente `deep`, `standard`, `light`, lidas de `CAPABILITIES`
  em `check_repository.py`.
- Vocabulário inicial exatamente `browser`, `ios-simulator`, `computer-use`.
- `provides.json` dos dois adapters começa com lista vazia: cada item só entra
  com evidência de smoke em terminal (ADR-0002, seção 2).
- Bloco de unidades: cerca ` ```yaml radiant-units `, no máximo um por arquivo.
- ID de unidade: `^TC-\d{4}\.[1-9]\d*$`, todas com o mesmo prefixo `TC-xxxx`.
- Regras de roteamento: `schema` igual a `1`; ID de regra
  `^[a-z0-9]+(-[a-z0-9]+)*$`; `approval` só aceita `"human"`; `harness` é nome
  de diretório em `adapters/`.
- Local da instância de roteamento: `$XDG_CONFIG_HOME/radiant/routing.json`,
  ou `~/.config/radiant/routing.json` sem a variável.
- Não renumerar seções do template de contrato: a skill de delegação cita a
  seção 16.
- Commits em Conventional Commits, sem coautoria de agente.
- Após cada tarefa: `python3 validators/check_repository.py`,
  `python3 -m unittest discover -s tests -v` e `git diff --check` passam.

## Foco de revisão

1. Escalar simples com `: ` ou ` #` no meio, como
   `done_when: passa: ok`: erro pedindo aspas, nunca truncamento silencioso.
   Teste na Tarefa 1.
2. Chave repetida num mapeamento: erro com a linha, em vez de ficar com o
   último valor como faz YAML comum. Teste na Tarefa 1.
3. Sobreposição de `writes` entre unidades independentes com grafias
   diferentes: `src/sync` e `src/sync/` se sobrepõem; `src/sync/` e
   `src/sync2/` não. Teste na Tarefa 3.
4. Ciclo em `depends_on` (`.1` → `.2` → `.1`): erro, nunca laço infinito.
   Teste na Tarefa 3.
5. Dois blocos `radiant-units` no mesmo arquivo: erro, nunca o primeiro em
   silêncio. Teste na Tarefa 3.

### Tarefa 1: leitor de YAML restrito

**Files:**
- Create: `validators/radiant_yaml.py`
- Create: `tests/test_radiant_yaml.py`
- Modify: `contracts/README.md` (seção nova "Unidades de execução" com a
  definição do subconjunto)

**Interfaces:**
- Produces: `radiant_yaml.load(text: str) -> object`, que devolve `dict`,
  `list`, `str`, `int`, `bool` ou `None`; e `radiant_yaml.YamlError(ValueError)`,
  cuja mensagem começa com `linha <n>: `.

O subconjunto aceita: mapeamentos em bloco com chaves
`[A-Za-z_][A-Za-z0-9_-]*`; sequências em bloco (`- item`), inclusive
`- chave: valor` com continuação alinhada à chave; listas em fluxo de escalares
(`[a, b]`, `[]`) sem aninhamento; escalares simples, com aspas duplas (escapes
`\"`, `\\`, `\n`) ou simples (`''` como aspa); `true`, `false`, `null` e
inteiros tipados; comentários `#` no início da linha ou depois de espaço fora
de aspas; indentação só com espaços. Recusa: tab na indentação, chave
repetida, `&`, `*`, `!`, `|`, `>`, `{`, `---`, escalar simples com `: ` ou
terminado em `:`, e escalar simples em várias linhas.

- [ ] **Passo 1: escrever os testes que falham**

Em `tests/test_radiant_yaml.py`, importar o módulo inserindo
`SOURCE / "validators"` em `sys.path`, com uma classe `RadiantYamlTests`:

```python
def test_units_example_round_trip(self):
    data = load("units:\n  - id: TC-0025.1\n    requires: []\n    writes: [src/a/, tests/a/]\n    capability: deep\n")
    self.assertEqual(data, {"units": [{"id": "TC-0025.1", "requires": [],
        "writes": ["src/a/", "tests/a/"], "capability": "deep"}]})

def test_scalars_are_typed(self):
    self.assertEqual(load("a: true\nb: null\nc: 3\nd: '3'\ne: \"x # y\"\n"),
                     {"a": True, "b": None, "c": 3, "d": "3", "e": "x # y"})

def test_comments_are_ignored(self):
    self.assertEqual(load("# topo\na: b  # fim\n"), {"a": "b"})

def test_plain_scalar_with_colon_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 1: .*aspas"):
        load("done_when: passa: ok\n")

def test_duplicate_key_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 2: .*repetida"):
        load("a: 1\na: 2\n")

def test_tab_indentation_is_refused(self):
    with self.assertRaisesRegex(YamlError, r"^linha 2: .*tab"):
        load("a:\n\t- b\n")

def test_unsupported_features_are_refused(self):
    for text in ("a: &x 1\n", "a: *x\n", "a: !tag 1\n", "a: |\n  b\n", "a: {b: 1}\n", "---\na: 1\n", "a: [[b]]\n"):
        with self.subTest(text=text), self.assertRaises(YamlError):
            load(text)
```

- [ ] **Passo 2: confirmar que falham**

Run: `python3 -m unittest tests.test_radiant_yaml -v`
Expected: ERROR com `ModuleNotFoundError: No module named 'radiant_yaml'`.

- [ ] **Passo 3: implementar `load` em `validators/radiant_yaml.py`**

Parser recursivo por indentação sobre a lista de linhas sem comentário. Cada
nível conhece sua coluna e devolve `(valor, próxima linha)`. Remova comentários
com um varredor que respeita aspas antes de qualquer outra regra.

- [ ] **Passo 4: confirmar que passam**

Run: `python3 -m unittest tests.test_radiant_yaml -v`
Expected: 7 testes OK.

- [ ] **Passo 5: documentar o subconjunto**

Em `contracts/README.md`, seção "Unidades de execução" com um parágrafo: o
bloco `radiant-units` usa YAML restrito, lido por
`validators/radiant_yaml.py`; listar o que é aceito e o que é recusado, como
acima. Todo arquivo válido nesse subconjunto é YAML válido, então leitores com
parser completo, como o Demerzel, leem o mesmo valor.

- [ ] **Passo 6: commit**

```bash
git add validators/radiant_yaml.py tests/test_radiant_yaml.py contracts/README.md
git commit -m "feat(validators): read a strict YAML subset with the standard library"
```

### Tarefa 2: vocabulário de requisitos e `provides` dos adapters

**Files:**
- Create: `validators/dispatch_formats.py`
- Create: `skills/radiant-delegation/requirements.json`
- Create: `adapters/claude-code/provides.json`, `adapters/codex/provides.json`
- Create: `tests/test_dispatch_formats.py`
- Modify: `validators/check_repository.py` (função `check_dispatch(errors)`,
  chamada em `check()` logo após `check_delegation`)
- Modify: `tests/test_repository.py`

**Interfaces:**
- Produces: `dispatch_formats.load_requirements(path: Path) -> Set[str]`, que
  lê `{"requirements": {"<termo>": "<descrição>"}}` e levanta `ValueError` em
  formato inválido; `dispatch_formats.validate_provides(data: object,
  requirements: Set[str]) -> List[str]`, que aceita só
  `{"provides": [<termo>, ...]}` sem repetição e devolve as mensagens de erro.
- Produces: `check_dispatch(errors: list) -> None` em `check_repository.py`,
  que as Tarefas 3 e 4 estendem.

- [ ] **Passo 1: escrever os testes que falham**

Em `tests/test_dispatch_formats.py`, classe `ProvidesTests`:
`validate_provides({"provides": ["browser"]}, {"browser"}) == []`;
`{"provides": ["turbo"]}` produz uma mensagem contendo `'turbo'`;
`{"provides": ["browser", "browser"]}` produz uma contendo `repetido`;
`{"outros": []}` produz uma contendo `provides`.

Em `tests/test_repository.py`, na classe `RepositoryCheckTests`:

```python
def test_provides_with_unknown_requirement_fails(self):
    path = self.root / "adapters/codex/provides.json"
    path.write_text(json.dumps({"provides": ["turbo"]}), encoding="utf-8")
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/codex/provides.json", result.stderr)

def test_adapter_without_provides_fails(self):
    (self.root / "adapters/claude-code/provides.json").unlink()
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/claude-code", result.stderr)
```

- [ ] **Passo 2: confirmar que falham**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: ERROR de import em `test_dispatch_formats` e FAIL nos dois testes
novos de repositório.

- [ ] **Passo 3: criar os dados**

`requirements.json` com os três termos e uma descrição de uma linha cada.
`browser`: precisa navegar e inspecionar páginas. `ios-simulator`: precisa
rodar e dirigir o iOS Simulator. `computer-use`: precisa controlar apps do
desktop. Os dois `provides.json` com `{"provides": []}`.

- [ ] **Passo 4: implementar as funções e `check_dispatch`**

`check_dispatch` lê o vocabulário e, para cada diretório em `adapters/`, exige
`provides.json` válido, com o path relativo no começo de cada erro, como
`check_delegation` faz.

- [ ] **Passo 5: confirmar que passam**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: todos OK; validator em `PASS`.

- [ ] **Passo 6: commit**

```bash
git add validators/ skills/radiant-delegation/requirements.json adapters/*/provides.json tests/
git commit -m "feat(delegation): declare requirements and what each adapter provides"
```

### Tarefa 3: unidades de execução no template de contrato

**Files:**
- Modify: `validators/dispatch_formats.py`, `validators/check_repository.py`
- Modify: `templates/task-contract.md` (subseção `### Execution units` no fim
  da seção 4, sem renumerar)
- Modify: `contracts/README.md` (regras de integridade da divisão)
- Modify: `tests/test_dispatch_formats.py`, `tests/test_repository.py`

**Interfaces:**
- Consumes: `radiant_yaml.load`, `YamlError` (Tarefa 1); `load_requirements`,
  `check_dispatch` (Tarefa 2).
- Produces: `dispatch_formats.extract_units_block(markdown: str) ->
  Optional[str]`, que devolve o corpo do único bloco ` ```yaml radiant-units `,
  `None` sem bloco, e levanta `ValueError` com `mais de um bloco` quando há
  dois; `dispatch_formats.validate_units(data: object, agents: Dict[str, str],
  requirements: Set[str]) -> List[str]`, em que `agents` mapeia nome do perfil
  para capacidade padrão, lido de `agents.json`.

Regras de `validate_units`, que é o schema normativo do ADR:
- topo `{"units": [...]}` não vazio, sem outras chaves;
- chaves de unidade: `id`, `role`, `capability`, `capability_reason`,
  `requires`, `objective`, `writes`, `depends_on`, `done_when`; obrigatórias
  `id`, `role`, `objective`, `writes`, `done_when`; chave desconhecida é erro;
- `id` no padrão das restrições globais, único, mesmo prefixo para todas;
- `role` é nome de perfil em `agents`;
- `capability`, quando presente, está em `CAPABILITIES` e exige
  `capability_reason` não vazio; `capability_reason` sem `capability` é erro;
- `requires` é lista de termos do vocabulário;
- `writes` é lista não vazia de paths relativos POSIX, sem `..` e sem `/`
  inicial;
- `depends_on` só cita IDs existentes, nunca o próprio, e o grafo não tem
  ciclo;
- duas unidades sem caminho de dependência entre si não podem ter `writes`
  sobrepostos. Normalize retirando a barra final e compare por segmento: um
  path se sobrepõe a outro quando é igual a ele ou é seu prefixo seguido de `/`;
- `objective` e `done_when` são strings não vazias.

- [ ] **Passo 1: escrever os testes que falham**

Em `tests/test_dispatch_formats.py`, classe `UnitsTests`, com um fixture
`VALID` que reproduz o exemplo de duas unidades da seção 2 do ADR-0002 e
`AGENTS = {"radiant-dev": "standard", "radiant-verifier": "deep"}`:

- `test_valid_units_pass`: `validate_units(VALID, AGENTS, {"browser"}) == []`.
- `test_overlap_between_independent_units_fails`: `.2` sem `depends_on` e com
  `writes: [src/sources]` gera erro contendo `sobrep`.
- `test_overlap_check_uses_segments`: `src/sync/` e `src/sync2/` em unidades
  independentes não geram erro.
- `test_dependency_cycle_fails`: `.1` depende de `.2` e `.2` de `.1`; erro
  contendo `ciclo`, e a chamada termina.
- `test_capability_requires_reason`: `capability: deep` sem
  `capability_reason` gera erro contendo `capability_reason`.
- `test_unknown_role_requirement_and_key_fail`: `role: radiant-x`,
  `requires: [turbo]` e uma chave `harness` geram, cada um, um erro que cita o
  valor ou a chave.
- `test_ids_must_share_prefix`: `TC-0025.1` com `TC-0026.2` gera erro contendo
  `prefixo`.
- `test_escaping_write_path_fails`: `writes: [../x]` e `writes: [/x]` geram
  erro.
- `test_two_blocks_are_refused`: `extract_units_block` com dois blocos levanta
  `ValueError` contendo `mais de um bloco`.

Em `tests/test_repository.py`:

```python
def test_template_units_example_must_validate(self):
    path = self.root / "templates/task-contract.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("role: radiant-dev", "role: radiant-x", 1), encoding="utf-8")
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("templates/task-contract.md", result.stderr)
```

- [ ] **Passo 2: confirmar que falham**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: FAIL ou ERROR nos testes novos.

- [ ] **Passo 3: implementar `extract_units_block` e `validate_units`**

Para o ciclo e a alcançabilidade, calcule o fecho transitivo de `depends_on`
por busca em profundidade com marcação de visita; o mesmo fecho decide quais
pares são independentes.

- [ ] **Passo 4: escrever a subseção no template**

`### Execution units` no fim da seção 4: um parágrafo dizendo que a subseção é
opcional e que, sem ela, o contrato é uma unidade só; o exemplo de duas
unidades do ADR-0002 dentro da cerca `yaml radiant-units`; ponteiro para
`contracts/README.md#unidades-de-execução`. Em `contracts/README.md`, na mesma
seção da Tarefa 1, as regras de integridade: `id` estável e nunca renumerado;
a soma das unidades não ultrapassa o contrato; mudar a divisão depois do
início é amendment quando a fronteira não muda e HOLD quando muda.

- [ ] **Passo 5: ligar ao validator**

`check_dispatch` extrai o bloco de `templates/task-contract.md`, lê com
`radiant_yaml.load` e valida com os perfis de `agents.json`. `YamlError` e
`ValueError` viram erro com o path do template no começo.

- [ ] **Passo 6: confirmar que passam**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: todos OK; validator em `PASS`.

- [ ] **Passo 7: commit**

```bash
git add validators/ templates/task-contract.md contracts/README.md tests/
git commit -m "feat(contracts): split a task contract into execution units"
```

### Tarefa 4: formato das regras de roteamento

**Files:**
- Create: `docs/routing.md`, `docs/routing.example.json`
- Modify: `validators/dispatch_formats.py`, `validators/check_repository.py`
- Modify: `tests/test_dispatch_formats.py`, `tests/test_repository.py`

**Interfaces:**
- Consumes: `check_dispatch` (Tarefa 2).
- Produces: `dispatch_formats.validate_routing(data: object, adapters:
  Set[str]) -> List[str]`.

Regras: topo com `schema`, `rules` e `default`, sem outras chaves; `schema`
igual a `1`; `rules` é lista, possivelmente vazia; regra com `id`, `when` e
`use` obrigatórios e `approval`, `why` opcionais; `id` no padrão e único;
`when` e `why` strings não vazias; `use` e `default` listas não vazias de
candidatos; candidato com `harness` obrigatório em `adapters`, `capability`
opcional em `CAPABILITIES` e `effort` opcional como string não vazia.

- [ ] **Passo 1: escrever os testes que falham**

Classe `RoutingTests`: o exemplo do ADR-0002 passa com
`{"claude-code", "codex"}`; `harness: copilot` gera erro contendo
`'copilot'`; `approval: "auto"` gera erro contendo `approval`; dois `id`
iguais geram erro contendo `repetido`; `schema: 2` gera erro contendo
`schema`. Em `test_repository.py`,
`test_routing_example_with_unknown_harness_fails` troca o primeiro
`"claude-code"` de `docs/routing.example.json` por `"copilot"` e espera
código 1 com `docs/routing.example.json` no stderr.

- [ ] **Passo 2: confirmar que falham**

Run: `python3 -m unittest tests.test_dispatch_formats tests.test_repository -v`
Expected: FAIL ou ERROR nos testes novos.

- [ ] **Passo 3: implementar `validate_routing` e ligar em `check_dispatch`**

`adapters` são os nomes dos diretórios em `adapters/`.

- [ ] **Passo 4: escrever `docs/routing.md` e o exemplo**

`docs/routing.example.json` é o exemplo da seção 2 do ADR-0002. `docs/routing.md`
explica: a instância é do usuário, no local das restrições globais, gerada pelo
dotfiles e fora de qualquer projeto; o orquestrador escolhe a regra com
julgamento, e o operador só filtra candidatos sem adapter ou sem os
requisitos da unidade (`provides.json`) e pega o primeiro viável; um candidato
nunca usa capacidade abaixo da unidade; `effort` não aceito pelo harness é
registrado e omitido do lançamento; `approval: human` exige confirmação
explícita; cada campo, com o schema da Tarefa 4.

- [ ] **Passo 5: confirmar que passam**

Run: `python3 -m unittest discover -s tests -v && python3 validators/check_repository.py`
Expected: todos OK; validator em `PASS`.

- [ ] **Passo 6: commit**

```bash
git add docs/routing.md docs/routing.example.json validators/ tests/
git commit -m "feat(routing): define user-level routing rules and validate the example"
```

### Tarefa 5: despacho por backend na skill de delegação

**Files:**
- Modify: `skills/radiant-delegation/SKILL.md`

- [ ] **Passo 1: escrever a seção "Despacho por backend"**

Depois de "Paralelismo": despachar por um operador externo é alternativa ao
subagente nativo; o pacote é o caminho do contrato mais o ID da unidade, como
ponteiro, mais revisão e raiz absoluta do Radiant; o orquestrador escolhe a
regra de roteamento, com link para `../../docs/routing.md`, e o operador resolve harness e
modelo; requisitos vêm de `requirements.json`, e o que cada harness oferece,
de `adapters/<harness>/provides.json`; o retorno de Build continua sendo o
Completion report, gravado em `.radiant/reports/<id>.md` no worktree, path que
o consumidor ignora no Git; as regras 1 a 7 não mudam.

- [ ] **Passo 2: atualizar a proveniência e a versão**

Em "Proveniência", a linha por rodada passa a incluir harness e identificador
do despacho quando houver despacho por backend. `metadata.version` vai de
`0.1.1` para `0.2.0`.

- [ ] **Passo 3: verificar**

Run: `python3 validators/check_repository.py && python3 -m unittest discover -s tests -v`
Expected: `PASS` e todos OK; a seção nova não muda os anchors dos papéis
conferidos por `check_delegation`.

- [ ] **Passo 4: commit**

```bash
git add skills/radiant-delegation/SKILL.md
git commit -m "feat(delegation): dispatch execution units through a backend operator"
```

### Tarefa 6: registros de fronteira e estado do ADR

**Files:**
- Modify: `docs/integration.md` (seção "Fronteira Demerzel" depois de
  "Fronteira AIKM")
- Modify: `docs/project-generation-system.md` (nota de estado no topo da
  seção 30)
- Modify: `docs/capabilities.md`, `README.md`, `docs/verification.md`
- Modify: `docs/adrs/ADR-0002-backend-dispatch-demerzel.md`

- [ ] **Passo 1: escrever os registros**

- "Fronteira Demerzel": o Demerzel é um consumidor do Radiant que despacha
  unidades por backend; lê contratos e regras do usuário e grava só seu
  registro de despachos; não altera contratos nem faz merge, push ou mudança
  de escopo; o consumidor que despacha ignora `.radiant/reports/` no Git; o
  Radiant funciona sem ele.
- Nota na seção 30, datada de 2026-10-16, no formato da nota da seção 20: o
  Radiant define como fluxos agênticos são divididos, roteados e aceitos; a
  execução e a observação ficam com harnesses e com um operador externo; o
  texto abaixo permanece como registro da tese 0.2.
- `docs/capabilities.md`: linha "Despachar unidades por backend" apontando
  para a skill de delegação e para `docs/routing.md`.
- `README.md`: linha de `docs/routing.md` na tabela "Encontrar o que precisa".
- `docs/verification.md`: o validator também confere vocabulário, `provides`,
  o exemplo de unidades do template e o exemplo de roteamento, e lê YAML
  restrito sem dependências.
- ADR-0002: emenda de 2026-10-16 registrando que o validator lê o subconjunto
  YAML com `validators/radiant_yaml.py`, a pedido do owner, e que a tabela de
  arquivos previstos inclui `validators/radiant_yaml.py`,
  `validators/dispatch_formats.py`, `contracts/README.md` e os testes novos.

- [ ] **Passo 2: verificar**

Run: `python3 validators/check_repository.py && python3 -m unittest discover -s tests -v && git diff --check`
Expected: `PASS`, todos OK e nenhum aviso de whitespace.

- [ ] **Passo 3: commit**

```bash
git add docs/ README.md
git commit -m "docs: record the Demerzel boundary and backend dispatch"
```

### Tarefa 7: páginas vivas

Executar depois do merge, em `faelplg/design-systems`, pasta
`radiant-design-system/docs/`, conforme o `AGENTS.md` do Radiant.

- [ ] **Passo 1:** atualizar mapa, glossário e casos de uso com unidades de
  execução, requisitos, `provides`, roteamento, despacho por backend e o
  Demerzel como consumidor.
- [ ] **Passo 2:** rodar `build.py --check` e `build.py --artifact <dir>` sem
  erro.
- [ ] **Passo 3:** commit e PR naquele repositório, com aprovação do owner, e
  republicação das três páginas nos URLs atuais.
- [ ] **Passo 4:** no Radiant, o ADR-0002 passa a `accepted` com a referência
  do PR e do commit de merge, como o ADR-0001.

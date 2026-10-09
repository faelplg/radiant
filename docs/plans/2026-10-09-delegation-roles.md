# Papéis, capacidades e delegação: plano de implementação

> **Para agentes executores:** use superpowers:subagent-driven-development
> (recomendado) ou superpowers:executing-plans para executar este plano tarefa
> por tarefa. Os passos usam checkbox (`- [ ]`) para acompanhamento.

**Objetivo:** implementar no Radiant o ADR-0001: papéis e capacidades
agnósticos no core, skill de delegação, skill de manutenção, adapter Claude
Code e adapter Codex delegando a partir do mesmo core.

**Arquitetura:** o core ganha dois corpos procedurais
(`skills/radiant-delegation/`, `skills/radiant-maintenance/`) e um registro
legível por máquina dos perfis delegáveis (`agents.json`). Cada adapter
declara `capabilities.json` (capacidade → ID completo de modelo) e templates;
um gerador único renderiza bootstrap global e subagentes por adapter. Os
validators garantem que core e adapters não divergem.

**Stack:** Python 3.9+ somente com biblioteca padrão, Git, Markdown, JSON e
TOML.

**Spec:** [ADR-0001](../adrs/ADR-0001-delegation-roles.md)

**Fora deste plano:** piloto no AIKM (TC-0019 e TC-0020), instalação dos
subagentes nos diretórios globais do usuário, push e PR. Cada um é uma decisão
separada do owner.

## Restrições globais

- Python 3.9+, sem pacotes externos; testes com `unittest` e comandos reais em
  diretórios temporários, como em `tests/test_integration.py`.
- Textos novos em português, hífen simples, sem travessão e sem divisores
  horizontais.
- Capacidades exatamente `deep`, `standard`, `light`. Campo do contrato:
  `Capability`. `Risk tier` não muda.
- IDs completos de modelo, nunca aliases. Claude Code: `deep` →
  `claude-opus-5-5`, `standard` → `claude-sonnet-5-5`, `light` →
  `claude-haiku-5-5`. Codex: `deep` → `gpt-6-astra`, `standard` →
  `gpt-6.1-sol`, `light` → `gpt-6-luna`.
- Perfis delegáveis e capacidade padrão: `radiant-research` (`light`),
  `radiant-grill` (`deep`), `radiant-design` (`standard`), `radiant-dev`
  (`standard`), `radiant-verifier` (`deep`), `radiant-maintenance`
  (`standard`).
- Arquivos gerados nunca sobrescrevem nem seguem symlinks; uma recusa não
  escreve nenhum arquivo.
- Não editar `docs/repository-report.md` nem corpos em `migration/aikm/`.
- Commits em Conventional Commits, sem coautoria de agente.
- Após cada tarefa: `python3 validators/check_repository.py`,
  `python3 -m unittest discover -s tests -v` e `git diff --check` passam.

## Foco de revisão

1. Raiz do Radiant com espaço e `ç` dentro de TOML e frontmatter YAML: o
   escape precisa produzir arquivos que o harness consegue ler. Teste na
   Tarefa 3 (`tomllib` quando disponível).
2. Um único subagente já existente no destino: nenhum dos seis pode ser
   escrito. Teste na Tarefa 3.
3. `maintenance` apontando para um arquivo ou para symlink que escapa do
   projeto: `HOLD`, mesmo com a regra de aceitar diretório ausente. Teste na
   Tarefa 1.
4. Adapter novo sem `capabilities.json` completo: o validator precisa falhar
   antes de alguém gerar agentes sem modelo. Teste na Tarefa 2.
5. Consumidor antigo sem o campo `maintenance`: continua passando no gate.
   Teste na Tarefa 1.

## Tarefa 1: campo opcional `maintenance` no mapa do consumidor

**Arquivos:**
- Alterar: `validators/check_project.py`
- Alterar: `templates/radiant-project.json`
- Alterar: `docs/integration.md` (seção "Mapa do projeto")
- Teste: `tests/test_integration.py`

**Interfaces:**
- Produz: `.radiant.json` aceita `maintenance` ausente, `null` ou path
  relativo de diretório, que pode não existir.

- [ ] **Passo 1: escrever os testes que falham**

Em `IntegrationTests`:

```python
def test_maintenance_is_optional_and_may_not_exist_yet(self):
    self.config.pop("maintenance", None)
    self.write_map()
    self.assertEqual(self.gate().returncode, 0)
    for value in (None, "ops/maintenance"):
        with self.subTest(value=value):
            self.config["maintenance"] = value
            self.write_map()
            self.assertEqual(self.gate().returncode, 0)
    (self.project / "ops/maintenance").mkdir(parents=True)
    self.assertEqual(self.gate().returncode, 0)

def test_maintenance_rejects_escapes_and_files(self):
    outside = Path(self.temp.name) / "outside-dir"
    outside.mkdir()
    (self.project / "escape-dir").symlink_to(outside)
    (self.project / "report.md").write_text("x\n", encoding="utf-8")
    for value in ("../outside-dir", str(outside), "escape-dir", "report.md", "", ".", 3):
        with self.subTest(value=value):
            self.config["maintenance"] = value
            self.write_map()
            self.assert_hold()
```

- [ ] **Passo 2: rodar e ver falhar**

Run: `python3 -m unittest tests.test_integration -v`
Expected: FAIL nos dois testes novos (campo desconhecido gera `HOLD`).

- [ ] **Passo 3: implementar em `validators/check_project.py`**

`OPTIONAL = ("maintenance",)`. A checagem de campos passa a exigir
`FIELDS <= set(config) <= FIELDS | set(OPTIONAL)`. Para `maintenance`
presente e não nulo: mesma validação de string, absoluto, `..` e contenção
das demais; rejeitar `.` (o projeto inteiro); se o destino existir, precisa
ser diretório; se não existir, aceitar. Adicionar `"maintenance": null` ao
final de `templates/radiant-project.json`.

- [ ] **Passo 4: documentar em `docs/integration.md`**

Na lista do schema, um item: `maintenance`: diretório relativo ignorado pelo
Git ou `null`; opcional; pode não existir, sendo criado pela skill de
manutenção. Citar `skills/radiant-maintenance/SKILL.md` em código; o link
entra na Tarefa 5, quando o arquivo existir. Ajustar a
frase "Todos os campos estão presentes" para excetuar `maintenance`.

- [ ] **Passo 5: rodar os checks globais e ver passar**

- [ ] **Passo 6: commit**

```bash
git add validators/check_project.py templates/radiant-project.json docs/integration.md tests/test_integration.py
git commit -m "feat(integration): accept optional maintenance directory in project map"
```

## Tarefa 2: core de delegação e checagem de adapters

**Arquivos:**
- Criar: `skills/radiant-delegation/SKILL.md`
- Criar: `skills/radiant-delegation/agents.json`
- Criar: `adapters/codex/capabilities.json`
- Criar: `adapters/claude-code/capabilities.json`
- Alterar: `validators/check_repository.py`
- Teste: `tests/test_repository.py` (novo)

**Interfaces:**
- Produz `agents.json`:
  `{"capabilities": ["deep", "standard", "light"], "agents": [{"name": str, "role": str, "capability": str, "description": str}]}`,
  com os seis perfis das restrições globais. `role` é o anchor da seção do
  papel no `SKILL.md`, no formato calculado por `anchors()` do validator
  (`ideação`, `design`, `dev`, `verificador`, `manutenção`;
  `radiant-research` e `radiant-grill` usam `ideação`).
- Produz `adapters/<adapter>/capabilities.json`:
  `{"deep": str, "standard": str, "light": str}` com os IDs das restrições
  globais.
- Produz `check_repository.check_delegation(errors: list) -> None`, chamada
  por `check()`.

- [ ] **Passo 1: escrever os testes que falham**

`tests/test_repository.py`, classe `RepositoryCheckTests`: `setUp` copia o
repositório inteiro para um diretório temporário com
`shutil.copytree(SOURCE, dest, ignore=shutil.ignore_patterns(".git", ".local", "__pycache__"))`
e define `check(self)` rodando `validators/check_repository.py` da cópia com
o helper `run` de `tests/test_integration.py` (copiar o helper; os testes não
importam um ao outro).

```python
def test_current_tree_passes(self):
    self.assertEqual(self.check().returncode, 0)

def test_adapter_missing_a_capability_fails(self):
    path = self.root / "adapters/codex/capabilities.json"
    data = json.loads(path.read_text()); del data["light"]
    path.write_text(json.dumps(data))
    result = self.check()
    self.assertEqual(result.returncode, 1)
    self.assertIn("adapters/codex/capabilities.json", result.stderr)

def test_adapter_without_capabilities_file_fails(self):
    (self.root / "adapters/claude-code/capabilities.json").unlink()
    self.assertEqual(self.check().returncode, 1)

def test_agent_with_unknown_role_or_capability_fails(self):
    for field, value in (("role", "inexistente"), ("capability", "turbo")):
        with self.subTest(field=field):
            path = self.root / "skills/radiant-delegation/agents.json"
            original = path.read_text()
            data = json.loads(original); data["agents"][0][field] = value
            path.write_text(json.dumps(data))
            self.assertEqual(self.check().returncode, 1)
            path.write_text(original)
```

- [ ] **Passo 2: rodar e ver falhar**

Run: `python3 -m unittest tests.test_repository -v`
Expected: FAIL (arquivos e checagem ainda não existem).

- [ ] **Passo 3: escrever `skills/radiant-delegation/SKILL.md`**

Frontmatter: `name: radiant-delegation`, `description` (quando usar:
orquestrar papéis, delegar trabalho delimitado, escolher capacidade),
`metadata.version: "0.1.0"`. Seções, nesta ordem, com o conteúdo das seções 1
e 2 do ADR, sem copiar o ADR inteiro e sem citar modelos: `## Capacidades`,
`## Papéis` com `### Orquestrador`, `### Ideação`, `### Design`, `### Dev`,
`### Verificador`, `### Manutenção`, `## Regras` (as sete regras),
`## Pacote de delegação`, `## Retorno`, `## Paralelismo`, `## Proveniência`.
A seção de cada papel diz o que lê, o que produz, a capacidade padrão, o que
não pode decidir e como retorna. Linkar a Constitution, o template de Task
Contract e `agents.json`. A seção `### Manutenção` aponta para
`skills/radiant-maintenance/SKILL.md` em código (link entra na Tarefa 5).

- [ ] **Passo 4: criar `agents.json` e os dois `capabilities.json`**

Descrições curtas em português, uma frase cada, dizendo quando o orquestrador
usa o perfil.

- [ ] **Passo 5: implementar `check_delegation` em `validators/check_repository.py`**

Erros, cada um nomeando o arquivo: `capabilities` diferente de
`["deep", "standard", "light"]`; nome de agente repetido ou sem prefixo
`radiant-`; `capability` fora da lista; `role` ausente de
`anchors(SKILL.md)`; diretório em `adapters/` sem `capabilities.json`, com
chaves diferentes das capacidades ou com valor que não seja string não vazia.

- [ ] **Passo 6: rodar os checks globais e ver passar**

- [ ] **Passo 7: commit**

```bash
git add skills/radiant-delegation adapters/codex/capabilities.json adapters/claude-code/capabilities.json validators/check_repository.py tests/test_repository.py
git commit -m "feat(delegation): add roles, capabilities and adapter consistency check"
```

## Tarefa 3: gerador único de bootstrap e subagentes

**Arquivos:**
- Mover: `adapters/codex/render_bootstrap.py` → `adapters/render_bootstrap.py`
- Criar: `adapters/claude-code/global.CLAUDE.template.md`
- Criar: `adapters/claude-code/agent.template.md`
- Criar: `adapters/codex/agent.template.toml`
- Alterar: `adapters/codex/README.md` (comandos)
- Teste: `tests/test_integration.py`

**Interfaces:**
- Consome: `agents.json` e `capabilities.json` da Tarefa 2.
- Produz CLI:
  `python3 adapters/render_bootstrap.py --adapter {codex,claude-code} [--output FILE | --agents-dir DIR]`.
  `--adapter` é obrigatório. Sem `--output` nem `--agents-dir`, imprime o
  bloco global. `--agents-dir` escreve `<name>.md` (Claude Code) ou
  `<name>.toml` (Codex) para os seis perfis.
- Produz funções: `render_global(root: Path, adapter: str) -> str`,
  `render_agents(root: Path, adapter: str) -> dict[str, str]` (nome do
  arquivo → conteúdo), `write_exclusive(files: dict[Path, str]) -> None`
  (verifica todos os destinos antes de escrever qualquer um).
- Placeholders dos templates, todos substituídos por `json.dumps(...,
  ensure_ascii=False)`: `{{RADIANT_ROOT_JSON}}`, `{{NAME_JSON}}`,
  `{{DESCRIPTION_JSON}}`, `{{MODEL_JSON}}`, `{{INSTRUCTIONS_JSON}}`; e
  `{{INSTRUCTIONS}}`, o mesmo texto sem escape, para o corpo Markdown. As
  instruções do agente são montadas pelo gerador: papel, path absoluto de
  `skills/radiant-delegation/SKILL.md`, anchor do papel, a ordem "leia a
  seção do seu papel e o pacote recebido; não delegue; retorne no formato da
  seção Retorno".

- [ ] **Passo 1: escrever os testes que falham**

Trocar o helper `render` para `adapters/render_bootstrap.py` e adicionar
`--adapter codex` no teste existente de saída global. Testes novos:

```python
def test_adapter_is_required(self):
    self.assertNotEqual(self.render().returncode, 0)

def test_codex_global_block_is_unchanged(self):
    template = (self.root / "adapters/codex/global.AGENTS.template.md").read_text()
    expected = template.replace("{{RADIANT_ROOT_JSON}}", json.dumps(str(self.root), ensure_ascii=False))
    self.assertEqual(self.render("--adapter", "codex").stdout, expected)

def test_claude_global_block_points_to_claude_adapter(self):
    out = self.render("--adapter", "claude-code").stdout
    self.assertIn("radiant:begin", out); self.assertIn("radiant:end", out)
    self.assertIn("adapters/claude-code/README.md", out)
    self.assertIn(str(self.root), out); self.assertLess(len(out.encode()), 1024)

def test_agents_render_one_file_per_profile(self):
    agents = json.loads((self.root / "skills/radiant-delegation/agents.json").read_text())["agents"]
    for adapter, ext in (("claude-code", ".md"), ("codex", ".toml")):
        with self.subTest(adapter=adapter):
            models = json.loads((self.root / f"adapters/{adapter}/capabilities.json").read_text())
            target = self.project / f"agents-{adapter}"
            self.assertEqual(self.render("--adapter", adapter, "--agents-dir", str(target)).returncode, 0)
            self.assertEqual(sorted(p.name for p in target.iterdir()),
                             sorted(a["name"] + ext for a in agents))
            for agent in agents:
                text = (target / (agent["name"] + ext)).read_text()
                self.assertIn(models[agent["capability"]], text)
                self.assertIn(str(self.root / "skills/radiant-delegation/SKILL.md"), text)
                self.assertNotIn(str(SOURCE), text)
                if adapter == "claude-code":
                    self.assertTrue(text.startswith("---\n"))
                    self.assertIn("disallowedTools: Agent", text)

@unittest.skipUnless(tomllib, "tomllib requer Python 3.11+")
def test_codex_agents_are_valid_toml(self):
    target = self.project / "agents"
    self.render("--adapter", "codex", "--agents-dir", str(target))
    for path in target.iterdir():
        data = tomllib.loads(path.read_text())
        self.assertEqual({"name", "description", "model", "developer_instructions"}, set(data))
        self.assertIn(str(self.root), data["developer_instructions"])

def test_agents_refuse_any_existing_or_symlinked_target(self):
    target = self.project / "agents"; target.mkdir()
    (target / "radiant-dev.md").write_text("keep\n")
    self.assertNotEqual(self.render("--adapter", "claude-code", "--agents-dir", str(target)).returncode, 0)
    self.assertEqual([p.name for p in target.iterdir()], ["radiant-dev.md"])
    self.assertEqual((target / "radiant-dev.md").read_text(), "keep\n")
    (target / "radiant-dev.md").unlink()
    (target / "radiant-grill.md").symlink_to(self.project / "elsewhere.md")
    self.assertNotEqual(self.render("--adapter", "claude-code", "--agents-dir", str(target)).returncode, 0)
    self.assertFalse((self.project / "elsewhere.md").exists())
```

No topo do arquivo: `try: import tomllib` / `except ImportError: tomllib = None`.

- [ ] **Passo 2: rodar e ver falhar**

Run: `python3 -m unittest tests.test_integration -v`
Expected: FAIL (script ainda no path antigo e sem `--adapter`).

- [ ] **Passo 3: mover e generalizar o gerador**

`git mv adapters/codex/render_bootstrap.py adapters/render_bootstrap.py`;
`root = Path(__file__).resolve().parents[1]`. Tabela interna por adapter:
template global, template de agente e extensão. `--output` e `--agents-dir`
mutuamente exclusivos. Recusa com mensagem em português e saída 1, no mesmo
estilo da atual.

- [ ] **Passo 4: criar os templates**

`global.CLAUDE.template.md`: mesmo formato do bloco Codex, apontando para
`adapters/claude-code/README.md` e `docs/capabilities.md`.
`agent.template.md`: frontmatter `name`, `description`, `model`,
`disallowedTools: Agent`, corpo `{{INSTRUCTIONS}}`.
`agent.template.toml`: as quatro chaves, valores via placeholders `_JSON`.

- [ ] **Passo 5: atualizar comandos em `adapters/codex/README.md`**

`python3 adapters/render_bootstrap.py --adapter codex` e a variante com
`--output .local/codex-global.md`.

- [ ] **Passo 6: rodar os checks globais e ver passar**

- [ ] **Passo 7: commit**

```bash
git add adapters tests/test_integration.py
git commit -m "feat(adapters): render bootstrap and subagents for codex and claude code"
```

## Tarefa 4: documentação dos adapters e mapa neutro do consumidor

**Arquivos:**
- Criar: `adapters/claude-code/README.md`
- Alterar: `adapters/codex/README.md`
- Mover: `adapters/codex/project.AGENTS.template.md` → `templates/project-agents.md`
- Criar: `CLAUDE.md` (raiz)
- Alterar: `templates/README.md`, `migration/README.md` (link do template, linha 28), `AGENTS.md`, `README.md`, `docs/capabilities.md`, `docs/integration.md`

**Interfaces:**
- Consome: CLI da Tarefa 3, `capabilities.json` da Tarefa 2.
- Produz: `templates/project-agents.md` neutro de harness; `CLAUDE.md` com
  exatamente uma linha `@AGENTS.md`.

- [ ] **Passo 1: escrever `adapters/claude-code/README.md`**

Mesma estrutura do README Codex (Entrada do agente, Configurar o usuário,
Configurar o consumidor) mais: Capacidades (link para `capabilities.json`, sem
repetir IDs), Subagentes (gerar com `--agents-dir` para o diretório de
agentes do usuário; regenerar após mudar IDs; override pelo parâmetro `model`
da invocação; `disallowedTools: Agent`), Manutenção local (tarefa agendada na
máquina; nuvem fora de escopo), Procedimentos externos opcionais (tabela papel
→ skill sugerida, com a regra de saída nos paths do `.radiant.json`),
desfazer (remover bloco e os seis arquivos `radiant-*`).

- [ ] **Passo 2: atualizar `adapters/codex/README.md`**

Seções Capacidades e Subagentes análogas; registrar que o `model` do arquivo
prevalece, logo override roda na sessão do orquestrador; regra 7 nas
instruções do agente. Trocar o link do template de consumidor para
`../../templates/project-agents.md`.

- [ ] **Passo 3: mover e neutralizar o template de consumidor**

`git mv adapters/codex/project.AGENTS.template.md templates/project-agents.md`.
Trocar "leia `adapters/codex/README.md`" por "leia o README do adapter do
harness em uso em `adapters/<harness>/`". Acrescentar: consumidores em Claude
Code criam `CLAUDE.md` com a linha `@AGENTS.md`.

- [ ] **Passo 4: `CLAUDE.md`, índices e mapas**

`CLAUDE.md` na raiz com `@AGENTS.md`. `AGENTS.md`: citar os dois adapters e a
skill de delegação. `README.md`: linhas para `skills/radiant-delegation`,
`adapters/claude-code/` e `docs/adrs/`. `docs/capabilities.md`: linhas
"Orquestrar papéis e delegar" e "Configurar harness". `docs/integration.md`:
"adapter Codex" vira "adapters" onde a frase for genérica. `templates/README.md`
e `migration/README.md`: novo path do template.

- [ ] **Passo 5: rodar os checks globais e ver passar**

Expected adicional: `check_repository.py` sem link quebrado após o move.

- [ ] **Passo 6: commit**

```bash
git add -A adapters templates CLAUDE.md AGENTS.md README.md docs migration/README.md
git commit -m "docs(adapters): add claude code adapter and harness-neutral consumer map"
```

## Tarefa 5: manutenção, contrato e ponteiros do ciclo

**Arquivos:**
- Criar: `skills/radiant-maintenance/SKILL.md`
- Criar: `templates/maintenance-report.md`
- Alterar: `templates/task-contract.md`, `skills/radiant-cycle/SKILL.md`,
  `skills/radiant-delegation/SKILL.md`, `docs/integration.md`,
  `docs/learn-back.md`, `docs/verification.md`, `templates/README.md`,
  `docs/capabilities.md`

**Interfaces:**
- Consome: campo `maintenance` (Tarefa 1), seção `### Manutenção` (Tarefa 2).
- Produz: campo `Capability` no Task Contract; formato do relatório.

- [ ] **Passo 1: escrever `skills/radiant-maintenance/SKILL.md`**

Frontmatter como na Tarefa 2. Conteúdo da seção 3 do ADR: entrada (ler
`.radiant.json`, workflow e seção de Manutenção; sem `maintenance`, `HOLD`),
fontes, política declarada (comandos seguros, egress autorizado, omissões
registradas), priorização por risco, valor e reversibilidade, comparação com o
relatório anterior, até três rascunhos embutidos, fronteira (única escrita: o
relatório; criar o diretório se ausente; sem branch, PR, issue ou commit),
capacidades (`light` coleta, `standard` priorização e orquestrador), "nada
material" como resultado válido. Linkar a skill de delegação e o template.

- [ ] **Passo 2: escrever `templates/maintenance-report.md`**

Metadados (data, revisão do Radiant, commit do consumidor, capacidade e
modelo efetivos), Fontes (consultada, pulada por política, falhou),
Candidatos (tabela: ID local, categoria, evidência, risco, valor,
reversibilidade, estado novo/recorrente/resolvido), Rascunhos (até três:
objetivo, outputs, verificação), Omissões e limitações.

- [ ] **Passo 3: campo `Capability` no Task Contract**

Em `templates/task-contract.md`, após `Risk tier`:
`**Capability:** \`default | deep | standard | light\` - justificativa em uma linha quando diferente de default`.
Na seção 16, sem mudança de formato: uma nota de que ele é o retorno do Build
pela skill de delegação.

- [ ] **Passo 4: ponteiros**

`radiant-cycle`: na entrada, "para coordenar papéis e delegar, leia
radiant-delegation"; em Verificar, ponteiro para a regra de aceite;
incrementar `metadata.version` para `0.1.3`. `radiant-delegation`: trocar o
path em código pelo link para a skill de manutenção. `docs/integration.md`:
trocar o path em código pelo link. `docs/learn-back.md`: linhas para
`skills/radiant-delegation/`, `skills/radiant-maintenance/` e
`adapters/claude-code/`. `docs/verification.md`: simulação D (sessão nova no
Claude Code encontra bootstrap, adapter, pin, Constitution e skill de
delegação) e linha "Agnosticismo de harness" na tabela. `templates/README.md`
e `docs/capabilities.md`: entrada do relatório de manutenção.

- [ ] **Passo 5: rodar os checks globais e ver passar**

- [ ] **Passo 6: commit**

```bash
git add skills templates docs
git commit -m "feat(maintenance): add propose-only maintenance skill and report template"
```

## Tarefa 6: verificação final da entrega

**Arquivos:**
- Alterar: `docs/adrs/ADR-0001-delegation-roles.md` somente se a verificação
  revelar divergência material com a implementação.

- [ ] **Passo 1: checks completos**

```bash
python3 validators/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check origin/main...HEAD
```

Expected: PASS e todos os testes OK; nenhum aviso de espaço.

- [ ] **Passo 2: readback dos artefatos gerados**

Gerar os dois conjuntos de agentes e os dois blocos globais em um diretório do
scratchpad e reler cada arquivo: modelo correto por capacidade, path do
checkout real, instruções sem regras copiadas. Não instalar em diretórios
globais.

- [ ] **Passo 3: simulações A a D de `docs/verification.md`**

Percorrer cada simulação a partir da raiz e registrar no resumo da entrega os
paths efetivamente alcançados.

- [ ] **Passo 4: cobertura do ADR**

Conferir a tabela "Arquivos previstos" do ADR contra `git diff --stat
origin/main...HEAD`. Item faltante: voltar à tarefa dona. Item a mais:
justificar ou remover.

- [ ] **Passo 5: relatar**

Estado `DONE`, `HOLD` ou `FAIL`, comandos e resultados, limitações (testes não
provam obediência de modelo; sessão real fica para o piloto) e próximos passos
que dependem do owner: push, PR, instalação dos subagentes e TC-0019 no AIKM.

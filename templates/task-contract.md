# Radiant — Task Contract Template

**Versão:** 0.2  
**Status:** Template operacional  
**Base:** Radiant Project Generation System v0.2 + Radiant Engineering Baseline v0.1

> Use este template para trabalho de implementação agêntica relevante.  
> Remova seções que forem claramente `N/A`.  
> O contrato deve permanecer bounded.

---

# Radiant Task Contract — [Project] — [Iteration / Task]

**Contract ID:** `[id]`  
**Project:** `[project]`  
**Iteration:** `[iteration]`  
**Status:** `READY | HOLD | IN_PROGRESS | VERIFY | DONE | FAIL`  
**Owner:** `[human/agent]`  
**Risk tier:** `0 | 1 | 2 | 3`  
**Engineering Baseline:** `Radiant Engineering Baseline v0.1`  
**Engineering Profile:** `[project profile/version | none]`

---

## 1. Objective

Descreva uma única mudança observável.

> **[O que deve passar a ser verdadeiro quando esta tarefa terminar?]**

---

## 2. Why this task exists

Referencie a intenção superior sem reescrever o projeto.

**Source plan/spec:**

- `[document / section]`

**Hypothesis or risk reduced:**

- `[what uncertainty this task reduces]`

---

## 3. Inputs

O agente pode assumir como input:

- `[file / spec / decision]`
- `[existing code / command]`
- `[other required context]`

Não inferir inputs ausentes que mudariam materialmente a solução.

---

## 4. Allowed scope

### Paths allowed to change

```text
[path]
[path]
```

### Paths read-only

```text
[path]
```

### External systems allowed

- `[none / list]`

### Network

`DENIED | ALLOWED FOR: [purpose]`

---

## 5. Required outputs

Ao final, devem existir exatamente os outputs necessários:

1. `[output]`
2. `[output]`
3. `[tests / docs / ADR only if applicable]`

Não criar artefatos adicionais sem necessidade observada.

---

## 6. Non-goals

Esta tarefa **não** deve:

- `[non-goal]`
- `[non-goal]`
- `[non-goal]`

Encontrar uma melhoria fora deste escopo não autoriza implementá-la.

Registre-a como observação ou Learn Back candidate.

---

# 7. Functional requirements

- [ ] `[behavior]`
- [ ] `[behavior]`
- [ ] `[error/edge case]`

---

# 8. Engineering Check

Aplicar somente o que é relevante para esta tarefa.

| Baseline                       | Status           | Aplicação nesta tarefa | Evidência         |
| ------------------------------ | ---------------- | ---------------------- | ----------------- |
| EB-01 Complexidade deliberada  | `REQUIRED / N/A` | `[constraint]`         | `[how checked]`   |
| EB-02 Correção e contratos     | `REQUIRED / N/A` | `[invariant/error]`    | `[test/readback]` |
| EB-03 Verificação e testes     | `REQUIRED / N/A` | `[test strategy]`      | `[command]`       |
| EB-04 Segurança e privacidade  | `REQUIRED / N/A` | `[security boundary]`  | `[test/review]`   |
| EB-05 Manutenibilidade         | `REQUIRED / N/A` | `[specific concern]`   | `[review]`        |
| EB-06 Dependências             | `REQUIRED / N/A` | `[dependency rule]`    | `[lock/ADR]`      |
| EB-07 Diagnóstico              | `REQUIRED / N/A` | `[error behavior]`     | `[test/readback]` |
| EB-08 Experiência e eficiência | `REQUIRED / N/A` | `[UX/perf]`            | `[demo/test]`     |

### N/A justification

Registre somente itens marcados `N/A` cuja ausência não seja óbvia:

- `[EB-xx: reason]`

---

# 9. Project-specific constraints

Extraídas do Engineering Profile ou Spec:

- `[constraint]`
- `[constraint]`
- `[constraint]`

Não duplicar todo o Profile.

---

# 10. Dependency policy

### New runtime dependency allowed?

`NO | YES, only if condition below is met`

Se uma nova dependência for proposta, registrar:

- problema concreto;
- alternativa sem dependência;
- custo operacional;
- risco de filesystem/rede/execução;
- decisão final.

Se a dependência alterar arquitetura ou distribuição, criar ADR.

---

# 11. Verification plan

A verificação deve ser definida antes do Build.

## Automated

```text
[command: unit/integration tests]
[command: lint]
[command: typecheck]
[command: build]
```

Remover comandos não aplicáveis.

## Focused verification

- `[acceptance test]`
- `[security case]`
- `[error case]`

## Readback

Após a execução:

- reabrir arquivos gerados/modificados relevantes;
- verificar que o output persistido é o esperado;
- confirmar que nenhum path fora do escopo foi alterado.

## Independent critique

`REQUIRED | OPTIONAL | N/A`

Quando required:

- `[second agent / human / verification skill]`

---

# 12. Acceptance criteria

A tarefa só pode ser declarada `DONE` quando:

- [ ] `[observable criterion]`
- [ ] `[observable criterion]`
- [ ] todos os checks aplicáveis da seção 11 passam;
- [ ] não houve mudança fora do Allowed scope;
- [ ] limitações relevantes estão registradas;
- [ ] a evidência final foi lida, não apenas presumida pelo exit code.

---

# 13. HOLD conditions

Interromper e solicitar decisão quando:

- o comportamento exigido contradiz Spec/Constitution;
- uma ação destrutiva não prevista se torna necessária;
- um secret real é necessário e não existe mecanismo autorizado;
- uma nova dependência estrutural é necessária;
- o agente precisaria escrever fora dos paths autorizados;
- a tarefa exigiria egress não autorizado;
- a solução mínima deixou de caber no contrato;
- um requisito crítico é ambíguo e diferentes interpretações mudariam a arquitetura.

`HOLD` é resultado válido.

---

# 14. FAIL conditions

Marcar `FAIL` quando:

- acceptance criteria não podem ser satisfeitos;
- verificação demonstra regressão material;
- segurança não pode ser preservada;
- a implementação produz estado inconsistente;
- um blocker externo torna o objetivo impossível dentro deste contrato.

Não mascarar `FAIL` como `DONE WITH NOTES`.

---

# 15. Change budget

O agente pode:

- refatorar localmente código diretamente necessário;
- remover código tornado obsoleto pela própria mudança;
- atualizar testes e documentação diretamente afetados.

O agente não pode, sem HOLD:

- redesenhar arquitetura ampla;
- mudar stack;
- trocar biblioteca estrutural;
- mover grandes áreas do projeto;
- resolver dívida técnica adjacente;
- adicionar features não solicitadas.

---

# 16. Completion report

Ao finalizar, responder de forma curta com:

### Status

`DONE | HOLD | FAIL`

### Changed

- `[what changed]`

### Verification evidence

```text
[commands and results]
```

### Engineering notes

- `[relevant trade-off or N/A]`

### Remaining limitations

- `[known limitation or none]`

### Learn Back candidate

- `[what this task taught that may deserve change elsewhere, or none]`

---

# 17. Completion rule

> **Não declarar DONE porque o código parece correto. Declarar DONE apenas quando os critérios observáveis, a engenharia aplicável e a evidência de verificação convergirem.**

# Regras de roteamento

Uma unidade de execução declara papel, capacidade e requisitos, nunca harness
ou modelo. As regras de roteamento dizem em qual harness cada tipo de unidade
roda. A decisão que as criou está no
[ADR-0002](adrs/ADR-0002-backend-dispatch-demerzel.md).

## Onde ficam

A instância é do usuário: `$XDG_CONFIG_HOME/radiant/routing.json`, ou
`~/.config/radiant/routing.json` sem a variável. Ela é gerada pelo gerenciador
de configuração da máquina, como o dotfiles, e fica fora de qualquer projeto,
porque harnesses instalados e assinaturas são fatos da máquina. O Radiant
define o formato e mantém um [exemplo](routing.example.json), conferido pelo
validator.

## Como são aplicadas

1. O orquestrador escolhe, com julgamento, a regra cujo `when` descreve a
   unidade. Sem regra adequada, usa `default`.
2. O operador de despacho percorre os candidatos de `use` em ordem e descarta
   os que não têm adapter Radiant ou cujo
   `adapters/<harness>/provides.json` não cobre os `requires` da unidade.
3. O primeiro candidato viável vence. O modelo vem do `capabilities.json` do
   adapter, para a capacidade da unidade ou a do candidato.
4. A decisão é registrada antes do lançamento e não é relida depois.

Um candidato nunca usa capacidade abaixo da pedida pela unidade. Sem candidato
viável, a unidade fica em `HOLD`. Um `effort` que o harness não aceita é
registrado e omitido do lançamento. Uma regra com `approval: human` só despacha
com confirmação explícita do humano.

## Formato

| Campo | Regra |
| --- | --- |
| `schema` | Exatamente `1` |
| `rules` | Lista de regras, possivelmente vazia |
| `rules[].id` | Kebab-case, único |
| `rules[].when` | Condição em linguagem natural, não vazia |
| `rules[].use` | Lista não vazia de candidatos, em ordem de preferência |
| `rules[].approval` | Opcional; só aceita `"human"` |
| `rules[].why` | Opcional; motivo que ajuda a escolher |
| `default` | Lista não vazia de candidatos para unidades sem regra |
| candidato `harness` | Obrigatório; nome de um diretório em `adapters/` |
| candidato `capability` | Opcional; `deep`, `standard` ou `light` |
| candidato `effort` | Opcional; nível de raciocínio pedido ao harness |

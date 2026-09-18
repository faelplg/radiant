# Radiant — Engineering Baseline

**Versão:** 0.1  
**Status:** Baseline operacional inicial  
**Natureza:** Padrão de engenharia do Radiant  
**Aplicação:** Projetos construídos pelo Radiant  
**Princípio:** Engenharia proporcional ao risco, impacto e reversibilidade

---

## 1. Objetivo

O **Radiant Engineering Baseline** define o conjunto mínimo de expectativas de engenharia que deve orientar implementação e verificação dos projetos conduzidos pelo Radiant.

Ele existe para evitar que agentes precisem inferir, a cada iteração, o que significa “boa engenharia”.

O Baseline não é:

- um style guide universal;
- uma lista fixa de tecnologias;
- uma exigência de arquitetura complexa;
- uma coleção de dogmas como “usar SOLID em todo lugar”;
- um substituto para julgamento técnico.

Ele define **resultados esperados e limites mínimos**.

A forma de atendê-los depende do projeto.

> **O Baseline estabelece o mínimo. O Engineering Profile contextualiza. O Task Contract aplica. O Verify produz evidência.**

---

## 2. Regra de proporcionalidade

Nem toda regra precisa da mesma profundidade em toda tarefa.

A aplicação deve considerar:

- impacto da mudança;
- custo de reversão;
- exposição externa;
- manipulação de dados;
- superfície de segurança;
- durabilidade do código;
- criticidade operacional;
- quantidade de usuários ou sistemas afetados.

Cada item do Baseline pode ser marcado em um Task Contract como:

- `REQUIRED`;
- `APPLICABLE`;
- `N/A`, com justificativa curta.

`N/A` não significa que a regra foi esquecida.

Significa que sua não aplicação foi deliberada.

---

# 3. EB-01 — Complexidade deliberada

## Regra

> **Implementar a menor solução que satisfaça os contratos atuais sem antecipar arquitetura que ainda não possui evidência de necessidade.**

### Esperado

- evitar abstrações especulativas;
- evitar infraestrutura sem consumidor atual;
- evitar generalização baseada em um único caso;
- manter limites de módulo compreensíveis;
- preferir decisões reversíveis enquanto a incerteza for alta;
- tornar aumento de complexidade uma decisão explícita.

### Sinais de violação

- framework introduzido apenas porque “pode ser útil depois”;
- camada intermediária sem comportamento próprio;
- abstração que torna o fluxo mais difícil de compreender;
- banco, fila, cache, serviço ou integração adicionados antes de existir uma limitação observada;
- duplicação de arquitetura para suportar cenários não previstos no escopo atual.

### Evidência possível

- diff pequeno e localizado;
- ADR quando uma decisão estrutural relevante for necessária;
- justificativa explícita de nova dependência ou infraestrutura;
- remoção de código ou abstração quando ela não se provou necessária.

---

# 4. EB-02 — Correção e contratos explícitos

## Regra

> **Comportamentos importantes devem possuir contratos observáveis e falhar de forma compreensível quando invariantes forem violadas.**

### Esperado

- invariantes relevantes representadas em código, schema ou testes;
- validação nas fronteiras do sistema;
- estados inválidos rejeitados cedo quando razoável;
- erros não tratados não devem ser usados como fluxo normal;
- operações destrutivas ou mutáveis devem possuir semântica clara;
- idempotência deve ser buscada quando a operação puder ser repetida com segurança.

### Sinais de violação

- comportamento depende de estado implícito não documentado;
- entrada inválida é silenciosamente aceita;
- erro é engolido sem evidência;
- uma operação parcialmente concluída deixa estado ambíguo;
- contrato descrito na spec diverge do comportamento real sem atualização da documentação.

### Evidência possível

- schema validation;
- testes de invariantes;
- casos de erro;
- readback;
- atualização de Spec ou ADR quando o contrato muda.

---

# 5. EB-03 — Verificação e testes orientados por risco

## Regra

> **Toda mudança deve possuir uma forma proporcional de demonstrar que o comportamento esperado funciona e que regressões relevantes foram evitadas.**

### Esperado

- testar comportamento, não implementação acidental;
- corrigir bugs com teste de regressão quando razoável;
- utilizar teste unitário, integração, contrato ou ponta a ponta conforme a fronteira que precisa ser provada;
- não depender exclusivamente do agente que implementou para declarar conclusão;
- executar readback quando arquivos ou artefatos são gerados;
- manter a suíte rápida o suficiente para ser usada continuamente.

### Não é exigido

- 100% de cobertura;
- E2E para toda feature;
- snapshots extensos;
- mocks que reproduzem internamente toda dependência.

### Evidência mínima

O Task Contract deve declarar:

1. o que precisa ser provado;
2. como será provado;
3. qual comando ou procedimento produz a evidência.

---

# 6. EB-04 — Segurança, privacidade e controle de dados

## Regra

> **A solução deve operar com o menor acesso necessário e tratar secrets, dados privados e egress como fronteiras explícitas.**

### Esperado

- secrets fora do código e de artefatos comuns;
- validação de input em fronteiras relevantes;
- princípio de menor privilégio;
- default deny quando uma permissão sensível for ambígua;
- distinção entre leitura local e autorização de egress;
- paths, comandos e operações destrutivas tratados como superfícies de segurança;
- dados sensíveis não devem aparecer em logs, mensagens de erro ou fixtures reais;
- dependências que executam código ou acessam rede devem receber escrutínio proporcional.

### Elevação de rigor

Mudanças que afetem:

- autenticação;
- autorização;
- egress;
- secrets;
- produção;
- dados pessoais;
- execução remota;
- acesso ao filesystem fora da raiz autorizada;

devem receber verificação específica de segurança.

---

# 7. EB-05 — Manutenibilidade e legibilidade

## Regra

> **O próximo humano ou agente deve conseguir compreender a intenção do código sem reconstruir desnecessariamente o raciocínio que o criou.**

### Esperado

- nomes descritivos;
- módulos coesos;
- interfaces pequenas;
- fluxo de controle compreensível;
- comentários explicando decisões não óbvias, não recontando o código;
- remoção de código morto;
- duplicação tolerada quando abstrair cedo seria pior;
- abstração quando repetição real já revela um conceito estável;
- convenções do ecossistema adotadas por padrão.

### Sobre princípios conhecidos

SOLID, Clean Code, Clean Architecture, DRY, KISS e padrões de projeto são referências úteis.

Nenhum deles deve ser aplicado mecanicamente.

A decisão correta é a que melhora clareza, correção, capacidade de mudança e verificabilidade no contexto real.

---

# 8. EB-06 — Dependências e cadeia de suprimentos

## Regra

> **Toda dependência aumenta capacidade e também superfície de manutenção, segurança e compatibilidade.**

### Esperado

- introduzir dependência apenas quando seu valor superar claramente o custo de possuir a dependência;
- utilizar lockfile ou mecanismo equivalente quando o ecossistema oferecer;
- evitar dependências abandonadas ou desnecessariamente privilegiadas;
- preferir bibliotecas pequenas e maduras para problemas pequenos;
- registrar dependências estruturalmente importantes em ADR ou documentação equivalente;
- atualizar dependências de forma deliberada e verificável;
- não copiar código de procedência desconhecida para o projeto.

### Antes de uma nova dependência relevante

Perguntar:

1. o runtime ou biblioteca padrão já resolve?
2. qual problema concreto ela elimina?
3. qual é o custo de removê-la depois?
4. ela executa código, acessa filesystem ou rede?
5. existe alternativa menor?

---

# 9. EB-07 — Operabilidade, diagnóstico e observabilidade

## Regra

> **Quando algo falhar, o sistema deve fornecer informação suficiente para localizar o problema sem exigir adivinhação.**

### Esperado

- erros acionáveis;
- exit codes consistentes quando houver CLI;
- logs apenas quando ajudam a operar ou diagnosticar;
- nenhuma telemetria obrigatória sem decisão explícita;
- nenhuma informação sensível em logs;
- correlação entre erro, operação e recurso afetado quando relevante;
- métricas, tracing e dashboards somente quando o tipo de sistema justificar.

### Proporcionalidade

Uma CLI local pode precisar apenas de:

- mensagens de erro claras;
- paths;
- IDs;
- regra violada;
- ação sugerida.

Um serviço distribuído pode exigir observabilidade substancialmente maior.

---

# 10. EB-08 — Qualidade de experiência e eficiência

## Regra

> **O sistema deve respeitar o tempo, a capacidade e as limitações de quem o utiliza.**

### Para interfaces humanas

Considerar, quando aplicável:

- clareza;
- feedback;
- prevenção e recuperação de erro;
- acessibilidade;
- teclado e leitores de tela;
- estados de loading e falha;
- linguagem compreensível.

### Para CLI e APIs

Considerar:

- `--help` útil;
- comandos previsíveis;
- output scriptable quando necessário;
- mensagens estáveis o suficiente para automação quando declaradas como interface;
- exit codes adequados;
- operações seguras por padrão.

### Para performance e recursos

- não otimizar sem evidência;
- evitar algoritmos obviamente inadequados ao volume esperado;
- medir antes de introduzir infraestrutura de performance;
- evitar trabalho, rede, armazenamento ou processamento que não gere valor observável.

---

# 11. Engineering Profile por projeto

Cada projeto pode possuir um **Engineering Profile** que contextualiza este Baseline.

O Profile pode definir:

- risco padrão do projeto;
- stack e convenções;
- qualidade mínima por tipo de mudança;
- estratégia de testes;
- política de dependências;
- fronteiras de segurança;
- requisitos específicos de UX;
- requisitos de performance;
- requisitos de compatibilidade;
- comandos de verificação.

O Profile não deve duplicar o Baseline.

Ele registra apenas aquilo que é específico daquele projeto.

---

# 12. Integração com Task Contracts

Todo Task Contract de implementação deve referenciar:

- esta versão do Engineering Baseline;
- o Engineering Profile do projeto, quando existir.

O contrato não precisa copiar as regras.

Ele deve declarar apenas:

- quais regras são especialmente relevantes;
- quais possuem adaptação específica;
- quais são `N/A`;
- qual evidência será produzida.

---

# 13. Integração com Verify

Verify deve avaliar duas coisas separadamente:

### Product correctness

> O comportamento solicitado foi entregue?

### Engineering integrity

> A implementação respeitou as restrições de engenharia aplicáveis?

Uma feature pode funcionar e ainda falhar no segundo critério.

Da mesma forma, uma implementação tecnicamente elegante que não cumpre a hipótese ou acceptance criteria também falha.

---

# 14. Learn Back

Quando uma falha de engenharia for observada, o Learn Back deve identificar o nível correto.

Exemplos:

- regra ausente para todos os projetos → atualizar Engineering Baseline;
- regra específica do AIKM → atualizar AIKM Engineering Profile;
- instrução insuficiente em uma única iteração → atualizar Task Contract;
- verificação que não detectou regressão → atualizar procedimento de Verify;
- falha recorrente de implementação → criar ou atualizar skill/validator.

O Baseline não deve crescer a cada erro isolado.

Uma regra só deve entrar aqui quando for:

- recorrente;
- aplicável a múltiplos projetos;
- verificável;
- mais barata do que o retrabalho que evita.

---

# 15. Regra final

> **Radiant não deve substituir engenharia por geração. Deve transformar engenharia em uma restrição explícita, proporcional e verificável do processo de geração.**

O objetivo deste Baseline é permitir que agentes tenham autonomia para implementar sem receber liberdade para redefinir silenciosamente o padrão de qualidade.

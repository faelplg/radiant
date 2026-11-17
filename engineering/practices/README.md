# Engineering practice catalog

A card names a practice, the Baseline outcomes it serves, when to choose it,
when to leave it out, observable violation signals and a verification method.
Use the [card form](../../templates/practice-card.md) for new entries.

Citation is opt-in: a Task Contract cites a practice only when its "Applies
when" holds. The Baseline table remains the required engineering check;
no contract is required to cite a practice.

New cards meet [Baseline section 14](../engineering-baseline.md#14-learn-back):
they recur, apply to several projects, can be verified and cost less than the
rework they avoid. A local preference alone does not qualify.

An id is a lowercase kebab slug matching `^[a-z0-9]+(-[a-z0-9]+)*$` and equals
the card's file stem. Never rename or reuse an id. Retiring a card is a Learn
Back change that preserves the history of its citations.

| Id | Practice | Serves | Applies when |
| --- | --- | --- | --- |
| [`solid-srp`](solid-srp.md) | Single responsibility | [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability) | A module changes for more than one actor or independent business reason. |
| [`solid-ocp`](solid-ocp.md) | Open-closed | [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity) | A second real variant exists, the variation point is stable, and evidence supports another variant. |
| [`solid-lsp`](solid-lsp.md) | Liskov substitution | [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts) | Code substitutes implementations behind a shared type or interface. |
| [`solid-isp`](solid-isp.md) | Interface segregation | [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability) | An interface has several consumers using disjoint parts. |
| [`solid-dip`](solid-dip.md) | Dependency inversion | [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests) | A policy module directly imports volatile I/O, networking or a vendor SDK, and needs an interface it owns to replace or fake that detail. |
| [`clean-architecture`](clean-architecture.md) | Clean Architecture and the dependency rule | [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability), [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity) | A durable system needs domain rules to outlive frameworks, storage and delivery mechanisms. |
| [`ports-and-adapters`](ports-and-adapters.md) | Ports and adapters | [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests), [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability) | More than one actor drives the application, such as UI, CLI and tests, or it drives storage, networks or a harness through ports it defines. |
| [`lightweight-ddd`](lightweight-ddd.md) | Lightweight domain-driven design | [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts), [EB-05](../engineering-baseline.md#7-eb-05---maintainability-and-readability) | A domain has real rules, experts share terms with the code, and words may have different meanings across bounded contexts. |
| [`test-strategy`](test-strategy.md) | Test pyramid and test strategy | [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests) | Any change has behavior to prove. |
| [`tdd`](tdd.md) | Test-driven development | [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests) | The expected result is known before coding, or a bug has a reproducible failure. |
| [`adr`](adr.md) | Architecture decision records | [EB-01](../engineering-baseline.md#3-eb-01---deliberate-complexity), [EB-06](../engineering-baseline.md#8-eb-06---dependencies-and-supply-chain) | A structural decision is costly to reverse or would make a later reader question why it was chosen. |
| [`semantic-versioning`](semantic-versioning.md) | Release and semantic versioning | [EB-02](../engineering-baseline.md#4-eb-02---correctness-and-explicit-contracts), [EB-06](../engineering-baseline.md#8-eb-06---dependencies-and-supply-chain) | A published interface has consumers that pin versions. |
| [`ci-cd`](ci-cd.md) | Continuous integration and delivery | [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests), [EB-07](../engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability) | A repository integrates several changes or contributors, or its output is deployed. |
| [`dora-metrics`](dora-metrics.md) | DORA metrics | [EB-07](../engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability) | A system is deployed repeatedly and delivery performance informs decisions. |

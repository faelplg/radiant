# DORA metrics

- Id: `dora-metrics`
- Serves: [EB-07](../engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability)

Use delivery trends for one deployed application to choose and assess an
improvement.

## Applies when

A system is deployed repeatedly and delivery performance informs decisions.

## Does not apply when

A library or CLI has no deployment, or too few deployments exist to read a
trend.

## Violation signals

Deployments cannot be joined to commits or failed-deployment incidents. A
dashboard ranks individuals, or reports a trend without a sample size and time
window.

## Verification

Measure change lead time, deployment frequency, failed deployment recovery
time, change fail rate and deployment rework rate for one service and window.
Trace samples to commit, deploy and recovery records. Older aliases: lead time
for changes, time to restore service/MTTR and change failure rate; recovery
here concerns failed deployments. Compare trends after an improvement, not
people.

## Source

Nicole Forsgren, Jez Humble and Gene Kim, [Accelerate: The Science of Lean
Software and DevOps](https://itrevolution.com/product/accelerate/) (2018).

DORA, [State of AI-assisted Software
Development](https://dora.dev/research/2025/dora-report/) (2025).

Nathen Harvey, [DORA's software delivery performance
metrics](https://dora.dev/guides/dora-metrics/) (2024; updated 2026).

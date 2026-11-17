# Continuous integration and delivery

- Id: `ci-cd`
- Serves: [EB-03](../engineering-baseline.md#5-eb-03---risk-driven-verification-and-tests), [EB-07](../engineering-baseline.md#9-eb-07---operability-diagnosis-and-observability)

Integrate frequently through automated checks and keep a reproducible path to
a releasable artifact; production deployment follows the project's
authorization.

## Applies when

A repository integrates several changes or contributors, or its output is
deployed.

## Does not apply when

The work is a personal throwaway with no integration or deployment need.

## Violation signals

Long-lived branches first meet at release time. A pipeline builds a different
revision than it tests, or deployment depends on undocumented manual steps.

## Verification

Inspect recent integration history and execute the pipeline on an exact
revision. Trace the tested artifact through release and deployment, including
smoke checks and recovery evidence.

## Source

Martin Fowler, [Continuous
Integration](https://martinfowler.com/articles/continuousIntegration.html)
(2006 rewrite; 2024 revision).

Jez Humble and David Farley, [Continuous Delivery: Reliable Software Releases
through Build, Test, and Deployment
Automation](https://www.pearson.com/en-us/subject-catalog/p/continuous-delivery-reliable-software-releases-through-build-test-and-deployment-automation/P200000009113)
(2010).

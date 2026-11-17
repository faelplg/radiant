# Engineering Profile: [project]

- Project: [project id]
- Radiant revision: [full pinned commit]
- Baseline version: [version]
- Stack pack: `none`

Replace `none` with at most one known id from the
[stack index](../engineering/stacks/README.md). The pack version is the Radiant
pin. This Profile copies neither the
[Baseline](../engineering/engineering-baseline.md#11-engineering-profile-per-project)
nor the selected pack; remove any section with nothing project-specific.
For a concrete instance, see the
[Demerzel example](../docs/engineering-profile.example.md).

## Default risk

[Default tier and the changes that raise it, with the reason.]

## Minimum quality per kind of change

| Kind of change | Required evidence beyond shared rules |
| --- | --- |
| [kind] | [project-specific gate or review] |

## Pack overrides

| Pack section | Override | Reason |
| --- | --- | --- |
| [exact selected pack section] | [replacement convention] | [evidence and decision] |

Omit the table if there are no overrides. An unlisted section retains its
pack rule. Under the [Constitution's precedence](../constitution/CONSTITUTION.md#3-order-of-precedence),
this canonical project artifact takes precedence over the shared pack.
Lowering a Baseline minimum requires an explicit human decision with its
reason under [section 2](../constitution/CONSTITUTION.md#2-normative-language).

## Commands

| Command | Working directory and prerequisites | Evidence produced |
| --- | --- | --- |
| [actual command] | [where, required fixture or environment reference] | [observable result] |

## Test strategy beyond the pack

[Project-specific boundaries, real integrations, interruptions, concurrency,
mutation proofs or human review that the aggregate command cannot establish.]

## Dependency policy

[Project-specific allowances, prohibited dependencies and approval boundary.]

## Security boundaries

[Project-specific resources, trust, secrets references and egress decisions.]

## UX requirements

[Required behavior for the project's CLI, API or human interface.]

## Compatibility and performance

[Supported runtimes, platforms and measurable budgets with their evidence.]

## Project practices

| Id | Consumer-owned card | Why it applies |
| --- | --- | --- |
| [unique project id] | [relative link to consumer card] | [context] |

Write project cards with the [practice-card form](practice-card.md), keep them
in the consumer and never reuse an id from the
[shared catalog](../engineering/practices/README.md). Listing cards here does
not validate citations in contracts.

## Deploy checklist

Following the [Deploy questions](../docs/lifecycle.md#deploy), record:

- Exact commit or artifact: [identity and evidence it was tested].
- Approval: [who approves this deploy and where the decision is recorded].
- Reversal: [rollback procedure and evidence it works].
- Data migrations: [order, reversibility and required approval].
- Smoke check: [command or procedure, expected result and owner].
- Watch: [who watches the rollout and for how long].

## Operations

[Environment-specific monitoring, diagnosis, recovery, incident ownership and
runbook pointers; include tooling only where this project needs it.]

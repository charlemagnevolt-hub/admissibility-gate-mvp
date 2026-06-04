# Runtime Admissibility Gate Architecture

This document describes the architecture of the Runtime Admissibility Gate MVP.

The prototype demonstrates a minimal execution-control boundary between an AI agent and an externally consequential action.



## Core Flow

```text
AI Agent
   |
   v
Proposed Action JSON
   |
   v
Admissibility Layer
   |
   v
Policy Evaluation
   |
   +--> ALLOW -------------> Execute Action
   |
   +--> BLOCK -------------> Stop
   |
   +--> REQUIRE_APPROVAL --> Human Review
   |
   v
Ledger Record
```



## Components

### 1. Proposed Action

The system receives a proposed action as a JSON object.

Example:

```json
{
  "type": "send_email",
  "recipient": "client@example.com",
  "recipient_type": "external",
  "contains_sensitive_data": true,
  "approved_by_human": false
}
```

The proposed action represents an intended external state transition.



### 2. Admissibility Layer

The admissibility layer determines which policy evaluation path applies to the proposed action.

In the current MVP:

* Email actions are routed to the email policy evaluator.
* Unsupported action types are blocked.

The admissibility layer serves as the execution-control boundary.



### 3. Policy Evaluation

The policy layer evaluates the proposed action against runtime constraints.

Current constraints include:

* recipient exists
* recipient type
* sensitive data flag
* human approval flag
* risk level

The result is a decision regarding admissibility.



### 4. Decision Space

The gate returns one of three decisions:

```text
ALLOW
BLOCK
REQUIRE_APPROVAL
```

#### ALLOW

The action may execute immediately.

#### BLOCK

The action must not execute.

#### REQUIRE_APPROVAL

The action is suspended until a human or supervisory process approves execution.



### 5. Execution

Only actions classified as `ALLOW` are executed.

Actions classified as `BLOCK` are stopped.

Actions classified as `REQUIRE_APPROVAL` are suspended pending review.

In the current MVP, execution is represented by a simulated email action.



### 6. Ledger

Every decision is recorded in a ledger.

The ledger records:

* timestamp
* action type
* recipient
* decision
* reason
* policy version
* raw action

The ledger provides a minimal audit trail for admissibility decisions.

The ledger enables traceability and post-decision analysis of execution-control outcomes.



## Formal Model

Runtime admissibility can be represented as:

```text
Adm(s, a, C) ∈ {ALLOW, BLOCK, REQUIRE_APPROVAL}
```

Execution is permitted only if:

```text
execute(a) ⇔ Adm(s,a,C) = ALLOW
```

where:

* `s` denotes the current system state
* `a` denotes the proposed action
* `C` denotes the applicable constraint set

The admissibility function is evaluated before an action is allowed to cause an external state transition.

Non-admissible actions do not cause an external state transition.



## Current Use Case

The first use case is email execution.

Email is used because it is:

* simple
* understandable
* externally consequential

Email is not the product.

Email is the demonstration of the control point.



## Example Decisions

| Scenario                                  | Decision         |
| ----------------------------------------- | ---------------- |
| Internal low-risk email                   | ALLOW            |
| External sensitive email without approval | REQUIRE_APPROVAL |
| External sensitive email with approval    | ALLOW            |
| Missing recipient                         | BLOCK            |
| Unsupported action type                   | BLOCK            |



## Generalization

The same architecture can be extended to other agentic tool calls, including:

* CRM updates
* database mutations
* payment instructions
* API calls
* infrastructure changes
* workflow triggers

The control pattern remains identical:

```text
Proposed Action
      ↓
Admissibility Evaluation
      ↓
ALLOW / BLOCK / REQUIRE_APPROVAL
      ↓
Execution Decision
      ↓
Ledger Record
```

The specific tool may change, but the execution-control boundary remains the same.



## Scope

This MVP is intentionally minimal.

It does not implement:

* real email delivery
* authentication
* approval workflow UI
* external policy engines
* production security controls

The purpose is not to build a complete safety platform.

The purpose is to make the execution-control boundary visible in code.



## Relation to SAFER 2026

This architecture accompanies the SAFER 2026 workshop paper:

**Control Before Consequence: Reframing Infrastructure and Governance for Agentic AI Systems**

The MVP serves as a minimal reference implementation of runtime admissibility and execution control for agentic systems.

The repository provides a concrete artifact that demonstrates how admissibility decisions can be evaluated before an AI-initiated action becomes consequential.
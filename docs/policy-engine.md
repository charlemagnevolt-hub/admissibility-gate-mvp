# Runtime Admissibility Policy Engine

## Purpose

The policy engine is responsible for evaluating proposed actions against applicable policies and constraints.

Within the Runtime Admissibility Gate, the policy engine produces one of three admissibility decisions:

* `ALLOW`
* `BLOCK`
* `REQUIRE_APPROVAL`

The policy engine represents the decision-making component of the admissibility gate.

---

## Position Within the Framework

```text
Control Before Consequence
        ↓
Runtime Admissibility
        ↓
Policy Engine
        ↓
Decision
        ↓
Execution
```

The policy engine determines whether a proposed action may become consequential under the current constraints.

---

## Inputs

The policy engine evaluates:

```text
System State (s)
Proposed Action (a)
Constraint Set (C)
```

Examples include:

* action type
* recipient type
* sensitivity level
* risk level
* approval status
* constraint set

---

## Decision Space

The policy engine returns one of the following decisions:

### ALLOW

The action is admissible and may execute immediately.

### BLOCK

The action is not admissible and must not execute.

### REQUIRE_APPROVAL

The action requires human or supervisory review before execution.

---

## Evaluation Flow

```text
Proposed Action
        ↓
Policy Engine
        ↓
Applicable Policies
        ↓
Decision
```

The policy engine evaluates admissibility only.

Execution remains outside the policy engine.

---

## Current Reference Policies

The current MVP contains reference policies for:

* send_email
* update_record
* call_api

All policies produce decisions within the same admissibility decision space.

---

## Relation to Runtime Admissibility

Runtime admissibility is represented formally as:

```text
Adm(s,a,C)
```

The policy engine serves as the implementation layer of this function.

It evaluates the proposed action against the applicable constraints and returns an admissibility decision.

---

## Scope

This document describes the conceptual policy engine.

The current MVP uses simple reference policies and is not intended as a production policy framework.

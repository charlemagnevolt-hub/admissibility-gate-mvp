# Runtime Admissibility Threat Model

## Motivation

Agentic systems increasingly possess the ability to trigger externally consequential actions.

Examples include:

- sending emails
- updating databases
- executing workflows
- invoking APIs
- transferring funds
- modifying infrastructure

In such systems, consequences emerge through action execution rather than text generation alone.



## Threat Assumption

The threat model assumes that:

- agents may generate unsafe actions
- policies may be incomplete
- context may be uncertain
- users may provide adversarial instructions
- execution environments may change

Therefore execution cannot be assumed admissible by default.



## Core Threat

The primary threat is:

> A consequential action executes before admissibility has been resolved.

Examples:

- sensitive information sent externally
- unauthorized record modification
- unintended API invocation
- irreversible state changes
- financial transactions



## Control Before Consequence

The framework assumes:

```text
Agent
    ↓
Proposed Action
    ↓
Admissibility Evaluation
    ↓
Execution Decision
    ↓
Execution
```

No externally consequential action should bypass admissibility evaluation.



## Threat Categories

### T1: Unauthorized Disclosure

Example:

- sensitive email sent externally

Potential impact:

- confidentiality breach



### T2: Unauthorized Modification

Example:

- unintended CRM update

Potential impact:

- integrity violation



### T3: Unauthorized Execution

Example:

- workflow triggered without approval

Potential impact:

- unintended operational consequences



### T4: Irreversible Actions

Example:

- payment execution
- record deletion

Potential impact:

- permanent state change



## Security Objective

The objective is not to determine whether an action is useful.

The objective is to determine whether an action is admissible.

Formally:

```text
Adm(s,a,C)
```

must be resolved before:

```text
execute(a)
```



## Formal Security Property

Runtime admissibility requires that:

```text
∀a : execute(a) ⇒ Adm(s,a,C) = ALLOW
```

In other words:

> No action may execute unless admissibility has been explicitly resolved.

This property represents the execution-control boundary of the system.



## Scope

This threat model focuses exclusively on runtime admissibility and execution control.

It does not address:

- model training
- model alignment
- content moderation
- infrastructure security
- authentication
- authorization mechanisms

These concerns are complementary but separate.



## Relation to Control Before Consequence

This threat model operationalizes the core principle of the Control Before Consequence framework:

> No externally consequential action should occur before admissibility has been evaluated.

Within the broader framework:

```text
Control Before Consequence
        ↓
Runtime Admissibility
        ↓
Admissibility Gate
        ↓
Reference Applications
```

The threat model focuses on the risks that emerge when externally consequential actions bypass
admissibility evaluation and execution control.
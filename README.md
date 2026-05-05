# Admissibility Gate MVP

A minimal runtime gate that decides whether an AI-initiated action may execute.

The goal is simple:

> No consequential action should execute before admissibility is resolved.

This project demonstrates a small control layer between an AI agent and a real-world action.



## Problem

AI systems are increasingly able to act, not just respond.

They can:

- send emails
- update records
- delete data
- call APIs
- trigger workflows

Most systems validate, observe, or audit after something happened.

This MVP focuses on the moment before execution.



## Core Question

Not:

> Can the system perform this action?

But:

> Should this action be allowed right now?



## What this MVP does

The system receives a proposed action.

It evaluates the action against runtime context and policy.

It returns one of three decisions:

- `ALLOW`
- `BLOCK`
- `REQUIRE_APPROVAL`

Only allowed actions are executed.

All decisions are recorded in a simple ledger.



## First Use Case

The first demo uses email because it is simple and easy to understand.

Email is not the product.

Email is the demonstration of the control point.



## Example

An AI agent proposes:

```json
{
  "type": "send_email",
  "recipient": "client@example.com",
  "recipient_type": "external",
  "contains_sensitive_data": true,
  "approved_by_human": false
}
```

The gate evaluates:

- recipient is external
- content contains sensitive data
- no human approval exists

Decision:

```
REQUIRE_APPROVAL
```

The email is not sent.



## Architecture

```
AI Agent
   |
   v
Proposed Action
   |
   v
Admissibility Gate
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



## Relation to guardrails

Traditional AI guardrails focus on:

- input filtering
- output validation
- moderation
- prompt injection prevention
- hallucination detection
- sensitive data detection

These are necessary.

But they mostly operate before reasoning or after generation.

This project focuses on a different boundary:

> the moment an AI-initiated action becomes executable.

It asks:

> Should this action be allowed to execute right now?

That is not only a content-safety question.

It is an execution-control question.



## Why this matters

Observability tells us what happened.

Audit records what happened.

This MVP shows a small mechanism for deciding what is allowed to happen before execution.

Without this gate, a system may still be fully observable, auditable, and policy-covered while executing actions that should not have happened.



## Current scope

This MVP implements:

- email actions
- simple policy checks
- runtime decisioning
- decision logging

It does not yet implement:

- real email delivery
- authentication
- user interface
- approval workflow UI
- external policy engines
- production security controls



## Future extensions

Possible next steps:

- CRM updates
- database mutations
- payments
- API calls
- approval workflow
- post-execution verification
- state transition modeling
- policy files
- tests
- simple API wrapper



## Run

```bash
python main.py examples/email_external_sensitive.json
```

Expected result:

```text
Decision: REQUIRE_APPROVAL
Reason: External email contains sensitive data and has no human approval.
Action was not executed.
Ledger entry written.
```

Run a safe internal email:

```bash
python main.py examples/email_internal_safe.json
```

Expected result:

```text
Decision: ALLOW
Reason: Action is admissible under current policy.
Email sent to team@company.local with subject: Internal meeting notes
Ledger entry written.
```



## Status

Experimental MVP.

The purpose is not to build a complete AI safety product yet.

The purpose is to make the control point visible in code.

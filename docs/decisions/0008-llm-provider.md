# 0008. Choice of LLM provider

## Status
Proposed. To be decided at the start of Milestone 1.

## Context
The LLM is used only to generate answers from retrieved chunks; embeddings run
locally. All LLM calls go through a thin adapter interface, with a fake
implementation for tests, so the provider can be changed later. The choice
affects cost per conversation, EN/ES answer quality, and how well instructions
about citations and untrusted text are followed.

## Options considered
- Claude, using an API key from the Claude Console.
- Another provider with a comparable API.

## Decision
Not yet made. It will be made at the start of Milestone 1, after checking current
pricing and spending-limit options. The adapter keeps the provider swappable.

## Consequences
- Milestone 1 tests can start with the fake LLM before the decision.
- Whichever provider is chosen, the demo uses a separate key with a low hard
  spending limit (see the threat model).
- When decided, this ADR's status and decision are updated.

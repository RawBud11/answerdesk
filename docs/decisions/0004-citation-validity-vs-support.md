# 0004. Check citation validity at runtime; measure support in evaluation

## Status
Accepted (2026-10-06)

## Context
Two different questions can be asked about a citation: is it a real chunk that
was retrieved (validity), and does that chunk actually support the claim
(support)? Validity can be checked cheaply and deterministically in code. Support
needs judgment, from a human or an LLM judge, which is too slow and costly to run
on every request.

## Decision
At runtime, the verifier checks only validity: every cited ID must be one of the
retrieved chunks, and an answer with no valid citation becomes "I don't know".
Support is measured offline as the "citation accuracy" metric in the evaluation.

## Consequences
- The runtime check is fast, free, and unit-testable.
- A valid citation can still point to a chunk that does not support the claim;
  the evaluation report states this gap explicitly.
- Runtime support checking can be revisited if evaluation shows it matters.

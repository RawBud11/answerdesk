# 0001. Verify the full answer before streaming it

## Status
Accepted (2026-10-06)

## Context
The chat pipeline verifies citations in code and replaces an answer that has no
valid citation with the "I don't know" response. If tokens are streamed to the
widget as the LLM produces them, the user may already have read an answer that
later fails verification, and streamed text cannot be taken back.

## Decision
The backend waits for the complete LLM answer, verifies its citations, and only
then streams the verified answer and its citations to the widget over SSE.

## Consequences
- Users never see an answer that failed verification.
- Time to the first visible token grows by the full generation time; the widget
  shows a typing indicator meanwhile. Latency is reported in the evaluation.
- SSE is still used, so true token streaming with verification as it streams can
  be added later without changing the widget protocol.

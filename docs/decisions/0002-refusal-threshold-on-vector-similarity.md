# 0002. Base the refusal threshold on raw vector similarity

## Status
Accepted (2026-10-06)

## Context
Retrieval merges vector search and full-text search with reciprocal rank fusion
(RRF). RRF scores depend only on rank positions, so they show how a chunk ranks
against the others, not how relevant it actually is. A question with no good
match still produces top-ranked chunks with normal-looking RRF scores.

## Decision
The decision to answer or refuse uses the highest raw cosine similarity between
the question embedding and the retrieved chunks. RRF is used only to order the
chunks passed to the LLM. The threshold value is tuned on the evaluation set
(Milestone 2), not guessed.

## Consequences
- The threshold has a stable meaning across questions.
- Full-text matches alone cannot prevent a refusal, which may cause some wrong
  refusals for exact-keyword questions; this is measured as the over-refusal rate.
- If the tuned threshold proves unstable, a reranker is the next option to test.

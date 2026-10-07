# 0007. Group unanswered questions by embedding similarity

## Status
Accepted (2026-10-06)

## Context
The admin's unanswered inbox lists refused and thumbs-down questions "grouped by
similarity", so that ten wordings of the same gap appear as one item. Clustering
libraries exist but add a dependency and parameters that are hard to explain.

## Decision
Embed each unanswered question with the existing embedding model. Assign each
question to the first existing group whose representative question has cosine
similarity above a fixed cutoff; otherwise start a new group. No clustering
library is used in the MVP.

## Consequences
- Simple, explainable, and needs no new dependency.
- Results depend on question order and on the cutoff, which is set by inspecting
  real examples.
- Fine for dozens or hundreds of questions; a proper clustering method can be
  added if volume grows.

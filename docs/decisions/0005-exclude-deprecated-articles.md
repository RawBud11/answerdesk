# 0005. Do not index deprecated articles

## Status
Accepted (2026-10-06)

## Context
Articles have a status of draft, published, or deprecated. The corpus deliberately
includes a deprecated article that conflicts with its replacement. If deprecated
content is retrievable, the bot can cite outdated policy.

## Decision
Only `published` articles are chunked and indexed. Deprecated and draft articles
stay in the `articles` table for history and editing, but have no chunks. Changing
an article's status to deprecated removes its chunks.

## Consequences
- Outdated content cannot be retrieved or cited.
- The conflicting deprecated article becomes an evaluation check: no answer should
  cite or repeat its facts.
- Admins cannot preview how a draft would be answered before publishing (a
  possible later feature).

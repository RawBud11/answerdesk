# 0003. Index full-text search with each chunk's own language

## Status
Accepted (2026-10-06)

## Context
Postgres full-text search needs a language setting (`english`, `spanish`) to
reduce words to their root form and skip common words. The corpus has English and
Spanish articles. A Spanish question will not keyword-match English text, whatever
the setting.

## Decision
Each chunk's `tsv` column is built with the language setting that matches its
article's `lang`. The question is searched with the setting for its detected
language (see 0006). Cross-lingual retrieval relies on the multilingual
embeddings only.

## Consequences
- Keyword search works properly within each language.
- For cross-lingual questions the full-text half of hybrid search adds nothing;
  the 5 cross-lingual evaluation questions measure whether vector search alone
  is enough.
- Adding a third language means adding its language setting and test questions.

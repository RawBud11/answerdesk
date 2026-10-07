# Demo help-center content

Synthetic help-center articles for **Larchwick Outfitters**, a fictional online
outdoor-gear store. Every word here is invented; nothing is copied from a real
company's help center.

## Store name
The strategy's working name, "Harbor & Pine", is already used by a real business
(a vacation rental in Maine), so the demo uses "Larchwick Outfitters" instead. A
web search on 2026-10-06 found no business with that name. That is not a
trademark search; rename it if you prefer.

Contact addresses use the reserved `.example` domain so they can never reach a
real mailbox.

## Status of this content
**Draft, written by Claude Code, not yet reviewed by the project owner.** Check
every number and policy before treating it as the reference corpus: the
evaluation questions in `eval/questions.jsonl` depend on these exact facts.

Phase 0 target (strategy, Section 7.2): about 24 English and 12 Spanish articles.
Current: 6 English (the first-week checklist), 0 Spanish.

## File format
One article per file: `content/articles/<lang>/<slug>.md`, with YAML front matter
followed by the Markdown body.

```yaml
---
slug: returns-and-exchanges     # unique across all languages
title: Returns and exchanges
lang: en                        # en | es
status: published               # draft | published | deprecated
replaced_by: other-slug         # optional, deprecated articles only; for humans
---
```

The fields match the `articles` table in the strategy (Section 5). Only
`published` articles are indexed (ADR 0005). `replaced_by` is informational and
is not stored by ingestion unless a later decision adds it.

## Deliberate difficulty
| Article | What it tests |
|---|---|
| `shipping-rates-and-times` | A cost table, a free-shipping threshold, regional exceptions (Alaska, Hawaii, territories), oversize fees |
| `international-shipping` | Similar to domestic shipping but every number differs; duties differ by country |
| `returns-and-exchanges` | Exchange vs refund label cost, final-sale exclusion, holiday extension |
| `returns-policy-2024` | **Deprecated**; conflicts with the current returns policy (30 vs 60 days, label cost, refund time) |
| `jacket-sizing` | A size table; different advice for shell vs insulated jackets |
| `warranty` | Overlaps with returns: unused items vs defects, Larchwick vs other brands |

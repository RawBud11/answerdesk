# 0006. Detect the question's language, falling back to the widget toggle

## Status
Accepted (2026-10-06)

## Context
The answer must be in the user's language, and full-text search needs the
question's language (see 0003). The widget has an EN/ES toggle for interface
text, but users may type in the other language. Short questions are hard to
classify reliably.

## Decision
The backend detects the language of each question with a small
language-detection library, limited to English and Spanish. If detection is
uncertain, it uses the language of the widget's toggle. The result is stored in
`conversations.lang_detected`. The library is chosen and approved when this is
implemented.

## Consequences
- Answers follow what the user actually typed, not only the toggle.
- Adds one dependency (pending approval).
- Detection mistakes on very short questions are possible; the evaluation's
  Spanish and cross-lingual questions will show how often.

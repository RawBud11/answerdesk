# Evaluation set

`questions.jsonl` holds one question per line. Fields match the `eval_questions`
table in the strategy (Section 5):

| Field | Meaning |
|---|---|
| `id` | Stable string ID: `<lang>-<category>-<nn>` (`in`, `xl` cross-lingual, `oos`, `adv`) |
| `lang` | Language of the question: `en` or `es` |
| `question` | The text sent to the chat API |
| `category` | `in_scope`, `cross_lingual`, `out_of_scope`, or `adversarial` |
| `expected_article_slugs` | Articles a correct answer should cite; empty for refusals |
| `expected_facts` | Facts the answer must contain, in the question's language; empty for refusals |
| `expected_behavior` | `answer` or `refuse` |

## Status
**Draft, written by Claude Code, not yet reviewed by the project owner.** Every
expected fact comes from the articles in `content/articles/`; if you change an
article, update the questions that depend on it.

Current: 15 questions (the first-week checklist). Target (strategy, Section 7.3):
about 60.

| Category | Now | Target |
|---|---|---|
| In scope, English | 9 | 20 |
| In scope, Spanish | 0 | 10 (needs Spanish articles) |
| Cross-lingual | 1 | 5 |
| Out of scope | 3 | 15 |
| Adversarial | 2 | 10, including a poisoned test article |

## Notes for reviewers
- `en-in-03` and `en-in-04` also check that the deprecated article
  (`returns-policy-2024`: 30 days, free labels) never leaks into answers.
- `en-in-07` needs two steps: read the chart (M), then apply the insulated-jacket
  rule (one size larger, L).
- `en-oos-03` asks for personal order data, which the bot cannot access; the
  expected refusal should offer the handoff to a person.
- The poisoned test article for adversarial cases must live outside
  `content/articles/` so it never reaches the production index. It is not written
  yet.

# Add Lingxi AI Assistant: 530/615 (86.18%)

Draft for a source-linked Steel WebVoyager submission. Source links and reporting date refer to the public evaluation repository. Replace the preparation checklist with actual PR changes and validation results when submitting to Steel.

## Submission

| Item | Value |
| --- | --- |
| System | Lingxi AI Assistant |
| Organization | China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司) |
| Agent model request | DeepSeek-V4.1-Flash |
| External judge | doubao-seed-2-0-pro-260215 (ark) |
| Total evaluated tasks | 615 |
| Success / failure / unknown | 530 / 49 / 22 |
| Execution errors / Judge errors | 12 / 2 |
| Success rate | 86.18% |
| Reporting date | 2026-11-11 |
| Public source | https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/REPORT.md |
| Product homepage | https://ai.soho.komect.com/ai/llm/home |

This is a self-reported, product-level result for the paid, closed-source Lingxi AI Assistant under the configuration described in the public report. All 615 tasks remain in the denominator. Only archived success verdicts contribute to the numerator.

## Task collection

The exact evaluated dataset has 615 unique IDs across 15 websites, inheriting 28 exclusions relative to the canonical 643 tasks. Ninety-nine retained instructions differ from canonical; 71 differ from the fixed omxyz current layer through date changes or date-format/year normalization. TASK_UPDATES.md provides exclusions and complete before/after questions. The score applies to this collection and is not an unmodified full-suite score.

## Execution and external evaluation

The recorded execution model request is DeepSeek-V4.1-Flash, with catalog name Deepseek-V4.1-flash. Browser Operation V2 was limited to 40 counted host calls per task, with batches counted once, four concurrent tasks, a 4800-second task timeout and a 2700-second worker limit. Historical execution-platform metadata is in METHODOLOGY.md.

The external Judge uses a custom evidence-v1 text-and-image protocol, not the original WebVoyager prompt. The source publishes the exact shared prompt, 613 frozen input bundles, 615 structured Judge records, and 611 selected screenshots. The recorded final answer is retained, rather than undergoing a newly introduced answer-cleaning step.

## Scoring and limitations

One archived classification is used per task. No rerun, new Judge call or changed verdict was introduced during publication preparation. The schedule establishes one dispatch per ID within this archive, not absence of earlier evaluations or transport retries. The historical provider-side model checkpoint, complete auxiliary model stack, product/Chrome versions, and Judge request/retry/raw-response provenance were not established.

Four tasks lack a selected screenshot; one retains a text-supported automated success with a disclosed interpretation caveat. The two Judge errors and all unknown/execution-error cases remain non-successes. A legacy missing-image diagnostic was corrected from a combined counter of six to four actual missing-image tasks; the score did not change.

## Evidence links

- Result report: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/REPORT.md
- Methodology: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/METHODOLOGY.md
- Exact tasks and question changes: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/evaluated-615.jsonl ; https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/TASK_UPDATES.md
- Structured judgments and frozen input index: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/JUDGE_EVALUATION.md
- Scoring audit: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/blob/main/SCORING_AUDIT.md
- Execution evidence and checksum manifests: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09

## Changes and checks to complete in the Steel PR

- Add the completed row to src/data/webvoyager.json and recalculate competition ranks.
- Update WebVoyager lastUpdated in src/lib/benchmark-hub.ts and regenerate README.md.
- Run npm run update-readme, npm run lint and npm run build; report their actual outcomes.

No rank, passed Steel CI result or maintainer approval is claimed by this draft.

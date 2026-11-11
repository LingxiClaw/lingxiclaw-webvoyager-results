# LingxiClaw / Lingxi AI Assistant WebVoyager Results

**86.18% success rate — 530 of 615 tasks.**

Organization: **China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司)**

[Product website](https://ai.soho.komect.com/ai/llm/home)

This repository records the LingxiClaw product result under the archived system name **Lingxi AI Assistant**.

This is a self-reported, product-level evaluation of Lingxi AI Assistant, a paid, closed-source assistant. The result describes the complete product running the documented configuration on a date-adjusted WebVoyager-derived task collection. The product name is used consistently in the proposed leaderboard entry; the historical execution environment is documented in [METHODOLOGY.md](METHODOLOGY.md).

Documentation prepared: **2026-11-11**. Execution: **2026-10-09 UTC**. Offline judging: **2026-10-10 UTC**. Public reporting date: **2026-11-11**. [Public evidence repository](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results). This is a self-reported result; no Steel leaderboard submission or acceptance is claimed.

## Result

| Outcome | Tasks |
| --- | ---: |
| Success | 530 |
| Failure | 49 |
| Unknown | 22 |
| Execution error | 12 |
| Judge error | 2 |
| Total | 615 |

Success rate = 530 / 615 × 100% = 86.1788617886%, displayed as **86.18%**. Every evaluated task remains in the denominator. No task was rerun, rejudged or removed while preparing these materials.

| Evaluation setting | Value |
| --- | --- |
| Agent model request | DeepSeek-V4.1-Flash |
| Recorded catalog model | Deepseek-V4.1-flash |
| External judge | ark / doubao-seed-2-0-pro-260215 |
| Judge protocol | Custom text-and-image evidence-v1 protocol |
| Task collection | 615 tasks across 15 websites; 28 inherited exclusions from canonical 643 |
| Task-instruction differences | 99 retained questions differ from canonical; 71 differ from the fixed omxyz current layer |
| Counted browser-call budget | 40 per task; a browser_v2_run batch counts as one host call |

The precise provider-side execution-model checkpoint, complete auxiliary runtime-model stack, historical product/browser builds, and judge request/retry provenance were not established. The archived model identifiers are reported as recorded. The judge is an offline scoring model, separate from the product's runtime-model stack.

## Read and inspect

| Material | Location |
| --- | --- |
| Full result report and 615-task evidence index | [REPORT.md](REPORT.md) |
| Execution and evaluation methodology | [METHODOLOGY.md](METHODOLOGY.md) |
| Every exclusion and task-text difference | [TASK_UPDATES.md](TASK_UPDATES.md) |
| Exact evaluated tasks | [evaluated-615.jsonl](evaluated-615.jsonl) |
| Machine-readable summary | [summary.json](summary.json) |
| Aggregated task judgments | [merged_results.json](merged_results.json) |
| Judge prompt and recorded input configuration | [JUDGE_EVALUATION.md](JUDGE_EVALUATION.md) |
| Scoring audit and missing-image cases | [SCORING_AUDIT.md](SCORING_AUDIT.md) |
| Execution logs, frozen inputs and screenshots | public/run/ (`public/run` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) |
| Privacy processing and provenance | [EVIDENCE.md](EVIDENCE.md) |
| Upload and submission procedure | [PUBLICATION_GUIDE.md](PUBLICATION_GUIDE.md) |
| English Steel PR and Issue drafts | [PR_BODY.md](PR_BODY.md) and [ISSUE_DRAFT.md](ISSUE_DRAFT.md) |

## Per-website results

| Website | Success / total | Success rate |
| --- | ---: | ---: |
| Allrecipes | 39/40 | 97.50% |
| Amazon | 38/40 | 95.00% |
| Apple | 37/40 | 92.50% |
| ArXiv | 39/43 | 90.70% |
| BBC News | 33/39 | 84.62% |
| Booking | 31/40 | 77.50% |
| Cambridge Dictionary | 38/41 | 92.68% |
| Coursera | 37/40 | 92.50% |
| ESPN | 38/44 | 86.36% |
| GitHub | 37/41 | 90.24% |
| Google Flights | 19/40 | 47.50% |
| Google Map | 35/40 | 87.50% |
| Google Search | 40/42 | 95.24% |
| Huggingface | 30/39 | 76.92% |
| Wolfram Alpha | 39/46 | 84.78% |

## Complete evidence archive

Download the [complete evidence archives](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09) from the [Release](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09). Download the common ZIP and **all 15 website ZIPs**, then verify them against [SHA256SUMS.txt](SHA256SUMS.txt) or [archive-manifest.json](archive-manifest.json), then extract all ZIPs into the same parent directory. Their union includes all 5,589 files, including the original directory layout and offline verification scripts. Historical evidence paths in the JSON records are relative to this extracted package.

## Offline verification

Use Python 3.9 or newer from the extracted `lingxiclaw-webvoyager-evidence` directory:

```sh
python3 scripts/verify_repository.py
python3 evaluation/recompute_results.py
```

These commands read local files, verify checksums and recompute the archived classification. They make no API requests and do not evaluate answers again. The individual files retain the original task-record layout. The public GitHub repository hosts the report, methodology and structured results; the complete directory, including logs and images, is distributed as [Release archives](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09). Extract all 16 ZIPs into the same parent directory before running these verification commands. The complete evidence occupies approximately 1.46 GB before Git compression.

The documentation is in English. Historical logs, model responses and judge decisions retain their recorded language. The bilingual organization name is intentional. Dataset license information is retained in [LICENSE-WebVoyager.txt](LICENSE-WebVoyager.txt).

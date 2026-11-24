# Lingxi AI Assistant WebVoyager evaluation with Kimi-K3

**Lingxi AI Assistant achieved 87.15% (536/615) after seven execution-error retries. The reconstructed initial-dispatch success rate is 86.02% (529/615).** Both figures are self-reported product-level results for the same 615 tasks on 15 websites. Evaluation and offline judging took place on November 23–24, 2026 UTC.

China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司) selected `ydy-kimi-K3` for this run. The custom offline evaluator used `ark / doubao-seed-2-0-pro-260215`.

| Attempt accounting | Success | Failure | Unknown | Execution error | Judge error | Total | Success rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Initial dispatch, reconstructed | 529 | 62 | 16 | 8 | 0 | 615 | 86.02% |
| Final records, including seven later executions | 536 | 62 | 16 | 1 | 0 | 615 | 87.15% |

The initial scheduler recorded 607 completions and eight errors. The final task directories contain seven later executions with later start times and successful judgments. Google Flights--30 kept its execution error and skipped judging. The initial-dispatch metric uses the original scheduler status for each error and the judgments for the 607 initial completions. All 614 raw judge responses agree with the published outcome categories. [Attempt history](ATTEMPTS.md) · [Scheduler log](run/schedule.jsonl)

## Scores by website

| Website | Tasks | First-dispatch successes | Final successes | Failure | Unknown | Execution error | Final success rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Allrecipes | 40 | 40 | 40 | 0 | 0 | 0 | 100.00% |
| Amazon | 40 | 30 | 30 | 9 | 1 | 0 | 75.00% |
| Apple | 40 | 37 | 37 | 1 | 2 | 0 | 92.50% |
| ArXiv | 43 | 40 | 41 | 2 | 0 | 0 | 95.35% |
| BBC News | 39 | 34 | 36 | 3 | 0 | 0 | 92.31% |
| Booking | 40 | 33 | 34 | 6 | 0 | 0 | 85.00% |
| Cambridge Dictionary | 41 | 39 | 39 | 2 | 0 | 0 | 95.12% |
| Coursera | 40 | 37 | 37 | 3 | 0 | 0 | 92.50% |
| ESPN | 44 | 35 | 36 | 6 | 2 | 0 | 81.82% |
| GitHub | 41 | 36 | 36 | 3 | 2 | 0 | 87.80% |
| Google Flights | 40 | 25 | 27 | 12 | 0 | 1 | 67.50% |
| Google Map | 40 | 34 | 34 | 6 | 0 | 0 | 85.00% |
| Google Search | 42 | 36 | 36 | 5 | 1 | 0 | 85.71% |
| Huggingface | 39 | 33 | 33 | 4 | 2 | 0 | 84.62% |
| Wolfram Alpha | 46 | 40 | 40 | 0 | 6 | 0 | 86.96% |

## Comparison with the original benchmark

The declared dataset contains 615 of the original 643 task IDs. It inherits 28 exclusions, and 99 retained questions differ from the canonical snapshot. The browser budget counts up to 40 host calls per execution. One call can carry multiple primitive actions. The custom judge uses text and selected screenshots. Different task sets, budgets, attempt policies and judges limit comparisons across systems.

[Methodology](METHODOLOGY.md) · [Task evidence](TASKS.md) · [Machine-readable scores](summary.json) · [Publication checks](EVIDENCE.md)

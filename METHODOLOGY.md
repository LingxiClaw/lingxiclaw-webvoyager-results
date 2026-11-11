# Evaluation Methodology

## System identity and scope

System: **Lingxi AI Assistant**. Organization: **China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司)**.

This is the product's full-system result under the configuration below. It evaluates the assistant, model access, prompts and browser execution layer together. Product source code is not part of this repository.

## Task collection

The exact file is [evaluated-615.jsonl](evaluated-615.jsonl), SHA-256 `e0f99161eeb09f30c94cb687143b67e6684347dc29ba863541f95ba15914f9b9`. It contains 615 unique task IDs across 15 websites. The fixed denominator is 615. See [TASK_UPDATES.md](TASK_UPDATES.md) for all exclusions and before/after instructions. This is a date-adjusted collection, not the unmodified 643-task benchmark.

Run task instructions and frozen judge tasks match the evaluated dataset after trimming boundary whitespace. Two recorded questions contain only boundary-whitespace differences. No substantive task edit was introduced during packaging.

## Historical execution environment

The retained manifest records **macOS 26.4 arm64**, Python **3.12.13**, and adapter `lingxi-webvoyager-v2-audit/2.0.0-single-acceptance-evidence-v1`. Execution ran from `2026-10-09T11:42:15.792807+00:00` to `2026-10-09T20:52:26.070681+00:00`.

The historical product build, release channel, Chrome version and complete network-region metadata were not established. Current installation versions are not substituted for historical values. Archived batch IDs and operating-system fields remain unchanged in the evidence.

## Runtime model identifiers

Requested model: `DeepSeek-V4.1-Flash`. Catalog model: `Deepseek-V4.1-flash`; catalog display: `Deepseek-V4.1-Flash(MOMOA)`; catalog ID: `62`; worker alias: `deepseek-v4-flash`.

These are recorded identifiers. They do not independently establish the provider-side model checkpoint, released-weight availability or the complete auxiliary-model stack. Requested temperature 0 and output limit 65536 are metadata, not proof of server-side enforcement.

## Execution budgets and dispatch

| Setting | Recorded value |
| --- | --- |
| Counted browser host calls | 40 per task |
| Task timeout | 4800 seconds |
| Worker runtime limit | 2700 seconds |
| Concurrency / same-site concurrency | 4 / 4 |
| Scheduling | Site round robin; 30-second site cooldown |
| Seed / shuffle | 42 / false |
| Browser interface | Browser Operation V2, ten browser_v2_* tools |

A `browser_v2_run` batch counts as one host round trip. The limit is not 40 primitive actions: 81 task records exceed 40 primitive actions, with a maximum of 88. No recorded budget-compliance check failed. Limited planning/capability metadata tools were allowed by the task contract.

The schedule contains one dispatch for each of 615 IDs in this archive. It does not establish absence of earlier evaluations, internal model retries or Judge transport retries. No best-of-N trajectory-selection claim is made.

## Answer and evidence preparation

The frozen input contains the task, recorded final answer, selected browser text and available selected screenshots. The answer has not been newly translated, cleaned of self-evaluation claims, or rewritten for this publication. The custom judge prompt explicitly treats agent assertions as insufficient proof.

The evidence-v1 profile has a 60,000-character text-selection budget, 4,000-character chunks and a conservative context-capacity check. Full frozen messages and profile values are retained in each `judge_input.json`; the extracted shared prompt and profile are in [evaluation/](JUDGE_EVALUATION.md).

There are 613 frozen input bundles and 611 selected screenshots. Original input/source/image consistency checks passed during preparation; public derivatives have new hashes after privacy redaction. These bundles are not claimed to be recovered byte-identical provider wire requests.

## External judge

Provider: `ark`. Model: `doubao-seed-2-0-pro-260215`. Scoring period: `2026-10-10T01:04:15.500613Z` to `2026-10-10T02:30:32.832372Z`.

The evaluator uses a **custom text-and-image prompt**, not the original WebVoyager GPT-4V protocol. It permits reliable browser text to establish textual facts and requires corresponding evidence for side effects or visual requirements. The full prompt is [judge_prompt.txt](judge_prompt.txt).

The 615 Judge records contain 601 completed judgments, 12 execution-error skips and 2 Judge errors. The historical `request_count=0` fields are default values, not measured counts. Exact transport attempts, retries, provider request IDs and raw provider responses were not recovered. No raw-provider-response archive is fabricated or substituted with structured Judge records.

## Scoring and judgment selection

Each unique task contributes one archived classification. An execution error or invalid benchmark contract is an execution failure; otherwise a Judge error is retained as a Judge error; otherwise the saved verdict determines success, failure or unknown. Only success contributes to the numerator. All 615 tasks remain in the denominator.

No additional Judge requests, replacement verdicts or selective exclusions were introduced in preparation. recompute_results.py (`evaluation/recompute_results.py` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) independently aggregates the retained records without model calls. It is an offline aggregation tool, not the historical online Judge runner.

## Exceptions and provenance

See [SCORING_AUDIT.md](SCORING_AUDIT.md) for the four missing-image cases, Huggingface--35's interpretation caveat, the two Judge errors and the legacy diagnostic-counter collision. These disclosures do not change the archived 530/615 result.

Nine archived runner files match manifest source hashes. The recovered archive also contains associated Judge source and dependency pins, but their exact use in the historical Judge invocation is not established. [harness-provenance.json](harness-provenance.json) records this distinction; the original online Judge implementation is not claimed to be reproduced by this repository's offline checker.

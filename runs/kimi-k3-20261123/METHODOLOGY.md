# Evaluation methodology

## Product and model

The evaluated system is the paid, closed-source Lingxi AI Assistant. The product team confirms `ydy-kimi-K3` as the requested, catalog and worker model. The catalog identifies it as entry 69, displayed as Kimi-K3(MoMA). The run requested temperature 0.0 and a maximum output of 65,536 tokens through request metadata. Those two values describe the request and do not attest to provider enforcement or an immutable service checkpoint. [Recorded configuration](run/manifest.json)

## Task collection

The evaluated file has SHA-256 `e0f99161eeb09f30c94cb687143b67e6684347dc29ba863541f95ba15914f9b9`. The October and November evaluations reference these same input bytes. All 615 IDs, websites, URLs and questions agree with the final run records after trimming outer question whitespace on two IDs (Google Map--15 and Google Search--42). The comparison with canonical WebVoyager gives 28 excluded IDs and 99 changed questions. Of the retained tasks, 71 questions differ from the pinned omxyz current layer. Date-sensitive prompts retain their archived dates, including dates already past at the time of this test. All selected tasks stay in the denominator. [Evaluated tasks](../../evaluated-615.jsonl) · [Canonical 643 tasks](../../original-643.jsonl) · [Dataset comparison](dataset-comparison.json)

## Browser and attempt policy

The assistant used the Browser V2 interface on live websites. The scheduler allowed four simultaneous tasks overall and four on a single site. The recorded task timeout was 4,800 seconds and the worker's maximum run duration was 2,700 seconds. All 615 final task records report hard enforcement and compliance with the 40-call budget per execution. Batched `browser_v2_run` operations count as one host round trip. Session lifecycle calls are excluded, and rejected dispatch attempts do not spend a call. 78 final executions logged more than 40 primitive actions, with a maximum of 136.

The original schedule dispatched every task once. The final score includes seven additional executions after initial errors. Attempt limits apply separately to each execution. [Attempt accounting](ATTEMPTS.md)

## Offline judge

The evidence-v1 evaluator used `ark / doubao-seed-2-0-pro-260215` and classified eligible tasks as success, failure or unknown. The published percentage counts only success. The profile provides 60,000 text characters, 4,000-character chunks and a maximum context of 131,072 tokens. Each eligible final execution has one recorded logical judge request and one complete provider response. There are 610 judged tasks with a selected image and four judged from text alone. The skipped task also has a selected screenshot. The applied prompt is identical across all 615 frozen bundles. [Exact judge prompt](judge_prompt.txt) · [Profile and counts](summary.json)

This is a custom evaluator. The evaluation used the recorded evidence and no new model calls during preparation. [Original WebVoyager project](https://github.com/MinorJerry/WebVoyager)

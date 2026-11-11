# Lingxi AI Assistant WebVoyager evaluation

Lingxi AI Assistant · China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司) · [Official product website](https://ai.soho.komect.com/ai/llm/home)

86.18% 530 / 615 tasks

Self-reported full-system result. Browser execution: 9 October 2026 UTC. Automated judging: 10 October 2026 UTC. Documentation prepared on 11 November 2026. Public reporting date: 11 November 2026. Public repository: https://github.com/LingxiClaw/lingxiclaw-webvoyager-results. This is a self-reported result; no Steel submission or leaderboard acceptance is claimed.

Lingxi is a paid, closed-source AI assistant. The evaluated configuration used Browser Operation V2 with the catalog model DeepSeek-V4.1-Flash and an offline Doubao judge. Core product code is not included in this evidence package.

## Result and scoring

The fixed denominator includes every one of the 615 selected tasks. There are 530 successes, 49 failures, 22 unknown outcomes, 12 execution errors and 2 judge errors. Only success counts toward the numerator. No errors or unknowns were removed, and no browser task or judge call was rerun while preparing this package.

The score is the archived automated judgment result, not independent human certification. The two judge errors are BBC News--13 and Google Search--8; both remain non-successes. The local report field formal=false refers to the harness acceptance mode and does not represent a benchmark-author certification.

## Dataset and comparability

The exact evaluated file is evaluated-615.jsonl (`public/datasets/evaluated-615.jsonl` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)). It has 615 unique IDs from 15 websites. Its SHA-256 is `e0f99161eeb09f30c94cb687143b67e6684347dc29ba863541f95ba15914f9b9`.

The ID set matches the omxyz shared 615-task layer: the 24-task Alumnium removal set plus four additional upstream exclusions. There were no additional exclusions based on the Lingxi outcomes. Compared with the canonical 643-task dataset, 99 retained task questions differ. Compared with the fixed omxyz current layer, 71 questions differ, all in Booking or Google Flights, through date replacements or date-format/year normalization. These statements describe the recovered files; the historical editing command was not recovered.

Every removed ID, source reference and before/after question is in [dataset provenance](dataset-provenance.json). The evaluated set must not be described as the unmodified full 643-task benchmark. Booking--5 retained a hotel stay dated October 1–4, already past when execution began on October 9; it failed and remains in the denominator.

## System and execution protocol

- Recorded platform: macOS 26.4 arm64; Python 3.12.13; adapter lingxi-webvoyager-v2-audit/2.0.0-single-acceptance-evidence-v1.
- Requested model: DeepSeek-V4.1-Flash. Catalog model: Deepseek-V4.1-flash, catalog ID 62. Worker alias: deepseek-v4-flash. A historical provider-side model snapshot was not established; the alias should not be mistaken for an independently verified checkpoint.
- The manifest records four concurrent tasks, same-site concurrency four, site-round-robin scheduling, 30-second site cooldown, seed 42 and no shuffle.
- Each task was limited to 40 counted browser host calls. A browser_v2_run batch counts as one host call. It is not a 40-primitive-action cap: 81 tasks recorded more than 40 primitive actions, with a maximum of 88. No recorded budget compliance check failed.
- Task timeout request: 4800 seconds; worker runtime limit: 2700 seconds. Requested execution temperature 0 and output limit 65536 were recorded as metadata; historical backend enforcement is not established.
- The task contract restricted browsing to the ten browser_v2_* tools, with limited planning/capability metadata tools. Product version/build, Chrome version, network region and the complete auxiliary-model stack were not established from historical artifacts.
- The schedule contains one dispatch for each of the 615 IDs. This proves no duplicate dispatch within this archive, not absence of previous runs, model-internal retries or judge transport retries.

Nine archived runner source files match the manifest hashes exactly; see [harness provenance](harness-provenance.json). Archived dependency pins are provided as provenance, not a claim that the historical environment installed every pinned version.

## Judge and evidence

Provider: ark. Model: `doubao-seed-2-0-pro-260215`. The evidence-v1 bundle contains the original task, agent answer, selected browser text and selected screenshots. Text selection has a 60,000-character budget and an additional context-capacity check. The frozen prompt requires support for every material constraint, treats agent claims as insufficient, and permits browser text to support textual facts. It is a custom evaluator, different from the original WebVoyager GPT-4V protocol.

There are 613 frozen input bundles and 611 selected screenshots. All original bundle/source/image hashes passed consistency checks, and all selected screenshots decoded. The 615 judge files include 601 completed judgments, 12 execution-error skips and 2 judge errors. The archived request_count values are defaults of zero; request-count, retry and raw-provider-response provenance was not recovered. Zero must not be interpreted as no judging, nor as evidence of one judge attempt.

Four tasks have no selected screenshot: Google Flights--15, GitHub--29, Huggingface--34 and Huggingface--35. Only Huggingface--35 was scored successful. Its text sources support the Diffusion-tag listing and the chosen article summary, but the broader interpretation of newest across community posts is uncertain. See [the supplementary review note](review-notes.json). Keeping its original judgment gives 530/615; excluding its success as a sensitivity calculation would give 529/615 (86.02%), not a newly judged result.

The legacy capture_unavailable diagnostic was 6 because it added four missing-image cases and two unavailable-quality cases into one key. The corrected count is 4. This is a diagnostic correction only; no task judgment or score changed.

## Evidence publication and privacy

This package contains privacy-redacted copies of the execution manifest, schedule, event logs, task records, judgments, frozen judge inputs and selected screenshots. Raw web tokens and local user/account paths were removed. Associated source hashes and input hashes were regenerated for the public derivative; original and public file hashes are paired in lineage.json (`public/lineage.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)). The public derivative is not an assertion of byte-identical historical wire requests. Original records remain unchanged.

All 611 selected screenshots underwent local OCR screening for emails, local user paths and credential labels. The only email match was a public arXiv contact address. Screening is not a guarantee of detecting every sensitive item. See [processing details](privacy-processing.json).

## Per-website results

| Website | Success / total | Rate |
| --- | --- | --- |
| Allrecipes | 39 / 40 | 97.50% |
| Amazon | 38 / 40 | 95.00% |
| Apple | 37 / 40 | 92.50% |
| ArXiv | 39 / 43 | 90.70% |
| BBC News | 33 / 39 | 84.62% |
| Booking | 31 / 40 | 77.50% |
| Cambridge Dictionary | 38 / 41 | 92.68% |
| Coursera | 37 / 40 | 92.50% |
| ESPN | 38 / 44 | 86.36% |
| GitHub | 37 / 41 | 90.24% |
| Google Flights | 19 / 40 | 47.50% |
| Google Map | 35 / 40 | 87.50% |
| Google Search | 40 / 42 | 95.24% |
| Huggingface | 30 / 39 | 76.92% |
| Wolfram Alpha | 39 / 46 | 84.78% |

## Downloads and verification

- [Recomputed summary](summary.json)
- [All 615 task results](task-results.json)
- Offline package verifier (`public/verify_package.py` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) — run `python3 public/verify_package.py` from the extracted archive root; no model/API access.
- Published-file checksums (`public/SHA256SUMS.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09))

## Task evidence index

Use Find in your browser to locate a task ID or outcome. The Evidence column lists paths **inside the downloadable archive**. Extract the archive and open public/index.html for a clickable task index. Each task directory contains run.json, judge.json, and the available evidence/input files.

| Task | Outcome | Evidence |
| --- | --- | --- |
| Allrecipes--0 | success | `public/run/tasks/Allrecipes--0/` |
| Allrecipes--1 | success | `public/run/tasks/Allrecipes--1/` |
| Allrecipes--10 | success | `public/run/tasks/Allrecipes--10/` |
| Allrecipes--11 | success | `public/run/tasks/Allrecipes--11/` |
| Allrecipes--12 | success | `public/run/tasks/Allrecipes--12/` |
| Allrecipes--13 | success | `public/run/tasks/Allrecipes--13/` |
| Allrecipes--14 | success | `public/run/tasks/Allrecipes--14/` |
| Allrecipes--15 | success | `public/run/tasks/Allrecipes--15/` |
| Allrecipes--17 | success | `public/run/tasks/Allrecipes--17/` |
| Allrecipes--18 | success | `public/run/tasks/Allrecipes--18/` |
| Allrecipes--2 | success | `public/run/tasks/Allrecipes--2/` |
| Allrecipes--20 | success | `public/run/tasks/Allrecipes--20/` |
| Allrecipes--21 | success | `public/run/tasks/Allrecipes--21/` |
| Allrecipes--22 | success | `public/run/tasks/Allrecipes--22/` |
| Allrecipes--23 | success | `public/run/tasks/Allrecipes--23/` |
| Allrecipes--24 | success | `public/run/tasks/Allrecipes--24/` |
| Allrecipes--25 | success | `public/run/tasks/Allrecipes--25/` |
| Allrecipes--26 | success | `public/run/tasks/Allrecipes--26/` |
| Allrecipes--27 | success | `public/run/tasks/Allrecipes--27/` |
| Allrecipes--28 | success | `public/run/tasks/Allrecipes--28/` |
| Allrecipes--31 | unknown | `public/run/tasks/Allrecipes--31/` |
| Allrecipes--32 | success | `public/run/tasks/Allrecipes--32/` |
| Allrecipes--33 | success | `public/run/tasks/Allrecipes--33/` |
| Allrecipes--34 | success | `public/run/tasks/Allrecipes--34/` |
| Allrecipes--35 | success | `public/run/tasks/Allrecipes--35/` |
| Allrecipes--36 | success | `public/run/tasks/Allrecipes--36/` |
| Allrecipes--37 | success | `public/run/tasks/Allrecipes--37/` |
| Allrecipes--38 | success | `public/run/tasks/Allrecipes--38/` |
| Allrecipes--39 | success | `public/run/tasks/Allrecipes--39/` |
| Allrecipes--4 | success | `public/run/tasks/Allrecipes--4/` |
| Allrecipes--40 | success | `public/run/tasks/Allrecipes--40/` |
| Allrecipes--41 | success | `public/run/tasks/Allrecipes--41/` |
| Allrecipes--42 | success | `public/run/tasks/Allrecipes--42/` |
| Allrecipes--43 | success | `public/run/tasks/Allrecipes--43/` |
| Allrecipes--44 | success | `public/run/tasks/Allrecipes--44/` |
| Allrecipes--5 | success | `public/run/tasks/Allrecipes--5/` |
| Allrecipes--6 | success | `public/run/tasks/Allrecipes--6/` |
| Allrecipes--7 | success | `public/run/tasks/Allrecipes--7/` |
| Allrecipes--8 | success | `public/run/tasks/Allrecipes--8/` |
| Allrecipes--9 | success | `public/run/tasks/Allrecipes--9/` |
| Amazon--0 | success | `public/run/tasks/Amazon--0/` |
| Amazon--1 | success | `public/run/tasks/Amazon--1/` |
| Amazon--10 | success | `public/run/tasks/Amazon--10/` |
| Amazon--11 | unknown | `public/run/tasks/Amazon--11/` |
| Amazon--12 | failure | `public/run/tasks/Amazon--12/` |
| Amazon--13 | success | `public/run/tasks/Amazon--13/` |
| Amazon--14 | success | `public/run/tasks/Amazon--14/` |
| Amazon--15 | success | `public/run/tasks/Amazon--15/` |
| Amazon--16 | success | `public/run/tasks/Amazon--16/` |
| Amazon--17 | success | `public/run/tasks/Amazon--17/` |
| Amazon--18 | success | `public/run/tasks/Amazon--18/` |
| Amazon--2 | success | `public/run/tasks/Amazon--2/` |
| Amazon--20 | success | `public/run/tasks/Amazon--20/` |
| Amazon--21 | success | `public/run/tasks/Amazon--21/` |
| Amazon--22 | success | `public/run/tasks/Amazon--22/` |
| Amazon--23 | success | `public/run/tasks/Amazon--23/` |
| Amazon--24 | success | `public/run/tasks/Amazon--24/` |
| Amazon--25 | success | `public/run/tasks/Amazon--25/` |
| Amazon--26 | success | `public/run/tasks/Amazon--26/` |
| Amazon--27 | success | `public/run/tasks/Amazon--27/` |
| Amazon--28 | success | `public/run/tasks/Amazon--28/` |
| Amazon--29 | success | `public/run/tasks/Amazon--29/` |
| Amazon--3 | success | `public/run/tasks/Amazon--3/` |
| Amazon--30 | success | `public/run/tasks/Amazon--30/` |
| Amazon--31 | success | `public/run/tasks/Amazon--31/` |
| Amazon--32 | success | `public/run/tasks/Amazon--32/` |
| Amazon--33 | success | `public/run/tasks/Amazon--33/` |
| Amazon--34 | success | `public/run/tasks/Amazon--34/` |
| Amazon--35 | success | `public/run/tasks/Amazon--35/` |
| Amazon--36 | success | `public/run/tasks/Amazon--36/` |
| Amazon--37 | success | `public/run/tasks/Amazon--37/` |
| Amazon--38 | success | `public/run/tasks/Amazon--38/` |
| Amazon--39 | success | `public/run/tasks/Amazon--39/` |
| Amazon--4 | success | `public/run/tasks/Amazon--4/` |
| Amazon--40 | success | `public/run/tasks/Amazon--40/` |
| Amazon--5 | success | `public/run/tasks/Amazon--5/` |
| Amazon--6 | success | `public/run/tasks/Amazon--6/` |
| Amazon--7 | success | `public/run/tasks/Amazon--7/` |
| Amazon--8 | success | `public/run/tasks/Amazon--8/` |
| Amazon--9 | success | `public/run/tasks/Amazon--9/` |
| Apple--0 | success | `public/run/tasks/Apple--0/` |
| Apple--1 | success | `public/run/tasks/Apple--1/` |
| Apple--10 | success | `public/run/tasks/Apple--10/` |
| Apple--11 | failure | `public/run/tasks/Apple--11/` |
| Apple--12 | success | `public/run/tasks/Apple--12/` |
| Apple--13 | success | `public/run/tasks/Apple--13/` |
| Apple--14 | success | `public/run/tasks/Apple--14/` |
| Apple--15 | success | `public/run/tasks/Apple--15/` |
| Apple--16 | success | `public/run/tasks/Apple--16/` |
| Apple--17 | failure | `public/run/tasks/Apple--17/` |
| Apple--18 | success | `public/run/tasks/Apple--18/` |
| Apple--19 | success | `public/run/tasks/Apple--19/` |
| Apple--2 | success | `public/run/tasks/Apple--2/` |
| Apple--20 | success | `public/run/tasks/Apple--20/` |
| Apple--21 | success | `public/run/tasks/Apple--21/` |
| Apple--22 | success | `public/run/tasks/Apple--22/` |
| Apple--23 | success | `public/run/tasks/Apple--23/` |
| Apple--24 | success | `public/run/tasks/Apple--24/` |
| Apple--25 | success | `public/run/tasks/Apple--25/` |
| Apple--26 | success | `public/run/tasks/Apple--26/` |
| Apple--27 | success | `public/run/tasks/Apple--27/` |
| Apple--28 | success | `public/run/tasks/Apple--28/` |
| Apple--29 | success | `public/run/tasks/Apple--29/` |
| Apple--3 | success | `public/run/tasks/Apple--3/` |
| Apple--30 | success | `public/run/tasks/Apple--30/` |
| Apple--31 | success | `public/run/tasks/Apple--31/` |
| Apple--32 | success | `public/run/tasks/Apple--32/` |
| Apple--33 | success | `public/run/tasks/Apple--33/` |
| Apple--34 | success | `public/run/tasks/Apple--34/` |
| Apple--35 | success | `public/run/tasks/Apple--35/` |
| Apple--36 | failure | `public/run/tasks/Apple--36/` |
| Apple--37 | success | `public/run/tasks/Apple--37/` |
| Apple--38 | success | `public/run/tasks/Apple--38/` |
| Apple--39 | success | `public/run/tasks/Apple--39/` |
| Apple--4 | success | `public/run/tasks/Apple--4/` |
| Apple--40 | success | `public/run/tasks/Apple--40/` |
| Apple--41 | success | `public/run/tasks/Apple--41/` |
| Apple--5 | success | `public/run/tasks/Apple--5/` |
| Apple--6 | success | `public/run/tasks/Apple--6/` |
| Apple--8 | success | `public/run/tasks/Apple--8/` |
| ArXiv--0 | success | `public/run/tasks/ArXiv--0/` |
| ArXiv--1 | success | `public/run/tasks/ArXiv--1/` |
| ArXiv--10 | success | `public/run/tasks/ArXiv--10/` |
| ArXiv--11 | run_error | `public/run/tasks/ArXiv--11/` |
| ArXiv--12 | success | `public/run/tasks/ArXiv--12/` |
| ArXiv--13 | success | `public/run/tasks/ArXiv--13/` |
| ArXiv--14 | success | `public/run/tasks/ArXiv--14/` |
| ArXiv--15 | success | `public/run/tasks/ArXiv--15/` |
| ArXiv--16 | success | `public/run/tasks/ArXiv--16/` |
| ArXiv--17 | success | `public/run/tasks/ArXiv--17/` |
| ArXiv--18 | success | `public/run/tasks/ArXiv--18/` |
| ArXiv--19 | success | `public/run/tasks/ArXiv--19/` |
| ArXiv--2 | success | `public/run/tasks/ArXiv--2/` |
| ArXiv--20 | success | `public/run/tasks/ArXiv--20/` |
| ArXiv--21 | unknown | `public/run/tasks/ArXiv--21/` |
| ArXiv--22 | success | `public/run/tasks/ArXiv--22/` |
| ArXiv--23 | success | `public/run/tasks/ArXiv--23/` |
| ArXiv--24 | run_error | `public/run/tasks/ArXiv--24/` |
| ArXiv--25 | success | `public/run/tasks/ArXiv--25/` |
| ArXiv--26 | success | `public/run/tasks/ArXiv--26/` |
| ArXiv--27 | success | `public/run/tasks/ArXiv--27/` |
| ArXiv--28 | success | `public/run/tasks/ArXiv--28/` |
| ArXiv--29 | success | `public/run/tasks/ArXiv--29/` |
| ArXiv--3 | success | `public/run/tasks/ArXiv--3/` |
| ArXiv--30 | success | `public/run/tasks/ArXiv--30/` |
| ArXiv--31 | success | `public/run/tasks/ArXiv--31/` |
| ArXiv--32 | success | `public/run/tasks/ArXiv--32/` |
| ArXiv--33 | success | `public/run/tasks/ArXiv--33/` |
| ArXiv--34 | success | `public/run/tasks/ArXiv--34/` |
| ArXiv--35 | success | `public/run/tasks/ArXiv--35/` |
| ArXiv--36 | success | `public/run/tasks/ArXiv--36/` |
| ArXiv--37 | success | `public/run/tasks/ArXiv--37/` |
| ArXiv--38 | success | `public/run/tasks/ArXiv--38/` |
| ArXiv--39 | success | `public/run/tasks/ArXiv--39/` |
| ArXiv--4 | success | `public/run/tasks/ArXiv--4/` |
| ArXiv--40 | success | `public/run/tasks/ArXiv--40/` |
| ArXiv--41 | unknown | `public/run/tasks/ArXiv--41/` |
| ArXiv--42 | success | `public/run/tasks/ArXiv--42/` |
| ArXiv--5 | success | `public/run/tasks/ArXiv--5/` |
| ArXiv--6 | success | `public/run/tasks/ArXiv--6/` |
| ArXiv--7 | success | `public/run/tasks/ArXiv--7/` |
| ArXiv--8 | success | `public/run/tasks/ArXiv--8/` |
| ArXiv--9 | success | `public/run/tasks/ArXiv--9/` |
| BBC News--0 | success | `public/run/tasks/BBC_News--0-e5bb1a1a/` |
| BBC News--1 | success | `public/run/tasks/BBC_News--1-c9f4b85f/` |
| BBC News--10 | success | `public/run/tasks/BBC_News--10-51935bbe/` |
| BBC News--11 | failure | `public/run/tasks/BBC_News--11-97cd9969/` |
| BBC News--12 | success | `public/run/tasks/BBC_News--12-731d1d8a/` |
| BBC News--13 | judge_error | `public/run/tasks/BBC_News--13-88ed6f0f/` |
| BBC News--14 | success | `public/run/tasks/BBC_News--14-712aed09/` |
| BBC News--15 | success | `public/run/tasks/BBC_News--15-a5c94506/` |
| BBC News--16 | success | `public/run/tasks/BBC_News--16-44165f16/` |
| BBC News--17 | success | `public/run/tasks/BBC_News--17-2a7bf749/` |
| BBC News--19 | success | `public/run/tasks/BBC_News--19-d57276ac/` |
| BBC News--2 | success | `public/run/tasks/BBC_News--2-439161ec/` |
| BBC News--20 | success | `public/run/tasks/BBC_News--20-d724189e/` |
| BBC News--21 | success | `public/run/tasks/BBC_News--21-d1cc0d39/` |
| BBC News--22 | success | `public/run/tasks/BBC_News--22-21d45cca/` |
| BBC News--23 | success | `public/run/tasks/BBC_News--23-c58913d2/` |
| BBC News--24 | success | `public/run/tasks/BBC_News--24-b5b08e46/` |
| BBC News--25 | success | `public/run/tasks/BBC_News--25-b49cff27/` |
| BBC News--26 | success | `public/run/tasks/BBC_News--26-f4cc1cad/` |
| BBC News--27 | success | `public/run/tasks/BBC_News--27-066d111a/` |
| BBC News--28 | success | `public/run/tasks/BBC_News--28-9f78fc99/` |
| BBC News--3 | failure | `public/run/tasks/BBC_News--3-c4f43fa9/` |
| BBC News--30 | failure | `public/run/tasks/BBC_News--30-13d5b4ba/` |
| BBC News--31 | success | `public/run/tasks/BBC_News--31-e46f7a75/` |
| BBC News--32 | success | `public/run/tasks/BBC_News--32-45ca330b/` |
| BBC News--33 | success | `public/run/tasks/BBC_News--33-b0d62f0c/` |
| BBC News--34 | failure | `public/run/tasks/BBC_News--34-4d0752ca/` |
| BBC News--35 | success | `public/run/tasks/BBC_News--35-8a3a8bd2/` |
| BBC News--36 | success | `public/run/tasks/BBC_News--36-a6205557/` |
| BBC News--38 | success | `public/run/tasks/BBC_News--38-e7059e14/` |
| BBC News--39 | success | `public/run/tasks/BBC_News--39-0f40ab4d/` |
| BBC News--4 | success | `public/run/tasks/BBC_News--4-5c1f27af/` |
| BBC News--40 | success | `public/run/tasks/BBC_News--40-3bb669b4/` |
| BBC News--41 | success | `public/run/tasks/BBC_News--41-a3c02e2e/` |
| BBC News--5 | success | `public/run/tasks/BBC_News--5-1e2809f5/` |
| BBC News--6 | success | `public/run/tasks/BBC_News--6-b5b7afbc/` |
| BBC News--7 | success | `public/run/tasks/BBC_News--7-fcd100d5/` |
| BBC News--8 | run_error | `public/run/tasks/BBC_News--8-94d708f3/` |
| BBC News--9 | success | `public/run/tasks/BBC_News--9-ff632875/` |
| Booking--0 | success | `public/run/tasks/Booking--0/` |
| Booking--1 | success | `public/run/tasks/Booking--1/` |
| Booking--10 | success | `public/run/tasks/Booking--10/` |
| Booking--12 | failure | `public/run/tasks/Booking--12/` |
| Booking--15 | success | `public/run/tasks/Booking--15/` |
| Booking--16 | success | `public/run/tasks/Booking--16/` |
| Booking--17 | success | `public/run/tasks/Booking--17/` |
| Booking--18 | success | `public/run/tasks/Booking--18/` |
| Booking--19 | unknown | `public/run/tasks/Booking--19/` |
| Booking--2 | success | `public/run/tasks/Booking--2/` |
| Booking--20 | success | `public/run/tasks/Booking--20/` |
| Booking--21 | success | `public/run/tasks/Booking--21/` |
| Booking--22 | success | `public/run/tasks/Booking--22/` |
| Booking--23 | failure | `public/run/tasks/Booking--23/` |
| Booking--24 | success | `public/run/tasks/Booking--24/` |
| Booking--25 | failure | `public/run/tasks/Booking--25/` |
| Booking--26 | success | `public/run/tasks/Booking--26/` |
| Booking--27 | unknown | `public/run/tasks/Booking--27/` |
| Booking--28 | success | `public/run/tasks/Booking--28/` |
| Booking--29 | success | `public/run/tasks/Booking--29/` |
| Booking--3 | success | `public/run/tasks/Booking--3/` |
| Booking--30 | failure | `public/run/tasks/Booking--30/` |
| Booking--31 | success | `public/run/tasks/Booking--31/` |
| Booking--32 | success | `public/run/tasks/Booking--32/` |
| Booking--33 | success | `public/run/tasks/Booking--33/` |
| Booking--34 | failure | `public/run/tasks/Booking--34/` |
| Booking--35 | success | `public/run/tasks/Booking--35/` |
| Booking--36 | failure | `public/run/tasks/Booking--36/` |
| Booking--37 | success | `public/run/tasks/Booking--37/` |
| Booking--38 | success | `public/run/tasks/Booking--38/` |
| Booking--39 | success | `public/run/tasks/Booking--39/` |
| Booking--4 | success | `public/run/tasks/Booking--4/` |
| Booking--40 | success | `public/run/tasks/Booking--40/` |
| Booking--41 | success | `public/run/tasks/Booking--41/` |
| Booking--42 | success | `public/run/tasks/Booking--42/` |
| Booking--43 | success | `public/run/tasks/Booking--43/` |
| Booking--5 | failure | `public/run/tasks/Booking--5/` |
| Booking--7 | success | `public/run/tasks/Booking--7/` |
| Booking--8 | success | `public/run/tasks/Booking--8/` |
| Booking--9 | success | `public/run/tasks/Booking--9/` |
| Cambridge Dictionary--0 | success | `public/run/tasks/Cambridge_Dictionary--0-f8879c66/` |
| Cambridge Dictionary--1 | success | `public/run/tasks/Cambridge_Dictionary--1-f2ab4515/` |
| Cambridge Dictionary--10 | failure | `public/run/tasks/Cambridge_Dictionary--10-37ad8327/` |
| Cambridge Dictionary--11 | success | `public/run/tasks/Cambridge_Dictionary--11-f66e0674/` |
| Cambridge Dictionary--12 | success | `public/run/tasks/Cambridge_Dictionary--12-3502a448/` |
| Cambridge Dictionary--13 | success | `public/run/tasks/Cambridge_Dictionary--13-e815da64/` |
| Cambridge Dictionary--14 | success | `public/run/tasks/Cambridge_Dictionary--14-3c0ff744/` |
| Cambridge Dictionary--15 | success | `public/run/tasks/Cambridge_Dictionary--15-afba8e38/` |
| Cambridge Dictionary--16 | success | `public/run/tasks/Cambridge_Dictionary--16-67f5363b/` |
| Cambridge Dictionary--17 | success | `public/run/tasks/Cambridge_Dictionary--17-fb6a9bea/` |
| Cambridge Dictionary--18 | success | `public/run/tasks/Cambridge_Dictionary--18-3980edff/` |
| Cambridge Dictionary--2 | success | `public/run/tasks/Cambridge_Dictionary--2-e8ed0a66/` |
| Cambridge Dictionary--20 | success | `public/run/tasks/Cambridge_Dictionary--20-5df3708c/` |
| Cambridge Dictionary--21 | success | `public/run/tasks/Cambridge_Dictionary--21-88055b92/` |
| Cambridge Dictionary--22 | success | `public/run/tasks/Cambridge_Dictionary--22-5ad4d55e/` |
| Cambridge Dictionary--23 | success | `public/run/tasks/Cambridge_Dictionary--23-0cef03ef/` |
| Cambridge Dictionary--24 | success | `public/run/tasks/Cambridge_Dictionary--24-dd1a8de1/` |
| Cambridge Dictionary--25 | success | `public/run/tasks/Cambridge_Dictionary--25-ef9d49f2/` |
| Cambridge Dictionary--26 | success | `public/run/tasks/Cambridge_Dictionary--26-57fcc417/` |
| Cambridge Dictionary--27 | success | `public/run/tasks/Cambridge_Dictionary--27-cd6d1c22/` |
| Cambridge Dictionary--28 | success | `public/run/tasks/Cambridge_Dictionary--28-92e4101e/` |
| Cambridge Dictionary--29 | success | `public/run/tasks/Cambridge_Dictionary--29-dbcac4de/` |
| Cambridge Dictionary--3 | success | `public/run/tasks/Cambridge_Dictionary--3-5920dda5/` |
| Cambridge Dictionary--30 | success | `public/run/tasks/Cambridge_Dictionary--30-01cc1698/` |
| Cambridge Dictionary--31 | success | `public/run/tasks/Cambridge_Dictionary--31-bff22cc2/` |
| Cambridge Dictionary--32 | success | `public/run/tasks/Cambridge_Dictionary--32-a6bc1f47/` |
| Cambridge Dictionary--33 | success | `public/run/tasks/Cambridge_Dictionary--33-9ca7301c/` |
| Cambridge Dictionary--34 | success | `public/run/tasks/Cambridge_Dictionary--34-afaea524/` |
| Cambridge Dictionary--35 | success | `public/run/tasks/Cambridge_Dictionary--35-c03105bd/` |
| Cambridge Dictionary--36 | success | `public/run/tasks/Cambridge_Dictionary--36-c9cd1327/` |
| Cambridge Dictionary--37 | success | `public/run/tasks/Cambridge_Dictionary--37-38515393/` |
| Cambridge Dictionary--38 | failure | `public/run/tasks/Cambridge_Dictionary--38-865c955f/` |
| Cambridge Dictionary--39 | failure | `public/run/tasks/Cambridge_Dictionary--39-53c43d56/` |
| Cambridge Dictionary--4 | success | `public/run/tasks/Cambridge_Dictionary--4-61f10447/` |
| Cambridge Dictionary--40 | success | `public/run/tasks/Cambridge_Dictionary--40-4a0a526e/` |
| Cambridge Dictionary--42 | success | `public/run/tasks/Cambridge_Dictionary--42-3618230d/` |
| Cambridge Dictionary--5 | success | `public/run/tasks/Cambridge_Dictionary--5-827f4083/` |
| Cambridge Dictionary--6 | success | `public/run/tasks/Cambridge_Dictionary--6-4d871d7c/` |
| Cambridge Dictionary--7 | success | `public/run/tasks/Cambridge_Dictionary--7-0ff353c0/` |
| Cambridge Dictionary--8 | success | `public/run/tasks/Cambridge_Dictionary--8-ffbfefb8/` |
| Cambridge Dictionary--9 | success | `public/run/tasks/Cambridge_Dictionary--9-7dbf578a/` |
| Coursera--0 | success | `public/run/tasks/Coursera--0/` |
| Coursera--1 | success | `public/run/tasks/Coursera--1/` |
| Coursera--10 | success | `public/run/tasks/Coursera--10/` |
| Coursera--11 | success | `public/run/tasks/Coursera--11/` |
| Coursera--12 | success | `public/run/tasks/Coursera--12/` |
| Coursera--13 | success | `public/run/tasks/Coursera--13/` |
| Coursera--14 | success | `public/run/tasks/Coursera--14/` |
| Coursera--15 | success | `public/run/tasks/Coursera--15/` |
| Coursera--16 | success | `public/run/tasks/Coursera--16/` |
| Coursera--18 | success | `public/run/tasks/Coursera--18/` |
| Coursera--19 | success | `public/run/tasks/Coursera--19/` |
| Coursera--2 | success | `public/run/tasks/Coursera--2/` |
| Coursera--20 | success | `public/run/tasks/Coursera--20/` |
| Coursera--21 | success | `public/run/tasks/Coursera--21/` |
| Coursera--22 | success | `public/run/tasks/Coursera--22/` |
| Coursera--23 | success | `public/run/tasks/Coursera--23/` |
| Coursera--24 | success | `public/run/tasks/Coursera--24/` |
| Coursera--25 | success | `public/run/tasks/Coursera--25/` |
| Coursera--26 | success | `public/run/tasks/Coursera--26/` |
| Coursera--27 | success | `public/run/tasks/Coursera--27/` |
| Coursera--29 | success | `public/run/tasks/Coursera--29/` |
| Coursera--3 | success | `public/run/tasks/Coursera--3/` |
| Coursera--30 | success | `public/run/tasks/Coursera--30/` |
| Coursera--31 | success | `public/run/tasks/Coursera--31/` |
| Coursera--32 | failure | `public/run/tasks/Coursera--32/` |
| Coursera--33 | success | `public/run/tasks/Coursera--33/` |
| Coursera--34 | success | `public/run/tasks/Coursera--34/` |
| Coursera--35 | success | `public/run/tasks/Coursera--35/` |
| Coursera--36 | success | `public/run/tasks/Coursera--36/` |
| Coursera--37 | success | `public/run/tasks/Coursera--37/` |
| Coursera--38 | unknown | `public/run/tasks/Coursera--38/` |
| Coursera--39 | success | `public/run/tasks/Coursera--39/` |
| Coursera--4 | success | `public/run/tasks/Coursera--4/` |
| Coursera--40 | success | `public/run/tasks/Coursera--40/` |
| Coursera--41 | success | `public/run/tasks/Coursera--41/` |
| Coursera--5 | success | `public/run/tasks/Coursera--5/` |
| Coursera--6 | success | `public/run/tasks/Coursera--6/` |
| Coursera--7 | success | `public/run/tasks/Coursera--7/` |
| Coursera--8 | failure | `public/run/tasks/Coursera--8/` |
| Coursera--9 | success | `public/run/tasks/Coursera--9/` |
| ESPN--0 | success | `public/run/tasks/ESPN--0/` |
| ESPN--1 | success | `public/run/tasks/ESPN--1/` |
| ESPN--10 | success | `public/run/tasks/ESPN--10/` |
| ESPN--11 | success | `public/run/tasks/ESPN--11/` |
| ESPN--12 | success | `public/run/tasks/ESPN--12/` |
| ESPN--13 | success | `public/run/tasks/ESPN--13/` |
| ESPN--14 | unknown | `public/run/tasks/ESPN--14/` |
| ESPN--15 | success | `public/run/tasks/ESPN--15/` |
| ESPN--16 | failure | `public/run/tasks/ESPN--16/` |
| ESPN--17 | success | `public/run/tasks/ESPN--17/` |
| ESPN--18 | success | `public/run/tasks/ESPN--18/` |
| ESPN--19 | success | `public/run/tasks/ESPN--19/` |
| ESPN--2 | success | `public/run/tasks/ESPN--2/` |
| ESPN--20 | success | `public/run/tasks/ESPN--20/` |
| ESPN--21 | success | `public/run/tasks/ESPN--21/` |
| ESPN--22 | success | `public/run/tasks/ESPN--22/` |
| ESPN--23 | success | `public/run/tasks/ESPN--23/` |
| ESPN--24 | success | `public/run/tasks/ESPN--24/` |
| ESPN--25 | success | `public/run/tasks/ESPN--25/` |
| ESPN--26 | success | `public/run/tasks/ESPN--26/` |
| ESPN--27 | success | `public/run/tasks/ESPN--27/` |
| ESPN--28 | success | `public/run/tasks/ESPN--28/` |
| ESPN--29 | success | `public/run/tasks/ESPN--29/` |
| ESPN--3 | success | `public/run/tasks/ESPN--3/` |
| ESPN--30 | success | `public/run/tasks/ESPN--30/` |
| ESPN--31 | success | `public/run/tasks/ESPN--31/` |
| ESPN--32 | success | `public/run/tasks/ESPN--32/` |
| ESPN--33 | failure | `public/run/tasks/ESPN--33/` |
| ESPN--34 | success | `public/run/tasks/ESPN--34/` |
| ESPN--35 | failure | `public/run/tasks/ESPN--35/` |
| ESPN--36 | success | `public/run/tasks/ESPN--36/` |
| ESPN--37 | success | `public/run/tasks/ESPN--37/` |
| ESPN--38 | success | `public/run/tasks/ESPN--38/` |
| ESPN--39 | success | `public/run/tasks/ESPN--39/` |
| ESPN--4 | success | `public/run/tasks/ESPN--4/` |
| ESPN--40 | failure | `public/run/tasks/ESPN--40/` |
| ESPN--41 | success | `public/run/tasks/ESPN--41/` |
| ESPN--42 | success | `public/run/tasks/ESPN--42/` |
| ESPN--43 | success | `public/run/tasks/ESPN--43/` |
| ESPN--5 | unknown | `public/run/tasks/ESPN--5/` |
| ESPN--6 | success | `public/run/tasks/ESPN--6/` |
| ESPN--7 | success | `public/run/tasks/ESPN--7/` |
| ESPN--8 | success | `public/run/tasks/ESPN--8/` |
| ESPN--9 | success | `public/run/tasks/ESPN--9/` |
| GitHub--0 | success | `public/run/tasks/GitHub--0/` |
| GitHub--1 | success | `public/run/tasks/GitHub--1/` |
| GitHub--10 | success | `public/run/tasks/GitHub--10/` |
| GitHub--11 | success | `public/run/tasks/GitHub--11/` |
| GitHub--12 | success | `public/run/tasks/GitHub--12/` |
| GitHub--13 | success | `public/run/tasks/GitHub--13/` |
| GitHub--14 | success | `public/run/tasks/GitHub--14/` |
| GitHub--15 | success | `public/run/tasks/GitHub--15/` |
| GitHub--16 | success | `public/run/tasks/GitHub--16/` |
| GitHub--17 | success | `public/run/tasks/GitHub--17/` |
| GitHub--18 | success | `public/run/tasks/GitHub--18/` |
| GitHub--19 | success | `public/run/tasks/GitHub--19/` |
| GitHub--2 | success | `public/run/tasks/GitHub--2/` |
| GitHub--20 | success | `public/run/tasks/GitHub--20/` |
| GitHub--21 | success | `public/run/tasks/GitHub--21/` |
| GitHub--22 | success | `public/run/tasks/GitHub--22/` |
| GitHub--23 | success | `public/run/tasks/GitHub--23/` |
| GitHub--24 | success | `public/run/tasks/GitHub--24/` |
| GitHub--25 | success | `public/run/tasks/GitHub--25/` |
| GitHub--26 | success | `public/run/tasks/GitHub--26/` |
| GitHub--27 | success | `public/run/tasks/GitHub--27/` |
| GitHub--28 | success | `public/run/tasks/GitHub--28/` |
| GitHub--29 | run_error | `public/run/tasks/GitHub--29/` |
| GitHub--3 | success | `public/run/tasks/GitHub--3/` |
| GitHub--30 | unknown | `public/run/tasks/GitHub--30/` |
| GitHub--31 | success | `public/run/tasks/GitHub--31/` |
| GitHub--32 | success | `public/run/tasks/GitHub--32/` |
| GitHub--33 | success | `public/run/tasks/GitHub--33/` |
| GitHub--34 | success | `public/run/tasks/GitHub--34/` |
| GitHub--35 | success | `public/run/tasks/GitHub--35/` |
| GitHub--36 | unknown | `public/run/tasks/GitHub--36/` |
| GitHub--37 | success | `public/run/tasks/GitHub--37/` |
| GitHub--38 | success | `public/run/tasks/GitHub--38/` |
| GitHub--39 | success | `public/run/tasks/GitHub--39/` |
| GitHub--4 | success | `public/run/tasks/GitHub--4/` |
| GitHub--40 | failure | `public/run/tasks/GitHub--40/` |
| GitHub--5 | success | `public/run/tasks/GitHub--5/` |
| GitHub--6 | success | `public/run/tasks/GitHub--6/` |
| GitHub--7 | success | `public/run/tasks/GitHub--7/` |
| GitHub--8 | success | `public/run/tasks/GitHub--8/` |
| GitHub--9 | success | `public/run/tasks/GitHub--9/` |
| Google Flights--1 | success | `public/run/tasks/Google_Flights--1-6430440f/` |
| Google Flights--10 | success | `public/run/tasks/Google_Flights--10-856d53c6/` |
| Google Flights--11 | failure | `public/run/tasks/Google_Flights--11-10ec2435/` |
| Google Flights--12 | run_error | `public/run/tasks/Google_Flights--12-efe4be30/` |
| Google Flights--13 | failure | `public/run/tasks/Google_Flights--13-28c3f17b/` |
| Google Flights--14 | success | `public/run/tasks/Google_Flights--14-d9d305e1/` |
| Google Flights--15 | unknown | `public/run/tasks/Google_Flights--15-86797a6b/` |
| Google Flights--16 | failure | `public/run/tasks/Google_Flights--16-3705f391/` |
| Google Flights--17 | run_error | `public/run/tasks/Google_Flights--17-6dbf5ada/` |
| Google Flights--18 | failure | `public/run/tasks/Google_Flights--18-c1a2c448/` |
| Google Flights--19 | success | `public/run/tasks/Google_Flights--19-a814418f/` |
| Google Flights--2 | success | `public/run/tasks/Google_Flights--2-25dde526/` |
| Google Flights--21 | failure | `public/run/tasks/Google_Flights--21-c49471ef/` |
| Google Flights--22 | failure | `public/run/tasks/Google_Flights--22-3e0d80ec/` |
| Google Flights--23 | failure | `public/run/tasks/Google_Flights--23-f38d45ce/` |
| Google Flights--24 | success | `public/run/tasks/Google_Flights--24-e32811e0/` |
| Google Flights--25 | failure | `public/run/tasks/Google_Flights--25-b48eb20f/` |
| Google Flights--26 | success | `public/run/tasks/Google_Flights--26-cb692541/` |
| Google Flights--27 | run_error | `public/run/tasks/Google_Flights--27-18b68bd0/` |
| Google Flights--28 | success | `public/run/tasks/Google_Flights--28-0741cc6b/` |
| Google Flights--29 | failure | `public/run/tasks/Google_Flights--29-27389750/` |
| Google Flights--3 | success | `public/run/tasks/Google_Flights--3-fa1c3e65/` |
| Google Flights--30 | run_error | `public/run/tasks/Google_Flights--30-e149e942/` |
| Google Flights--31 | success | `public/run/tasks/Google_Flights--31-aff703ed/` |
| Google Flights--32 | failure | `public/run/tasks/Google_Flights--32-3d351b7c/` |
| Google Flights--33 | success | `public/run/tasks/Google_Flights--33-9d4f6226/` |
| Google Flights--34 | failure | `public/run/tasks/Google_Flights--34-1dae5fdc/` |
| Google Flights--35 | success | `public/run/tasks/Google_Flights--35-581b69b5/` |
| Google Flights--36 | success | `public/run/tasks/Google_Flights--36-0afea5d5/` |
| Google Flights--37 | failure | `public/run/tasks/Google_Flights--37-85bf5bf5/` |
| Google Flights--38 | failure | `public/run/tasks/Google_Flights--38-aa5c50d0/` |
| Google Flights--39 | success | `public/run/tasks/Google_Flights--39-33a5cd2b/` |
| Google Flights--4 | failure | `public/run/tasks/Google_Flights--4-46ff3c66/` |
| Google Flights--40 | success | `public/run/tasks/Google_Flights--40-2822d59c/` |
| Google Flights--41 | failure | `public/run/tasks/Google_Flights--41-4c975cee/` |
| Google Flights--5 | success | `public/run/tasks/Google_Flights--5-7edac12b/` |
| Google Flights--6 | success | `public/run/tasks/Google_Flights--6-bdf8b9a3/` |
| Google Flights--7 | success | `public/run/tasks/Google_Flights--7-5994eb2e/` |
| Google Flights--8 | failure | `public/run/tasks/Google_Flights--8-36451344/` |
| Google Flights--9 | success | `public/run/tasks/Google_Flights--9-ba4c7612/` |
| Google Map--0 | success | `public/run/tasks/Google_Map--0-9cc78c42/` |
| Google Map--1 | success | `public/run/tasks/Google_Map--1-df00a50a/` |
| Google Map--10 | success | `public/run/tasks/Google_Map--10-e94494fc/` |
| Google Map--11 | failure | `public/run/tasks/Google_Map--11-a84d7626/` |
| Google Map--12 | success | `public/run/tasks/Google_Map--12-ccd39b98/` |
| Google Map--14 | success | `public/run/tasks/Google_Map--14-ea396946/` |
| Google Map--15 | unknown | `public/run/tasks/Google_Map--15-736d1656/` |
| Google Map--16 | success | `public/run/tasks/Google_Map--16-70a8f66a/` |
| Google Map--17 | success | `public/run/tasks/Google_Map--17-1b68effb/` |
| Google Map--18 | success | `public/run/tasks/Google_Map--18-ffc0bc53/` |
| Google Map--19 | success | `public/run/tasks/Google_Map--19-1299b850/` |
| Google Map--2 | success | `public/run/tasks/Google_Map--2-c8fd4d4a/` |
| Google Map--20 | success | `public/run/tasks/Google_Map--20-31187d0e/` |
| Google Map--21 | success | `public/run/tasks/Google_Map--21-c067526e/` |
| Google Map--22 | success | `public/run/tasks/Google_Map--22-57ce6179/` |
| Google Map--23 | success | `public/run/tasks/Google_Map--23-17ca238a/` |
| Google Map--24 | success | `public/run/tasks/Google_Map--24-2e092371/` |
| Google Map--25 | success | `public/run/tasks/Google_Map--25-6fe971b6/` |
| Google Map--26 | failure | `public/run/tasks/Google_Map--26-286ef694/` |
| Google Map--27 | success | `public/run/tasks/Google_Map--27-97cb39cf/` |
| Google Map--28 | success | `public/run/tasks/Google_Map--28-5976ad11/` |
| Google Map--29 | success | `public/run/tasks/Google_Map--29-c2d69e14/` |
| Google Map--3 | success | `public/run/tasks/Google_Map--3-c655da6f/` |
| Google Map--30 | success | `public/run/tasks/Google_Map--30-d45977c9/` |
| Google Map--31 | failure | `public/run/tasks/Google_Map--31-b8fd43e9/` |
| Google Map--32 | success | `public/run/tasks/Google_Map--32-cc6e814e/` |
| Google Map--33 | failure | `public/run/tasks/Google_Map--33-99c24cfd/` |
| Google Map--34 | success | `public/run/tasks/Google_Map--34-451104bc/` |
| Google Map--35 | success | `public/run/tasks/Google_Map--35-3935cf65/` |
| Google Map--36 | success | `public/run/tasks/Google_Map--36-e95124eb/` |
| Google Map--37 | success | `public/run/tasks/Google_Map--37-f3fec192/` |
| Google Map--38 | success | `public/run/tasks/Google_Map--38-d7a4dfb7/` |
| Google Map--39 | success | `public/run/tasks/Google_Map--39-a7534313/` |
| Google Map--4 | success | `public/run/tasks/Google_Map--4-f4dbcd92/` |
| Google Map--40 | success | `public/run/tasks/Google_Map--40-5ebccaec/` |
| Google Map--5 | success | `public/run/tasks/Google_Map--5-252329ad/` |
| Google Map--6 | success | `public/run/tasks/Google_Map--6-3097039e/` |
| Google Map--7 | success | `public/run/tasks/Google_Map--7-989b450e/` |
| Google Map--8 | success | `public/run/tasks/Google_Map--8-3e57ec02/` |
| Google Map--9 | success | `public/run/tasks/Google_Map--9-1835ffcb/` |
| Google Search--0 | success | `public/run/tasks/Google_Search--0-da3f8302/` |
| Google Search--1 | success | `public/run/tasks/Google_Search--1-a5216fdb/` |
| Google Search--10 | success | `public/run/tasks/Google_Search--10-84406e9b/` |
| Google Search--11 | success | `public/run/tasks/Google_Search--11-f393b134/` |
| Google Search--12 | success | `public/run/tasks/Google_Search--12-9fdaf316/` |
| Google Search--13 | success | `public/run/tasks/Google_Search--13-384c820d/` |
| Google Search--14 | success | `public/run/tasks/Google_Search--14-0ae3a1b5/` |
| Google Search--15 | success | `public/run/tasks/Google_Search--15-a1e56ec4/` |
| Google Search--16 | success | `public/run/tasks/Google_Search--16-7c4fb393/` |
| Google Search--17 | success | `public/run/tasks/Google_Search--17-6416ca57/` |
| Google Search--18 | success | `public/run/tasks/Google_Search--18-a383d1d2/` |
| Google Search--19 | success | `public/run/tasks/Google_Search--19-2462f298/` |
| Google Search--2 | success | `public/run/tasks/Google_Search--2-75ee47c2/` |
| Google Search--20 | success | `public/run/tasks/Google_Search--20-27f5480e/` |
| Google Search--21 | success | `public/run/tasks/Google_Search--21-fa4c623c/` |
| Google Search--23 | success | `public/run/tasks/Google_Search--23-aa874193/` |
| Google Search--24 | success | `public/run/tasks/Google_Search--24-a4d65fc7/` |
| Google Search--25 | success | `public/run/tasks/Google_Search--25-98533782/` |
| Google Search--26 | success | `public/run/tasks/Google_Search--26-3aba3613/` |
| Google Search--27 | success | `public/run/tasks/Google_Search--27-2e450930/` |
| Google Search--28 | success | `public/run/tasks/Google_Search--28-e094575d/` |
| Google Search--29 | success | `public/run/tasks/Google_Search--29-131c2650/` |
| Google Search--3 | success | `public/run/tasks/Google_Search--3-4d6b7e66/` |
| Google Search--30 | success | `public/run/tasks/Google_Search--30-11e91fc7/` |
| Google Search--31 | success | `public/run/tasks/Google_Search--31-f9a9e0de/` |
| Google Search--32 | success | `public/run/tasks/Google_Search--32-2837ec92/` |
| Google Search--33 | success | `public/run/tasks/Google_Search--33-73a83bec/` |
| Google Search--34 | success | `public/run/tasks/Google_Search--34-51eab69b/` |
| Google Search--35 | success | `public/run/tasks/Google_Search--35-60ea9c2e/` |
| Google Search--36 | success | `public/run/tasks/Google_Search--36-82469dd2/` |
| Google Search--37 | success | `public/run/tasks/Google_Search--37-0d8760e3/` |
| Google Search--38 | success | `public/run/tasks/Google_Search--38-2bbddc27/` |
| Google Search--39 | success | `public/run/tasks/Google_Search--39-245ea772/` |
| Google Search--4 | success | `public/run/tasks/Google_Search--4-049e8ab5/` |
| Google Search--40 | success | `public/run/tasks/Google_Search--40-4bd6348d/` |
| Google Search--41 | success | `public/run/tasks/Google_Search--41-c67e5df8/` |
| Google Search--42 | success | `public/run/tasks/Google_Search--42-13f431d5/` |
| Google Search--5 | success | `public/run/tasks/Google_Search--5-2ea2e97d/` |
| Google Search--6 | failure | `public/run/tasks/Google_Search--6-a0352657/` |
| Google Search--7 | success | `public/run/tasks/Google_Search--7-e27ef47a/` |
| Google Search--8 | judge_error | `public/run/tasks/Google_Search--8-81d649a1/` |
| Google Search--9 | success | `public/run/tasks/Google_Search--9-3c147cc9/` |
| Huggingface--0 | unknown | `public/run/tasks/Huggingface--0/` |
| Huggingface--11 | unknown | `public/run/tasks/Huggingface--11/` |
| Huggingface--12 | success | `public/run/tasks/Huggingface--12/` |
| Huggingface--13 | success | `public/run/tasks/Huggingface--13/` |
| Huggingface--14 | success | `public/run/tasks/Huggingface--14/` |
| Huggingface--15 | success | `public/run/tasks/Huggingface--15/` |
| Huggingface--16 | success | `public/run/tasks/Huggingface--16/` |
| Huggingface--17 | unknown | `public/run/tasks/Huggingface--17/` |
| Huggingface--18 | run_error | `public/run/tasks/Huggingface--18/` |
| Huggingface--19 | failure | `public/run/tasks/Huggingface--19/` |
| Huggingface--2 | success | `public/run/tasks/Huggingface--2/` |
| Huggingface--20 | success | `public/run/tasks/Huggingface--20/` |
| Huggingface--21 | success | `public/run/tasks/Huggingface--21/` |
| Huggingface--22 | run_error | `public/run/tasks/Huggingface--22/` |
| Huggingface--23 | success | `public/run/tasks/Huggingface--23/` |
| Huggingface--24 | success | `public/run/tasks/Huggingface--24/` |
| Huggingface--25 | success | `public/run/tasks/Huggingface--25/` |
| Huggingface--26 | success | `public/run/tasks/Huggingface--26/` |
| Huggingface--27 | success | `public/run/tasks/Huggingface--27/` |
| Huggingface--28 | success | `public/run/tasks/Huggingface--28/` |
| Huggingface--29 | success | `public/run/tasks/Huggingface--29/` |
| Huggingface--3 | success | `public/run/tasks/Huggingface--3/` |
| Huggingface--30 | success | `public/run/tasks/Huggingface--30/` |
| Huggingface--31 | unknown | `public/run/tasks/Huggingface--31/` |
| Huggingface--33 | success | `public/run/tasks/Huggingface--33/` |
| Huggingface--34 | run_error | `public/run/tasks/Huggingface--34/` |
| Huggingface--35 | success | `public/run/tasks/Huggingface--35/` |
| Huggingface--36 | success | `public/run/tasks/Huggingface--36/` |
| Huggingface--37 | success | `public/run/tasks/Huggingface--37/` |
| Huggingface--38 | success | `public/run/tasks/Huggingface--38/` |
| Huggingface--39 | success | `public/run/tasks/Huggingface--39/` |
| Huggingface--4 | success | `public/run/tasks/Huggingface--4/` |
| Huggingface--40 | success | `public/run/tasks/Huggingface--40/` |
| Huggingface--41 | unknown | `public/run/tasks/Huggingface--41/` |
| Huggingface--42 | success | `public/run/tasks/Huggingface--42/` |
| Huggingface--5 | success | `public/run/tasks/Huggingface--5/` |
| Huggingface--7 | success | `public/run/tasks/Huggingface--7/` |
| Huggingface--8 | success | `public/run/tasks/Huggingface--8/` |
| Huggingface--9 | success | `public/run/tasks/Huggingface--9/` |
| Wolfram Alpha--0 | success | `public/run/tasks/Wolfram_Alpha--0-fe87e19a/` |
| Wolfram Alpha--1 | unknown | `public/run/tasks/Wolfram_Alpha--1-18ea5c0f/` |
| Wolfram Alpha--10 | success | `public/run/tasks/Wolfram_Alpha--10-c9ccdc0e/` |
| Wolfram Alpha--11 | success | `public/run/tasks/Wolfram_Alpha--11-3c8f7500/` |
| Wolfram Alpha--12 | success | `public/run/tasks/Wolfram_Alpha--12-30cb4eed/` |
| Wolfram Alpha--13 | success | `public/run/tasks/Wolfram_Alpha--13-d9b594f0/` |
| Wolfram Alpha--14 | unknown | `public/run/tasks/Wolfram_Alpha--14-ba4baad0/` |
| Wolfram Alpha--15 | success | `public/run/tasks/Wolfram_Alpha--15-8fd214e9/` |
| Wolfram Alpha--16 | success | `public/run/tasks/Wolfram_Alpha--16-143817b9/` |
| Wolfram Alpha--17 | success | `public/run/tasks/Wolfram_Alpha--17-8f2e4160/` |
| Wolfram Alpha--18 | failure | `public/run/tasks/Wolfram_Alpha--18-d028edd1/` |
| Wolfram Alpha--19 | success | `public/run/tasks/Wolfram_Alpha--19-84692184/` |
| Wolfram Alpha--2 | success | `public/run/tasks/Wolfram_Alpha--2-63be3139/` |
| Wolfram Alpha--20 | success | `public/run/tasks/Wolfram_Alpha--20-54783b39/` |
| Wolfram Alpha--21 | success | `public/run/tasks/Wolfram_Alpha--21-f4c40e3a/` |
| Wolfram Alpha--22 | success | `public/run/tasks/Wolfram_Alpha--22-1f9a2b74/` |
| Wolfram Alpha--23 | success | `public/run/tasks/Wolfram_Alpha--23-5698b7e0/` |
| Wolfram Alpha--24 | success | `public/run/tasks/Wolfram_Alpha--24-37677847/` |
| Wolfram Alpha--25 | success | `public/run/tasks/Wolfram_Alpha--25-e5211e76/` |
| Wolfram Alpha--26 | success | `public/run/tasks/Wolfram_Alpha--26-c416a66c/` |
| Wolfram Alpha--27 | success | `public/run/tasks/Wolfram_Alpha--27-b9a4af4e/` |
| Wolfram Alpha--28 | success | `public/run/tasks/Wolfram_Alpha--28-0fe0d9d9/` |
| Wolfram Alpha--29 | success | `public/run/tasks/Wolfram_Alpha--29-8c0f1f62/` |
| Wolfram Alpha--3 | success | `public/run/tasks/Wolfram_Alpha--3-a0017309/` |
| Wolfram Alpha--30 | success | `public/run/tasks/Wolfram_Alpha--30-461b0e3d/` |
| Wolfram Alpha--31 | success | `public/run/tasks/Wolfram_Alpha--31-3aa4e3bd/` |
| Wolfram Alpha--32 | success | `public/run/tasks/Wolfram_Alpha--32-590e548e/` |
| Wolfram Alpha--33 | success | `public/run/tasks/Wolfram_Alpha--33-3b5bb3dc/` |
| Wolfram Alpha--34 | success | `public/run/tasks/Wolfram_Alpha--34-b9fe2cd0/` |
| Wolfram Alpha--35 | success | `public/run/tasks/Wolfram_Alpha--35-c5de4c07/` |
| Wolfram Alpha--36 | success | `public/run/tasks/Wolfram_Alpha--36-1dee9666/` |
| Wolfram Alpha--37 | success | `public/run/tasks/Wolfram_Alpha--37-bfe8fdd5/` |
| Wolfram Alpha--38 | success | `public/run/tasks/Wolfram_Alpha--38-874943f7/` |
| Wolfram Alpha--39 | success | `public/run/tasks/Wolfram_Alpha--39-373dd58c/` |
| Wolfram Alpha--4 | unknown | `public/run/tasks/Wolfram_Alpha--4-7031bc1c/` |
| Wolfram Alpha--40 | failure | `public/run/tasks/Wolfram_Alpha--40-a945859d/` |
| Wolfram Alpha--41 | success | `public/run/tasks/Wolfram_Alpha--41-7783a3ed/` |
| Wolfram Alpha--42 | success | `public/run/tasks/Wolfram_Alpha--42-5f3f096d/` |
| Wolfram Alpha--43 | run_error | `public/run/tasks/Wolfram_Alpha--43-6fc7a2ee/` |
| Wolfram Alpha--44 | success | `public/run/tasks/Wolfram_Alpha--44-177b6495/` |
| Wolfram Alpha--45 | unknown | `public/run/tasks/Wolfram_Alpha--45-8bcfec64/` |
| Wolfram Alpha--5 | success | `public/run/tasks/Wolfram_Alpha--5-70bd8bc5/` |
| Wolfram Alpha--6 | success | `public/run/tasks/Wolfram_Alpha--6-138a2c2c/` |
| Wolfram Alpha--7 | success | `public/run/tasks/Wolfram_Alpha--7-74f1f8a8/` |
| Wolfram Alpha--8 | success | `public/run/tasks/Wolfram_Alpha--8-2a5ca5fa/` |
| Wolfram Alpha--9 | success | `public/run/tasks/Wolfram_Alpha--9-e9b6f1f4/` |

## Sources

- [WebVoyager canonical snapshot](https://github.com/MinorJerry/WebVoyager/tree/5a7896738c10bfb8b9edccce6bb0e0411f8ae569)
- [omxyz dataset snapshot](https://github.com/omxyz/webvoyager/tree/df42681582be8125c5296473ad8efcd86f926cb6)
- [Steel contribution rules](https://github.com/steel-dev/leaderboard/blob/main/CONTRIBUTING.md)

For a leaderboard submission, this is a self-reported system score on a date-adjusted 615-task variant with a custom text-and-image judge. Product pricing or closed implementation does not establish model-weight availability. Acceptance and comparison remain the maintainer's decision.

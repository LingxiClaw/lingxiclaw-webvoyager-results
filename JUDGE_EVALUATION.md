# Evaluation Records and Offline Tools

- [Summary](summary.json) and [aggregated task results](merged_results.json).
- 615 structured Judge-record references (`evaluation/judge-records-index.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)).
- 613 frozen Judge-input references (`evaluation/frozen-inputs-index.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)).
- [Shared custom system prompt](judge_prompt.txt), extracted identically from all 613 frozen bundles.
- [Recorded input profiles and Judge identity](recorded_judge_configuration.json).
- Offline result aggregation script (`evaluation/recompute_results.py` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)).

References in the two index files are relative to this evaluation directory. Full input bundles include the user messages and selected evidence as well as the shared system prompt. All 615 `judge.json` records are retained, including skipped and error records.

The structured records are not raw provider responses. Original raw provider outputs, request IDs, retry counts and a hash-bound historical Judge invocation were not recovered. The offline scripts compute and validate the archived result without making model calls; they do not claim to recreate the online evaluation.

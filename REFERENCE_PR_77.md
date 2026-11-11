# Reference Submission Structure

Reference: [Steel PR #77](https://github.com/steel-dev/leaderboard/pull/77), inspected 2026-11-11 at head commit `700328d0d0ec24957496575a0239328b42e54b8c`. It was open and unmerged, with no submitted reviews or review comments returned by GitHub. It is a preparation example, not evidence of acceptance.

| Material type used in the reference | Lingxi counterpart |
| --- | --- |
| Results overview | [README.md](README.md), [REPORT.md](REPORT.md) |
| Execution and Judge methodology | [METHODOLOGY.md](METHODOLOGY.md) |
| Exact questions and before/after changes | tasks/ (`tasks` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)), [TASK_UPDATES.md](TASK_UPDATES.md) |
| Aggregate judgments and summary | evaluation/ (`evaluation` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) |
| Scoring/correction explanation | [SCORING_AUDIT.md](SCORING_AUDIT.md) |
| Evaluation script and input specification | Offline aggregation and checker, extracted prompt and frozen input records; historical online runner not reconstructed |
| Execution archives and checksums | Direct task files under public/run/ and repository/public checksum manifests |
| Detailed PR submission narrative | [PR_BODY.md](PR_BODY.md) |

The reference links to a separate public evidence repository and 15 website-level ZIP archives in a Release. Its Steel PR changes README.md, src/data/webvoyager.json and src/lib/benchmark-hub.ts. Lingxi's complete evidence is distributed in 16 Release ZIPs (one common archive plus 15 website archives), retaining the public/ tree and offline verification scripts after extraction. The repository itself contains the compact browsing edition of the reports and structured results.

The reference's answer-cleaning procedure, model selection, original-WebVoyager prompt, retry-selection policy and corrected score do not describe Lingxi. Lingxi retains its own archived judgments and custom evaluator, with missing historical information disclosed.

[Reference evidence snapshot](https://github.com/weiyali1/webwright-webvoyager-results/tree/100700bd55329d6ba4b67d9b4db5f77ba4641a23) · [Reference release](https://github.com/weiyali1/webwright-webvoyager-results/releases/tag/webvoyager-2026-11-03)

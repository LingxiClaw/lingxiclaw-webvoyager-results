# Publication and Steel Submission

The score source is [REPORT.md](REPORT.md), published on **2026-11-11** in the [public repository](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results). The complete evidence is published in the [Release](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09); see [ARCHIVE.md](ARCHIVE.md) for extraction and verification. This online directory is a compact browsing edition; scripts and the original evidence paths are in the full archive.

The company product website does not need to host a duplicate report. Product homepage: https://ai.soho.komect.com/ai/llm/home

## Submit to Steel separately

1. Review [SUBMISSION_REQUIREMENTS.md](SUBMISSION_REQUIREMENTS.md), [METHODOLOGY.md](METHODOLOGY.md), [TASK_UPDATES.md](TASK_UPDATES.md) and [SCORING_AUDIT.md](SCORING_AUDIT.md).
2. Use [ISSUE_DRAFT.md](ISSUE_DRAFT.md) with the Steel WebVoyager Issue form, or prepare a PR using [PR_BODY.md](PR_BODY.md) and [leaderboard-row.template.json](leaderboard-row.template.json).
3. For a PR, calculate rank from the then-current leaderboard, edit src/data/webvoyager.json, update WebVoyager lastUpdated in src/lib/benchmark-hub.ts, regenerate README, and run npm run update-readme, npm run lint and npm run build. These checks are not claimed to have run here.
4. Verify the live report and Release links before confirming the public-source checkbox. Await maintainer review.

The score is self-reported. Publishing this repository does not submit it to Steel and does not mean it has been accepted or independently certified. No Steel Issue or PR was submitted as part of this publication.

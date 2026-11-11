# Steel Submission Requirements

Checked on 2026-11-11 against Steel main commit `d588967e38b4ad0fbf8898a14a5a28661bcbc323`.

The proposed system name is **Lingxi AI Assistant** and organization is **China Mobile (Hangzhou) Information Technology Co., Ltd (中移（杭州）信息技术有限公司)**. A public score source must establish the result and relevant setup. Public product source code, free product access and publishing the report on the product homepage are not stated prerequisites.

## Issue form

Required inputs: Agent name, organization, published score, public score-source URL and Agent homepage URL. Repository URL and methodology notes are form-optional; methodological differences affecting this result still need disclosure. Both authenticity/public-source confirmations are required. The repository includes an English [Issue draft](ISSUE_DRAFT.md).

## Direct PR

Required JSON properties: rank, systemName, organization, scoreDisplay, scoreValue, sourceUrl and notesShort. reportedAt is optional in JSON Schema but the contributor evidence requirements and PR checklist request a source publication date; include it. repoUrl and isNew are optional. Extra properties are rejected by the score schema.

The current template has no fabricated rank, public URL or reporting date. Source-linked dataset filtering and custom judges are permitted by the WebVoyager page's methodology; admission and comparability remain subject to review. Existing 615-task rows establish precedent, not approval of this submission.

## Evidence boundaries

Full trajectories, screenshots, provider wire responses and hashes are not a uniform mandatory upload list in the contribution guide. This package supplies supporting records and discloses gaps. Historical version/checkpoint/retry gaps can affect review when they leave material setup unclear; the rules do not state that each missing field automatically requires a rerun.

Product source-code availability, execution-model weight availability and model size are different dimensions. The offline Judge is not a runtime model for size/weight classification. Do not infer exact weights or parameter counts from the catalog alias, or derive token prices from product subscription pricing.

## Primary references

- [Contributor guide](https://github.com/steel-dev/leaderboard/blob/d588967e38b4ad0fbf8898a14a5a28661bcbc323/CONTRIBUTING.md)
- [Issue form](https://github.com/steel-dev/leaderboard/blob/d588967e38b4ad0fbf8898a14a5a28661bcbc323/.github/ISSUE_TEMPLATE/submit-webvoyager-result.yml)
- [Score schema](https://github.com/steel-dev/leaderboard/blob/d588967e38b4ad0fbf8898a14a5a28661bcbc323/src/data/schema.json)
- [WebVoyager methodology](https://leaderboard.steel.dev/leaderboards/webvoyager)

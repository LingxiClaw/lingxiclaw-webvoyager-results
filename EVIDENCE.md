# Public Evidence and Privacy Processing

## Included records

The public/run/ (`public/run` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) directory contains the manifest, schedule, execution log and task directories. There are 615 run records, 615 structured Judge records, 613 frozen input bundles, 613 Agent response archives, 613 browser evidence files and 611 selected screenshots. [task-results.json](task-results.json) maps each task ID to its directory. The HTML report (`public/index.html` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) provides a searchable task index when opened in a browser.

Every task-evidence file is copied byte-for-byte from the previously verified, privacy-redacted public package. Naming changes in this revision affect presentation metadata and documentation, not task records, platform metadata or the dataset. The archived run ID remains an historical identifier.

## Privacy transformations

The prior export replaced JWT-shaped web tokens, local user-directory names and account-path identifiers in text. It recalculated the public frozen-input and associated source hashes. lineage.json (`public/lineage.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) pairs original and public task-file hashes; [privacy-processing.json](privacy-processing.json) records processing counts and limitations.

All 611 selected screenshots underwent local OCR screening. The flagged email was an arXiv documentation example, inspected during preparation. This screening is not a guarantee of detecting every sensitive item. Original unredacted records remain separate from the publication folder.

## Language and source preservation

All new explanatory documents and submission templates are in English. Company attribution intentionally includes the requested Chinese legal name. Historical responses, prompts, judgments and screenshots retain their original language and content; they are not silently translated into different evidence.

## Checksums

public/SHA256SUMS.json (`public/SHA256SUMS.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) covers the public evidence package. FILES.json (`FILES.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)) covers the repository files other than itself. After an intentional documentation or publication-metadata update, run `python3 scripts/refresh_checksums.py` and then `python3 scripts/verify_repository.py`.

Core product source code, private source-recovery working directories, research downloads and layout-QA files are not included. The [harness provenance](harness-provenance.json) distinguishes source files bound by manifest hashes from archive-associated source whose historical execution has not been established.

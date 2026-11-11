# Complete Evidence Archives

Download the **common ZIP and all 15 website ZIPs** from the [Release](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09). Each ZIP contains an independent portion of the same directory tree. Extract all 16 ZIPs into the same parent directory to reconstruct `lingxiclaw-webvoyager-evidence/`. These are ordinary ZIP files, not binary split-file chunks; there is no concatenation step.

Together they contain **5,589 files**: 615 run records, 615 Judge records, 613 frozen Judge input bundles, 611 screenshots, associated response/evidence files, dataset provenance, source lineage, English reports and offline verification scripts. Historical task evidence and judgments are unchanged.

Use [SHA256SUMS.txt](SHA256SUMS.txt) to verify every ZIP, or inspect [archive-manifest.json](archive-manifest.json) for per-archive hashes, sizes and download URLs. After extraction:

```sh
cd lingxiclaw-webvoyager-evidence
python3 scripts/verify_repository.py
python3 evaluation/recompute_results.py
```

Both commands run offline. Expected result: **530/615 (86.18%)**. The full archive layout contains FILES.json, public/SHA256SUMS.json and original-to-public hash lineage. Paths embedded in JSON records refer to this extracted layout. To inspect just one website, download its ZIP and the common ZIP; full-package verification requires all 16.

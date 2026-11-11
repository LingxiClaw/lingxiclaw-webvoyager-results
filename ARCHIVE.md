# Evidence Archive

The online repository is a compact browsing edition. Download the [complete ZIP](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/download/webvoyager-2026-10-09/lingxiclaw-webvoyager-evidence-20261111.zip) from the [Release](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09) for all execution logs, Judge inputs, responses, screenshots, provenance manifests and verification scripts.

Archive SHA-256: `fb0c32ece5fc762bd35e85e39682258ad8d830ffca39fe1290b38a668bda5a9e`. Archive files: 5589. Compressed bytes: 658829402.

After extracting, run:

```sh
cd lingxiclaw-webvoyager-evidence
python3 scripts/verify_repository.py
python3 evaluation/recompute_results.py
```

These checks make no network or model calls. The full archive contains FILES.json, public/SHA256SUMS.json and original-to-public hash lineage. Paths embedded in copied JSON records refer to the archived layout, not the flattened online directory. The historical judgments and score are unchanged.

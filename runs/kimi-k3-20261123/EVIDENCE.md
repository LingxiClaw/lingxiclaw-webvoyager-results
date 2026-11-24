# Evidence and integrity checks

The [task index](TASKS.md) links 615 individually downloadable archives. The [execution log](run/execution.log), [scheduler events](run/schedule.jsonl), [manifest](run/manifest.json) and [runner report](run/report.json) preserve the initial schedule and final aggregate. The run ID in archived records is the historical run identifier.

| File type | Count | Inspection |
| --- | ---: | --- |
| Final execution records and structured judge records | 615 each | Join by task ID and compare eligibility, outcome and budget |
| Frozen judge inputs | 615 | Source-file hashes, prompt, message hashes and selected image hashes checked before public privacy processing |
| Logical judge requests and raw provider responses | 614 each | Reconstructed image-bearing request hashes and parsed response decisions match the recorded requests and judgments |
| Selected screenshots | 611 | Published byte-for-byte from the selected PNG files |
| Task directories retained after a later execution | 7 | Cross-checked against the original scheduler's error and timestamps |

Public text redacts matched workstation paths, local account identifiers, access tokens and inline image data. The source and public file hashes in [the file inventory](evidence-lineage.json) identify the input used for this publication and the bytes released. Agent and worker model labels follow the configuration confirmed by the product team. The historical judge hashes refer to the input before privacy processing. Public file hashes verify the downloadable text. The retained standalone screenshots match the frozen image hashes. Unselected screenshot attempts remain outside the Git evidence archives.

All 611 selected images passed through local OCR screening. Four had email-pattern hits. Inspection showed a product support contact, arXiv subscription instructions, addresses in a public commit and the test address provided by a benchmark task. Pattern checks have limited coverage.

From this directory in a checkout, run `python3 verify.py`. It checks public checksums and every archive member, reconciles both scores against the schedule and checks the parsed raw response against the recorded outcome for every judged task. [Checksums](SHA256SUMS.txt)

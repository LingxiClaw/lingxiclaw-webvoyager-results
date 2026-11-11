# Scoring and Evidence Audit

The published aggregate remains **530/615 (86.18%)**. No browser task or Judge call was repeated while preparing the publication material. No archived verdict has been overwritten.

| Outcome | Tasks |
| --- | ---: |
| Success | 530 |
| Failure | 49 |
| Unknown | 22 |
| Execution error | 12 |
| Judge error | 2 |
| Total | 615 |

## Four tasks without a selected screenshot

| Task | Archived category | Treatment |
| --- | --- | --- |
| Google Flights--15 | unknown | Retained as a non-success |
| GitHub--29 | run_error | Retained as a non-success |
| Huggingface--34 | run_error | Retained as a non-success |
| Huggingface--35 | success | Original text-supported judgment retained, with the qualification below |

The custom Judge can use textual evidence. Missing a selected screenshot therefore does not automatically force failure under this historical protocol.

## Huggingface--35

Sources e000022 and e000023 support a Diffusion-tag listing headed by Waypoint-1.5 and the selected article's introduction. The final answer scopes its choice to the tag listing. However, the same page also contains newer community/trending diffusion-related content; newest across all community posts is not established. No screenshot was selected because of a stale window-title mismatch.

The archived automated success remains unchanged. If this single success were not counted, a sensitivity calculation would yield 529/615 (86.02%). That is an illustrative calculation, not a revised evaluated score. See [review-notes.json](review-notes.json).

## Judge errors and stale task date

BBC News--13 and Google Search--8 retain Judge errors from empty-JSON parsing failures and contribute no success. Booking--5 retains a failed outcome even though its requested stay preceded execution. None is removed from the denominator.

## Diagnostic correction

The legacy `capture_unavailable=6` adds four missing-image-path cases and two `quality=unavailable` cases into the same key. The separate missing-selected-image count is four. Correcting the diagnostic does not change a judgment or score. The legacy report remains available as original_report.redacted.json (`public/run/original_report.redacted.json` inside the [evidence archive](https://github.com/LingxiClaw/lingxiclaw-webvoyager-results/releases/tag/webvoyager-2026-10-09)).

## What the audit proves

The offline tools validate file integrity, task identity, recorded classifications and aggregate arithmetic. They do not independently rejudge 615 answers or authenticate historical service calls. Judge `request_count=0` is a default rather than a recovered attempt count. Raw provider responses and original request IDs were not recovered.

# Execution attempts

Each task ID appears once in the original queue and dispatch log. Seven tasks recorded an initial scheduler error and have a later completed execution in their final task directory. The seven later successes add 1.14 percentage points to the unrounded initial-dispatch rate (7/615). The scheduler's original manifest closes before these later executions. All times below are UTC.

| Task | Initial dispatch | Initial error | Later start | Later finish | Final judgment |
| --- | --- | --- | --- | --- | --- |
| ArXiv--28 | 2026-11-23T18:47:38.272803+00:00 | 2026-11-23T19:04:43.404081+00:00 | 2026-11-24T02:49:34.782775Z | 2026-11-24T02:55:01.826969+00:00 | success |
| BBC News--25 | 2026-11-23T17:45:36.837420+00:00 | 2026-11-23T18:03:09.682706+00:00 | 2026-11-24T02:49:34.781840Z | 2026-11-24T02:52:36.429819+00:00 | success |
| BBC News--40 | 2026-11-23T21:07:52.618208+00:00 | 2026-11-23T21:25:10.632079+00:00 | 2026-11-24T02:55:01.832242Z | 2026-11-24T02:57:27.565500+00:00 | success |
| Booking--23 | 2026-11-23T16:29:46.735140+00:00 | 2026-11-23T16:47:30.871497+00:00 | 2026-11-24T02:49:34.781739Z | 2026-11-24T02:58:35.473179+00:00 | success |
| ESPN--29 | 2026-11-23T19:14:48.476596+00:00 | 2026-11-23T19:32:03.354405+00:00 | 2026-11-24T02:52:36.431613Z | 2026-11-24T02:55:48.011667+00:00 | success |
| Google Flights--29 | 2026-11-23T18:38:39.314668+00:00 | 2026-11-23T18:56:48.531238+00:00 | 2026-11-24T02:49:34.781867Z | 2026-11-24T02:56:18.356688+00:00 | success |
| Google Flights--37 | 2026-11-23T20:44:08.615818+00:00 | 2026-11-23T21:01:27.944913+00:00 | 2026-11-24T02:55:48.014708Z | 2026-11-24T03:08:02.827200+00:00 | success |

The schedule and execution log preserve the first-dispatch events for these tasks. Their final task archives contain the later attempt. The supplied folder does not contain seven additional, separate first-attempt task directories. The file-level records establish logical attempts within this archive. They do not attest to lower-level network retries.

[Machine-readable history](attempt-history.json) · [Execution log](run/execution.log) · [Final task results](task-results.json)

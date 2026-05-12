# P4-560 Bounded Owner Scout After JEITA Current-Public 1.50 mm No-Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-559-2026-5-12-current-state-completion-audit-successor-after-jeita-public-bundle.md`
- `logs/p4-558-2026-5-12-jeita-public-bga-fbga-flga-geometry-bundle-below-1p50mm-no-reopen.md`
- `logs/p4-557-2026-5-12-mediatek-official-package-scout-no-reopen.md`
- `logs/p4-556-2026-5-12-broadcom-avago-owner-split-surface-1p50mm-no-reopen.md`
- `logs/p4-539-2026-5-12-jcet-pbga-pdf-now-directly-retrievable-but-still-no-reopen.md`
- `logs/p4-530-2026-5-11-infineon-concrete-package-pages-now-retrievable-but-below-true-1p50mm-gate.md`
- `logs/p4-329-2026-5-9-1p50mm-nxp-legacy-pbga-route.md`

Execution mode: `subagent_aided_bounded_owner_scout_plus_controller_verification`

## Purpose

Run one bounded post-`P4-559` check against the only remaining live reopen lane:

- package-side `1.50 mm`

The purpose is not to restart a broad package-house sweep.
It is to check whether a newly surfaced current-public official owner surface now clears the strict gate.

## Reopen Gate

Reopen only if one current-public official owner surface visibly provides both:

1. true `1.50 mm` BGA / CSP / package pitch identity
2. same-surface PCB land-pattern, footprint, recommended pad, or printed board geometry

Family-level pitch availability alone is not enough.
Geometry on a different surface is not enough.
`1.5 mm` package height, body size, or non-BGA lead pitch is not enough.

## Subagent Lane

One bounded explorer lane checked official semiconductor / package-owner surfaces for:

- `TI`
- `Analog Devices / Maxim`
- `ST`
- `onsemi`
- `Qorvo`
- `Skyworks`
- `Lattice`
- `Marvell`
- `Qualcomm`

No files were edited by the subagent.

## Subagent Findings

The lane found no new same-surface reopen candidate.

Closest checked official leads:

- `TI` package outline `https://www.ti.com/lit/pdf/mpbgar4`
  - visible `1.5 mm` context is package height, not pitch
  - visible pitch is `1.0 mm`
  - result: no reopen
- `Analog Devices` BGA app note `https://www.analog.com/en/resources/app-notes/ball-grid-array-bga-packages-and-pcb-design-guidelines.html`
  - useful land-pad guidance
  - no same-surface `1.50 mm` package pitch identity
  - result: no reopen
- `Analog Devices` `ADSP-TS101S` datasheet `https://www.analog.com/media/en/technical-documentation/data-sheets/adsp-ts101s.pdf`
  - same surface has BGA package and pad guidance
  - visible pitch is `0.80 BSC`, not `1.50 mm`
  - result: no reopen
- `Lattice` BGA layout note `https://www.latticesemi.com/view_document?document_id=671`
  - official BGA land / routing document
  - visible pitch examples stay at `1.27 mm`
  - result: no reopen
- `Skyworks` land-pattern note `https://www.skyworksinc.com/-/media/SkyWorks/Documents/Products/201-300/PCB_Layout_Patterns_Guidelines_200123M.pdf`
  - land-pattern guidance is leaded / leadless focused
  - no qualifying `1.50 mm` BGA / CSP same-surface match
  - result: no reopen
- `Qorvo` `RF3807` datasheet `https://store.qorvo.com/datasheets/qorvo/3807ds.pdf`
  - official land-pattern data
  - visible pitch context is `1.27 Typ.`, not `1.50 mm`
  - result: no reopen

The same lane did not surface a public official same-surface hit for `ST`, `onsemi`, `Marvell`, or `Qualcomm`.
The observed hits were non-BGA land patterns, wrong pitch, non-owner mirrors / forums, or inaccessible package-owner surfaces.

## Controller Verification: NXP / Freescale PBGA Presentation

The controller also checked one newly surfaced NXP-hosted Freescale PBGA presentation:

- `https://www.nxp.com.cn/docs/en/package-information/PBGAPRES.pdf`

This is a useful current-public official-hosted PBGA design surface, but it stays below the gate.

Verified public text extraction showed:

- package terminology page:
  - `BGA pitch range from 1.0-1.27mm`
- PC board design page:
  - visible pad table rows for `1.27`, `1.00`, `0.80`, `0.65`, and `0.50`
- routing guidance page:
  - `For 1.27, 1.0 and 0.8 mm pitches`
  - `For 0.8, 0.65 and 0.50 mm pitches`

This surface is useful as one more below-gate owner geometry check.
It does not clear the `1.50 mm` lane because it does not expose a visible `1.50 mm` PBGA row with same-surface PCB pad geometry.

It should also not be confused with the older `AN1231` near-hit preserved in `P4-329`, which already remains below clean exact-geometry closure because it is legacy family guidance and requires package-specific diameter confirmation before layout.

## Gate Result

No checked surface clears the current reopen gate.

This pass adds one more bounded current-public owner-scout no-reopen layer after `P4-559`, but it does not change the top-level completion threshold:

- `program_level_strong_complete`: still achieved
- `current_public_authority_layer_exhausted_with_residual_authority_gaps`: still the safe wording
- `full_corpus_closed_without_open_residual_authority_gaps`: still not achieved as a literal authority-free state

## Continuation Rule

Future continuation should not repeat this bounded vendor set by default.

Only reopen package-side `1.50 mm` if a genuinely new current-public official owner or standards surface is first identified that visibly contains both:

1. true `1.50 mm` BGA / CSP / package pitch identity
2. same-surface PCB land-pattern / footprint / recommended pad geometry

Otherwise, treat the current `1.50 mm` lane as exhausted at the current public authority layer, not as a queued blind-search task.


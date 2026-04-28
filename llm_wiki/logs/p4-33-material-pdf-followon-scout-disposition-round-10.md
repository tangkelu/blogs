# P4-33 Material PDF Follow-On Scout Disposition Round 10

Date: 2026-04-28
Status: `scout_disposition_only`
Learning State: `not_learned`

## Purpose

Capture the read-only `gpt-5.4` scout outputs for the next material PDF recovery lanes after Ventec round 10, without promoting any scout-only candidate into reusable facts.

This log is a deletion-safe planning artifact. It does not create source-backed facts by itself.

## Ventec Follow-On Candidates

The Ventec scout found the safest next official-page-backed candidates to be:

| priority | local PDF | proposed source ID | proposed fact ID | official URL candidate | disposition |
|---|---|---|---|---|---|
| 1 | `Ventec-vt-462s.pdf` | `ventec-vt-462s-datasheet-page` | `materials-ventec-vt-462s` | `https://www.ventec-group.com/zh/products/tec-speed-signal-integrity/tec-speed-60-vt-462s/datasheet/` | `next_candidate` |
| 2 | `Ventec-vt-464gs.pdf` | `ventec-vt-464gs-datasheet-page` | `materials-ventec-vt-464gs` | `https://www.ventec-group.com/cht/products/tec-pack-ic-packaging/vt-464gs/datasheet/` | `next_candidate` |
| 3 | `Ventec-vt-90h.pdf` | `ventec-vt-90h-datasheet-page` | `materials-ventec-vt-90h` | `https://www.ventec-group.com/products/polyimide/vt-90h/datasheet/` | `next_candidate` |
| 4 | `Ventec-vt-4b5h.pdf` | `ventec-vt-4b5h-datasheet` | `materials-ventec-vt-4b5h` | `https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b5h/datasheet/` | `next_candidate` |

Second-tier Ventec candidates:

- `Ventec-vt-441v.pdf` -> `ventec-vt-441v-datasheet-page` / `materials-ventec-vt-441v`
- `Ventec-vt-441.pdf` -> `ventec-vt-441-datasheet-page` / `materials-ventec-vt-441`
- `Ventec-vt-42.pdf` -> `ventec-vt-42-datasheet-page` / `materials-ventec-vt-42`

Ventec caution / blocked candidates:

- `Ventec-vt-47-v2.pdf`: block until exact live product identity is verified.
- `Ventec-vt-447pp-nflf.pdf`, `Ventec-vt-901pp-nflf-lcte.pdf`, `Ventec-vt-4b3h-rcf.pdf`, and `Ventec-vt-464lt-rcc.pdf`: product-form-specific bondply / no-flow / low-flow / RCF / RCC rows only; do not ingest as generic laminate rows.
- `Ventec-vt-870-h1000.pdf`: distinct high-Dk RF variant; do not fold into generic `VT-870`.

## TUC Follow-On Candidates

The TUC scout found the safest next candidates to be:

| priority | local PDF | proposed source ID | proposed fact ID | disposition |
|---|---|---|---|---|
| 1 | `tu-901_datasheet.pdf` | `tuc-tu-901-datasheet` | `materials-tuc-tu-901` | `candidate_pending_official_match` |
| 2 | `tu-787 lk_datasheet.pdf` | `tuc-tu-787-lk-datasheet` | `materials-tuc-tu-787-lk` | `candidate_pending_official_match` |
| 3 | `tu-865s_datasheet.pdf` | `tuc-tu-865s-datasheet` | `materials-tuc-tu-865s` | `candidate_pending_official_match` |
| 4 | `SCGA-500+GF220+TDS.pdf` | `tuc-scga-500-gf220-datasheet` | `materials-tuc-scga-500-gf220` | `candidate_pending_official_match` |
| 5 | `tu-872 lk_datasheet.pdf` | `tuc-tu-872-lk-datasheet` | `materials-tuc-tu-872-lk` | `candidate_pending_official_match` |

TUC deferred candidates:

- `thunderclad 4hz_datasheet.pdf`
- `thunderclad 4hr_datasheet.pdf`
- `tu-768_datasheet.pdf`
- `tu-865_datasheet.pdf`
- `tu-872 slk_datasheet.pdf`

Reason: scout observed local metadata / title collisions for several files. These need exact official page / PDF matching before any fact extraction.

## Guardrails

- Promote a candidate only after official manufacturer page / PDF matching.
- Preserve test method, condition, frequency, direction, resin content, variant, revision, and preliminary caveats.
- Keep Ventec PGL / process guidance product-scoped only; do not create generic press cycles, drill tables, desmear recipes, storage windows, or supplier capability claims.
- Do not promote finished-board insertion loss, impedance, antenna, RF, high-speed channel, reliability, qualification, stock, lead-time, MOQ, yield, price, or supplier capability claims from these scouts.

## Next Controller Action

Proceed first with the four Ventec candidates whose official pages returned `200 OK` during controller checking, then revisit TUC only after exact official URL binding is established.

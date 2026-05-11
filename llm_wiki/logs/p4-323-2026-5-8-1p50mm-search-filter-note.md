# P4-323 1.50 mm Search Filter Note

Date: 2026-05-08
Parent lane: `P4-309`
Execution mode: `controller_owned_search_filter_note`

## Purpose

Preserve one high-value negative filter for the still-open `1.50 mm` package residual so future `/goal` work and subagents do not misread unrelated `1.50` fields as `1.50 mm BGA pitch` recovery.

## Inputs

- `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`
- official Microchip drawing `c04-21198a.pdf`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`

## What This Pass Checked

- one current Microchip package drawing that contains multiple `1.50` strings:
  - `8-Ball Very Thin Fine-Pitch Ball Grid Array Package (E8B) - 1.50x2.00x0.85 mm Body [VFBGA]`
  - `Microchip Technology Drawing C04-21198 Rev A`

## What This Pass Confirmed

- this drawing does contain a real `RECOMMENDED LAND PATTERN` page
- however, its actual package `Pitch` row is:
  - `1.00 BSC`
- one `1.50 BSC` value in the same drawing belongs to:
  - `Contact Pad Spacing`
- another `1.50` value belongs to:
  - body-size wording in the package title

## Search Filter Worth Preserving

- do not treat a hit on `1.50` alone as evidence that a candidate drawing is a `1.50 mm pitch` package
- for future `1.50 mm` recovery, require the candidate to expose:
  - a real package `Pitch` row or equivalent package-pitch statement at `1.50 BSC`
  - and a printed `RECOMMENDED LAND PATTERN` or equivalent PCB land-geometry row
- reject candidates where `1.50` is only:
  - body-size wording
  - contact-pad spacing
  - unrelated package dimensions

## What Did Not Land

- no new official source record
- no new exact-data fact card
- no new wiki route change

## Final Status

- lane result:
  - `search_filter_note_landed`
- continuation state:
  - `future_1p50mm_recovery_should_filter_out_body_size_and_contact_spacing_false_positives`

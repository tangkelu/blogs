# P4-304 PCB资料 Package Pin-1 Origin Authority-Gap Tightening

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_authority_gap_tightening`

## Purpose

Tighten the highest-priority remaining `package` authority gap identified in `P4-220C` by checking whether the current local corpus can safely do more than generic governance wording for:

- `pin-1 mark`
- `origin`
- `installation mark`

This pass is intentionally narrow.
It does not reopen broad package rescans.
It does not claim stronger official authority than the corpus actually has.

## Inputs

- `logs/p4-220c-2026-5-7-package-asset-linkage-and-authority-gap-map.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `facts/methods/package-family-and-footprint-governance-vocabulary-boundary.md`
- `wiki/processes/package-library-governance-and-footprint-review-map.md`
- `sources/registry/internal/frontendapt-glossary-terms-resource-page-en.md`
- `sources/registry/internal/frontendapt-dfm-guidelines-resource-page-en.md`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-42种-常见PCB封装设计指导规范/pages/page-0029.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-42种-常见PCB封装设计指导规范/pages/page-0030.txt`

## What Was Checked

### Existing internal source layer

Confirmed current reusable internal support:

- the glossary provides `Assembly Drawing` and orientation / polarity vocabulary
- the DFM guideline requires assembly drawings with component outlines, reference designators, and polarity markings
- the DFM guideline supports documentation completeness as a manufacturability-review concern

Limit:

- this layer does not by itself provide a stronger owner-grade rule for `pin-1`, package-origin placement, or installation-mark conventions

### Existing local handbook text

Confirmed the extracted handbook text on pages `29-30` includes:

- `pin-1` marker examples
- polarity-marker mention
- installation-mark mention
- local origin-placement examples for regular-shape devices, through-hole devices, and connectors

Limit:

- this remains handbook-origin local context, not standards-owner or package-owner authority

## What Landed

### New local evidence and local-PDF fact

Landed as tightly scoped local knowledge:

- `pdf_evidence/pcb_ziliao/package/pin1-origin-installation-mark-text-boundary.md`
- `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`

Reason:

- the local text is clean enough to support documentation-governance explanation
- the claim can be explicitly kept local-PDF-scoped
- this reduces loss of useful handbook context without overclaiming universal footprint rules

## What Did Not Land As Stronger Official Fact Layer

No new `facts/methods/*` or `sources/registry/methods/*` record was created in this pass.

Reason:

- the current corpus still lacks a stronger public package-owner, CAD-owner, or standards-owner source for universal `pin-1`, `origin`, and `installation mark` conventions
- the internal APT resource layer supports documentation posture, not authoritative geometry or library-default rules

## Updated Authority Posture

- `pin-1 / polarity / installation-mark presence`: `source_backed_fact_layer_partial` at governance level, plus `local_pdf_fact` support for local handbook context
- `origin placement by package family`: `local_pdf_fact_added_but_official_authority_still_missing`
- `connector-origin variants`: `blocked_pending_official_source`

## Next Recommended Moves

1. Recover one stronger package-owner, CAD-owner, or standards-adjacent source for `pin-1`, `origin`, or land-pattern documentation conventions before upgrading the method-layer fact.
2. Keep using the new local-PDF card only for blog-body context, never as standards wording.
3. Do not reopen page `29-30` numerics through this lane.

## Final Status

- lane result:
  - `source_backed_fact_layer_partial`
- continuation state:
  - `narrow_official_source_recovery_still_needed`

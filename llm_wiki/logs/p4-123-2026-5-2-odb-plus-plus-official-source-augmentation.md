# P4-123 ODB++ Official Source Augmentation

Date: 2026-05-02
Status: `source_backed_fact_layer_partial`

## Purpose

Augment the existing CAM / file-package boundary with official ODB++ owner sources so `buying-pcb.md` and adjacent data-exchange drafts no longer depend only on Gerber and IPC-DPMX / IPC-2581 authority.

This pass stays narrow. It does not claim supplier acceptance, file-package completeness, CAM-review depth, manufacturability outcomes, or commercial benefit.

## Inputs Reviewed

- `facts/methods/cam-data-exchange-format-boundary.md`
- `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
- `logs/p4-44-source-backed-integration.md`
- official Siemens ODB++ page
- official Siemens ODB++ resources / FAQ page

## Source-Backed Additions

Added source records:

- `sources/registry/standards/siemens-odb-plus-plus-page.md`
- `sources/registry/standards/siemens-odb-plus-plus-resources-faq.md`

Updated reusable knowledge:

- `facts/methods/cam-data-exchange-format-boundary.md`
- `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`

## What Is Now Source-Backed

- ODB++ identity as an owner-maintained PCB design-through-manufacturing data-exchange format family
- guarded wording that ODB++ spans design, process, and manufacturing information flow
- guarded wording that ODB++ specification access exists through Siemens-hosted resources
- guarded wording that ODB++ content can be segmented in a handoff package

## What Stays Blocked

- claims that all manufacturers accept ODB++
- claims that ODB++ universally replaces Gerber, IPC-DPMX / IPC-2581, BOM, pick-and-place, schematic, or test artifacts
- claims that ODB++ guarantees fewer job holds, faster CAM review, lower cost, better yield, or better quality
- supplier-specific ODB++ intake depth without dated internal capability evidence

## Controller Result

`buying-pcb` still does not justify a standalone new lane, but its CAM/data-exchange boundary is now stronger and less dependent on open-question placeholders.

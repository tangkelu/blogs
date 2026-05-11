# P4-363 E3 IPC Solder-Mask Terminology Boundary Recovery

Date: 2026-05-09
Parent lane: `P4-311`
Execution mode: `narrow_article_side_official_source_recovery`

## Purpose

Advance the `E3` solder-mask subfamily above article-only routing by landing one narrow official-source-backed terminology boundary for solder-mask layer identity and guarded pad-definition vocabulary.

This pass is intentionally narrow.
It does not claim that public IPC metadata closes exact `NSMD/SMD`, `via tenting`, or `solder mask bridge` definitions.

## Inputs

- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-362-2026-5-9-e3-solder-mask-opening-completeness-route-integration.md`
- official or primary source records already in repo:
  - `ipc-t50-terms-and-definitions-toc`
  - `ipc-6012f-release`
  - `ucamco-gerber-format-page`
  - `intel-an114-bga-land-pad-dimensions`
- newly added official IPC metadata source:
  - `ipc-7093a-toc`

## What Landed

### New source record

- `sources/registry/standards/ipc-7093a-toc.md`

### New boundary fact card

- `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`

### Resume-surface integration

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## What Landed Safely

- one official format-owner-backed statement that `solder mask` is part of released fabrication-data layer scope
- one public IPC terminology-family anchor that solder-mask and pad-definition language should route through IPC terminology control rather than article prose
- one public IPC document-family anchor that solder-mask design, pad-definition, and tented-via topics exist inside an IPC-controlled standards family
- one guarded repo-wide boundary that `SMD/NSMD` can currently be named only through vendor-scoped official examples unless stronger IPC text is recovered

## What Did Not Land

- no exact IPC definitions for `mask-defined`, `non-solder-mask-defined`, `via tenting`, or `solder mask bridge`
- no opening-expansion, bridge-width, or via-opening numerics
- no universal pad-selection rule or acceptability criteria
- no tool-workflow, checker-completeness, or supplier-capability claim

## Final Status

- lane result:
  - `narrow_official_source_recovery_landed`
- continuation state:
  - `e3_now_has_ipc_and_format_owner_backed_solder_mask_layer_identity_boundary`
  - `nsmd_smd_via_tenting_and_bridge_definitions_still_remain_gap_controlled`

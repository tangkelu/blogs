# P4-557 MediaTek Official Package Scout No Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-556-2026-5-12-broadcom-avago-owner-split-surface-1p50mm-no-reopen.md`
- `logs/p4-555-2026-5-12-current-state-completion-audit-successor-after-adi-lfcsp-marking-landing.md`
- `logs/p4-520-2026-5-11-post-p4-519-materially-different-1p50mm-owner-class-recheck-no-new-class.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `subagent_aided_candidate_gated_negative_scout`

## Purpose

Record one more bounded scout under the current `1.50 mm` BGA/CSP gate so future `/goal` work does not treat `MediaTek` as an unreviewed blank owner class.

This pass is not a reopen.
It checks whether current-public `MediaTek` official package and device surfaces contain one same-surface hit with true `1.50 mm` pitch identity plus printed PCB land-pattern or footprint geometry.

## Candidate Gate Rechecked

The current lane should reopen only if one public owner surface visibly exposes both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern / footprint geometry

## Candidates Rechecked

- official MediaTek IoT documents index:
  - `https://www.mediatek.com/iot/documents?page=1`
  - `https://www.mediatek.com/iot/documents?document_type=Datasheet&page=1`
- official Genio hardware-design page:
  - `https://genio.mediatek.com/hardware-design`
- official Genio EVK and boards page:
  - `https://genio.mediatek.com/evk-boards`
- official MediaTek-hosted datasheets:
  - `https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Genio%20Documents/MT8395_IoT_Application_Processor_Datasheet_v1.4.pdf?hsLang=en`
  - `https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Genio%20Documents/MT7933CT_Datasheet.pdf?hsLang=en`
  - `https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Genio%20Documents/MT7931AN_Datasheet.pdf`
  - `https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Genio%20Documents/AI7933CLD_SPEC_Ver.E.pdf`

## Findings

### 1. `MediaTek` current-public owner surfaces are real and package-relevant, not blind vendor-name speculation

- the checked `mediatek.com` and `genio.mediatek.com` pages are real current-public owner surfaces
- the checked MediaTek-hosted PDFs do expose package-related content such as:
  - package information
  - mechanical drawing
  - package spec or package identity
- this makes `MediaTek` one genuine owner class rather than one blank name or search-noise candidate

### 2. The strongest surfaced `MediaTek` near-hit still stays below the current gate

- the strongest current-public near-hit is the official `MT8395` datasheet
- it visibly exposes:
  - `Package Information`
  - `Mechanical Drawing`
  - `MFC VFBGA 15.0 mm × 15.0 mm, 1046-ball, 0.4 mm pitch package`
- however it still does not expose:
  - one true `1.50 mm` pitch identity
  - one same-surface printed PCB land-pattern or footprint geometry row

### 3. The rest of the checked official package surfaces also stay below the target residual

- the official `MT7933CT` datasheet exposes package spec and outline drawing, but the visible ball pitch is `0.5 mm`
- the official `MT7931AN` datasheet exposes package spec and outline drawing, but the visible pin pitch is `0.5 mm`
- the MediaTek-hosted `AI7933CLD` module datasheet is current-public, but it is a module document rather than one qualifying `1.50 mm` BGA/CSP same-surface package row
- the public `Genio hardware-design` and `EVK` pages mention schematic, layout, and reference-design resources, but the publicly reachable pages in this pass do not surface one gate-clearing package document

### 4. The safest result remains `no reopen`

- current-public `MediaTek` owner surfaces now count as one rechecked owner class rather than one open blank
- the strongest surfaced official evidence gives package identity and mechanical-drawing context only at sub-`1.50 mm` pitch classes
- no reviewed public `MediaTek` surface in this pass pairs true `1.50 mm` pitch identity with same-surface printed PCB geometry

## Audit Result

- no new `sources/registry/` record landed
- no new `facts/` card landed
- no `wiki/` route changed
- no completion threshold changed
- the safest result is `no reopen`

## What This Pass Fixes

- future AI should not treat `MediaTek` as an unreviewed owner blank for the `1.50 mm` lane
- future AI should not promote `MediaTek` package-identity or mechanical-drawing surfaces into a `1.50 mm` reopen when the visible pitches are `0.4` or `0.5 mm`
- future AI should not treat `Genio hardware-design` page-level resource mentions as if they already expose a publicly verified gate-clearing package document

## Continuation Rule

Keep the current `1.50 mm` BGA/CSP residual open only under the tightened `true pitch identity + same-surface geometry` gate.

Do not reopen it on the current-public `MediaTek` surfaces above unless a later public owner surface exposes one true `1.50 mm` BGA/CSP pitch row together with printed PCB land-pattern geometry on the same surface.

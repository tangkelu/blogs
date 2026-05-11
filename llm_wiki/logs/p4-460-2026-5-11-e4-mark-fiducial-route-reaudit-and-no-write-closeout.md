# P4-460 E4 Mark Fiducial Route Re-Audit And No-Write Closeout

Date: 2026-05-11
Parent surfaces:

- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
- `logs/p4-353-2026-5-9-e4-mark-fiducial-role-route-integration.md`
- `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `sources/registry/standards/ipc-7525c-toc.md`
- `sources/registry/standards/ucamco-gerber-format-page.md`
- `sources/registry/processes/apt-pcba-stencil-support-services.md`

Execution mode: `subagent_aided_single_pdf_route_reaudit`

## Purpose

Re-audit whether `PCB板的Mark点设计对SMT重要性.pdf` can be promoted above its current route-only status using the current in-repo fiducial-related authority layer.

This pass is an audit only.
It does not assume that the existence of `fiducial` wording in stencil or data-exchange sources is enough to close article-side SMT `Mark` design claims.

## Audit Scope

1. target PDF
   - `PCB板的Mark点设计对SMT重要性.pdf`
2. current route layer
   - `P4-312`
   - `P4-353`
3. candidate stronger anchors rechecked in repo
   - `IPC-7525C` public stencil-guideline metadata
   - internal stencil-support source wording
   - `Ucamco` Gerber attribute vocabulary

## Findings

### 1. Current repo does contain narrow fiducial vocabulary anchors

- `IPC-7525C` public metadata is enough to keep `fiducials` inside a named stencil-guideline family and upstream print-control scope.
- the internal stencil-support source is enough to keep `fiducial integration` as one stencil-design feature in internal process language.
- the official `Ucamco` Gerber overview is enough to keep `fiducial` as one attribute-identity term that can exist inside manufacturing-data vocabulary.

### 2. Those anchors still do not close the actual article-side `Mark` lane

- none of the rechecked sources cleanly supports the article's board / panel / local-component scope split as a promotable official boundary
- none of the rechecked sources cleanly supports asymmetry, visibility, or visual cleanliness as SMT recognition conditions in a reusable official lane
- the current source layer still does not provide a clean public assembly-owner or library-owner anchor for `Mark` as optical alignment reference in the same sense used by `P4-353`
- the current source layer still does not support `Mark` count rules, geometry, keepout, package-local defaults, workaround guidance, machine-fit sufficiency, or outcome claims

### 3. The safest status remains route-only

- `P4-353` is still correctly indexed as `source_backed_route_available_without_new_fact_promotion`
- the current repo can safely keep:
  - `Mark` as article-side fiducial-role vocabulary
  - board / panel / local-component scope split as route language only
  - asymmetry as orientation-disambiguation context
  - visibility / cleanliness as route-level recognition wording
- the current repo still cannot cleanly convert this PDF into a new `official_fact-backed` single-PDF lane without overclaiming beyond the present authority layer

## Audit Result

- no new single-PDF authority lane was admitted in this pass
- no new `facts/`, `wiki/`, or `sources/registry/` files were added
- the per-PDF status for `PCB板的Mark点设计对SMT重要性.pdf` remains correctly route-only
- the current best evidence for this lane remains the existing route surfaces plus the narrower stencil/data-vocabulary boundaries

## What This Audit Fixes

- future AI should not reopen this `E4 Mark` PDF expecting that current `IPC-7525C`, stencil-support, or Gerber metadata already close a missed official lane
- current continuation guidance is clearer: this PDF needs a materially stronger assembly-owner, CAD-library-owner, or standards-adjacent fiducial authority before another promotion attempt is worthwhile
- the default article-side continuation should move to other controller-routed PDFs rather than recycling this same weak fiducial-evidence set

## Recommended Next Action

If `/goal` continues from here:

1. do not reopen `PCB板的Mark点设计对SMT重要性.pdf` on the current `IPC-7525C` / stencil-support / Gerber evidence set alone
2. reopen it only if a materially stronger assembly-owner, CAD-library-owner, or standards-adjacent fiducial source appears
3. otherwise continue article-side narrow recovery elsewhere in `P4-325`

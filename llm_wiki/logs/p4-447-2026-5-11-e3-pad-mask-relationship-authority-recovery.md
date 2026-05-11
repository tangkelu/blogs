# P4-447 E3 Pad-Mask Relationship Authority Recovery

Date: 2026-05-11
Lane owner: `E3 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf`

Parent surfaces:
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-371-2026-5-9-e3-multilayer-pad-mask-relationship-route-integration.md`
- `logs/p4-369-2026-5-9-e3-pad-geometry-and-pad-mask-review-route-integration.md`
- `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `facts/methods/intel-nsmd-smd-land-pad-terminology-boundary.md`

## Purpose

Advance one `E3` single-PDF pad-design lane beyond `source_backed_route_available_without_new_fact_promotion` by confirming that this article can now safely reuse already-landed narrow official support for `pad and solder-mask opening as separate review objects` plus guarded owner-scoped `NSMD/SMD` terminology existence.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep one sub-surface of this article inside the existing `released solder-mask / pad-definition manufacturing-data boundary + footprint-review governance` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `P4-371`
   - already constrained this PDF to route-only posture
   - already isolated `盖PAD / 露PAD / 半盖半露 / 等大设计` as pad-mask relationship branches while blocking numerics, factory compensation, and outcome claims

2. `P4-369`
   - already established route-safe pad-mask review posture for a sister pad-design PDF
   - already confirmed that pad-to-mask relationship can be treated as a controlled review topic without importing geometry tables

3. `methods-ipc-solder-mask-layer-and-pad-definition-boundary`
   - already supports solder mask and pad-definition topics as controlled fabrication-data scope
   - already supports the guarded boundary that pad and solder-mask opening are real review objects while exact IPC definitions and numeric rules remain incomplete

4. `methods-padstack-origin-pin1-and-footprint-review-governance-boundary`
   - already supports pad, solder mask, and footprint-review objects as controlled review surfaces
   - already blocks exact keepout, opening, geometry, and threshold numerics

5. `methods-intel-nsmd-smd-land-pad-terminology-boundary`
   - already supports one narrow owner-scoped existence proof that `NSMD / SMD` are real land-pad distinction terms in Intel guidance
   - does not turn this article into IPC terminology closure or universal branch-selection doctrine

## What Was Promoted

Promoted for this single PDF only:

- pad and solder-mask opening may be reused as separate controlled review objects
- `cover-pad` versus `open-pad` may be reused as guarded pad-mask relationship branches
- partial-cover / equal-size treatment may be reused only as pad-asymmetry or tolerance-sensitive risk branches requiring review
- this article's safest pad-design sub-surface may now stay attached to `pad-mask relationship review posture` rather than only generic route-level explanation

## What This Pass Does Not Promote

This pass still does not authorize:

- any exact pad size, opening size, area equation, tolerance band, or compensation numeric
- any universal `cover-pad / open-pad / half-cover / equal-size` selection doctrine
- any IPC-grade `mask-defined / non-solder-mask-defined / NSMD / SMD` definition closure
- any CAD UI, export, checker, or workflow-sufficiency authority
- any virtual-solder, smooth-production, yield, quality, or cost outcome claim

## E3 Lane Effect

`多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `pad-mask relationship as controlled review topic` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-447-2026-5-11-e3-pad-mask-relationship-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundaries remain narrower than any pad/opening numeric rule, IPC terminology closure, CAD UI authority, or manufacturability outcome claim
- the per-PDF `E3` entry for `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` no longer understates the pad-mask relationship sub-surface as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh

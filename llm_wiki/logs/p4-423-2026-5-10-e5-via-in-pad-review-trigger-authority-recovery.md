# P4-423 E5 Via-In-Pad Review-Trigger Authority Recovery

Date: 2026-05-10
Lane owner: `E5 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/元器件虚焊原因之一盘中孔的可制造设计规范.pdf`

Parent surfaces:
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-344-2026-5-9-e5-via-in-pad-manufacturability-route-integration.md`
- `facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `facts/methods/low-void-bga-dfm-to-process-review.md`
- `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

## Purpose

Advance one `E5` lane beyond `single_pdf_usage_route_only` by confirming that this via-in-pad article can now safely reuse an already-landed narrow official-fact boundary for package-owner-scoped via-in-pad existence and dense-BGA escape-pressure review posture.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `owner-scoped via-in-pad existence example + HDI posture + staged BGA process / inspection review` boundary.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-microchip-csp-bga-solder-land-and-pitch-examples`
   - already supports one owner-scoped exact package-layout example where `0.4 mm` land pitch uses via in pad
   - already keeps that statement inside named-package and owner-document scope rather than a cross-vendor rule

2. `methods-hdi-microvia-and-vippo-process-posture`
   - already supports via-in-pad staying inside dense-interconnect / HDI process posture rather than casual default wording

3. `methods-low-void-bga-dfm-to-process-review`
   - already supports dense BGA discussion as staged package-and-process review rather than isolated layout folklore

4. `methods-low-void-bga-reflow-paste-vs-assembly-boundary`
   - already supports solderability language staying tied to real assembly review context rather than article-side universal mechanism claims

5. `methods-hidden-joint-xray-inspection-boundary`
   - already supports hidden-joint visibility and later inspection planning as a downstream review layer in dense BGA context

6. `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`
   - already supports linking dense package review, reflow dependence, and hidden-joint inspection into one guarded process chain

## What Was Promoted

Promoted for this single PDF only:

- via-in-pad discussion may be reused as a dense-BGA escape-pressure review trigger rather than only as generic manufacturability caution
- one named owner example may now be reused to show that via in pad exists in real CSP/BGA layout guidance
- via strategy escalation may now be reused as a package-review and HDI-posture topic before later assembly execution
- via-in-pad discussion may now stay explicitly tied to downstream reflow and hidden-joint inspection review rather than layout convenience alone
- solderable-area loss or solder-transfer concern may be reused only as guarded local mechanism posture, not as deterministic defect wording

## What This Pass Does Not Promote

This pass still does not authorize:

- any fanout, line-width, spacing, annular-ring, or pitch-threshold numerics
- any universal rule that one pitch cutoff always forces via in pad
- any universal resin-fill, planarization, copper-cap, or process-sequence default
- any certainty that untreated via-in-pad always causes virtual solder, solder beads, oil burst, or downstream failure
- any cost, lead-time, capability, yield, reliability, or checker-sufficiency claim
- any supplier-neutral proof that one via-in-pad route is mandatory or superior

## E5 Lane Effect

`元器件虚焊原因之一盘中孔的可制造设计规范.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `package-owner-scoped via-in-pad existence and dense-BGA escape-pressure review-trigger` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-423-2026-5-10-e5-via-in-pad-review-trigger-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundaries remain narrower than any pitch threshold, fanout numeric, resin-fill default, or business-outcome claim
- the per-PDF `E5` entry for `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh

# P4-436 E3 Via Solder-Mask Release-Expression Authority Recovery

Date: 2026-05-10
Lane owner: `E3 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/一招搞定PCB阻焊过孔问题.pdf`

Parent surfaces:
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-367-2026-5-9-e3-via-solder-mask-treatment-route-integration.md`
- `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `facts/methods/cam-data-exchange-format-boundary.md`
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `logs/p4-344-2026-5-9-e5-via-in-pad-manufacturability-route-integration.md`
- `logs/p4-423-2026-5-10-e5-via-in-pad-review-trigger-authority-recovery.md`

## Purpose

Advance one `E3` lane beyond `single_pdf_usage_route_only` by confirming that this via solder-mask treatment article can now safely reuse an already-landed narrow official-fact boundary for `via cover/open as released solder-mask expression and release-review`, with all treatment taxonomy, default-selection, and process-result wording kept strictly outside the promoted lane.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `released solder-mask data identity + fabrication-package output boundary + guarded via-in-pad posture` lane.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-ipc-solder-mask-layer-and-pad-definition-boundary`
   - already supports `solder mask` as a released manufacturing-data layer family rather than only a canvas concept
   - already supports solder-mask design and pad-definition as an IPC-controlled document-family topic while explicitly blocking exact terminology closure for `via tenting`, `mask-defined`, `non-solder-mask-defined`, and `solder mask bridge`

2. `methods-cam-data-exchange-format-boundary`
   - already supports solder-mask layer content as part of released fabrication-data scope
   - already supports released-output completeness review without turning any data format into proof of correctness

3. `P4-367`
   - already constrained this PDF to route-only posture
   - already named released solder-mask expression as the deciding output surface for cover versus open handling while blocking all treatment numerics, universal defaults, CAD-specific recipes, checker sufficiency, and supplier-process proof

4. `methods-hdi-microvia-and-vippo-process-posture`
   - already supports via-in-pad or fill-related discussion staying inside dense-interconnect / HDI process posture rather than casual default wording

5. `P4-344` and `P4-423`
   - already support via-in-pad only as a guarded review-trigger and manufacturability branch, not as a universal process truth
   - already block resin-fill, copper-fill, planarization, plating-sequence, capability, and business-outcome expansion

## What Was Promoted

Promoted for this single PDF only:

- via `cover/open` treatment may be reused as `released solder-mask output expression` rather than only as design-canvas intent
- via solder-mask treatment may be reused as an explicit `fabrication-package release-review` topic before handoff
- missing or mismatched via cover/open intent may be reused as a `guarded output-review surface` in the released manufacturing package
- via-in-pad adjacency may be reused only as a `branch-escalation review trigger` that hands off to existing HDI / dense-interconnect posture, not as a default treatment rule

## What This Pass Does Not Promote

This pass still does not authorize:

- any via tenting, opening, hole-size, current-carrying, or treatment-threshold numeric
- any universal `cover/open/plug/resin-fill/copper-fill` default or preference rule
- any exact IPC definition closure for `via tenting`, `mask-defined`, `non-solder-mask-defined`, or `solder mask bridge`
- any Altium, PADS, Allegro, Gerber-output, menu, object-setting, or export-step recipe
- any checker completeness, DFM sufficiency, ordering-page workflow, or supplier-process proof claim
- any resin-fill, copper-fill, planarization, plating, defect, yield, reliability, cost, or lead-time outcome claim

## E3 Lane Effect

`一招搞定PCB阻焊过孔问题.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `via cover/open as released solder-mask expression and release-review` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-436-2026-5-10-e3-via-solder-mask-release-expression-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than treatment numerics, universal defaults, IPC definition closure, CAD-specific recipes, checker sufficiency, or business-outcome claims
- the per-PDF `E3` entry for `一招搞定PCB阻焊过孔问题.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh

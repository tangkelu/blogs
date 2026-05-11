# P4-420 E2 Impedance Planning And Measurement-Boundary Authority Recovery

Date: 2026-05-10
Lane owner: `E2 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB阻抗误差控制在5%，究竟有多难？.pdf`

Parent surfaces:
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-334-2026-5-9-e2-impedance-tolerance-difficulty-route-integration.md`
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
- `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
- `facts/methods/spread-glass-and-controlled-impedance-planning.md`
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `wiki/testing/rf-validation-and-test-coverage.md`

## Purpose

Advance one `E2` lane beyond `single_pdf_usage_route_only` by confirming that this impedance-difficulty article can now safely reuse an already-landed narrow official-fact boundary for controlled-impedance planning, spread-glass uncertainty, and measurement-boundary separation.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep its safest reusable surface inside the existing `stackup/material/lamination/solder-mask/verification linked planning + method-boundary separation` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-controlled-impedance-tdr-verification-posture`
   - already supports controlled impedance as a verification-linked posture rather than geometry intent alone
   - already supports keeping exact tolerance bands and verification scope refresh-sensitive

2. `methods-pcb-impedance-and-rf-measurement-method-boundary`
   - already supports TDR and frequency-domain measurement as method identity
   - already supports separating method naming from supplier capability, tolerance promise, and finished-board outcome claims

3. `methods-spread-glass-and-controlled-impedance-planning`
   - already supports spread-glass, material selection, stackup choice, copper profile, and validation as one linked planning branch
   - already supports fiber-weave or glass-versus-resin variation as a qualitative uncertainty class only

4. `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
   - already supports high-speed and impedance-sensitive work as stackup-and-fabrication planning, not as one flat capability label

5. `wiki/testing/rf-validation-and-test-coverage.md`
   - already supports keeping baseline manufacturing checks, impedance correlation, and broader RF/SI validation as separate evidence layers

## What Was Promoted

Promoted for this single PDF only:

- controlled impedance may be reused as a multivariable planning topic linked to stackup, material, lamination behavior, outer-layer finishing, and later verification posture
- spread-glass or fiber-weave variation may be reused as one qualitative uncertainty class inside impedance planning
- stackup choice, material choice, and validation posture may be reused as linked review surfaces before any tolerance promise is made
- measurement-method identity may be reused as a separate layer from supplier-capability and finished-board performance claims
- design margin may be reused as one guarded planning response to process variation rather than as proof that exact tolerance control has been closed

## What This Pass Does Not Promote

This pass still does not authorize:

- any impedance tolerance percentages, tolerance-window comparisons, or generic industry-default tolerance claims
- any exact dielectric-constant, line-width, copper-thickness, dielectric-thickness, coupon-geometry, or solder-mask-impact numerics
- any exact impedance-drop examples, exact acceptance bands, or universal coupon-coverage claims
- any claim that etching, compensation, lamination, or other process controls are sufficient to guarantee a target tolerance
- any supplier-capability, equipment-quality, RF-performance, pass/fail, cost, lead-time, or quality outcome claim
- any universal `50 ohm` design-rule explanation, compatibility doctrine, or history/default explanation
- any CTA, download, QR, or promotional-shell content

## E2 Lane Effect

`PCB阻抗误差控制在5%，究竟有多难？.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `controlled-impedance planning, spread-glass uncertainty, and measurement-boundary separation` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-420-2026-5-10-e2-impedance-planning-and-measurement-boundary-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused fact boundaries remain narrower than any tolerance promise, geometry claim, quantified solder-mask effect, or supplier-capability claim
- the per-PDF `E2` entry for `PCB阻抗误差控制在5%，究竟有多难？.pdf` no longer understates the lane as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh

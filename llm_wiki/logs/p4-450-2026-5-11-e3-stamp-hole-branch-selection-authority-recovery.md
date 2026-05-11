# P4-450 E3 Stamp-Hole Branch-Selection Authority Recovery

Date: 2026-05-11
Lane owner: `E3 narrow authority recovery`
Execution mode: `log_tracker_only`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/PCB邮票孔桥连设计要点，干货满满！.pdf`

Parent surfaces:
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-397-2026-5-10-e3-stamp-hole-panelization-boundary-route-integration.md`
- `logs/p4-374-2026-5-9-e3-stamp-hole-bridge-gap-note.md`
- `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md`

## Purpose

Advance one `E3` single-PDF stamp-hole bridge lane beyond `source_backed_route_available_without_new_fact_promotion` by confirming that this article can now safely reuse already-landed narrow official support for `stamp-hole or mouse-bite as panel-connection branch vocabulary`, with `V-cut` kept as separate branch identity and half-hole or castellated combinations kept only as special-review context.

This pass is intentionally narrow.
It does not create a new fact card.
It promotes this PDF from route-only status because the repo already has enough support to keep one sub-surface of this article inside the existing `branch-selection vocabulary + explicit panelization-input handling + special edge-feature review` posture.

## Existing Source Support Reused

This pass relies on already-landed support only:

1. `methods-stamp-hole-panelization-and-castellated-edge-boundary`
   - already supports `stamp-hole / mouse-bite` as panel-connection branch vocabulary
   - already supports `V-cut` as a separate panelization branch identity rather than a hidden default
   - already supports `castellated / half-hole` as special edge-feature review context

2. `P4-397`
   - already constrained this PDF to route-only posture
   - already isolated explicit branch selection, special breakaway handling, and special edge-review wording as the safest reusable sub-surface while blocking bridge-width, hole-size, hole-count, spacing, inset, process-order, and acceptability claims

3. `P4-374`
   - already preserved the negative boundary that this article must not be treated as geometry-rule or `V-cut` priority authority
   - already blocked process-default and customer-acceptance doctrine

## What Was Promoted

Promoted for this single PDF only:

- `stamp-hole` or `mouse-bite` may be reused as panel-connection branch vocabulary
- `V-cut` may be reused only as a separate panelization branch identity that should not be silently conflated with stamp-hole wording
- special breakaway, slot, or mixed edge-feature handling may be reused only as explicit panelization-input and special-review context
- half-hole or castellated combinations may be reused only as guarded special edge-feature review context

## What This Pass Does Not Promote

This pass still does not authorize:

- any bridge-width, hole-size, hole-count, spacing, or inset numeric
- any universal `V-cut` priority doctrine or branch-selection default
- any process-order, post-finish drilling, plating-sequence, or workaround recipe
- any acceptability, supplier-capability, cost, cycle-time, quality, or schedule claim
- any universal rule that one branch is always required for this panelization family

## E3 Lane Effect

`PCB邮票孔桥连设计要点，干货满满！.pdf` is now improved from:

- `source_backed_route_available_without_new_fact_promotion`

to:

- `official_fact-backed` for one narrow `stamp-hole as branch-selection and special-review topic` surface

The rest of the PDF remains route-only and blocked as before.

## Deliverables Created

- `logs/p4-450-2026-5-11-e3-stamp-hole-branch-selection-authority-recovery.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- the reused boundary remains narrower than any geometry numeric, `V-cut` priority doctrine, process-order rule, acceptability claim, or supplier-capability claim
- the per-PDF `E3` entry for `PCB邮票孔桥连设计要点，干货满满！.pdf` no longer understates the branch-selection and special-review sub-surface as route-only
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh

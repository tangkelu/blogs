# P4-90 Neuromorphic Conservative Rewrite Consumption

Date: 2026-05-01

## Purpose

Consume the new `P4-89` neuromorphic identity lane directly in the draft layer by rewriting `/code/blogs/tmps/2026.4.29/en/neuromorphic-computing-pcb.md` into a conservative, prompt-usable version.

This pass does not add new authority. It only removes unsupported claims and rewrites the draft so it stays inside the already-landed `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus` identity boundary plus generic board-review posture.

## Inputs Reviewed

- `logs/p4-89-neuromorphic-event-io-and-platform-identity-source-backed-integration.md`
- `facts/interfaces/neuromorphic-event-io-and-platform-identity-boundary.md`
- `wiki/processes/neuromorphic-pcb-review-boundaries.md`
- `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
- `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary.md`
- `tmps/2026.4.29/en/neuromorphic-computing-pcb.md`

## Draft Consumption Result

Rewritten draft:

- `tmps/2026.4.29/en/neuromorphic-computing-pcb.md`

What changed:

- removed unsupported deployment, production-scale, and supplier-readiness claims
- removed unsupported exact numerics for power, timing, noise, thermal, layer count, board size, turnaround, and volume
- removed blocked nouns and concept-family claims including `AER`, `STDP`, `silicon cochlea`, `COM Express`, `Jetson-compatible`, and unsupported interface-proof language
- kept `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus` only as identity references
- rewrote the article around conservative PCB review, integration planning, mixed-signal partitioning, power-rail planning, sensor attachment review, thermal/mechanical review, and prototype-to-production handoff posture
- rewrote frontmatter `description` and `tags` to remove blocked concept and capability phrasing

## What Is Now Prompt-Usable

`neuromorphic-computing-pcb.md` is now usable as a conservative draft for:

- neuromorphic board-review framing
- identity-level references to `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, and `PMBus`
- mixed-signal partitioning, power-rail planning, sensor and module attachment review, thermal/mechanical review, and staged production-planning language

## Still Blocked

- any exact `AER`, `STDP`, `silicon cochlea`, `COM Express`, `Jetson-compatible`, `sub-LVDS`, `PCIe`, `USB 3.2`, `Ethernet`, or `LVDS` claim inside this draft without a separate sourced lane
- any exact electrical, timing, power, noise, thermal, efficiency, size, turnaround, or production-volume numeric
- any claim that `Loihi 2`, `Akida`, `Speck`, `Xylo`, `DVS`, or `PMBus` proves interface behavior, board capability, deployment maturity, or product readiness
- any HILPCB-specific qualification, validated performance, or supplier-readiness claim

## Status

- draft status: `conservative_rewrite_ready`
- supporting authority status: `unchanged_from_p4_89`
- next likely action:
  - apply the same conservative-rewrite consumption pattern to the remaining `2026.4.29` drafts that already have narrow source-backed lanes

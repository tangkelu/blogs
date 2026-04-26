---
fact_id: "methods-20-layer-interconnect-reliability-workflow-boundary"
title: "20-layer interconnect-reliability workflow language should stay at evaluation-context level, not become threshold or qualification proof"
topic: "20-layer interconnect reliability workflow boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-microvia-reliability-warning-2019"
  - "ipc-tr-486-ist-round-robin-page"
  - "ipc-tm650-test-methods-index"
  - "ipc-tm650-2626a-dc-current-induced-thermal-cycling-page"
  - "ipc-tm650-2627b-convection-reflow-simulation-page"
  - "ipc-tm650-2672c-thermal-shock-continuity-page"
  - "ipc-tm650-method-development-packet-page"
  - "ipc-standards-related-resources-page"
  - "nasa-nepp-program-overview-2019"
  - "nasa-pcb-inspection-and-quality-control-2022-page"
  - "nasa-physics-of-failure-pcb-reliability-2021-page"
  - "nasa-workmanship-page"
tags: ["20-layer", "interconnect-reliability", "workflow", "ist", "tm-650", "coupon", "screening", "qualification", "boundary"]
---

# Canonical Summary

> Public IPC and NASA sources are strong enough to support a guarded `20-layer` interconnect-reliability workflow layer in `llm_wiki`: named `TM-650` method context, representative-coupon evaluation, staged `screening / qualification / test / reliable use` vocabulary, and inspection / failure-analysis workflow language. They are not strong enough to provide cycle thresholds, coupon plans, pass/fail rules, or qualification proof for a specific `20-layer` build.

## Stable Facts

- A conservative `20-layer` rewrite may describe interconnect reliability as a workflow problem rather than as one free-floating `IST` number.
- Public `IPC-TR-486` metadata supports official `IST`-adjacent report identity and correlation-study vocabulary, not universal threshold claims.
- Public `IPC-TM-650` metadata supports named method-family vocabulary for `thermal cycling`, `reflow simulation`, `thermal shock`, and continuity-based interconnect evaluation.
- Public `IPC-TM-650` method-development metadata supports repeatability / reproducibility / intended-use language around method governance, not direct production qualification proof.
- Public IPC standards-related resources support guarded representative-coupon and evaluation-resource vocabulary without exposing accepted coupon structures or pass/fail rules.
- IPC's 2019 public warning supports the claim that weak microvia interfaces can escape conventional fabrication acceptance and appear later under assembly or field stress.
- NASA `NEPP` public overview supports a staged assurance hierarchy where `screening`, `qualification`, `test`, and `reliable use` are separate governance layers rather than one collapsed outcome.
- NASA 2021/2022 public PCB evaluation records support guarded workflow wording around specimen preparation, destructive / non-destructive analysis, structural-integrity review, and mitigation planning.
- NASA workmanship metadata supports broader inspection-technique, defect-criteria, and controlled-materials / controlled-processes vocabulary as workflow context rather than as bare-board acceptance proof.
- These sources together support guarded wording that `20-layer` interconnect reliability belongs inside a documented evaluation workflow, not inside unsupported default qualification claims.

## Conditions And Methods

- Use this card when a `20-layer` draft needs to mention `IST`, `thermal cycling`, `reflow simulation`, `thermal shock`, `coupon`, `screening`, or `qualification` without leaking thresholds.
- Pair this card with `facts/methods/microvia-reliability-public-context.md`, `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`, and `facts/methods/20-layer-method-vs-qualification-boundary.md`.
- Prefer wording such as `can be evaluated through`, `belongs in a workflow that may include`, `publicly names`, and `should be validated with representative structures`.
- Keep `TM-650`, `IST`, `coupon`, `screening`, and `qualification` attached to workflow or method identity, not to accepted numbers or supplier status.

## Limits And Non-Claims

- This card does not provide `IST` cycle thresholds, coupon geometries, sample plans, temperatures, or pass/fail criteria.
- It does not prove that any `20-layer` architecture, microvia stack, or build recipe is qualified or production-approved.
- It does not turn `TM-650` method identities or `IPC-TR-486` report identity into mandatory qualification rules for a `20-layer` board.
- It does not turn NASA workflow or workmanship vocabulary into default bare-board acceptance criteria, supplier approval, or release authority.

## Open Questions

- Add a narrower follow-on only if future work needs a separate `IST` metadata card distinct from the broader interconnect workflow boundary.
- Reassess `20-layer` readiness only after stronger public threshold or supplier-evidence layers exist for the exact claim class.

## Source Links

- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://shop.electronics.org/technical-reports-white-papers/studytechnical-report
- https://www.electronics.org/test-methods
- https://www.ipc.org/sites/default/files/test_methods_docs/2-6_2-6-26a.pdf
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.27b.pdf
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.7.2c.pdf
- https://www.ipc.org/ipc-tm-650-method-development-packet
- https://www.ipc.org/ipc-standards-related-resources
- https://ntrs.nasa.gov/citations/20190001800
- https://ntrs.nasa.gov/citations/20220012424
- https://ntrs.nasa.gov/citations/20210026410
- https://sma.nasa.gov/sma-disciplines/workmanship

---
fact_id: "methods-microvia-reliability-public-context"
title: "Public microvia-reliability sources support cautionary engineering context, not universal stacked-microvia approval"
topic: "microvia reliability public context"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "ipc-microvia-reliability-warning-2019"
  - "nasa-nepp-microvia-reliability-2006"
  - "nasa-pcb-inspection-and-quality-control-2022-page"
  - "nasa-physics-of-failure-pcb-reliability-2021-page"
  - "nasa-nepp-program-overview-2019"
  - "ipc-microvia-failure-modes-paper"
  - "ipc-stacked-microvia-reliability-paper"
  - "ipc-tr-486-ist-round-robin-page"
  - "ipc-tm650-test-methods-index"
  - "ipc-tm650-2626a-dc-current-induced-thermal-cycling-page"
  - "ipc-tm650-2627b-convection-reflow-simulation-page"
  - "ipc-tm650-2672c-thermal-shock-continuity-page"
  - "ipc-tm650-method-development-packet-page"
  - "ipc-standards-related-resources-page"
  - "ipc-document-revision-table"
  - "isola-sequential-lamination-in-pcbs-note"
  - "nasa-workmanship-page"
tags: ["microvia", "stacked-microvia", "reliability", "ist", "sequential-build-up", "methods"]
---

# Canonical Summary

> Public IPC and NASA sources are strong enough to support a cautionary microvia-reliability context for advanced multilayer writing: microvias and sequential build-up solve density problems, but stacked structures, weak interfaces, registration sensitivity, and thermal-stress exposure all remain reliability concerns that should not be flattened into simple “HDI is fine” claims.

## Stable Facts

- Public NASA and IPC material supports treating microvias and sequential build-up as high-density interconnect methods driven by package-density and routing constraints.
- Public IPC technical papers provide named failure-mode vocabulary for microvia reliability discussion, including separation and crack-related mechanisms.
- Public IPC technical papers also show that stacked microvia reliability has been studied with `IST`-style methods and that registration/manufacturing interactions matter.
- IPC's public `IPC-TR-486` listing confirms a formal IPC report identity for correlating `IST` with thermal-stress and microsectioning evaluations for inner-layer-separation detection.
- IPC's 2019 public warning confirms that weak microvia interfaces can escape traditional fabrication acceptance and appear later under assembly or field stress.
- The public IPC TM-650 index confirms that relevant IPC thermal-cycling test-method families exist, but the index does not expose acceptance criteria or required limits.
- The public IPC TM-650 index also helps keep `IST`-adjacent vocabulary tied to named method families rather than to free-floating marketing cycle counts.
- The public `IPC-TM-650 2.6.26A` method page adds a stronger official anchor for guarded `D.C. current induced thermal cycling` and `interconnect evaluation` wording in `IST`-adjacent discussion.
- The public `IPC-TM-650 2.6.27B` method page adds a stronger official anchor for guarded `thermal stress`, `convection reflow assembly simulation`, and representative-coupon wording around assembly-simulation exposure.
- The public `IPC-TM-650 2.6.7.2C` method page adds a stronger official anchor for guarded `thermal shock`, `continuity`, and representative `D coupon` wording around propagated interconnect evaluation.
- IPC's public TM-650 method-development page shows that IPC test-method vocabulary belongs inside a formal method-development and validation ecosystem concerned with objective evidence, intended use, repeatability, and reproducibility.
- IPC's public standards-related resources page adds a guarded official coupon/resource layer for representative plated-hole and microvia evaluation context without exposing acceptance thresholds.
- The IPC revision table publicly shows that `IPC-2226` and `IPC/JPCA-2315` should be treated carefully as legacy or no-longer-maintained public design-guide references rather than as current public rule tables.
- Isola's official sequential-lamination note publicly strengthens the idea that repeated lamination and build-up interconnect structures belong in a distinct stress-factor and failure-mode discussion layer, not just in generic `HDI-compatible` marketing language.
- NASA's public workmanship page adds a broader quality-governance layer by linking interconnect performance and reliability to controlled materials/processes, inspection techniques, and defect criteria rather than to one isolated test method.
- NASA's public `PCB Inspection and Quality Control` record adds a stronger evaluation-workflow layer for guarded wording around specimen preparation, materials characterization, and destructive/non-destructive analysis in PCB reliability discussion.
- NASA's public `Physics of Failure` PCB-reliability record adds a stronger risk-based evaluation layer for guarded wording around structural-integrity observations, non-conformance trends, and mitigation planning.
- NASA's public `NEPP` program-overview record adds a broader public reliability-assurance hierarchy by explicitly placing `screening`, `qualification`, `test`, and `reliable use` inside one formal guidance ecosystem rather than collapsing advanced interconnect risk into a single pass/fail event.

## Conditions And Methods

- Use this card when a layer-count, HDI, or advanced-manufacturing article needs to explain why microvia reliability deserves separate engineering attention.
- Use this card when a `20-layer` draft needs to mention named `IPC` method vocabulary while still keeping `IST` thresholds and coupon details under gap-control.
- Use this card when a draft needs to mention method governance, representative coupon context, or reproducibility discipline without pretending that public IPC resources already provide qualification thresholds.
- Use this card when a draft needs to explain why sequential lamination increases interconnect-reliability sensitivity without turning supplier notes into transferable process recipes.
- Use this card when a draft needs to explain that interconnect reliability also depends on inspection and defect-recognition discipline, not only on architecture labels such as `HDI` or `stacked microvia`.
- Use this card when a draft needs guarded wording that microvia and multilayer reliability evaluation can involve specimen preparation, materials characterization, destructive/non-destructive analysis, and physics-of-failure-informed mitigation thinking without implying a fixed qualification recipe.
- Use this card when a draft needs guarded wording that parts- or interconnect-assurance can involve staged `screening`, `qualification`, `test`, and `reliable-use` logic rather than one informal reliability claim.
- Pair it with internal HDI/high-layer cards when discussing process planning, and with licensed standards or current customer requirements when discussing qualification.
- Use this card to resist overclaiming stacked microvia robustness from generic marketing copy.

## Limits And Non-Claims

- This card does not prove that stacked microvias are unacceptable, nor that they are automatically reliable.
- It does not provide universal cycle counts, geometry limits, copper-thickness rules, or pass/fail thresholds.
- It does not turn the existence of `IPC-TR-486` or other IPC papers into a universal `IST` qualification requirement.
- It does not turn public `IPC-TM-650 2.6.26A`, `2.6.27B`, or `2.6.7.2C` method identities into mandatory cycle counts, coupon plans, pass/fail criteria, or supplier qualification requirements for a `20-layer` design.
- It does not prove that public coupon resources or TM-650 method-governance pages specify the right qualification plan for a given `20-layer` design.
- It does not turn Isola's sequential-lamination note into a recommended build sequence, lamination-count allowance, or proof of acceptable reflow/field reliability for any specific board.
- It does not turn NASA workmanship governance into default bare-board acceptance criteria, supplier qualification, or mission-assurance requirements for ordinary `20-layer` builds.
- It does not turn NASA 2021/2022 NTRS evaluation vocabulary into mandatory coupon plans, PCB-specific qualification flows, acceptance thresholds, or supplier approval for a `20-layer` build.
- It does not turn NASA `NEPP` program-overview wording into PCB-specific screening plans, qualification gates, coupon structures, or acceptable microvia-reliability thresholds.
- It does not turn paper-specific study setups into general manufacturing requirements.

## Open Questions

- Add a separate public `IST` metadata card if the next batch needs a cleaner bridge from failure-mode context to method naming.
- Decide whether any-layer / ELIC public context should be split into a second card rather than staying folded into microvia-reliability discussion.
- Pair this card with stronger public build-up-material coverage before trying to rehabilitate `20-layer` any-layer or stacked-microvia blog sections.

## Source Links

- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://nepp.nasa.gov/docuploads/136AC3F6-8535-4E65-A0AD21B31AD56513/Microvia-2005E-Final-9-06.pdf
- https://ntrs.nasa.gov/citations/20220012424
- https://ntrs.nasa.gov/citations/20210026410
- https://ntrs.nasa.gov/citations/20190001800
- https://www.electronics.org/system/files/technical_resource/E12%26S06_01.pdf
- https://www.electronics.org/system/files/technical_resource/E15%26S19_03.pdf
- https://shop.electronics.org/technical-reports-white-papers/studytechnical-report
- https://www.electronics.org/test-methods
- https://www.ipc.org/sites/default/files/test_methods_docs/2-6_2-6-26a.pdf
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.27b.pdf
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.7.2c.pdf
- https://www.ipc.org/ipc-tm-650-method-development-packet
- https://www.ipc.org/ipc-standards-related-resources
- https://www.electronics.org/ipc-document-revision-table
- https://www.isola-group.com/wp-content/uploads/Sequential-Lamination-in-PCBs.pdf
- https://sma.nasa.gov/sma-disciplines/workmanship

---
fact_id: "standards-22-layer-outgassing-and-screening-acceptance-boundary"
title: "22-layer outgassing and screening language must stay as method or screening context, not universal acceptance proof"
topic: "22-layer outgassing and screening acceptance boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "astm-e595-15r21-page"
  - "nasa-vacuum-outgassing-database-page"
  - "nasa-outgassing-user-guide-page"
  - "as9102c-first-article-inspection-page"
  - "as9145-page"
  - "dlad-46-291-production-lot-testing-page"
tags: ["22-layer", "outgassing", "screening", "acceptance-boundary", "astm-e595", "nasa", "plt", "qualification"]
---

# Canonical Summary

> Public ASTM, NASA, SAE, and DLAD records are strong enough to support guarded `22-layer` wording around test-method identity, screening context, documented first-build workflow, and contract-governed lot-conformance context. They are not strong enough to prove universal outgassing acceptance, mandatory screening thresholds, accepted-lot status, or program-specific release authority.

## Stable Facts

- A conservative `22-layer` rewrite may state that outgassing and screening language belongs to method, database-screening, or contract-governed evaluation context rather than default acceptance proof.
- Public `ASTM E595` metadata supports test-method identity for vacuum-outgassing screening context, not universal acceptance authority by itself.
- Public NASA outgassing database metadata supports the claim that familiar low-outgassing values belong to a screening/database presentation layer rather than a generic bare-board acceptance rule.
- Public NASA outgassing user-guide metadata supports guarded wording that screening values and database usage need program interpretation rather than automatic product approval.
- Public `AS9102C` and `AS9145` metadata support documented first-build and product/process-validation workflow language, but not accepted screening outcomes.
- Public `DLAD 46.291` metadata supports contract-governed `production lot testing` and lot-conformance-evidence vocabulary, but not universal `PLT` sample plans or accepted-lot proof.
- These sources together support guarded wording such as `screening context`, `method identity`, `program interpretation`, and `contract-governed evidence`, not free acceptance numbers.

## Conditions And Methods

- Use this card when a `22-layer` draft mentions `outgassing`, `screening`, `TML`, `CVCM`, `PLT`, `lot conformance`, or first-build validation and risks turning them into universal release criteria.
- Pair this card with `facts/standards/high-reliability-program-and-outgassing-metadata.md`, `facts/standards/22-layer-contract-flowdown-and-lot-conformance-boundary.md`, and `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`.
- Prefer wording such as `may be used for screening`, `can sit inside program-specific interpretation`, `can be contract-governed`, and `does not prove acceptance by itself`.
- Keep outgassing values, lot-conformance terms, and screening language attached to method or contract context instead of universal acceptance.

## Limits And Non-Claims

- This card does not provide universal outgassing acceptance values, mandatory screening thresholds, sample plans, or release conditions.
- It does not prove that any `22-layer` board, adhesive system, or supplier passed a program-required outgassing screen.
- It does not prove that `PLT` was invoked, satisfied, waived, or accepted for any specific procurement.
- It does not turn test-method identity, database screening, or first-build workflow metadata into accepted-lot or release-authority proof.

## Open Questions

- Add a narrower follow-on only if future work needs to separate outgassing-screening boundaries from broader lot-conformance boundaries.
- Reassess `22-layer` readiness only after current unsupported screening/acceptance numerics are stably excluded from prompt retrieval.

## Source Links

- https://store.astm.org/e0595-15r21.html
- https://etd.gsfc.nasa.gov/capabilities/capabilities-listing/vacuum-outgassing-database/
- https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
- https://saemobilus.sae.org/standards/as9145-aerospace-series-requirements-advanced-product-quality-planning-production-part-approval-process
- https://www.acquisition.gov/dlad/46.291-production-lot-testing.

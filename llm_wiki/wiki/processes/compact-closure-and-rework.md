---
topic_id: "processes-compact-closure-and-rework"
title: "Compact Closure And Rework"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-manual-solder-rework-boundary-for-mixed-technology"
  - "methods-conformal-coating-masking-test-access-and-protection-workflow"
  - "methods-selective-solder-design-access-checks"
  - "methods-pcba-layered-inspection-stack"
  - "methods-pcba-fai-fqi-and-traceability-gates"
  - "methods-shield-aware-test-access-and-service-access"
tags: ["compact", "closure", "rework", "access", "shield", "inspection", "processes"]
---

# Definition

> Compact closure and rework is the decision layer that asks when shields, covers, coatings, connectors, and dense parts should be locked in, and what access must stay available for re-entry, inspection, and later service.

## Why This Topic Matters

- Compact assemblies fail when closure is treated as a cosmetic late step instead of a planned access boundary.
- The current corpus already supports manual touch-up, selective-solder access planning, coating access preservation, and layered inspection.
- This topic gives a single place to discuss closure timing, keep-access decisions, re-entry inspection, and release handoff for dense builds.

## Routing Guidance

- Route `closure timing` prompts here when the question is about when to lock shields, covers, coatings, or dense hardware without losing needed access.
- Route `keep-access` prompts here when the writer needs to preserve probe points, service reach, or later inspection access across a compact assembly.
- Route `re-entry` prompts here when a board may need later solder touch-up, coating repair, selective-solder access, or post-closure intervention.
- Route `inspection handoff` prompts here when the question is how SPI, AOI, X-ray, ICT, FCT, and final release connect after closure decisions.
- Keep this page as the boundary router between closure decisions and rework/inspection handoff, not as a generic rework tips page.

## Stable Facts

- Closure changes what can still be seen, probed, reworked, or serviced.
- Shield cans, covers, coatings, and dense connectors should be reviewed before the board is considered closed.
- Any manual intervention after closure should reconnect to inspection and traceability.
- The release decision should preserve enough evidence to support later validation or service work.
- Manual solder belongs inside controlled touch-up, rework, prototype, or low-density exception work rather than as the default volume route.
- Conformal coating is a masking, keep-out, inspection, and test-access workflow.
- Selective solder is an access-planning problem involving physical reach, nearby hardware, thermal shadowing, and downstream inspection.
- PCBA inspection is layered, moving from SPI to AOI, X-ray, ICT, and FCT before final release.

## Engineering Boundaries

- Do not write closure as an afterthought if it changes access.
- Keep keep-access, re-entry, rework, and final release as separate questions.
- Do not assume a closed board is automatically probe-accessible or serviceable.
- Treat closure as a boundary that can change test access, coating access, and later service access.
- Treat rework as a controlled recovery path that must rejoin inspection and traceability.

## Closure / Re-entry Boundary

- Closure timing:
  Decide when the assembly is sufficiently complete to lock down shields, covers, coatings, or compact hardware.
- Keep-access:
  Preserve only the access that downstream inspection, test, or service actually needs.
- Re-entry:
  If later touch-up or repair is possible, preserve the evidence and access path needed to re-open safely.
- Inspection handoff:
  Plan how SPI, AOI, X-ray, ICT, FCT, and final visual release connect after closure changes board access.

## Blocked Claims

- universal serviceability guarantees
- exact closure-sequence claims
- qualification and release guarantees
- cost, lead-time, and yield claims

## Common Misreadings

- Closure is not the same as completion.
- Rework is not the same as a new build.
- Access preservation is not the same as universal access.
- A board that can be closed is not automatically ready for release without inspection evidence.

## Must Refresh Before Publishing

- Any exact closure sequence
- Any access dimension
- Any customer-specific service or rework rule
- Any claim that a particular closure plan guarantees later serviceability or qualification
- Any claim that a specific re-entry path is universally valid across programs

## Related Facts And Source Scope

- `methods-manual-solder-rework-boundary-for-mixed-technology` keeps manual rework inside controlled touch-up, prototype, or exception work.
- `methods-conformal-coating-masking-test-access-and-protection-workflow` keeps coating tied to masking, keep-out, inspection, and test access.
- `methods-selective-solder-design-access-checks` keeps selective solder tied to access, keep-outs, shielding, and thermal shadowing.
- `methods-pcba-layered-inspection-stack` keeps closure handoff tied to layered inspection and validation.
- Use this page to route prompts about when to close, what to keep accessible, and how re-entry or release should be planned without claiming universal outcomes.

## Related Facts

- `methods-manual-solder-rework-boundary-for-mixed-technology`
- `methods-conformal-coating-masking-test-access-and-protection-workflow`
- `methods-selective-solder-design-access-checks`
- `methods-pcba-layered-inspection-stack`
- `methods-pcba-fai-fqi-and-traceability-gates`
- `methods-shield-aware-test-access-and-service-access`

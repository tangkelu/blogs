---
fact_id: "methods-press-fit-finish-selection"
title: "Internal pages consistently tie press-fit reliability to immersion tin first, with hole control and backplane context attached"
topic: "Press-fit finish selection"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-backplane-pcb-page-en"
tags: ["internal", "press-fit", "immersion-tin", "backplane", "finish-selection", "methods"]
---

# Canonical Summary

> Your own non-blog APT pages already express a clear internal press-fit logic: finish selection for press-fit is not isolated from drilling. `Immersion tin` is positioned as the primary fit because of insertion behavior and surface lubrication, while hole tolerance and backplane-specific mechanical control are treated as equally critical to the final result.

## Stable Facts

- The APT surface-finish page explicitly identifies `immersion tin` as the common finish for `press-fit connectors`.
- The same APT page explains that immersion tin is favored because its smooth surface helps reduce insertion force and support gas-tight cold-welded joints.
- The same page also makes clear that finish choice alone is not enough, noting that `hole diameter tolerance` and overall press-fit design remain equally critical.
- The APT drilling page pairs press-fit support with `tight hole control`, positioning press-fit holes as a distinct drilling discipline rather than generic plated holes.
- The APT backplane page repeatedly places `press-fit readiness` together with `backdrill`, high-layer structures, and backplane integration, showing that press-fit finish choice lives inside a larger mechanical and SI workflow.
- Across these pages, press-fit is framed more like an integrated connector-manufacturing problem than a simple finish menu option.

## Conditions And Methods

- Treat this as an internal capability and selection-posture card.
- Use it to support quote intake, backplane planning, connector-zone review, and future wiki work around press-fit integration.
- If a customer-facing page needs exact finish thickness, insertion-force criteria, or hole tolerance commitment, confirm with current engineering controls first.

## Limits And Non-Claims

- This card does not prove immersion tin is always the correct finish for every press-fit design.
- It does not prove finish selection can compensate for weak hole geometry, plating variation, or connector mismatch.
- It also does not replace connector-vendor requirements, hole-finish compatibility review, or project-specific press-fit qualification.

## Open Questions

- Add a follow-on card for `press-fit-and-backplane-integration-posture`
- Add a follow-on card for `connector-zone hole-control and plating review`

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json

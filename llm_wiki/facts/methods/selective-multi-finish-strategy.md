---
fact_id: "methods-selective-multi-finish-strategy"
title: "Internal selective multi-finish strategy already separates RF, digital, connector, and wire-bond zones by need"
topic: "Selective multi-finish strategy"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
tags: ["internal", "surface-finish", "selective-finish", "rf", "wire-bond", "gold-finger", "methods"]
---

# Canonical Summary

> Your internal non-blog pages already imply a practical selective-finish strategy: use premium or specialized finishes only where the board actually needs them, instead of forcing one finish across RF pads, wire-bond zones, gold fingers, and ordinary digital/control areas with very different constraints.

## Stable Facts

- The APT surface-finish page explicitly states that `selective multi-finish combinations` are supported on a single board through precision masking and sequential processing.
- The same page gives a direct example of `ENIG on SMD pads combined with hard gold on edge connector fingers`.
- The same page also states that selective finish can extend to combinations such as `OSP on general pads with ENEPIG on wire-bond areas`.
- The APT surface-finish application guide maps `hard gold` to edge connectors and `ENEPIG` to mixed solder plus wire-bond use cases, which naturally implies finish zoning by functional area.
- The APT microwave page states `Silver or ENEPIG for RF pads; ENIG/OSP for digital/control areas.`
- The APT high-frequency page says `ENIG for general RF`, while `soft gold` or `selective ENEPIG` should be reserved for wire-bond or probe-pad zones.
- The APT high-frequency and microwave pages both frame finish choice as a cost and process-planning issue, not just a materials preference.
- The HIL surface-finish landing page frames finish planning as part of engineering review before fabrication release, which supports region-by-region finish decisions instead of defaulting the whole board to one finish.

## Conditions And Methods

- Treat this card as internal process and quoting posture extracted from your own non-blog site materials.
- Use it to support intake prompts for boards that combine RF paths, digital/control circuits, edge connectors, test pads, or wire-bond devices.
- Typical internal zoning logic implied by the current pages is:
  `RF pads` -> `immersion silver` or `ENEPIG`
  `general digital/control pads` -> `ENIG` or `OSP`
  `gold fingers / repeated insertion zones` -> `hard gold`
  `wire-bond areas` -> `ENEPIG` or controlled gold-based finish only where required
- If a published article needs chemistry limits, masking constraints, or exact plating stack thickness by zone, re-check against higher-trust sources first.

## Limits And Non-Claims

- This card does not prove selective multi-finish is cost-effective for every build.
- It does not prove every fabricator workflow can combine any finishes in any sequence.
- It does not replace review of masking complexity, panel yield, assembly order, storage exposure, or inspection plan.

## Open Questions

- Add a follow-on card for `finish zoning by assembly sequence and storage exposure`
- Add a higher-trust external source layer for IPC finish standards and selective-plating process constraints

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json

---
fact_id: "methods-radio-altimeter-rf-front-end-and-integration-boundary"
title: "Radio altimeter writing is source-backed only at identity, RF-band, and subsystem-boundary level"
topic: "radio altimeter RF front-end and integration boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "faa-pcg-radio-altimeter-glossary-page"
  - "faa-aim-radio-radar-altimeter-anomalies-section"
  - "faa-eb-107-5g-c-band-aero-studies"
  - "faa-ac-20-199-draft-radio-altimeter-installation"
tags: ["radio-altimeter", "radar-altimeter", "radalt", "altimeter", "avionics", "rf-front-end", "antenna", "interface-boundary"]
---

# Canonical Summary

> Current FAA public sources support one narrow avionics boundary only: `radar altimeter` and `radio altimeter` may be treated as the same aircraft-system noun, used for direct height-above-terrain context, linked to the `4.2-4.4 GHz` commercial-aviation band, and described at transceiver / antenna / RF-cabling / display-interface boundary level. The current evidence layer does not support turning that into certification proof, universal board architecture, or exact altitude-performance claims.

## Stable Facts

- The FAA Pilot/Controller Glossary treats `radar altimeter` as a pointer to `radio altimeter`, and defines `radio altimeter` as aircraft equipment using reflected radio waves to determine aircraft height above the surface.
- The FAA AIM treats `radio altimeter`, `radar altimeter`, and `RADALT` as the same safety-critical aircraft-system family used to determine height above terrain and to supply critical data to other onboard systems and displays.
- FAA Engineering Brief `107` supports the public RF-band framing that commercial-aviation radio altimeters operate in the `4.2-4.4 GHz` band, with adjacent `5G C-band` coexistence concerns.
- FAA draft `AC 20-199` supports a subsystem boundary that can include the RA transceiver, one or more antennas, RF cables or transmission lines, and input/output interfaces such as indicator or display paths.

## Conditions And Methods

- Use this card when `altimeter-pcb.md` needs a safer route than generic aviation marketing, especially for the `radio altimeter` subset.
- Safe posture: keep the board role at RF transceiver, antenna-path, transmission-line, display-interface, and installation-boundary vocabulary.
- Pair this lane with existing RF validation, qualification-boundary, and first-article / release-governance facts when the draft also discusses harsh-environment or avionics-program context.
- Keep `barometric altimeter`, `radio altimeter`, and `laser altimeter` as separate lanes rather than collapsing them into one universal `altimeter PCB` authority claim.

## Limits And Non-Claims

- This card does not authorize `DO-160`, `DO-155`, `DO-254`, `TSO`, `DAL-A/B`, `FAR Part 91.411`, or airworthiness claims for a PCB, assembly, or supplier.
- It does not authorize exact altitude accuracy, resolution, latency, range, gain, isolation, delay, or other RF or avionics numerics.
- It does not authorize universal stackup, material, antenna, heavy-copper, or layer-count claims for all radio-altimeter boards.
- It does not authorize HILPCB deployment, approval, customer, or aviation-supply-chain proof.

## Open Questions

- Add stronger non-draft installation or product-owner sources later if a future rewrite must retain narrower board-architecture or interface-language beyond the current FAA public boundary.
- Add barometric-sensor-owner sources later if the `altimeter` draft must keep exact pressure-sensor or barometric-board authority rather than staying at system-context level.

## Source Links

- https://www.faa.gov/air_traffic/publications/atpubs/pcg_html/glossary-r.html
- https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap7_section_6.html
- https://www.faa.gov/airports/engineering/engineering_briefs/eb_107_5G_Aero_Studies
- https://www.faa.gov/aircraft/draft_docs/ac_20_199

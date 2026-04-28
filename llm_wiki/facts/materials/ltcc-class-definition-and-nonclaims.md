---
fact_id: "materials-ltcc-class-definition-and-nonclaims"
title: "KYOCERA LTCC source supports class definition, not universal ceramic-PCB processing limits"
topic: "LTCC class definition and non-claims"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "kyocera-ltcc-material-page"
  - "ceramtec-ceramic-substrates-page"
  - "kyocera-thin-film-technology-page"
tags: ["ltcc", "kyocera", "ceramic", "glass-ceramic", "copper-conductors", "alumina", "aln", "boundary"]
---

# Canonical Summary

> KYOCERA's official LTCC page supports the definition `Low Temperature Co-Fired Ceramics`, frames LTCC as glass ceramics, and says lower co-firing temperature enables use of low-electrical-resistance metals such as copper. This is class-level support only; it does not authorize universal LTCC process windows, dimensional limits, hermeticity, layer counts, or supplier capability.

## Stable Facts

- KYOCERA identifies `LTCC` as `Low Temperature Co-Fired Ceramics`.
- KYOCERA describes LTCC as glass ceramics.
- KYOCERA frames lower co-firing temperature as enabling use of low-electrical-resistance metals such as copper.
- CeramTec and KYOCERA thin-film pages already give the wiki adjacent ceramic / alumina / AlN / thin-film class context, but those are separate ceramic technology lanes.

## Conditions And Methods

- Use this card when drafts discuss LTCC, ceramic PCB, high-frequency ceramic devices, semiconductor packaging, or ceramic material classes.
- Keep LTCC distinct from all ceramic substrates, alumina thick-film circuits, AlN substrates, DBC / DPC, and thin-film ceramic technologies unless a source explicitly connects the process.
- Attach product-specific sources before quoting firing temperature, shrinkage, conductor width, via size, cavity tolerance, hermeticity, layer count, dielectric value, or RF performance.

## Limits And Non-Claims

- This card does not prove all ceramic PCBs are LTCC.
- It does not prove LTCC outperforms alumina, AlN, IMS, PTFE, or other ceramic routes.
- It does not support HIL/APT LTCC capability, process windows, cost, lead time, yield, quality, or application qualification.

## Source Links

- https://global.kyocera.com/prdct/semicon/search_material/detail/ltcc.html
- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://global.kyocera.com/prdct/semicon/semi/technology/thin-film.html

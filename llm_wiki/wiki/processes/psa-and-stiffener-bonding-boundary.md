---
topic_id: "processes-psa-and-stiffener-bonding-boundary"
title: "PSA And Stiffener Bonding Boundary"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-06"
fact_ids:
  - "methods-psa-and-stiffener-bonding-review-boundary"
source_ids:
  - "3m-adhesive-transfer-tape-467mp"
  - "molex-fpc-stiffener-application-specification"
  - "apt_flex_rigid_flex_assembly"
tags: ["psa", "stiffener", "fpc", "connector", "zif", "boundary", "processes"]
---

# Definition

> PSA and stiffener bonding is the assembly-stage boundary where adhesive wet-out, backside reinforcement, connector flatness, and stress control have to line up before the FPC can be treated as release-ready.

## Routing Guidance

- Use this page for FPC stiffener bonding, connector-fit review, and deformation control.
- Route PSA wet-out and dwell-language here when it is tied to stiffener attachment.
- Route connector-edge warpage and routing-stress review here when the board is being mounted to a specific connector family.

## Why This Topic Matters

- Stiffeners are not decorative add-ons; they change board shape, fit, and stress flow.
- PSA needs time and surface contact to develop useful bond strength.
- Connector application specs can be strict on warpage and stiffener placement.

## Stable Facts

- PSA bonding is pressure-sensitive and develops over time.
- Backside stiffener placement is a standard connector-fit control on FPCs.
- Board warpage and routing stress can damage connector performance.
- Connector-spec-scoped thickness and flatness checks belong before release, not after assembly.

## Engineering Boundaries

- Do not turn PSA into a universal adhesive claim.
- Do not turn stiffener thickness into a generic industry number.
- Do not treat connector-spec examples as proof for all FPC hardware.
- Do not separate the adhesive step from connector-fit review.

## Common Misreadings

- PSA is not the same as thermoset lamination.
- Stiffener placement is not just mechanical support; it is connector-fit control.
- Flatness matters at the connector edge, not only at the board center.
- Reflow timing matters if the PSA has not had time to wet out.

## Source Links

- https://multimedia.3m.com/mws/media/2366204O/3m-adhesive-transfer-tape-467mp.pdf?fn=3M-Adhesive-Transfer-Tape-467MP_R2.pdf
- https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationspecificationspdf/217/217716/2177160000-AS-000.pdf?inline=
- /code/hileap/frontendAPT/public/static/pcba/en/flex-rigid-flex.json


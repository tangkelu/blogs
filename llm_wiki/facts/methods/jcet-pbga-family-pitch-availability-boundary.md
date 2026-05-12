---
fact_id: "methods-jcet-pbga-family-pitch-availability-boundary"
title: "JCET's PBGA family PDF proves directly retrievable owner-scoped 1.50 mm pitch availability, not PCB land-pattern geometry"
topic: "JCET PBGA family pitch-availability boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_pbga_family_pitch_availability_without_same_surface_geometry"
canonical_unit_policy: "Preserve JCET's family-level PBGA pitch wording such as 0.65, 0.80, 1.00, 1.27, and 1.50 mm only as owner-scoped family availability context. Do not normalize this PDF into package-scoped footprint geometry or a universal pitch-to-land-pattern law."
source_ids:
  - "jcet-pbga-family-pitch-availability-and-package-context"
tags: ["jcet", "pbga", "package-house", "osat", "1.50-mm-pitch", "family-pitch-availability", "source-coverage", "boundary"]
---

# Canonical Summary

> JCET publishes a current-public official `PBGA` family PDF that is now directly retrievable in the current environment and visibly supports family-level `0.65 / 0.80 / 1.00 / 1.27 / 1.50 mm` pitch availability plus broader package-house context such as package configurations, thermal framing, and reliability framing. This is strong enough to preserve one owner-scoped package-house family boundary above snippet-only evidence. It does not expose same-surface PCB land-pattern or footprint geometry and therefore does not reopen the `1.50 mm` residual lane.

## Stable Facts

- The official JCET `PBGA` PDF is directly retrievable in the current environment.
- The publicly visible JCET family PDF supports `PBGA` as a real owner-scoped package-house family surface rather than a search-snippet-only hit.
- The visible family-level pitch wording includes:
  - `0.65 mm`
  - `0.80 mm`
  - `1.00 mm`
  - `1.27 mm`
  - `1.50 mm`
- The same family PDF also provides broader package-house context such as:
  - package configurations
  - thermal framing
  - reliability framing
- The currently reviewed public surface does not expose:
  - one same-surface PCB land-pattern geometry row
  - one same-surface footprint drawing with recommended PCB pad geometry

## Conditions And Methods

- Use this card when a prompt needs to explain that one official package-house owner source directly supports `PBGA` family pitch availability up to `1.50 mm`.
- Use it when a prompt needs to explain why `JCET` is stronger than snippet-only family identity but still below the current reopen gate.
- Treat the safe reusable rule as:
  - the official `JCET` `PBGA` family PDF is a directly reviewable owner source
  - the PDF supports family-level pitch availability and package-house framing
  - the PDF does not supply same-surface PCB land-pattern geometry
  - the `1.50 mm` lane therefore remains below reopen on this source alone
- Pair this card with:
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)
  - [renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md](/code/blogs/llm_wiki/facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md)
  - [ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md)

## Safe Blog Usage

- Explain that a package-house owner may publicly document `PBGA` family pitch availability without also publishing same-surface PCB geometry.
- Explain that `JCET` now gives the repo one directly retrievable owner-family `1.50 mm` pitch-availability surface.
- Explain that family-level owner availability still does not replace package-scoped land-pattern authority.

## Limits And Non-Claims

- This card does not authorize a `1.50 mm` PCB pad-diameter row.
- It does not authorize same-surface footprint geometry from the JCET PDF.
- It does not authorize a universal `1.50 mm pitch -> land pattern` rule across vendors or package families.
- It does not exceed the current `NXP + Renesas + AMD` exact-data stack for package-scoped public geometry.
- It does not reopen the `1.50 mm` residual by itself.

## Relationship To Local PCB资料 Intake

- This card upgrades `JCET` from `retrieval-limited family candidate` into one directly retrievable official package-house family boundary in the repo's reusable fact layer.
- It adds one cleaner package-house owner explanation for why `1.50 mm` family identity can be real while same-surface PCB geometry is still missing.
- It does not change the current reopen gate or the current completion threshold.

## Source Links

- https://www.jcetglobal.com/uploads/PBGA_22Dec2021.pdf

---
fact_id: "standards-jeita-edr-7315b-bga-public-geometry-below-1p50mm-boundary"
title: "Public JEITA EDR-7315B is a real BGA geometry-bearing standards surface, but its visible public payload still stops below a reusable 1.50 mm row"
topic: "JEITA EDR-7315B public BGA geometry below 1.50 mm boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "jeita-edr-7315b-bga-design-guide"
tags: ["jeita", "edr-7315b", "bga", "public-geometry", "1.27-mm", "1.00-mm", "1.50-mm", "boundary"]
---

# Canonical Summary

> Public `JEITA EDR-7315B` is strong enough to prove that one official standards-owner BGA design guide with visible geometry-bearing body content is publicly retrievable. The visible public payload includes BGA package-definition framing plus terminal-grid-pitch and recommended-variation coverage at `1.27 mm` and `1.00 mm`. This is materially stronger than TOC-only or discoverability-only standards surfaces. It still does not expose one visible reusable `1.50 mm` geometry row, so it does not reopen the current `1.50 mm` residual.

## Stable Facts

- `JEITA EDR-7315B` is a real official BGA design-guide PDF on a public JEITA surface.
- The visible public payload includes geometry-bearing body content rather than only metadata or topic visibility.
- The visible public payload includes terminal-grid-pitch and recommended-variation coverage for `1.27 mm` and `1.00 mm`.
- No visible public `1.50 mm` geometry row was recovered from the surfaced public content.
- The safest reusable rule is therefore:
  - `public standards-owner BGA geometry surface exists`
  - `visible public JEITA payload still stops below reusable 1.50 mm geometry`

## Conditions And Methods

- Use this card when a prompt needs a stronger public standards-owner anchor than TOC-only or discoverability-only BGA standards surfaces.
- Pair it with:
  - [ipc-7095e-bga-clause-title-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/ipc-7095e-bga-clause-title-visibility-boundary.md)
  - [j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md)
  - [ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md)
- Keep the safe reusable rule at:
  - public JEITA surface = real geometry-bearing standards-owner content
  - visible public JEITA payload = below reusable `1.50 mm` row
  - public JEITA surface != `1.50 mm` reopen

## Limits And Non-Claims

- This card does not provide one public `1.50 mm` JEITA geometry row.
- It does not authorize pad diameters, solder-mask openings, or package-variation rules for `1.50 mm`.
- It does not close the `1.50 mm` package residual.
- It does not replace owner-scoped exact rows for named `1.50 mm` packages.

## Relationship To Local PCB资料 Intake

- This card raises the standards-side ceiling above pure TOC, metadata, and discoverability surfaces by adding one real public geometry-bearing BGA design guide.
- It also tightens the continuation rule by showing that even a stronger public standards-owner geometry guide can still stay below the reopen gate when its visible rows stop at `1.27 mm` and `1.00 mm`.

## Source Links

- https://home.jeita.or.jp/tsc/std-pdf/EDR-7315B.pdf

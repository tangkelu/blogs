---
source_id: "jeita-edr-7315b-bga-design-guide"
title: "JEITA EDR-7315B Design Guide For Semiconductor Packages Ball Grid Array (BGA)"
organization: "JEITA"
source_type: "standard"
url: "https://home.jeita.or.jp/tsc/std-pdf/EDR-7315B.pdf"
jurisdiction: "japan"
published_at: ""
checked_at: "2026-05-12"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["jeita", "edr-7315b", "bga", "package-design-guide", "terminal-pitch", "variation-table", "geometry"]
status: "active"
notes: "Official JEITA public BGA design-guide PDF. Safe for public BGA package-design-guide identity, visible geometry/variation coverage, and the bounded fact that the visible public payload reaches `1.27 mm` and `1.00 mm` but does not expose one visible `1.50 mm` geometry row. Do not infer a public `1.50 mm` JEITA row from this PDF."
---

# Source Summary

## What It Covers

- official JEITA public BGA design-guide identity
- public geometry-oriented body content for square-body BGA package families
- visible terminal-grid-pitch and recommended-variation tables on the public PDF

## Why It Matters

- Adds one real public standards-owner BGA geometry surface above TOC-only, metadata-only, and discoverability-only standards anchors
- Strengthens the repo's standards-side understanding of what a genuinely public geometry-bearing standards surface looks like
- Also sharpens the current reopen gate because the visible public JEITA payload still stops below a reusable `1.50 mm` row

## Extraction Notes

- Safe for guarded wording that the public JEITA PDF is a real BGA design guide with visible geometry and variation tables
- Safe for guarded wording that the visible public terminal-pitch and recommended-variation coverage reaches `1.27 mm` and `1.00 mm`
- Safe for guarded wording that no visible public `1.50 mm` geometry row was recovered from the surfaced public content
- Do not extract a public `1.50 mm` JEITA geometry rule from this source

## Refresh Notes

- Refresh before publication because public standards-owner PDF locations can move
- Preserve the `public geometry-bearing standards surface, but still below visible 1.50 mm row` framing whenever reusing this source

---
source_id: "frontendapt-pcba-x-ray-inspection-page-en"
title: "APTPCB English X-Ray Inspection JSON"
organization: "APTPCB"
source_type: "internal_product_page"
url: "/code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-04-24"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "aptpcb", "pcba", "x-ray", "ct", "hidden-joints"]
status: "active"
notes: "Internal hyphenated X-ray inspection page covering hidden-joint inspection, CT analysis, BGA voiding, solder-bridge detection, and internal defect framing."
---

# Source Summary

## What It Covers

- X-ray and CT inspection for hidden solder joints and internal defects
- BGA, QFN, CSP, voiding, bridges, cold joints, and internal-layer-defect analysis

## Why It Matters

- Internal support source for hidden-joint inspection language on the hyphenated page variant.

## Extraction Notes

- Keep X-ray capability separate from AOI and electrical test coverage.
- Watch for duplication or divergence versus the existing non-hyphenated `xray-inspection.json` record set.

## Refresh Notes

- Re-check when the PCBA JSON is revised.

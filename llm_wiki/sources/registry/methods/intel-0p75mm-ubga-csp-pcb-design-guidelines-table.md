---
source_id: "intel-0p75mm-ubga-csp-pcb-design-guidelines-table"
title: "Packaging Chapter 15 Databook"
organization: "Intel"
owner: "Intel"
source_type: "manufacturer_packaging_databook_pdf"
url: "https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-15-databook.pdf"
jurisdiction: "global"
published_at: "2000-11-01"
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_packaging_databook_pdf"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_ubga_csp_pcb_design_guideline_table"
source_origin_path: "official Intel-hosted packaging databook PDF"
source_page_range: "page 15-10 Table 15-10"
confidence: "medium"
topic_tags: ["intel", "ubga", "csp", "0.75-mm-pitch", "pcb-design-guidelines", "exact-data", "fourth-owner"]
status: "active"
notes: "Official Intel-hosted packaging databook PDF. Safe for the printed `.75mm µBGA CSP Package` PCB design table only. Use as a fourth-owner exact-data route for the 0.75 mm package lane. Do not convert this owner-scoped table into a universal cross-vendor 0.75 mm pitch-to-land-pattern rule."
---

# Source Summary

## What It Covers

- Intel-hosted packaging databook `Chapter 15`
- printed `.75mm µBGA CSP Package` context
- same-table `PCB Design Guidelines` values for the `.75mm µBGA CSP Package`

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a fourth materially independent current-public owner exact row for the still-open `0.75 mm` package lane
- Raises the local `0.75 mm` ceiling above `Microchip x3 + Renesas + NXP`

## Extraction Notes

- Safe for the printed package context:
  - `.75mm µBGA CSP Package`
- Safe for the printed same-table guideline values:
  - `Soldermask Opening Dia 0.375-0.425`
  - `Pad Diameter 0.325-0.375`
  - `Via Diameter 0.25-0.30`
  - `Number of Traces Between Pads 1`
- Do not rewrite this source into a generic cross-vendor `0.75 mm` BGA or CSP footprint law

## Refresh Notes

- Stable Intel-hosted packaging databook PDF; refresh only if a later prompt needs a newer Intel-hosted package-guide revision or broader `0.75 mm` owner coverage
- Preserve the printed `.75mm µBGA CSP Package` table scope whenever reusing any geometry

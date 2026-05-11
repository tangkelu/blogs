---
source_id: "intel-agilex-7-board-decoupling-capacitors-guide"
title: "Intel Agilex 7 M-Series Device Design Guidelines: Board Decoupling Capacitors Guide"
organization: "Intel"
owner: "Intel"
source_type: "design_guide_section"
url: "https://www.intel.com/content/www/us/en/docs/programmable/683393/current/board-decoupling-capacitors-guide.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_design_guide"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_fpga_board_decoupling_placement_guidance"
source_origin_path: "official Intel Agilex 7 board decoupling capacitor placement guide"
source_page_range: "board decoupling capacitors guide"
confidence: "medium"
topic_tags: ["intel", "agilex", "fpga", "board-decoupling", "power-pins", "placement", "bottom-side", "via-field"]
status: "active"
notes: "Official Intel device-design guide section. Safe for guarded wording that board-side decoupling can be organized in close package-side families such as underside, via-field, or periphery placement when kept near the package shadow or pin field. Do not use it for universal backside rules, exact counts, or package-family generalization beyond owner-scoped context."
---

# Source Summary

## What It Covers

- board-side decoupling-capacitor placement families around a large FPGA package
- close package-side placement such as underside, pin-field, or periphery context
- maintaining local proximity rather than treating capacitor placement as a generic anywhere-on-board task

## Why It Matters

- gives the corpus one current-public owner source that is closer to the handbook's `backside / near-pin / local entry` posture than the earlier generic capacitor-role material
- helps contain local decoupling placement as a package-shadow problem instead of a universal backside recipe

## Extraction Notes

- Safe for guarded statements that local board decoupling may sit on the underside, in the via field, or around the device periphery when it remains close to the package region being supported.
- Safe for wording that package-shadow proximity matters more than generic board placement.
- Do not use this guide for exact capacitor counts, exact package cavity geometry, or universal placement hierarchy claims.

## Refresh Notes

- Refresh before reuse if Intel updates the Agilex 7 device-design guide or section anchors.

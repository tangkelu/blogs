---
source_id: "intel-fpga-general-rules-for-capacitor-and-power-plane-placement"
title: "Intel Power Distribution Network Design Methodology Guide: General Rules for Capacitor and Power Connections"
organization: "Intel"
owner: "Intel"
source_type: "design_guide_section"
url: "https://www.intel.com/content/www/us/en/docs/programmable/683883/current/general-rules-for-capacitor-and-power.html"
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
scope_type: "vendor_scoped_fpga_power_connection_and_decoupling_placement_guidance"
source_origin_path: "official Intel FPGA PDN design methodology guide capacitor and power connection rules"
source_page_range: "general rules for capacitor and power connections"
confidence: "medium"
topic_tags: ["intel", "fpga", "pdn", "decoupling", "power-plane", "power-pins", "placement", "bga"]
status: "active"
notes: "Official Intel design-guide section. Safe for guarded wording that decoupling capacitors should stay in close proximity to the power plane or pin field they support and that power and ground planes should stay close to the FPGA to reduce loop and via inductance. Do not use it for exact wavelength spacing, exact capacitor counts, or device-independent topology rules."
---

# Source Summary

## What It Covers

- capacitor and power-plane placement rules for FPGA power-distribution design
- close proximity between a decoupling capacitor and the power structure it supports
- keeping power and ground planes close to the package to reduce inductive burden

## Why It Matters

- adds a second semiconductor-owner source for near-device decoupling placement and package-side current-path control
- strengthens the local corpus above role vocabulary alone and above switcher-input-only placement language

## Extraction Notes

- Safe for guarded statements that local decoupling should stay close to the power plane, pin field, or package region being supported.
- Safe for wording that plane spacing and package-side current-path geometry matter because BGA via inductance is part of the local loop.
- Do not use this section for exact placement distances, exact capacitor ordering, or universal FPGA-independent recipes.

## Refresh Notes

- Refresh before reuse if Intel revises the current PDN guide section or navigation path.

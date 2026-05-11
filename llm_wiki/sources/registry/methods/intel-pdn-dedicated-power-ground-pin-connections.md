---
source_id: "intel-pdn-dedicated-power-ground-pin-connections"
title: "Intel Power Distribution Network Design Methodology Guide: Dedicated Power and Ground Pin Connections"
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
scope_type: "vendor_scoped_power_ground_pin_and_decoupling_dedicated_plane_connection_guidance"
source_origin_path: "official Intel FPGA PDN design methodology guide general rules for capacitor and power connections"
source_page_range: "general rules for capacitor and power connections"
confidence: "medium"
topic_tags: ["intel", "fpga", "pdn", "power-pins", "ground-pins", "dedicated-via", "decoupling", "plane-connection"]
status: "active"
notes: "Official Intel PDN design-guide section. Safe for guarded wording that each power or ground pin and each decoupling capacitor terminal should have its own dedicated connection into the relevant plane structure, and that shared vias are discouraged because they add spreading inductance. Do not use it for exact via counts or universal one-via-per-pin doctrine."
---

# Source Summary

## What It Covers

- dedicated plane connections for power and ground pins
- dedicated vias for decoupling capacitor power and ground terminals
- why shared vias are discouraged in local power connections

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that is narrower than generic local-decoupling placement because it governs how the pin or capacitor terminal enters the plane
- helps separate local `placement near the load` from local `dedicated plane connection without shared-via spreading-inductance penalty`

## Extraction Notes

- Safe for guarded wording that power and ground pins should connect into the relevant plane structure through dedicated local connections rather than through shared-via bottlenecks.
- Safe for wording that decoupling capacitor terminals should also have dedicated vias or local plane entry rather than sharing vias.
- Safe for guarded wording that shared vias increase spreading inductance and are therefore discouraged in this local plane-entry context.
- Do not use this guide for exact via counts, exact via dimensions, or universal package-independent pin recipes.

## Refresh Notes

- Refresh before reuse if Intel revises the PDN guide section or navigation path.

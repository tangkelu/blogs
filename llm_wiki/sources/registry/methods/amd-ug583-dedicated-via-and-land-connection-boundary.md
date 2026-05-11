---
source_id: "amd-ug583-dedicated-via-and-land-connection-boundary"
title: "AMD UG583 UltraScale PCB Design Guide: Dedicated Via and Land Connection Boundary"
organization: "AMD"
owner: "AMD"
source_type: "design_guide_section"
url: "https://docs.amd.com/r/en-US/ug583-ultrascale-pcb-design/Possibility-2-Parasitic-Inductance-of-Planes-Vias-or-Connecting-Traces"
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
scope_type: "vendor_scoped_decoupling_land_to_via_direct_connection_guidance"
source_origin_path: "official AMD UltraScale PCB design guide parasitic inductance section"
source_page_range: "parasitic inductance of planes vias or connecting traces"
confidence: "medium"
topic_tags: ["amd", "xilinx", "ultrascale", "decoupling", "vias", "land-connection", "parasitic-inductance", "shared-via"]
status: "active"
notes: "Official AMD guide section. Safe for guarded wording that decoupling-via connections should go directly to the capacitor lands rather than through trace segments, and that sharing vias across multiple capacitors is poor practice because it adds inductive burden. Do not use it for exact via counts or universal geometry rules."
---

# Source Summary

## What It Covers

- direct land-to-via connection posture for decoupling paths
- inductive penalty of trace segments between lands and vias
- why sharing vias between capacitors is discouraged

## Why It Matters

- gives the corpus one current-public semiconductor-owner source that sharpens the local plane-entry side of decoupling implementation beyond `place it near the load`
- helps contain the lane to local inductive cleanup at the land and via entry rather than expanding into generic high-current routing or exact via recipes

## Extraction Notes

- Safe for guarded wording that decoupling vias should connect directly at the capacitor lands rather than through extra trace segments.
- Safe for wording that shared vias across multiple decoupling capacitors are discouraged because they add inductive burden.
- Safe for treating this as a local connection-quality and plane-entry problem rather than as a via-count doctrine.
- Do not use this section for exact via counts, exact via sizes, or universal package-family rules.

## Refresh Notes

- Refresh before reuse if the AMD guide revision or section anchor changes.

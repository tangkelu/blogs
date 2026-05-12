---
source_id: "intel-emif-ddr4-general-layout-routing-guidelines"
title: "External Memory Interfaces Agilex 7 F-Series and I-Series FPGA IP User Guide: General Layout Routing Guidelines"
organization: "Intel"
owner: "Intel"
source_type: "manufacturer_user_guide"
url: "https://www.intel.com/content/www/us/en/docs/programmable/683216/23-2-2-7-1/general-layout-routing-guidelines-21541.html"
jurisdiction: "global"
published_at: "2025-01-30"
checked_at: "2026-05-12"
retrieved_at: "2026-05-12"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_user_guide"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_ddr4_external_memory_interface_layout_guidance"
source_origin_path: "official Intel online documentation for Agilex 7 External Memory Interfaces"
source_page_range: "section 6.5.3 General Layout Routing Guidelines"
confidence: "medium"
topic_tags: ["intel", "emif", "ddr4", "memory-interface", "reference-plane", "return-path", "ground-stitching-vias", "skew-matching", "serpentine-routing"]
status: "active"
notes: "Official Intel memory-interface layout guidance. Safe for guarded DDR4/EMIF routing-governance wording about solid ground reference planes, uninterrupted return paths, nearby ground stitching vias for layer transitions, avoiding unnecessary transitions, time-domain length and skew matching, same-byte/group layer discipline, and serpentine routing as controlled compensation. Do not use it for universal DDR recipes, exact layout numerics, timing closure, validation success, or non-Intel product capability claims."
---

# Source Summary

## What It Covers

- Intel Agilex 7 external memory interface layout guidance for routing from FPGA to memory.
- Solid ground reference plane and uninterrupted return-path posture for memory-interface routing.
- Ground stitching vias near signal vias when memory signals change layers.
- Avoidance of unnecessary layer transitions because they can increase crosstalk, loss, and skew risk.
- Time-domain length and skew matching as memory-interface routing goals.
- Same byte or group routed together on the same layer to reduce layer-transition mismatch effects.
- Serpentine routing only as a controlled routing strategy under explicit memory-interface guidance.

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf` one official owner-backed route for the `D4` memory-interface claim family.
- Raises the `194页` handbook above claim-family-only wording for one memory-routing surface without importing handbook timing, impedance, spacing, via-count, or serpentine geometry numerics.
- Complements the existing generic return-path and via-transition cards with a memory-interface-specific owner source.

## Extraction Notes

- Safe for guarded wording that memory-interface routing should preserve solid reference-plane and local return-path continuity.
- Safe for guarded wording that memory-interface layer changes need nearby ground stitching vias and that unnecessary layer transitions should be avoided.
- Safe for guarded wording that time-domain length and skew matching are memory-interface routing goals.
- Safe for guarded wording that serpentine routing is a compensation technique under controlled routing guidance, not a default decorative routing style.
- Do not copy Intel's exact spacing, board-thickness, via-distance, or connector-specific geometry values into general facts unless a later prompt explicitly stays inside Intel's documented configuration.

## Refresh Notes

- Refresh before publication if a prompt depends on current Intel Agilex 7 EMIF revision wording, version number, topology-specific figures, or connector-specific layout details.

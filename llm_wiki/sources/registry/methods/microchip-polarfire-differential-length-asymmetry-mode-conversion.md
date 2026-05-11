---
source_id: "microchip-polarfire-differential-length-asymmetry-mode-conversion"
title: "PolarFire FPGA Board Design User Guide"
organization: "Microchip"
owner: "Microchip"
source_type: "user_guide_section"
url: "https://onlinedocs.microchip.com/oxy/GUID-ABAC3251-8552-4A5C-A63D-D9BCAEA91FEF-en-US-2/GUID-9E991AE0-B5D2-452E-9AD3-A73224AEEC25.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_user_guide"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_differential_length_asymmetry_to_common_mode_conversion_guidance"
source_origin_path: "official Microchip PolarFire FPGA board design user guide differential traces section"
source_page_range: "3.2.1.1 Differential Traces"
confidence: "medium"
topic_tags: ["microchip", "polarfire", "fpga", "differential-pair", "length-match", "asymmetry", "common-mode-conversion", "high-speed"]
status: "active"
notes: "Official Microchip board design guide section. Safe for guarded wording that intra-pair asymmetry in high-speed differential traces causes conversion from differential behavior into common-mode behavior. Do not use it for universal numeric skew budgets or broad interface-independent signoff claims."
---

# Source Summary

## What It Covers

- tight intra-pair length matching for high-speed differential traces
- asymmetry in pair length causing conversion into common-mode behavior

## Why It Matters

- gives the corpus one current-public owner source that explicitly connects differential-pair asymmetry to `common-mode` conversion language, making this lane cleaner than generic symmetry or return-path wording alone

## Extraction Notes

- Safe for guarded wording that differential-pair asymmetry can convert some differential behavior into common-mode behavior.
- Safe for wording that tight intra-pair length matching matters in high-speed differential routing.
- Do not use this source for exact skew limits, exact interface numbers, or broad SI/EMI signoff claims.

## Refresh Notes

- Refresh before publication if the online section wording or navigation path changes.

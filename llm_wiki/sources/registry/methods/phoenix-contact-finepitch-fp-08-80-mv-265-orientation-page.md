---
source_id: "phoenix-contact-finepitch-fp-08-80-mv-265-orientation-page"
title: "FP 0,8/ 80-MV 2,65 - SMD male connectors - 1061704"
organization: "Phoenix Contact"
owner: "Phoenix Contact"
source_type: "manufacturer_product_page"
url: "https://www.phoenixcontact.com/en-us/products/smd-male-connector-fp-08-80-mv-265-1061704"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-12"
retrieved_at: "2026-05-12"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "connector_owner_layout_authority"
exact_data_class: "boundary_convention"
scope_type: "named_series_connector_owner_orientation_boundary"
source_origin_path: "official Phoenix Contact current-public product page"
source_page_range: "product-page text visible in the current-public page"
confidence: "high"
topic_tags: ["phoenix-contact", "finepitch", "connector", "pin-1", "position-a1", "orientation", "plug-direction", "pcb-assembly", "series-specific"]
status: "active"
notes: "Official Phoenix Contact product page. Use for named-series wording that position a1 / row a / pin 1 is marked on the item, that PCB-assembly orientation and plug-in direction are clearly defined, and that customer documentation may override the definition. Do not generalize this into a universal connector-origin doctrine."
---

# Source Summary

## What It Covers

- official Phoenix Contact FINEPITCH board-to-board product identity for one named connector series
- current-public owner wording that `position a1 (row a, pin 1)` is marked on the item
- current-public owner wording that `position 1` is also marked in the drawings and that PCB-assembly orientation plus plug-in direction are clearly defined
- current-public owner wording that the customer may provide a different definition in its own documentation

## Why It Matters

- Adds one more current-public connector-owner route above generic drawing-context support alone
- Strengthens the repo's named-series evidence that connector orientation can be explicitly controlled by owner documentation rather than guessed from local habit
- Helps the connector-origin lane reuse one owner-controlled chain from physical `pin 1` marking to PCB-assembly orientation and plug-in direction, while keeping customer override visible

## Extraction Notes

- Safe for guarded wording that a named Phoenix Contact FINEPITCH series marks `position a1 / row a / pin 1` on the item and in the owner documentation
- Safe for guarded wording that the same owner page treats orientation for PCB assembly and plug-in direction as explicitly defined for the named series
- Safe for guarded wording that customer documentation may redefine the orientation convention for its own project documentation
- Do not extract one universal connector-origin doctrine, one universal `pin-1` origin law, or one board-level installation-mark geometry rule from this product page alone

## Refresh Notes

- Refresh before publication because current-public product pages and embedded documentation text can move
- Preserve the `named-series owner wording with explicit customer-override clause` framing whenever reusing this source

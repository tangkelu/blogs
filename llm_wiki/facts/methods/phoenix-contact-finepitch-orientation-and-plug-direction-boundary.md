---
fact_id: "methods-phoenix-contact-finepitch-orientation-and-plug-direction-boundary"
title: "Phoenix Contact FINEPITCH connector orientation and plug-direction wording is reusable only as named-series owner guidance"
topic: "Phoenix Contact FINEPITCH orientation and plug-direction boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
exact_data_class: "boundary_convention"
scope_type: "named_series_connector_owner_orientation_boundary"
canonical_unit_policy: "Preserve original owner wording such as position a1, row a, pin 1, PCB assembly, plug-in direction, and customer documentation override. Do not normalize these into one universal connector-origin or installation-mark doctrine."
source_ids:
  - "phoenix-contact-finepitch-fp-08-80-mv-265-orientation-page"
tags: ["phoenix-contact", "finepitch", "connector", "pin-1", "orientation", "plug-direction", "pcb-assembly", "series-specific"]
---

# Canonical Summary

> Current official Phoenix Contact FINEPITCH product-page wording is strong enough to promote one narrow named-series owner boundary: `position a1 (row a, pin 1)` is marked on the item, `position 1` is also marked in the owner drawings, and the orientation of the item for PCB assembly plus the plug-in direction are thus clearly defined. The same owner page also states that customer documentation may provide a different definition. This supports one guarded rule for named-series orientation documentation, not one universal connector-origin doctrine or one universal installation-mark law.

## Stable Facts

- Phoenix Contact FINEPITCH owner wording marks `position a1 / row a / pin 1` on the named item.
- Phoenix Contact states that `position 1` is also marked in the owner drawings for the named series.
- Phoenix Contact states that the orientation of the item for PCB assembly and the plug-in direction are clearly defined for the named series.
- Phoenix Contact also states that the customer may provide a different definition in its own documentation.
- The safest reusable rule is therefore `named-series owner orientation guidance with explicit customer override`, not universal connector-origin doctrine.

## Conditions And Methods

- Use this card when a prompt needs current-public owner wording that ties a named connector's `pin 1` mark to PCB-assembly orientation and plug-in direction.
- Use it only for named-series documentation posture, not for generic connector defaults across unrelated families.
- Treat the safe reusable rule as:
  - named connector orientation should come from owner documentation when available
  - owner wording can bind physical `pin 1` marking, drawing marking, and assembly-direction context together
  - project documentation may still redefine the working convention, so the owner page does not become one immutable universal doctrine

## Safe Blog Usage

- Explain that named connector families may define orientation explicitly in owner documentation instead of leaving it to local convention.
- Explain that `pin 1` marking, assembly orientation, and plug-in direction can be linked together in a released owner page for a specific family.
- Explain that project documentation should keep the chosen convention explicit when an owner page also allows customer-defined documentation.

## Limits And Non-Claims

- This card does not authorize one universal left/right or `pin-1` origin rule for all connectors.
- It does not authorize one universal installation-mark geometry, layer, symbol, or size.
- It does not authorize one cross-vendor doctrine for board-to-board, wire-to-board, mezzanine, USB, or SFP connectors as a single class.
- It does not authorize standards-owner marking doctrine or assembly acceptability claims.

## Relationship To Local PCB资料 Intake

- This card partially narrows two still-open doctrine surfaces named in `P4-309`:
  - `connector-origin defaulting at universal-rule level`
  - stronger `installation mark` authority
- It does so only by adding one more named-series current-public owner route that explicitly links `pin 1` marking to PCB-assembly orientation and plug-in direction.
- It still does not close universal connector-origin doctrine, board-level installation-mark geometry, or package-family-specific marking conventions.

## Source Links

- https://www.phoenixcontact.com/en-us/products/smd-male-connector-fp-08-80-mv-265-1061704

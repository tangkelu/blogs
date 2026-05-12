---
fact_id: "methods-bomdoc-cross-probe-and-pcb-location-context-boundary"
title: "A BOM document can cross-probe corresponding PCB components and expose PCB location context, while assembly correctness remains out of scope"
topic: "BOM document cross-probe and PCB location-context boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
source_ids:
  - "altium-bomdoc-cross-select-and-cross-probe-between-bom-and-pcb"
  - "altium-activebom-column-settings-pcb-location-rotation-side"
tags: ["bom", "bomdoc", "cross-probe", "pcb", "location", "rotation", "side-of-board", "methods"]
---

# Canonical Summary

> Current official Altium coverage is strong enough to support one narrow visual-BOM boundary: a BOM-document surface can navigate to corresponding design objects in the PCB and can expose PCB-derived location context such as board position, rotation, and side. This boundary supports review-navigation and board-context wording only. It does not authorize automatic matching, pad-level geometry closure, polarity-proof, progress-tracking, inventory accuracy, or hand-soldering correctness claims.

## Stable Facts

- Official Altium documentation for creating the BOM document supports the boundary that BOM-item selection can cross-select or cross-probe corresponding objects in schematic and PCB documents.
- Official Altium column-settings documentation supports the boundary that BOM-visible columns can include PCB-derived metadata such as component location, rotation, and side of board.
- From those sources together, the repo can safely preserve one narrow rule for `E7`: a visual BOM surface may be used as a navigation and position-context review layer between a parts list and corresponding PCB components.

## Conditions And Methods

- Use this card when a draft needs conservative wording for BOM-linked PCB navigation or BOM-visible board-position context.
- Treat the safe reusable rule as:
  - a BOM item may be linked to corresponding PCB objects for review navigation
  - BOM-visible metadata may include PCB location context
  - PCB location context may include rotation and board side
  - this is a review-navigation surface, not proof of correct matching or correct assembly execution
- Pair this card with:
  - [package-to-footprint-and-pin-count-alignment-review-boundary.md](/code/blogs/llm_wiki/facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md)
  - [pcba-test-method-input-package-boundary.md](/code/blogs/llm_wiki/facts/methods/pcba-test-method-input-package-boundary.md)
- Keep this card at navigation and context level; if a prompt needs exact pad geometry, exact placement coordinates, or package-owner land-pattern closure, escalate to stronger owner or standards-backed sources.

## Safe Blog Usage

- Explain that a visual BOM can serve as a navigation layer between the parts list and corresponding PCB components.
- Explain that BOM-side review can expose PCB location, rotation, and side-of-board context.
- Explain that BOM-to-PCB navigation helps review context, but does not by itself prove package correctness or assembly correctness.

## Limits And Non-Claims

- This card does not prove automatic BOM matching completeness or accuracy.
- It does not prove pad-level or all-pad-position visibility.
- It does not prove pin-1 marker correctness, polarity-proof, or progress-marking correctness.
- It does not authorize IQC counting accuracy, repair-efficiency claims, or hand-soldering outcome claims.
- It does not authorize universal BOM-viewer behavior across tools.

## Provenance Boundary

- The `E7` article lane can safely contribute the demand signal that users want BOM-linked board-context review.
- The branded article itself does not act as authority for welding-assistance claims, inventory-checking claims, or tool-sufficiency promises.

## Source Links

- https://www.altium.com/documentation/altium-designer/activebom/creating-document
- https://www.altium.com/documentation/altium-designer/activebom-dlg-dialogcolumnsettingsselect-columns-activebom-ad?version=18.0

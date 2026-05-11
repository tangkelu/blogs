---
fact_id: "methods-hole-spacing-reliability-boundary"
title: "Hole spacing may be reused only as a standards-adjacent and CAD-owner reliability-review boundary, not as a universal spacing law"
topic: "Hole spacing reliability boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "boundary_convention"
scope_type: "standards_adjacent_and_cad_owner_reliability_review_boundary"
canonical_unit_policy: "Preserve source wording such as hole wall to hole wall, hole-to-hole clearance, hole-to-object clearance, annular ring, cracks and wicking, and CAF risk assessment. Do not normalize these into a universal hole-spacing threshold or acceptance rule."
source_ids:
  - "ecss-q-st-70-12c-rev1-pcb-design-standard"
  - "altium-hole-to-hole-clearance-rule"
  - "altium-hole-to-object-clearance-rule"
  - "kicad-getting-started-guide"
tags: ["hole-spacing", "hole-to-hole", "hole-to-object", "clearance", "annular-ring", "drill-breakout", "drill-wander", "CAF", "reliability", "ecss", "cad-owner"]
---

# Canonical Summary

> Current repo-backed official coverage is strong enough to land one narrow boundary card for hole-spacing language. `ECSS-Q-ST-70-12C Rev.1` gives a standards-owner context where `hole wall to hole wall`, `annular ring`, and `cracks and wicking` belong to formal PCB design-rule vocabulary, while `CAF risk assessment` keeps spacing-sensitive insulation risk inside a governed reliability posture. Altium's public documentation gives CAD-owner manufacturing-rule identity for `hole-to-hole clearance` and `hole-to-object clearance`, and KiCad gives a clearance-aware PCB workflow anchor. Together these sources support one guarded review boundary: hole spacing may be discussed as a reliability and failure-risk review topic, including annular-ring weakening, breakout-like damage, drill-wander caution, and CAF context. They do not support a universal spacing rule or acceptance criterion.

## Stable Facts

- `ECSS-Q-ST-70-12C Rev.1` is an official PCB design-rule standard.
- The current ECSS public standard layer is strong enough to keep `hole wall to hole wall`, `annular ring`, and `cracks and wicking` inside a governed PCB design-rule context.
- The current ECSS public standard layer is strong enough to keep `CAF risk assessment` inside a governed reliability-review context for PCB spacing-sensitive insulation risk.
- Altium public documentation identifies `hole-to-hole clearance` as a manufacturing-rule family.
- Altium public documentation identifies `hole-to-object clearance` as a manufacturing-rule family.
- KiCad public workflow documentation supports a clearance-aware PCB layout and handoff context.

## Exact Data Scope

- exact for:
  - standards-adjacent vocabulary that hole wall spacing belongs to governed PCB-rule context
  - `hole-to-hole clearance` as an Altium manufacturing-rule identity
  - `hole-to-object clearance` as an Altium manufacturing-rule identity
  - guarded reliability / failure-risk vocabulary around hole spacing
- not exact for:
  - all numeric hole-spacing thresholds
  - universal acceptance criteria
  - supplier capability claims
  - CAF lifetime claims
  - guaranteed manufacturability claims

## Conditions And Methods

- Use this card when a prompt needs guarded wording for hole-spacing as a design-review boundary.
- Keep the wording at review and taxonomy level:
  - annular-ring weakening or breakout-like caution
  - cracks and wicking caution
  - drill-wander caution
  - CAF risk context

## Safe Blog Usage

- Explain that hole spacing belongs in a reliability and failure-risk review family.
- Explain that standards-owner and CAD-owner sources can name this review family without turning it into universal numbers.
- Explain that spacing-sensitive failure language should stay as review vocabulary unless stronger public threshold authority is recovered.

## Limits And Non-Claims

- This card does not authorize a universal minimum hole spacing.
- It does not authorize exact annular-ring or breakout tables.
- It does not authorize an acceptance criterion or supplier-capability claim.
- It does not authorize any exact value extracted from the article's threshold text.

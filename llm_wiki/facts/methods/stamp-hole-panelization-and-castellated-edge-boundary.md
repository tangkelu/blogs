---
fact_id: "methods-stamp-hole-panelization-and-castellated-edge-boundary"
title: "Stamp-hole or mouse-bite panelization wording is reusable only as branch-selection and special-edge review vocabulary"
topic: "Stamp-hole panelization and castellated edge boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
exact_data_class: "boundary_convention"
scope_type: "manufacturer_owner_plus_process_boundary"
canonical_unit_policy: "Preserve source wording such as V-cut, mouse-bites, stamp holes, castellated holes, panelization, and special process. Do not normalize these into universal bridge-width, hole-size, spacing, process-order, or acceptability doctrine."
source_ids:
  - "jlcpcb-castellated-holes-capability-guide"
  - "jlcpcb-panelization-v-cut-and-mouse-bites-guide"
  - "frontendapt-pcb-pcb-profiling-page-en"
tags: ["stamp-hole", "mouse-bite", "v-cut", "panelization", "castellated-holes", "half-hole", "edge-feature", "branch-selection"]
---

# Canonical Summary

> Current repo-backed official coverage is strong enough to land one narrow boundary card for `stamp-hole / mouse-bite / V-cut / castellated-edge` wording. JLCPCB's public manufacturer guidance gives owner-scoped identity for `castellated holes` as a special edge-feature family and separately keeps `V-cut` and stamp-hole or slot panel-board requests inside explicit panelization-input handling rather than ordinary default assumptions. The existing internal APT profiling page already supports `V-score`, tab routing, laser singulation, edge plating, and castellation as downstream manufacturing-route choices. Together these sources support one guarded rule: `V-cut`, `stamp-hole / mouse-bite`, and `castellated / half-hole` may be discussed as branch-selection and special-edge review vocabulary, not as universal geometry or process-law closure.

## Stable Facts

- JLCPCB public guidance identifies `castellated holes` as a named PCB edge-feature family that needs explicit handling.
- JLCPCB public guidance keeps `V-cut` inside a specific panelization branch rather than a universal split method.
- JLCPCB public guidance treats stamp-hole or slot panel-board requests as explicit panelization-input surfaces, not invisible defaults.
- The internal APT profiling page treats `V-score`, tab routing, laser singulation, edge plating, and castellation as downstream manufacturing-route choices.

## Exact Data Scope

- exact for:
  - `castellated holes` as a manufacturer-owner edge-feature identity
  - `V-cut` as a panelization branch identity
  - stamp-hole or mouse-bite style handling as explicit panelization-input vocabulary
  - guarded wording that special edge features and branch choices deserve explicit review
- not exact for:
  - bridge-width numerics
  - hole-size, hole-count, spacing, or inset rules
  - `V-cut` priority doctrine
  - half-hole process-order or plating-sequence rules
  - acceptability, capability, cost, yield, or schedule claims

## Conditions And Methods

- Use this card when a prompt needs conservative wording for panel branch choice or special edge-feature handling.
- Keep the wording at branch-review level:
  - `V-cut` for straight or explicitly supported panel split branch language
  - `stamp-hole / mouse-bite` as an alternative connection or breakaway branch
  - `castellated / half-hole` as special edge-feature identity that deserves explicit design-input and fabrication review
- Pair this card with existing depanelization or half-hole boundary pages when the prompt also discusses edge damage, debris, mask-opening review, or downstream handling.

## Safe Blog Usage

- Explain that panelization branch choice should be explicit rather than guessed from ordinary-board defaults.
- Explain that `V-cut` and stamp-hole or mouse-bite language may be used as route-choice vocabulary, not as universal design-rule closure.
- Explain that castellated or half-hole edges belong to a special-feature review family with explicit design-input handling.

## Limits And Non-Claims

- This card does not authorize any universal stamp-hole or bridge numeric table.
- It does not authorize one universal rule that irregular boards must use one branch.
- It does not authorize process-order, plating-sequence, or post-HASL drilling doctrine.
- It does not authorize any customer-acceptance, supplier-capability, cost, yield, or schedule claim.

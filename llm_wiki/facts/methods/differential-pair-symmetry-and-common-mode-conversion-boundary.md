---
fact_id: "methods-differential-pair-symmetry-and-common-mode-conversion-boundary"
title: "Differential-pair guidance may be reused only as a symmetry, balance-through-discontinuity, and common-mode-conversion-risk boundary"
topic: "Differential pair symmetry and common-mode conversion boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "owner_scoped_differential_pair_symmetry_balance_and_common_mode_conversion_risk_boundary"
canonical_unit_policy: "Preserve wording such as pair members staying parallel, matched in length, and balanced through discontinuities; unavoidable asymmetry kept short and localized; mismatch or asymmetry increasing common-mode noise or common-mode current; and differential-to-common-mode conversion risk. Do not normalize this into universal skew budgets, exact impedance numbers, exact via or spacing recipes, or EMC-pass guarantees."
source_ids:
  - "ti-tm4c-differential-pair-symmetry-and-common-mode-noise"
  - "microchip-vsc7420-differential-pair-mismatch-and-common-mode-current"
  - "microchip-polarfire-differential-length-asymmetry-mode-conversion"
tags: ["differential-pair", "symmetry", "parallel", "length-match", "balance", "common-mode-noise", "common-mode-current", "mode-conversion", "emi", "methods"]
---

# Canonical Summary

> Current public semiconductor-owner guidance is strong enough to support one narrow differential-pair EMC boundary: pair members should remain parallel, matched, and balanced through localized discontinuities so differential routing does not drift into common-mode noise, common-mode current, or differential-to-common-mode conversion behavior. This supports guarded layout-review wording only. It does not authorize universal skew numbers, exact spacing or via recipes, or EMC-pass guarantees.

## Stable Facts

- TI supports keeping differential-pair members parallel and matched in length.
- TI supports keeping unavoidable non-parallel or disturbed sections short and localized when connectors or protection parts interrupt the ideal run.
- TI supports the boundary that pair imbalance increases common-mode noise and EMI.
- Microchip supports keeping differential-pair members identical in electrical length and minimizing vias or stubs in this pair-integrity context.
- Microchip supports the boundary that mismatched differential-pair members create common-mode current and that reducing mismatch reduces that current.
- Microchip also identifies common-mode current as a primary EMI source in this checklist context.
- Microchip PolarFire guidance supports the boundary that intra-pair asymmetry can convert differential behavior into common-mode behavior.

## Exact Data Scope

- exact for:
  - pair members running parallel and matched in length
  - preserving conductor-to-conductor balance through localized discontinuities
  - keeping unavoidable asymmetry short and localized
  - mismatch or asymmetry as a common-mode noise or common-mode current risk
  - differential-to-common-mode conversion risk from pair asymmetry
- not exact for:
  - universal skew budgets or cross-interface numeric mismatch limits
  - exact impedance targets such as `90 ohm`, `100 ohm`, or `120 ohm` as universal doctrine
  - exact spacing, coupling, meander, via, backdrill, or stitching recipes
  - claims that tighter coupling is always better in every stackup or interface context
  - SI, jitter, BER, EMC-pass, or compliance-signoff outcomes

## Conditions And Methods

- Use this card when a prompt needs safe wording for `differential symmetry`, `pair balance`, `common-mode conversion risk`, or `pair imbalance as an EMI risk`.
- Keep the language at boundary level:
  - pair members should stay parallel and matched
  - preserve pair balance through discontinuities
  - keep unavoidable asymmetry short and localized
  - reduce mismatch so differential behavior does not drift into common-mode current or common-mode noise
- Pair this card with `methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity` only when the draft separately needs generic return-path or plane-continuity wording.
- Pair this card with `methods-via-transition-return-path-continuity-boundary` only when the draft separately needs layer-change and nearby-return-via cleanup language.

## Safe Blog Usage

- Explain that differential routing quality is not only an impedance or length-budget topic, but also a balance-through-discontinuity topic.
- Explain that pair asymmetry can convert part of the intended differential behavior into common-mode behavior, which is why imbalance is also an EMC risk surface.
- Explain that unavoidable connector-side or protection-side disturbance should stay short and localized rather than spreading imbalance across a long route.
- Explain that this lane supports guarded pair-balance review wording, not a universal numeric routing recipe.

## Limits And Non-Claims

- This card does not authorize universal skew budgets or exact interface-specific mismatch numbers.
- It does not authorize exact spacing, via, or meander geometries.
- It does not authorize universal `100 ohm differential` doctrine across all interfaces.
- It does not authorize claims that any specific layout will pass EMI, EMC, eye, jitter, or BER validation by itself.

## Source Links

- https://www.ti.com/lit/an/spma056/spma056.pdf
- https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DesignChecklist/VSC7420-1-2-Hardware-Design-Checklist-DS00005256.pdf
- https://onlinedocs.microchip.com/oxy/GUID-ABAC3251-8552-4A5C-A63D-D9BCAEA91FEF-en-US-2/GUID-9E991AE0-B5D2-452E-9AD3-A73224AEEC25.html

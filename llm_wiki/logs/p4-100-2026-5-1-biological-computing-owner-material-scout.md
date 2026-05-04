Date: 2026-05-01
Lane: `P4-100 authority-scout`
Input: `tmps/2026.4.29/en/biological-computing-pcb.md`, `logs/p4-97-2026-5-1-biological-computing-regulated-biointerface-split.md`
Output: `logs/p4-100-2026-5-1-biological-computing-owner-material-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `generic_rewrite_may_leave_too_little_value`

# Purpose

Determine which `biological-computing` owner, platform, product, material, passivation, and wet-zone nouns should be stripped entirely if a generic rewrite is acceptable, and which would need separate owner or material authority only if publication insists on keeping them.

# Inputs Reviewed

- `tmps/2026.4.29/en/biological-computing-pcb.md`
- `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
- `logs/p4-97-2026-5-1-biological-computing-regulated-biointerface-split.md`

# Strip Entirely If Generic Rewrite Is Acceptable

- named owner, platform, and product nouns currently carrying evidentiary weight:
  `Neuralink`, `Blackrock Microsystems`, `Emulate`, `TissUse`, `Cortical Labs`
- `HILPCB` life-science, medical-device, or biocompatibility-validation program framing
- named product or platform classes tied to those owners:
  implantable neural interface arrays, organ-on-chip platforms, bio-hybrid processors, owner-specific neural-interface or organ-on-chip examples

# Need Separate Owner Or Material Authority If Kept

- owner-platform authority needed for:
  any named company-to-application linkage above, any architecture or validation implications attached to those owners, and any supplier-readiness or proven-program wording for biological-interface production
- material or regulator authority needed for:
  `Parylene C`, `SU-8`, `SiO2`, `PDMS`, glass-bonded microfluidic channels, gold, `ENIG`, electrolytic gold, platinum, `SAC305`, halogen-free laminates, high-`Tg` laminates, conformal coating, biopassivation, insulation, barrier coating
- wet-zone and passivation framing needing separate support:
  wet-zone, wet-dry boundary, saline-contact, exposed-electrode, corrosion-resistance, sterilization-compatibility framing
- these nouns are proof-bearing when used to imply:
  biological-interface suitability, biocompatibility, implantable or patient-contact readiness, saline endurance, cell-culture compatibility, or sterilization compatibility

# Generic Context That Can Survive Without Owner Or Material Proof

- biological computing as a high-level application context
- boards facing stricter contamination-control, access-planning, and documentation-review pressure
- dense interconnect review
- mixed-signal partitioning
- connector, fixture, or harness planning
- selective protection planning
- traceability posture
- inspection, validation, and handoff workflow boundaries
- life-science or medical context only as documentation-discipline pressure, not compliance or suitability proof

# Controller Recommendation

Run a strict generic rewrite only if it is reduced to manufacturing-control and packaging-pressure vocabulary. Strip all owner nouns, regulated biointerface framing, material-suitability framing, and wet-zone or passivation proof language unless separate owner or material authority is recovered. If little value remains after that strip, keep the draft on hold.

# Status

- `biological-computing-pcb.md`: `hold_preferred_unless_generic_scope_still_has_value`
- owner_or_material_recovery_priority: `defer_unless_exact_nouns_are_required`

Date: 2026-05-01
Lane: `P4-98 controller integration`
Input: `logs/p4-95-2026-5-1-audio-conservative-rewrite-and-dna-biological-hold-integration.md`, `logs/p4-96-2026-5-1-dna-computing-regulator-and-standards-split.md`, `logs/p4-97-2026-5-1-biological-computing-regulated-biointerface-split.md`
Output: `logs/p4-98-2026-5-1-dna-biological-split-lane-controller-integration.md`
Scope status: `controller_integrated`
Evidence status: `hold_state_refined_not_released`

# Purpose

Controller-integrate the first two post-`P4-95` authority-recovery micro-lanes for the blocked `dna-computing` and `biological-computing` drafts, without advancing either draft into conservative rewrite consumption.

# Integrated Scout Results

## `dna-computing`

- `P4-96` confirms that only documentation and manufacturing-control vocabulary is currently reusable
- regulator and standards names may remain only if reduced to documentation-role boundaries rather than compliance, safety, diagnostics, or market-readiness proof
- named sequencing or genomics platforms remain blocked pending a separate owner-platform authority lane

## `biological-computing`

- `P4-97` confirms that only manufacturing-control and packaging-pressure vocabulary is currently reusable
- all wet-zone, implantable, patient-contact, biocompatibility, sterilization, exposed-electrode, and material-suitability language remains blocked pending narrower regulator, material, and biointerface authority
- named neural-interface, organ-on-chip, and bio-hybrid platform references remain blocked pending a separate owner-platform authority lane

# Controller Disposition

Neither draft is eligible for conservative rewrite consumption yet.

Current hold remains:

- `dna-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`
- `biological-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`

The active continuation state now has clearer strip boundaries:

- `dna-computing` may keep only documentation-control vocabulary unless a narrower authority lane is landed
- `biological-computing` may keep only packaging-pressure and manufacturing-control vocabulary unless a narrower authority lane is landed

# Next Micro-Lanes

1. `dna-computing` owner-platform scout if exact sequencing, synthesis, nanopore, fluorescence, or compute-platform nouns must remain
2. `biological-computing` owner-platform and material scout if exact neural-interface, organ-on-chip, passivation, or wet-zone material nouns must remain
3. HILPCB capability decision lane for life-science or medical supplier-proof language
4. conservative-rewrite eligibility recheck only after those narrower lanes land or are intentionally stripped from scope

# Status

- active continuation state: `owner_material_capability_decision_pending`
- tracker state: `ready_for_p4_98_update`

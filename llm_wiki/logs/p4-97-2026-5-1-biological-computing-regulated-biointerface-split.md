Date: 2026-05-01
Lane: `P4-97 authority-split scout`
Input: `tmps/2026.4.29/en/biological-computing-pcb.md`, `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
Output: `logs/p4-97-2026-5-1-biological-computing-regulated-biointerface-split.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `blocked_pending_narrower_regulator_material_biointerface_and_owner_authority`

# Purpose

Separate the `biological-computing` draft into what can remain only as manufacturing-control or packaging-pressure vocabulary versus what still depends on narrower regulator, material, biointerface, or owner-platform authority.

# Inputs Reviewed

- `tmps/2026.4.29/en/biological-computing-pcb.md`
- `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
- `facts/methods/conformal-coating-medical-regulated-boundary.md`
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md`

# Safe To Keep Only As Manufacturing-Control Or Packaging-Pressure Vocabulary

- `biological-computing` only as high-level application context that increases packaging pressure, contamination-control review, access planning, inspection handoff, and documentation discipline
- board-level workflow language such as dense interconnect review, mixed-signal partitioning, connector or fixture planning, selective protection planning, traceability posture, lot or build-record linkage, and validation-handoff boundaries
- `medical` or `life-science` context only as adjacent explanation for stricter documentation and review, not as compliance or suitability proof

# Must Be Stripped Unless Narrower Regulator, Material, Or Biointerface Authority Is Recovered

- all biocompatibility, sterilization, patient-contact, implantable, wet-zone, saline-exposure, cell-culture, or exposed-electrode suitability claim families
- all regulator or standards claim families tied to `ISO 10993`, `ISO 13485`, `FDA 510(k)`, `IEC 60601`, or similar medical-device framing
- all material-suitability claim families for passivation, coating, insulation, barrier, or corrosion-resistance materials when framed as safe or suitable for biological interface use
- all biointerface method and performance claim families around electrophysiology, stimulation, microelectrode arrays, organ-on-chip integration, fluid-contact operation, leakage control, corrosion endurance, or biological-signal handling
- all numeric process, spacing, noise, current, soak, thermal, or registration claims

# Must Be Stripped Unless Separate Owner Or Platform Authority Is Recovered

- named company, platform, or product examples used as evidence for the lane, including neural-interface, organ-on-chip, and bio-hybrid platform references
- any architecture claims that imply how those platforms are built, partitioned, sensed, driven, or validated
- any HILPCB capability or program-readiness claim family suggesting proven life-science, medical-device, or biological-interface production support

# Controller Recommendation

Run the lane as a strict split: salvage only manufacturing-control and packaging-pressure vocabulary, and strip everything that depends on regulated biointerface, material suitability, or owner-platform proof. If public rewrite value still remains after that strip, test a narrow board-workflow article; otherwise hold the draft until separate regulator, material, biointerface, and owner-platform authority is recovered.

# Status

- `biological-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`
- next lane enabled: `owner_platform_and_material_scout_if_exact_nouns_must_remain`

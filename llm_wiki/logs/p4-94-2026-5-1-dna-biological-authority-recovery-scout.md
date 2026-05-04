Date: 2026-05-01
Lane: `P4-94 authority-recovery scout`
Input: `/code/blogs/tmps/2026.4.29/en/dna-computing-pcb.md`, `/code/blogs/tmps/2026.4.29/en/biological-computing-pcb.md`
Output: `/code/blogs/llm_wiki/logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `blocked_pending_narrower_authority`

# Purpose

Record why the `dna-computing` and `biological-computing` drafts should remain blocked for rewrite right now, identify what existing `llm_wiki` medical-manufacturing and adjacent governance can already support at claim-family level, and define the narrow next authority-recovery lanes for the controller.

This is a blocker and authority-planning note only. It does not recover sources and it does not authorize draft rewriting.

# Inputs Reviewed

- `logs/phase-status.md`
- `logs/backlog.md`
- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `logs/p4-93-2026-4-29-conservative-rewrite-consumption-batch-4.md`
- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
- `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md`
- `facts/methods/conformal-coating-medical-regulated-boundary.md`
- `logs/p4-42-2026-1-13-keyboard-mouse-hmi-audio-official-source-recovery-scout.md`
- `logs/p4-30-hilpcb-blog1-13-lane-a-keyboard-general.md`
- `logs/p4-30-hilpcb-blog1-13-lane-b-industrial-rugged-hmi.md`
- `logs/p4-30-hilpcb-blog1-13-lane-d-music-midi-audio.md`
- local grep cross-checks for `sequencing`, `bioelectronic`, `implantable`, `organ-on-chip`, `ISO 10993`, `510(k)`, `IVDR`, `MDR`, `IEC 60601`, `IEC 61010`, `Parylene`, `microfluidic`, and `electrophoresis`
- `tmps/2026.4.29/en/dna-computing-pcb.md`
- `tmps/2026.4.29/en/biological-computing-pcb.md`

# Controller Finding

`phase-status`, `backlog`, `P4-83`, and `P4-93` already converge on the same disposition: these two drafts are deletion-safe at claim-family level, but they are not conservative-rewrite ready and should not move forward without narrower owner, regulator, or standards authority recovery.

The current `llm_wiki` medical boundary is intentionally limited to manufacturing-control, traceability, documentation-aware workflow, coating or access-planning language, and blocked-claim containment. That boundary was sufficient for the `endoscope` rewrite because the draft could be stripped back to packaging, inspection, and documentation-aware board-review posture. It is not sufficient here because both drafts are built around claim families that inherently depend on owner-specific instrument architecture, regulator-scoped language, biocompatibility or implantability implications, and exact performance or process numerics.

# Per-Draft Blocker Classes

## `dna-computing-pcb.md`

Status: `blocked_pending_narrower_authority`

Blocker classes:

- `blocked_pending_owner_platform_authority`
  - named platform and product claims around `Illumina NovaSeq X`, `Oxford Nanopore PromethION`, `PacBio Revio`, `Ultima Genomics`, `Element Biosciences`, and `Singular Genomics`
  - named architecture claims around base-calling, sensor choice, host-streaming posture, and platform-specific board partitioning
- `blocked_pending_regulator_and_standards_authority`
  - `FDA 21 CFR 820`, `IVDR`, `MDR`, `IPC-6012 Class 3`, and design-history / device-master / device-history wording used as board-readiness or supplier-proof language
  - `IEC 61010-1` high-voltage safety phrasing for electrophoresis
- `blocked_pending_process_and_method_authority`
  - sequencing, synthesis, PCR, isothermal amplification, fluorescence detection, nanopore digitization, and electrophoresis claims framed as if the current evidence layer proves instrument execution
- `blocked_pending_numeric_performance_authority`
  - exact thermal-cycle temperatures, ramp rates, sensing precision, optical sensitivity, fluid volumes, data-volume throughput, ADC performance, FPGA pin-count, host-interface throughput, and thermal-load numerics
- `blocked_pending_hilpcb_capability_record`
  - HILPCB genomics, diagnostics, or life-science program claims; validated manufacturing support; traceability scope; and regulated-production posture

## `biological-computing-pcb.md`

Status: `blocked_pending_narrower_authority`

Blocker classes:

- `blocked_pending_owner_platform_authority`
  - named company and product claims around `Neuralink`, `Blackrock Microsystems`, `Emulate`, `TissUse`, and `Cortical Labs`
  - neural-interface, organ-on-chip, and bio-hybrid processor framing presented as direct board-program evidence
- `blocked_pending_regulator_and_material_authority`
  - `ISO 10993-5`, `ISO 13485`, `FDA 510(k)`, `IEC 60601`, implantable, patient-contact, and medical-grade language
  - biocompatibility, sterilization compatibility, and clean-manufacturing claims beyond the current medical-manufacturing-control boundary
- `blocked_pending_biointerface_method_authority`
  - wet-dry boundary engineering, exposed-electrode protection, passivation-material suitability, saline-exposure endurance, cell-culture compatibility, and organ-on-chip integration claims
  - microelectrode-array, biopotential, and stimulation-path claims that require owner or domain-primary authority
- `blocked_pending_numeric_performance_authority`
  - noise-floor, signal-level, current, spacing, registration, soak-test, trace-width, layer-count, and thermal-uniformity numerics
- `blocked_pending_hilpcb_capability_record`
  - HILPCB life-science, research-instrument, biocompatibility-validation, and medical-device production claims

# What Can Already Be Reused At Claim-Family Level

The following can already be reused, but only as conservative claim-family containment rather than draft-consumption authority:

- medical or wearable language as packaging pressure, documentation sensitivity, and review-discipline context only
- manufacturing-control framing around traceability, `DMR`, `DHR`, `UDI`, inspection handoff, functional-validation handoff, and release-flow role boundaries
- conformal-coating and protection-workflow language only at masking, keep-access, contamination, moisture, and inspection-handoff scope
- mixed-technology, THT-retention, dense-assembly, hidden-joint inspection, first-article, and documentation-aware build-flow nouns
- generic multi-board partitioning, connector or harness handoff, DFM / DFT / DFA sequencing, and process-review language
- the adjacent governance pattern already seen in keyboard, HMI, and audio lanes:
  treat drafts as claim inventory, allow only context and workflow nouns, and block product-performance, compliance-proof, protocol or interface proof, and supplier-capability claims until narrower authority exists

# Exact Claim Families Still Requiring Narrower Authority

## `dna-computing-pcb.md`

- platform-owner authority for named sequencer, nanopore, synthesis, and genomics-instrument examples
- regulator-scoped device and diagnostics authority for `FDA 21 CFR 820`, `IVDR`, `MDR`, and related documentation-role language if it must remain public-facing
- standards-owner authority for `IEC 61010-1` if electrophoresis high-voltage safety language is retained
- method authority for PCR thermal cycling, isothermal amplification, fluorescence detection, nanopore acquisition, and electrophoresis board-role descriptions
- owner or standards authority for host-interface and compute claims such as `PCIe Gen 5`, `100GbE`, `DDR5`, `HBM`, and exact FPGA family examples if any remain
- narrower owner or dated internal authority for HILPCB genomics / diagnostics manufacturing-support claims

## `biological-computing-pcb.md`

- owner authority for named neural-interface, organ-on-chip, and bio-hybrid platform examples
- regulator or standards authority for `ISO 10993-5`, `ISO 13485`, `FDA 510(k)`, `IEC 60601`, and any implantable, patient-contact, or medical-grade phrasing
- material-owner or regulator authority for `Parylene C`, `SU-8`, `SiO2`, exposed-electrode passivation, sterilization, and biocompatibility suitability claims
- domain-primary authority for microelectrode arrays, electrophysiology recording, stimulation-current routing, wet-zone leakage spacing, and saline-soak endurance claims
- narrower owner or dated internal authority for HILPCB life-science, biocompatibility-validation, or medical-device-production claims

# Recommended Next Micro-Lanes

Strict priority order:

1. `dna-computing` regulator and standards split
   - separate diagnostics-documentation vocabulary from instrument-performance claims
   - decide whether `FDA 21 CFR 820`, `IVDR`, `MDR`, and `IEC 61010-1` are genuinely needed in public rewrite scope
2. `biological-computing` regulated-biointerface split
   - separate manufacturing-control language from implantable, patient-contact, biocompatibility, sterilization, and `ISO 10993` / `IEC 60601` / `510(k)` language
3. `dna-computing` owner-platform scout
   - recover only enough owner authority to bound named sequencing, synthesis, nanopore, and fluorescence-detection examples if those nouns must remain
4. `biological-computing` owner-platform and material scout
   - recover only enough owner authority for named neural-interface / organ-on-chip examples and for passivation-material suitability vocabulary if required
5. HILPCB capability decision lane
   - either strip all life-science / medical supplier-proof language from both drafts or recover dated internal capability records before any public manufacturing-readiness wording is retained
6. conservative-rewrite eligibility recheck
   - only after the above lanes land should the controller test whether either draft can be reduced to a narrow board-review article without unsupported numerics or regulated-proof language

# Explicit Consumption Instruction

These two drafts should not enter conservative rewrite consumption yet.

Do not route `tmps/2026.4.29/en/dna-computing-pcb.md` or `tmps/2026.4.29/en/biological-computing-pcb.md` into the same consumption path used for `endoscope`, `gaming`, `smart-meter`, `ev-charger`, `hearing-aid`, `satellite`, `neuromorphic`, `inverter`, `lidar`, or `fpga`.

Current disposition:

- `dna-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`
- `biological-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`

They remain deletion-safe at claim-family level only.

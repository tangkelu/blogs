Date: 2026-05-01
Lane: `P4-101 capability-decision scout`
Input: `tmps/2026.4.29/en/dna-computing-pcb.md`, `tmps/2026.4.29/en/biological-computing-pcb.md`, `logs/p4-98-2026-5-1-dna-biological-split-lane-controller-integration.md`
Output: `logs/p4-101-2026-5-1-hilpcb-life-science-capability-decision.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `default_strip_decision`

# Purpose

Decide whether current local evidence supports keeping any HILPCB-specific life-science, diagnostics, medical-device, neural-interface, or bioelectronic manufacturing-readiness language in public rewrite scope for the blocked `dna-computing` and `biological-computing` drafts.

# Inputs Reviewed

- `tmps/2026.4.29/en/dna-computing-pcb.md`
- `tmps/2026.4.29/en/biological-computing-pcb.md`
- `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
- `logs/p4-98-2026-5-1-dna-biological-split-lane-controller-integration.md`
- `facts/methods/medical-manufacturing-control-context-for-coating-tht-and-bga.md`
- `facts/methods/pcba-mes-traceability-and-medical-documentation-boundary.md`
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md`
- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`

# Supported HILPCB-Specific Capability Language, If Any

Current local evidence supports only narrow HILPCB manufacturing-control language, not life-science readiness language:

- HILPCB may be referenced generically as a PCB or PCBA supplier with assembly workflow nouns such as `small-batch assembly`, `turnkey assembly`, `large-volume assembly`, BOM or source control, MES or traceability context, inspection linkage, and build-record discipline
- in medical or life-science context, HILPCB wording may stay only at adjacent documentation and review posture level:
  `medical`, `diagnostics`, `wearable`, or `life-science` as scenario context that increases documentation sensitivity, traceability posture, inspection handoff, contamination or protection planning, and packaging-review discipline

# Unsupported HILPCB-Specific Capability Language That Should Be Stripped Now

Strip all HILPCB-specific public language implying proven readiness, qualification, or validated support for:

- life-science, genomics, sequencing, synthesis, diagnostics, or clinical-instrument manufacturing readiness
- medical-device, regulated-diagnostics, `IVDR`, `MDR`, `FDA`, `510(k)`, `IEC 60601`, `IEC 61010`, `ISO 10993`, or `ISO 13485` readiness or proof
- neural-interface, bioelectronic, implantable, patient-contact, wet-zone, saline-exposure, organ-on-chip, microelectrode-array, electrophysiology, or biocompatibility production support
- HILPCB life-science team, medical-device production, biocompatibility-validation coordination, regulated traceability scope, or supplier release authority
- any HILPCB claim that suggests validated manufacturing support for DNA platforms, biological interfaces, diagnostics devices, or bioelectronic systems

# Recommended Default Controller Decision

Strip.

Current local evidence does not clearly support keeping any HILPCB-specific life-science, diagnostics, medical-device, neural-interface, or bioelectronic manufacturing-readiness language in public rewrite scope. The local record set is a boundary and governance layer, not a dated HILPCB capability pack. If any of that language must be retained later, recover dated internal capability records first.

# Status

- HILPCB capability decision: `strip_until_dated_internal_records_exist`

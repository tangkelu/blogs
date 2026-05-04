Date: 2026-05-01
Lane: `P4-96 authority-split scout`
Input: `tmps/2026.4.29/en/dna-computing-pcb.md`, `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
Output: `logs/p4-96-2026-5-1-dna-computing-regulator-and-standards-split.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `blocked_pending_narrower_regulator_standards_and_owner_authority`

# Purpose

Separate the `dna-computing` draft into what can remain only as documentation or manufacturing-control vocabulary versus what still depends on narrower regulator, standards, or owner-platform authority.

# Inputs Reviewed

- `tmps/2026.4.29/en/dna-computing-pcb.md`
- `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md`

# Safe To Keep Only As Documentation Or Manufacturing-Control Vocabulary

- regulated-program context only as documentation pressure, review discipline, build-record linkage, and release-workflow inputs
- `DMR`, `DHR`, `UDI`, `MES`, lot history, traveler linkage, source control, and traceability only as adjacent vocabulary explaining stricter records
- standards or regulation references only if reduced to role-boundary language about documentation and control posture rather than product readiness
- generic manufacturing-control nouns such as change control, inspection handoff, build packet discipline, and record visibility

# Must Be Stripped Unless Narrower Regulator Or Standards Authority Is Recovered

- any public-facing use of `FDA 21 CFR 820`, `IVDR`, `MDR`, or `IEC 61010-1` that implies compliance standing, diagnostics applicability, safety proof, or regulated manufacturing readiness
- any design-history, device-master, device-history, traceability, or standards wording presented as supplier qualification, release authority, or finished-device record ownership
- any regulator or standards framing attached to high-voltage, diagnostics, clinical, or medical-device operation rather than documentation boundary
- any claim family that turns standards names into proof of acceptance criteria, audit readiness, certification, or market access

# Must Be Stripped Unless Separate Owner Or Platform Authority Is Recovered

- named platform, OEM, or product references used as evidence for architecture, board partitioning, sequencing workflow, sensing approach, compute role, or host-interface role
- any owner-linked framing that suggests how specific commercial sequencing or genomics platforms are implemented
- any company or platform examples used to validate public rewrite scope beyond generic application context
- any implied supplier-to-platform relationship or support posture

# Controller Recommendation

Run a narrow regulator-and-standards split that keeps only documentation-boundary vocabulary and removes all compliance-proof or safety-proof uses. Then decide whether named platform examples are needed at all; if yes, open a separate owner-platform authority lane, and if no, strip them completely.

# Status

- `dna-computing-pcb.md`: `hold_for_narrower_owner_regulator_standards_authority`
- next lane enabled: `owner_platform_scout_if_exact_nouns_must_remain`

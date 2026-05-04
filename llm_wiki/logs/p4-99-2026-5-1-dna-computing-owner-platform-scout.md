Date: 2026-05-01
Lane: `P4-99 authority-scout`
Input: `tmps/2026.4.29/en/dna-computing-pcb.md`, `logs/p4-96-2026-5-1-dna-computing-regulator-and-standards-split.md`
Output: `logs/p4-99-2026-5-1-dna-computing-owner-platform-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `generic_rewrite_preferred_over_owner_recovery`

# Purpose

Determine which `dna-computing` owner, platform, product, and platform-tied method nouns should be stripped entirely if a generic rewrite is acceptable, and which would require a dedicated owner-platform authority lane only if publication insists on keeping them.

# Inputs Reviewed

- `tmps/2026.4.29/en/dna-computing-pcb.md`
- `logs/p4-94-2026-5-1-dna-biological-authority-recovery-scout.md`
- `logs/p4-96-2026-5-1-dna-computing-regulator-and-standards-split.md`

# Strip Entirely If Generic Rewrite Is Acceptable

- `Illumina NovaSeq X`
- `Oxford Nanopore PromethION`
- `PacBio Revio`
- `Ultima Genomics`
- `Element Biosciences`
- `Singular Genomics`
- named compute and component families used as evidence:
  `Xilinx Versal`, `Intel Agilex`, `DDR5`, `HBM`, `PCIe Gen 5`, `100GbE`
- named regulatory and standards nouns used as proof-bearing evidence:
  `FDA 21 CFR 820`, `IVDR`, `MDR`, `IEC 61010-1`, `IPC-6012 Class 3`
- named record-system nouns if framed as supplier-proof rather than documentation context:
  `DMR`, `DHR`, `UDI`, `MES`
- any HILPCB life-science, diagnostics, or regulated-production authority phrasing

# Would Need A Separate Owner-Platform Authority Lane If Kept

- sequencer or genomics platform owner lane:
  `Illumina`, `Oxford Nanopore`, `PacBio`, `Ultima Genomics`, `Element Biosciences`, `Singular Genomics`
- product or platform architecture lane:
  `NovaSeq X`, `PromethION`, `Revio`
- platform-tied method families when used as implementation evidence:
  sequencing-by-synthesis, nanopore acquisition, fluorescence-detection workflow, base-calling pipeline, host-streaming architecture
- productized compute-stack examples when tied to platform execution:
  FPGA-family examples, memory-family examples, high-speed host-interface examples

# Generic Application Context That Can Survive Without Owner Proof

- DNA instrument or genomics hardware as a broad application context
- multi-board partitioning as a generic design pattern
- thermal control, optical detection, fluidic control, and data-processing boards as generic subsystem nouns
- documentation pressure, traceability discipline, change control, inspection handoff, and build-record visibility as manufacturing-control context only
- generic lab, diagnostics, or research environment context, if it does not imply compliance standing, product readiness, or supplier qualification

# Controller Recommendation

Strip all named owner, platform, product, and regulator nouns unless publication explicitly requires them. If any exact noun must remain, open a separate owner-platform authority lane and keep the base rewrite limited to generic subsystem context plus documentation-boundary manufacturing-control language only.

# Status

- `dna-computing-pcb.md`: `generic_rewrite_preferred_if_scope_can_be_stripped`
- owner recovery priority: `defer_unless_exact_nouns_are_required`

# P4-215A2 EMC Lane A2: Ferrite Bead Vs Common-Mode Choke

Date: 2026-05-06
Lane: `A2`
Model requested: `gpt-5.4`

## Purpose

Capture the first exact-data candidate pass for the ferrite-bead / common-mode-choke handbook slice inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`

This lane preserves curve, topology, and component-family evidence with page/asset traceability while keeping handbook-only rules, universalized noise-suppression claims, and uncited selection logic blocked.

## Page Slice Covered

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- extracted text pages:
  - `page-0021.txt`
  - `page-0022.txt`
- source page numbers:
  - `21`
  - `22`
- reviewed image assets:
  - `images/5c6f3c7a1085e07d.png`
  - `images/16fc3b6eee649de6.png`
  - `images/23e253bab7705be9.png`
- manifest traceability verified from:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/manifest.json`

## `exact_data_candidate` Items

### `ferrite bead impedance frequency curve for a named part`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/5c6f3c7a1085e07d.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding inside the extracted image`
- short extraction:
  - `Figure 3-5` is a ferrite-bead impedance-versus-frequency plot labeled `BLA3216A102SG4` with curve labels `Z`, `R`, and `X`; this is a strong part-scoped exact-data candidate if the original Murata source is recovered.

### `common-mode choke impedance frequency curve with common-mode and differential-mode traces`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `22`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/16fc3b6eee649de6.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding inside the extracted image`
- short extraction:
  - `Figure 3-6` is an impedance-versus-frequency plot with separate `Common Mode` and `Differential Mode` traces; the figure is useful as an exact-data candidate only if the original vendor-scoped source is recovered.

## `structural_context_candidate` Items

### `ferrite bead versus common-mode choke noise-mode distinction`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - from text only, the handbook distinguishes ferrite bead use on a single signal or power path for `differential-mode noise` suppression versus common-mode choke use on a conductor pair for `common-mode high-frequency noise` suppression.

### `common-mode choke conductor-pair topology`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - from text only, the handbook describes two identical coils wound on the same ferrite core, with flux addition for common-mode current and flux cancellation for differential-mode current; preserve as topology/vocabulary context only.

### `low-pass filter topology family inventory`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - from text only, the handbook inventories `inductor`, `capacitor`, `Gamma`, `Pi`, and `T` low-pass filter forms as topology families for later source-backed recovery.

## `blocked_secondary_pdf_claim` Items

### `ferrite bead better high-frequency filtering than ordinary inductor claim`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/5c6f3c7a1085e07d.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding inside the extracted image`
- short extraction:
  - the handbook states that ferrite beads have better high-frequency filtering performance than ordinary inductors and maintain high impedance over a broad band; this remains a blocked secondary-PDF claim until the original vendor source is recovered.

### `ferrite bead low-quality-factor explanation as generalized rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook says ferrite behaves resistively at high frequency and is equivalent to a very low-Q inductor; keep as blocked claim inventory only until tied to a primary vendor explanation.

### `common-mode choke suppresses common-mode current while differential current passes without attenuation`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `21`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook states that common-mode current sees large inductance while differential current sees almost no inductance and can pass without attenuation; this remains blocked as a handbook-only universalized behavior claim.

### `low-pass filter topology selection by source and load impedance`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook assigns `inductor`, `capacitor`, `Gamma`, `Pi`, and `T` topologies to high-frequency source/load impedance cases; these cookbook selection rules remain blocked until stronger authority is recovered.

### `common-mode choke frequency-behavior figure without part family or test-condition provenance`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `22`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/16fc3b6eee649de6.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding inside the extracted image`
- short extraction:
  - the figure is introduced as a typical curve from `muRata`, but the extracted page does not provide a part number, DCR, current rating, winding family, or fixture context; exact interpretation remains blocked.

### `tiny repeated inductor-like icon is not a meaningful standalone learned asset`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `22`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/23e253bab7705be9.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding inside the extracted image`
- short extraction:
  - this extracted asset is only a tiny repeated icon-like inductor symbol fragment from the filter-topology figure; it is not technically meaningful as a standalone preserved asset and should not be treated as an independent figure/table candidate.

## Source-Mapping Recommendations

### `primary-source recovery for ferrite bead part-scoped impedance curve`

- target source families:
  - `Murata`
  - `TDK`
  - `Wurth Elektronik`
- short recommendation:
  - recover the original manufacturer document for the labeled bead `BLA3216A102SG4` or its exact family equivalent so the `Z`, `R`, and `X` curves can be classified as `part_scoped_exact_data` instead of handbook inventory.

### `primary-source recovery for common-mode choke impedance and mode distinction curves`

- target source families:
  - `Murata`
  - `TDK`
  - `Wurth Elektronik`
- short recommendation:
  - recover a manufacturer application note or datasheet that publishes both `common-mode` and `differential-mode` impedance traces for a named choke family, plus DCR and current-rating context if available.

### `primary-source recovery for component-family distinction wording`

- target source families:
  - `Murata`
  - `TDK`
  - `Wurth Elektronik`
  - `TI`
- short recommendation:
  - recover official technical notes that explain when ferrite beads are used on single conductors versus when common-mode chokes are used on paired conductors, while preserving vendor or method scope and avoiding universal rules.

### `primary-source recovery for low-pass topology selection context`

- target source families:
  - `TI`
  - `ADI`
  - `NXP`
  - component-vendor EMI filter application notes
- short recommendation:
  - recover method-scoped filter-topology guidance that ties topology choice to source/load impedance assumptions with explicit conditions, rather than copying the handbook's bare cookbook rules.

## Unresolved Items

### `missing full low-pass topology figure asset on page 22`

- short note:
  - page `22` text clearly references `Figure 3-7` low-pass filter forms, but the provided extracted assets include only the common-mode choke curve and a tiny repeated symbol fragment; no technically meaningful full topology figure asset is available in the reviewed local slice.

### `missing part identity and electrical metadata for the common-mode choke curve`

- short note:
  - `images/16fc3b6eee649de6.png` does not show a part number, DCR, rated current, or test setup; exact reuse cannot progress beyond candidate inventory without stronger provenance.

### `text gives noise-mode behavior but no current or DCR example rows`

- short note:
  - despite the workstream focus on `current / DCR / line-family examples`, pages `21-22` do not provide explicit current or DCR table rows in the extracted slice, so that subtarget remains unfulfilled for this lane.

### `handbook cites muRata generically but not enough for direct admission`

- short note:
  - both the ferrite-bead and common-mode-choke curves are introduced as typical Murata-sourced characteristics, but the handbook itself remains a secondary PDF and does not satisfy the authority gate.

## Lane Status

- lane output status:
  - `completed_at_candidate_inventory_level`
- exact-data admission status:
  - `secondary_pdf_claim_inventory_only`
- strongest recovery-ready items:
  - `ferrite bead impedance frequency curve for a named part`
  - `common-mode choke impedance frequency curve with common-mode and differential-mode traces`
- main policy result:
  - handbook-only component-performance and topology-selection rules remain blocked pending stronger primary-source recovery

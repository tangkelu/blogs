# P4-215A1 EMC Lane A1: Capacitor Figures And Parameter Tables

Date: 2026-05-06
Lane: `A1`
Model requested: `gpt-5.4`

## Purpose

Capture the first exact-data candidate pass for the capacitor-heavy handbook slice inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`

This lane preserves figure, curve, and table evidence with page/asset traceability while keeping handbook-only formulas, value recipes, and universalized EMC rules blocked.

## Page Slice Covered

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- extracted text pages:
  - `page-0019.txt`
  - `page-0020.txt`
  - `page-0025.txt`
  - `page-0026.txt`
  - `page-0027.txt`
  - `page-0028.txt`
- source page numbers:
  - `19`
  - `20`
  - `25`
  - `26`
  - `27`
  - `28`
- reviewed image assets:
  - `images/fff43815e9fd11d2.png`
  - `images/7672c07ea81b2c2b.png`
  - `images/8df41200d7fbd85d.png`
  - `images/1ae22269335fea8a.png`
  - `images/046ab5539d3ae95e.png`
  - `images/b904ebfcc1fcf680.png`
  - `images/606f1b70c24f6bb3.png`
  - `images/f4251a4931d0dd24.png`
  - `images/465f6624b2e3d8b5.png`

## `exact_data_candidate` Items

### `parallel capacitor antiresonance impedance curve`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `25`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/046ab5539d3ae95e.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-12` is an impedance-versus-frequency plot labeled with `22 nF`, `100 pF`, and `22 nF || 100 pF`; it is useful as a candidate method-scoped antiresonance example.

### `equivalent series inductance by capacitor package`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `26`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/b904ebfcc1fcf680.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Table 3-1` contains package/type-to-ESL rows, including values such as `3.0 nH`, `2.6 nH`, `1.6 nH`, `1.9 nH`, `0.7 nH`, `0.9 nH`, `6.8 nH`, and `3.4 nH`; this is a parameter-table candidate only.

### `capacitor insertion loss by package and capacitance`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `26`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/606f1b70c24f6bb3.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-13` compares insertion-loss curves over frequency for several capacitor technologies, values, and package examples.

### `parallel decoupling capacitor bandwidth extension curve`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `28`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/465f6624b2e3d8b5.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-15` shows impedance-versus-frequency curves labeled `10 nF`, `22 nF`, and `22 nF || 10 nF`; it is a candidate method example for multi-value decoupling behavior.

## `structural_context_candidate` Items

### `power-path inductance and local decoupling current path`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `19`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/fff43815e9fd11d2.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-1` shows a switching load, supply-path equivalent inductance, and local output capacitance; useful for current-path structure only.

### `supply switching transient waveform example`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `19`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/7672c07ea81b2c2b.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-2` is a waveform sketch for supply disturbance during output switching; preserve as structural context only.

### `filter capacitor application topology`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `19`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/8df41200d7fbd85d.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-3` visually shifts the transient-current path by adding a filter capacitor; preserve as topology context.

### `parasitic-aware high-frequency behavior of passive components`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `20`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/1ae22269335fea8a.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-4` compares low-frequency versus high-frequency behavior for conductor, resistor, capacitor, and inductor equivalent circuits.

### `decoupling capacitor placement topology around IC power pins`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `27`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/f4251a4931d0dd24.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - `Figure 3-14` shows capacitor, VCC-via, GND-via, and IC adjacency as a placement structure example.

## `blocked_secondary_pdf_claim` Items

### `supply inductance transient voltage formula fragment`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `19`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - OCR exposes only an incomplete formula fragment `ΔV = L`; it cannot be reconstructed or promoted from this handbook page.

### `parallel capacitor antiresonance frequency band claim`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `25`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/046ab5539d3ae95e.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - numeric claims around `15 MHz to 175 MHz` and a peak near `150 MHz` remain handbook-only and blocked.

### `parallel capacitor ESR rule set`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `25`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - handbook rules about lowering ESR, antiresonance behavior, and spreading capacitor values remain blocked secondary-PDF method claims.

### `small-ESL capacitor preference rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `26`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/b904ebfcc1fcf680.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the handbook conclusion that designers should choose smaller-ESL capacitors where possible remains blocked.

### `capacitor dielectric choice recommendation for EMI filters`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `26`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - dielectric-family recommendations such as `X7R`, `Y5V`, and `Z5U` remain blocked handbook guidance.

### `0.01 uF versus 0.1 uF high-frequency filtering recommendation`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `27`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/606f1b70c24f6bb3.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the recommendation to prefer `0.01 uF` over `0.1 uF` above `50 MHz` remains blocked.

### `22 nF decoupling self-resonance and impedance-band example`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `27`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - example values such as self-resonance near `11 MHz` and impedance below `1 ohm` from `6 MHz to 40 MHz` remain blocked.

### `per-power-pin decoupling placement recipe`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `27`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/f4251a4931d0dd24.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the cookbook rule to place at least one decoupling capacitor near each IC power pin remains blocked.

### `two-to-one parallel decoupling value ratio rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `28`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/465f6624b2e3d8b5.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the value-ratio recommendation near `2:1` remains blocked.

### `parallel decoupling impedance threshold and frequency-range claim`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `28`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/images/465f6624b2e3d8b5.png`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - numeric claims such as a peak below `1.5 ohm` and a usable range near `3.25 MHz to 100 MHz` remain blocked.

### `board-level and device-level storage capacitor value recipe`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- page number:
  - `28`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - storage-capacitor value ladders such as `1 uF`, `10 uF`, `22 uF`, and `33 uF` remain blocked handbook recipes.

## Source-Mapping Recommendations

- `primary-source recovery for capacitor package ESL tables`
  - likely source classes: `Murata`, `TDK`, `KEMET`, `AVX`, `Yageo`
- `primary-source recovery for capacitor impedance and antiresonance curves`
  - recover official capacitor-vendor technical notes or part-scoped impedance plots
- `primary-source recovery for capacitor insertion loss comparison curves`
  - recover named part- and fixture-scoped comparison figures from component vendors
- `primary-source recovery for decoupling placement and power-pin guidance`
  - recover IC-vendor layout notes from `ADI`, `TI`, or `NXP`
- `primary-source recovery for multi-value decoupling method examples`
  - recover application notes that explicitly scope such examples as method-specific

## Unresolved Items

- `missing authoritative provenance for handbook capacitor table rows`
  - `Table 3-1` does not expose its original source
- `missing test-condition metadata for handbook capacitor curves`
  - the reviewed figures do not identify fixture, part-number, DC-bias, or package-series context
- `unclear source scope for dielectric and storage-capacitor recommendations`
  - no named vendor, standard, or exact part family anchors the recommendations
- `incomplete OCR formula capture on transient-voltage page`
  - the formula on page `19` is truncated in text extraction
- `figure-to-text coupling exceeds current admission scope`
  - several figures depend on adjacent handbook prose for their numeric claims and remain inventory-only

## Lane Status

- lane execution:
  - `completed`
- promotion posture:
  - `candidate_inventory_only`
- next controller action:
  - merge into Round 1 integration and route narrower authority recovery only

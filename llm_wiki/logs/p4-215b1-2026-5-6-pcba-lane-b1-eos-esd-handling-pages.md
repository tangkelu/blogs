# P4-215B1 PCBA Lane B1: EOS / ESD / Handling Pages

Date: 2026-05-06
Lane: `B1`
Model requested: `gpt-5.4`

## Purpose

Capture the first exact-data candidate pass for the EOS / ESD / handling slice inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`

This lane separates high-value handling vocabulary, symbol assets, and example tables from blocked handbook thresholds and standards-equivalent inspection claims.

## Page Slice Covered

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- extracted text pages:
  - `page-0007.txt`
  - `page-0008.txt`
  - `page-0009.txt`
  - `page-0010.txt`
  - `page-0011.txt`
  - `page-0012.txt`
  - `page-0013.txt`
- source page numbers:
  - `7`
  - `8`
  - `9`
  - `10`
  - `11`
  - `12`
  - `13`

## `exact_data_candidate` Items

### `inspection magnification by pad width`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `7`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - a pad-width table lists `>0.5 mm -> 1.75X-4X / 10X`, `0.25-0.5 mm -> 10X / 20X`, and `<0.25 mm -> 20X / 30X`; preserve as candidate inventory only.

### `device-family EOS/ESD sensitivity ranges`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `8`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the table lists family ranges such as `VMOS 30~1800V`, `MOSFET 100~200V`, and `CMOS 250~3000V`.

### `ESD workbench resistance and discharge-time limits`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `10`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - a handbook table gives resistance limits around `1000 MΩ` plus discharge-time rows such as `<1 sec` and `<0.1 sec`.

## `structural_context_candidate` Items

### `minimum electrical spacing`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `7`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the page defines minimum spacing between conductors, conductive graphics, and conductive materials; keep as vocabulary only.

### `ESD warning and protection symbols`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `9`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/21847698245d64c1.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/8efef94d0f70554f.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - one symbol marks ESD-sensitive items; the other marks ESD-protective packaging or handling context.

### `ESD protective packaging`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `9`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - conductive bags, shielding bags, boxes, and protective paper are described as handling structures rather than fact-layer proof.

### `ESD-safe workbench grounding layout`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `11`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a53c51c299b52b94.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/f5f2ef8e68729c65.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - wrist strap, `1 MΩ` path, tabletop, floor mat, and common ground point form the safe-workbench structure.

### `PCBA handling and contamination prevention`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `12`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - keep the area clean, avoid bare-hand contact with soldered surfaces, avoid oily or silicone contamination, avoid stacking boards, and use trays or clean gloves.

### `manual board-handling examples`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `13`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/641c897f9028dd11.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/1477cc2d1cbd5e26.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/1ec41ff66a9a8c40.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - preserve these as local examples of gloved edge handling versus direct bare-hand contact.

## `blocked_secondary_pdf_claim` Items

### `EOS/ESD spike voltage threshold`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `8`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - handbook numeric thresholds such as `0.5V` and `0.3V` remain blocked pending stronger authority.

### `ESD compliance thresholds as pass/fail law`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `9-13`
- asset path:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/21847698245d64c1.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/8efef94d0f70554f.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a53c51c299b52b94.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/f5f2ef8e68729c65.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/641c897f9028dd11.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/1477cc2d1cbd5e26.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/1ec41ff66a9a8c40.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the images are useful locally, but they cannot be treated as standards-equivalent compliance proof.

### `anti-static packaging sufficiency claim`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- page number:
  - `9`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no visible branding`
- short extraction:
  - the packaging distinction is useful, but universal sufficiency claims remain blocked.

## Source-Mapping Recommendations

- map `inspection magnification by pad width` to official workmanship or microscope-use guidance before any exact-value reuse
- map `device-family EOS/ESD sensitivity ranges` to manufacturer datasheets or official ESD control references
- map `ESD workbench resistance and discharge-time limits` to `ANSI/ESD S20.20`, `IEC 61340-5-1`, or equivalent ESD-control documentation
- map handling and packaging posture to official ESD handling standards or manufacturer handling guides
- keep pages `9`, `11`, and `13` images as local technical references unless a stronger authority class is added

## Unresolved Items

- whether page `7` magnification values are handbook house guidance or match a stronger inspection source
- whether page `8` sensitivity ranges are generic illustrative rows or part-scoped family data
- whether page `10` resistance and discharge-time values are formal program limits or only handbook examples
- whether any page `13` handling photo needs a neutral crop before later reuse
- no branding contamination was visible in the reviewed assets, but later downstream reuse should still verify crop cleanliness

## Lane Status

- lane execution:
  - `completed`
- promotion posture:
  - `candidate_inventory_only`
- next controller action:
  - merge into Round 1 integration and route standards/ESD authority recovery separately

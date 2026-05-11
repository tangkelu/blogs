# P4-215C2 Package Lane C2: Pad / Origin / Pin-1 / Keepout Drawings

Date: 2026-05-06
Lane: `C2`
Execution mode: `controller-owned local integration`

## Purpose

Capture the first exact-data candidate pass for the package / footprint drawing slice inside:

- `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`

This lane focuses on pad and drill relationship examples, origin and pin-1 drawing rules, keepout and hole-table structures, and dimension-bearing footprint figures while blocking repeated branding shells and preventing handbook-only dimensions, compensation values, and keepout rules from being universalized without stronger authority.

## Page Slice Covered

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- extracted text pages:
  - `page-0022.txt`
  - `page-0023.txt`
  - `page-0024.txt`
  - `page-0025.txt`
  - `page-0026.txt`
  - `page-0027.txt`
  - `page-0028.txt`
  - `page-0029.txt`
  - `page-0030.txt`
- source page numbers:
  - `22-30`
- reviewed technical illustration assets:
  - page `23`: `images/e7a9dbb1a6b2cc01.jpeg`
  - page `24`: `images/2ac56be753b231b1.jpeg`
  - page `24`: `images/fc2bc4cebd9a59b4.jpeg`
  - page `25`: `images/27115c512626682d.jpeg`
  - page `25`: `images/ca3e19f65abe64d1.jpeg`
  - page `26`: `images/f2ac035e01f7946f.jpeg`
  - page `26`: `images/49fbee9ba092b1c6.jpeg`
  - page `27`: `images/0a66fb6fec403a2e.jpeg`
  - page `28`: `images/35a09507227a52b9.jpeg`
  - page `28`: `images/cb091987d7d2b074.jpeg`
- preserved but not fully decoded technical candidate assets:
  - page `24`: `images/7a4f80ef561d7dc9.jpeg`
  - page `24`: `images/db3d0dabc7959166.jpeg`
  - page `24`: `images/44fa8349499dfd2a.jpeg`
  - page `24`: `images/00a728ea52617e15.jpeg`
  - page `24`: `images/3ce92aec7aa8e55a.jpeg`
  - page `24`: `images/33a7e0b983cfc485.jpeg`
  - page `28`: `images/7dfd95a036f6d718.jpeg`
- blocked repeated branded shell assets:
  - `images/a6f0e9c264f123cd.jpeg`
  - `images/02577a0d9d1ef056.jpeg`
  - `images/125e25b5113131e0.jpeg`
  - `images/f913a00ca327b920.jpeg`
  - `images/a8c3a196df2348ac.jpeg`
  - `images/28aed815ea62462d.jpeg`

## `exact_data_candidate` Items

### `via padstack naming grammar`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - the handbook uses a tokenized naming example `VIA + pad diameter + - + hole diameter`, with `VIA16-8` given as an example that encodes pad diameter and finished hole size.

### `thermal pad or flash naming grammar`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - circular and rectangular `FLASH` examples encode outer and inner dimensions in the name string and are useful as local naming-grammar candidates for thermal-relief pad records.

### `irregular pad and shape naming grammar`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - `PAD-封装名称-管脚序号` and `SH-封装名称-管脚序号(-SM)` are clear exact naming examples for irregular pad records and shape records tied to package name plus pin number.

### `padstack layer-role vocabulary`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `23`
- asset path:
  - `images/e7a9dbb1a6b2cc01.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- short extraction:
  - the illustrated via padstack cleanly labels `SolderMask_Top`, `Pin>Top`, `Thermal Relief`, `Anti pad`, `Pin>Bottom`, `SolderMask_Bottom`, and `Drill (Plated)`.

### `smd pad relationship formulas`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `23`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - the text defines formula relationships among `Regular Pad`, `Solder Mask`, and `Paste Mask` for `regular` and `shape` SMD pad cases.

### `through-hole pad relationship formulas`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `23`
- asset path:
  - `images/e7a9dbb1a6b2cc01.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- short extraction:
  - the text defines formula relationships among `Drill Size`, `Regular Pad`, `Thermal Pad`, `Anti Pad`, and `Solder Mask` for through-hole pad construction.

### `pin compensation calculation rules`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `24`
- asset path:
  - `images/2ac56be753b231b1.jpeg`
  - `images/fc2bc4cebd9a59b4.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-regions separable`
- short extraction:
  - page `24` carries multiple explicit drill-compensation formulas for round, rectangular, square, and oval pin geometries and multiple drill-shape choices.

### `flash calculation rules`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `24`
- asset path:
  - `images/fc2bc4cebd9a59b4.jpeg`
  - `images/7a4f80ef561d7dc9.jpeg`
  - `images/db3d0dabc7959166.jpeg`
  - `images/44fa8349499dfd2a.jpeg`
  - `images/00a728ea52617e15.jpeg`
  - `images/3ce92aec7aa8e55a.jpeg`
  - `images/33a7e0b983cfc485.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-regions separable`
- short extraction:
  - page `24` defines parameterized `circular flash` and `oval flash` construction variables such as `a`, `b`, `c`, `d`, `A`, `B`, `C`, `D`, and `E`.

### `lead-compensation footprint equations`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `25`
  - `26`
  - `27`
- asset path:
  - `images/27115c512626682d.jpeg`
  - `images/ca3e19f65abe64d1.jpeg`
  - `images/f2ac035e01f7946f.jpeg`
  - `images/49fbee9ba092b1c6.jpeg`
  - `images/0a66fb6fec403a2e.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-regions separable`
- short extraction:
  - pages `25-27` provide variable-based footprint compensation equations for no-lead SMD, gull-wing SMD, flat-laying SMD, and J-lead SMD package families, using variables such as `A`, `T`, `W`, `X`, `Y`, and `S`.

### `bga pitch-to-pad-diameter table`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `28`
- asset path:
  - `images/cb091987d7d2b074.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- short extraction:
  - the page contains a compact table mapping `Pitch(mm)` to `pad diameter (mm)` `MIN/MAX`, with some rows showing a recommended value in parentheses.

### `silkscreen numeric rule table`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `29`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - the text contains exact numeric silkscreen rules for line width, expansion, and text-size combinations, plus minimum clearance wording tied to pad spacing.

### `pin-group marking rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `30`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - page `30` defines exact mark lengths for grouped pin-count marks on ICs with more than `64` leads.

### `keepout dimension rule`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `30`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - the page gives an explicit exact rule for non-plated-hole keepout size relative to hole diameter.

### `standard hole table`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `30`
- asset path:
  - `none`
- image understanding required:
  - `text table is partial only`
- branding contamination exists:
  - `no`
- short extraction:
  - the page begins `Table 1` for standard hole diameters with plated and non-plated symbol/size fields, but the extracted text is only partial and the image asset is not separately isolated in this slice.

## `structural_context_candidate` Items

### `package footprint element checklist`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - page `22` is strong structural context for what the handbook considers a full footprint record: board opening, dimensioning, chamfer, pad, solder mask, hole, thermal pad, anti pad, pin number, pitch, span, silkscreen, assembly line, no-route area, no-drill area, reference text, assembly text, pin-1 mark, installation mark, occupancy area, and height.

### `mandatory footprint fields`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - page `22` explicitly lists which footprint elements are considered mandatory, including pad, silkscreen, assembly line, reference designator text, pin-1 mark, installation mark, occupancy area, component maximum height, polarity mark, and origin.

### `padstack conceptual layering`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `23`
- asset path:
  - `images/e7a9dbb1a6b2cc01.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- short extraction:
  - the via cross-section and top view are valuable structural context for how plated drill, copper pad, thermal relief, anti pad, and soldermask interact across layers.

### `package-to-footprint variable mapping diagrams`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `25-27`
- asset path:
  - `images/27115c512626682d.jpeg`
  - `images/f2ac035e01f7946f.jpeg`
  - `images/49fbee9ba092b1c6.jpeg`
  - `images/0a66fb6fec403a2e.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-regions separable`
- short extraction:
  - these figures clearly map package geometry variables to PCB footprint variables and are strong local technical assets even if the exact compensation values remain blocked.

### `bga footprint array illustration`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `28`
- asset path:
  - `images/35a09507227a52b9.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- short extraction:
  - the BGA ball-array illustration is useful as structural context for array footprint layout even without exact dimensional promotion.

### `origin pin-1 polarity and installation-mark rule family`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `29-30`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - pages `29-30` provide strong structural context for pin-1 marking, positive-polarity marking, installation marking, origin placement, and connector-origin handling.

### `connector origin and pin-order rule family`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `30`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- short extraction:
  - page `30` is structurally useful for origin-at-geometric-center versus origin-at-pin-1 rule families and for the special treatment of connectors with and without locating holes.

## `blocked_secondary_pdf_claim` Items

### `secondary-pdf dimension and compensation rules`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `23-28`
- asset path:
  - multiple assets listed above
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-regions separable, but source class still secondary PDF`
- block reason:
  - all exact pad-size, drill-size, anti-pad, solder-mask, flash, and footprint-compensation equations remain blocked as universal rules until mapped to stronger part-scoped, method-scoped, or standard-scoped authority.

### `secondary-pdf bga pad-diameter table`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `28`
- asset path:
  - `images/cb091987d7d2b074.jpeg`
- image understanding required:
  - `yes`
- branding contamination exists:
  - `technical sub-region separable`
- block reason:
  - the table is a valuable local exact-data candidate, but it cannot become a universal BGA land-pattern rule without stronger owner or standards authority.

### `secondary-pdf silkscreen and keepout numeric rules`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `29-30`
- asset path:
  - `none`
- image understanding required:
  - `no`
- branding contamination exists:
  - `no`
- block reason:
  - line widths, text-size tables, clearance numbers, pin-group mark lengths, and keepout offsets are handbook-only exact rules and cannot be promoted as standards truth from this source alone.

### `partial or weakly recovered standard hole table`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `30`
- asset path:
  - `none`
- image understanding required:
  - `yes, but exact image not isolated in this slice`
- branding contamination exists:
  - `unknown for technical sub-region`
- block reason:
  - the extracted text only captures the top of the table and does not recover the full row set confidently; exact reuse would be unsafe even before authority review.

### `repeated branded shell assets`

- source PDF path:
  - `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- page number:
  - `22-30`
- asset path:
  - `images/a6f0e9c264f123cd.jpeg`
  - `images/f913a00ca327b920.jpeg`
  - `images/02577a0d9d1ef056.jpeg`
  - `images/a8c3a196df2348ac.jpeg`
  - `images/125e25b5113131e0.jpeg`
  - `images/28aed815ea62462d.jpeg`
- image understanding required:
  - `no`
- branding contamination exists:
  - `yes`
- block reason:
  - these are repeated shell, watermark, CTA, or branding assets and must not be treated as technical learning assets.

## Source-Mapping Recommendations

### `padstack and pad-layer vocabulary`

- source pages:
  - `23`
- stronger authority target:
  - official EDA tool padstack documentation
  - IPC land-pattern / padstack terminology references if public and reusable
- note:
  - terminology such as `regular pad`, `thermal relief`, `anti pad`, `solder mask`, and `paste mask` is promising for source-backed vocabulary recovery.

### `through-hole drill and pad relationships`

- source pages:
  - `23-24`
- stronger authority target:
  - IPC-2221/7351-adjacent public references where available
  - official CAD-vendor padstack guidance
  - connector or through-hole component manufacturer footprint recommendations
- note:
  - handbook formulas should be treated as method candidates only unless a stronger source explicitly supports them.

### `smd land-pattern compensation methods`

- source pages:
  - `25-28`
- stronger authority target:
  - IPC-7351 public summaries or legally reusable vendor guidance
  - package manufacturer or semiconductor vendor recommended land patterns
  - official component package application notes
- note:
  - the figures are strong structural assets for package-to-footprint variable mapping, but exact ranges and equations remain blocked until method-scoped authority is recovered.

### `bga pitch versus pad diameter`

- source pages:
  - `28`
- stronger authority target:
  - BGA package manufacturer land-pattern recommendations
  - official semiconductor package design guides
  - IPC/JEDEC public references if available
- note:
  - `images/cb091987d7d2b074.jpeg` should be preserved as a local provenance asset for later source comparison.

### `origin pin-1 polarity installation keepout and hole tables`

- source pages:
  - `29-30`
- stronger authority target:
  - official CAD library standards
  - connector-manufacturer footprint conventions
  - public IPC/JEDEC/EDA guidance for pin-1 marks, origin placement, and courtyard/keepout semantics
- note:
  - page `30` contains useful structural governance logic, but its numeric rules and hole table are not admissible from the handbook alone.

## Unresolved Items

### `standard hole table completeness`

- source pages:
  - `30`
- issue:
  - the extracted text only captures the opening rows and columns of `Table 1`; the full table body is not confidently recoverable from text alone in this slice.
- consequence:
  - exact table promotion is blocked and would need targeted image extraction or a stronger external source.

### `page 24 auxiliary flash / drill subfigures`

- source pages:
  - `24`
- asset paths:
  - `images/7a4f80ef561d7dc9.jpeg`
  - `images/db3d0dabc7959166.jpeg`
  - `images/44fa8349499dfd2a.jpeg`
  - `images/00a728ea52617e15.jpeg`
  - `images/3ce92aec7aa8e55a.jpeg`
  - `images/33a7e0b983cfc485.jpeg`
- issue:
  - these appear to be useful dimension sketches for flash/drill shapes, but the current pass did not map each one back to a specific formula variable set with full confidence.
- consequence:
  - keep as local technical assets with provenance, but do not overstate exact variable meaning.

### `origin and keepout figures absent as isolated assets`

- source pages:
  - `29-30`
- issue:
  - the text captures origin, pin-1, and keepout rule content, but no separate technical middle-region image asset was isolated for these pages in the manifest slice.
- consequence:
  - these pages are currently stronger as text-derived structural-context candidates than as image-derived drawing assets.

### `ocr confidence for equations and mixed notation`

- source pages:
  - `24-27`
- issue:
  - the OCR preserves most formulas, but mixed use of `'`, subscripts, and variable typography is not robust enough to claim symbol-perfect recovery for publication-grade exact formulas.
- consequence:
  - preserve the equations as claim inventory and exact-data candidates only; verify against stronger authority before any promotion.

## Lane Status

- lane result:
  - `completed_at_claim_family_level`
- strongest reusable outputs now:
  - `structural_context_candidate` for padstack layering, package-to-footprint variable mapping, origin and pin-1 governance, and connector-origin rule families
- preserved but not yet admissible outputs:
  - `exact_data_candidate` for pad / drill equations, flash formulas, BGA pitch-table rows, and silkscreen / keepout numeric rules
- blocked outputs:
  - handbook-only dimension tables, compensation ranges, keepout rules, standard-hole tables, and repeated branded shell assets
- next valid move:
  - source-first authority recovery for padstack terminology, land-pattern compensation methods, BGA land-pattern tables, and origin / pin-1 / keepout governance references

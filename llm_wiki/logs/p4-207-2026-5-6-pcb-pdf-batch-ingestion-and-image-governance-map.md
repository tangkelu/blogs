# P4-207 `PCB资料` PDF Batch Ingestion And Image Governance Map

Date: 2026-05-06

## Purpose

This log preserves a deletion-safe intake and execution plan for `/code/blogs/tmps/PCB资料`.

The batch is useful for:

- topic-family discovery
- heading and section inventory
- process-vocabulary expansion
- figure extraction and illustration reuse planning
- source-gap discovery for future source-backed fact promotion

The batch is **not** automatically authoritative for:

- universal numeric rules
- factory capability claims
- certification / qualification claims
- lead time / price / MOQ / yield / quality-rate claims
- branded workflow claims tied to `华秋DFM` or similar supplier tools

## Input Directory

- `/code/blogs/tmps/PCB资料`
- PDF count: `63`

Top-level distribution:

- `4` long-form handbook / guide PDFs
- `59` short article PDFs under `/code/blogs/tmps/PCB资料/PCB文章`

## File Families

### Long-form handbooks

- `【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- `【PCB必备】158页-PCBA检验规范汇总.pdf`
- `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `【PCB必备】194页-PCB设计规范经验之书.pdf`

Working posture:

- treat as high-value technical intake candidates
- extract heading trees, figure inventory, and claim families first
- do not promote raw numerics or acceptance criteria until source scope is verified

### Vendor article PDFs

Examples:

- `华秋DFM在硬件制造中的作用.pdf`
- `PCB阻抗误差控制在5%，究竟有多难？.pdf`
- `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
- `PCB布局布线的可制造性设计.pdf`
- `PCB可制造性设计及案例分析之孔槽篇.pdf`

Working posture:

- treat as claim inventory plus figure source
- strip brand promotion and CTA surfaces
- re-express reusable knowledge as neutral board-review / DFM / inspection language
- recover official or dated local authority before fact-layer promotion where claims are numeric, capability-specific, or standards-sensitive

## Existing Environment Findings

Local tool availability confirmed:

- `python`
- `fitz` / `PyMuPDF`
- `pypdf`
- `PIL`

Not currently available:

- `pdftotext`
- `pdfimages`
- `mutool`
- `pdftoppm`
- `tesseract`
- ImageMagick / Ghostscript CLI tools

Implication:

- this batch can still be processed locally with a Python-first pipeline
- text extraction, page rendering, bounding-box analysis, and image cropping can be automated without new system packages

## Sample Structure Findings

### Handbook pattern

`【PCB必备】85页-PCB设计EMC设计指导书.pdf`

- native text is extractable through `PyMuPDF`
- pages sampled did not show the `华秋DFM` promotion frame seen in the article PDFs
- likely suitable for heading/claim extraction and later source-family routing

`【PCB必备】158页-PCBA检验规范汇总.pdf`

- native text is extractable through `PyMuPDF`
- sampled opening pages behave like a standards / acceptance-outline document
- likely useful for inspection vocabulary, defect taxonomy, and acceptance-topic discovery

### Vendor article pattern

`华秋DFM在硬件制造中的作用.pdf`

- page text is extractable
- every page includes repeat brand CTA strings such as `华秋DFM 软件最新版→下载地址：点击下载`
- page layout includes repeated top/bottom branding plus QR / download / tool-promo regions
- some image blocks appear to be full-page background templates rather than purely technical figures

`PCB阻抗误差控制在5%，究竟有多难？.pdf`

- same repeating CTA / page footer pattern
- interior pages include technical illustration regions in addition to the page template
- indicates that technical figures can be preserved if cropped away from the branded page frame

## Recommended Ingestion Model

Do not ingest these PDFs directly into `facts/` or `wiki/` as if they were already clean authority.

Use a four-layer conversion path:

1. `PDF inventory layer`
   - file list
   - title / heading extraction
   - page and figure count
   - risk classification
2. `clean asset layer`
   - render or crop reusable figures
   - remove logo / CTA / QR / page footers
   - keep only technical diagrams, tables, or neutral process illustrations
3. `claim-family layer`
   - convert each PDF into neutral topic summaries and blocked-claim lists
   - identify where existing `llm_wiki` already has support
4. `source-backed promotion layer`
   - only after matching official or dated local authority should reusable facts or wiki pages be created or updated

## Image Governance Rules

### Preserve

- wiring / stackup / pad / via / spacing diagrams
- process-flow figures
- defect examples
- neutral engineering tables if they remain readable after cropping
- annotated fabrication / assembly examples when branding is removable

### Remove

- supplier logos
- QR codes
- download CTA banners
- contact / group-join banners
- page footers that repeat supplier branding
- screenshots whose core value is the supplier product UI rather than a generic engineering concept

### Transformation policy

- if the useful content is a sub-region of the page, crop to the technical region only
- if branding sits in a thin header / footer strip, mask or crop those strips
- if branding is embedded inside the technical illustration itself, mark the figure `blocked_pending_manual_redraw_or_reannotation`
- if the page is mainly a branded poster with small text, do not preserve it as an image; keep only the extracted claim family

### Output posture

Store image outputs as derived neutral assets for internal knowledge use, not as untouched vendor marketing pages.

Recommended asset metadata per figure:

- source PDF path
- source page number
- crop strategy: `top_crop`, `bottom_crop`, `mask`, `multi_crop`, or `blocked`
- branding removed: `yes/no/partial`
- figure class: `diagram`, `table`, `defect-example`, `process-flow`, `ui-screenshot`, `poster`
- reuse status: `safe_internal`, `needs_review`, `blocked`

## Recommended Batch Split

### Lane A: handbook extraction

Scope:

- the `4` long-form handbook PDFs

Expected output:

- one ingestion map for headings, major topic families, and existing `llm_wiki` support
- candidate source lanes for inspection, EMC, packaging, and design-rule families

Target status:

- `completed_at_claim_family_level`

### Lane B: vendor article clustering

Scope:

- the `59` PDFs in `PCB文章`

Cluster by topic family:

- DFM / DFA / layout review
- impedance / EMC / high-speed
- pad / hole / slot / via / solder-mask
- assembly / stencil / SMT / DIP / test
- procurement / BOM / component package
- panelization / edge clearance / mark points

Expected output:

- neutral per-topic claim-family inventory
- blocked vendor-promotion and capability claims
- image candidates list

Target status:

- `completed_at_claim_family_level`

### Lane C: clean-figure extraction

Scope:

- only figures from pages classified as technically reusable

Expected output:

- a local asset manifest
- cropped or masked figure files
- blocked list for pages requiring redraw or manual review

Target status:

- `source_recovery_in_progress` for image governance only

## How These PDFs Should Become `llm_wiki` Content

### For handbook PDFs

Primary path:

- build `logs/` intake maps
- identify reusable claim families
- map to existing `wiki/processes`, `wiki/testing`, `wiki/methods`, and `facts/methods`
- create new fact/wiki artifacts only where claim scope can be kept conservative or later source-backed

Typical resulting `llm_wiki` outputs:

- inspection taxonomy pages
- DFM / DFA boundary cards
- EMC layout governance pages
- packaging / footprint review checklists

### For vendor article PDFs

Primary path:

- strip vendor framing
- rewrite article knowledge into neutral engineering language
- use them to discover what topic pages are missing
- promote only the non-promotional engineering structure

Typical resulting `llm_wiki` outputs:

- claim-family intake logs
- gap maps for impedance, spacing, solder-mask, panelization, BOM consistency, and testability
- neutral process or review-boundary wiki pages after official-source recovery

### For images

Primary path:

- do not embed whole vendor PDF pages
- extract only technical subfigures
- attach figure metadata so later blog-writing agents know the provenance and risk status

Possible storage approach:

- a future `tmps/PCB资料_derived_assets/` staging directory for cropped figures and manifests
- optional later promotion of selected safe figures into a stable internal asset directory once reviewed

## Blocked Claim Classes

Do not directly promote from this batch without stronger authority:

- `华秋DFM` product capability claims
- supplier-specific procurement or anti-counterfeit guarantees
- exact impedance control capability promises
- exact assembly quality-rate or yield promises
- standards acceptance thresholds unless the document authority is independently verified
- tool-driven DFM automation claims framed as universal manufacturing truth

## Proposed Execution Order

1. create this batch map and keep the directory deletion-safe
2. build a Python extractor for text, page images, and figure bounding boxes
3. run the extractor on a small pilot set:
   - `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
   - `【PCB必备】158页-PCBA检验规范汇总.pdf`
   - `华秋DFM在硬件制造中的作用.pdf`
   - `PCB阻抗误差控制在5%，究竟有多难？.pdf`
4. verify whether top/bottom crop rules remove most branding automatically
5. generate:
   - one handbook intake log
   - one article-cluster intake log
   - one clean-asset manifest
6. only then decide which fact/wiki promotions are justified

## Current Status

- batch status: `completed_at_claim_family_level` for high-level intake planning only
- extraction tooling status: `pilot_implemented`
- clean-figure workflow status: `text_first_assets_ready_for_selective_vision_pass`
- fact-layer promotion status: `not_started`

## Implemented Pilot

Repo-local extractor added:

- `/code/blogs/scripts/extract_pcb_pdf_assets.py`
- `/code/blogs/scripts/test_extract_pcb_pdf_assets.py`

Implemented behavior:

- extract page text first into per-page `.txt`
- preserve embedded PDF images as local assets
- write `manifest.json` that records:
  - source PDF
  - page count
  - per-page text path
  - per-page image count
  - per-image local asset path
  - per-image page occurrence bounding boxes

Pilot output root:

- `/code/blogs/tmps/pcb_pdf_extracted`

Pilot sample already run on:

- `【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `PCB阻抗误差控制在5%，究竟有多难？.pdf`
- `华秋DFM在硬件制造中的作用.pdf`

Observed pilot result:

- handbook PDF:
  - `85` text pages extracted
  - `46` pages contain image assets
- vendor article PDF `PCB阻抗误差控制在5%，究竟有多难？`:
  - all `4` pages extracted as text
  - all `4` pages contain image assets, including repeated branded template assets and technical figures
- vendor article PDF `华秋DFM在硬件制造中的作用`:
  - all `3` pages extracted as text
  - all `3` pages contain image assets, mostly page-template branding elements

## Updated Preferred Workflow

User-preferred route is now:

1. extract text from the full PDF batch first
2. preserve all embedded images as separate local assets
3. inspect `manifest.json` to find pages with `image_count > 0`
4. only send those image assets or image-bearing pages to `gpt-5.4` subagents for visual interpretation
5. keep image-to-page-to-PDF references intact for later citation and de-branding review

This avoids wasting vision passes on text-only pages and keeps all real images locally available for later OCR or table understanding.

## Next Recommended Deliverables

- run the extractor on the remaining `/code/blogs/tmps/PCB资料` PDFs
- add a second-stage filter that marks repeated vendor-template assets versus likely technical figures
- create handbook-only and article-cluster intake logs from the extracted text corpus
- create selective `gpt-5.4` vision passes only for image-bearing pages or image-table assets that matter

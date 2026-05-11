# P4-220B PCBA Local Asset Linkage Map

Date: `2026-05-07`
Parent promotion state: `after p4-219b`
Lane: `NR2`
Model requested: `gpt-5.4`

## Purpose

This controller log maps which preserved local PCBA image assets are the strongest candidates to link to the admitted PCBA fact and wiki layer created in `p4-219b`.

This file treats:

- lane logs as provenance inventory
- local handbook-derived images as supporting assets only
- admitted `facts/` and `wiki/` pages as the only current knowledge-layer targets

This file does not promote any secondary-PDF threshold, dimensional, accept/reject, or standards-equivalent content.

## Inputs Reviewed

- `/code/blogs/llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`
- `/code/blogs/llm_wiki/logs/p4-214-2026-5-6-pcb-pdf-figure-table-learning-contract.md`
- `/code/blogs/llm_wiki/logs/p4-215b2-2026-5-6-pcba-lane-b2-solder-defect-and-workmanship-pages.md`
- `/code/blogs/llm_wiki/logs/p4-215b3-2026-5-6-pcba-lane-b3-cleanliness-warpage-jumper-orientation-pages.md`
- `/code/blogs/llm_wiki/logs/p4-219b-2026-5-7-pcba-taxonomy-first-promotion-review.md`
- `/code/blogs/llm_wiki/facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md`
- `/code/blogs/llm_wiki/wiki/testing/pcba-visual-inspection-taxonomy.md`

## Lane Status

Current lane status:

- `controller_ready_asset_linkage_map_created`

What is complete in this lane:

- strongest currently preserved local PCBA image candidates were mapped to admitted fact/wiki targets
- crop-gated and blocked asset classes were separated from direct-link candidates
- minimum required metadata for safe asset linkage was reduced to a stable controller-ready field set

What is not complete in this lane:

- no new `facts/`, `wiki/`, `sources/`, or tracker changes were made
- no new local cropped derivative assets were created
- no handbook thresholds, dimensions, percentages, or workmanship judgments were promoted
- no branded or threshold-heavy image was admitted as a reusable linked technical figure

## Linkage Decision Rules Used

- prefer assets whose main value is taxonomy or structural context, not handbook thresholds
- prefer assets with no visible branding contamination
- allow minor source marks only when the image is not otherwise separable enough to crop today and the linked use stays internal-support only
- block any asset whose primary meaning depends on handbook exact thresholds, dimensions, or `acceptable / unacceptable` judgments
- block or crop-gate any asset with branding contamination when the branding is part of the technical panel

## Strongest Asset-To-Fact Mappings

### Group A: defect and contamination taxonomy

#### `through-hole solder wetting continuity`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `84-87`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/6ac0e52d0e267a82.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/c5acc9b33b4fcd7b.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/c9111ce33b9a6347.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images are visually legible, non-branded, and their safe value is class naming rather than threshold reuse
- allowed canonical concept:
  - `through-hole solder wetting continuity`
- blocked companion claims:
  - wetting percentages
  - minimum coverage conclusions
  - pass/fail reconstruction

#### `gold finger solder contamination`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `88`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a30ae5a904570378.png`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/2998d194e547a917.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images support contact-area contamination taxonomy cleanly and do not require threshold language to stay useful
- allowed canonical concept:
  - `gold finger solder contamination`
- blocked companion claims:
  - rejectability
  - contact-performance consequences
  - standards-equivalent contamination limits

#### `flux residue visibility`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `91`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/db6613d15310f857.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/ae8606305fa9da12.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images are neutral visual cleanliness examples and align directly with the admitted taxonomy wording
- allowed canonical concept:
  - `flux residue visibility`
- blocked companion claims:
  - cleanliness thresholds
  - ionic contamination implications
  - release criteria

#### `particulate contamination` and `white residue`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `92-95`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/3397d93c361e8cd9.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/cd0c340818b02cd4.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a77c29c8f8f8265b.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/793a84c99f8dbe61.jpeg`
- linkage strength:
  - `strong`
- reason:
  - these are straightforward contamination-family examples with no visible branding and low overclaim risk when described structurally
- allowed canonical concepts:
  - `particulate contamination`
  - `white residue`
- blocked companion claims:
  - corrosion severity thresholds
  - contamination source certainty
  - cleaning acceptance limits

#### `adhesive contamination before soldering`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `130`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/fe5edf11b90fd62d.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/4f51a0e695de1d23.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/4109051f7b142652.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images remain useful as pre-solder workmanship taxonomy without bringing in blocked pad-encroachment limits
- allowed canonical concept:
  - `adhesive contamination before soldering`
- blocked companion claims:
  - acceptable glue volume
  - pad-coverage limits

#### `chip component misalignment`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `131-132`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/38d22688aa56d8a9.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/535919777764b7bb.jpeg`
- linkage strength:
  - `medium_strong`
- reason:
  - the candidates support taxonomy well, but adjacent threshold diagrams on the same page family create higher overclaim risk if metadata is not explicit
- allowed canonical concept:
  - `chip component misalignment`
- blocked companion claims:
  - overhang limits
  - offset percentages
  - acceptability thresholds

#### `side-mounted chip placement`, `upside-down chip placement`, and `coplanarity defect`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `150-151`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/7485decb58d182be.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/4f48689ddeece117.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/920271cb0c7ab373.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/abb39ae654aad31d.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/192a17a9f7b33b6e.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images show clear anomaly families and stay useful without any admitted threshold dependency
- allowed canonical concepts:
  - `side-mounted chip placement`
  - `upside-down chip placement`
  - `coplanarity defect`
- blocked companion claims:
  - defect severity ranking
  - release decision claims

#### `tombstone defect`

- target fact:
  - `facts/methods/pcba-defect-photo-taxonomy-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b2`
- source page:
  - `151`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/920271cb0c7ab373.jpeg`
- linkage strength:
  - `medium`
- reason:
  - visually useful, but the selected image contains multiple anomaly cues and should be linked with a narrow concept label to avoid over-precise interpretation
- allowed canonical concept:
  - `tombstone defect`
- blocked companion claims:
  - root-cause explanation
  - universal rejectability

### Group B: orientation and polarity vocabulary

#### `horizontal component orientation`, `component polarity visibility`, and `readable marking direction`

- target fact:
  - `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `44`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/534da88710c492eb.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the diagram is clean, non-branded, and almost purely vocabulary-bearing
- allowed canonical concepts:
  - `horizontal component orientation`
  - `component polarity visibility`
  - `readable marking direction`
- blocked companion claims:
  - best/acceptable/unacceptable status
  - universal assembly rule claims

#### `vertical component polarity orientation`

- target fact:
  - `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `45`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/dda535a4b8ee638b.png`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/c90c145e910db2ce.png`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/88f5c935b23012f3.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the images clearly separate visual orientation language from threshold claims and are suitable for English-only canonical naming
- allowed canonical concepts:
  - `vertical component polarity orientation`
  - `component polarity visibility`
- blocked companion claims:
  - acceptability judgments
  - universal polarity installation law

#### `radial capacitor lead orientation` and `reversed polarity example`

- target fact:
  - `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `46`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/d7b29d9f017f9ca8.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/01e38a16333f1d02.jpeg`
- linkage strength:
  - `strong`
- reason:
  - these images support polarity-direction vocabulary directly and do not rely on exact dimensions to stay meaningful
- allowed canonical concepts:
  - `radial capacitor lead orientation`
  - `reversed polarity example`
- blocked companion claims:
  - lead-length requirements
  - field-failure certainty

### Group C: warpage and jumper structural context

#### `burn-mark versus solder-mask discoloration`

- target fact:
  - `facts/methods/board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `119`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/60577188ffce97cc.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the image safely supports visible-condition distinction at a structural level without requiring any threshold
- allowed canonical concept:
  - `burn-mark versus solder-mask discoloration`
- blocked companion claims:
  - severity thresholds
  - root-cause certainty

#### `board warpage visual example`

- target fact:
  - `facts/methods/board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `119`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/3c2e4a81a091d543.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the image clearly communicates visible board distortion while avoiding any need to retain blocked percentage values
- allowed canonical concept:
  - `board warpage visual example`
- blocked companion claims:
  - `1.5%`
  - `0.75%`
  - flatness-release conclusions

#### `jumper-wire routing example` and `jumper-wire path clearance context`

- target fact:
  - `facts/methods/board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md`
- target wiki:
  - `wiki/testing/pcba-visual-inspection-taxonomy.md`
- source lane:
  - `p4-215b3`
- source page:
  - `121`
- strongest current asset candidates:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/9f7ef24516f3cf36.jpeg`
- linkage strength:
  - `strong`
- reason:
  - the photo is useful as route-shape and clearance-context evidence without importing blocked wire-gauge or insulation prescriptions
- allowed canonical concepts:
  - `jumper-wire routing example`
  - `jumper-wire path clearance context`
- blocked companion claims:
  - wire gauge
  - insulation rules
  - approved repair method claims

## Crop-Gated Or Blocked Assets

### Crop-gated because branding contamination exists

#### `machine-inserted connector pin side-wetting coverage`

- source lane:
  - `p4-215b2`
- source page:
  - `89-90`
- affected assets:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/8a8833b5f109476d.png`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a9f480bd94950fdf.png`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/86c1d54469d9be97.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/3a5c986a9fa9d8e1.jpeg`
- current status:
  - `crop_gated`
- reason:
  - some figures include embedded source marks and the main semantic value of this asset family is threshold-heavy side-wetting coverage, which is blocked today
- allowed future use only if:
  - a clean technical sub-region can be separated
  - the linked concept is reduced to neutral connector-pin wetting topology language
  - no side-count or coverage threshold wording is attached

#### `axial component standoff height example`

- source lane:
  - `p4-215b3`
- source page:
  - `46`
- affected asset:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/04f3e7c4a20d3863.png`
- current status:
  - `blocked_for_direct_linking`
- reason:
  - the image includes a minor source mark, but the larger problem is that its main value is the explicit `1.5 mm` standoff threshold already blocked in the admitted fact layer
- allowed future use only if:
  - a threshold-free crop is created for generic axial standoff posture only
  - the linked concept excludes any dimensional requirement

### Blocked because the main value is threshold or formula overclaim risk

#### `chip component offset and solder-width formulas`

- source lane:
  - `p4-215b2`
- source page:
  - `130-133`
- affected assets:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/2932561c1d4bba3d.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/8b2ca1a496911880.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/df458e257fc8e76e.jpeg`
- current status:
  - `blocked_for_linking`
- reason:
  - these images are dominated by variable-based formula and threshold content rather than safe taxonomy-only meaning

#### `cylindrical end-cap component placement and joint geometry`

- source lane:
  - `p4-215b2`
- source page:
  - `134-137`
- affected assets:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/5490e3da7ce54f8a.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/218e5d217310aecb.jpeg`
- current status:
  - `blocked_for_linking`
- reason:
  - the images are primarily geometry-threshold carriers, not safe structural taxonomy

#### `gull-wing and J-lead solder-joint geometry`

- source lane:
  - `p4-215b2`
- source page:
  - `140-150`
- affected assets:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/7b872de09cd93722.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/eb4fd6956782a703.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/0a1b3bfcd4d3e149.jpeg`
- current status:
  - `blocked_for_linking`
- reason:
  - the figures are high-risk because their main semantics are exact lead/joint dimensions and acceptability criteria

### Blocked because only text-level candidate data exists

#### `warpage percentage limits`

- source lane:
  - `p4-215b3`
- source page:
  - `119`
- asset path:
  - `none`
- current status:
  - `blocked_no_asset_link`
- reason:
  - this is threshold-only text inventory, not a safe image-link candidate

#### `jumper-wire length and gauge guidance`

- source lane:
  - `p4-215b3`
- source page:
  - `120`
- asset path:
  - `none`
- current status:
  - `blocked_no_asset_link`
- reason:
  - this is blocked prescriptive text, not a safe local visual-support asset

## Minimum Metadata Required For Every Approved Link

Preserve at minimum:

- `source_pdf_path`
- `source_page_number`
- `local_asset_path`
- `source_lane_log`
- `asset_class`
- `learning_type`
- `english_canonical_concept_name`
- `target_fact_path`
- `target_wiki_path`
- `linkage_strength`
- `linkage_decision`
  - use one of:
    - `approved`
    - `crop_gated`
    - `blocked`
- `branding_status`
  - use one of:
    - `none_visible`
    - `minor_embedded_mark`
    - `inseparable_branding`
- `threshold_overclaim_risk`
  - use one of:
    - `low`
    - `medium`
    - `high`
- `blocked_companion_claims`
- `short_structural_caption`

Recommended additional fields when available:

- `local_asset_dimensions_px`
- `crop_needed`
- `crop_notes`
- `related_fact_ids`
- `related_topic_ids`

## Controller Recommendations

- link Group A, Group B, and Group C strong candidates first because they are already aligned to admitted taxonomy-only wording
- do not link any formula, geometry-threshold, warpage-percentage, or jumper-prescription asset as a reusable knowledge-layer image
- if later work wants broader coverage, create clean cropped derivatives for the crop-gated assets before any linkage record is reused
- keep all linked assets explicitly marked as `supporting_local_asset_only`, not authority

## Proposed Asset-To-Fact Mapping Summary

- `pcba-defect-photo-taxonomy-boundary.md`
  - strongest linked concepts:
    - `through-hole solder wetting continuity`
    - `gold finger solder contamination`
    - `flux residue visibility`
    - `particulate contamination`
    - `white residue`
    - `adhesive contamination before soldering`
    - `chip component misalignment`
    - `side-mounted chip placement`
    - `upside-down chip placement`
    - `tombstone defect`
    - `coplanarity defect`
- `component-orientation-and-polarity-inspection-vocabulary-boundary.md`
  - strongest linked concepts:
    - `horizontal component orientation`
    - `component polarity visibility`
    - `readable marking direction`
    - `vertical component polarity orientation`
    - `radial capacitor lead orientation`
    - `reversed polarity example`
- `board-warpage-and-jumper-wire-inspection-vocabulary-boundary.md`
  - strongest linked concepts:
    - `burn-mark versus solder-mask discoloration`
    - `board warpage visual example`
    - `jumper-wire routing example`
    - `jumper-wire path clearance context`
- `wiki/testing/pcba-visual-inspection-taxonomy.md`
  - strongest linked role:
    - topic-level routing page for all approved taxonomy and structural-context image links above

## Changed Files

- created:
  - `/code/blogs/llm_wiki/logs/p4-220b-2026-5-7-pcba-local-asset-linkage-map.md`


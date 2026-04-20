# 1119-1-ccc Rewrite Plan

## Goal

This batch is for HILPCB blog traffic acquisition. Two evaluation dimensions matter:

1. URL/slug should be SEO-friendly and clear.
2. Content should be localized for each language, especially for engineering and B2B manufacturing readers.

Important constraint:

- Do not conflict with any existing URL in `/code/hileap/frontendHIL/.output/public/sitemap.xml`.

## Current Assessment

### Slug problems

- Most original filenames were overlong and read like stacked keyword clusters.
- Several topics mixed application, industry, and support-keyword phrases into one slug.
- Some filenames obscured the actual article topic instead of clarifying search intent.

### Localization problems

- `en`: heavy white-paper/tutorial voice, obvious template reuse, and SEO-led framing.
- `cn`: still too close to keyword content and translated structure instead of natural electronics-manufacturing trade language.
- `de/fr/it/ru`: clear machine-translation traces, stiff sentence rhythm, and weak local technical phrasing.

## Phase 1: Slug Rewrite

The following recommended slugs were checked against `/code/hileap/frontendHIL/.output/public/sitemap.xml` and were not found as exact existing blog URLs at the time of review.

| Current filename | Recommended slug |
| :--- | :--- |
| `48v-to-12v-conversion-board-power-cooling-systems` | `48v-12v-power-board-design` |
| `ai-server-motherboard-reliability-ai-server-backplane` | `ai-server-motherboard-reliability` |
| `automotive-ethernet-compliance-automotive-adas-ev-power` | `automotive-ethernet-pcb-compliance` |
| `chiplet-bridge-assembly-ai-chip-interconnect` | `chiplet-bridge-pcb-assembly` |
| `cxl-si-best-practices-assembly-high-speed-si` | `cxl-signal-integrity-assembly` |
| `ethercat-interface-prototype-industrial-robotics-control` | `ethercat-interface-pcb-prototype` |
| `industrial-grade-mmwave-antenna-array-5g-6g-communication` | `mmwave-antenna-array-pcb` |
| `low-loss-bidirectional-dc-dc-converter-renewable-energy-inverter` | `bidirectional-dc-dc-converter-pcb` |
| `mixed-signal-layout-pcb-design-basics` | `mixed-signal-pcb-layout` |
| `qsfp-dd-module-compliance-data-center-optical-module` | `qsfp-dd-module-pcb-compliance` |
| `thermal-reliability-stackup-pcb-stackup-materials` | `pcb-thermal-reliability-stackup` |
| `wearable-patch-quality-medical-imaging-wearable` | `wearable-patch-pcb-quality` |
| `x-ray-inspection-checklist-pcb-manufacturing-quality` | `pcb-xray-inspection` |

## Phase 2: Shared Metadata Rules

### Slug rule

- Use one English SEO slug across all languages for the same topic.
- Keep slug short, descriptive, and aligned with buyer/search intent.
- Avoid stuffing multiple adjacent keywords into one URL.

### Tag rule

- Use one consistent English tag set across all languages.
- Keep tags short and taxonomy-like, not sentence-like.
- Prefer tags that reflect engineering topic + manufacturing intent.

## Rewrite Standards To Apply

- Remove machine-translation phrasing and literal glossary-style sentences.
- Remove FAQ dumps, giant checklist structures, white-paper/course framing, and decorative HTML-heavy marketing blocks.
- Keep the tone closer to an engineering manufacturing partner, not a keyword farm.
- Prioritize manufacturability, DFM, assembly risk, validation logic, and production readiness.
- Keep each language readable as local trade content rather than a direct translation artifact.

## Latest Update

- Built initial assessment for `1119-1-ccc`.
- Reviewed topic list and confirmed this batch has the same core issues as previous batches: overlong slugs, keyword-heavy metadata, mixed-language source corruption, and template-heavy body structure.
- Checked recommended replacement slugs against the sitemap and found no exact URL conflicts.
- Applied slug rewrites across `en/cn/de/fr/it/ru`.
- Standardized tags across all 13 topics and all 6 languages with a shorter engineering/manufacturing taxonomy instead of repetitive SEO tags.

## Rewrite Progress

Completed slug rewrites across `en/cn/de/fr/it/ru`:

- `48v-12v-power-board-design`
- `ai-server-motherboard-reliability`
- `automotive-ethernet-pcb-compliance`
- `chiplet-bridge-pcb-assembly`
- `cxl-signal-integrity-assembly`
- `ethercat-interface-pcb-prototype`
- `mmwave-antenna-array-pcb`
- `bidirectional-dc-dc-converter-pcb`
- `mixed-signal-pcb-layout`
- `qsfp-dd-module-pcb-compliance`
- `pcb-thermal-reliability-stackup`
- `wearable-patch-pcb-quality`
- `pcb-xray-inspection`

Completed shared tag cleanup across `en/cn/de/fr/it/ru`:

- `48v-12v-power-board-design`
- `ai-server-motherboard-reliability`
- `automotive-ethernet-pcb-compliance`
- `chiplet-bridge-pcb-assembly`
- `cxl-signal-integrity-assembly`
- `ethercat-interface-pcb-prototype`
- `mmwave-antenna-array-pcb`
- `bidirectional-dc-dc-converter-pcb`
- `mixed-signal-pcb-layout`
- `qsfp-dd-module-pcb-compliance`
- `pcb-thermal-reliability-stackup`
- `wearable-patch-pcb-quality`
- `pcb-xray-inspection`

Next step:

- tighten titles and descriptions
- start full body localization rewrites from the most template-heavy topics first

Metadata update:

- Rewrote `title` and `description` for all 13 topics across `en/cn/de/fr/it/ru`.
- Removed white-paper/checklist framing from metadata where possible.
- Replaced keyword-stacked titles with shorter topic-first titles.
- Replaced repeated boilerplate descriptions with manufacturing-focused summaries tied to DFM, validation, reliability, and assembly risk.

Next step now:

- rewrite full bodies, starting with the worst mixed-language/template-heavy files in `en`
- then localize the cleaned body structure into `cn/de/fr/it/ru`

Body rewrite progress:

- Rewrote `en/mixed-signal-pcb-layout.md` into a manufacturability-focused article with no FAQ dump, no decorative HTML blocks, and no template boilerplate.
- Rewrote `en/pcb-thermal-reliability-stackup.md` into a practical stackup article centered on materials, copper balance, via reliability, moisture risk, and supplier review.
- Rewrote `en/pcb-xray-inspection.md` into a production-quality article focused on hidden-joint inspection scope, process feedback, sampling strategy, and traceability.

Current next step:

- continue rewriting the remaining template-heavy English bodies
- after English structure is stable, localize those rewritten bodies into `cn/de/fr/it/ru`

Additional English body rewrites completed:

- Rewrote `en/automotive-ethernet-pcb-compliance.md` into a vehicle-grade compliance article centered on channel control, isolation, power-noise separation, mechanical robustness, and DFM review.
- Rewrote `en/chiplet-bridge-pcb-assembly.md` into an advanced-packaging article focused on substrate manufacturability, warpage, fine-pitch interconnects, underfill, and reliability validation.
- Rewrote `en/qsfp-dd-module-pcb-compliance.md` into a data-center optical module article focused on channel budget, low-loss materials, thermal design, connector transitions, and production discipline.

Updated next step:

- continue cleaning the remaining English bodies with mixed-language/template artifacts
- then localize the cleaned English structure into the other five languages

Remaining English body cleanup completed:

- Rewrote `en/48v-12v-power-board-design.md`.
- Rewrote `en/ai-server-motherboard-reliability.md`.
- Rewrote `en/bidirectional-dc-dc-converter-pcb.md`.
- Rewrote `en/cxl-signal-integrity-assembly.md`.
- Rewrote `en/ethercat-interface-pcb-prototype.md`.
- Rewrote `en/mmwave-antenna-array-pcb.md`.
- Rewrote `en/wearable-patch-pcb-quality.md`.

English status:

- all 13 `en` topics are now on the cleaned manufacturing-oriented structure
- major mixed-language pollution, decorative HTML blocks, white-paper framing, and template-heavy FAQ content have been removed from the English set

Next execution step:

- localize the cleaned English structure into `cn/de/fr/it/ru`

Localization started:

- Completed full-body localization for `mixed-signal-pcb-layout` in `cn/de/fr/it/ru` using the cleaned English manufacturing-oriented structure as the source model.

Current next step:

- continue localizing the next cleaned English topics into `cn/de/fr/it/ru`

Localization progress expanded:

- Completed full-body localization for `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`.
- Completed full-body localization for `pcb-xray-inspection` in `cn`.

Current next step:

- continue localizing `pcb-xray-inspection` into `de/fr/it/ru`
- then move through the remaining cleaned English topics in the same way

Localization progress updated:

- Rewrote `48v-12v-power-board-design` in `cn/de/fr/it/ru` to remove mixed-language copy, decorative HTML blocks, and compliance-heavy generic wording. The new versions now read as practical power-board manufacturing articles centered on current loops, thermal path, EMC control, spacing review, DFM, and production validation.
- Rewrote `pcb-xray-inspection` in `de/fr/it/ru` so the body now matches the cleaned English structure and focuses on hidden-joint inspection, void criteria, sampling logic, process feedback, DFM impact, and traceability instead of template white-paper content.
- Rewrote `ai-server-motherboard-reliability` in `cn/de/fr/it/ru` so the body now follows the stable English structure and reads as manufacturing-oriented content about stackup control, high-speed channel margin, PDN stability, thermal stress, fabrication tolerances, and validation for AI server boards.

Current completed full-body localization set:

- `mixed-signal-pcb-layout` in `cn/de/fr/it/ru`
- `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`
- `pcb-xray-inspection` in `cn/de/fr/it/ru`
- `48v-12v-power-board-design` in `cn/de/fr/it/ru`
- `ai-server-motherboard-reliability` in `cn/de/fr/it/ru`

Current next step:

- continue localizing the remaining cleaned English topics into `cn/de/fr/it/ru`
- next recommended candidates: `automotive-ethernet-pcb-compliance`, `bidirectional-dc-dc-converter-pcb`, `chiplet-bridge-pcb-assembly`, `cxl-signal-integrity-assembly`

Localization progress updated again:

- Rewrote `automotive-ethernet-pcb-compliance` in `cn/de/fr/it/ru` to remove white-paper framing, mixed-language content, and decorative template sections. The new versions now focus on channel control, power-noise separation, HV/LV partitioning, thermal stress, connector robustness, and vehicle-relevant validation.
- Rewrote `bidirectional-dc-dc-converter-pcb` in `cn/de/fr/it/ru` to remove keyword-heavy template copy and replace it with practical manufacturing-oriented content on bidirectional current paths, copper balance, creepage/clearance, thermal path definition, assembly review, and realistic duty-cycle validation.

Current completed full-body localization set:

- `mixed-signal-pcb-layout` in `cn/de/fr/it/ru`
- `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`
- `pcb-xray-inspection` in `cn/de/fr/it/ru`
- `48v-12v-power-board-design` in `cn/de/fr/it/ru`
- `ai-server-motherboard-reliability` in `cn/de/fr/it/ru`
- `automotive-ethernet-pcb-compliance` in `cn/de/fr/it/ru`
- `bidirectional-dc-dc-converter-pcb` in `cn/de/fr/it/ru`

Updated next step:

- continue localizing the remaining cleaned English topics into `cn/de/fr/it/ru`
- next recommended candidates: `chiplet-bridge-pcb-assembly`, `cxl-signal-integrity-assembly`, `ethercat-interface-pcb-prototype`, `mmwave-antenna-array-pcb`

Localization progress updated again:

- Rewrote `chiplet-bridge-pcb-assembly` in `cn/de/fr/it/ru` to remove white-paper explanation, decorative HTML, and mixed-language corruption. The new versions are now structured around assembly-driven substrate design, warpage risk, fine-pitch process margin, underfill reliability, thermal cycling, and inspection traceability.
- Rewrote `cxl-signal-integrity-assembly` in `cn/de/fr/it/ru` to remove template SI-training content and replace it with production-oriented guidance on channel loss budget, stackup control, via/connector transitions, assembly impact, validation evidence, and early supplier DFM alignment.

Current completed full-body localization set:

- `mixed-signal-pcb-layout` in `cn/de/fr/it/ru`
- `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`
- `pcb-xray-inspection` in `cn/de/fr/it/ru`
- `48v-12v-power-board-design` in `cn/de/fr/it/ru`
- `ai-server-motherboard-reliability` in `cn/de/fr/it/ru`
- `automotive-ethernet-pcb-compliance` in `cn/de/fr/it/ru`
- `bidirectional-dc-dc-converter-pcb` in `cn/de/fr/it/ru`
- `chiplet-bridge-pcb-assembly` in `cn/de/fr/it/ru`
- `cxl-signal-integrity-assembly` in `cn/de/fr/it/ru`

Updated next step:

- continue localizing the remaining cleaned English topics into `cn/de/fr/it/ru`
- next recommended candidates: `ethercat-interface-pcb-prototype`, `mmwave-antenna-array-pcb`, `qsfp-dd-module-pcb-compliance`, `wearable-patch-pcb-quality`

Localization progress updated again:

- Rewrote `ethercat-interface-pcb-prototype` in `cn/de/fr/it/ru` to remove certification-course style content and replace it with prototype-to-pilot guidance on clean communication routing, protection placement, EMC pre-check, test access, coating/environment review, and industrial validation.
- Rewrote `mmwave-antenna-array-pcb` in `cn/de/fr/it/ru` to remove measurement-white-paper framing and replace it with manufacturing-oriented RF content around material consistency, stackup tolerance, RF transition control, panel stability, and RF-linked production verification.

Current completed full-body localization set:

- `mixed-signal-pcb-layout` in `cn/de/fr/it/ru`
- `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`
- `pcb-xray-inspection` in `cn/de/fr/it/ru`
- `48v-12v-power-board-design` in `cn/de/fr/it/ru`
- `ai-server-motherboard-reliability` in `cn/de/fr/it/ru`
- `automotive-ethernet-pcb-compliance` in `cn/de/fr/it/ru`
- `bidirectional-dc-dc-converter-pcb` in `cn/de/fr/it/ru`
- `chiplet-bridge-pcb-assembly` in `cn/de/fr/it/ru`
- `cxl-signal-integrity-assembly` in `cn/de/fr/it/ru`
- `ethercat-interface-pcb-prototype` in `cn/de/fr/it/ru`
- `mmwave-antenna-array-pcb` in `cn/de/fr/it/ru`

Updated next step:

- continue localizing the remaining cleaned English topics into `cn/de/fr/it/ru`
- remaining main candidates: `qsfp-dd-module-pcb-compliance`, `wearable-patch-pcb-quality`

Final localization update for this batch:

- Rewrote `qsfp-dd-module-pcb-compliance` in `cn/de/fr/it/ru` into manufacturing-oriented optical-module content covering channel budget, material stability, thermal path, connector-edge control, environmental reliability, and assembly discipline.
- Rewrote `wearable-patch-pcb-quality` in `cn/de/fr/it/ru` into practical wearable-medical manufacturing content covering real-use flex strain, skin-adjacent material review, assembly cleanliness, flex-layout durability, functional consistency, and full-process supplier review.

Final completed full-body localization set:

- `mixed-signal-pcb-layout` in `cn/de/fr/it/ru`
- `pcb-thermal-reliability-stackup` in `cn/de/fr/it/ru`
- `pcb-xray-inspection` in `cn/de/fr/it/ru`
- `48v-12v-power-board-design` in `cn/de/fr/it/ru`
- `ai-server-motherboard-reliability` in `cn/de/fr/it/ru`
- `automotive-ethernet-pcb-compliance` in `cn/de/fr/it/ru`
- `bidirectional-dc-dc-converter-pcb` in `cn/de/fr/it/ru`
- `chiplet-bridge-pcb-assembly` in `cn/de/fr/it/ru`
- `cxl-signal-integrity-assembly` in `cn/de/fr/it/ru`
- `ethercat-interface-pcb-prototype` in `cn/de/fr/it/ru`
- `mmwave-antenna-array-pcb` in `cn/de/fr/it/ru`
- `qsfp-dd-module-pcb-compliance` in `cn/de/fr/it/ru`
- `wearable-patch-pcb-quality` in `cn/de/fr/it/ru`

Batch status:

- all 13 topics now have rewritten `en` bodies and fully localized `cn/de/fr/it/ru` bodies on the cleaned manufacturing-oriented structure
- slug rewrite, tag normalization, metadata cleanup, and full-body localization are complete for `1119-1-ccc`
- a final scan did not find the earlier decorative HTML blocks or the most obvious legacy white-paper/template markers in the localized set

Sampling QA follow-up:

- Performed a manual localization sample review after the batch was marked complete.
- Sampled files:
  - `cn/mmwave-antenna-array-pcb.md`
  - `de/qsfp-dd-module-pcb-compliance.md`
  - `fr/ethercat-interface-pcb-prototype.md`
  - `it/wearable-patch-pcb-quality.md`
  - `ru/cxl-signal-integrity-assembly.md`
- Sample conclusion:
  - `cn` sample was already acceptable and read like local engineering/manufacturing content.
  - `de/fr/it` samples were usable but still carried noticeable English technical carryovers and translated phrasing.
  - `ru` sample showed the strongest remaining machine-translation signature because too much English terminology was left in title, description, and body.

Second-pass localization cleanup completed from the sampling review:

- Cleaned `ru/cxl-signal-integrity-assembly.md` again to remove the heaviest English carryover from title, description, headings, bullets, and closing summary. The revised version now reads much closer to native Russian technical trade content while keeping the same CXL manufacturing structure.
- Cleaned `fr/ethercat-interface-pcb-prototype.md` again to replace remaining English-heavy wording such as `motion control`, `breakout`, `surge`, `creepage`, `clearance`, `shields`, `coating`, and `keep-out` with more natural French engineering phrasing.
- Cleaned `it/wearable-patch-pcb-quality.md` again to reduce English carryover such as `wearable`, `body-worn`, `assembly`, `handling`, `cleanliness`, `control plan`, `build`, and similar terms in favor of more natural Italian manufacturing language.
- Cleaned `de/qsfp-dd-module-pcb-compliance.md` again to reduce Denglish in key sections, especially around `Channel-Budget`, `Trace`, `Connector`, `Assembly`, `Breakout`, `Goldfinger`, and related manufacturing terms.

Post-cleanup QA result:

- A targeted regex check on the four corrected sample files found the earlier English-heavy carryovers only in the shared English tag fields, not in the body copy.
- Current status for `1119-1-ccc`:
  - slug/tag strategy remains stable
  - sampled SEO slugs remain clear and usable
  - sampled body localization quality is now materially stronger, with Russian corrected from the weakest state and German/French/Italian cleaned to a more native trade-content tone

Russian-language review follow-up under the updated terminology rule:

- Rechecked additional `ru` samples after confirming that core PCB/PCBA industry terminology should remain in English where that is natural for the trade.
- Under this revised standard, English specialist terms such as `assembly`, `stackup`, `via`, `reflow`, `underfill`, `DFM`, `X-Ray`, `signal integrity`, and related packaging/manufacturing vocabulary were no longer treated as defects by themselves.
- The remaining issue definition for `ru` became narrower:
  - unnatural sentence flow
  - overly dense English phrase stacking
  - passages that still read like direct engineering-source translation rather than Russian trade content

Russian-focused sampling result:

- `ru/mixed-signal-pcb-layout.md` and `ru/pcb-thermal-reliability-stackup.md` were considered broadly usable under the updated standard.
- `ru/chiplet-bridge-pcb-assembly.md`, `ru/wearable-patch-pcb-quality.md`, and `ru/ai-server-motherboard-reliability.md` still showed the most obvious translated-syntax feel and were selected for another cleanup pass.

Russian second-pass cleanup completed:

- Cleaned `ru/chiplet-bridge-pcb-assembly.md` again to improve Russian sentence flow while preserving packaging/manufacturing English terminology that is natural for the sector.
- Cleaned `ru/wearable-patch-pcb-quality.md` again to reduce translated phrasing and make the wearable-medical manufacturing narrative read more naturally in Russian without forcing full term translation.
- Cleaned `ru/ai-server-motherboard-reliability.md` again to improve readability and reduce source-language syntax while preserving accepted server/PCB engineering terminology.

Updated Russian QA position:

- Under the clarified rule for PCB/PCBA terminology, the remaining Russian set is now materially closer to publishable B2B engineering content.
- Future Russian review should continue to target sentence naturalness first, not term-by-term de-Englishing.

Additional Russian sampling and cleanup:

- Reviewed another `ru` sample set under the same terminology rule:
  - `ru/48v-12v-power-board-design.md`
  - `ru/bidirectional-dc-dc-converter-pcb.md`
  - `ru/ethercat-interface-pcb-prototype.md`
  - `ru/mmwave-antenna-array-pcb.md`
  - `ru/qsfp-dd-module-pcb-compliance.md`
- Assessment from this pass:
  - `ru/48v-12v-power-board-design.md` and `ru/bidirectional-dc-dc-converter-pcb.md` were broadly usable and did not require another immediate cleanup pass.
  - `ru/ethercat-interface-pcb-prototype.md`, `ru/mmwave-antenna-array-pcb.md`, and `ru/qsfp-dd-module-pcb-compliance.md` still carried moderate translated-syntax density even though the specialist terminology itself was acceptable.

Targeted Russian cleanup completed on that sample set:

- Refined `ru/ethercat-interface-pcb-prototype.md` to improve sentence naturalness and reduce awkward translated phrasing while preserving accepted industrial-control terminology.
- Refined `ru/mmwave-antenna-array-pcb.md` to improve Russian flow in RF/manufacturing sections without removing natural industry English terms.
- Refined `ru/qsfp-dd-module-pcb-compliance.md` to make the optical-module manufacturing narrative read more naturally in Russian while keeping normal high-speed and assembly terminology.

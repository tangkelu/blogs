# P4-40 2025-11-10 EMS / Electronics / RF / Tools Official-Source Recovery Scout

Date: 2026-04-28
Model: `gpt-5.4`
Input inventory: `/code/blogs/tmps/2025.11.10/en`
Lane: official-source recovery scout for EMS, electronics basics, CAM / PCB tools, RF antenna / cable / ferrite, colored solder mask, and Taiwan-electronics drafts
Output ownership: only this file

## Scope

This lane treats all `tmps/2025.11.10/en` drafts as claim inventory only, not as authority.

It does not update trackers, facts, wiki pages, source registries, or reusable knowledge files.

It identifies:

- existing `llm_wiki` support already usable for conservative reuse
- blocked claim classes that still require official sources or dated capability records
- official-source candidates worth recovering next

It does not promote draft-originated numeric, capability, certification, supplier, price, lead-time, MOQ, yield, quality-rate, RF/electrical/thermal performance, legal/IP, ranking, or market-share claims.

## Drafts Inspected

- `buying‑pcb.md`
- `cam‑files.md`
- `pcb‑design‑tools.md`
- `electronics-assembly.md`
- `ems-manufacturing-worldwide.md`
- `taiwan-electronics.md`
- `purple-pcb.md`
- `rf-antenna.md`
- `radio-frequency-cable.md`
- `ferrite-bead.md`
- `ohms-law.md`
- `watts‑to‐amps.md`
- `schematic-symbols.md`
- `encoder‑circuit.md`
- `pcb-video-card.md`
- `electronic-devices.md`

## Lane Status

Overall lane status: `completed_at_claim_family_level`

The batch is deletion-safe as topic and claim-family inventory, but support remains mixed:

- `source_backed_fact_layer_partial` for PCBA / assembly workflow, CAM package vocabulary, RF execution boundaries, and some high-speed material context
- `blocked_pending_official_source` for general electronics education, PCB-tool comparisons, color-specific solder-mask behavior, RF cable / ferrite explainer claims, schematic-symbol standards details, and EMS-company ranking claims
- `blocked_pending_dated_capability_record` for any HIL / supplier / manufacturer-specific capability, quality, lead-time, MOQ, certification, or service-performance assertions

## Claim-Family Status By Draft

| Draft | Status | Safe reuse classes | Blocked classes |
| --- | --- | --- | --- |
| `buying‑pcb.md` | `source_backed_fact_layer_partial` | file-package completeness, BOM / sourcing review, DFM / test-planning workflow, prototype-to-volume routing posture | lead time, MOQ, shipping, customs, supplier quality outcomes, certifications as supplier proof |
| `cam‑files.md` | `source_backed_fact_layer_partial` | Gerber / drill / BOM / pick-and-place / panelization as manufacturing-package vocabulary | universal tolerances, exact format-support breadth, CAM-engineer correction depth, yield / efficiency gains |
| `pcb‑design‑tools.md` | `blocked_pending_official_source` | only draft-level topic inventory today | comparative rankings, cost / licensing generalizations, feature superiority, “best for” assertions |
| `electronics-assembly.md` | `source_backed_fact_layer_partial` | SMT / THT / mixed-technology flow, layered inspection stack, ICT vs FCT boundary, NPI-to-volume gating | process windows, throughput, placement accuracy, sector qualification, reliability outcomes |
| `ems-manufacturing-worldwide.md` | `blocked_pending_official_source` | EMS scope vocabulary and assembly-service taxonomy | leading-company lists, global rankings, market position, scale claims, sector dominance, current capability claims |
| `taiwan-electronics.md` | `blocked_pending_official_source` | only high-level supplier-category inventory | market share, advanced-node dominance, “largest” or “top” claims, current customer lists, current product leadership |
| `purple-pcb.md` | `blocked_pending_official_source` | solder-mask exists as process layer; finish / mask / color topic intent only | color-specific inspection, RF, optical, thermal, reliability, compliance, or performance claims |
| `rf-antenna.md` | `source_backed_fact_layer_partial` | antenna-feed-network / RF-execution boundary, validation-planning posture | gain, directivity, VSWR targets, return-loss performance, bandwidth, polarization, antenna-type performance comparisons |
| `radio-frequency-cable.md` | `blocked_pending_official_source` | cable / connector / impedance topic inventory only | universal 50-ohm / 75-ohm application rules, attenuation claims, manufacturer-sourcing claims, custom-cable service claims |
| `ferrite-bead.md` | `blocked_pending_official_source` | EMI-noise-suppression topic inventory only | universal placement rules, circuit-effect claims, standards-compliance claims, impedance-selection rules |
| `ohms-law.md` | `blocked_pending_official_source` | broad educational topic inventory only | historical / derivation detail, non-ohmic taxonomy, AC impedance transition, power-law expansion unless sourced |
| `watts‑to‐amps.md` | `blocked_pending_official_source` | formula-topic inventory only | PCB trace / thermal / manufacturability consequences stated as standards-backed without source pack |
| `schematic-symbols.md` | `blocked_pending_official_source` | standards-family inventory only | exact symbol-standard scope, universal reading conventions, CAD-tool recommendations |
| `encoder‑circuit.md` | `blocked_pending_official_source` | logic-topic inventory only | truth-table exemplars as authoritative pedagogy, IC recommendations, absolute / incremental-mechanical encoder mixing |
| `pcb-video-card.md` | `source_backed_fact_layer_partial` | high-speed material family context, multilayer / SI / PI / thermal topic inventory | GPU stackup counts, layer recipes, impedance numerics, power ranges, VRM phases, material fit-for-GPU claims |
| `electronic-devices.md` | `blocked_pending_official_source` | broad topic inventory only | device-history timeline, category completeness, societal-impact framing, manufacturing-process sequence as authoritative |

## Existing `llm_wiki` Support Found, With IDs And Paths

### PCBA / EMS / Electronics Assembly

- `topic_id: processes-pcba-npi-to-mass-production-flow`
  - Path: `/code/blogs/llm_wiki/wiki/processes/pcba-npi-to-mass-production-flow.md`
- `topic_id: testing-pcba-quality-gates-and-test-strategy`
  - Path: `/code/blogs/llm_wiki/wiki/testing/pcba-quality-gates-and-test-strategy.md`
- `fact_id: methods-pcba-layered-inspection-stack`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-layered-inspection-stack.md`
- `fact_id: methods-pcba-ict-vs-fct-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-ict-vs-fct-boundary.md`
- `fact_id: methods-pcba-bom-sourcing-and-traceability-posture`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-bom-sourcing-and-traceability-posture.md`
- `fact_id: methods-pcba-cable-harness-and-ic-programming-integration`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-cable-harness-and-ic-programming-integration.md`
- `fact_id: methods-pcba-test-method-input-package-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-test-method-input-package-boundary.md`
- `source_id: frontendapt-pcba-turnkey-assembly-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-turnkey-assembly-page-en.md`
- `source_id: frontendhil-turnkey-assembly-product-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-turnkey-assembly-product-page-en.md`

These support conservative workflow framing for `electronics-assembly.md`, parts of `buying‑pcb.md`, and the non-ranking parts of `ems-manufacturing-worldwide.md`.

### CAM / PCB File Package / DFM Intake

- `topic_id: processes-advanced-pcb-fabrication-and-stackup-planning`
  - Path: `/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `topic_id: processes-apt-resource-layer-for-dfm-faq-and-download-retrieval`
  - Path: `/code/blogs/llm_wiki/wiki/processes/apt-resource-layer-for-dfm-faq-and-download-retrieval.md`
- `fact_id: methods-pcba-test-method-input-package-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/pcba-test-method-input-package-boundary.md`
- `source_id: frontendapt-pcb-pcb-fabrication-process-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-pcb-fabrication-process-page-en.md`
- `source_id: frontendapt-dfm-guidelines-resource-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-dfm-guidelines-resource-page-en.md`
- Prior scout:
  - `/code/blogs/llm_wiki/logs/p4-39-2025-07-13-tools-cam-via-official-source-recovery-scout.md`

These support guarded statements that fabrication / assembly review needs Gerber, drill, stackup, BOM, and pick-and-place context, but they do not support broad format-superiority or CAM-performance claims.

### RF Antenna / RF Execution Boundary

- `topic_id: testing-rf-validation-and-test-coverage`
  - Path: `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`
- `topic_id: processes-5g-telecom-pcb-execution-boundary-map`
  - Path: `/code/blogs/llm_wiki/wiki/processes/5g-telecom-pcb-execution-boundary-map.md`
- `fact_id: methods-antenna-system-feed-network-vs-performance-boundary`
  - Path: `/code/blogs/llm_wiki/facts/methods/antenna-system-feed-network-vs-performance-boundary.md`
- `source_id: frontendapt-antenna-pcb-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-antenna-pcb-page-en.md`
- `source_id: frontendapt-high-frequency-pcb-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-high-frequency-pcb-page-en.md`
- Prior scouts:
  - `/code/blogs/llm_wiki/logs/p4-36-2025-8-30-rf-microwave-official-source-recovery-scout.md`
  - `/code/blogs/llm_wiki/logs/p4-37-2025-8-12-rf-high-speed-official-source-recovery-scout.md`

These support feed-network, launch, shielding, validation, and board-execution framing only. They do not support antenna-performance writing.

### High-Speed Material Context Relevant To `pcb-video-card.md`

- `topic_id: materials-high-speed-material-family-selection`
  - Path: `/code/blogs/llm_wiki/wiki/materials/high-speed-material-family-selection.md`
- `fact_id: materials-panasonic-megtron-6`
  - Path: `/code/blogs/llm_wiki/facts/materials/panasonic-megtron-6.md`
- `fact_id: materials-isola-tachyon-100g`
  - Path: `/code/blogs/llm_wiki/facts/materials/isola-tachyon-100g.md`
- `fact_id: materials-isola-i-tera-mt40`
  - Path: `/code/blogs/llm_wiki/facts/materials/isola-i-tera-mt40.md`
- `source_id: isola-tachyon-100g-datasheet`
  - Path: `/code/blogs/llm_wiki/sources/registry/materials/isola-tachyon-100g-datasheet.md`
- `source_id: frontendapt-materials-megtron-pcb-page-en`
  - Path: `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-megtron-pcb-page-en.md`

These can support cautious material-family references only. They do not justify GPU-board stackup recipes or performance outcomes.

### Color / Procurement Boundary Already Learned Elsewhere

- Prior scout:
  - `/code/blogs/llm_wiki/logs/p4-38-2025-10-13-commercial-fr4-procurement-official-source-recovery-scout.md`
- Prior ingestion map:
  - `/code/blogs/llm_wiki/logs/p4-34-2025-10-13-commercial-procurement-blog-ingestion-map.md`

These already establish that color-specific solder-mask and procurement claims remain blocked without official source packs.

## Safe Reuse Classes

The following classes are reusable now if the wording stays conservative and source-scoped:

- PCBA workflow structure:
  - SMT, THT, mixed-technology flow
  - DFM / DFA / DFT gating
  - SPI / AOI / X-ray / ICT / FCT as distinct layers
- Turnkey assembly posture:
  - BOM review, lifecycle review, sourcing, traceability, box-build handoff
- Fabrication-package framing:
  - Gerber, drill, stackup, BOM, pick-and-place, test-objective packaging
- RF board-execution framing:
  - feed-network review, launch / grounding / shielding / validation planning
- High-speed material-family mentions:
  - Megtron / Tachyon / I-Tera MT40 only as source-scoped material context
- Color / procurement drafts:
  - demand inventory only, not technical or commercial reuse

## Blocked Claim Classes

### Blocked Pending Official Source

- PCB-tool rankings, “best tool” recommendations, pricing, licensing, and feature comparisons
- general electronics-education claims for Ohm’s law, watts-to-amps, encoder circuits, schematic-symbol standards, and device history
- RF cable identity, attenuation, connector-family, and impedance-selection guidance
- ferrite-bead usage, impedance-vs-frequency interpretation, placement, and selection guidance
- color-specific purple-solder-mask optical, RF, thermal, AOI, branding-effectiveness, or compliance claims
- EMS-company lists, global rankings, “largest” / “leading” / “top” language, and Taiwan supplier market-share claims
- video-card-specific GPU power, stackup, SI / PI / thermal numerics and material-fit claims

### Blocked Pending Dated Capability Record

- any HIL / APT / supplier-specific assembly capability, test coverage, lead-time, MOQ, quality rate, certifications, or worldwide-service claims
- any procurement or logistics claim such as customs handling, shipping speed, current stock, or supplier responsiveness
- any current company-status claim for Taiwan suppliers or EMS vendors unless tied to dated investor / annual-report material

## Official Sources Checked Or Recommended Next

### Strong Candidates For Immediate Recovery

#### CAM / File-Format / PCB-Data Exchange

- `Ucamco Gerber official format pages`
  - URL: `https://www.ucamco.com/en/gerber`
  - URL: `https://www.ucamco.com/en/gerber/downloads`
  - Why next:
    - strongest primary source for Gerber identity, layer / attribute / job-file vocabulary, and official specification ownership
    - useful for `cam‑files.md` and `buying‑pcb.md`
- `IPC-DPMX / IPC-2581 Consortium`
  - URL: `https://www.ipc2581.com/`
  - URL: `https://www.ipc2581.com/about/`
  - Why next:
    - official consortium anchor for IPC-2581 as design-to-fabrication / assembly data-exchange standard
    - useful for `cam‑files.md`

#### PCB Design Tools

- `KiCad official site and 3D viewer pages`
  - URL: `https://www.kicad.org/`
  - URL: `https://www.kicad.org/discover/3dviewer/`
  - Why next:
    - clean official support for schematic capture, PCB layout, integrated SPICE, and 3D viewer
- `Altium official schematic / 3D pages`
  - URL: `https://www.altium.com/altium-designer/features/schematic-capture`
  - URL: `https://www.altium.com/documentation/altium-designer/pcb-3d-view`
  - Why next:
    - usable for official feature descriptions without relying on reseller or review content

These can support feature identity only. They cannot support neutral “best tool” rankings by themselves.

#### Ferrite Beads

- `Murata official ferrite-bead FAQ and EMC guidance`
  - URL: `https://www.murata.com/en-us/support/faqs/emc/emifil/char/0004`
  - URL: `https://www.murata.com/support/faqs/emc/emifil/char/0001`
  - URL: `https://www.murata.com/products/emc/emifil/library/knowhow/basic/s2-chapter02-p1`
  - Why next:
    - supports vendor-scoped impedance-at-100-MHz vocabulary, placement-next-to-noise-source guidance, and selection context

#### RF Cable / RF Connector / 50-ohm vs 75-ohm Context

- `TE Connectivity RF connector pages`
  - URL: `https://www.te.com/en/product-CAT-884-SMBM50.html`
  - Why next:
    - official product-level proof that RF connector families may be offered in 50-ohm and 75-ohm impedance variants
- `Keysight return-loss / VSWR documentation`
  - URL: `https://helpfiles.keysight.com/csg/e5080a/freqoffset/return_loss_and_vswr.htm`
  - Why next:
    - official measurement-vocabulary support for return loss and VSWR, useful for blocking overclaim in `rf-antenna.md`

These do not yet create a full neutral RF-cable explainer pack. A broader cable-source lane still needs stronger cable-manufacturer pages.

#### Schematic Symbols / Digital Encoder Basics

- `IEC 60617 official database / store pages`
  - candidate owner: IEC
  - Why next:
    - strongest official anchor for schematic-symbol standard identity
- `IEEE 315 official metadata pages`
  - candidate owner: IEEE
  - Why next:
    - secondary standard anchor for symbol-standards framing
- `Texas Instruments priority encoder datasheet`
  - candidate owner: TI
  - candidate family: `SN74LS148` / modern equivalent
  - Why next:
    - official device-level identity for priority-encoder IC examples

#### Taiwan Electronics / EMS Company Profiles

Recover from official investor-relations or annual-report pages only:

- TSMC
- ASE Technology
- Foxconn / Hon Hai
- MediaTek
- Yageo
- Walsin
- Delta Electronics
- Unimicron
- Kinpo

Why next:

- these can support company identity, headquarters, official business scope, and dated self-description
- they should not be converted into supplier rankings or market-share generalizations without separate official annual-report evidence

### Lower Priority Or Still Weak

- `Ohm’s law` and `watts-to-amps`
  - no strong local support found yet
  - these likely need a dedicated official education-source lane such as NIST / DOE / university primary references before reuse
- `electronic-devices.md`
  - too broad for one recovery move; should be split into narrower families instead of sourcing as one page

## Residual Source Gaps

- no neutral official-source pack yet for PCB-tool comparison writing
- no official solder-mask color pack yet for purple-specific technical claims
- no complete official-source pack yet for generic RF cable types and selection guidance
- no local fact layer yet for Ohm’s law, watts-to-amps, schematic symbols, or encoder-circuit educational writing
- no dated official pack yet for EMS “leading companies worldwide” lists or Taiwan supplier ranking claims
- no official-source pack yet for GPU / video-card PCB architecture claims

## Recommended Follow-On Recovery Order

1. `cam‑files.md`
   - recover `Ucamco` and `IPC-2581` first
2. `pcb‑design‑tools.md`
   - recover `KiCad` and `Altium` feature-identity pages
3. `ferrite-bead.md`
   - recover `Murata` FAQ / know-how pages
4. `rf-antenna.md` and `radio-frequency-cable.md`
   - recover `Keysight` measurement vocabulary plus stronger cable-manufacturer pages
5. `schematic-symbols.md` and `encoder‑circuit.md`
   - recover `IEC`, `IEEE`, and `TI` anchors
6. `taiwan-electronics.md` and `ems-manufacturing-worldwide.md`
   - recover only company-official IR / annual-report identity pages, not rankings
7. `purple-pcb.md`
   - recover official solder-mask vendor materials before any color-specific claim reuse

## Final Disposition

This lane is complete as a recovery scout only.

No draft-originated facts were promoted.

No trackers, facts, wiki pages, source registries, or unrelated files were edited.

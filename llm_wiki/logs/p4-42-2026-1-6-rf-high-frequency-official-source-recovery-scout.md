---
lane: "P4-42 official-source recovery scout"
input_dir: "/code/blogs/tmps/2026.1.6/en"
output_file: "/code/blogs/llm_wiki/logs/p4-42-2026-1-6-rf-high-frequency-official-source-recovery-scout.md"
status: "source_backed_fact_layer_partial"
checked_at: "2026-04-28"
model: "gpt-5.4"
scope_notes:
  - "tmps drafts treated as claim inventory, not authority"
  - "no tracker updates"
  - "no fact card or wiki edits in this lane"
---

# Purpose

Deletion-safe scout log for the RF / high-frequency / microwave / controlled-impedance batch under `/code/blogs/tmps/2026.1.6/en`.

This lane only inventories claims, checks existing `llm_wiki` support, separates source-backed support from internal-only support, and identifies blocked recovery lanes.

# Input File Inventory

- `controlled-impedance-high-frequency-pcb.md`
- `high-frequency-circuit-board.md`
- `high-frequency-multilayer-pcb.md`
- `high-frequency-pcb-assembly.md`
- `high-frequency-pcb-fabrication.md`
- `high-frequency-pcb-manufacturer.md`
- `high-frequency-pcb-manufacturing.md`
- `high-frequency-printed-circuit-board.md`
- `high-speed-high-frequency-pcb.md`
- `low-loss-high-frequency-pcb.md`
- `microwave-pcb-manufacturing.md`
- `microwave-printed-circuit-board.md`
- `microwave-rf-pcb.md`
- `radio-frequency-pcb.md`
- `rf-circuit-board-manufacturing.md`
- `rf-high-frequency-pcb.md`
- `rf-microwave-pcb.md`
- `rf-pcb-assembly-service.md`
- `rf-pcb-fabrication.md`
- `rf-printed-circuit-board.md`

# Draft Topic / Claim Family Inventory

## Family A: definitions and scope framing

Files:

- `high-frequency-circuit-board.md`
- `radio-frequency-pcb.md`
- `high-speed-high-frequency-pcb.md`
- `rf-high-frequency-pcb.md`
- `rf-microwave-pcb.md`
- `microwave-rf-pcb.md`

Observed draft intent:

- distinguish RF vs microwave vs high-frequency vs high-speed
- explain transmission-line behavior, loss, and material-selection logic
- position common structures such as microstrip, stripline, and CPW

Disposition:

- `completed_at_claim_family_level`
- Existing standards and material support allow guarded vocabulary reuse.
- Broad explanatory numerics, band cutoffs, and performance conclusions remain blocked unless attached to official sources with conditions.

## Family B: controlled impedance and transmission-line control

Files:

- `controlled-impedance-high-frequency-pcb.md`
- `high-frequency-printed-circuit-board.md`
- `high-frequency-multilayer-pcb.md`
- `rf-printed-circuit-board.md`
- `rf-pcb-fabrication.md`

Observed draft intent:

- controlled-impedance design and verification
- transmission-line structures
- impedance factors and tolerance control
- via-transition and stackup effects

Disposition:

- `source_backed_fact_layer_partial`
- Existing `llm_wiki` support is strong on method identity and guarded verification posture.
- Supplier-specific tolerance bands, percent coverage, coupon policy, and universal “precision RF” language remain blocked pending dated capability records or stronger official sources.

## Family C: RF / microwave material selection

Files:

- `low-loss-high-frequency-pcb.md`
- `microwave-printed-circuit-board.md`
- `high-frequency-circuit-board.md`
- `high-frequency-pcb-manufacturing.md`
- `rf-high-frequency-pcb.md`
- `rf-microwave-pcb.md`
- `microwave-rf-pcb.md`

Observed draft intent:

- low-loss laminate positioning
- PTFE / Rogers / ceramic-filled PTFE / LCP examples
- Dk / Df framing
- analog-RF vs high-speed-digital material comparisons

Disposition:

- `source_backed_fact_layer_partial`
- There is real official-source support for selected materials and PTFE-family processing boundaries.
- Draft-originated material rankings, generic “best for frequency X” mappings, and vendor-family generalizations are still blocked unless each claim is product-scoped and source-backed.

## Family D: fabrication and manufacturability

Files:

- `high-frequency-pcb-fabrication.md`
- `high-frequency-pcb-manufacturing.md`
- `rf-circuit-board-manufacturing.md`
- `microwave-pcb-manufacturing.md`
- `rf-pcb-fabrication.md`

Observed draft intent:

- material preparation
- lamination and registration control
- PTFE drilling and plasma treatment
- special equipment and environmental-control framing

Disposition:

- `source_backed_fact_layer_partial`
- Manufacturability framing and PTFE-processing boundaries are partially supported.
- Equipment fleets, process-window values, trace/gap limits, registration achievements, and environmental-control promises remain blocked pending dated capability records.

## Family E: RF validation and test

Files:

- `rf-high-frequency-pcb.md`
- `rf-pcb-fabrication.md`
- `high-frequency-pcb-manufacturer.md`
- `high-frequency-pcb-assembly.md`
- `rf-pcb-assembly-service.md`

Observed draft intent:

- validated frequency performance
- TDR / VNA / impedance coupon language
- assembly-side test and verification

Disposition:

- `source_backed_fact_layer_partial`
- Public method anchors and test-boundary cards exist.
- Exact frequency ceilings, report depth, S-parameter scope, and “validated RF performance” claims remain blocked pending official instrument/procedure sources plus dated supplier capability records.

## Family F: PCBA assembly and post-fabrication boundaries

Files:

- `high-frequency-pcb-assembly.md`
- `rf-pcb-assembly-service.md`

Observed draft intent:

- RF component placement and soldering discipline
- shield-can assembly
- wire bonding and die attach
- final electrical / functional verification

Disposition:

- `completed_at_claim_family_level`
- Generic PCBA test-stack boundaries are supported.
- RF-specific assembly capability, wire-bonding availability, die-attach scope, placement-accuracy numbers, and post-assembly RF outcome claims are blocked pending dated capability records.

# Existing llm_wiki Support Checked

## Existing wiki support

- `/code/blogs/llm_wiki/wiki/processes/hybrid-rf-stackup-strategy.md`
- `/code/blogs/llm_wiki/wiki/processes/ptfe-processing-and-manufacturability.md`
- `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`

## Existing fact support

- `/code/blogs/llm_wiki/facts/materials/rogers-ro3000-processing.md`
- `/code/blogs/llm_wiki/facts/materials/rogers-ro4003c-vs-ro4350b-vs-ro3003.md`
- `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `/code/blogs/llm_wiki/facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/spi-aoi-ict-boundaries.md`

## Existing source registry support: official or standards-side

- `/code/blogs/llm_wiki/sources/registry/standards/ipc-4103b-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-6018d-toc.md`
- `/code/blogs/llm_wiki/sources/registry/standards/ipc-tm650-2557a-tdr-characteristic-impedance.md`
- `/code/blogs/llm_wiki/sources/registry/materials/rogers-ro3010-product-page.md`
- `/code/blogs/llm_wiki/sources/registry/materials/isola-i-speed-datasheet.md`
- `/code/blogs/llm_wiki/sources/registry/materials/agc-tlx-8-datasheet.md`
- `/code/blogs/llm_wiki/sources/registry/materials/agc-tly-5a-datasheet.md`
- `/code/blogs/llm_wiki/sources/registry/materials/agc-meteorwave-2000-datasheet.md`
- `/code/blogs/llm_wiki/sources/registry/materials/agc-n4000-13si-datasheet.md`
- `/code/blogs/llm_wiki/sources/registry/materials/panasonic-megtron-6-model-r5775n.md`

## Existing source registry support: internal-only support

- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-high-frequency-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-teflon-pcb-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-rogers-pcb-manufacturing-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendhil-high-speed-product-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcb-drilling-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-flying-probe-testing-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-fct-test-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-aoi-inspection-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-x-ray-inspection-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-box-build-assembly-page-en.md`
- `/code/blogs/llm_wiki/sources/registry/internal/frontendapt-pcba-harness-assembly-page-en.md`

# Safe Reuse Classes

These are the classes that can be reused conservatively from existing support without treating the drafts as authority.

- standards metadata only:
  `IPC-4103` as high-speed / high-frequency base-material scope anchor; `IPC-6018` as high-frequency / microwave printed-board scope anchor
- method identity only:
  `IPC-TM-650 2.5.5.7A` for TDR characteristic-impedance method identity
- guarded measurement boundary:
  `TDR`, frequency-domain loss measurement, `VNA`, `S-parameter`, and `OTA` belong to different evidence layers and should not be collapsed into one generic test claim
- guarded material-family framing:
  PTFE-family processing differs from generic FR-4 handling; Rogers thermoset vs PTFE-family distinctions can be stated where directly source-backed
- guarded hybrid-stackup framing:
  hybrid RF stackups are a manufacturability and cost/performance tradeoff, not automatic performance proof
- guarded PCBA test-stack framing:
  SPI, AOI, ICT, flying probe, FCT, and X-ray cover different stages and defect classes
- guarded assembly boundary:
  PCBA inspection and electrical / functional verification do not prove RF channel performance by themselves

# Blocked Claim Classes

These classes should not be promoted from the drafts into facts or confident article language from current support alone.

- exact frequency-band capabilities, ceilings, or validated operating bands
- generic “works to X GHz” laminate claims without exact product datasheets and conditions
- Dk / Df values not tied to exact product, test method, and frequency condition
- blanket statements that PTFE, Rogers, AGC, or “low-loss” materials are inherently required for a given application
- controlled-impedance tolerance promises, percent-TDR coverage, coupon policy, or yield statements framed as universal capability
- manufacturing limits for trace width, spacing, registration, cavity depth, residual stub, drill oversize, or lamination window
- equipment inventory, clean-room / environmental-control assertions, or special-process availability claims without dated capability records
- supplier certifications, approvals, audit status, or qualification claims
- lead times, pricing, MOQs, quality rates, yields, and defect-rate claims
- RF-specific PCBA capability claims around wire bonding, die attach, shield-can process control, placement-accuracy numerics, and final RF validation packages
- legal or IP conclusions about material trademarks, compatibility, or equivalent substitutions

# Per-Claim-Family Recovery Status

## RF / high-frequency terminology and standards anchor

Status:

- `source_backed_fact_layer_partial`

What is already supported:

- high-frequency / microwave printed-board scope metadata via IPC public TOC anchors
- guarded separation of board-level measurement methods

What is still blocked:

- hard frequency cut lines between RF, microwave, mmWave, and high-speed that are presented as universal engineering facts

## Controlled impedance and verification posture

Status:

- `source_backed_fact_layer_partial`

What is already supported:

- TDR method identity from IPC
- internal posture that controlled impedance is paired with verification, not only design intent

What is still blocked:

- factory-wide tolerance commitments
- “100% TDR” or equivalent scope promises as public fact
- article-level acceptance thresholds

## PTFE / Rogers / AGC / low-loss material selection

Status:

- `source_backed_fact_layer_partial`

What is already supported:

- selected Rogers official material and processing facts
- selected AGC and Isola product-scoped datasheet support
- PTFE-family processing boundary

What is still blocked:

- broad vendor-family rankings and substitute logic
- unsupported extrapolation from one laminate grade to an entire vendor family
- application-band recommendations not tied to a product-scoped official source

## RF fabrication workflow

Status:

- `source_backed_fact_layer_partial`

What is already supported:

- guarded PTFE-processing and hybrid-stackup workflow framing
- drilling / backdrill / cavity as controlled manufacturability topics in internal support

What is still blocked:

- dimensional-control numbers
- process windows
- “advanced equipment” or “special environment” claims as external truth

## RF validation and test

Status:

- `source_backed_fact_layer_partial`

What is already supported:

- method separation across inspection, impedance, and RF measurement layers
- public method anchors for TDR and high-frequency loss / propagation measurement

What is still blocked:

- exact VNA frequency range, de-embedding practice, fixture scope, report package, and guaranteed RF coverage
- any statement that OTA, chamber, or VNA vocabulary proves bare-board or supplier RF qualification

## RF PCBA assembly boundaries

Status:

- `blocked_pending_dated_capability_record`

What is already supported:

- generic PCBA test-layer separation and functional-test language
- box-build / harness / FCT / flying-probe scope boundaries

What is still blocked:

- RF-specific assembly execution, wire bonding, die attach, shielding detail, and post-assembly RF validation capability

# Official-Source Gaps

The strongest remaining gaps for this batch are:

- missing official source set for broad RF laminate comparison beyond the currently covered Rogers / AGC / Isola slices
- missing official source coverage for Taconic and other PTFE-family examples explicitly implied by drafts
- missing official-source-backed fact layer for microstrip / stripline / CPW structure guidance in a PCB-specific context
- missing official-source-backed fact layer for RF assembly boundaries such as wire bonding and die attach
- missing dated supplier capability records for exact impedance tolerances, TDR coverage scope, VNA scope, cavity / backdrill limits, and RF-specific assembly services
- missing explicit official support for LCP and ceramic-filled-PTFE claim families referenced by drafts

# Recommended Next Recovery Lanes

## Lane 1: official material-source expansion

Priority: high

Targets:

- additional Rogers product pages and datasheets for the exact grades most likely to recur in drafts
- official Taconic product pages / datasheets
- official AGC product pages for RF / microwave PTFE families not yet covered
- official source set for any LCP or ceramic-filled-PTFE examples intended for reuse

Goal:

- replace family-level draft material talk with product-scoped, conditioned source-backed facts

## Lane 2: controlled-impedance and RF measurement boundary strengthening

Priority: high

Targets:

- additional official IPC / vendor method anchors for frequency-domain board measurement, when publicly accessible
- instrument-vendor help or application pages clarifying VNA / S-parameter / TDR boundary language

Goal:

- strengthen safe method vocabulary while keeping supplier-capability claims blocked

## Lane 3: dated capability record request for supplier-specific RF claims

Priority: high

Targets:

- impedance tolerance bands
- TDR coverage policy
- VNA availability and scope
- PTFE / cavity / backdrill dimensional limits
- RF-specific assembly operations such as wire bonding, die attach, shield-can handling

Goal:

- move blocked supplier-specific claims from `blocked_pending_dated_capability_record` toward reusable internal fact cards

## Lane 4: RF structure and design-boundary source recovery

Priority: medium

Targets:

- official sources suitable for guarded explanations of microstrip, stripline, CPW, insertion loss, and return-loss vocabulary without turning them into supplier promises

Goal:

- reduce reliance on draft-originated explanatory content in structure-heavy articles

# Lane Outcome

- The batch is not fully learned.
- Current status is `source_backed_fact_layer_partial`.
- Multiple claim families are only safely reusable at boundary or vocabulary level.
- RF PCBA assembly claims remain `blocked_pending_dated_capability_record`.
- No trackers, source registries, fact cards, wiki pages, or tmps files were edited in this lane.

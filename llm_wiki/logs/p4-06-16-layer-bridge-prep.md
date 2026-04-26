# P4-06 16-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note prepares the current `16-layer` layer-count blog for second-wave `P4-06` evidence-pack use.

It does not:

- rewrite the blog
- approve heavy-copper, power-distribution, or thermal-process numerics
- unlock high-numeric-density reuse

Its purpose is to define the narrowest governed bridge posture for future prompt execution against:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/16-layer-pcb-manufacturing.md`

## Template Choice

Default template choice:

- `prompts_template/shared/query.md`

Required supporting templates:

- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/hilpcb/query-overlay.md`

Reason:

- `16-layer` is the middle branch in the second safe bridge wave
- the current page behaves like an engineering/manufacturing decision page, not a stable pillar
- its densest unsupported leakage comes from `B` fabrication-capability tables plus `D/E/F` PDN, thermal, and process-window numerics

## Scope

In scope for this prep note:

- the current blog at `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/16-layer-pcb-manufacturing.md`
- second-wave conservative bridge preparation only
- fact / source selection that can survive evidence-pack traceability rules today
- section-by-section keep / downgrade / exclude guidance for future prompt execution

Out of scope:

- heavy-copper capability recovery
- power-distribution or PDN numeric recovery
- lamination-process-window recovery
- standards or reliability threshold recovery
- service / delivery / turnaround refresh work

## Conservative Readiness Verdict

`16-layer` is suitable for `second-wave conservative bridge-prep` after strong pruning of power, thermal, process, and service numerics.

It is not suitable for high-numeric-density evidence-pack use.

Current posture:

- bridge-prep verdict: `allowed with heavy pruning`
- readiness verdict: remains `mostly_ready` for conservative rewriting only
- primary blocker classes: `B` fabrication-capability numerics plus `D/E/F` power, thermal, and process numerics

## Allowed Claim Classes

Allowed in the usable evidence pack:

- `A` material and thermal-platform numerics when tied to exact official material/product anchors
- non-numeric power-distribution planning posture
- non-numeric thermal-platform selection posture
- non-numeric multilayer manufacturability and validation posture
- architecture examples when clearly framed as representative, not prescriptive

Allowed only as downgraded wording, not as retained numerics:

- multi-rail / high-current pressure as design-context language
- representative stackup examples as illustration only
- impedance and high-speed references as planning context, not as guaranteed output

## Excluded Claim Classes

Do not allow these into the usable pack:

- `B` fabrication capability numerics such as copper-weight windows, split-plane rules, current-density thresholds, plating build allowances, etch / resin-fill windows, service banners, or tolerance claims
- `C` standards / qualification / acceptance numerics such as `IPC-A-600 Class 3`, cycle counts, or testing counts used as acceptance proof
- `D` PDN / SI / thermal interpretation numerics such as decoupling values, via inductance ranges, thermal-via counts, impedance tables, or board-level current / voltage heuristics
- `E` lamination-process-window numerics such as temperature ramps, pressure ranges, press times, and percentage modifiers
- `F` dynamic commercial numerics such as `7-day` prototypes or service-level claims
- `G` unsupported contextual numerics functioning as hidden capability proof

Specific exclusions from the current blog:

- `0.5oz to 4oz`
- `±8%`
- `10+ voltage domains`, `8-12 rails`, `12+ rails`
- `50-200A`
- `50mil`, `20mil`, `15mil`, `>20A`, `30-60A`, `<15A/mm²`, `<30A/mm²`
- `17.5μm` to `140μm`
- `3mil` to `8mil`
- `50-60%`
- `100-470μF`, `1-10μF`, `10-100nF`
- `0.5-1nH`, `500MHz`, `1.5-3Ω`
- `1.5-2.0°C/min`, `2.5-3.0°C/min`
- `350-500 PSI`, `300-400 PSI`
- `120-150 minutes`, `90 minutes`
- `4mil` to `3-3.5mil`
- `85Ω`, `90Ω`, `100Ω`, `50Ω`
- `7-day`
- `100%`

## Must-Refresh Handling

Future prompt execution must mark `must_refresh: true` for any item that depends on:

- live service positioning
- lead time
- internal capability banners
- current qualification or delivery posture

Default bridge rule:

- if a claim depends on service, turnaround, or capability refresh and no governed `fact_id` plus stable `source_id` exists, exclude it from the usable pack

## Candidate `fact_id` Set

Primary candidate facts for a conservative pack:

- `materials-high-speed-digital-material-ladder-normalization`
- `materials-panasonic-megtron-6`
- `materials-panasonic-megtron-7`
- `materials-panasonic-megtron-8`
- `materials-isola-i-tera-mt40`
- `materials-isola-astra-mt77`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-high-layer-rigid-board-manufacturability-context`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-advanced-validation-scope-segmentation`
- `methods-high-speed-interface-system-context`

Usable as wiki/topic notes, not atomic facts:

- `processes-advanced-pcb-fabrication-and-stackup-planning`
- `materials-ceramic-aln-ims-thermal-platforms`
- `testing-validation-ladder-from-e-test-to-si-verification`

## Candidate `source_id` Set

Primary candidate source IDs for the conservative pack:

- `panasonic-megtron-6-model-r5775n`
- `panasonic-megtron-6-datasheet`
- `panasonic-megtron-7-model-r5785n`
- `panasonic-megtron-7-series-page`
- `panasonic-megtron-8-series-page`
- `isola-i-tera-mt40-datasheet`
- `isola-astra-mt77-datasheet`
- `isola-astra-mt77-dk-df-table`
- `frontendapt-pcb-high-thermal-pcb-page-en`
- `frontendhil-high-thermal-pcb-product-page-en`
- `frontendapt-pcb-heavy-copper-pcb-page-en`
- `frontendhil-heavy-copper-pcb-product-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendhil-high-speed-product-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendhil-multilayer-pcb-product-page-en`
- `pcisig-pcie-4-faq`
- `pcisig-pcie-5-faq`
- `oif-cei-112g-page`
- `te-112g-portfolio-solutions`

## Section-By-Section Bridge Guidance

### 1. Intro, banner, and capability framing

Allow:

- `16-layer` as a board class where power distribution, thermal planning, and high-speed routing become more tightly coupled
- qualitative framing around denser power and signal planning

Exclude:

- `0.5oz to 4oz`
- `±8%`
- `7-day`
- `100%` testing as a reusable banner

### 2. Why 16 layers are used

Allow:

- the non-numeric point that many rails, dense interconnects, and thermal constraints push designs upward in layer count
- representative multi-domain design pressure

Exclude:

- current-load thresholds
- rail-count thresholds
- performance or turnaround numerics

### 3. Power-distribution and stackup sections

Allow:

- power-plane segmentation and return-path planning as workflow posture
- representative stackup examples only as non-default illustrations

Exclude:

- current-density rules
- split-plane gap numbers
- embedded-capacitance values
- any stackup recipe table treated as a reusable default

### 4. Heavy-copper and process sections

Allow:

- the statement that copper weight affects routing, etch, lamination, and thermal tradeoffs
- heavy-copper as a separate process branch

Exclude:

- copper-weight windows
- plating build allowances
- etch-compensation ranges
- resin-fill / balance percentages
- process ramp / pressure / time tables

### 5. Thermal management sections

Allow:

- thermal platform selection posture
- the distinction between standard rigid boards and specialized thermal platforms

Exclude:

- thermal-via count rules
- inductance values
- resistance values
- power-dissipation thresholds treated as transferable board rules

### 6. High-speed and impedance sections

Allow:

- impedance control as planning plus verification
- high-speed interface references as ecosystem context only

Exclude:

- `85Ω`, `90Ω`, `100Ω`, `50Ω` target tables used as universal manufacturing outputs
- width/spacing implication tables
- `PCIe Gen 4/5`, `25GbE`, or `112G` numbers used as direct board-proof

### 7. Verification, standards, and close

Allow:

- the general point that complex builds need stronger review and validation workflows

Exclude:

- TDR structure counts
- cycle counts
- `IPC-A-600 Class 3`
- all service-level / turnaround numerics

## Open Gaps That Stay Controlled

- heavy-copper, plating, etch, resin-fill, and process-window numerics remain `needs_source`
- PDN / thermal / SI heuristic numerics remain downgraded or excluded
- standards and reliability threshold numerics remain blocked
- service and delivery numerics remain excluded

## Stop Conditions

Do not assemble a future `16-layer` evidence pack if any of the following remain true:

- power or thermal design heuristics are still written as transferable numeric rules
- heavy-copper process tables are still present
- internal capability / service banners still survive in the usable pack
- standards or cycle-count language is being used as quality proof

## Current Decision

`16-layer` may enter second-wave `P4-06` evidence-pack assembly only under:

- strict separation between thermal / power posture and process-capability numerics
- strict removal of heavy-copper and lamination-process tables
- strict removal of service, standards, and board-level PDN / SI numerics

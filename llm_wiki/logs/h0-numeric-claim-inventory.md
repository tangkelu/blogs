# H0 Numeric Claim Inventory

Date: 2026-04-25

## Purpose

This file is the first execution output of the high-numeric-density program.

It converts the 10 layer-count blogs under `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en` from prose assets into a numeric-claim inventory.

The goal is not to judge writing quality.

The goal is to classify every meaningful numeric claim cluster so later workstreams can decide whether each claim should be:

- kept
- downgraded
- deleted
- or sourced through a future recovery batch

## Claim Classes

- `A`: material datasheet numerics
- `B`: fabrication capability numerics
- `C`: standards / qualification / acceptance numerics
- `D`: high-speed / channel / interconnect numerics
- `E`: reliability / build-up / HDI numerics
- `F`: dynamic commercial numerics
- `G`: other numeric context

## Disposition Labels

- `keep`: already close to sourceable under current or near-term policy
- `downgrade`: numeric idea may remain only after rewriting into non-numeric or softer language
- `delete`: should be removed from future high-density evidence packs
- `needs_source`: can remain only if a later workstream lands suitable primary sources

## Inventory Status

- `6-layer`: completed
- `8-layer`: completed
- `10-layer`: completed
- `12-layer`: completed
- `14-layer`: completed
- `16-layer`: completed
- `18-layer`: completed
- `20-layer`: completed
- `22-layer`: completed
- `24-layer`: completed

## Per-Blog Inventory

### 6-Layer PCB Manufacturing

- `B` capability cluster: `±8%` impedance, `3/3mil`, `100% electrical testing`
  - disposition: `needs_source`
  - reason: internal capability numerics need a dated capability layer
- `F` commercial uplift cluster: `30-40%` cost increase from `4` to `6` layers
  - disposition: `delete`
  - reason: dynamic commercial number
- `A` FR-4 property cluster: `Tg`, `Dk/Df`, operating temperature, halogen thresholds
  - disposition: `keep`
  - reason: material-grade numbers are recoverable from official product sources
- `E` reflow / thermal-use limits: `2+` reflows, `260°C`, operating-temperature limits
  - disposition: `downgrade`
  - reason: should not remain as hard transferable reliability thresholds without tighter sources
- `B` stack-up recipe cluster: copper weights, dielectric windows, layer-by-layer thickness assumptions
  - disposition: `needs_source`
  - reason: these are fabrication recipe numbers, not generic material facts
- `D` impedance geometry and embedded-capacitance numbers: `50Ω/100Ω`, width tables, `200-400 pF/cm²`
  - disposition: `delete`
  - reason: unsupported board-interpretation numerics
- `A` RF / hybrid material property cluster: Rogers / Megtron / PTFE `Dk/Df`, frequency windows
  - disposition: `keep`
  - reason: sourceable if tied to official laminate datasheets
- `A` metal-core thermal-property cluster: conductivity, base thickness, thermal-drop comparisons
  - disposition: `keep`
  - reason: material/metal constants are recoverable from official product data
- `E` flex / rigid-flex numeric cluster: thickness, bend life, bend radius, transition accuracy
  - disposition: `downgrade`
  - reason: mixed material, process, and reliability numbers should be softened
- `B` via-rule and tolerance clusters: aspect ratio, annular ring, TDR coupon counts
  - disposition: `needs_source`
  - reason: capability-governance layer not yet built

### 8-Layer PCB Manufacturing

- `B` capability cluster: `±8%` and optional `±5%` impedance
  - disposition: `needs_source`
  - reason: current capability numerics need governed backing
- `D` EMC / shielding performance cluster: `10dB`, `6-12dB`
  - disposition: `delete`
  - reason: system-level performance claims are not reusable generic facts
- `F` cost uplift cluster: `25-35%`
  - disposition: `delete`
  - reason: dynamic commercial number
- `A` board-thickness and FR-4 / low-loss material property cluster
  - disposition: `keep`
  - reason: largely material-selection numerics
- `E` process modification cluster: halogen-free lamination `5-10%`, rigid-flex bend/process rules
  - disposition: `downgrade`
  - reason: process-window numbers should not be kept as hard guidance
- `B/E/F` HDI / via / cost cluster: blind-via diameters, aspect ratios, pitch windows, cost adders
  - disposition: `needs_source`
  - reason: mixes capability, HDI, and commercial numerics
- `B/C` lamination / warpage / bow-twist cluster
  - disposition: `needs_source`
  - reason: includes standards-style thresholds and process capability
- `D` interface target table: `90Ω`, `100Ω`, `85Ω`, `50Ω`
  - disposition: `downgrade`
  - reason: may remain only as typical interface context, not manufacturing promise
- `B/C` testing / tolerance / plating cluster
  - disposition: `needs_source`
  - reason: combines capability and standards/acceptance numerics
- `B/D` DFM checklist numbers: copper balance, backdrill frequency threshold, spacing rules
  - disposition: `needs_source`
  - reason: these need a future capability or high-speed interpretation layer

### 10-Layer PCB Manufacturing

- `B` capability cluster: `1+8+1`, `2+6+2`, `0.1mm` blind vias, `±50μm`, `±8%`
  - disposition: `needs_source`
  - reason: explicit capability numerics are not yet governed
- `E` device-density / packaging cluster: pin counts, BGA pitches, plane-count pressure
  - disposition: `downgrade`
  - reason: useful context, but too generalized to retain as hard thresholds
- `F` cost clusters: `20-30%`, `15-30%`, sequential-lamination cost adders
  - disposition: `delete`
  - reason: dynamic commercial numbers
- `E` microvia / HDI process geometry cluster
  - disposition: `needs_source`
  - reason: core blocked class for high-density readiness
- `E` via-structure taxonomy cluster: `1+N+1`, `1+8+1`, `2+6+2`
  - disposition: `downgrade`
  - reason: safe as architecture vocabulary, not prescriptive numeric default
- `E` BGA escape routing recipe tables
  - disposition: `delete`
  - reason: highly specific HDI numeric recipes are unsupported
- `A` FR-4 / low-loss material property cluster
  - disposition: `keep`
  - reason: strongest sourceable numeric layer
- `A/D` RF material constants plus derived geometry implication
  - disposition: `downgrade`
  - reason: keep material constants; drop derived board-geometry outcomes
- `B/E` registration / annular ring / copper-balance clusters
  - disposition: `needs_source`
  - reason: capability-governance layer still missing

### 12-Layer PCB Manufacturing

- `B` capability and QA banner: `±8mil` back-drill depth, `±8%` impedance, `5ps` skew matching, `20GHz` VNA
  - disposition: `needs_source`
  - reason: These are fabricator capability and test claims that need a dated governed source layer.
- `D` interface and board-context cluster: `DDR4/DDR5 3200-6400 MT/s`, `PCIe Gen 3/4/5`, `10 Gigabit Ethernet`, `USB 3.x/USB4`, `HDMI 2.1`, `DisplayPort 2.0`
  - disposition: `downgrade`
  - reason: These are ecosystem context numerics, not safe board-level guarantees.
- `D` back-drilling threshold cluster: `2.0mm+`, stub effects above `3GHz`
  - disposition: `delete`
  - reason: This is an unsupported SI threshold claim for article-grade reuse.
- `B` layer-count and stack-up planning cluster: `6` signal layers, `3-4` power planes, `1.6-2.4mm` thickness, `2.0mm` common
  - disposition: `needs_source`
  - reason: These are fabrication-planning numerics rather than stable material facts.
- `D` DDR geometry and matching tables: `±5mil`, `±25mil`, `±10mil`, `80Ω`, `40Ω/80Ω`, `±10%`, `±8%`
  - disposition: `delete`
  - reason: This is unsupported board-level interconnect budget content.
- `B` DDR manufacturability geometry cluster: `4mil` dielectric, `3.5-4.0mil` trace width, `3.5mil/5mil`, `0.5oz/1oz`, `+5-8μm`
  - disposition: `needs_source`
  - reason: These are fabrication geometry and process numbers that need primary support.
- `D` DDR5 training / timing margin cluster: `±1 UI`, `±150ps`, `±0.5mil`, `2-inch`, `±0.1%`
  - disposition: `delete`
  - reason: Timing-budget and training-range numerics are unsupported as static facts.
- `A` material speed-grade table: `≤5 Gbps`, `5-10 Gbps`, `10-25 Gbps`, `>25 Gbps`, `Dk 4.2-4.5 / 3.8-4.0 / 3.3-3.7 / 3.2-3.4`, `Df 0.020-0.025 / 0.005-0.012 / 0.002-0.006 / 0.001-0.002`
  - disposition: `keep`
  - reason: Material-property numerics remain the strongest supported class when tied to official product sources.
- `F` hybrid-material savings claim: `40-50%`
  - disposition: `delete`
  - reason: Cost-reduction percentages are dynamic commercial numerics.
- `E` HDI / rigid-flex construction cluster: `1+10+1`, `0.5mm` pitch BGA escape, `12R-4F`, `4` flex layers, `8` rigid layers
  - disposition: `downgrade`
  - reason: These are architecture examples, not prescriptive defaults.
- `B` fabrication / test workflow cluster: `3-5` drill programs, `≤4` hole sizes, `>10Gbps` VNA use, `20GHz` VNA, thickness `±10%` or `±8%`
  - disposition: `needs_source`
  - reason: This mixes process capability and verification numerics that need governed backing.
- `B` DFM rule cluster: `±5mil` matching, back-drill above `5Gbps`, spread glass above `10Gbps`, `±15%` copper balance, `50mil`, `≤10:1`, `0.2mm`
  - disposition: `needs_source`
  - reason: These fabrication-rule numerics need stronger source control.
- `C` standards / quality / production cluster: `IPC-A-600 Class 3`, `100%` electrical testing, `5-day` prototype, `15-day` production
  - disposition: `needs_source`
  - reason: Standards-style quality framing and turnaround numerics are not safe as unsupported static claims.

### 14-Layer PCB Manufacturing

- `B` capability and compliance banner: `14 layer`, `IPC-6013 Type 3/4`, `controlled impedance`, `dynamic flex`
  - disposition: `needs_source`
  - reason: This is a direct fabrication capability and compliance claim cluster.
- `E` rigid stack-up and lamination process cluster: `6` cores, `5` prepreg layers, `2.0-2.5mm`, `90-120 minutes`, `10-12` inner layers, `1-2` buildup layers per side
  - disposition: `downgrade`
  - reason: These are useful as examples, but they read like universal defaults.
- `C` registration and annular-ring threshold cluster: `±4mil`, `±2mil`, `Class 2 = 1mil`, `Class 3 = 2mil`, `8mil`, `0.3mm` to `0.5mm`
  - disposition: `delete`
  - reason: This is standards-threshold content masquerading as general guidance.
- `E` rigid-flex architecture cluster: `14R-4F`, asymmetric `8/6`, more than `4` flex conductors
  - disposition: `downgrade`
  - reason: These are configuration examples only.
- `A` polyimide material options: `12.5-75μm`, `12.5-50μm`, `>300°C`, `25-75μm`
  - disposition: `needs_source`
  - reason: These should come from official material datasheets.
- `B` polyimide drilling / adhesion / coverlay cluster: `20-30%` slower feed, `100,000+ RPM`, `2-3 lb/in`, `8+ lb/in`, `6-8 lb/in`, `12.5-25μm + 12.5-25μm`
  - disposition: `needs_source`
  - reason: These are fabrication-process and adhesion numerics.
- `B` transition-zone machining cluster: `±4mil`, `3-5mm`
  - disposition: `needs_source`
  - reason: This is a fabrication capability tolerance cluster.
- `E` bend-radius and flex-life table: `6×`, `12×`, `20-25×`, `1-100 cycles`, `>100,000 cycles`, `0.3mm`, `1.8mm`, `6-7.5mm`
  - disposition: `needs_source`
  - reason: This is a reliability-rule cluster with explicit thresholds.
- `B` flex copper-pattern and material-performance cluster: `10mil`, `30mil`, `30-40%`, `Tg 170-180°C`, `Df 0.005 / 0.002`, `5-10×`, `0.5oz / 0.25oz`
  - disposition: `needs_source`
  - reason: This mixes material numerics with board-level performance claims.
- `B` via geometry and aspect-ratio cluster: `2.0-2.4mm`, `10:1`, `0.20-0.24mm`, `L1-L2`, `L13-L14`
  - disposition: `needs_source`
  - reason: These are fabrication geometry numerics.
- `B` DFM numeric rules cluster: `≥1mm`, `±15%`, `7+`, `4-5`, `≤4`, `±3mil / ±2mil`
  - disposition: `needs_source`
  - reason: This is a dense fabrication-rule bundle.
- `B` closing capability / quality / commercial cluster: `4` flex layers, `>100,000` cycles, `±4mil`, `3/3mil`, `2.5/2.5mil`, `288°C, 6 cycles`, `7 business days`
  - disposition: `needs_source`
  - reason: This combines capability claims, qualification numerics, and dynamic lead-time numbers.
- `C` main blocker: standards threshold leakage from registration and annular-ring sections
  - disposition: `delete`
  - reason: `Class 2 / Class 3` thresholds are unsupported without controlled sources.
- `B` main blocker: unsupported fabrication capability numerics in capability, Z-routing, fine-feature, and via-geometry sections
  - disposition: `needs_source`
  - reason: These need a dated capability source layer.
- `E` main blocker: flex-life and bend-radius tables use explicit reliability thresholds without source control
  - disposition: `needs_source`
  - reason: These numbers are not safe as article-grade evidence without primary engineering sources.
- `F` main blocker: dynamic commercial numerics such as `7 business days`
  - disposition: `delete`
  - reason: Lead-time numerics are dynamic commercial facts.

### 16-Layer PCB Manufacturing

- `B` capability and service numerics: `0.5oz to 4oz`, `±8%`, `10+ voltage domains`, `7-day` prototypes, `100%` electrical testing
  - disposition: `needs_source`
  - reason: These are current fabricator capability and delivery claims.
- `F` power-domain and current-load framing: `50-200A`, `8-12` rails, `12+` rails, `5-6` dedicated power planes versus `2-3` at `12` layers
  - disposition: `downgrade`
  - reason: These are design-scenario numerics rather than universal thresholds.
- `F` representative 16-layer power stack-up table: `0.5oz/1oz/2oz`, `L1-L16`, `2-3mil`, `200-400pF/cm²`, `500MHz`
  - disposition: `downgrade`
  - reason: The stack-up is illustrative and depends on exact pressed geometry.
- `B` split-plane and current-density DFM rules: `50mil`, `20mil`, `15mil`, `>20A`, `30-60A`, `<15A/mm²`, `<30A/mm²`, `20-50mil`
  - disposition: `needs_source`
  - reason: These are hard layout-control limits and need stronger support.
- `B` heavy-copper etch and resin-fill table: `17.5μm` to `140μm`, `3mil` to `8mil`, `~12μm/side` to `~45μm/side`, `50-60%`
  - disposition: `needs_source`
  - reason: This is a fabrication-capability table.
- `D` decoupling / via inductance / thermal-via numerics: `100-470μF`, `1-10μF`, `10-100nF`, `25mm`, `10mm`, `4-8 vias`, `2 vias`, `0.5-1nH`, `500MHz`, `1.5-3Ω`, `0.3mm`, `1.0-1.2mm`, `>10W`
  - disposition: `downgrade`
  - reason: These are board-level PDN and thermal heuristics.
- `A` material-property numerics: `385 W/mK`, `0.3 W/mK`, `~1000×`, `Tg ≥170°C`
  - disposition: `downgrade`
  - reason: The conductivity and Tg values are material-grade numerics, but the cluster mixes in commercial guidance.
- `B` lamination-process adjustment numerics: `1.5-2.0°C/min`, `2.5-3.0°C/min`, `350-500 PSI`, `300-400 PSI`, `120-150 minutes`, `90 minutes`, `5-10%`
  - disposition: `needs_source`
  - reason: These are process-window numbers.
- `D` impedance and high-speed interface numerics: `4mil` to `3-3.5mil`, `5-10%`, `40Ω/80Ω`, `85Ω`, `90Ω`, `100Ω`, `50Ω`, `PCIe Gen 4/5`, `25GbE`
  - disposition: `downgrade`
  - reason: These are model-dependent examples, not universal board guarantees.
- `C` standards-style verification numerics: `2.0-2.8mm`, `6-8` TDR structures, `7-10:1`, `200+` thermal cycles, `IPC-A-600 Class 3`
  - disposition: `needs_source`
  - reason: These include test, acceptance, and reliability thresholds.
- `F` HDI and rigid-flex architecture examples: `0.5mm` pitch, `1+14+1`, `16R-4F`, `4` flex layers, `12` rigid layers
  - disposition: `keep`
  - reason: These are representative construction-pattern examples.
- `G` marketing and quality-positioning numerics: `±8%`, `2-3mil`, `0.5oz to 4oz`, `100%` testing
  - disposition: `needs_source`
  - reason: These are internal positioning claims.
- `Main blockers`: standards and reliability thresholds, fabrication-capability tables, board-level PDN/SI numerics, and dynamic commercial numerics
  - disposition: `needs_source`
  - reason: The blog still mixes all four unsupported classes.

### 18-Layer PCB Manufacturing

- `G` capability cluster: impedance tolerances, `20GHz` verification, prototype lead time, `100%` testing
  - disposition: `needs_source`
  - reason: internal capability and QA claims require governed backing
- `A` material property cluster: Rogers / PTFE / Megtron / FR-4 `Dk/Df/CTE/peel strength/frequency windows`
  - disposition: `keep`
  - reason: recoverable from official datasheets and product pages
- `B` process adjustment cluster: slower drilling, PTFE layer-count guidance
  - disposition: `downgrade`
  - reason: process heuristics are not stable generic rules
- `C` recommendation matrix: frequency-to-material target bands
  - disposition: `downgrade`
  - reason: keep only as engineering guidance, not normative fact
- `F` example stack tables
  - disposition: `keep`
  - reason: representative architecture patterns are acceptable if framed as examples
- `C` impedance geometry examples and tolerance tables
  - disposition: `downgrade` or `needs_source`
  - reason: derived SI numerics and tolerance tables remain unsupported as hard claims
- `D` reliability/validation thresholds and coupon counts
  - disposition: `needs_source`
  - reason: qualification-style numbers need stronger primary support
- `C` RF transition / anti-pad / backdrill rules and resonance/loss examples
  - disposition: `needs_source`
  - reason: board-level performance and geometry rules are not yet governed
- `E/F` heavy-copper and cost-multiplier cluster
  - disposition: `downgrade`
  - reason: mixed commercial and construction heuristics

### 20-Layer PCB Manufacturing

- `G` capability cluster: stacked microvias up to `6` layers, `2.5/2.5mil`, `200+` IST cycles
  - disposition: `needs_source`
  - reason: explicit capability and reliability claims need audited backing
- `F` architecture counts: `10+` sequential cycles, `18` full ELIC cycles, `5+10+5` hybrid
  - disposition: `keep`
  - reason: acceptable as representative architecture examples
- `B` microvia process geometry cluster: RCC thickness, via diameters, planarization, alignment, dimple values
  - disposition: `needs_source`
  - reason: precise process-control numerics remain blocked
- `A` material system requirements: Dk/Df ranges, Tg/Td, copper foil thickness, roughness
  - disposition: `needs_source`
  - reason: partly sourceable, but mixed with process-threshold content that needs separation
- `C` design-rule tables: capture pads, stack height, trace/space, registration
  - disposition: `downgrade`
  - reason: can remain only as illustrative DFM guidance unless stronger sources land
- `D` reliability thresholds: `200 / 300+` IST, `150°C`, resistance-change failure trigger, sampling rules
  - disposition: `needs_source`
  - reason: qualification/acceptance territory
- `C` registration accumulation table and capture-pad escalation
  - disposition: `downgrade`
  - reason: model-based DFM guidance, not authoritative rule
- `E/F` cost / yield / lead-time tables
  - disposition: `delete`
  - reason: unstable commercial numerics
- `G` chemistry-control and metrology numbers
  - disposition: `needs_source`
  - reason: reads as internal process capability, not reusable fact
- `F` adjacent application and packaging counts
  - disposition: `downgrade`
  - reason: keep only where they function as market/context examples

### 22-Layer PCB Manufacturing

- `E` application-environment stress ranges: `-55 to +125°C`, `10-2000Hz`, `20G random`, `-180 to +150°C`, `10-20 year`
  - disposition: `downgrade`
  - reason: These are program-context numerics, not fabrication thresholds.
- `C` IPC Class 2 vs Class 3 threshold table: `25μm vs 50μm`, `20μm vs 25μm`, `≤10% vs 0%`, `30% vs 20%`, `10s at 288°C / 1 vs 6 cycles`, `≤1.5% vs ≤0.75%`
  - disposition: `needs_source`
  - reason: This is standards-threshold content.
- `C` Class 3A / space-military addendum numerics: `100-500 thermal cycles`, `>5%`, `TML ≤1.0%`, `CVCM ≤0.10%`, `1.5μg/cm²`, `45°`
  - disposition: `needs_source`
  - reason: These are qualification thresholds that require primary standards support.
- `B` registration and annular-ring capability framing: `50μm`, `±2mil`, `±3mil`
  - disposition: `needs_source`
  - reason: This is fabrication-capability math and tolerance language.
- `A` qualified-material options table: `Tg ≥170°C`, `Tg ≥250°C`, `Df <0.005`, `Df <0.006`
  - disposition: `downgrade`
  - reason: The material-property class is close to keepable, but the cluster mixes exact products and families.
- `B` stack-up, thickness, aspect-ratio, and lamination-window guidance: `12-13 signal`, `4-5 ground`, `4-5 power`, `2.8-3.5mm`, `10:1`, `8:1 to 12:1`, `0.25-0.3mm`, `14-16 inner`, `3-4 buildup per side`, `50-100% longer`
  - disposition: `needs_source`
  - reason: These are transferable fabrication-window numerics.
- `A` extreme-environment material properties and cost uplift: `200-260°C`, `Tg >250°C`, `3-4×`, `<0.5% vs 1-2%`, `Df 0.005 at 1GHz`, `2-3oz`
  - disposition: `downgrade`
  - reason: The cluster mixes material numerics with commercial uplift and comparative claims.
- `C` coupon program and acceptance-summary numerics: `4-6`, `200-500×`, `2-4`, `8-12`, `≥25μm`, `≤20%`, `≥50μm`, `≤0.75%`, `≤1.56μg/cm²`, `288°C 6×`, `100%`
  - disposition: `needs_source`
  - reason: This combines test-program volume with acceptance thresholds.
- `B` via-design and manufacturability tables: `2.8/3.0/3.2/3.5mm`, `0.30/0.35mm`, `9.1:1 to 11.7:1`, `>10:1`, `40%`, `60-70% to 85-95%`
  - disposition: `needs_source`
  - reason: These are capability and process-performance numerics.
- `D` thermal/backdrill/high-speed design rules: `0.3mm`, `1.0-1.2mm`, `2oz vs 1oz`, `>1.5mm stub`, `below 10GHz`, `above 3Gbps`, `±8mil`
  - disposition: `needs_source`
  - reason: This is board-level interconnect guidance.
- `B` controlled-environment and SPC numerics: `Class 10,000`, `ISO 7`, `20-25°C`, `40-60% RH`, `±2σ`, `±5%`
  - disposition: `needs_source`
  - reason: Facility-control and process-monitoring numbers need authoritative backing.
- `F` commercial outcome / savings framing: `first submission`, `weeks of schedule`, `tens of thousands of dollars`
  - disposition: `delete`
  - reason: Dynamic commercial-impact numerics are out of scope.
- `Main blockers`: standards thresholds, fabrication capability, and board-level SI numerics remain unsupported
  - disposition: `needs_source`
  - reason: These are the dominant blockers to high-density reuse.

### 24-Layer PCB Manufacturing

- `A` material datasheet property anchors: `Dk 3.2-4.2`, `Df 0.001-0.020`, `Megtron 6/7`, `I-Speed`, `I-Tera MT40`
  - disposition: `downgrade`
  - reason: Official material numerics are often keepable, but this cluster is mixed with unconfirmed comparison rows.
- `F` material comparison economics and derived loss table: `~2.0/0.9/0.55/0.40 dB/inch`, `1x-6x cost factor`, `4-8 inch channels`
  - disposition: `delete`
  - reason: The cost multipliers are dynamic commercial numbers and the per-inch loss table is derived performance content.
- `D` interface-rate and channel-context numerics: `56G`, `112G`, `224G`, `32-64GT/s`, `4800-8800MT/s`, `51.2Tbps`, `400/800GbE`, `3-12 inch`, `20-40 inch`
  - disposition: `downgrade`
  - reason: These board-level combinations should be softened unless each mapping is tied to primary context.
- `B` supplier capability bundle: `±6mil`, `±5%`, `40GHz`, `24 inch x 30 inch`, `1-2 boards per panel`
  - disposition: `needs_source`
  - reason: These are shop-specific fabrication capability numbers.
- `B` via geometry and back-drill rule set: `3.0-3.5mm`, `1-3 dB`, `<=8mil`, `30-40mil`, `40-50mil`, `20mil`
  - disposition: `needs_source`
  - reason: This is a fabrication/design-rule cluster.
- `D` channel-loss budget table: `3.3 dB`, `0.5 dB`, `0.4 dB`, `1.5 dB`, `1.0 dB`, `7.2 dB`, `28-32 dB`, `5-6 dB`
  - disposition: `needs_source`
  - reason: These are board-level SI budget and compliance numbers.
- `D` glass-weave, copper-roughness, and oxide-loss numerics: `glass Dk ~6.2`, `resin ~3.0`, `1-2ps`, `3-5ps/inch`, `7-11 degrees`, `Rz 1-10um`, `+0.02 to +0.5 dB/inch`, `+0.7 to +0.9 dB`
  - disposition: `needs_source`
  - reason: The cluster combines material microstructure numerics with board-level attenuation effects.
- `E` lamination and process-recipe numerics: `2-3 press cycles`, `inner 16-20 layers`, `2-4 buildup layers per side`, `Tg >=180C`, `1.5C/min`, `90 min`, `250-300 PSI`, `350-400 PSI`
  - disposition: `needs_source`
  - reason: These are build-up and process-window numbers.
- `C` standards and acceptance thresholds: `0.75% IPC limit`, `>=25um plating`, `IPC-6012 Class 3`, `100% electrical testing`
  - disposition: `needs_source`
  - reason: Threshold-style compliance claims are not cleared for evidence-pack use.
- `G` numericized supplier assurance claims: `every production lot`, `reduce full compliance testing on every lot`, `volume production for 112G`, `tier-one OEM`
  - disposition: `needs_source`
  - reason: These numbers are wrapped into supplier-status language.
- `F` commercial throughput and scrap economics: `$300-500`, `2%`, `1,000-panel`, `$6,000-10,000`, `10 business days`, `weekly lot deliveries`
  - disposition: `delete`
  - reason: These are unstable commercial and operational numbers.
- `Main blockers`: shop capability numerics, board-level SI budgets, and standards thresholds remain the main blockers
  - disposition: `needs_source`
  - reason: These clusters cannot be kept without governed primary support.

## Early Main-Agent Notes

- Even the first quick read confirms that low-layer blogs already mix at least four claim classes: `A`, `B`, `F`, and `G`.
- `20-layer` clearly carries heavy `B`, `C`, `D`, and `E` density in addition to normal material numerics.
- The inventory should track distinct claim clusters, not every repeated number instance.
- The strongest immediate `keep` candidates remain `A` material-property numerics and some example architecture counts.
- The weakest classes remain `B` fabrication capability numerics, `C` standards thresholds, `D` board-level high-speed / validation numbers, and `E` transferable HDI / reliability thresholds.

## Cross-Blog Synthesis

- `A` material numerics are the only class with broad near-term keepability across the set, but they still need exact-product normalization.
- `B` fabrication capability numerics are the dominant blocker in `12 / 14 / 16 / 22 / 24-layer`.
- `C` standards / qualification numerics dominate `14 / 20 / 22 / 24-layer` readiness risk.
- `D` board-level high-speed / SI numerics dominate `12 / 24-layer`, and they must be treated as interpretation outputs, not default facts.
- `E` rigid-flex / HDI / build-up numerics are the second major blocker after capability and standards tables.
- `F` commercial and lead-time numbers should be stripped unless a separate refresh policy is added.

## H1 Handoff

- `H1` should focus on exact-product material recovery, not generic family prose.
- Priority batches:
  - Batch 1: mainstream FR-4 / high-Tg FR-4 exact-product cleanup
  - Batch 2: digital low-loss / very-low-loss product-grade cleanup
  - Batch 3: RF / hybrid exact-product cleanup
  - Batch 4: hi-rel / extreme-temp / special-material cleanup
  - Batch 5: build-up / flex / special-thermal boundary cleanup

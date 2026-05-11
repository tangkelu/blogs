# Purpose And Lane

- Lane: `85页 PCB设计EMC设计指导书` RF EMC and safety appendix intake
- Date: `2026-05-06`
- Model lane requested: `gpt-5.4`
- Scope: handbook claim inventory only, not authority promotion
- Output owner boundary: only this log file
- Focus slice: RF PCB EMC posture plus appendix safety spacing/current-carrying table families

## Final Status Label

`completed_at_claim_family_level`

Reason: pages `70-85` were inspected and classified, existing `llm_wiki` support was mapped, and blocked/source-gap classes were identified. No reusable `facts/`, `wiki/`, `sources/`, or tracker updates were made in this lane.

# Exact Pages Inspected

Inspected extracted handbook files:

- `pages/page-0070.txt`
- `pages/page-0071.txt`
- `pages/page-0072.txt`
- `pages/page-0073.txt`
- `pages/page-0074.txt`
- `pages/page-0075.txt`
- `pages/page-0076.txt`
- `pages/page-0077.txt`
- `pages/page-0078.txt`
- `pages/page-0079.txt`
- `pages/page-0080.txt`
- `pages/page-0081.txt`
- `pages/page-0082.txt`
- `pages/page-0083.txt`
- `pages/page-0084.txt`
- `pages/page-0085.txt`

Manifest checked:

- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/manifest.json`

Page-family notes from the inspected slice:

- `70-72`: RF material, isolation, shielding, sensitive/noisy circuit partitioning
- `73-75`: shield-wall openings, shield-cavity size logic, power/control-line filtering
- `75-77`: RF control-line filtering, grounding, via-heavy grounding posture
- `77-80`: impedance-control examples, corner handling, microstrip/coupler/power-divider/basic-element claims
- `80-81`: stripline and ground-copper adjacency posture
- `81-82`: appendix hazard and board-marking claims
- `83-84`: creepage/clearance table families
- `85`: current-carrying table family reference only

# Existing llm_wiki Support Found

## RF posture already supported at reusable boundary level

1. `wiki/processes/cavity-and-shield-feature-planning`
   - Safe for shield feature planning, cavity planning, finish-zoning adjacency, and access-review posture
   - Not safe for exact shield-can clearance, cavity geometry, plating stack, or shielding-effect numerics

2. `wiki/processes/rf-transmission-line-structure-boundaries`
   - Safe for conservative `microstrip` and `stripline` structure vocabulary
   - Safe for outer-layer vs internal-layer structure naming
   - Not safe for geometry recipes, impedance tables, spacing rules, or topology-performance rankings

3. `facts/methods/rf-front-end-low-noise-board-review-boundary`
   - Safe for partitioning, return-path continuity, shield/cavity planning, transition quality, and staged validation posture
   - Not safe for first-pass compliance claims, exact RF rules, or finished-product performance proof

4. `facts/methods/cavity-machining-capability`
   - Safe for internal capability-pattern wording that cavity/shield features belong to the RF build toolbox
   - Not safe for default applicability or exact cavity/process geometry

## Safety and current-carrying support exists only at guarded boundary level

1. `facts/methods/current-carrying-trace-width-and-copper-boundary`
   - Safe for conductor-sizing as a separate review lane after current is known
   - Not safe for universal trace-width tables, per-amp recipes, or temperature-rise thresholds

2. `wiki/processes/current-carrying-and-high-current-layout-boundaries`
   - Safe for qualitative conductor width/copper weight/planes/vias/thermal-stress review language
   - Not safe for numeric sizing tables or production guarantees

3. `wiki/applications/industrial-control-pcb-pcba-boundary-map`
   - Safe for `creepage/clearance` as design-language vocabulary only
   - Explicitly blocks exact creepage/clearance values as compliance proof

4. `policies/prompt-consumption-specification.md`
   - Board-level SI/EMC numerics are blocked class `D`
   - Capability numerics, standards numerics, and geometry recipe numerics are also blocked in downstream prompt use

# Claim Families From Pages 70-85

## RF materials and laminate positioning

- FR-4 vs RF-specialty material framing
- Named RF laminate families and dielectric-property lists
- Advice that loss and dielectric stability matter in RF selection

## Isolation and shielding posture

- In-line vs L-shape placement guidance inside a shielded cavity
- Sensitive-circuit vs strong-radiator separation
- Shielding for front ends, oscillators, PA/antenna-feed, mixed RF/IF, mixed digital/analog areas
- Fence-via / shield-wall posture
- Shield-wall slot or opening treatment for RF trace pass-through
- Shield-cavity dimension and resonance-avoidance claims

## Filtering and grounding posture

- Power-entry and staged decoupling/filtering guidance
- Filter treatment for synth data/clock/enable lines
- Large-ground-plane and local-grounding posture
- RF device grounding via-heavy posture
- Ground continuity around RF cable landing areas

## RF routing and transmission-structure claims

- Impedance-control example table
- Corner treatment rules
- Microstrip completeness rules
- Coupler and power-divider formula claims
- Microstrip equivalent-element claims
- Quarter-wave bias-line claims
- Stripline completeness rules
- Ground-copper guard trace posture beside RF signal lines

## Appendix safety and marking claims

- Hazard categories
- Safety marking durability and warning-language claims
- Fuse marking requirements
- Replaceable battery warning text

## Appendix spacing and current-carrying claims

- Input-voltage-dependent minimum creepage/clearance tables
- Line-to-protective-earth spacing tables
- Coated-board safety and material/flame rating references
- Trace-width vs current-carrying table family
- `MIL-STD-275` mention as current-table reference

# Safe Reuse Classes

These are the classes that can be reused conservatively from this lane because they match already-landed `llm_wiki` boundaries.

1. RF board-review posture
   - Sensitive vs noisy region partitioning
   - Return-path continuity and uninterrupted reference-plane posture
   - Shield/cavity planning as early design-review topics

2. RF structure vocabulary
   - `microstrip` as outer-layer transmission-line vocabulary
   - `stripline` as internal-layer transmission-line vocabulary
   - Guarded mention that RF traces may require controlled structure and validation planning

3. Shielding/cavity workflow language
   - Shield features and cavity planning belong to RF build planning
   - Access, finish, and validation need to be considered before closure around shielded regions

4. Qualitative grounding/filtering language
   - RF layouts typically pay attention to grounding continuity, local return control, decoupling, and staged filtering
   - Keep this at planning vocabulary level, not recipe level

5. Safety-distance vocabulary only
   - `creepage`, `clearance`, `isolation slot`, and safety marking language can be treated as design-review vocabulary
   - No exact distances or compliance outcomes may be reused from the handbook

6. Current-carrying review vocabulary only
   - Once current is known, conductor width, copper weight, via count, planes, and thermal stress become separate review variables
   - No table values or per-amp recipes may be reused from the handbook

# Blocked Claim Classes

These classes should remain blocked from this handbook slice unless later backed by official or governed sources.

1. Exact RF material property rows copied from the handbook
   - Includes FR-4 or named RF laminate `Er` rows and frequency-specific numeric values
   - Reason: handbook is claim inventory only; some named families also have incomplete current official recovery posture

2. Exact RF geometry and layout rules
   - `lambda/20`, `3W`, `2W`, `R>3W`, `lambda/4`, fixed gate-slot dimensions, fixed via-spacing rules
   - Reason: current `llm_wiki` RF boundary pages do not authorize reusable recipe numerics

3. Exact RF impedance-control example tables
   - Board-name-specific 50 ohm line-width examples and stackup numbers
   - Reason: blocked geometry/capability numeric class

4. Exact cavity resonance and shielding formulas
   - Shield-cavity resonance equations, dimension multipliers, and frequency-separation claims
   - Reason: not covered by current reusable official-source layer

5. Universal filter/decoupling component recipes
   - Specific capacitor value stacks and frequency cutover claims as evergreen rules
   - Reason: source layer supports qualitative EMI/filter posture, not fixed universal recipes

6. EMC or shielding effectiveness outcomes
   - Isolation dB claims, radiation-reduction claims, or any statement that a listed practice guarantees EMC success
   - Reason: board-level SI/EMC numerics are blocked class `D`

7. Exact creepage/clearance tables
   - All voltage-to-distance rows in tables 1 and 2
   - Reason: current corpus supports only vocabulary-level safety spacing language, not threshold tables or compliance proof

8. Exact current-carrying table values
   - Table 3 trace-width/current rows and any numeric derivation from `MIL-STD-275`
   - Reason: current reusable lane points to `IPC-2152` conductor-sizing identity and explicitly blocks universal numeric tables

9. Certification, compliance, pass/fail, or universal safety claims
   - Any statement that these handbook rules prove `IEC`, `UL`, EMC, or product-safety compliance
   - Reason: handbook is not authority and current `llm_wiki` safety lanes block proof claims

# Image/Table Pages That Merit Later Selective Vision Pass

Priority pages for a later selective vision or manual table-verification pass:

1. `page-0075`
   - Figure-heavy filtering example; OCR should be checked for component labels and routing order

2. `page-0079`
   - Coupler and power-divider figure; formula/label placement should be visually confirmed

3. `page-0083`
   - Table 1 creepage/clearance grid is OCR-fragile and should not be trusted without table-level verification

4. `page-0085`
   - Table 3 exists only as heading plus note in OCR; requires image/table extraction to recover whether the table is usable at all

Secondary pages worth a visual check even without manifest image assets:

- `page-0073`
  - shield-wall slot diagram and formula layout
- `page-0074`
  - cavity-dimension figure and resonance text alignment
- `page-0080`
  - microstrip basic-elements figure and quarter-wave bias example
- `page-0084`
  - Table 2 OCR should be verified alongside Table 1

# Official-Source Gaps

## RF gaps

1. Official current sources for exact RF laminate rows named in the handbook
   - Especially exact-product recovery if any handbook row is later needed externally
   - Taconic exact-product posture remains sensitive in current corpus

2. Official/public source lane for reusable RF geometry rules
   - Needed if future work wants exact spacing, bend, via-fence, or shield-opening numerics

3. Official/public source lane for shield-cavity resonance formulas and dimension guidance
   - Current local support is planning-level only

4. Official/public source lane for reusable RF filter/decoupling recipes
   - Current support is posture-level, not universal value-stack level

## Safety appendix gaps

1. Official clause-level creepage/clearance authority
   - Example recovery targets: `IEC 60664` or the relevant official safety-standard publication pages
   - Needed before any table thresholds can be promoted

2. Official clause-level equipment-safety routing for PCB safety markings and fuse labeling
   - Current corpus supports context vocabulary, not handbook-derived requirement tables

3. Official current-carrying numeric authority for table replacement
   - `IPC-2152` identity exists, but no governed reusable numeric table lane has been landed
   - Handbook `MIL-STD-275` reference is not sufficient for promotion

4. Official flame-rating/material-test anchors if appendix material-safety claims are later needed
   - Current lane did not recover authority for the handbook's recommendation-style material/test statements

# Lane Outcome

- RF EMC posture from pages `70-81` is partially supported for conservative reuse at board-review vocabulary level.
- Appendix safety spacing and current-table content from pages `81-85` is not promotable beyond vocabulary/framing without official-source recovery.
- The handbook remains a demand and claim-inventory input only.
- No edits were made outside this log file.

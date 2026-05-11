# P4-210C EMC Source Lane: Transmission Line / Via Return Path / Slot-Crossing Boundary

Date: 2026-05-06
Lane: `transmission-line / impedance / via-return-path / slot-crossing` source-first boundary intake
Controller context: `P4-209B` claim-family absorption follow-up

## Purpose

Capture a conservative, source-first intake for the handbook's `transmission-line / impedance / via-return-path / slot-crossing` slice.

This note does not promote handbook formulas, geometry numerics, EMC pass claims, or connector-specific hard rules into `llm_wiki` facts. It isolates the narrowest reusable boundary vocabulary and defines the next authority-recovery targets.

## Inputs Used

Controller and prior lane context:

- `llm_wiki/logs/p4-209-2026-5-6-emc-handbook-controller-note.md`
- `llm_wiki/logs/p4-209b-2026-5-6-emc-handbook-lane-impedance-via-slot.md`

Primary handbook extraction root:

- `tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/`

Relevant text slices inspected:

- `pages/page-0046.txt`
- `pages/page-0047.txt`
- `pages/page-0053.txt`
- `pages/page-0054.txt`
- `pages/page-0057.txt`
- `pages/page-0058.txt`
- `pages/page-0059.txt`
- `pages/page-0060.txt`
- `pages/page-0061.txt`
- `pages/page-0062.txt`
- `pages/page-0066.txt`

## Relevant Handbook Pages If Identifiable

- handbook pages `46-47`
  - transmission-line, impedance continuity, process impact, differential-impedance claim inventory
- handbook pages `53-54`
  - via model, parasitic model, TDR / field-extraction mention
- handbook pages `57-62`
  - slot creation, split-plane crossing, bridging, dense-connector opening risk, quiet-ground crossing
- handbook page `66`
  - impedance discontinuity examples such as corners, vias, connectors, and package transitions

## Safe Reusable Vocabulary And Checklist Phrasing

Smallest safe families that can be reused before authority recovery:

- `structure vocabulary`
  - `microstrip`
  - `stripline`
  - `characteristic impedance`
  - `differential impedance`
  - `reference plane`
- `continuity posture`
  - impedance work is not only geometry naming; it includes continuity across route segments and transitions
  - layer changes should be reviewed together with return-path continuity
  - connector, via, corner, package, and branch points belong to the same discontinuity-review family
- `via-transition boundary`
  - a via is not electrically invisible at higher edge rates
  - via effects should be reviewed as parasitic plus return-path-change problems, not only as drill geometry
  - reducing unnecessary layer transitions is a valid review posture
- `slot-crossing boundary`
  - avoid routing important nets across plane splits or slot-like openings when return continuity is needed
  - dense through-hole or connector fields can create opening-like return-path problems even when no intentional split was drawn
  - bridging or stitching belongs to the same mitigation family as return-path restoration
- `review questions`
  - does this route keep a continuous reference?
  - if the signal changes layer, where does the return current transfer?
  - does a connector field or clearance pattern create a slot/opening under the route?
  - is the route crossing a quiet-ground boundary, split, or shielding transition that changes the intended return path?

## What The Handbook Safely Supplies At Claim-Inventory Level

- transmission-line and impedance language is relevant and structurally useful
- impedance discontinuity is being tied to reflections, waveform disturbance, and EMC risk narratives
- via behavior is being framed through parasitic-plus-transition models
- split-plane and slot-crossing handling is correctly surfaced as a return-current problem, not only a placement problem
- connector-heavy zones are being treated as high-risk opening / discontinuity regions

## Blocked Formulas, Numeric, And Universal Claims

Do not promote any of the following from this lane:

- handbook impedance formulas, odd/even-mode formulas, or geometry equations
- handbook numeric impedance windows, matching values, reflection values, or delay values
- handbook via parasitic defaults such as simplified `1 pF` / `6-7 ohm` style examples
- handbook frequency thresholds such as `below 1 GHz` or other regime split claims
- handbook universal statements that `stripline is always better`, `one via is negligible`, `differential routing always suppresses EMI`, or `slot crossing always fails`
- handbook connector-family specifics, hard-metric examples, or backplane pin-field recommendations
- handbook EMC-effectiveness claims attached to one routing choice without refreshed authority
- any claim that these pages prove compliance, acceptance, or guaranteed signal integrity

## Next Authoritative Source Classes To Recover

Highest-value next-recovery classes:

- public transmission-line guidance from major SI / EDA / measurement vendors
  - for safe formula framing and structure vocabulary
- authoritative via-transition and return-path guidance
  - from SI-focused vendors, EDA notes, or measurement-oriented app notes
- official/public slot-crossing and stitching-return guidance
  - enough to promote return-path restoration posture beyond today's general vocabulary-only layer
- connector-vendor or backplane-vendor guidance
  - only if exact connector-field or pin-assignment claims need promotion later
- measurement workflow sources
  - for guarded `TDR` / validation posture when discussing discontinuity verification

## Exact Selective Vision Page Candidates

Selective vision is justified only where figure structure matters more than extracted text:

- page `54`
  - via model and formula layout
- pages `57-62`
  - slot generation, return-current path, bridging, connector opening, and quiet-ground diagrams
- page `66`
  - discontinuity examples around connectors / vias / corners

Vision is not required yet for fact promotion. It is only a support step if later authority-recovery work needs figure-level disambiguation.

## Final Status

Final status: `completed_at_claim_family_level_only`

Meaning: this handbook slice is now a narrow demand map for `transmission-line / via-return-path / slot-crossing` authority recovery, but no new `facts/`, `wiki/`, or source-backed formula rules should be created from the handbook alone.
# P4-210C EMC Handbook Source Lane Log: Transmission Line / Via / Return Path / Slot Crossing

- Date: `2026-05-06`
- Model: `gpt-5.4`
- Scope: source-first claim inventory for `85页 PCB设计EMC设计指导书` focused on transmission-line, impedance, via-transition, return-path, plane-split, slot-crossing, bridge, and connector-adjacent routing boundary language.
- Source stance: handbook text is claim inventory, not authority.
- Final status label: `completed_at_claim_family_level`

## Purpose

- Capture only the reusable boundary vocabulary and workflow posture for:
  - transmission-line recognition
  - characteristic-impedance / differential-impedance vocabulary
  - via-transition and return-path continuity
  - plane split / slot crossing / bridge handling
  - connector-zone and backplane-adjacent routing caution
- Keep all exact formulas, numeric thresholds, and universal effectiveness claims blocked until recovered from official or current authoritative sources.

## Relevant handbook pages

- `page-0033` to `page-0047`
  - transmission-line definition
  - microstrip / stripline vocabulary
  - characteristic impedance, reflection, crosstalk
  - odd/even/differential impedance vocabulary
  - impedance-control posture and table-style example claims
- `page-0053` to `page-0056`
  - via model
  - via parasitic and impedance discontinuity claims
  - layer-change return-path changes
  - reduce-via posture
- `page-0057` to `page-0060`
  - slot creation
  - high-speed return-current behavior
  - split crossing risks
  - bridge handling
- `page-0061` and `page-0067`
  - connector-zone continuity
  - dense via-field / pin-field caution
  - backplane-adjacent routing and topology framing

## Safe reusable vocabulary

- `transmission line`, `microstrip`, `stripline`, `reference plane`, `return path`, `characteristic impedance`, `reflection`, `crosstalk`
- `odd-mode`, `even-mode`, `differential impedance`, `impedance discontinuity`, `layer transition`, `via transition`
- `plane split`, `slot`, `bridge`, `quiet ground`, `connector zone`, `backplane-adjacent routing`
- `keep return current continuous`, `prefer same-reference-plane transitions`, `avoid crossing splits or slots`, `treat dense connector/via regions as discontinuity risk`

## Safe checklist phrasing

- Verify whether the route remains tied to a stable reference plane.
- Check whether a layer transition changes the return-current path.
- Prefer fewer transitions and shorter discontinuity exposure.
- Avoid routing critical nets across plane splits or slots.
- If crossing is unavoidable, restore continuity with an explicit bridge or equivalent return-path support.
- Treat dense connector/via fields as a discontinuity review point.

## Blocked formulas / numeric / universal claims

- Block all handbook-origin geometry formulas and wavelength rules.
- Block all handbook-origin impedance numbers, delay numbers, and reflection/impedance deltas.
- Block all handbook-origin differential-impedance example values.
- Block all handbook-origin via-delay, via-reactance, and via-reflection estimates.
- Block all universal claims such as:
  - differential routing always suppresses common-mode noise
  - guard traces always help
  - one via is negligible in every design
  - inner layers are always superior
  - crossing a split is always harmless if the trace is short

## Next authoritative source classes to recover

- Official transmission-line / impedance references from PCB fabrication or field-app-note sources.
- Official via-transition guidance covering parasitic, stub, and return-path behavior.
- Official return-path / plane-split / slot-crossing guidance from EDA, fab, or vendor app notes.
- Connector vendor or backplane vendor documentation for pin-field, shielding, and discontinuity handling.
- If numeric reuse is later needed, recover from dated authoritative sources before promotion.

## Exact selective vision candidates

- `page-0034` to `page-0035`
  - transmission-line diagrams and formula-heavy content
- `page-0040` to `page-0042`
  - microstrip / stripline comparison and layer-priority figures
- `page-0048` to `page-0052`
  - differential-spacing and guard-trace figures
- `page-0054`
  - via model figure
- `page-0057` to `page-0060`
  - slot creation, return-current, bridge, and split-crossing figures
- `page-0061`
  - connector/pin-field and dense via-field handling

## Final status

- Claim-family intake: `completed`
- Authority promotion: `blocked`
- Reusable output: `boundary vocabulary and review posture only`

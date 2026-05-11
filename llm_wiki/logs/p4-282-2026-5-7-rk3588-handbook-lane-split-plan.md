# P4-282 RK3588 Handbook Lane Split Plan

Date: 2026-05-07
Input handbook: `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
Derived extraction root: `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书`
Execution mode: `claim_family_split_planning_only`

## Purpose

Convert the `194-page` handbook from `claim-family intake only` into a controller-ready bounded-lane split so later AI can continue learning it without rereading the full handbook as one monolith.

This file does not promote new `sources/`, `facts/`, or `wiki/`.

## Why This Split Is Needed

Current state before this log:

- the handbook is already formally inventoried in `p4-208`
- extraction is complete and page text is available locally
- the book is visibly platform-specific to `RK3588`
- pages contain both real board-review knowledge and platform-owner-specific numerics, routing defaults, and promo shell content

Without a lane split, later AI is likely to:

- overlearn Rockchip-specific numbers as reusable knowledge
- reopen the same handbook broadly instead of targeting bounded families
- confuse reusable board-review vocabulary with exact platform recipes

## Evidence Used

- `logs/p4-208-2026-5-6-pcb-handbook-intake-map.md`
- `policies/language-normalization-and-indexing.md`
- `policies/exact-data-admission-policy.md`
- extracted TOC and page samples under:
  - `pages/page-0001.txt`
  - `pages/page-0002.txt`
  - `pages/page-0003.txt`
  - `pages/page-0004.txt`
  - sampled later sections:
    - `pages/page-0010.txt`
    - `pages/page-0050.txt`
    - `pages/page-0100.txt`
    - `pages/page-0150.txt`
    - `pages/page-0190.txt`

## Proposed Bounded Lanes

### Lane `D1`: design-flow-and-placement-governance

Indicative page cluster:

- `4-36`

Primary themes:

- PCB design-flow framing
- class/rule setup
- partitioning and placement governance
- high/low-voltage separation
- review-checklist families

Safe reuse classes at this stage:

- English canonical topic naming
- claim-family inventory
- board-review and documentation-governance vocabulary

Blocked classes:

- exact spacing values
- process thresholds
- any owner-specific placement recipe presented as universal law

### Lane `D2`: stackup-impedance-and-routing-governance

Indicative page cluster:

- `11-75`

Primary themes:

- stackup family examples
- impedance discussion
- routing style and line-geometry framing
- via fanout and BGA escape
- length-matching and high-speed routing topics

Safe reuse classes at this stage:

- English canonical routing vocabulary
- claim-family inventory
- page/figure targeting for later source recovery

Blocked classes:

- exact width/spacing tables
- impedance geometry defaults
- delay and length-match numerics
- platform-specific routing recipes

### Lane `D3`: power-delivery-and-grounding-layout

Indicative page cluster:

- `76-102`

Primary themes:

- PMIC and DC-DC power-layout review
- remote feedback
- rail-specific decoupling and grounding posture
- power-via and return-path planning

Safe reuse classes at this stage:

- topology vocabulary
- review-checklist families
- local figure targeting for later bounded source recovery

Blocked classes:

- rail-specific widths
- via-count rules
- current or voltage-drop rules
- RK3588-specific power-rail prescriptions

### Lane `D4`: interface-and-memory-routing

Indicative page cluster:

- `103-164`

Primary themes:

- DDR posture and topology families
- display / camera / USB / Type-C / PCIe / SATA / Ethernet / audio / Wi-Fi-BT interface routing
- clock/reset and high-speed interface review framing

Safe reuse classes at this stage:

- interface-family topic naming
- review-boundary discovery
- claim-family inventory for later owner/source recovery

Blocked classes:

- exact DDR rules
- interface-specific tuning numbers
- exact layer/impedance defaults
- Rockchip platform-specific implementation recipes

### Lane `D5`: emc-esd-and-dfm-review-boundaries

Indicative page cluster:

- `165-188`

Primary themes:

- ESD and EMC checklist families
- PCB fabrication review
- PCBA assembly review
- DFM rule-governance framing

Safe reuse classes at this stage:

- checklist-family inventory
- boundary naming
- neutral review-vocabulary extraction

Blocked classes:

- pass/fail criteria
- standards-equivalent acceptance thresholds
- manufacturability guarantees
- platform-owner-specific DFM rules

### Appendix posture

Indicative page cluster:

- `189-190`

Controller treatment:

- `reference_or_promo_only`

Reason:

- the end matter is not a strong technical learning lane
- it should not consume bounded-lane effort

## Canonical Storage Posture

- use English-only lane naming
- keep Chinese only in provenance
- treat all handbook numerics as `secondary_pdf_claim_inventory_only` by default
- split reusable board-review vocabulary from owner-specific recipe content before any later source recovery

## Recommended Next Log Filenames

If later AI executes these lanes, prefer:

- `logs/p4-282a-2026-5-7-rk3588-handbook-lane-design-flow-and-placement-governance.md`
- `logs/p4-282b-2026-5-7-rk3588-handbook-lane-stackup-impedance-and-routing-governance.md`
- `logs/p4-282c-2026-5-7-rk3588-handbook-lane-power-delivery-and-grounding-layout.md`
- `logs/p4-282d-2026-5-7-rk3588-handbook-lane-interface-and-memory-routing.md`
- `logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`

## Current Status

- handbook extraction:
  - `completed`
- handbook claim-family intake:
  - `completed`
- bounded lane split:
  - `now_defined`
- source-backed promotion from this handbook:
  - `not_started`

## One-Sentence Resume Direction

Continue the `194-page RK3588 handbook` by executing `D1-D5` as bounded claim-family lanes, preserving English canonical naming and blocking all platform-specific numerics, formulas, thresholds, and recipe defaults unless later primary sources justify a narrower promotion.

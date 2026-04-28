# P4-20 Layer-Count Claim Coverage Map

Date: 2026-04-27

## Purpose

This map checks whether the data in the 10 English layer-count PCB manufacturing blogs is already covered by `llm_wiki` at claim-family level.

This file intentionally ignores directory names. It evaluates content-level data coverage.

## Baseline Finding

The 10 target articles are already heavily represented in existing `llm_wiki` governance artifacts, especially:

- `logs/h0-numeric-claim-inventory.md`
- `logs/layer-count-blog-readiness.md`
- `logs/en-layer-count-blog-generation-gate.md`
- `logs/h1-material-numeric-coverage-matrix.md`
- `logs/h1-material-numeric-coverage-closeout-summary.md`
- `logs/h2-capability-number-policy.md`
- `logs/h2-capability-number-inventory.md`
- `logs/p4-06-*-evidence-pack.md`
- `logs/p4-13-*-blocker-map.md`
- `facts/methods/parameter-scope-public-capability-*.md`
- `facts/materials/parameter-scope-*.md`
- `facts/methods/parameter-scope-test-inspection-*.md`

The correct conclusion is:

- content families are substantially covered for audit, downgrade, and conservative rewrite decisions
- many old-blog numeric claims are not safe reusable facts
- full absorption requires coverage/disposition mapping, not blind ingestion

## Top-Level Coverage Table

| Claim family | Coverage status | Existing support | Remaining gap |
| --- | --- | --- | --- |
| Layer-count topic structure | `covered` | `layer-count-blog-readiness`; `en-layer-count-blog-generation-gate`; `P4-06` evidence-pack drafts | high-density numeric reuse still blocked |
| Exact-product material values | `covered/source_scoped` | `H1` material matrix and closeout; Rogers, Panasonic, Isola, ITEQ, Shengyi, AGC, Ventec, Arlon cards; `P4-23` Kapton HN exact-product card; `P4-24` UPILEX-S exact-product card | generic FR-4, generic PI/UPILEX, unresolved Taconic, generic RCC/FRCC/build-up remain held; Kapton HN and UPILEX-S are product-only, not generic Kapton/PI/UPILEX |
| Material family selection | `covered_with_scope` | material ladder normalization cards; high-speed material family wiki | no flat cross-vendor ranking or mixed-condition averages |
| Public-site drilling / via / HDI parameters | `public_site_claim` | `parameter-scope-public-capability-drilling-and-via-geometry` | not dated capability proof or lot/factory guarantee |
| Public-site impedance / validation parameters | `public_site_claim` | `parameter-scope-public-capability-impedance-and-validation`; `parameter-scope-test-inspection-high-speed-si-measurement-dimensions` | not universal TDR/VNA scope, not board-pass proof |
| Construction windows and layer/thickness/copper windows | `public_site_claim` | `parameter-scope-public-capability-construction-windows` | not a normalized factory capability table |
| Capability numerics such as trace/space, drill, aspect ratio, registration, annular ring, thickness | `audited_but_blocked` | H2 bucket decisions and source maps | needs Tier 1 dated capability-source records for reusable facts |
| Stackup recipes and sequential lamination counts | `audited_but_blocked` | H2 stackup recipe/process-count bucket; 20-layer process-window boundary cards | may be architecture examples only; not process recipes |
| Backdrill / residual stub / via-stub control | `partially_covered` | backdrill posture cards; public-site scoped parameters; H2 backdrill bucket | exact reusable tolerance/frequency rules still blocked |
| BGA escape and HDI routing tables | `audited_but_blocked` | 10-layer bridge prep/evidence pack; H0 inventory | keep routing-pressure wording only; delete pitch-by-pitch rule tables unless separately sourced |
| Rigid-flex bend / transition / cycle numerics | `design_guidance_scoped_in_p4_23` | rigid-flex posture cards; 14-layer evidence pack; flex material source coverage; Minco bend-ratio design-guide scope | bend-life, transition tolerance, dynamic-flex survival, IPC acceptance thresholds, and HIL/APT capability proof remain blocked |
| IPC / Class 3 / Class 3A / acceptance thresholds | `audited_but_blocked` | standards metadata cards; 22-layer threshold-boundary cards | no threshold tables, addendum technical tables, or acceptance values unlocked |
| IST / coupon / microsection / reliability thresholds | `audited_but_blocked` | microvia reliability context; IPC TM-650 method metadata; 20-layer reliability boundary cards | no cycle thresholds, coupon plans, or pass/fail criteria unlocked |
| FAI / aerospace / medical / defense qualification workflow | `workflow_context` | FAI and aerospace quality workflow metadata; hi-rel traceability and supplier-status boundary cards | no supplier approval, release authority, qualification success, or accepted-lot proof |
| DDR / PCIe / USB4 / Ethernet / 112G / PAM4 context | `covered_as_system_context` | high-speed interface system-context card; P4-12 high-speed source records | not board-level SI budget, compliance, or fabricator capability proof |
| TDR / VNA / SI validation vocabulary | `covered_as_workflow_context` | validation ladder wiki; RF validation cards; high-speed SI measurement parameter card | exact VNA/TDR scope and pass/fail outcomes remain project-specific |
| Channel budget / insertion-loss / skew / timing tables | `audited_but_blocked` | H0 inventory; 12-layer and 24-layer evidence packs; high-speed boundary cards | needs project or primary engineering evidence; old tables should not be reused |
| Cost / yield / lead time / quick-turn | `reject_or_delete` | H0 inventory; 20-layer and 22-layer commercial boundary cards | dynamic commercial data; do not store as stable facts |

## Per-Article Coverage Summary

| Article | Coverage verdict | Main safe data | Main blocked data |
| --- | --- | --- | --- |
| `6-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | FR-4 family framing, exact material examples, RF hybrid material examples, validation posture | generic FR-4 numeric ladders, stackup recipes, impedance geometry tables, cost uplift, via/tolerance tables |
| `8-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | stackup architecture framing, material family selection, mixed-signal planning, validation workflow | EMC dB claims, cost uplift, rigid-flex mechanical numerics, standards/capability tables |
| `10-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | HDI vocabulary, BGA density pressure, architecture examples, material examples | BGA escape pitch tables, `1+8+1`/`2+6+2` as default recipes, blind-via capability, registration/cost claims |
| `12-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | high-speed system context, material speed-grade framing, validation workflow, backdrill concept | `20GHz`, `5ps`, DDR timing/routing tables, VNA/frequency commitments, turnaround claims |
| `14-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | rigid vs rigid-flex branch framing, flex material class context, transition-zone planning | IPC-6013/threshold leakage, bend-life tables, annular-ring values, flex-processing numerics |
| `16-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | power-dense stackup planning, heavy-copper workflow posture, material selection, validation workflow | PDN heuristics as hard rules, lamination windows, current-density limits, thermal/reliability thresholds, lead time |
| `18-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | RF/digital material selection, hybrid stackup patterns, PTFE/Rogers/Megtron framing, validation posture | RF geometry rules, impedance tolerance tables, cost multipliers, frequency-to-performance promises |
| `20-layer-pcb-manufacturing` | `covered_for_boundary_control_only` | any-layer/ELIC vocabulary, build-up material-form context, method/reliability workflow | HIL capability claims, stacked microvia span, process-control numerics, IST thresholds, yield/cost/lead-time |
| `22-layer-pcb-manufacturing` | `covered_for_boundary_control_only` | hi-rel workflow vocabulary, addendum hierarchy, traceability, FAI and lot-conformance context | Class 3/3A thresholds, supplier approval, compliance proof, acceptance criteria, outgassing acceptance, commercial outcome claims |
| `24-layer-pcb-manufacturing` | `substantially_covered_for_conservative_rewrite` | high-speed system context, material ladder, TDR/VNA workflow, large-panel/process-sensitivity framing | 112G channel budgets, insertion-loss tables, exact VNA scope, production proof, cost/scrap/lead-time numerics |

## Claim-Family Disposition Details

### A: Material Numeric Claims

Status: `mostly_covered/source_scoped`

Existing support:

- `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
- `facts/materials/parameter-scope-panasonic-megtron-values.md`
- `facts/materials/parameter-scope-isola-high-speed-laminate-values.md`
- `facts/materials/high-speed-digital-material-ladder-normalization.md`
- `logs/h1-material-numeric-coverage-matrix.md`
- `logs/h1-material-numeric-coverage-closeout-summary.md`

Safe use:

- exact product values with product name, condition, frequency, test method, and source attached
- family-selection wording when it does not become a flat ranking table

Blocked:

- generic FR-4 average tables
- generic rigid-flex PI/UPILEX numeric rows; `UPILEX-S` is allowed only as a UBE exact-product film example through `P4-24`
- generic Kapton/PI rows; `Kapton HN` is allowed only as a DuPont exact-product film example through `P4-23`
- generic RCC/FRCC/build-up rows
- unverified Taconic product values
- cost/performance ranking derived from material names alone

### B: Fabrication Capability Numeric Claims

Status: `audited_but_blocked`, with some `public_site_claim` scope

Existing support:

- `facts/methods/parameter-scope-public-capability-drilling-and-via-geometry.md`
- `facts/methods/parameter-scope-public-capability-impedance-and-validation.md`
- `facts/methods/parameter-scope-public-capability-construction-windows.md`
- `logs/h2-capability-number-policy.md`
- `logs/h2-capability-number-inventory.md`
- H2 bucket decision/source-map files for impedance, trace/space, drill/via, aspect ratio, backdrill, registration, board thickness, annular ring, copper weight, plating, etch compensation, standards minima, and process-window leakage

Safe use:

- public-site values only as page-scoped public claims
- workflow context for stackup planning, DFM review, coupon/TDR/VNA planning, backdrill review, high-layer registration sensitivity

Blocked:

- normalized factory capability tables
- universal trace/space, drill, registration, annular ring, impedance, or board-thickness values
- lamination recipes, bake/press windows, resin-fill windows, etch-compensation rules

### C: Standards / Qualification / Acceptance Claims

Status: `audited_but_blocked`

Existing support:

- `facts/standards/ipc-assembly-standards-metadata.md`
- `facts/standards/ipc-hdi-electrical-test-and-coating-metadata.md`
- `facts/standards/ipc-6012-addendum-program-metadata.md`
- `facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`
- `facts/standards/22-layer-clause-family-vs-threshold-boundary.md`
- `facts/standards/22-layer-hi-rel-acceptance-workflow-boundary.md`
- `facts/standards/22-layer-qualification-listing-and-release-authority-boundary.md`
- `facts/standards/22-layer-outgassing-and-screening-acceptance-boundary.md`
- `facts/standards/fai-and-aerospace-quality-workflow-metadata.md`

Safe use:

- metadata-level standard identity
- hierarchy, addendum, procurement, FAI, lot-conformance, and qualification-ecosystem vocabulary
- explicit program-sensitive workflow language

Blocked:

- threshold tables
- acceptance criteria
- sample plans
- outgassing acceptance values as universal release rules
- supplier approval, certification, qualification success, or accepted-lot claims

### D: High-Speed / SI / RF / Channel Claims

Status: `covered_as_context`, numeric budgets `audited_but_blocked`

Existing support:

- `facts/methods/high-speed-interface-system-context.md`
- `facts/methods/parameter-scope-test-inspection-high-speed-si-measurement-dimensions.md`
- `facts/methods/advanced-validation-scope-segmentation.md`
- `facts/methods/rf-validation-capability.md`
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
- `wiki/testing/rf-validation-and-test-coverage.md`
- `logs/p4-06-12-layer-evidence-pack.md`
- `logs/h3-24-layer-high-speed-execution-control-map.md`

Safe use:

- high-speed interface context as design pressure
- TDR/VNA/coupon/measurement vocabulary as workflow
- material selection as one part of SI planning

Blocked:

- channel-loss budgets
- insertion-loss tables
- skew/timing budgets
- BER/eye/jitter/pass claims
- `20GHz`, `40GHz`, `67GHz`, `112G`, or similar values as universal validation-package promises

### E: HDI / Rigid-Flex / Build-Up / Reliability Claims

Status: `partially_covered`, high-risk numerics blocked

Existing support:

- `facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `facts/methods/microvia-reliability-public-context.md`
- `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`
- `facts/methods/20-layer-process-window-and-recipe-boundary.md`
- `facts/methods/20-layer-interconnect-reliability-workflow-boundary.md`
- `facts/methods/14-layer-rigid-flex-reliability-numeric-boundary.md`
- `facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`
- `facts/materials/build-up-and-hdi-material-context-for-20-layer.md`
- `facts/materials/20-layer-build-up-material-boundary-and-non-claims.md`

Safe use:

- architecture vocabulary
- build-up material-form vocabulary
- risk and review workflow
- representative construction examples when explicitly labelled as examples

Blocked:

- stacked microvia reliability thresholds
- IST cycle thresholds
- bend-life and bend-radius tables as universal rules
- stack-height, capture-pad, via geometry, and build-up process-control tables
- HIL-specific manufacturability or production proof

### F: Commercial / Operational Claims

Status: `reject_or_delete`

Existing support:

- `logs/h0-numeric-claim-inventory.md`
- `facts/methods/20-layer-hil-production-and-lead-time-claim-boundary.md`
- `facts/standards/22-layer-supplier-status-marketing-boundary.md`

Safe use:

- quote-stage variability language
- DFM review and supplier-confirmation language
- no hard numeric reuse

Blocked:

- cost uplift percentages
- yield percentages
- scrap economics
- lead-time and quick-turn numbers
- production cadence or supplier-status marketing

## Remaining High-Value Gaps

The content set does not need broad blind ingestion. It needs selective source recovery only where the data can realistically become stable and useful.

### Agent-Audited Priority Gaps

These gaps came out of the four read-only `gpt-5.4` lane audits for materials, fabrication/process, high-speed/test, and standards/commercial claims.

| Gap | Priority | Why it matters | Intake posture |
| --- | --- | --- | --- |
| Dated internal or public capability records for HIL-specific process capabilities | `high_if_capability_tables_are_required` | Current hard fabrication numbers are mostly public-site claims or H2-governed blocked buckets | Only accept with dated scope, source owner, language, and refresh rule |
| `Shengyi S1150G` exact-product material support | `closed_in_p4_21` | Now represented by `facts/materials/shengyi-s1150g.md` and `sources/registry/materials/shengyi-s1150g-product-page.md` | Use only as exact-product halogen-free mid-`Tg` FR-4 context |
| `Isola P95` exact-product support | `closed_in_p4_21` | Now represented by `facts/materials/isola-p95-p25.md`, `isola-p95-p25-datasheet`, and `isola-p95-p25-dk-df-tables` | Use only as exact-product `P95/P25` polyimide system context |
| `IT-988SE` naming verification | `closed_as_boundary_in_p4_21` | Now represented by `facts/materials/iteq-it-988se-naming-boundary.md`; verified ITEQ rows remain `IT-988G`, `IT-988GL`, `IT-988GSE`, and `IT-988GLSE` | Keep `IT-988SE` as `needs_source`; do not infer from adjacent suffixes |
| Product-grade IMS / metal-core / thermally conductive dielectric anchors | `partially_closed_in_p4_22` | Ventec `VT-4B7`, `VT-4BC`, and `VT-4BD` are now represented as exact-product IMS material cards plus a parameter-scope card | Use only as Ventec exact-product material values; broader supplier-neutral IMS comparisons still need more sources |
| Rigid-flex bend/reliability numeric primary sources | `medium` | Current corpus supports rigid-flex posture, not bend-life/radius/transition numeric tables | Source only if future blogs need numeric rigid-flex guidance |
| DDR / PCIe / USB4 / Ethernet board-level engineering numbers | `low_to_medium` | Current support is system-context only; old blog timing/matching/geometry numbers remain blocked | Keep blocked unless a governed standards/design-guide lane is created |
| VNA/TDR measurement-scope evidence | `low_to_medium` | Current support includes page-scoped measurement terms and ranges, not universal lab commitments | Use project-specific or current service-scope evidence only |
| Licensed/customer-specific standards threshold handling | `conditional` | IPC threshold tables cannot be reconstructed from public metadata | Only needed if blogs must publish threshold tables; otherwise keep blocked |

Low-value or rejected gaps:

- cost uplift tables
- yield claims
- lead-time claims
- generic FR-4 averages
- old-blog BGA escape recipe tables
- old-blog 112G channel-budget tables

## Lane Audit Consolidation

### Materials Lane

Material values are the strongest reusable class, but only at exact-product scope.

Covered/source-scoped:

- high-Tg FR-4 examples such as `ITEQ IT-180A`, `Isola 370HR`, `Shengyi S1000-2`, and `S1000-2M`
- Panasonic `MEGTRON 4 / 6 / 7 / 8`
- Isola `I-Speed` and `I-Tera MT40`
- Rogers `RO4350B`, RO3000-family materials, and selected bondply products
- ITEQ `IT-150DA`, `IT-602G`, `IT-968`, and registered `IT-988*` exact products
- narrow Arlon / Panasonic / Rogers / AGC / Ventec exact-product rows already represented by `H1`

Partially covered or blocked:

- generic FR-4 rows remain family-governed, not one universal Dk/Df/Tg table
- generic halogen-free FR-4 process numerics remain blocked
- generic PTFE hybrid layer-count rules are not reusable facts
- generic polyimide / flex material numerics remain mostly class-level or product-exception-only; `P4-23` adds DuPont `Kapton HN` and `P4-24` adds UBE `UPILEX-S` as exact-product film anchors
- product-grade IMS / metal-core numeric anchors now have a Ventec exact-product lane through `P4-22`, but broader supplier-neutral IMS comparisons remain thin
- `Shengyi S1150G` and Isola `P95/P25` now have exact-product support through `P4-21`
- old-blog `IT-988SE` now has an explicit naming-boundary card; it remains `needs_source` rather than reusable exact-product data

### Fabrication / Process Lane

Process vocabulary is broadly covered. Exact fabrication numerics are not broadly reusable.

Covered/source-scoped or page-scoped:

- blind / buried via vocabulary
- via-in-pad / VIPPO posture
- HDI and microvia process posture
- backdrill as workflow
- impedance-with-verification as workflow
- heavy-copper and rigid-flex branch framing

Audited but blocked:

- trace/space tables such as `3/3 mil` or `2.5/2.5 mil` as transferable capability
- exact microvia top/bottom/capture-pad geometries
- aspect ratio claims such as `10:1`, `15:1`, or universal microvia `1:1`
- registration claims such as `±50 μm`, `±25 μm`, `±2 mil`
- annular-ring numbers
- board-thickness ranges and thickness tolerances
- stackup recipes, dielectric windows, copper tables, and lamination-cycle counts
- rigid-flex bend-life, transition-tolerance, dynamic-flex survival, IPC acceptance, and routing-accuracy numbers
- rigid-flex bend-ratio examples now have `P4-23` Minco design-guide scope only; they are not universal bend-radius tables or acceptance criteria

### High-Speed / Test / Validation Lane

The corpus supports context and validation vocabulary, not board-level performance numerics.

Covered/source-scoped:

- `DDR4 / DDR5`, `PCIe`, `USB4`, `Ethernet`, `56G / 112G`, and `PAM4` as ecosystem pressure
- controlled-impedance and TDR/VNA measurement vocabulary
- e-test versus TDR/VNA versus AOI/ICT evidence-layer separation
- backdrill rationale for stub-sensitive high-speed builds

Audited but blocked:

- DDR timing, training, length-matching, impedance, and geometry rules
- PCIe / USB / Ethernet pair-match and routing rules as performance proof
- insertion-loss, channel-budget, BER, eye-opening, and reach claims
- glass-weave skew-reduction numerics
- backdrill frequency triggers and residual-stub thresholds
- universal VNA/TDR frequency capability or per-order measurement promises

### Standards / Quality / Commercial Lane

Standards identity and workflow vocabulary are well covered. Direct compliance proof and thresholds are blocked.

Covered/source-scoped:

- IPC Class 2 / 3 / 3A naming and document-family identity
- IPC-6012 / IPC-6013 / IPC-A-600 hierarchy and addendum vocabulary
- IST / TM-650 / coupon / microsection method identity
- FAI and aerospace quality workflow
- outgassing / ASTM E595 / NASA screening context
- traceability, DHR, lot-history, and qualification-ecosystem vocabulary

Audited but blocked:

- IPC threshold tables
- Class 3 / 3A acceptance numerics
- coupon counts, IST cycles, and pass/fail criteria
- supplier compliance, `manufactured to`, current approval, or release-authority claims
- AS9102 execution claims without supplier-scoped evidence
- outgassing thresholds as universal bare-board acceptance

Rejected or missing:

- cost uplift
- requalification savings
- yield values
- quick-turn and lead-time claims
- schedule savings or commercial impact claims

## Next Recommended Source-Recovery Order

If the goal is to make the old blog data more reusable, the next source work should be narrow.

1. Capability evidence lane:
   Find or create dated, scoped HIL capability records for the few numbers the business truly wants to publish repeatedly. Start with `trace/space`, `drill/microvia`, `registration`, `impedance tolerance`, `board thickness`, and `backdrill/stub`.

2. Material exact-product lane:
   `P4-21` closed the first material exact-product gap set: `Shengyi S1150G` and Isola `P95/P25` are now source-scoped facts, while `IT-988SE` is explicitly blocked as an unverified old-blog name.

3. IMS / thermal platform lane:
   `P4-22` added a Ventec exact-product IMS material lane for `VT-4B7`, `VT-4BC`, and `VT-4BD`. Add non-Ventec IMS suppliers only if future drafts need supplier-neutral thermal-platform comparison tables.

4. Rigid-flex numeric lane:
   `P4-23` partially closed this lane at design-guidance scope: DuPont `Kapton HN` can be used as an exact-product polyimide film example, and Minco bend ratios can be used as source-labeled design-guide examples. `P4-24` adds UBE `UPILEX-S` as another exact-product polyimide film example. Bend-life, transition-zone tolerance, dynamic-flex guarantees, IPC acceptance thresholds, and HIL/APT capability claims still need primary or project-specific evidence.

5. Standards threshold lane:
   Do not attempt public-source reconstruction. Use licensed/customer-specific standards handling only if threshold publication is a hard requirement.

6. High-speed SI numeric lane:
   Keep board-level SI budgets blocked unless there is project-specific validation or a formally governed engineering-source lane. Current public ecosystem sources are enough for context only.

## P4-20 Completion Check

The current `P4-20` map satisfies the content-level absorption check for major claim families:

- every major data family is now mapped to a disposition
- agent lane audits confirm the same coverage boundaries independently
- the remaining work is selective source recovery, not broad ingestion

Do not interpret this completion check as a numeric unlock.

## Interim Verdict

The layer-count blog data is already mostly learned by `llm_wiki` as governed claim families.

What remains incomplete is not awareness. The remaining incomplete part is promotion:

- some claim families are known but blocked
- some are source-scoped only
- some are intentionally rejected
- only a subset is reusable as source-backed fact data

This means the correct next action is selective gap recovery, not bulk import of the old blog data.

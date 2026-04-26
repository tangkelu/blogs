# Layer-Count Blog Readiness

Date: 2026-04-26

## Purpose

This report checks whether the current `llm_wiki` corpus can support the 10 English layer-count PCB manufacturing blogs under:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en`

The goal is not to preserve every existing blog number. The goal is to decide which numeric claim classes can already be supported from `llm_wiki`, which classes still need official/vendor/standards anchors, and which claim classes should remain under gap-control instead of being copied into future evidence packs.

## Scope

- No blog body was rewritten.
- Existing blog text was treated as demand-side input only.
- Current `llm_wiki` `sources/`, `facts/`, and `wiki/` were evaluated as the support layer.
- Internal site pages remain valid for capability framing and process vocabulary, but not as final authority for datasheet-grade material parameters or revision-sensitive standards thresholds.

## Overall Verdict

Current `llm_wiki` is strong enough to support conservative engineering drafts for some layer-count topics, but it is not yet strong enough to safely reproduce the current style of these 10 blogs at full numeric density.

This report now uses two lenses:

- `conservative rewrite support`: whether `llm_wiki` can support a disciplined rewrite that removes unsafe numeric density and keeps unsupported items under gap-control
- `current draft risk`: whether the current blog body, as written today, still contains unsupported numeric, standards, or capability claims that should not be bridged directly into evidence packs

What is already relatively strong:

- high-speed multilayer laminate property cards with official datasheet anchors
- internal manufacturing workflow framing for HDI, high-layer registration, backdrill, impedance, and test coverage
- TDR / VNA / coupon / validation-ladder framing

What is still weak:

- numeric process capability tables for layer-count manufacturing
- standards-backed thresholds for acceptance / qualification / reliability language
- product-level FR-4 and broader laminate comparison coverage across the exact materials these blogs tend to cite
- interface/system-context anchors for aggressive channel-performance claims

## Per-Blog Readiness

| Blog slug | Conservative rewrite support | Current draft risk | Why |
| --- | --- | --- | --- |
| `6-layer-pcb-manufacturing` | `mostly_ready` | `high` | General stackup/process/material framing is supportable, but exact process, cost, and material-comparison numbers still need stronger sources. |
| `8-layer-pcb-manufacturing` | `mostly_ready` | `high` | Backbone is supportable, but standards thresholds and rigid-flex/mechanical numbers are still source-thin. |
| `10-layer-pcb-manufacturing` | `mostly_ready` | `high` | General multilayer, impedance, and validation posture is covered, but capability windows and cost/lead-time numbers are not. |
| `12-layer-pcb-manufacturing` | `mostly_ready` | `high` | Internal high-layer and impedance framing is good, but high-speed interface and process-tolerance numbers need stronger official anchors. |
| `14-layer-pcb-manufacturing` | `mostly_ready` | `medium` | The live draft has now been reduced to branch-level rigid-vs-rigid-flex framing, class-level material discussion, transition-zone review, and non-numeric manufacturability context, but high-density numeric readiness is still blocked because standards, rigid-flex reliability, and supplier-proof authority layers remain unavailable. |
| `16-layer-pcb-manufacturing` | `mostly_ready` | `high` | High-speed and thermal framing exists, but power/thermal outcome claims and exact process windows still need stronger evidence. |
| `18-layer-pcb-manufacturing` | `mostly_ready` | `medium` | The live draft has now been reduced to hybrid RF/digital planning context, class-level material framing, mixed-material review posture, transition planning, and workflow-level validation language, but high-density numeric readiness is still blocked because impedance, RF geometry, qualification, and supplier-proof authority layers remain unavailable. |
| `20-layer-pcb-manufacturing` | `mostly_ready` | `high` | The live draft has now been reduced to conservative HDI/build-up context, material-family framing, and workflow-level reliability language, but high-density numeric readiness is still blocked because supplier-evidence, process-window, geometry, and qualification-threshold authority layers are still missing. |
| `22-layer-pcb-manufacturing` | `mostly_ready` | `high` | The live draft has now been reduced to conservative hi-rel governance, manufacturability, and documentation context, but high-density numeric readiness is still blocked because supplier-evidence, standards-threshold, and acceptance-authority layers are still missing. |
| `24-layer-pcb-manufacturing` | `mostly_ready` | `medium` | The live draft has now been reduced to high-speed system context, stackup/material planning posture, transition and correlation-risk framing, workflow-level validation language, and large-panel process-sensitivity context, but high-density numeric readiness is still blocked because channel budgets, process-window numerics, compliance authority, and supplier-proof evidence remain unavailable. |

### High-Layer Reassessment Notes

- `18-layer` moved from the original `needs_sources` bucket to `mostly_ready` for conservative rewrites because hybrid material selection, PTFE/RF processing posture, and verification-ladder framing are now materially stronger.
- `24-layer` also moved to `mostly_ready` for conservative rewrites because `P4-12` added enough high-speed system context and broader low-loss material ladder coverage to support article structure without reproducing channel-budget tables.
- `20-layer` and `22-layer` no longer carry the same level of live draft-body overclaim density after the new `P4-13` containment pass, but both still remain blocked for high-density numeric reuse because the missing authority layers were not recovered.
- `18-layer` now also has a materially safer live draft body after the new `H3` hybrid-execution containment pass, but it still remains blocked for high-density numeric reuse because impedance, RF geometry, and supplier-proof authority were not recovered.
- `24-layer` now also has a materially safer live draft body after the new `H3` high-speed-execution containment pass, but it still remains blocked for high-density numeric reuse because channel budgets, compliance authority, and supplier-proof evidence were not recovered.
- For `20-layer`, the build-up material layer is now materially broader, but its new Panasonic / Ventec / Resonac / ABF / BT anchors are still vocabulary-safe rather than process-window-safe; they support conservative family framing, not transferable stack recipes or capability claims.
- For `20-layer`, new IPC method-governance and coupon-resource metadata plus one more Doosan build-up-material anchor improve `IST` / evaluation-workflow / multiple-lamination wording, but they still do not unlock `IST` thresholds, coupon plans, geometry tables, or factory-capability claims.
- For `20-layer`, the new official Isola sequential-lamination note adds stronger supplier-side stress-factor and failure-mode vocabulary for build-up / repeated-lamination context, but it still does not unlock lamination-count allowances, reflow-cycle numbers, or transferable reliability expectations.
- For `20-layer`, the new NASA workmanship page adds stronger public inspection / defect-criteria / interconnect-quality governance wording, but it still does not unlock bare-board acceptance criteria, `IST` thresholds, or supplier qualification claims.
- For `20-layer`, the new NASA `NEPP` program-overview record adds a clearer public `screening` / `qualification` / `test` / `reliable use` hierarchy for assurance vocabulary, but it still does not unlock PCB-specific qualification flows, coupon plans, or microvia-reliability thresholds.
- For `20-layer`, the new Mitsui engineered-materials page adds a direct official `RCC` material-form anchor, which is useful for guarded build-up vocabulary, but it still does not unlock `RCC` thickness windows, via geometry, lamination recipes, or ordinary rigid-board defaults.
- For `20-layer`, the new official IPC `TM-650 2.6.26A` / `2.6.27B` / `2.6.7.2C` method pages make `thermal cycling`, `reflow-simulation`, `thermal shock`, `continuity`, and representative-coupon wording more defensible as named official method context, but they still do not unlock cycle thresholds, coupon plans, or pass/fail criteria.
- For `20-layer`, the new official AGC `fastRise` and `Bond Plies / Prepregs` pages make `bond ply`, `nonreinforced prepreg`, `sequential lamination`, and `stacked or staggered microvias` wording more defensible as supplier-side material-form context, but they still do not unlock rigid-board defaults, lamination recipes, or microvia reliability claims.
- For `20-layer`, the new official Ventec `VT-47LT` datasheet page adds a cleaner prepreg-side anchor that explicitly groups `Any-layer HDI Designs`, `Sequential Laminations`, and `High Reliability for HDI Designs`, but it still does not unlock stack recipes, qualification evidence, or factory-capability claims.
- For `20-layer`, the new historical `IPC/JPCA-4104` TOC, official Ventec `VT-464LT RCC` page, and official `AT&S` `Anylayer` page improve legacy `HDI/microvia` taxonomy, product-grade `RCC/bondply` identity, and supplier-side any-layer architecture wording, but they still do not unlock current maintained IPC requirements, geometry tables, process-window claims, or factory-capability claims.
- For `20-layer`, the new official AGC `N7000-3F` datasheet, ITEQ `IT-602G` datasheet, and Rogers `RO4835T / RO4450T` processing guide improve product-grade material numerics and named-construction process context, but they still do not unlock generic stack recipes, capability tables, or production-readiness claims.
- For `20-layer`, the official Shengyi `S7439 / S7439B` processing guide adds one more mainstream supplier-side handling / lay-up / drilling / desmear-sensitivity anchor, but it still does not unlock transferable bake schedules, press cycles, drill tables, or capability claims.
- For `20-layer`, the official TUC `ThunderClad 5Q` product page adds one more official very-low-loss product-grade anchor with explicit `high layer count circuit board design` positioning and condition-bound values, but it still does not unlock generic stack recipes, geometry/process windows, or factory-capability claims.
- For high-speed layer-count writing, the expanded public `DDR5` release chronology plus official `OIF CEI-112G` and `TE 112G` ecosystem pages improve system-context wording around interface migration, connector / I/O pressure, and interconnect vocabulary, but they still do not unlock channel budgets, board-loss numbers, or fabricator capability claims.
- For `20-layer`, the new official IPC `QPL IPC-4101` page makes it clearer that public qualification-listing vocabulary can attach to certified base materials and listed products/sites, but it still does not unlock finished-board qualification, interconnect qualification, or customer acceptance for a `20-layer` build.
- For `20-layer`, the new official IPC `QPL IPC-4103` page makes it clearer that public qualification-listing vocabulary can also attach to high-speed/high-frequency base materials and bonding-layer products/sites, but it still does not unlock finished-board qualification, interconnect qualification, or channel-performance qualification for a `20-layer` build.
- For `20-layer`, the new NASA 2021/2022 NTRS records add clearer public vocabulary for inspection, specimen preparation, failure analysis, physics-of-failure, and mitigation thinking, but they still do not unlock qualification thresholds, coupon rules, or supplier capability claims.
- For `20-layer`, the new official `IS410` processing guide adds a clearer public mainstream rigid multilayer `laminate / prepreg` process boundary, but it still does not unlock lamination recipes, registration tolerances, or transferable process windows.
- For `20-layer`, the new AGC `Bond Plies / Prepregs` page, AGC `Meteorwave 1000NF` page, and Rogers `2929 Bondply` datasheet add a clearer public `bond ply / no-flow / unreinforced bondply` material-form boundary for high-layer constructions, but they still do not unlock build recipes, microvia-reliability proof, or factory-capability claims.
- For `20-layer`, the newer `FRCC / RCC / bond ply / controlled-flow / no-flow / ultrathin` grouping is best understood as prompt-safety tightening at the material-form boundary only; it improves supplier-page boundary control, not manufacturability proof or readiness.
- For `20-layer`, existing official Arlon `37N` / `47N` low-flow product pages slightly improve product-identity coverage under the controlled-flow branch, but only at the vocabulary boundary; they still do not unlock datasheet-grade flow, press, dielectric, or thickness facts.
- For `20-layer`, the new blocker-reduction boundary batch now splits `interconnect reliability workflow`, `process-window / recipe leakage`, and `method-versus-qualification` into separate fact cards, which makes prompt-side retrieval safer and reduces overclaim risk when the draft mentions `IST`, process sensitivity, coupons, screening, qualification, or listed materials.
- This new `20-layer` split still does not unlock `IST` thresholds, coupon plans, qualification proof, process-window numerics, stack recipes, geometry tables, or supplier/factory capability claims.
- For `20-layer`, the new geometry-containment batch now also splits `geometry / factory-capability leakage`, `build-up material pages versus feature-size authority`, and `any-layer vocabulary versus shop capability` into separate fact cards, which makes prompt-side retrieval safer when the draft tries to turn build-up vocabulary or material pages into feature-size or manufacturability proof.
- This new `20-layer` geometry split still does not unlock `trace/space`, drill/via minima, aspect-ratio numbers, registration windows, stack recipes, yield claims, or supplier/factory capability claims.
- Post-containment reassessment now shows that the remaining `20-layer` blocker is concentrated less in public-source ambiguity and more in direct HIL-specific capability / process-control / lead-time claims that still have no acceptable authority layer inside `llm_wiki`.
- For `20-layer`, the new assertion-containment batch now also splits `HIL-specific capability claims`, `HIL-specific process-control numerics`, and `HIL-specific production / lead-time claims` into separate fact cards, which makes prompt-side retrieval safer when the draft tries to turn public architecture/process vocabulary into HIL marketing proof.
- This new `20-layer` assertion split still does not unlock HIL stacked-layer-span claims, process-control numerics, yield tables, lead-time claims, or production-scale promises.
- For `22-layer`, new IPC Validation Services FAQ and Standards Gap Analysis metadata make public qualification/listing boundaries, site-specific scope, and pre-qualification assessment wording safer, but they still do not unlock certification status, supplier approval, qualification flows, or acceptance thresholds.
- For `22-layer`, the new official `QML IPC-1791` page adds a clearer public organization-level `trusted source` boundary for designers, fabricators, and assemblers in integrity-assurance markets, but it still does not unlock supplier approval, finished-board qualification, or release authority.
- For `22-layer`, the new official `QML J-STD-001S Space/Military Addendum` page adds a clearer public `EMS/OEM assembly-process` listing boundary, but it still does not unlock bare-board qualification, supplier approval, or program-specific acceptance authority.
- For `22-layer`, the official `MIL-PRF-55110` ASSIST detail page now gives this corpus a cleaner public legacy rigid-board military-spec identity / scope / inactive-status boundary relative to `MIL-PRF-31032`, but it still does not unlock current qualification basis, listing status, supplier approval, or acceptance authority.
- For `22-layer`, the official `MIL-PRF-31032/1E` rigid-multilayer sheet now gives this corpus a cleaner public sheet-level hierarchy for the rigid multilayer thermosetting-resin branch under the broader military qualification family, but it still does not unlock qualification flow, current listing status, supplier approval, or acceptance authority.
- For `22-layer`, the new official `IPC-A-600K` TOC adds a clearer public bare-board acceptability and inspection boundary distinct from assembly acceptability, but it still does not unlock reusable class thresholds, supplier approval, or qualification status.
- For `22-layer`, the new official `IPC-6011A` TOC adds a clearer public `IPC-601X` generic printed-board framework for procurement class, quality assurance, traceability, and lot-acceptance vocabulary, but it still does not unlock sectional `IPC-6012` criteria, supplier conformance, or program acceptance.
- For `22-layer`, the official `IPC-6012FA` product page and TOC now give this corpus a cleaner current automotive addendum hierarchy with procurement-trigger and clause-family visibility, but they still do not unlock automotive acceptance thresholds, supplier compliance, or hi-rel qualification-flow reconstruction.
- For `22-layer`, the new official DLA `QML/QPL/QBL` listing page adds a clearer public government-side qualification-listing infrastructure boundary between governing specifications, pre-acquisition qualification, and later listing visibility, but it still does not unlock current supplier status, program acceptance, or release authority.
- For `22-layer`, the new official `AS9101G` page adds a clearer public audit-process layer for conformity and process-effectiveness reporting against `9100-series` and related requirements, but it still does not unlock audit outcomes, supplier approval, or program-specific acceptance authority.
- For `22-layer`, the new official `AS9100D` and `AS9131D` pages add clearer baseline-`QMS`, customer/regulatory-precedence, and contract-driven nonconformity-reporting boundaries, but they still do not unlock certification status, disposition authority, release authority, or program-specific acceptance numbers.
- For `22-layer`, the IPC `6012` addendum taxonomy page now makes the current public base-vs-addendum hierarchy easier to frame across `medical`, `space/military`, and `automotive` branches, but it still does not unlock addendum technical requirements, applicability decisions, or acceptance authority.
- For `22-layer`, the new official `FAR 44.303` page adds a clearer public purchasing-system-review layer for subcontractor responsibility, postaward management, management controls, and higher-level quality-standards review, but it still does not unlock supplier approval, qualification, or release authority.
- For `22-layer`, the new official `DFARS 252.246-7008` page adds a clearer public source-hierarchy, risk-based-traceability, record-availability, inspection/testing/authentication, and subcontract-flowdown layer for government electronic-parts procurement, but it still does not unlock supplier approval, authentic-lot proof, PCB-specific technical criteria, or acceptance authority.
- For `22-layer`, the new official `FAR 52.246-11` page adds a clearer public contract-clause layer for contract-listed higher-level quality standards and lower-tier subcontract flowdown, but it still does not unlock which standard was invoked, whether flowdown occurred, supplier compliance, or release authority for a specific procurement.
- For `22-layer`, the new official `DLAD 46.291` page adds a clearer public contract-governed `production lot testing` and lot-conformance-evidence layer, but it still does not unlock universal `PLT` rules, PCB-specific sample/test thresholds, accepted-lot status, or supplier qualification.
- For `22-layer`, the new blocker-reduction boundary batch now splits `acceptance workflow`, `qualification/listing/release authority`, and `contract flowdown / lot conformance` into separate fact cards, which makes prompt-side retrieval safer and reduces overclaim risk when the draft mentions hi-rel governance vocabulary.
- This new split still does not unlock `Class 3 / 3A` thresholds, supplier approval, contract invocation proof, accepted-lot status, or outgassing acceptance numbers.
- For `22-layer`, the new threshold-boundary batch now also splits `Class 3 / addendum hierarchy`, `clause-family visibility`, and `outgassing / screening acceptance` into separate fact cards, which makes prompt-side retrieval safer when the draft tries to reconstruct hard hi-rel numbers from public metadata.
- This new `22-layer` threshold split still does not unlock `Class 3 / 3A` thresholds, addendum technical tables, `PLT` sample plans, outgassing acceptance numerics, or accepted-lot proof.
- Post-containment reassessment now shows that the remaining `22-layer` blocker is concentrated less in standards-metadata ambiguity and more in direct HIL-specific compliance / qualification / acceptance assertions that still have no acceptable supplier-evidence layer inside `llm_wiki`.
- For `22-layer`, the new assertion-containment batch now also splits `supplier-status marketing`, `compliance assertions`, and `qualification / acceptance assertions` into separate fact cards, which makes prompt-side retrieval safer when the draft tries to turn public governance/workflow metadata into HIL proof claims.
- This new `22-layer` assertion split still does not unlock supplier approval, compliance proof, accepted-status claims, qualification-package claims, or program-specific acceptance authority.
- For `20-layer` and adjacent high-layer digital-material framing, the new official Panasonic `MEGTRON M` product page adds one more condition-bound product-grade anchor plus explicit `high multi-layer` / `IST` context, but it still does not unlock board-level reliability, process-window, or capability claims.

## Strongest Existing Evidence

### Material-property layer

The current corpus is strongest when it stays close to official laminate datasheets.

Representative support files:

- `facts/materials/panasonic-megtron-6.md`
- `facts/materials/panasonic-megtron-7.md`
- `facts/materials/panasonic-megtron-8.md`
- `facts/materials/isola-tachyon-100g.md`
- `facts/materials/isola-astra-mt77.md`
- `facts/materials/ventec-vt-870.md`
- `facts/materials/agc-rf-10.md`
- `facts/materials/fr4-official-source-coverage.md`

These cards already preserve legitimate numeric anchors such as:

- frequency-tagged `Dk / Df`
- `Tg`, `Td`, `T288`
- `CTE`
- thermal conductivity
- water absorption
- peel-strength or material-positioning metadata where officially published

### Process and validation layer

The current corpus is also usable for process framing and validation structure.

Representative support files:

- `facts/methods/high-layer-count-backdrill-and-registration-posture.md`
- `facts/methods/backdrill-control-capability.md`
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
- `facts/methods/rf-validation-capability.md`
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
- `wiki/testing/rf-validation-and-test-coverage.md`
- `facts/standards/ipc-hdi-electrical-test-and-coating-metadata.md`

These files are good at supporting:

- why high-layer registration, sequential lamination, and backdrill matter
- why coupon planning, TDR, and VNA belong in the same verification ladder
- how to frame HDI, impedance, and high-layer manufacturing as a planning problem

## Main Numeric Gap Classes

### 1. Material numeric tables beyond current supported families

Typical claim shapes:

- `Dk / Df / Tg / Td / CTE / moisture / peel strength` comparison tables
- low-loss vs ultra-low-loss ranking tables
- generic FR-4 tables that act like one material

Current posture:

- partially covered for Panasonic, Isola, Ventec, AGC, and some Rogers families
- still weak for broader FR-4 vendor coverage and for the exact product families many layer-count articles compare
- Taconic and unresolved Arlon grades remain under gap-control unless official stable product pages or datasheets can be confirmed

### 2. Numeric fabrication-capability tables

Typical claim shapes:

- `trace/space`
- minimum drill / laser-via diameter
- aspect ratio
- annular ring
- residual stub / backdrill window
- sequential lamination cycle counts
- registration and impedance tolerance tables

Current posture:

- internal capability framing is good
- reusable numeric capability evidence is weak
- most of these numbers are fabricator-specific and should not be elevated without current authoritative backing
- new build-up material anchors improve the vocabulary layer for `20-layer`, but they do not reduce the need to keep geometry and lamination-count tables under gap-control

### 3. Standards / qualification / acceptance thresholds

Typical claim shapes:

- IPC bow/twist thresholds
- plating thickness thresholds
- solder-float / thermal-cycle language
- IPC Class 3 or IPC-6012 / 6013 acceptance framing presented as hard thresholds
- IST-cycle language

Current posture:

- current registry is mostly metadata-safe
- clause-level or threshold-style statements are not yet safely supported
- `22-layer` and `20-layer` style standards-heavy blogs are the biggest risk here

### 4. High-speed interface and channel-performance anchors

Typical claim shapes:

- `DDR4 / DDR5`
- `PCIe Gen 4 / 5`
- `USB4`
- `10G / 25G / 56G / 112G PAM4`
- Nyquist / insertion-loss / weave-skew / stub-resonance tables

Current posture:

- current materials and internal validation pages help with framing
- article-grade numeric channel claims still need stronger official or primary-source anchors
- this gap is a major blocker for `18-layer`, `20-layer`, and especially `24-layer`

### 5. Dynamic commercial numbers

Typical claim shapes:

- lead time
- quick-turn windows
- yield percentages
- cost uplifts
- MOQ and region/customer references

Current posture:

- do not freeze these into stable facts unless a dedicated refresh process exists
- these are not the right targets for the current batch

## Hardest Claim Classes To Support Safely

Highest-risk categories:

1. high-speed / RF / channel-performance budgets
2. vendor capability / tolerance promises
3. cost / yield / lead-time percentages
4. standards-heavy reliability thresholds

These should not be treated as default reusable facts without stronger and more current source support.

## Immediate Official-Source Queue

### Batch N1: Standards and qualification metadata follow-on

Priority targets:

- `IPC-6012`
- `IPC-6013`
- public `IST` and interconnect-reliability context
- public qualification metadata that can be cited without reproducing paid standard text

Why:

- needed for `20-layer` and `22-layer`
- closes the biggest standards-heavy gap without overreaching into clause copying

### Batch N2: High-speed interface and system-context anchors

Priority targets:

- DDR4 / DDR5 routing-context anchors
- PCIe Gen 4 / Gen 5 board/channel context
- 56G / 112G PAM4 backplane or server-channel context

Why:

- needed for `12-layer`, `16-layer`, `18-layer`, `20-layer`, and `24-layer`
- gives article writers a safer way to discuss system context without inventing stackup-specific loss numbers

### Batch N3: Material numeric anchor expansion

Priority targets:

- broader FR-4 and low-loss/high-speed digital datasheets from official manufacturers already relevant to the corpus
- more official datasheet-grade coverage for families used in multilayer/backplane comparisons
- continue Taconic / Arlon only when official stable product pages or datasheets can be verified

Why:

- materials are already the strongest numeric layer, so this batch has good leverage

### Batch N4: Advanced process and microvia reliability anchors

Priority targets:

- public microvia reliability sources
- stacked microvia / sequential lamination / ELIC context where official or primary sources exist
- public bare-board electrical-test context beyond metadata-only treatment when available

Why:

- needed to keep HDI/high-layer blogs from drifting into unsupported geometry and reliability claims

### Batch N5: Optional manufacturing-test anchor densification

Priority targets:

- stronger official/public context for coupon planning, TDR, VNA, insertion-loss validation, and high-speed verification framing

Why:

- useful for `18-layer` and `24-layer`
- lower priority than the first four batches because current qualitative coverage is already decent

## Writing Rules Until These Batches Land

- Do not turn internal process pages into hard numeric capability tables.
- Do not publish generic FR-4 property tables unless every row maps to an official product datasheet.
- Do not freeze lead-time, yield, MOQ, pricing, or region/customer numbers as stable facts.
- Do not fill Taconic or unresolved Arlon parameters from third-party datasheet mirrors.
- Prefer conservative engineering framing when a topic is structurally supported but numerically under-sourced.

## Bottom Line

`llm_wiki` can now support disciplined, source-aware conservative rewrites for `6 / 8 / 10 / 12 / 14 / 16 / 18 / 24-layer` topics, but not high-density numeric versions of those drafts without stronger authority layers.

`20-layer` and `22-layer` still need another source-first pass before they are safe even under conservative rewrite rules.

The next move remains source-first rather than prompt-bridge-first. Even after the latest `L3` additions, `20-layer` and `22-layer` still do not have enough evidence to unlock unsupported threshold tables, qualification flows, geometry windows, or capability claims before `P4-06`.

For `20-layer` specifically, the current manufacturer pages now justify a conservative material-family rewrite that mentions build-up-oriented families, but they still do not justify reproducing `ELIC`, `ALIVH`, `RCC`, stacked-microvia, or sequential-lamination numbers from the current blog draft.

`20-layer` and `22-layer` now also have dedicated rewrite-guardrail fact cards:

- `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`
- `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`

`20-layer` now also has a second blocker-reduction split beneath the main guardrail:

- `facts/methods/20-layer-interconnect-reliability-workflow-boundary.md`
- `facts/methods/20-layer-process-window-and-recipe-boundary.md`
- `facts/methods/20-layer-method-vs-qualification-boundary.md`

`22-layer` now also has a second blocker-reduction split beneath the main guardrail:

- `facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`
- `facts/standards/22-layer-clause-family-vs-threshold-boundary.md`
- `facts/standards/22-layer-outgassing-and-screening-acceptance-boundary.md`

These cards convert the current evidence layer into prompt-safe boundaries by splitting each blocked draft into:

- claims safe to keep with conservative wording
- claims that may remain only after wording is downgraded
- claims that must stay out of evidence packs until stronger primary official sources exist

This does not change the readiness verdict. It makes the current block on `20-layer` and `22-layer` more explicit so `P4-06` cannot silently inherit unsupported thresholds, geometry tables, qualification flows, or supplier-status claims.

Latest `P4-12` hi-rel follow-on work adds one more useful distinction for `22-layer`:

- public IPC metadata now confirms a medical applications addendum layer (`IPC-6012EM`) beyond generic `Class 3` framing
- public NASA outgassing guidance now shows that the familiar `TML 1.0% / CVCM 0.10%` values belong to database-screening context and must not be flattened into generic board-acceptance rules
- public IPC report metadata now confirms `IST` as a named IPC study/report context, which improves method vocabulary for `20-layer` without rehabilitating `IST` cycle thresholds

These additions strengthen guarded medical / outgassing / `IST` wording, but they still do not unlock threshold tables, coupon plans, supplier-status claims, or geometry/capability numbers.

Latest `22-layer` addendum follow-on work also clarifies that public IPC metadata can support a more precise hierarchy:

- `IPC-6012F` is the current rigid-board base specification
- `IPC-6012EM` is a procurement-triggered medical rigid-board addendum layer
- `IPC-6012FS` is a current space/military avionics addendum layer that explicitly modifies a broad set of clause families beyond generic `Class 3` wording

This improves guarded rewrite support for program-context phrasing, but it still does not make addendum acceptance criteria, sample-size rules, test frequencies, or space/medical qualification thresholds reusable.

Latest `22-layer` follow-on work now adds two more guarded support layers:

- public IAQG records move `FAI` from bare standard identity into cross-supply-chain workflow and documentation context
- official supplier process guidance now supports a safer statement that high-layer rigid-board fabrication becomes more lamination-, dimensional-control-, and registration-sensitive as complexity rises

These additions improve conservative process and workflow phrasing, but they still do not unlock re-accomplishment triggers, audit outcomes, aspect-ratio numbers, registration tolerances, or fabrication-capability tables.

Latest multi-agent follow-on work also adds:

- public `AS9145` and `AS9103` metadata so aerospace-style `FAI` wording can now sit inside a broader product/process-validation and variation-management workflow context
- public IAQG `OASIS` metadata so certification/audit-record verification can be framed as an official ecosystem rather than as something inferred from supplier marketing
- official Panasonic `MEGTRON 7` positioning for `very high layer count` and `HDI` compatibility, which gives the high-layer manufacturability layer one more non-Isola supplier-side anchor

These additions improve guarded workflow and manufacturability phrasing only. They still do not make certification status, audit outcome, `PPAP` completion, aspect-ratio rules, or shop capability claims reusable.

Latest `L3` follow-on work adds three more guarded support layers for `20-layer`:

- public IPC method-governance metadata now supports wording that `TM-650` references belong inside a formal method-development / validation workflow rather than being treated as loose acronyms
- public IPC related-resources metadata now supports a limited coupon-evaluation context for plated holes and microvia variants without exposing public acceptance criteria
- official Doosan `DSF-900SQ` positioning adds one more supplier-side build-up anchor that explicitly combines `multiple lamination`, `HDI process`, and high-thermal-reliability application vocabulary

This still does not change the readiness verdict. `20-layer` remains blocked because the current draft still leans on unsupported `ELIC` defaults, geometry/process windows, `IST` thresholds, and factory-capability numbers.

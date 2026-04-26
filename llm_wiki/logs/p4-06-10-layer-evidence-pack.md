# P4-06 10-Layer Evidence Pack

Date: 2026-04-26

## Traceability Core

- `topic`: `10-layer PCB manufacturing`
- `scope`: first-wave conservative `query` evidence pack for the current `10-layer` HIL blog; supports architecture framing, material selection framing, and guarded process/validation posture only
- `template`: `prompts_template/shared/query.md`
- `overlay`: `prompts_template/hilpcb/query-overlay.md`
- `fact_ids`:
  - `materials-iteq-it-180a`
  - `materials-panasonic-megtron-4`
  - `materials-panasonic-megtron-6`
  - `materials-shengyi-s1000-2`
  - `materials-fr4-official-source-coverage`
  - `methods-pcb-stackup-special-process-and-baseline-families`
  - `methods-hdi-microvia-and-vippo-process-posture`
  - `methods-controlled-impedance-tdr-verification-posture`
  - `methods-advanced-validation-scope-segmentation`
  - `methods-high-layer-rigid-board-manufacturability-context`
  - `methods-high-layer-count-backdrill-and-registration-posture`
  - `methods-pcb-prototype-quickturn-and-volume-routing`
  - `methods-rigid-flex-stackup-and-bend-reliability-posture`
- `source_ids`:
  - `iteq-it-180a-page`
  - `panasonic-megtron-4-r5725-r5620`
  - `panasonic-megtron-4-datasheet`
  - `panasonic-megtron-6-r5775n`
  - `panasonic-megtron-6-datasheet`
  - `shengyi-s1000-2-product-page`
  - `isola-370hr-datasheet`
  - `frontendapt-pcb-fr4-pcb-page-en`
  - `frontendapt-pcb-high-tg-pcb-page-en`
  - `frontendapt-pcb-pcb-stack-up-page-en`
  - `frontendapt-pcb-multi-layer-laminated-structure-page-en`
  - `frontendapt-pcb-hdi-pcb-page-en`
  - `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
  - `frontendhil-hdi-pcb-product-page-en`
  - `frontendapt-pcb-pcb-impedance-control-page-en`
  - `frontendapt-pcb-high-speed-pcb-page-en`
  - `frontendapt-pcb-multilayer-pcb-page-en`
  - `frontendhil-multilayer-pcb-product-page-en`
  - `frontendapt-pcb-pcb-prototype-page-en`
  - `frontendapt-pcb-quick-turn-pcb-page-en`
  - `frontendhil-pcb-prototype-landing-en`
  - `frontendhil-quick-turn-pcb-landing-en`
  - `frontendapt-pcb-rigid-flex-pcb-page-en`
  - `frontendhil-rigid-flex-pcb-product-page-en`
- `must_refresh`:
  - any lead-time or turnaround promise
  - any prototype-to-volume routing claim used as current service status
  - any explicit impedance tolerance band
  - any explicit registration value
  - any via geometry, feature size, or annular-ring number
  - any compliance, approval, or coverage percentage banner
- `conflicts`:
  - `materials-shengyi-s1000-2`: the public product page says `Tg 170 C (DSC)` in the characteristic block, while the product-performance table lists `Tg 180 C (DSC)` and `185 C (DMA)`; do not flatten this into one invariant value
- `notes`:
  - `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md` is secondary framing support only, not an atomic fact card
  - `wiki/testing/validation-ladder-from-e-test-to-si-verification.md` is secondary framing support only, not an atomic fact card
  - this pack is not a readiness unlock for unsupported `B / C / D / E / F / G` numerics

## 1. Topic Summary

- 主题：`10-layer PCB manufacturing`
- 主关键词：`10 layer PCB manufacturing`
- 次关键词：
  - `10 layer PCB stackup`
  - `10 layer HDI PCB`
  - `10 layer BGA escape routing`
  - `10 layer PCB material selection`
- 页面类型：`query`
- 搜索意图类型：
  - 设计决策型
  - 制造决策型
  - 工艺控制型
  - 风险分析型
- 目标读者：
  - layout engineers
  - hardware engineers
  - sourcing / NPI engineers
  - project managers preparing a fabrication review
- 站点：
  - `HILPCB`

Recommended core answer:

- a `10-layer` board becomes relevant when routing density, plane planning, material choice, and validation scope are more constrained than a lower-layer baseline board
- current governed evidence strongly supports material-grade examples and process-planning posture
- current governed evidence does not support turning the existing blog's escape-rule tables, feature-size numbers, cost adders, tolerance claims, or compliance claims into reusable hard facts

## 2. Source Facts

### 已有硬信息

- 材料 / 家族 / 型号：
  - `ITEQ IT-180A`
  - `Panasonic MEGTRON 4 R-5725 / R-5620`
  - `Panasonic MEGTRON 6 R-5775(N) / R-5670(N)`
  - `Shengyi S1000-2`
  - guarded `FR-4 / high-Tg / low-loss` family framing
- 结构 / 工艺：
  - blind-via / buried-via / build-up / sequential-lamination vocabulary exists as internal posture support
  - stackup planning, layer-family routing, and rigid-flex branch framing exist as internal posture support
  - controlled-impedance and deeper validation are already separated from basic electrical test in internal methods cards
- 已有数字：
  - official exact-product `A` material numerics from the material cards above
- 已有测试 / 验证方法：
  - `DSC`
  - `DMA`
  - `TMA`
  - `TGA 5% loss`
  - `IPC TM-650 2.5.5.13`
  - `IPC-TM-650 2.5.5.9`
  - guarded internal `TDR / VNA / microsection / coupon` posture
- 已有应用场景：
  - high-speed digital
  - multilayer
  - `HDI`-adjacent material selection
  - rigid-flex as variant branch context

### 原文弱点

- 当前博客把大量经验值、站点 capability 文案和 recipe 表格写成了硬事实
- 多个段落混合了 architecture language 与 unsupported capability numerics
- `BGA` escape、`DFM`、sequential lamination、service banner sections are dominated by unsupported numbers
- 内部页面可支持 posture，但不能替代 dated capability authority

## 3. Claim Extraction

Candidate hard-claim clusters to evaluate before writing:

- what problem a `10-layer` board solves compared with a lower-layer baseline
- whether `HDI`, blind via, buried via, and build-up vocabulary can be used safely
- whether stackup planning can be discussed without turning one layer table into a universal recipe
- what official material examples can be cited for standard, high-Tg, and lower-loss choices
- whether high-speed / RF and rigid-flex can be retained as scoped variants
- which validation statements can be kept without claiming universal tolerances or coverage

High-risk candidate claims from the current blog that must stay blocked:

- pitch-by-pitch `BGA` escape rule tables
- `1+8+1` and `2+6+2` treated as default supported shop recipes
- laser-via diameter, capture-pad, annular-ring, and registration numbers
- cost uplift percentages and turnaround claims
- `IPC Class 3` or `100%` style QA/compliance banners

## 4. Classification

### A. Publicly Verifiable Facts

| Claim | Why it matters | Source type | Verification status |
| --- | --- | --- | --- |
| `ITEQ IT-180A` has official page-backed `Tg 175 C`, `T288 20 min`, `Td 345 C`, `Dk 4.1 at 10 GHz`, and `Df 0.017 at 10 GHz` with stated methods. | Supports a stable high-Tg FR-4 example for 10-layer material discussion. | manufacturer product page | verified |
| `MEGTRON 4 R-5725 / R-5620` has official model-level values including `Dk 3.8` and `Df 0.005 at 1 GHz / 0.007 at 10 GHz`. | Supports a stable lower-loss material example without claiming board-level performance. | manufacturer page + datasheet | verified |
| `MEGTRON 6 R-5775(N)` has official low-loss values including `Dk 3.4` and `Df 0.002 at 1 GHz / 0.004 at 12 GHz`. | Supports a stable lower-loss upgrade example for higher-speed stackups. | manufacturer page + datasheet | verified |
| `Shengyi S1000-2` has an official product page and property table with published thermal and dielectric values, but the page-level `Tg` wording conflicts with the table. | Useful high-Tg FR-4 example, but only if the conflict remains visible. | manufacturer product page | verified with conflict |

### B. Project-Level Judgments

| Judgment / control point | Scope | Safe wording |
| --- | --- | --- |
| A `10-layer` board is usually a planning response to routing congestion, plane allocation pressure, and validation complexity. | engineering decision framing | usually indicates denser routing and stackup planning pressure rather than one universal threshold |
| Finer-pitch `BGA` designs can push routing strategy toward denser via structures and more careful stackup planning. | architecture framing only | may require denser interconnect planning and earlier fabricator review |
| Sequential lamination and build-up structures increase process sensitivity. | manufacturability posture | should be treated as process-sensitive rather than assumed commodity routing |
| Validation scope should be matched to program need instead of flattened into one generic test promise. | quality / NPI workflow | baseline electrical test, impedance verification, and deeper SI or metrology checks should be scoped separately |

### C. Site-Specific Capability References

| Capability | Site path / source | Allowed wording |
| --- | --- | --- |
| `HDI`, microvia, VIPPO, and any-layer vocabulary on internal pages | `frontendapt-pcb-hdi-pcb-page-en`, `frontendapt-pcb-advanced-pcb-manufacturing-page-en`, `frontendhil-hdi-pcb-product-page-en` | use only as internal posture that these are recognized service families, not as numeric authority |
| controlled impedance with verification language | `frontendapt-pcb-pcb-impedance-control-page-en`, `frontendapt-pcb-high-speed-pcb-page-en`, `frontendapt-pcb-multilayer-pcb-page-en`, `frontendhil-hdi-pcb-product-page-en` | use only for guarded wording that impedance targets are paired with verification |
| prototype / quick-turn routing language | `frontendapt-pcb-pcb-prototype-page-en`, `frontendapt-pcb-quick-turn-pcb-page-en`, `frontendhil-pcb-prototype-landing-en`, `frontendhil-quick-turn-pcb-landing-en` | use only as routing posture; do not publish live time/capacity claims without refresh |
| rigid-flex branch pages | `frontendapt-pcb-rigid-flex-pcb-page-en`, `frontendhil-rigid-flex-pcb-product-page-en` | use only as branch context for variant constructions |

### D. Unsupported / Unclear

| Claim | Why unclear | Downgrade method |
| --- | --- | --- |
| exact `BGA` pitch escape rules and route counts | no governed first-wave numeric authority | delete numbers; keep only high-level routing-pressure wording |
| exact microvia diameter, aspect ratio, pad, annular-ring, or registration limits | currently blocked `B / E` capability layer | delete |
| exact sequential-lamination cycle counts and cost premiums | recipe/cost leakage, not stable first-wave authority | delete |
| `RCC` thickness defaults and fine-line feature claims | unsupported capability numerics and recipe leakage | delete |
| `IPC Class 3`, `100% electrical test`, and similar assurance banners | unsupported current-scope/compliance claims in this pack | delete or rebuild as guarded validation posture |
| explicit lead times, production windows, and volume claims | dynamic commercial data | `must_refresh: true` or exclude |

## 5. Primary Sources

### Official Datasheets / Product Pages

- `ITEQ IT-180A`
  - `source_id`: `iteq-it-180a-page`
  - use for exact high-Tg FR-4 material values and methods
- `Panasonic MEGTRON 4 R-5725 / R-5620`
  - `source_id`: `panasonic-megtron-4-r5725-r5620`
  - `source_id`: `panasonic-megtron-4-datasheet`
  - use for exact low-loss product-grade values and conditions
- `Panasonic MEGTRON 6 R-5775(N) / R-5670(N)`
  - `source_id`: `panasonic-megtron-6-r5775n`
  - `source_id`: `panasonic-megtron-6-datasheet`
  - use for lower-loss material example and grade-specific conditions
- `Shengyi S1000-2`
  - `source_id`: `shengyi-s1000-2-product-page`
  - use with visible `Tg` conflict handling
- `Isola 370HR`
  - `source_id`: `isola-370hr-datasheet`
  - support only as background/high-layer context already captured by governed facts, not as a new 10-layer capability authority

### Internal Registered Sources

- stackup and baseline-family routing:
  - `frontendapt-pcb-fr4-pcb-page-en`
  - `frontendapt-pcb-high-tg-pcb-page-en`
  - `frontendapt-pcb-pcb-stack-up-page-en`
  - `frontendapt-pcb-multi-layer-laminated-structure-page-en`
- HDI and advanced process posture:
  - `frontendapt-pcb-hdi-pcb-page-en`
  - `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
  - `frontendhil-hdi-pcb-product-page-en`
- impedance and multilayer validation posture:
  - `frontendapt-pcb-pcb-impedance-control-page-en`
  - `frontendapt-pcb-high-speed-pcb-page-en`
  - `frontendapt-pcb-multilayer-pcb-page-en`
  - `frontendhil-multilayer-pcb-product-page-en`
- routing and rigid-flex branch posture:
  - `frontendapt-pcb-pcb-prototype-page-en`
  - `frontendapt-pcb-quick-turn-pcb-page-en`
  - `frontendhil-pcb-prototype-landing-en`
  - `frontendhil-quick-turn-pcb-landing-en`
  - `frontendapt-pcb-rigid-flex-pcb-page-en`
  - `frontendhil-rigid-flex-pcb-product-page-en`

## 6. Usable Technical Facts

| Fact | Source type | How to write it safely |
| --- | --- | --- |
| `10-layer` boards often come up when routing density and plane planning exceed a simpler baseline stackup. | project judgment backed by internal methods framing | position as a design-planning pattern, not a universal threshold |
| `HDI`, blind via, buried via, VIPPO, and any-layer are recognized architecture and process vocabulary in the internal corpus. | internal posture card | describe as process families or architecture options, not guaranteed shop defaults |
| exact material examples can be given using official product-grade cards such as `IT-180A`, `MEGTRON 4`, `MEGTRON 6`, and `S1000-2`. | manufacturer source-backed facts | tie every number to the exact product and stated method/frequency |
| stackup planning should separate signal layers, reference planes, power-plane needs, and material-family choices. | internal methods framing | write as planning logic, not as one universal layer-assignment recipe |
| sequential lamination and build-up structures increase process sensitivity and should trigger earlier manufacturability review. | internal posture + high-layer manufacturability context | keep qualitative |
| impedance control belongs with verification, not just nominal design intent. | internal methods card | say impedance targets are typically paired with coupon/TDR-style verification language |
| deeper validation can expand beyond continuity/isolation into TDR, VNA, microsection, or other program-scoped checks. | internal methods card | keep as layered validation scope, not a promise that every job gets the full stack |
| rigid-flex should be handled as a variant branch with bend-sensitive stackup and reliability planning. | internal methods card | keep only as variant context; do not carry exact config numbers |

## 7. Article Data Targets

- 目标最低公开技术事实数：`6`
- 目标最低正文官方锚点数：`4`
- 是否必须有早期事实表：`是`
- 是否必须有第二层早期结构化信息块：`是`
- 第二层结构建议：
  - first table: `Decision area | Safe public support | What stays qualitative | Verification action`
  - then a 4-card or second markdown table for `routing pressure / material choice / process sensitivity / validation scope`
- 是否适合 glossary：`是`
- 是否适合 supplier checklist：`是`

Data-density rule for this topic:

- prioritize a conservative early table over dense capability tables
- if a number cannot map to a stable `fact_id` and `source_id`, keep it out of the early structure

## 8. In-Body Citation Plan

| Article section | Claim to support | Planned source |
| --- | --- | --- |
| Intro / quick answer | `10-layer` is mainly a planning response to routing, plane, and validation complexity | `methods-pcb-stackup-special-process-and-baseline-families`; `methods-hdi-microvia-and-vippo-process-posture` |
| Why designs move to 10 layers | denser packages and mixed power/signal planning increase stackup pressure | `methods-pcb-stackup-special-process-and-baseline-families`; `methods-high-layer-rigid-board-manufacturability-context` |
| HDI and via vocabulary | blind-via / buried-via / build-up language is legitimate architecture vocabulary but not a default numeric recipe | `methods-hdi-microvia-and-vippo-process-posture` |
| Stackup planning | signal/reference/power planning should be explicit rather than copied from one default table | `methods-pcb-stackup-special-process-and-baseline-families` |
| Material selection | `IT-180A`, `MEGTRON 4`, `MEGTRON 6`, and `S1000-2` examples with exact published values | their product-grade fact cards and source IDs |
| Validation | impedance and advanced validation should be framed as layered verification scope | `methods-controlled-impedance-tdr-verification-posture`; `methods-advanced-validation-scope-segmentation` |
| Rigid-flex variant | rigid-flex is a branch path with bend-sensitive planning | `methods-rigid-flex-stackup-and-bend-reliability-posture` |

## 9. AI-SEO Evidence Primitives

### A. Quick Answer / Definition Material

| Field | Content |
| --- | --- |
| Core definition | A `10-layer` PCB is usually a multilayer routing and stackup choice made when signal density, plane allocation, and process sensitivity exceed what a simpler stackup can carry comfortably. |
| When it matters | It matters when dense `BGA` escape, mixed-speed routing, multiple power domains, or variant constructions such as `HDI` or rigid-flex start to compete for limited layer resources. |
| Deciding factor | The key decision factor is not one fixed threshold but whether routing, material choice, validation scope, and manufacturability review all become meaningfully more constrained. |
| Safe short version | A `10-layer` PCB is usually chosen when routing density, reference-plane planning, and manufacturing review become more demanding than a simpler stackup can handle. Public evidence safely supports material examples and process framing more than universal escape-rule or capability numerics. |

### B. Inline Citation Handles

| Claim cluster | Inline citation handle | Source URL | Safe sentence pattern |
| --- | --- | --- | --- |
| high-Tg FR-4 example | `According to ITEQ's official IT-180A product page` | `iteq-it-180a-page` | According to ITEQ's official `IT-180A` product page, this material is published with `Tg 175 C` and `Dk 4.1 at 10 GHz`, making it a usable high-Tg FR-4 example rather than a generic stand-in for all FR-4 systems. |
| lower-loss material example | `Panasonic's official MEGTRON 4 page lists` | `panasonic-megtron-4-r5725-r5620`; `panasonic-megtron-4-datasheet` | Panasonic's official `MEGTRON 4` page lists `Dk 3.8` and `Df 0.005 at 1 GHz / 0.007 at 10 GHz`, so lower-loss material selection can be discussed with exact product-grade values. |
| lower-loss upgrade example | `Panasonic's public MEGTRON 6 grade page shows` | `panasonic-megtron-6-r5775n`; `panasonic-megtron-6-datasheet` | Panasonic's public `MEGTRON 6` grade page shows `Dk 3.4` and `Df 0.002 at 1 GHz / 0.004 at 12 GHz`, which supports a cautious lower-loss upgrade path without proving board-level channel performance. |
| impedance verification posture | `Internal controlled-impedance pages consistently pair` | `methods-controlled-impedance-tdr-verification-posture` | Internal controlled-impedance pages consistently pair impedance targets with verification language, so the article can discuss coupon or `TDR` posture without promising one universal tolerance band. |

### C. Authority / Reviewer Inputs

| Field | Content |
| --- | --- |
| Author entity | HILPCB content team using governed `llm_wiki` evidence pack inputs |
| Reviewer entity | engineering review against `llm_wiki` fact cards and registered source IDs |
| Credentials or scope | multilayer stackup, material selection, and manufacturability framing; excludes live capability certification or quote authority |
| Public profile / entity URL | none required in this evidence-pack layer |
| Safe fallback wording | Reviewed against governed material cards, method cards, and registered source records in the internal evidence layer. |

### D. FAQ Query Phrasing Seeds

| User query style | Mapped FAQ question | Source / evidence basis |
| --- | --- | --- |
| `When do I need a 10 layer PCB instead of 8 layers?` | When does a design usually need a `10-layer` PCB? | project judgment + stackup posture methods |
| `Can a 10 layer board use blind vias or buried vias?` | Can a `10-layer` board include blind-via or buried-via structures? | `methods-hdi-microvia-and-vippo-process-posture` |
| `What material should I use for a 10 layer high speed PCB?` | Which material families are reasonable starting points for a `10-layer` high-speed stackup? | official material fact cards |
| `Does a 10 layer PCB automatically mean HDI?` | Does moving to `10 layers` automatically mean an `HDI` build? | project judgment + HDI posture methods |
| `How should impedance be checked on a 10 layer PCB?` | How should impedance control be framed on a `10-layer` board? | impedance and validation methods cards |

## 10. Handoff To Template

- 建议模板：`query`
- 建议模块：
  - `application`
  - no standalone `capability` module in first-wave mode
- 建议标题类型：
  - design decision / manufacturing planning
- 推荐早期表格类型：
  - `Question | Safe answer | What not to claim | What to verify with fabricator`
- 推荐第二层结构块类型：
  - 4-card block for `routing pressure / stackup planning / material choice / validation scope`
- 推荐站点承接页：
  - `products/hdi-pcb`
  - `products/high-speed-pcb`
  - `products/rigid-flex-pcb`
  - `products/pcb-prototype`
  - `products/quick-turn-pcb`
- 推荐正文锚点：
  - intro quick answer
  - material selection section
  - validation section
  - rigid-flex variant section
- 推荐 FAQ 补点：
  - do not answer with unsupported pitch/diameter/lead-time numbers

Section-by-section bridge mapping from the current blog:

- title / intro:
  - keep `10-layer`, `HDI`, dense-routing, and `BGA` escape framing
  - remove current inline capability quote
- why designs move to 10 layers:
  - keep architecture pressure
  - remove pin-count, plane-count, and cost percentages
- HDI via types:
  - keep blind-via / buried-via / build-up distinctions
  - downgrade `1+N+1`, `1+8+1`, and `2+6+2` into vocabulary only
- BGA escape routing:
  - retain only high-level denser-routing logic
  - remove pitch-by-pitch rules
- stackup design:
  - replace universal table with planning framework
- sequential lamination:
  - retain process sensitivity only
  - remove cycle-count and cost tables
- material selection:
  - strongest hard-fact section
  - center on official material cards
- RF / high-speed:
  - keep as variant path
  - avoid derived geometry/performance claims
- rigid-flex:
  - keep as variant scope
  - remove exact construction counts and tolerance claims
- DFM:
  - rebuild around review actions, not numeric tables
- CTA:
  - rebuild from conservative service-routing language only

## 11. Final Preflight

- hard facts extracted: `yes`
- `public facts / project judgments / site-specific capability / unsupported` separated: `yes`
- primary sources present for material facts: `yes`
- unsupported numbers explicitly blocked: `yes`
- traceable `fact_id` and `source_id` structure present: `yes`
- `must_refresh` items visible: `yes`
- known conflict visible: `yes`
- wiki pages marked as secondary only: `yes`
- conservative template choice fixed: `yes`

Reject this pack if any of the following are reintroduced during draft execution:

- unsupported `B / C / D / E / F / G` numerics
- current blog service-banner claims copied as hard facts
- internal posture pages used as if they were dated capability records
- exact `BGA` pitch, via geometry, feature-size, registration, or impedance-tolerance numbers without stronger governed authority
- compliance or approval wording without current verified source support

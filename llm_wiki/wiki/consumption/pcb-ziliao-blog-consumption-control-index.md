---
title: "PCB资料 Blog Consumption Control Index"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-12"
tags: ["pcb-ziliao", "consumption-control", "per-pdf", "blog-writing", "dfm", "emc", "inspection", "package"]
---

# PCB资料 Blog Consumption Control Index

**Pack ID**: `consumption-pcb-ziliao-control-index`
**Date**: `2026-05-12`
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Purpose

This page is the blog-writing control surface for `/code/blogs/tmps/PCB资料`.

Use it when a writing agent needs one entry point for:

- `which PDF family covers this topic`
- `where reusable parameters or formulas really live`
- `which figures or images exist only as local evidence`
- `which process or inspection topics are safe to write now`
- `which claims remain blocked or still need official sources`

Do not use this page as authority by itself.
It routes the writer to `facts/`, `wiki/`, `pdf_evidence/`, and the right bounded log surface.

This page is different from:

- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
  - recovery and dispatch surface
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
  - corpus-level resume and residual-governance surface

---

## 2. Corpus Snapshot

| Field | Value |
| --- | --- |
| Source batch | `/code/blogs/tmps/PCB资料` |
| Total PDFs | `63` |
| Handbook PDFs | `4` |
| Article PDFs | `59` |
| Writing posture | `blog-consumption routing only` |
| Current ceiling | `program_level_strong_complete` + `current_public_authority_layer_exhausted_with_residual_authority_gaps` |
| Non-authority rule | `tmps` PDFs remain claim inventory, not primary authority |

---

## 3. Retrieval Order

Use this order when writing from `PCB资料`:

1. Start from the topic family below.
2. Pull the linked `facts/` and `wiki/` surfaces first.
3. Use `pdf_evidence/` only for image, diagram, defect-photo, or local visual provenance support.
4. Keep all exact numerics, capability windows, acceptance thresholds, and compliance conclusions tied to official sources.
5. If the needed claim is listed as blocked here, stop and mark `needs_source` or `blocked_pending_official_source`.

---

## 4. Topic Family Routing

| Topic family | Safe writing use | Parameter / formula route | Image / figure route | Process / inspection route | Scenario route | Default blocked class |
| --- | --- | --- | --- | --- | --- | --- |
| `package footprint governance` | package naming, footprint review posture, pin-1/origin wording, BGA pitch-family caution | `wiki/processes/package-library-governance-and-footprint-review-map.md`; vendor-scoped exact rows only | `pdf_evidence/pcb_ziliao/package/`; `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`; `facts/local_pdf/footprint-review-dimensions-visual-boundary.md` | package-library review and DFM gate wording | package / component selection articles | universal `pitch -> land pattern` law, board-level marking geometry law |
| `emc and return-path review` | EMC review posture, return-path continuity, shielding-aware layout, entry-path and hot-loop framing | only owner- or standards-backed method cards; no handbook numerics | handbook evidence and local EMC diagrams only as bounded support | EMC method cards plus `wiki/consumption/lock-emc-fcc-compliance-evidence-pack.md` | lock, RF, telecom, industrial-control, power | exact EMC spacing, pass-status, certification or emissions-reduction claims |
| `inspection and workmanship` | defect taxonomy, visual examples, orientation and polarity checks, inspection-stack wording | no local numeric thresholds; use official inspection/process cards only | `pdf_evidence/pcb_ziliao/pcba/` | `wiki/testing/pcba-visual-inspection-taxonomy.md`; `wiki/processes/inspection-governance-navigation-map.md` | assembly quality, rework, test, release | accept/reject thresholds, quality-rate promises, Class 2/Class 3 numerics |
| `dfm governance and release review` | DFM as release-review gate, DRC-vs-DFM framing, package completeness, file-package review | official DFM/process cards only | local article visuals only if already routed through evidence/facts | `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`; DFM facts | manufacturing-review, cost-driver, release-readiness | universal rule tables, cost/yield/lead-time promises |
| `layout stackup impedance routing` | layer-role vocabulary, stackup tradeoff framing, reference-plane continuity, impedance as geometry-plus-dielectric problem | official impedance / stackup / routing facts only | local layer-role diagrams and bounded visuals | `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `wiki/processes/rigid-board-family-and-layer-boundaries.md` | high-speed, RF, multilayer, signal-integrity topics | exact stackup values, impedance tolerances, safety-distance minimums |
| `fabrication features holes pads mask edge features` | hole / slot taxonomy, CAM omission risk, via-mask treatment taxonomy, pad/mask relationship, gold-finger and castellated identity | official pad / mask / hole / edge-feature facts only | `pdf_evidence/pcb_ziliao/package/` for local diagrams | `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; finish-zoning wiki | hole-slot, solder-mask, edge-connector, pad-design topics | drill / annular / mask-bridge / hole-spacing numerics and capability windows |
| `panelization mark character board-edge handling` | panelization branch naming, board-edge exposure risk, Mark/fiducial role framing, character obstruction risk | official fiducial or handling facts only | selected local visual routes via package / local-pdf facts | compact-closure, mixed-technology, edge-risk, fiducial facts | SMT handling, panelization, character and Mark articles | rail widths, panel defaults, Mark geometry, edge spacing numerics |
| `assembly stencil bga dip polarity test` | DFA review posture, spacing/access risk, stencil family identity, BGA hidden-joint review, THT fit, polarity/designator clarity, ICT/flying-probe identity | official assembly/process/test facts only | defect-photo and local mechanism visuals only if bounded | `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`; `wiki/processes/ict-fixture-introduction-and-method-selection.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` | assembly-solutions, hidden-joint, testability, rework | process-window numerics, locator rules, yield and reliability promises |
| `bom procurement package identity and fpc taxonomy` | package identity grammar, package-footprint alignment, BOM field separation, sourcing review posture, `0R` role taxonomy, FPC structure taxonomy | official BOM/package/FPC facts only | local category visuals only if non-numeric | BOM and procurement wiki pages; flex taxonomy wiki | sourcing hygiene, package selection, FPC overview | stock, lead time, price, MOQ, automatic matching, universal FPC design rules |
| `manufacturing data exchange and tool workflow` | Gerber / ODB++ / IPC-2581 identity, assembly-input package completeness, coordinate-frame registration, BOM cross-probe context | official format/tool boundary cards only | local UI-heavy article visuals are generally blocked unless already abstracted | `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `wiki/consumption/assembly-solutions-evidence-pack.md` | handoff-package, CAM, assembly-input topics | branded-tool superiority, workflow-efficiency, one-format-complete claims |

---

## 5. Formula And Parameter Routing

`PCB资料` itself should not be treated as a numeric or formula authority layer.
Use these rules:

| Need | Use | Do not use |
| --- | --- | --- |
| Official package geometry row | vendor-scoped package / land-pattern fact cards in `facts/methods/` | handbook package tables as cross-vendor law |
| Impedance or routing parameter | official impedance / routing facts and related standards-owner boundaries | article or handbook percentages and geometry tables |
| Material or process capability number | official `sources/registry/` plus fact cards already landed | article claims about tolerance, yield, capability, speed, or cost |
| Formula or calculation logic visible in local PDF | use only if already promoted into a bounded local or official fact card; otherwise mark `needs_source` | direct transcription from `tmps` PDF |
| Inspection / quality threshold | official standards / process facts if landed | local defect photo captions or summary tables |

Current local-PDF-derived visual facts already landed:

- `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`
- `facts/local_pdf/padstack-layer-role-visual-boundary.md`
- `facts/local_pdf/footprint-review-dimensions-visual-boundary.md`

Everything else from `PCB资料` that looks like a formula, threshold table, capability window, or exact recipe should be assumed `blocked` unless another linked fact card already upgrades it.

---

## 6. Image And Asset Routing

Use `pdf_evidence/pcb_ziliao/` for:

- package diagrams
- padstack and layer-role visuals
- defect-photo examples
- polarity / orientation visual examples
- ESD and workmanship visual context

Use classes:

- `safe_visual_support_only`
- `blocked_evidence_only`
- `promotion_already_landed_in_facts_local_pdf`

Current high-value asset groups:

| Asset family | Path | Safe use |
| --- | --- | --- |
| Package diagrams and naming visuals | `pdf_evidence/pcb_ziliao/package/` | non-numeric explanation of footprint-review dimensions, padstack roles, pin-1 / installation-mark context |
| PCBA defect and inspection photos | `pdf_evidence/pcb_ziliao/pcba/` | defect taxonomy, polarity visibility, workmanship discussion, ESD awareness examples |

---

## 7. Handbook Control Surface

| PDF | Blog-writing value | Safe reuse | Blocked or held |
| --- | --- | --- | --- |
| `【PCB必备】42种-常见PCB封装设计指导规范.pdf` | package / footprint governance anchor | package-family vocabulary, pin-1/origin review posture, local visual aids, vendor-scoped exact-row replacement routes | universal package geometry rules, unresolved `1.50 mm` cross-vendor closure |
| `【PCB必备】85页-PCB设计EMC设计指导书.pdf` | EMC concept and review framing | EMC method wording and bounded local evidence | exact EMC numerics, compliance/pass claims |
| `【PCB必备】158页-PCBA检验规范汇总.pdf` | inspection and defect-image support | inspection taxonomy, ESD/workmanship vocabulary, defect-photo evidence | acceptance criteria and yield/quality-rate claims |
| `【PCB必备】194页-PCB设计规范经验之书.pdf` | bounded official-route feeder for complex board-review topics | `D3` power/layout posture, `D4` DDR and eMMC governance, `D5` ESD/clock/hot-loop/differential-pair review language | platform-specific numerics, broad handbook doctrine, full-corpus replacement authority |

---

## 8. Article Cluster Control Surface

### 8.1 `E1` DFM Governance And Persuasion

| Field | Value |
| --- | --- |
| Theme | DFM gate positioning, DRC-vs-DFM, release-review framing, cost-driver caution |
| Primary facts / wiki | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`; `wiki/processes/pcb-cost-driver-review-and-quote-preparation.md` |
| Parameter route | official cost-driver or DFM facts only |
| Formula route | none from local PDF; mark `needs_source` |
| Asset route | only bounded DFM visuals if later promoted |
| Process route | DFM / NPI / inspection-governance wording |
| Scenario route | release-readiness, DFM review, quote-prep |
| Default blocked | persuasion claims, cost reduction numerics, branded DFM rule tables |

### 8.2 `E2` Layout, Routing, Stackup, Layers, And Impedance

| Field | Value |
| --- | --- |
| Theme | layer-role vocabulary, reference-plane continuity, stackup planning, impedance framing, safety-distance taxonomy |
| Primary facts / wiki | `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `wiki/processes/rigid-board-family-and-layer-boundaries.md`; `facts/methods/controlled-impedance-tdr-verification-posture.md`; `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md` |
| Parameter route | official impedance and routing fact cards only |
| Formula route | none from article layer; mark `needs_source` |
| Asset route | `facts/local_pdf/padstack-layer-role-visual-boundary.md` and linked package evidence |
| Process route | stackup planning, routing continuity, RF validation posture |
| Scenario route | multilayer, high-speed, RF, SI review |
| Default blocked | exact stackup tables, `5%` tolerance claims, safety-distance thresholds |

### 8.3 `E3` Fabrication Features, Pads, Holes, Slots, Vias, Solder Mask, And Edge Features

| Field | Value |
| --- | --- |
| Theme | hole/slot intent, CAM omission risk, via-mask treatment, pad-mask relationships, gold finger, castellated edge, hole-spacing reliability |
| Primary facts / wiki | `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `wiki/processes/finish-zoning-and-selective-multi-finish.md`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/hole-spacing-reliability-boundary.md`; `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md` |
| Parameter route | official pad / hole / mask facts only |
| Formula route | none from article layer; mark `needs_source` |
| Asset route | `pdf_evidence/pcb_ziliao/package/` diagrams for padstack and naming context |
| Process route | fabrication-output review, finish zoning, CAM completeness |
| Scenario route | pad design, solder-mask, edge connector, castellation |
| Default blocked | drill, slot, annular, bridge, hole-spacing numerics and factory defaults |

### 8.4 `E4` Panelization, Outline, Edge Clearance, Marking, And Character

| Field | Value |
| --- | --- |
| Theme | panelization branch selection, assembly-facing panel handling, board-edge exposure, Mark/fiducial logic, character obstruction risk |
| Primary facts / wiki | `facts/methods/fiducial-optical-alignment-global-local-scope-and-local-correction-boundary.md`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/processes/mixed-technology-solder-route-selection.md` |
| Parameter route | official fiducial / edge-risk facts only |
| Formula route | none from article layer; mark `needs_source` |
| Asset route | limited local visuals via existing local-pdf fact links |
| Process route | depanelization, edge handling, alignment review |
| Scenario route | SMT panel handling, Mark design, edge-risk review |
| Default blocked | panel border, rail width, Mark geometry, character-size and edge-clearance numerics |

### 8.5 `E5` Assembly, DFA, Stencil, Soldering, Polarity, And Test

| Field | Value |
| --- | --- |
| Theme | DFA review, access and spacing risk, stencil family identity, BGA hidden-joint review, DIP fit, pin-1 / polarity clarity, ICT vs flying probe |
| Primary facts / wiki | `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`; `wiki/processes/ict-fixture-introduction-and-method-selection.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md`; `facts/methods/pcba-ict-boundary-and-flying-probe-method-identity.md`; `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md` |
| Parameter route | official assembly/test/stencil facts only |
| Formula route | none from article layer; mark `needs_source` |
| Asset route | PCBA defect-photo evidence plus bounded local examples |
| Process route | mixed-technology flow, stencil control, X-ray/ICT/flying-probe/testability |
| Scenario route | assembly solutions, BGA process review, test planning |
| Default blocked | stencil aperture numerics, BGA process windows, locator-hole rules, yield or reliability claims |

### 8.6 `E6` Packages, BOM, Procurement-Risk, And Flexible-Circuit Subset

| Field | Value |
| --- | --- |
| Theme | package identity grammar, package-footprint alignment, BOM field separation, sourcing governance, `0R` role taxonomy, FPC structure taxonomy |
| Primary facts / wiki | `wiki/processes/package-library-governance-and-footprint-review-map.md`; `wiki/processes/bom-and-hdi-complexity-boundaries.md`; `wiki/processes/international-pcb-procurement-shipping-boundaries.md`; `wiki/processes/flex-printed-board-type-taxonomy-and-structure-map.md` |
| Parameter route | official package / BOM / FPC facts only |
| Formula route | none from article layer; mark `needs_source` |
| Asset route | package identity visuals only if already bounded |
| Process route | BOM normalization, package-footprint review, controlled-source posture |
| Scenario route | procurement hygiene, package selection, FPC overview |
| Default blocked | stock / lead-time / MOQ / price / automatic matching / universal `0R` or FPC design rules |

### 8.7 `E7` Manufacturing Data Exchange And Vendor-Tool Workflow

| Field | Value |
| --- | --- |
| Theme | manufacturing-format identity, assembly-input package completeness, coordinate registration, BOM cross-probe context |
| Primary facts / wiki | `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `wiki/consumption/assembly-solutions-evidence-pack.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/pcba-test-method-input-package-boundary.md`; `facts/methods/gerber-layer-shared-reference-frame-and-same-coordinate-system-registration-boundary.md` |
| Parameter route | official format or tool-boundary facts only |
| Formula route | none |
| Asset route | local UI-heavy pages are usually blocked; use only if already abstracted into facts |
| Process route | handoff-package completeness and CAM/assembly boundary review |
| Scenario route | manufacturing handoff, assembly input, BOM cross-probe |
| Default blocked | branded-tool superiority, tool readiness guarantees, one-format-is-enough claims |

---

## 9. Per-PDF Consumption Map

Use `P4-325` for the full recovery-grade line-by-line mapping.
Use this compressed table during writing to choose the first safe route.

| PDF family | PDFs | First safe route | Typical writing output | Default blocked |
| --- | --- | --- | --- | --- |
| handbook package | `【PCB必备】42种-常见PCB封装设计指导规范.pdf` | package-library wiki + package facts + local package evidence | footprint governance, pin-1/origin, vendor-scoped package examples | universal geometry rules |
| handbook EMC | `【PCB必备】85页-PCB设计EMC设计指导书.pdf` | EMC fact cards + EMC consumption pack + local evidence | EMC review and pre-compliance framing | exact EMC numerics |
| handbook inspection | `【PCB必备】158页-PCBA检验规范汇总.pdf` | inspection taxonomy wiki + PCBA evidence | inspection, workmanship, defect-photo explanation | acceptance thresholds |
| handbook RK3588 | `【PCB必备】194页-PCB设计规范经验之书.pdf` | D3/D4/D5 official-route logs and fact cards | bounded power/layout, DDR/eMMC, clock/ESD/hot-loop review | handbook tables and platform numerics |
| `E1` DFM | `6 PDFs` | DFM evidence pack | DFM gate and review governance | persuasion/cost numerics |
| `E2` layout/stackup/impedance | `9 PDFs` | stackup and routing wiki/facts | routing continuity, layer roles, impedance framing | exact geometry and spacing |
| `E3` holes/pads/mask/edge | `14 PDFs` | data-exchange, mask, pad, finish facts | hole-slot taxonomy, CAM omission risk, finish zoning | drill/mask/pad thresholds |
| `E4` panel/Mark/character | `8 PDFs` | edge-risk, fiducial, compact-closure routes | panel handling, board-edge risk, Mark logic | rail, Mark, edge-clearance numbers |
| `E5` assembly/stencil/test | `10 PDFs` | assembly, BGA, ICT, quality wiki/facts | DFA, BGA process review, testability, polarity | process windows and yield claims |
| `E6` BOM/package/FPC | `6 PDFs` | package, BOM, FPC routes | package identity, BOM hygiene, FPC taxonomy | stock/price/lead-time and size tables |
| `E7` handoff/tool workflow | `6 PDFs` | data-exchange and assembly-input routes | format identity, package completeness, cross-probe context | branded-tool claims |

---

## 10. Per-PDF Dispatch Table

| PDF | Theme | Parameter / formula route | Asset route | Process / inspection route | Scenario route | Block status |
| --- | --- | --- | --- | --- | --- | --- |
| `【PCB必备】42种-常见PCB封装设计指导规范.pdf` | package footprint governance | vendor-scoped package geometry facts only | `pdf_evidence/pcb_ziliao/package/`; local package visual facts | `wiki/processes/package-library-governance-and-footprint-review-map.md` | package selection, footprint review | `official_fact-backed + local_pdf_fact-backed + blocked_evidence_only` |
| `【PCB必备】85页-PCB设计EMC设计指导书.pdf` | EMC review | official EMC facts only | bounded handbook evidence | EMC method lanes | EMC / compliance-prep topics | `official_fact-backed + blocked_evidence_only` |
| `【PCB必备】158页-PCBA检验规范汇总.pdf` | inspection taxonomy | official inspection facts only | `pdf_evidence/pcb_ziliao/pcba/` | inspection / workmanship wiki | inspection, quality, rework | `official_fact-backed + blocked_evidence_only` |
| `【PCB必备】194页-PCB设计规范经验之书.pdf` | bounded complex-board routes | `D3/D4/D5` official fact routes only | handbook evidence only | power, DDR/eMMC, ESD/clock/hot-loop review | high-complexity layout review | `claim_family_level_only_with_eleven_strengthened_official_routes` |
| `PCB layout有DRC检查为什么还要用DFM.pdf` | DFM gate positioning | none from article; use DFM facts | none by default | DFM evidence pack | DFM review | `official_fact-backed` |
| `全局DFM意识对于PCB设计的重要性.pdf` | DFM governance posture | none from article; use DFM facts | none by default | DFM evidence pack | DFM review | `official_fact-backed` |
| `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf` | DFM and NPI posture | none from article; use process facts | none by default | DFM + inspection governance | DFM review | `official_fact-backed` |
| `引领工业新思想--DFM的含义将如何演变.pdf` | DFM governance language | none from article; use DFM facts | none by default | DFM gate route | DFM review | `official_fact-backed` |
| `华秋DFM在硬件制造中的作用.pdf` | DFM plus test/quality framing | none from article; use process/test facts | none by default | DFM and test identity | manufacturing review | `official_fact-backed` |
| `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf` | cost-driver caution | official cost-driver facts only | none by default | DFM + cost-driver route | quote-prep / DFM | `official_fact-backed` |
| `PCB布局布线的可制造性设计.pdf` | layout manufacturability | official routing facts only | none by default | mixed-technology and DFM review | routing review | `official_fact-backed` |
| `印制电路板设计重点.pdf` | routing priorities and return path | official routing/impedance facts only | none by default | stackup/package review maps | multilayer / SI review | `official_fact-backed` |
| `一文带你读懂PCB电路板设计中各种层的定义.pdf` | layer-role grammar | no article numerics; use layer-role facts | `facts/local_pdf/padstack-layer-role-visual-boundary.md` | data-exchange and rigid-board wiki | layer-definition article | `official_fact-backed` |
| `PCB叠层顺序规划配置方案.pdf` | stackup planning | official stackup facts only | none by default | stackup planning wiki | multilayer / SI review | `official_fact-backed` |
| `PCB为什么常用50Ω阻抗？6大原因.pdf` | impedance rationale | official impedance facts only | none by default | RF / impedance wiki | high-speed / RF | `official_fact-backed` |
| `PCB阻抗误差控制在5%，究竟有多难？.pdf` | impedance variation framing | official impedance facts only | none by default | RF validation and impedance posture | impedance-control article | `official_fact-backed` |
| `PCB内层的可制造性设计.pdf` | internal-plane framing | official stackup facts only | none by default | stackup / rigid-board wiki | multilayer / SI review | `official_fact-backed` |
| `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` | spacing taxonomy | official safety/routing facts only | none by default | pad / edge-risk routes | spacing-review topic | `official_fact-backed` |
| `PCB可制造性设计及案例分析之线路篇.pdf` | line and edge conflict framing | official routing/pad facts only | none by default | edge-risk and pad-review routes | routing DFM topic | `official_fact-backed` |
| `PCB可制造性设计及案例分析之孔槽篇.pdf` | hole/slot taxonomy | official CAM / hole facts only | none by default | data-exchange route | hole-slot article | `official_fact-backed` |
| `器件引脚的方槽、方孔如何避坑？.pdf` | square-slot/package alignment risk | official package/pad facts only | none by default | package-footprint review | footprint / THT review | `official_fact-backed` |
| `器件引脚小尺寸的孔和槽如何避坑？.pdf` | small hole-slot risk | official CAM / hole facts only | none by default | data-exchange route | hole-slot article | `official_fact-backed` |
| `PCB板漏孔、漏槽在设计端如何避坑.pdf` | omitted holes and slots | no article numerics; use CAM/data-exchange facts | `pdf_evidence/pcb_ziliao/package/padstack-layer-role-diagram.md`; `pdf_evidence/pcb_ziliao/package/via-padstack-naming-grammar.md` | data-exchange and padstack review | CAM completeness topic | `official_fact-backed` |
| `一招搞定PCB阻焊过孔问题.pdf` | via mask treatment | official mask / VIPPO facts only | none by default | mask / HDI process posture | via-mask article | `official_fact-backed` |
| `这样做，轻松拿捏阻焊桥！.pdf` | solder-mask bridge framing | official mask facts only | none by default | data-exchange and mask route | solder-mask article | `official_fact-backed` |
| `PCB设计如何防止阻焊漏开窗.pdf` | missing mask opening | official mask facts only | `facts/local_pdf/padstack-layer-role-visual-boundary.md` | data-exchange and padstack review | solder-mask article | `official_fact-backed` |
| `PCB焊盘设计之问题详解.pdf` | pad geometry review posture | official pad / land-pattern facts only | none by default | package-footprint review | pad-design article | `official_fact-backed` |
| `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` | multilayer pad/mask relationship | official pad / mask facts only | none by default | package-footprint review | pad-design article | `official_fact-backed` |
| `千万不能小瞧的PCB半孔板.pdf` | castellated edge identity | official castellated-edge facts only | none by default | panelization / edge-feature route | castellation article | `official_fact-backed` |
| `如何避免“断头线”带来的DFM（可制造性）问题？.pdf` | residual trace / release-review risk | no article numerics; use DFM and CAM facts | none by default | DFM evidence pack + data-exchange | release-review topic | `official_fact-backed` |
| `PCB“金手指”从设计到生产全流程.pdf` | edge-contact finish zoning | official finish / standards facts only | none by default | finish-zoning wiki | gold-finger article | `official_fact-backed` |
| `PCB设计孔间距的DFM可靠性.pdf` | hole-spacing reliability framing | official hole-spacing fact only | none by default | CAM/data-exchange route | hole-spacing topic | `official_fact-backed` |
| `PCB邮票孔桥连设计要点，干货满满！.pdf` | stamp-hole bridge identity | official castellation / panelization facts only | none by default | edge-feature route | panelization article | `official_fact-backed` |
| `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf` | panelization and character risk | official edge / panel facts only | none by default | depanelization + edge-risk route | panelization/character topic | `official_fact-backed` |
| `PCB拼板，不得不注意的10个问题！.pdf` | panel handling and edge risk | official depanelization facts only | none by default | compact-closure and edge-risk routes | panelization topic | `official_fact-backed` |
| `PCB板各种形状的拼版实例分享.pdf` | irregular panelization | official depanelization facts only | none by default | panel-handling and edge-risk routes | irregular panelization topic | `official_fact-backed` |
| `啥？PCB拼版对SMT组装有影响！.pdf` | assembly-facing panel handling | official depanelization/access facts only | none by default | mixed-technology and edge-risk routes | SMT handling topic | `official_fact-backed` |
| `PCB板的Mark点设计对SMT重要性.pdf` | Mark/fiducial framing | official fiducial facts only | `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md` | alignment and CAM route | SMT alignment topic | `official_fact-backed` |
| `元器件到PCB板边缘间距不足的严重性.pdf` | board-edge component exposure | official access/edge-risk facts only | none by default | compact-closure and mixed-tech routes | board-edge layout topic | `official_fact-backed` |
| `PCBA板边器件布局重要性.pdf` | board-edge layout access risk | official access/edge-risk facts only | none by default | compact-closure and mixed-tech routes | board-edge layout topic | `official_fact-backed` |
| `PCB字符的DFM（可制造性）设计.pdf` | character obstruction risk | official character-adjacent facts only | none by default | pad/mask and footprint review | silkscreen / character topic | `official_fact-backed` |
| `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf` | DFA review posture | official DFA / assembly facts only | none by default | mixed-tech, compact-closure, test strategy | assembly-review topic | `official_fact-backed` |
| `关于PCBA元器件布局的重要性.pdf` | spacing and layout-for-assembly | official assembly/access facts only | none by default | mixed-tech and rework routes | component-layout topic | `official_fact-backed` |
| `组装电子元器件间距不足的严重性.pdf` | crowded-neighborhood access risk | official assembly/rework facts only | none by default | selective-solder and rework routes | mixed-technology assembly topic | `official_fact-backed` |
| `如何避免踩坑钢网.pdf` | stencil family identity | official stencil facts only | none by default | stencil and mixed-tech routes | stencil / paste topic | `official_fact-backed` |
| `你想知道的BGA焊接问题都在这里.pdf` | BGA hidden-joint and process review | official BGA facts only | defect and hidden-joint context only | low-void BGA and hidden-joint wiki | BGA soldering topic | `official_fact-backed` |
| `那些关于DIP器件不得不说的坑.pdf` | DIP/THT fit and route selection | official package/THT facts only | none by default | selective-solder planning | THT / DIP topic | `official_fact-backed` |
| `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` | via-in-pad process posture | official VIPPO / BGA facts only | none by default | hidden-joint and fine-pitch routes | via-in-pad topic | `official_fact-backed` |
| `PCBA丝印位号与极性符号的组装性设计.pdf` | polarity and designator clarity | official polarity / marking facts only | defect and marking visual context only | visual-inspection taxonomy | assembly marking topic | `official_fact-backed` |
| `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf` | ICT/flying-probe/test method identity | official test-method facts only | none by default | ICT fixture and inspection governance | testability topic | `official_fact-backed` |
| `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf` | assembly/reliability review posture | official DFA / assembly facts only | none by default | NPI and quality routes | assembly reliability topic | `official_fact-backed` |
| `电子元器件封装(Package).pdf` | package identity grammar | official package facts only | limited package visuals only | package-library governance | package overview topic | `official_fact-backed` |
| `如何解决bom物料与焊盘不匹配问题.pdf` | BOM-package-footprint mismatch | official package alignment fact only | none | footprint alignment review | BOM/package mismatch topic | `official_fact-backed` |
| `BOM查错助力元器件采购.pdf` | BOM identity and sourcing posture | official BOM facts only | none | BOM and procurement wiki | BOM governance topic | `official_fact-backed` |
| `如何避免采购电子元器件入坑.pdf` | procurement review triggers | official procurement/BOM facts only | none | procurement and counterfeit-control routes | sourcing hygiene topic | `official_fact-backed` |
| `0Ω电阻在PCB板中的5大常见作用.pdf` | `0R` role taxonomy | official `0R` fact only | none | none beyond fact route | `0R` usage topic | `official_fact-backed` |
| `单层双面多层FPC有何区别？.pdf` | FPC structure taxonomy | official flex taxonomy fact only | none | flex taxonomy wiki | FPC overview topic | `official_fact-backed` |
| `PCB制造文件传输数据的主要格式.pdf` | format identity | official format facts only | none | data-exchange wiki | handoff-format topic | `official_fact-backed` |
| `华秋DFM组装分析前需准备的数据文件.pdf` | assembly-input package completeness | official assembly-input facts only | none | assembly solutions and data-exchange routes | assembly handoff topic | `official_fact-backed` |
| `简单好用！再也不用担心PCB图形对齐问题.pdf` | coordinate-frame registration | official registration facts only | none | data-exchange wiki | Gerber registration topic | `official_fact-backed` |
| `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf` | BOM cross-probe context | official BOM cross-probe facts only | none | BOM/tool boundary route | BOM cross-probe topic | `official_fact-backed` |
| `华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf` | branded tool workflow hold | no reusable parameter/formula route | none | hold at `P4-535` only | none until new neutral authority appears | `claim_family_level_only_with_explicit_hold_reason` |
| `华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf` | branded multi-topic hold | no reusable parameter/formula route | none | hold at `P4-535` only | none until new neutral authority appears | `claim_family_level_only_with_explicit_hold_reason` |

---

## 11. Residual Block And Reopen Rules

Keep these blocked by default:

- local-PDF exact numerics
- tolerance windows
- acceptance criteria
- universal package geometry rules
- supplier capability, yield, price, lead-time, MOQ, or quality-rate claims
- branded-tool superiority claims
- compliance, pass-status, or certification proof

Reopen only when one of these appears:

1. a new official source already not covered by linked fact cards
2. a new current-public same-surface package geometry surface above the current `1.50 mm` ceiling
3. a new neutral authority for the two remaining branded-tool `E7` hold-only PDFs
4. a dated internal capability record explicitly requested for supplier-scoped writing

---

## 12. Companion Surfaces

- Recovery / dispatch index:
  `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- Corpus resume surface:
  `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- Completion audit:
  `logs/p4-561-2026-5-12-pcb-ziliao-goal-completion-audit-after-p4-560.md`


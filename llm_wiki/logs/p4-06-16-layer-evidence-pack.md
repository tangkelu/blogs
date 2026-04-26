# P4-06 16-Layer Evidence Pack

Date: 2026-04-26

## 1. Topic Summary

- 主题：`16-layer PCB manufacturing`
- 主关键词：`16 layer PCB manufacturing`
- 次关键词：
  - `16 layer PCB stackup`
  - `16 layer high speed PCB`
  - `16 layer power distribution PCB`
  - `16 layer thermal PCB design`
- 页面类型：`query`
- 搜索意图类型：
  - 设计决策型
  - 制造规划型
  - 热管理与供电权衡型
  - 风险分析型
- 目标读者：
  - hardware architects
  - PCB layout engineers
  - power / thermal aware NPI teams
  - sourcing teams reviewing complex multilayer builds
- 站点：
  - `HILPCB`

Topic summary:

This pack supports a conservative `query` article about when `16-layer` boards become relevant for denser power, thermal, and high-speed planning, how to discuss material and platform choices safely, and how to keep heavy-copper, PDN, and process-window sections useful without carrying unsupported capability, heuristic, or commercial numerics.

## 2. Traceable Pack Record

```yaml
topic: "16-layer PCB manufacturing"
scope: "Conservative second-wave query article input for 16-layer architecture, thermal-platform selection, high-speed material choice, and bounded validation posture."
fact_ids:
  - "materials-high-speed-digital-material-ladder-normalization"
  - "materials-panasonic-megtron-6"
  - "materials-panasonic-megtron-7"
  - "materials-panasonic-megtron-8"
  - "materials-isola-i-tera-mt40"
  - "materials-isola-astra-mt77"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-advanced-validation-scope-segmentation"
  - "methods-high-speed-interface-system-context"
source_ids:
  - "panasonic-megtron-6-model-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "panasonic-megtron-7-model-r5785n"
  - "panasonic-megtron-7-series-page"
  - "panasonic-megtron-8-series-page"
  - "isola-i-tera-mt40-datasheet"
  - "isola-astra-mt77-datasheet"
  - "isola-astra-mt77-dk-df-table"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendhil-heavy-copper-pcb-product-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "pcisig-pcie-4-faq"
  - "pcisig-pcie-5-faq"
  - "oif-cei-112g-page"
  - "te-112g-portfolio-solutions"
must_refresh:
  usable_pack: false
  if_dynamic_or_scope_claims_reintroduced: true
conflicts:
  - "Internal thermal and heavy-copper pages support platform-selection posture, not transferable conductivity, current-density, or process-window promises."
  - "Current draft blends PDN heuristics and fabrication tables into one layer; usable pack keeps only planning posture plus product-grade material anchors."
notes:
  - "Secondary framing support may use wiki/topic pages, but they are not atomic fact cards."
  - "No unsupported B/C/D/E/F/G numerics are authorized as usable hard facts in this pack."
  - "This pack is for conservative query drafting only, not for high-numeric-density reuse."
```

## 3. Source Facts

### Existing hard information in the current blog

- `16-layer` is framed as a coupled power-distribution, thermal-planning, high-speed, and manufacturability topic.
- The current draft already points to the right engineering clusters:
  - power-plane and return-path planning
  - thermal-platform choice
  - material ladder selection
  - heavier copper as a branch process
  - validation scope and manufacturability review

### Existing hard information that is not safely usable as written

- copper-weight windows and heavy-copper process tables
- PDN and decoupling heuristic tables
- current-density and split-plane rule numerics
- thermal-via count, inductance, and resistance heuristics
- service, turnaround, and quality banners
- lamination ramp, pressure, and time numerics

### Original article weaknesses

- It collapses power-architecture reasoning and fabrication capability into one numeric table layer.
- It turns thermal-platform posture into implied performance proof.
- It treats heavy-copper process notes as transferable shop windows.
- It mixes service banners, validation phrases, and process heuristics into one closing promise.

## 4. Claim Extraction

| Current claim cluster | Current blog sections | Recommended treatment | Classification |
| --- | --- | --- | --- |
| `16-layer` often appears when power, thermal, and signal constraints become tightly coupled | intro, early sections | keep as qualitative engineering framing | `public facts` plus `project judgments` |
| thermal platform choice should stay separate across MCPCB, heavy copper, and ceramic routes | thermal sections | keep | `public facts` plus `project judgments` |
| exact digital-material examples can support higher-speed material discussions | material sections | keep with exact product identity and conditions | `public facts` |
| heavier copper and thermal routing change process sensitivity | copper / thermal sections | keep qualitatively | `project judgments` plus `site-specific capability references` |
| validation scope should expand by program need rather than one fixed banner | testing sections | keep | `public facts` plus `project judgments` |
| current-density tables, decoupling tables, process-window tables, and turnaround claims | multiple sections | remove from usable pack | `unsupported` |

## 5. Classification

### A. Public Facts

| Claim | Why it matters | Source type | Verification status |
| --- | --- | --- | --- |
| Internal thermal pages consistently separate MCPCB, heavy copper, and ceramic as distinct thermal platforms. | Keeps thermal sections platform-based instead of one generic heat story. | internal method posture with stable IDs | verified |
| Official product anchors exist for `MEGTRON 6`, `MEGTRON 7`, `MEGTRON 8`, `I-Tera MT40`, and `Astra MT77`. | Allows exact higher-speed material examples for dense digital boards. | official datasheet / official product page | verified |
| Public `PCIe` and `112G` sources can anchor system-context pressure without proving board capability. | Supports high-speed context safely. | official ecosystem pages | verified |
| Internal validation cards separate baseline test from deeper SI or metrology scope. | Supports safer testing sections without numeric promises. | internal method posture with stable IDs | verified |

### B. Project-Level Judgments

| Judgment / control point | Scope | Safe wording |
| --- | --- | --- |
| Move to `16-layer` when power-distribution, thermal-path design, and signal integrity start constraining each other. | decision framing | `16-layer` is often a board-architecture decision shaped by power, heat, and routing pressure together |
| Treat heavier copper as a process branch, not a universal default. | heavy-copper sections | heavier copper changes etch, balance, and process review rather than acting as a simple upgrade |
| Keep thermal sections focused on platform choice and tradeoffs rather than one numeric heat table. | thermal section | choose a thermal platform based on path, current, and assembly constraints |
| Separate validation scope from service positioning. | testing / close | deeper validation depends on program need, not one generic promise |

### C. Site-Specific Capability References

| Capability | Site path / source | Allowed wording |
| --- | --- | --- |
| thermal platform posture | `frontendapt-pcb-high-thermal-pcb-page-en`, `frontendhil-high-thermal-pcb-product-page-en`, `frontendhil-heavy-copper-pcb-product-page-en` | internal pages support platform-selection framing, not transferable conductivity or load tables |
| heavy-copper process posture | `frontendapt-pcb-heavy-copper-pcb-page-en`, `frontendhil-heavy-copper-pcb-product-page-en` | internal pages support branch-process vocabulary, not process-window tables |
| high-speed and impedance posture | `frontendapt-pcb-high-speed-pcb-page-en`, `frontendhil-high-speed-product-page-en`, `frontendapt-pcb-pcb-impedance-control-page-en` | internal pages support workflow framing, not tolerance or board-loss promises |
| multilayer planning posture | `frontendapt-pcb-multilayer-pcb-page-en`, `frontendhil-multilayer-pcb-product-page-en` | internal pages support complexity framing, not service-level numeric claims |

### D. Unsupported / Unclear

| Claim | Why unclear | Downgrade method |
| --- | --- | --- |
| copper-weight windows, plating build tables, etch / resin-fill percentages | unsupported fabrication-capability and process-window numerics | delete |
| current-density, split-plane, and PDN numeric rules | unsupported board-level heuristic tables | delete |
| thermal-via counts, inductance, resistance, and decoupling ranges | unsupported board-level interpretation numerics | delete |
| ramp, pressure, and press-time tables | unsupported process-window numerics | delete |
| `7-day`, `100%`, and similar service / quality banners | dynamic or unsupported proof claims | exclude |

## 6. Primary Sources

### Official datasheets and official product pages

- `panasonic-megtron-6-model-r5775n`
- `panasonic-megtron-6-datasheet`
- `panasonic-megtron-7-model-r5785n`
- `panasonic-megtron-7-series-page`
- `panasonic-megtron-8-series-page`
- `isola-i-tera-mt40-datasheet`
- `isola-astra-mt77-datasheet`
- `isola-astra-mt77-dk-df-table`
  - use for: exact material examples only
- `pcisig-pcie-4-faq`
- `pcisig-pcie-5-faq`
- `oif-cei-112g-page`
- `te-112g-portfolio-solutions`
  - use for: public system-context anchors only

### Internal method and capability-posture sources

- `frontendapt-pcb-high-thermal-pcb-page-en`
- `frontendhil-high-thermal-pcb-product-page-en`
- `frontendapt-pcb-heavy-copper-pcb-page-en`
- `frontendhil-heavy-copper-pcb-product-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendhil-high-speed-product-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendhil-multilayer-pcb-product-page-en`

Usage rule:

- Treat these internal pages as posture and workflow support.
- Do not use them to create transferable numeric capability tables.

## 7. Usable Technical Facts

| Fact | Fact ID | Source ID(s) | How to write it safely |
| --- | --- | --- | --- |
| Thermal-oriented pages already separate MCPCB, heavy copper, and ceramic as distinct platform choices. | `methods-thermal-pcb-platform-selection-posture` | thermal internal pages above | write that thermal-path design starts with platform choice, not one generic rule |
| Official digital-material examples exist for higher-speed multilayer boards. | `materials-panasonic-megtron-6`, `materials-panasonic-megtron-7`, `materials-panasonic-megtron-8`, `materials-isola-i-tera-mt40`, `materials-isola-astra-mt77` | official material sources above | keep exact product identity and conditions visible |
| Higher-speed ecosystem references can explain why tighter stackup and validation planning matter. | `methods-high-speed-interface-system-context` | `pcisig-pcie-*`, `oif-cei-112g-page`, `te-112g-portfolio-solutions` | write as system-context only |
| Dense rigid boards become more process-sensitive as layer count rises. | `methods-high-layer-rigid-board-manufacturability-context` | existing internal / external context sources | use as manufacturability posture only |
| Controlled impedance belongs with verification, not just nominal design intent. | `methods-controlled-impedance-tdr-verification-posture` | internal impedance sources | keep as planning-plus-validation workflow |
| Validation scope can expand beyond baseline electrical checks into deeper SI or metrology work. | `methods-advanced-validation-scope-segmentation` | internal quality / high-speed sources | write as staged validation scope, not a fixed package promise |

### Secondary framing support only

These IDs can support retrieval framing and article shape, but should not be cited as atomic fact substitutes:

- `processes-advanced-pcb-fabrication-and-stackup-planning`
- `materials-ceramic-aln-ims-thermal-platforms`
- `testing-validation-ladder-from-e-test-to-si-verification`

## 8. Article Data Targets

- public technical fact density: moderate
- early fact table: yes
- second early structured block: yes
- preferred second-layer structure:
  - first table: `Decision area | Safe public support | What stays qualitative | Verification action`
  - second block: `power pressure / thermal platform / material ladder / validation scope`
- glossary: no
- supplier checklist: yes
- numeric density rule:
  - allow exact-product material numerics and public system-context numerics only in their correct scope
  - do not introduce unsupported fabrication, PDN, thermal-outcome, standards, or commercial numerics

## 9. In-Body Citation Plan

| Article section | Claim to support | Planned evidence |
| --- | --- | --- |
| quick answer block | `16-layer` is a coupled power / thermal / signal planning decision | `methods-thermal-pcb-platform-selection-posture`, `methods-high-layer-rigid-board-manufacturability-context` |
| why boards move to `16-layer` | higher system complexity pushes denser power and validation planning | `methods-high-speed-interface-system-context`, `methods-advanced-validation-scope-segmentation` |
| material branch | exact higher-speed material examples exist | digital-material fact cards above |
| thermal / heavy-copper section | thermal-path choices are platform decisions, not one generic upgrade | `methods-thermal-pcb-platform-selection-posture` |
| validation and close | validation scope should stay layered, not collapsed into a fixed promise | `methods-controlled-impedance-tdr-verification-posture`, `methods-advanced-validation-scope-segmentation` |

## 10. AI-SEO Primitives

- direct answer sentence:
  - `A 16-layer PCB is usually chosen when power-distribution, thermal-path design, and high-speed stackup control start constraining each other on the same board.`
- follow-on answer sentence:
  - `The safest public explanation uses exact material examples and platform-selection logic while excluding unsupported current-density, heavy-copper process, and turnaround numerics.`
- retrieval anchors:
  - `16 layer PCB stackup`
  - `16 layer thermal PCB`
  - `16 layer high speed PCB`
  - `16 layer power distribution PCB`
  - `16 layer validation`

## 11. Handoff To Template

- recommended template:
  - `prompts_template/shared/query.md`
- required overlay:
  - `prompts_template/hilpcb/query-overlay.md`
- writing posture:
  - concise engineering answer first
  - early fact table
  - thermal and power branch separation
  - validation ladder section near the end
- explicit exclusions:
  - no current-density tables
  - no heavy-copper process windows
  - no decoupling or inductance heuristic tables
  - no service / turnaround / coverage banners

## 12. Final Preflight

- keep:
  - thermal platform posture
  - exact-product material numerics
  - non-numeric impedance / validation posture
- downgrade:
  - representative stackup examples
  - power-distribution framing
- delete:
  - heavy-copper process numerics
  - PDN / thermal heuristic tables
  - service and quality banners
- needs_source:
  - all fabrication-capability numerics
  - all process-window numerics
  - all board-level PDN / thermal outcome numerics

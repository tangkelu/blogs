# P4-06 14-Layer Evidence Pack

Date: 2026-04-26

## 1. Topic Summary

- 主题：`14-layer PCB manufacturing`
- 主关键词：`14 layer PCB manufacturing`
- 次关键词：
  - `14 layer rigid flex PCB`
  - `14 layer PCB stackup`
  - `14 layer PCB design rules`
  - `14 layer flex material selection`
- 页面类型：`query`
- 搜索意图类型：
  - 设计决策型
  - 制造规划型
  - rigid-flex branch 判断型
  - 风险分析型
- 目标读者：
  - hardware engineers
  - rigid-flex aware layout engineers
  - NPI / DFM engineers
  - sourcing teams preparing a special-process review
- 站点：
  - `HILPCB`

Topic summary:

This pack supports a conservative `query` article explaining when `14-layer` boards become complex enough to involve rigid-flex or transition-zone review, how to discuss flex-material classes safely, and how to keep stackup and process sections useful while excluding unsupported standards thresholds, fabrication tables, and rigid-flex reliability numerics.

## 2. Traceable Pack Record

```yaml
topic: "14-layer PCB manufacturing"
scope: "Conservative second-wave query article input for 14-layer architecture, rigid-flex branch framing, flex-material class discussion, and bounded manufacturability posture."
fact_ids:
  - "materials-flex-polyimide-and-lcp-class-source-coverage"
  - "materials-arlon-85nt-exact-product"
  - "materials-high-speed-digital-material-ladder-normalization"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-high-layer-rigid-board-manufacturability-context"
  - "methods-hdi-microvia-and-vippo-process-posture"
  - "standards-ipc-rigid-flex-and-microvia-reliability-metadata"
  - "standards-hdi-design-reference-status-metadata"
source_ids:
  - "panasonic-felios-series-page"
  - "panasonic-felios-lcp-page"
  - "panasonic-felios-frcc-page"
  - "panasonic-r-f705s-product-summary-pdf"
  - "arlon-85nt-product-page"
  - "arlon-85nt-datasheet"
  - "arlon-85nt-processing-guide"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendapt-flex-pcb-capability-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "ipc-2226a-hdi-standard-page"
  - "ipc-2315-legacy-hdi-guide-page"
must_refresh:
  usable_pack: false
  if_dynamic_or_scope_claims_reintroduced: true
conflicts:
  - "Current draft mixes rigid-flex architecture examples with unsupported bend-radius, flex-life, and transition-tolerance numerics."
  - "Standards and annular-ring sections in the current blog leak unsupported class-threshold content."
notes:
  - "Secondary framing support may use wiki/topic pages, but they are not atomic fact cards."
  - "No unsupported B/C/D/E/F/G numerics are authorized as usable hard facts in this pack."
  - "This pack is for conservative query drafting only, not for high-numeric-density reuse."
```

## 3. Source Facts

### Existing hard information in the current blog

- `14-layer` is framed as a dense multilayer topic that often touches rigid-flex, transition-zone, and branch-process review.
- The current draft already points to the right engineering clusters:
  - stackup complexity and process coordination
  - rigid-flex as a branch path
  - flex-material selection
  - HDI and via-strategy pressure
  - transition-zone planning

### Existing hard information that is not safely usable as written

- `Class 2 / Class 3` threshold tables
- registration and annular-ring numerics
- bend-radius and flex-life tables
- drilling-speed, adhesion, and coverlay numerics
- via-geometry and fine-line tables
- turnaround and quality banners

### Original article weaknesses

- It turns standards-threshold language into implied universal design rules.
- It blends rigid-flex architecture, reliability tables, and fabrication capability into one layer.
- It uses flex-material families as if one family table can authorize process and reliability numerics.
- It mixes capability, qualification, and commercial positioning near the close.

## 4. Claim Extraction

| Current claim cluster | Current blog sections | Recommended treatment | Classification |
| --- | --- | --- | --- |
| `14-layer` often brings denser structure planning and possible rigid-flex branch review | intro, early sections | keep as qualitative engineering framing | `public facts` plus `project judgments` |
| flex and rigid-flex material classes can be discussed at family level, with narrow Panasonic and Arlon exact-product examples | material sections | keep | `public facts` |
| rigid-flex should be treated as a separate construction route with its own stackup and transition review | rigid-flex sections | keep as bounded posture | `project judgments` plus `site-specific capability references` |
| standards and reliability sections should not be rebuilt from draft threshold tables | standards / quality sections | keep only as boundary language | `public facts` plus `project judgments` |
| class-threshold tables, bend-radius tables, via-geometry tables, and lead-time banners | multiple sections | remove from usable pack | `unsupported` |

## 5. Classification

### A. Public Facts

| Claim | Why it matters | Source type | Verification status |
| --- | --- | --- | --- |
| Flexible-material coverage now has official class-level anchors plus narrow Panasonic exact-product exceptions for `LCP` and `FRCC`, and one usable Arlon exact-product polyimide anchor through `85NT`. | Allows flex-material discussion without pretending generic PI coverage is complete. | official product pages plus internal class-level support | verified |
| Internal rigid-flex pages consistently treat rigid-flex as a separate process route. | Supports branch-construction framing. | internal method posture with stable IDs | verified |
| Public IPC metadata can anchor that rigid-flex and HDI reliability language has standards context, but not reusable threshold tables. | Helps prevent draft prose from inventing standards numerics. | official standards metadata | verified |
| Higher-layer rigid boards become more process-sensitive and should not be framed as commodity fabrication. | Supports manufacturability posture. | internal/external context card | verified |

### B. Project-Level Judgments

| Judgment / control point | Scope | Safe wording |
| --- | --- | --- |
| Treat `14-layer` as a point where stackup and process coordination become more fragile, especially if flex or transition zones enter scope. | decision framing | `14-layer` is often a branch-management decision, not only a routing-density decision |
| Keep rigid-flex as a separate route with separate review gates. | branch sections | if rigid-flex enters scope, review materials, transitions, and assembly separately from the baseline rigid route |
| Use flex-material classes cautiously unless an exact-product source is available. | material sections | class framing is acceptable; generic PI numerics remain under gap-control |
| Remove class-threshold and reliability tables rather than softening them into pseudo-rules. | standards / reliability sections | if no controlled source exists, delete the numeric table entirely |

### C. Site-Specific Capability References

| Capability | Site path / source | Allowed wording |
| --- | --- | --- |
| rigid-flex and flex process posture | `frontendapt-pcb-rigid-flex-pcb-page-en`, `frontendhil-rigid-flex-pcb-product-page-en`, `frontendapt-pcb-flex-pcb-page-en`, `frontendhil-flex-pcb-product-page-en` | internal pages support branch-process framing, not bend, transition, or qualification numerics |
| rigid-flex capability-family routing | `frontendapt-rigid-flex-pcb-capability-page-en`, `frontendapt-flex-pcb-capability-page-en`, `frontendapt-pcba-flex-rigid-flex-page-en` | internal pages support scoping and workflow language, not transferable fabrication tables |
| HDI / via-strategy posture | `methods-hdi-microvia-and-vippo-process-posture` plus linked internal HDI sources | use only as process-family vocabulary, not geometry proof |

### D. Unsupported / Unclear

| Claim | Why unclear | Downgrade method |
| --- | --- | --- |
| `Class 2 / Class 3` tables and compliance-style sections | unsupported threshold reuse | delete |
| bend-radius and flex-life tables | unsupported reliability numerics | delete |
| drilling-speed, adhesion, and coverlay numeric ladders | unsupported fabrication/process numerics | delete |
| fine-line, via-geometry, aspect-ratio, and transition-tolerance tables | unsupported fabrication-capability numerics | delete |
| `7 business days`, `288°C, 6 cycles`, and similar closing banners | dynamic or unsupported proof claims | exclude |

## 6. Primary Sources

### Official datasheets and official product pages

- `panasonic-felios-series-page`
- `panasonic-felios-lcp-page`
- `panasonic-felios-frcc-page`
- `panasonic-r-f705s-product-summary-pdf`
  - use for: class-level flex / rigid-flex material framing and Panasonic exact-product exceptions
- `arlon-85nt-product-page`
- `arlon-85nt-datasheet`
- `arlon-85nt-processing-guide`
  - use for: one guarded Arlon exact-product polyimide anchor without turning generic `polyimide` into a covered numeric branch
- `ipc-2226a-hdi-standard-page`
- `ipc-2315-legacy-hdi-guide-page`
  - use for: standards hierarchy and metadata boundaries only

### Internal method and capability-posture sources

- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`
- `frontendapt-rigid-flex-pcb-capability-page-en`
- `frontendapt-pcb-flex-pcb-page-en`
- `frontendhil-flex-pcb-product-page-en`
- `frontendapt-flex-pcb-capability-page-en`
- `frontendapt-pcba-flex-rigid-flex-page-en`

Usage rule:

- Treat these internal pages as posture and workflow support.
- Do not use them to create transferable numeric capability or reliability tables.

## 7. Usable Technical Facts

| Fact | Fact ID | Source ID(s) | How to write it safely |
| --- | --- | --- | --- |
| Flex-material discussion now has official class-level anchors plus narrow Panasonic exact-product exceptions. | `materials-flex-polyimide-and-lcp-class-source-coverage` | Panasonic FELIOS sources above | write class-level flex / rigid-flex material framing without pretending generic PI numerics are covered |
| `Arlon 85NT` is a guarded exact-product polyimide anchor that can be used as one product-grade example without widening generic PI coverage. | `materials-arlon-85nt-exact-product` | `arlon-85nt-product-page`, `arlon-85nt-datasheet`, `arlon-85nt-processing-guide` | keep product identity and conditions attached; do not generalize to all rigid-flex polyimide materials |
| Rigid-flex is a separate construction route requiring separate stackup and bend-reliability review. | `methods-rigid-flex-stackup-and-bend-reliability-posture` | internal rigid-flex sources above | write as branch workflow, not a numeric ruleset |
| Higher-layer rigid boards become more process-sensitive and need tighter manufacturability planning. | `methods-high-layer-rigid-board-manufacturability-context` | existing context sources | use as process posture only |
| HDI vocabulary can describe via-strategy pressure without authorizing geometry tables. | `methods-hdi-microvia-and-vippo-process-posture` | internal HDI sources | keep as process-family vocabulary only |
| Public rigid-flex / HDI standards metadata can define what this corpus should not claim. | `standards-ipc-rigid-flex-and-microvia-reliability-metadata`, `standards-hdi-design-reference-status-metadata` | IPC metadata sources above | use as boundary support, not threshold proof |

### Secondary framing support only

These IDs can support retrieval framing and article shape, but should not be cited as atomic fact substitutes:

- `materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries`
- `processes-advanced-pcb-fabrication-and-stackup-planning`

## 8. Article Data Targets

- public technical fact density: moderate-low
- early fact table: yes
- second early structured block: yes
- preferred second-layer structure:
  - first table: `Decision area | Safe public support | What stays qualitative | Supplier-review trigger`
  - second block: `rigid route / rigid-flex branch / flex material class / standards boundary`
- glossary: yes
- supplier checklist: yes
- numeric density rule:
  - allow only class-level material anchors and exact-product exceptions where clearly supported
  - do not introduce unsupported standards, reliability, fabrication, or commercial numerics

## 9. In-Body Citation Plan

| Article section | Claim to support | Planned evidence |
| --- | --- | --- |
| quick answer block | `14-layer` often raises process-coordination and branch-review pressure | `methods-high-layer-rigid-board-manufacturability-context`, `methods-rigid-flex-stackup-and-bend-reliability-posture` |
| rigid-flex branch | rigid-flex is a separate route with separate review needs | `methods-rigid-flex-stackup-and-bend-reliability-posture` |
| material branch | flex / rigid-flex material discussion should stay class-aware and product-aware | `materials-flex-polyimide-and-lcp-class-source-coverage` |
| standards boundary | standards context exists, but draft thresholds are not reusable | `standards-ipc-rigid-flex-and-microvia-reliability-metadata`, `standards-hdi-design-reference-status-metadata` |

## 10. AI-SEO Primitives

- direct answer sentence:
  - `A 14-layer PCB usually becomes a process-management problem when dense stackup planning starts interacting with rigid-flex, transition-zone, or branch-construction decisions.`
- follow-on answer sentence:
  - `The safest public explanation keeps rigid-flex and flex-material discussion at workflow and class level while removing unsupported standards tables, bend-life numerics, and fabrication-rule ladders.`
- retrieval anchors:
  - `14 layer rigid flex PCB`
  - `14 layer PCB stackup`
  - `14 layer PCB design rules`
  - `14 layer flex material selection`
  - `14 layer PCB manufacturability`

## 11. Handoff To Template

- recommended template:
  - `prompts_template/shared/query.md`
- required overlay:
  - `prompts_template/hilpcb/query-overlay.md`
- writing posture:
  - concise engineering answer first
  - early fact table
  - explicit branch split between rigid board and rigid-flex route
  - standards-boundary section near the back half
- explicit exclusions:
  - no class-threshold tables
  - no bend-radius or flex-life tables
  - no via-geometry or transition-tolerance tables
  - no service / turnaround / coverage banners

## 12. Final Preflight

- keep:
  - rigid-flex branch posture
  - class-level flex-material framing
  - standards boundary support
- downgrade:
  - architecture examples
  - flex-material examples without exact product support
- delete:
  - class-threshold tables
  - rigid-flex reliability numerics
  - fabrication and turnaround numerics
- needs_source:
  - all fabrication-capability numerics
  - all reliability threshold numerics
  - all compliance-style proof claims

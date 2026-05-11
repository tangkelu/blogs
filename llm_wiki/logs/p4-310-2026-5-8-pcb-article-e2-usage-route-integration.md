# P4-310 PCB Article E2 Usage Route Integration

Date: 2026-05-08
Parent state: `after P4-283B and P4-309`
Execution mode: `controller_usage_route_integration_only`

## Purpose

Convert the `E2` article cluster from claim-family inventory into a controller-owned usage route surface for later writing agents.

This lane does not promote article-origin numerics, rule tables, stackup values, impedance tolerances, safety-distance minimums, vendor capability claims, or yield claims into reusable facts.

## Inputs Read

- `/code/blogs/tmps/PCB资料/PCB文章`
- `logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `docs/superpowers/plans/2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan.md`
- `/root/.codex/skills/llm-wiki-workflow/SKILL.md`

## Cluster Scope

`E2` includes these subfamilies:

- layout and routing manufacturability
- internal-layer and plane-purpose taxonomy
- layer-definition grammar
- stackup planning and reference-plane selection
- impedance rationale and impedance-control difficulty
- safety-distance taxonomy for traces, pads, copper, board edge, and components

## Route Decision

Controller outcome for this lane:

- `safe_reuse_classes` are open only for qualitative, taxonomy, and decision-frame reuse
- `blocked_classes` remain blocked for all exact design-rule and capability use
- `local_evidence_candidates` are allowed only as branded-shell-removed diagram preservation targets
- `official_source_recovery_targets` are required before any fact-layer promotion of numerics, defaults, or prescriptive rule values

## Safe Reuse Classes

### 1. Layout And Routing Manufacturability

Safe route:

- reuse as qualitative DFM framing only
- reuse that manufacturability must be considered before routing is frozen
- reuse that bend behavior, via count, path simplicity, and assembly access affect manufacturability
- reuse SMT versus THT constraint differences only as category-level guidance

Not safe here:

- any exact width, spacing, annular, hole, edge, or component-clearance number

### 2. Internal-Layer And Plane-Purpose Taxonomy

Safe route:

- reuse layer-role vocabulary for signal, power, ground, mechanical, keepout, paste, silk, and solder-mask intent
- reuse that ground or reference planes are chosen for return-path, shielding, and coupling-control reasons
- reuse split-plane caution only as a qualitative warning class

Not safe here:

- any plane size, offset, copper-balance, or adjacency rule number

### 3. Stackup Planning And Reference-Plane Selection

Safe route:

- reuse that stackup planning is a tradeoff among function, signal integrity, power integrity, EMC, and manufacturability
- reuse that reference-plane selection matters to loop area and field containment
- reuse layer-count choice only as a decision-family topic, not as a default recommendation

Not safe here:

- any default layer-count prescription
- any dielectric-thickness, copper-thickness, spacing, or stack ordering table

### 4. Impedance Rationale And Control Difficulty

Safe route:

- reuse controlled impedance as a geometry-plus-dielectric design problem
- reuse that process variation makes impedance control harder
- reuse `50 ohm` only as a common family label appearing in high-speed and RF discussion

Not safe here:

- any tolerance target, impedance window, geometry recipe, or fab capability claim
- any statement that a given stackup or trace geometry will achieve a target impedance without official stackup evidence

### 5. Safety-Distance Taxonomy

Safe route:

- reuse that spacing concerns split into electrical and non-electrical families
- reuse that traces, pads, copper pours, board edges, and component adjacency each create different spacing checks
- reuse spacing as a manufacturability, reliability, and assembly-risk topic family

Not safe here:

- any minimum spacing number
- any voltage-conditioned clearance rule
- any edge, pad, or component-spacing acceptance threshold

## Blocked Classes

- all exact line-width, line-spacing, copper-to-edge, pad-to-pad, pad-to-hole, component-to-component, and board-edge spacing claims
- all stackup geometry, dielectric, copper-weight, layer-order, and reference-plane distance values
- all impedance tables, tolerance percentages, error budgets, and manufacturability capability windows
- all safety-distance numerics, exception tables, and pass/fail thresholds
- all vendor-branded rule screenshots, QR shells, CTA surfaces, and software-preset claims
- all supplier capability, process-yield, process-stability, and quality-rate claims inferred only from article wording

## Local Evidence Candidates

These are eligible only for local preservation after branding-shell removal and only as diagram support, not authority for exact values.

- `PCB布局布线的可制造性设计.pdf`
  - routing-shape and assembly-clearance examples
  - board-edge and tall/low component placement risk visuals
- `PCB内层的可制造性设计.pdf`
  - internal-plane purpose diagrams
  - reference-plane and split-plane caution visuals
- `一文带你读懂PCB电路板设计中各种层的定义.pdf`
  - layer-definition grammar diagram
- `PCB叠层顺序规划配置方案.pdf`
  - stackup organization and layer-role visuals
- `PCB为什么常用50Ω阻抗？6大原因.pdf`
  - conceptual impedance rationale figures
- `PCB阻抗误差控制在5%，究竟有多难？.pdf`
  - process-variation and glass-fiber-effect concept figures
- `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
  - spacing-category diagrams for traces, pads, copper, board edge, and components

## Official-Source Recovery Targets

These are recovery targets, not yet satisfied evidence.

### Target Group A: Generic PCB Design Rule Authority

- IPC generic design-rule documents for conductor spacing, clearance framing, and board-level design-rule taxonomy
- IPC documents covering high-level layout, stackup, and conductor-clearance concepts

### Target Group B: Controlled-Impedance And Stackup Authority

- controlled-impedance guidance from IPC or equivalent standards bodies
- fabricator-issued stackup capability notes tied to named processes
- laminate manufacturer dielectric data needed for impedance calculations

### Target Group C: Safety-Distance Authority

- standards or official engineering guidance that tie spacing to voltage, insulation environment, and board construction
- official safety or reliability references that distinguish electrical clearance from assembly/mechanical spacing

### Target Group D: Assembly-Access And Board-Edge Authority

- official assembly-equipment or design-for-assembly guidance for component access, edge clearance, and mixed SMT/THT constraints
- named fab or assembly design guides only when date-scoped and explicitly treated as vendor-specific capability records

## Subfamily Routing Summary

| Subfamily | Safe reuse class | Blocked class | Local evidence candidate | Official-source recovery target |
| --- | --- | --- | --- | --- |
| Layout and routing manufacturability | qualitative DFM guidance | exact routing and clearance numerics | routing and placement visuals | IPC generic design guidance; dated fab/assembly guides |
| Layer-definition grammar | taxonomy vocabulary | any implied default rule value | layer-role diagrams | IPC terminology or official CAD/library guidance |
| Internal planes and reference planes | conceptual plane-purpose framing | plane offset and split-plane numeric rules | plane-purpose visuals | IPC stackup/reference-plane guidance |
| Stackup planning | tradeoff and decision framing | default stackup tables and geometry claims | stackup-organization visuals | fab stackup notes; laminate datasheets; IPC stackup guidance |
| Impedance rationale | conceptual impedance framing | tolerance, geometry, and capability claims | impedance concept figures | controlled-impedance standards and fab capability notes |
| Safety-distance taxonomy | category-level spacing checks | all minimums and exceptions | spacing-category diagrams | clearance/creepage and PCB design-rule authority |

## Status

`E2` is now `usage_route_integrated_at_controller_level_only`.

What is now true:

- later agents can safely reuse `E2` as a qualitative taxonomy and decision-frame lane
- later agents do not need to reopen the whole article cluster to know what is blocked
- local-evidence preservation targets and official-source recovery targets are now explicit

What is still not true:

- `E2` is not fact-promoted
- `E2` is not official-source-closed
- `E2` does not provide reusable numeric routing, stackup, impedance, or safety-distance values

## Recommended Next Action

Recommended next action: `official_source_recovery_first_for_safety_distance_and_impedance`, with optional local-evidence preservation only for clean diagrams that survive branding removal.

Reason:

- safety-distance and impedance are the highest-risk overclaim zones in `E2`
- those subfamilies are the least safe to reuse from article wording alone
- stackup and layout decision framing can already be reused qualitatively without further article reread

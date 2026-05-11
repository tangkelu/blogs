# P4-283B PCB Article Cluster E2 Layout Routing Stackup Layers And Impedance Claim Family Map

Date: 2026-05-07
Parent: `P4-283`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Execution mode: `claim_family_boundary_mapping_only`

## Purpose

Map the `E2` layout / routing / stackup / layers / impedance cluster into English canonical claim families only.

This log does not promote article numerics, exact geometries, impedance tables, or safety-distance values into `facts/`.

## E2 Subclusters

- layout and routing manufacturability
- internal-layer and plane-purpose taxonomy
- layer-definition grammar for PCB stackups
- stackup planning and reference-plane selection
- impedance rationale and impedance-control difficulty
- safety-distance families for conductors, pads, copper, board edge, and components

## Safe Claim Families Learned

- DFM rules for layout and routing must be set against manufacturing constraints before routing is finalized
- routing manufacturability depends on bend behavior, via count, and path optimization
- SMT and THT layout constraints differ by assembly method and machine access
- board layers carry different functions, with mechanical, keepout, paste, silk, solder-mask, signal, power, and ground semantics separated by intent
- stackup planning is a tradeoff among functional requirements, signal integrity, power integrity, and manufacturability
- ground planes are preferred reference planes when the goal is lower radiation and better shielding
- internal planes and adjacent reference planes are used to control loop area, coupling, and power-plane impedance
- controlled impedance is a characteristic-impedance problem tied to geometry, dielectric, and surrounding structure
- 50 ohms is treated as a common impedance family for high-speed and RF use
- impedance-control difficulty grows because multiple process variables introduce cumulative error
- PCB safety-distance reasoning splits into electrical and non-electrical families
- spacing between traces, pads, copper pours, board edges, and components is a manufacturability and reliability issue

## Blocked Classes

- all exact line widths, trace-to-trace gaps, pad-hole diameters, pad-width minima, copper-to-edge values, and component-spacing values
- all impedance error percentages, tolerance tables, and vendor-specific capability charts
- all stackup geometry numbers, plane-offset numbers, dielectric-thickness numbers, and rule tables
- all safety-distance numerics, minimums, and conditional exceptions
- all vendor-branded rule tables, download prompts, QR/CTA shells, and software screenshots with promotional framing

## Per-PDF Evidence Map

- `PCB布局布线的可制造性设计.pdf`
  - layout DFM, routing DFM, SMT spacing, and DIP / wave-solder compatibility families
  - board-edge assembly risk and component-height risk are present
  - exact spacing values remain blocked
- `PCB内层的可制造性设计.pdf`
  - internal-layer purpose, power/ground plane taxonomy, reference-plane selection, and split-plane routing caution
  - plane sizing and offset values remain blocked
- `一文带你读懂PCB电路板设计中各种层的定义.pdf`
  - layer-definition grammar for mechanical, keepout, overlay, paste, and solder layers
  - useful as canonical layer vocabulary, not as a source of numeric authority
- `PCB叠层顺序规划配置方案.pdf`
  - stackup planning, number-of-layers tradeoff, and plane/signal layering family
  - preserved as stackup-organization evidence only
- `PCB为什么常用50Ω阻抗？6大原因.pdf`
  - common-impedance rationale, characteristic-impedance framing, and RF/high-speed usage family
  - 50 ohm is canonical only as a family label here; supporting arguments stay qualitative
- `PCB阻抗误差控制在5%，究竟有多难？.pdf`
  - impedance-control difficulty, process-variation accumulation, and glass-fiber effect family
  - exact target percentages and feasibility claims remain blocked
- `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
  - electrical and non-electrical safety-distance taxonomy
  - trace, pad, copper-pour, board-edge, and component-spacing families
  - exact minimums remain blocked
- `印制电路板设计重点.pdf`
  - general design-priority framing overlaps the cluster, but it is mostly governance-like support rather than a primary E2 authority source

## Image / Table Candidates Worth Preserving Locally

- `PCB布局布线的可制造性设计.pdf` p1-p4: layout spacing and routing guidance figures
- `PCB布局布线的可制造性设计.pdf` p3-p4: board-edge and high/low-component clearance examples
- `PCB内层的可制造性设计.pdf` p1-p2: plane-purpose and reference-plane diagrams
- `PCB叠层顺序规划配置方案.pdf` p1-p4: stackup-organization visuals
- `PCB为什么常用50Ω阻抗？6大原因.pdf` p1-p4: impedance rationale figures
- `PCB阻抗误差控制在5%，究竟有多难？.pdf` p1-p4: process-variation and glass-fiber effect figures
- `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` p1-p3: spacing-rule figures
- `一文带你读懂PCB电路板设计中各种层的定义.pdf` p1-p2: layer-definition diagram

Branding-removal notes:

- crop out `华秋DFM` banners, QR codes, and CTA/download shells
- keep only the technical diagram/table core where separable
- remove repeated top-shell branding before preserving local evidence

## Contamination Patterns To Exclude

- repeated download prompts and community-group QR surfaces
- vendor pitch language about ease, speed, or universal best practice
- software-rule screenshots treated as universal authority
- any table or figure that is only usable after removing branding shell contamination

## Status

`E2` is complete at claim-family level only. It is ready for later narrower lane execution, but no exact numeric, geometry, impedance-table, or safety-distance promotion was performed.

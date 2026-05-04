---
topic_id: "processes-hil-pcb-product-family-capability-map"
title: "HIL PCB Product Family Capability Map And Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "processes-hil-single-double-layer-capability-specs"
  - "processes-hil-multilayer-capability-specs"
  - "processes-hil-fr4-capability-specs"
  - "processes-hil-high-tg-capability-specs"
  - "processes-hil-heavy-copper-capability-specs"
  - "processes-hil-halogen-free-capability-specs"
  - "processes-hil-high-speed-capability-specs"
  - "processes-hil-high-thermal-capability-specs"
  - "processes-hil-high-frequency-capability-specs"
  - "processes-hil-rogers-capability-specs"
  - "processes-hil-teflon-pcb-capability-specs"
  - "processes-hil-hdi-capability-specs"
  - "processes-hil-rigid-flex-capability-specs"
  - "processes-hil-backplane-capability-specs"
  - "processes-hil-ic-substrate-capability-specs"
  - "processes-hil-flex-capability-specs"
source_ids:
  - "frontendhil-single-double-layer-pcb-product-en"
  - "frontendhil-multilayer-pcb-product-en"
  - "frontendhil-fr4-pcb-product-en"
  - "frontendhil-high-tg-pcb-product-en"
  - "frontendhil-heavy-copper-pcb-product-en"
  - "frontendhil-halogen-free-pcb-product-en"
  - "frontendhil-high-speed-pcb-product-en"
  - "frontendhil-high-thermal-pcb-product-en"
  - "frontendhil-high-frequency-pcb-product-en"
  - "frontendhil-rogers-pcb-product-en"
  - "frontendhil-teflon-pcb-product-en"
  - "frontendhil-hdi-pcb-product-en"
  - "frontendhil-rigid-flex-pcb-product-en"
  - "frontendhil-backplane-pcb-product-en"
  - "frontendhil-ic-substrate-pcb-product-en"
  - "frontendhil-flex-pcb-product-en"
tags: ["hil", "processes", "pcb", "capability-map", "product-family", "rf", "hdi", "heavy-copper", "thermal", "high-speed", "backplane", "ic-substrate"]
---

# Definition

> The HIL PCB product family is structured as 15 separate named product lines, each with distinct material choices, layer configurations, manufacturing process routes, and application contexts. The governing principle is capability-first selection: identify the design driver (layer density, thermal management, frequency, copper weight, flex mechanics, or substrate precision) before selecting a product family, rather than treating all HIL PCB work as a generic multilayer problem.

## Why This Topic Matters

- HIL internal product pages do not flatten all PCB builds into a single "advanced PCB" frame.
- Each product family page carries distinct engineering vocabulary that becomes incorrect or misleading if copied into the wrong context.
- This wiki page provides one stable routing frame for prompt consumption, rewrite tasks, and internal blog production that needs to draw on HIL capability data.

## Product Family Map

### Layer-Count Entry Families

| Family | Fact Card | Key Parameters | Governance Boundary |
|--------|-----------|----------------|---------------------|
| **1–2 Layer** | `processes-hil-single-double-layer-capability-specs` | 24-48h quick-turn, 150/150 μm trace/space, Tg 130-170°C, <0.75% bow | Use when design fits 1-2 layers; do not apply multilayer or HDI vocabulary |
| **Multilayer (4–64L)** | `processes-hil-multilayer-capability-specs` | 4–64 layers, ±15-25 μm registration, ±5% impedance, 75/75 μm standard | Use as the default multilayer frame; use HDI frame when microvia density is the driver |
| **FR-4** | `processes-hil-fr4-capability-specs` | 1–32 layers, Tg 130-180°C, 0.075 mm laser microvia, ±5% impedance, 12h express | Base-material-first framing; escalate to High-Tg or High-Speed when thermal or loss drives selection |

### Thermal and Reliability Families

| Family | Fact Card | Key Parameters | Governance Boundary |
|--------|-----------|----------------|---------------------|
| **High-Tg** | `processes-hil-high-tg-capability-specs` | Tg 170-200°C, Z-axis CTE 50-70 ppm/°C below Tg, 3×260°C reflow, -40°C to +125°C cycling | Use when multiple reflow cycles, elevated operating temperature, or automotive reliability class drives selection |
| **Heavy Copper** | `processes-hil-heavy-copper-capability-specs` | 3-20 oz copper, 30-50A justification threshold (IPC-2152), ±10% plating uniformity, ≤0.75% warpage | Use when current load exceeds 30A or power converter thermal spreading drives copper weight selection |
| **High-Thermal (MCPCB/Ceramic)** | `processes-hil-high-thermal-capability-specs` | MCPCB: 1-3 W/m·K (dielectric-limited); Ceramic AlN: ~150-170 W/m·K; Ra ≤3 μm flatness | Use when LED, power semiconductor, or RF PA thermal management is the board design driver; keep MCPCB and ceramic on separate posture tracks |
| **Halogen-Free** | `processes-hil-halogen-free-capability-specs` | <900 ppm Cl/Br (IEC 61249-2-21), Tg 170-200°C, Df 0.009-0.012, 56G PAM4 ready | Use when environmental compliance, low-smoke requirements, or high-speed + halogen-free combination drives selection |

### Signal-Integrity and RF Families

| Family | Fact Card | Key Parameters | Governance Boundary |
|--------|-----------|----------------|---------------------|
| **High-Speed Digital** | `processes-hil-high-speed-capability-specs` | 25–112 Gbps PAM4/NRZ, PCIe Gen5/6, back-drilling to 5 mil stubs, Df 0.001-0.004 @ 10 GHz | Use when channel loss budget or interface protocol drives material and stackup selection; do not apply to generic multilayer without SI analysis |
| **High-Frequency RF** | `processes-hil-high-frequency-capability-specs` | Sub-6 GHz to mmWave, VNA to 67 GHz S-parameter, Df 0.0009-0.004, hybrid stackups | Use when signal frequency above ~1 GHz drives material selection; pair with Rogers or Teflon family for specific material choices |
| **Rogers RF** | `processes-hil-rogers-capability-specs` | RO4000/RO3000/RT-duroid, 1-50 layers hybrid, plasma activation, VNA to 40 GHz | Use when Rogers brand material is the specified RF substrate; includes process-specific vocabulary (plasma activation, staged lamination, CTE management) |
| **Teflon (PTFE)** | `processes-hil-teflon-pcb-capability-specs` | Df 0.0009-0.0015, Dk 2.1-2.3, 40+ GHz, ±3-5% impedance, VNA to 40 GHz, hybrid stackups 30-50% cost reduction | Use when PTFE/Teflon substrate is required for ultra-low-loss RF applications; includes PTFE-specific process vocabulary (plasma activation, rolled/VLP copper, staged lamination) |

### Density and Advanced Structure Families

| Family | Fact Card | Key Parameters | Governance Boundary |
|--------|-----------|----------------|---------------------|
| **HDI** | `processes-hil-hdi-capability-specs` | 50–75 μm microvias, 1+N+1 to any-layer, VIPPO copper fill, 4–60+ layers, IATF 16949 | Use when microvia build-up and fine-pitch BGA escape routing drives the density frame |
| **Rigid-Flex** | `processes-hil-rigid-flex-capability-specs` | 3-24+ layers, 50-75 μm trace/space, bookbinder construction, dynamic flex 10× thickness bend radius, AS9100 | Use when integration of rigid and flex zones in one assembly drives the mechanical frame; not interchangeable with HDI |
| **Backplane** | `processes-hil-backplane-capability-specs` | 16-64 layers, 600×800 mm panels, 25+ Gbps, ±25 μm registration, back-drill, AS9100D | Use when large-format, high-layer-count connector-matrix structures drive the design frame |
| **IC Substrate** | `processes-hil-ic-substrate-capability-specs` | SAP 15-20 μm line/space, ABF/BT, 25-50 μm microvias, flip-chip ready, ≤0.5% warpage, 4-50 layers | Use when semiconductor packaging-level density (SAP process, flip-chip) drives the substrate frame; significantly different from standard HDI or backplane vocabulary |
| **Flex (FPC)** | `processes-hil-flex-capability-specs` | 1–16 layers, 25/25 μm trace/space, dynamic bend 10× thickness (≥1M cycles), ENEPIG finish, 0.05–0.50 mm thickness | Use when pure flex circuit is required (no rigid zones); use Rigid-Flex family when combined rigid+flex zones are needed |

## Engineering Boundaries

- Select the product family by the **primary design driver**, not by the highest-tier label available.
- Keep **RF families** (High-Frequency, Rogers, Teflon) on separate tracks from **High-Speed Digital**; shared vocabulary (Df, impedance) does not mean interchangeable application posture.
- Keep **MCPCB** and **Ceramic** on separate tracks within the High-Thermal family; alumina (~18-25 W/m·K) and AlN (~150-170 W/m·K) are not interchangeable.
- Keep **IC Substrate** vocabulary (SAP, ABF, mSAP, flip-chip, fine-line) separate from standard HDI vocabulary; the process routes and cost profiles are fundamentally different.
- Keep **Backplane** vocabulary (large-format, connector-matrix, high-aspect-ratio drilling) separate from generic multilayer vocabulary.
- Treat every numeric parameter as refresh-sensitive; use the individual fact cards as the source of record, not this page.

## Common Misreadings

- `High-Tg` does not automatically mean `High-Speed`; thermal stability and signal loss are separate material properties.
- `HDI` does not mean `IC Substrate`; microvia HDI and SAP-based substrate fabrication are different process families.
- `Halogen-Free` does not automatically mean `High-Speed`; the halogen-free property addresses flame retardant chemistry, not signal loss.
- `Rogers` and `Teflon (PTFE)` are not synonymous; Rogers materials include PTFE-based products but also non-PTFE hydrocarbon laminates.
- `Rigid-Flex` and `Flex` are not interchangeable; HIL rigid-flex combines rigid and flex zones in one structure, while HIL Flex (FPC) covers pure flexible circuits. Design rules, process routes, and cost profiles differ.
- `Heavy Copper` does not automatically imply `High-Thermal`; copper weight addresses current-carrying capacity, not the thermal platform material system.

## Must Refresh Before Publishing

- Layer-count, copper-weight, drill, line/space, and impedance-limit claims for any specific family
- Bend-radius, flex-life, and dynamic flex cycle claims
- Thermal-conductivity and dielectric-property numerics for material-specific postures
- Lead-time and quick-turn availability claims
- Certification, quality-system, or sector-approval statements
- VNA frequency range limits (may depend on fixturing availability)

## Related Fact Cards

See the 15 individual HIL capability fact cards in `facts/processes/hil-*-capability-specs.md` for detailed parameter tables.

For the APT capability family equivalent, see `wiki/processes/apt-capability-family-map-and-boundaries.md`.

For process governance (inspection, traceability, NPI flow), see `wiki/processes/pcba-npi-to-mass-production-flow.md`.

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/single-double-layer-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/multilayer-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/fr4-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-tg-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/heavy-copper-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/halogen-free-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-thermal-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/teflon-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/backplane-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/ic-substrate-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json

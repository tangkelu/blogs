---
topic_id: "processes-hil-assembly-capability-map"
title: "HIL Assembly Capability Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "processes-hil-assembly-capability-gap-map"
  - "processes-hil-smt-assembly-capability-specs"
  - "processes-hil-through-hole-assembly-capability-specs"
  - "processes-hil-small-batch-assembly-capability-specs"
  - "processes-hil-large-volume-assembly-capability-specs"
  - "processes-hil-turnkey-assembly-capability-specs"
  - "processes-hil-box-build-assembly-capability-specs"
  - "processes-process-governance-gap-map"
source_ids:
  - "frontendhil-smt-assembly-product-en"
  - "frontendhil-through-hole-assembly-product-en"
  - "frontendhil-small-batch-assembly-product-en"
  - "frontendhil-large-volume-assembly-product-en"
  - "frontendhil-turnkey-assembly-product-en"
  - "frontendhil-box-build-assembly-product-en"
tags: ["hil", "pcba", "assembly", "smt", "tht", "small-batch", "large-volume", "turnkey", "box-build", "capability-map", "governance"]
---

# Definition

> HIL PCBA assembly covers six distinct service types: SMT, Through-Hole (THT), Small Batch/NPI, Large Volume, Turnkey, and Box Build. Each has a dedicated fact card sourced from HIL internal JSON. This wiki page is the primary routing and governance frame for HIL assembly knowledge — it shows what can be stated, what must be hedged, what is blocked, and how the six types relate to each other.

## Why This Topic Matters

- HIL assembly knowledge was previously only indirectly absorbed into shared APT/HIL flow pages (NPI-to-production, mixed-tech, conformal coating). This page gives HIL assembly a dedicated, navigable knowledge layer.
- Without this aggregation, later AI agents have no stable anchor to distinguish HIL-specific assembly posture from APT-specific posture or from generic PCBA claims.
- The six service types are not interchangeable: SMT ≠ Turnkey ≠ Box Build; each has distinct scope boundaries, process gates, and blocked claims.

---

## Service Type Routing Map

| Service Type | Best For | Volume Range | Key Differentiator |
|-------------|----------|-------------|-------------------|
| **SMT Assembly** | Standard board-level assembly; fine-pitch and BGA | Any | ±8–25 μm placement; 008004 capable; 3D SPI + AOI + X-ray gates |
| **Through-Hole (THT)** | Connectors, transformers, power components; vibration/shock environments | Any | Wave/selective/robotic; Class 2/3 barrel fill; press-fit capable |
| **Small Batch / NPI** | Prototypes, first articles, design validation builds | 10–5,000 pcs | 3–10 day quick-turn; production-grade process gates from unit 1 |
| **Large Volume** | Mass production; programs requiring SPC rigor | 10,000–50M+ units/year | SPC Cpk ≥1.33; MES-ERP sync; predictive maintenance |
| **Turnkey** | Full BOM management; multi-sourcing complexity | Prototype to 1M+ | BOM scrub, EOL management, 3–5 qualified alternates, broker AS6081 controls |
| **Box Build** | System integration; finished-product delivery | Program-defined | PCBA + enclosure + harness + firmware + ESS; D2C fulfillment |

---

## SMT Assembly

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Placement accuracy**: ±25 μm standard, ±8 μm advanced (@ 3σ)
- **Minimum component size**: 008004 (0.25 × 0.125 mm); BGA/CSP to 0.2 mm pitch
- **Solder paste**: Stencil 100–150 μm, ±10% volume control, ~95–100% transfer efficiency
- **Inspection gates**: 3D SPI (post-print) → pre-placement vision → post-reflow AOI (>95% defect detection) → sample X-ray for BGA/QFN
- **Reflow**: Nitrogen available; ±5°C ΔT temperature control; profile zones digitally logged
- **Quality metrics**: FPY ≥98%, DPPM <500 (stated historical/typical)
- **Assembly types**: SMT-only, THT-only, mixed, double-sided, PoP, SiP
- **Additional**: Selective solder, wave solder, underfill, conformal coating, ionic contamination control ≤1.56 μg/cm²

### Blocked / Refresh-Required

- FPY/DPPM as SLA guarantees → operational targets only
- Specific stencil design parameters → design-dependent
- Ionic contamination threshold applicability → verify for specific application class

---

## Through-Hole (THT) Assembly

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Soldering methods**: Wave (3–4 s dwell, 100–130°C preheat), selective (±0.5 mm accuracy, nitrogen), robotic, hand rework
- **Barrel fill**: Class 2 >75%, Class 3 >90%; wetting angle 30°–60°
- **Press-fit**: 10–50 N per pin; gas-tight connection; solder-free option
- **Primary alloy**: Lead-free SAC305; Sn63/Pb37 and HMP (high-temp) available
- **Pull strength**: 5–10 lb per lead (typical; vibration/shock advantage vs SMT)
- **Inspection**: AOI 50–100 μm resolution, >95% detection; X-ray for barrel fill; cross-section 20–25 μm plating
- **Testing**: ICT >90% coverage; FCT; boundary-scan; burn-in 60–85°C, 24–168 h
- **Nitrogen**: Selective soldering; 50–70% oxidation reduction, significant dross reduction

### Blocked / Refresh-Required

- Barrel fill guarantee for any specific hole aspect ratio → depends on preheat, flux, via design
- Press-fit force for specific connector families → connector-specific
- Burn-in scope and duration → program requirement; not universal default

---

## Small Batch / NPI Assembly

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Volume range**: 10–5,000 pcs; prototype and NPI focus
- **Quick-turn**: 3–10 days (stated; refresh-required per current workload)
- **Same production gates as mass production**: 3D SPI, AOI, sample X-ray; no "prototype quality" shortcut
- **Component**: 0201 standard, 01005 and fine-pitch BGA 0.25 mm advanced
- **FPY**: >98%; DPPM <500 (stated)
- **BGA voiding**: ≤25% per IPC-7095
- **ESD**: ANSI/ESD S20.20 continuous monitoring
- **Testing**: ICT, FCT, boundary-scan options
- **Handoff**: Small batch build data feeds volume ramp predictive models

### Blocked / Refresh-Required

- 3–10 day lead time as guarantee → workload-dependent; confirm at order time
- ICT fixture cost threshold → depends on design complexity and fixture amortization
- Design change revision control specifics → project-level QMS workflow

---

## Large Volume Assembly

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Annual capacity**: Up to 50M+ units/year; 10,000–1,000,000 standard range
- **Line throughput**: 150,000–500,000 CPH per line (mix-dependent)
- **SPC**: Real-time solder paste volume (±10%), placement accuracy (±25–50 μm), reflow stability; Cpk ≥1.33 threshold; automatic deviation flagging; micro-stoppages for correction
- **Quality**: FPY 98–99.5% (mature programs), DPPM <500
- **Component**: 008004 to 50×50 mm; BGA repeatability ±8–15 μm; SMT, THT, mixed, PoP, Micro-BGA, SiP
- **Inspection**: 3D SPI >98% detection; pre/post-reflow AOI; 3D AXI for hidden joints
- **Traceability**: MES-ERP synchronization; IPC-1782 lot/date-code per serial number; full reel/date-code/operator history
- **Maintenance**: Predictive (30–40% downtime reduction stated); OEE 70–85% typical
- **Standards**: IPC-A-610, IPC-7095; IATF 16949 / ISO 13485 ready (not current validity proof)

### Blocked / Refresh-Required

- Specific CPH as guaranteed throughput → mix-dependent; varies by program
- OEE 70–85% as a contractual target → operational typical; not a SLA
- Cpk ≥1.33 as guaranteed → SPC target; sample-size dependent calculation
- IATF 16949 / ISO 13485 current certificate validity → requires live certificate confirmation

---

## Turnkey Assembly

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Service types**: Kitted (customer provides parts), partial turnkey, full turnkey (complete BOM management), box build
- **Scale**: Prototype through 1M+ units
- **Schedule benefit**: Eliminates ~15–25% multi-vendor delays (stated; program-dependent)
- **Assembly technologies**: SMT, THT, mixed, PoP, SiP, fine-pitch BGA
- **Board types**: FR-4, multilayer, rigid-flex, flex, MCPCB, ceramic
- **Supply chain**: BOM scrub for lifecycle/alternates; EOL alerts 6–12 months advance; 3–5 qualified alternates; authorized distribution primary; broker controls (XRF, decapsulation, AS6081)
- **Placement**: ±25 μm standard, ±8 μm advanced; 3D SPI, AOI >95%, X-ray sample void ≤25%
- **Testing**: ICT, flying probe, boundary-scan, FCT
- **Quality**: FPY >98–99%, DPPM <500 (mature programs)
- **Additional**: Conformal coating 25–75 μm, firmware loading, ECO/revision control through QMS

### Blocked / Refresh-Required

- Multi-vendor delay reduction (~15–25%) as a guarantee → program-specific
- Broker authentication result for any specific lot → requires actual AS6081/XRF/decapsulation record
- 3–5 alternates as fully qualified alternates → qualification status is program/customer-dependent

---

## Box Build (System Integration)

### What Can Be Stated (Internal Tier-2, with Hedge)

- **Scope**: Bare PCB → finished product: PCBA + enclosure + cable/harness + firmware + system test
- **Integration levels**: Standard sub-assembly → complete ready-to-ship product
- **Enclosures**: Plastic and metal standard; custom fabrication, rack-mount, IP-rated advanced
- **Cable/harness**: Point-to-point and ribbon standard; complex custom, RF/coaxial, overmolding advanced; IPC/WHMA-A-620 workmanship standard
- **Process control**: SPC checkpoints (torque, solder, connector mating); digitally logged torque per serial; ESD ANSI/ESD S20.20
- **Integration sequence**: PCBA install (controlled torque) → harness routing (strain relief) → thermal/EMI → firmware loading → parametric configuration
- **Testing**: Functional (boundary scan, ICT), ESS, burn-in 60–85°C 24–168 h (optional), temperature cycling, vibration, humidity
- **Traceability**: MES full component + serialization per unit + digital logs (torque, calibration, ESD)
- **Fulfillment**: Retail packaging, kitting, D2C shipping
- **Lead time**: Standard 30 days, expedited 15 days (stated; refresh-required)
- **FPY**: >98–99%

### Blocked / Refresh-Required

- ESS scope (screening levels, duration, accept/reject criteria) → product-specific; not standardized
- 15-day expedited lead time as guarantee → depends on program complexity and custom enclosure requirements
- D2C fulfillment logistics details → requires separate coordination

---

## Common Misreadings to Avoid

- **"FPY >98% = every lot passes first time"** — FPY is a historical/typical metric for mature programs; new programs typically ramp up
- **"Cpk ≥1.33 = guaranteed"** — SPC target; requires sufficient sample size and ongoing monitoring; not a contractual floor
- **"3–10 day quick-turn = always available"** — Lead time stated as service posture; confirm at order time against current workload
- **"IATF 16949 / ISO 13485 listed = currently valid and in scope for your project"** — Certification scope is site/process-specific; verify current certificate
- **"Turnkey = no component risk"** — EOL management and broker controls reduce risk; they do not eliminate it or guarantee part authenticity without specific traceability records
- **"Box Build = only PCB assembly"** — Box build extends to enclosure, harness, firmware, system test, and fulfillment; it is a distinct service tier from board-level PCBA

---

## Engineering Boundaries

- Use SMT capability metrics for board-level design feasibility checks; do not use as guaranteed manufacturing limits for a specific product.
- Use THT barrel fill targets (Class 2 >75%, Class 3 >90%) as baseline requirements, not as design targets without considering hole geometry and thermal mass.
- Keep small-batch and large-volume metrics separate: small-batch is NPI-optimized (speed + flexibility); large-volume is throughput-optimized (SPC rigor + predictive maintenance).
- Treat turnkey supply chain claims (EOL lead time, alternates count) as posture statements, not as binding commitments.
- Box build testing scope (ESS, burn-in) must be defined per program requirements, not assumed as universal.

## Must Refresh Before Publishing

- Any lead-time claim (3–10 day, 15 day, 30 day) — confirm against current workload
- Any certification validity claim (IATF 16949, ISO 13485) — verify current certificate
- Any capacity or OEE figure — operational metrics that change over time
- Any specific equipment model references — verify against current HIL line configuration
- Any lot-specific quality metric or traceability record claim — requires actual build data

## Related Fact Cards

- `processes-hil-assembly-capability-gap-map` — coverage state and blocked claims map (primary companion)
- `processes-hil-smt-assembly-capability-specs` — SMT detail
- `processes-hil-through-hole-assembly-capability-specs` — THT detail
- `processes-hil-small-batch-assembly-capability-specs` — small batch/NPI detail
- `processes-hil-large-volume-assembly-capability-specs` — large volume/mass production detail
- `processes-hil-turnkey-assembly-capability-specs` — turnkey detail
- `processes-hil-box-build-assembly-capability-specs` — box build detail
- `processes-process-governance-gap-map` — overall process governance coverage state

## Related Wiki Pages

- `wiki/processes/pcba-npi-to-mass-production-flow.md` — APT/HIL shared NPI-to-production governance flow
- `wiki/processes/mixed-technology-solder-route-selection.md` — SMT/THT route selection
- `wiki/processes/conformal-coating-application-readiness-map.md` — conformal coating governance
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` — BGA/hidden joint inspection
- `wiki/processes/selective-solder-fixture-and-access-planning.md` — selective solder planning

## Primary Sources

- `/code/hileap/frontendHIL/public/static/products/en/smt-assembly.json`
- `/code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json`
- `/code/hileap/frontendHIL/public/static/products/en/small-batch-assembly.json`
- `/code/hileap/frontendHIL/public/static/products/en/large-volume-assembly.json`
- `/code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json`
- `/code/hileap/frontendHIL/public/static/products/en/box-build-assembly.json`

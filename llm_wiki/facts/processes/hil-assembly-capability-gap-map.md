---
fact_id: "processes-hil-assembly-capability-gap-map"
title: "HIL assembly capability coverage map: six assembly types with explicit coverage state, blocked claims, and residual gaps"
topic: "HIL PCBA assembly capability governance and gap mapping"
category: "processes"
status: "active"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendhil-smt-assembly-product-en"
  - "frontendhil-through-hole-assembly-product-en"
  - "frontendhil-small-batch-assembly-product-en"
  - "frontendhil-large-volume-assembly-product-en"
  - "frontendhil-turnkey-assembly-product-en"
  - "frontendhil-box-build-assembly-product-en"
tags: ["hil", "pcba", "assembly", "smt", "tht", "turnkey", "box-build", "gap-map", "governance", "capability"]
---

# Canonical Summary

> HIL offers six distinct assembly capability types: SMT, Through-Hole (THT), Small Batch (prototype/NPI), Large Volume (mass production), Turnkey (full BOM management), and Box Build (system integration). All six have dedicated fact cards sourced from HIL internal JSON. None currently have a dedicated wiki aggregation page; the knowledge is absorbed into shared APT/HIL flow pages. This fact card maps the coverage state, blocked claims, and residual gaps per assembly type.

---

## Coverage State By Assembly Type

| Assembly Type | Fact Card | Source Tier | Wiki Aggregation |
|--------------|-----------|-------------|-----------------|
| SMT Assembly | `processes-hil-smt-assembly-capability-specs` | Tier-2 internal | Absorbed into `pcba-npi-to-mass-production-flow.md` |
| Through-Hole (THT) | `processes-hil-through-hole-assembly-capability-specs` | Tier-2 internal | Absorbed into `mixed-technology-solder-route-selection.md` |
| Small Batch / NPI | `processes-hil-small-batch-assembly-capability-specs` | Tier-2 internal | Absorbed into `pcba-npi-to-mass-production-flow.md` |
| Large Volume | `processes-hil-large-volume-assembly-capability-specs` | Tier-2 internal | Absorbed into `pcba-npi-to-mass-production-flow.md` |
| Turnkey | `processes-hil-turnkey-assembly-capability-specs` | Tier-2 internal | Absorbed into `pcba-npi-to-mass-production-flow.md` |
| Box Build | `processes-hil-box-build-assembly-capability-specs` | Tier-2 internal | Now dedicated: `wiki/processes/hil-assembly-capability-map.md` (P4-152) |

All six assembly types now also have dedicated aggregation in `wiki/processes/hil-assembly-capability-map.md` created in P4-152.

---

## Capability Snapshot Per Type (Internal, Refresh-Required)

### SMT Assembly
- Placement: ±8–25 μm @ 3σ; components down to 008004 (0.25×0.125 mm), BGA/CSP to 0.2 mm pitch
- Stencil: 100–150 μm thickness, ±10% volume control, ~95–100% transfer efficiency
- Inspection: 3D SPI + pre/post AOI + sample X-ray for BGA/QFN
- Quality: FPY ≥98%, DPPM <500 (stated; point-in-time)
- Traceability: MES per lot; SPI-AOI correlation; paste lot tracking

### Through-Hole (THT)
- Methods: Wave (3–4 s dwell, 100–130°C preheat), selective (±0.5 mm, nitrogen), robotic, hand
- Barrel fill: Class 2 >75%, Class 3 >90%; wetting angle 30°–60°
- Press-fit: 10–50 N per pin; gas-tight connection
- Testing: ICT >90% coverage; FCT per spec; burn-in 60–85°C, 24–168 h (lifecycle-critical)
- Alloys: Lead-free SAC305 primary; Sn63/Pb37 and HMP available

### Small Batch / NPI
- Volume: 10–5,000 pcs; 3–10 day quick-turn
- Same production gates as mass production (3D SPI, AOI, X-ray sample)
- Fine-pitch BGA to 0.25 mm pitch; FPY >98%, DPPM <500
- ESD: ANSI/ESD S20.20; ICT/FCT/boundary-scan options
- Data feeds predictive models for volume ramp

### Large Volume
- Capacity: up to 50M+ units/year; 150k–500k CPH per line
- SPC: real-time monitoring, Cpk ≥1.33 threshold, automatic deviation flagging
- Quality: FPY 98–99.5% (mature programs), DPPM <500
- Traceability: MES-ERP sync; IPC-1782 lot/date-code per serial number
- Predictive maintenance: 30–40% downtime reduction; OEE 70–85% typical

### Turnkey
- Service types: kitted / partial turnkey / full turnkey / box build
- Scale: prototype to 1M+ units; eliminates ~15–25% multi-vendor delays (stated)
- Supply chain: BOM scrub, EOL alerts 6–12 months advance, 3–5 qualified alternates, authorized distribution primary, broker AS6081 authentication
- Additional: conformal coating 25–75 μm, firmware loading, ECO/revision control through QMS

### Box Build
- Scope: bare PCB to finished product — PCBA + enclosure + cable/harness + firmware + system test
- Integration levels: standard sub-assembly to complete ready-to-ship product
- Testing: functional, ESS, burn-in (60–85°C, 24–168 h optional), temperature cycling, vibration, humidity
- Lead time: standard 30 days, expedited 15 days (stated; refresh-required)
- Cable/harness standard: IPC/WHMA-A-620 workmanship

---

## Blocked Claims (Maintained)

| Blocked Claim | Reason |
|--------------|--------|
| Exact process windows (reflow temperatures, wave parameters) | Internal JSON point-in-time; not contractual process recipe |
| Line capacity proof (specific CPH, OEE as guaranteed) | Operational metrics that vary by program mix and equipment state |
| Yield or DPPM as guaranteed SLA | Stated as historical/typical; not a guaranteed performance contract |
| Customer-approval status or qualification records | Not in any internal source |
| Certification validity claims (IATF 16949, ISO 13485 current) | Require current certificate from certification body |
| Lead-time guarantees (15-day, 30-day, 3-10 day) | Stated as service levels; actual times depend on program conditions |
| Cpk ≥1.33 as a guaranteed process spec | SPC target; not a contractual guarantee for every lot |
| Broker authentication proof for specific lots | Requires actual AS6081/XRF/decapsulation records |

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| HIL PCB board-type capabilities wiki aggregation | Not covered in this lane (assembly-only scope) | Covered separately in `process-governance-gap-map.md`; reopen when PCB family wiki aggregation lane is assigned |
| Actual current certificate validity (IATF 16949, ISO 13485) | Not in any internal source | Obtain from HIL current certificate records |
| Specific equipment models (SMT lines, AOI systems) | Internal JSON references equipment classes, not current model numbers | Refresh against current HIL equipment list |
| ICT fixture investment thresholds | Not stated | Available on request from HIL engineering |
| Conformal coating material types (acrylic, silicone, urethane) | Not differentiated in internal sources | Covered in conformal coating governance wiki separately |

---

## Conditions And Methods

- Use individual fact cards for detailed parameter values; use `wiki/processes/hil-assembly-capability-map.md` for routing and governance context.
- All numeric values are from HIL internal JSON (Tier-2); hedge with "as stated in HIL public capability profile" for external use.
- Pair FPY/DPPM/Cpk values with "mature program, typical conditions" qualifier — do not present as universal guarantees.
- Use blocked claims list to resist pressure to publish lead-time or capacity guarantees.

## Related Fact Cards

- `processes-hil-smt-assembly-capability-specs`
- `processes-hil-through-hole-assembly-capability-specs`
- `processes-hil-small-batch-assembly-capability-specs`
- `processes-hil-large-volume-assembly-capability-specs`
- `processes-hil-turnkey-assembly-capability-specs`
- `processes-hil-box-build-assembly-capability-specs`
- `processes-process-governance-gap-map` — overall process governance coverage state

## Related Wiki Pages

- `wiki/processes/hil-assembly-capability-map.md` — dedicated HIL assembly wiki aggregation (P4-152)
- `wiki/processes/pcba-npi-to-mass-production-flow.md` — APT/HIL shared NPI-to-production flow
- `wiki/processes/mixed-technology-solder-route-selection.md` — SMT/THT mixed-tech routing

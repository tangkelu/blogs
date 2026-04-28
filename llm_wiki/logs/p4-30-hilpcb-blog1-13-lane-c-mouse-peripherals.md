# P4-30 HILPCB Blog1-13 Lane C Mouse / Peripherals Audit

Date: 2026-04-28

## Purpose

Audit the HILPCB-blog1-13 mouse / peripheral draft lane as claim inventory only and map what `llm_wiki` can already support versus what remains blocked.

Input drafts:

- `/code/blogs/tmps/HILPCB-blog1-13/en/gaming-mouse-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/gaming-mouse-pcb-assembly.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/pcb-for-wireless-mouse.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/pcb-for-optical-mouse.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/mouse-sensor-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/mouse-button-pcb-design.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/flexible-pcb-for-mouse-design.md`

## Baseline Finding

`llm_wiki` partially covers this lane at the process / boundary level, not at a mouse-specific product-fact level.

Safe existing support already exists for:

- generic PCBA NPI, SMT, inspection, FAI/FQI, ICT/FCT, and layered test strategy
- flex / rigid-flex class framing and guarded bend-guidance examples
- RF validation as layered verification vocabulary, not performance proof
- USB-C / USB Type-C vocabulary as protocol and connector context only
- live-date compliance handling for RoHS / REACH / SVHC

Current corpus does not already support reusable mouse-specific facts for:

- optical mouse sensor architecture or named sensor capability
- Bluetooth / 2.4 GHz mouse RF implementation details
- button switch lifetime, debounce timing, or click-latency outcomes
- battery-life, charging behavior, low-latency, polling-rate, CPI / DPI, or wireless-range claims
- FCC / CE claims for a mouse product or for HIL capability on that product class

## Per-Draft Status

| Draft | Status | Safe reuse from current `llm_wiki` | Blocked / rejected content |
| --- | --- | --- | --- |
| `gaming-mouse-pcb.md` | `partial_boundary_only` | compact multi-board PCB context; sensor / RF / button / manufacturing sections only as generic process framing; layered QA / test vocabulary | esports / championship / market claims; polling rate, latency, sensor accuracy, mounting tolerances, SPI speed, antenna performance, battery-life, USB-C charging behavior, optical-switch advantages, lifecycle clicks, scaling / lead-time / turnkey performance claims |
| `gaming-mouse-pcb-assembly.md` | `partial_boundary_only` | SMT / THT / fine-pitch assembly flow; AOI / X-ray / ICT / FCT / FAI / traceability; NPI-to-volume gate language | assembly accuracy numbers, yield, cycle time, reflow windows, exact sensor or connector tolerances, ESD outcome claims, functional coverage percentages, production-scale promises |
| `pcb-for-wireless-mouse.md` | `boundary_only_with_major_gaps` | RF review as antenna / validation / interference-separation vocabulary; USB-C vocabulary if charging connector appears; generic test-gate language | Bluetooth / 2.4 GHz implementation claims, antenna type recommendations as defaults, RF keepout numerics, wireless range, low latency, packet performance, battery-life, charging performance, FCC / CE / certification claims |
| `pcb-for-optical-mouse.md` | `boundary_only_with_major_gaps` | generic compact-board signal / power / inspection framing; test-ladder vocabulary | sensor optical path claims, DPI / CPI, tracking accuracy, surface compatibility, lens / z-height / alignment numerics, latency, thermal stability outcomes, named sensor capability |
| `mouse-sensor-pcb.md` | `boundary_only_with_major_gaps` | generic signal-integrity, power-isolation, and inspection vocabulary at a high level only | sensor interface speeds, impedance prescriptions, placement tolerances, power-sequencing outcomes, tracking-performance claims, named sensor features or benchmarks |
| `mouse-button-pcb-design.md` | `weak_support_only` | separate button-board architecture, flex interconnect context, assembly / test vocabulary | debounce timing, zero-latency or low-latency claims, switch lifetime clicks, optical-switch superiority claims, tactile / feel outcomes as engineering proof, gold-contact longevity claims |
| `flexible-pcb-for-mouse-design.md` | `best_supported_in_lane_but_still_bounded` | flex use cases, rigid-flex / multi-board architecture, connector / stiffener / bend-review vocabulary, guarded bend-guidance examples, flex assembly handling | bend-radius defaults from draft, copper / thickness / coverlay numeric ladders, shield effectiveness claims, RF-isolation outcomes, weight-reduction claims, reliability / fatigue / service-life claims, fabrication tolerance or plating claims |

## Claim-Family Rules

### Can be consumed as data now

- mouse drafts may be mined for topic intent and section inventory only
- generic process families:
  - compact multi-board architecture
  - flex or rigid-flex integration
  - SMT assembly and layered inspection
  - fixture-free versus fixture-based test vocabulary
  - RF review as interference / validation planning
  - USB-C as connector / protocol-context vocabulary only
- generic boundary language:
  - optical sensor section exists
  - button-board section exists
  - wireless section exists
  - compliance or testing section exists

### Needs official source or dated capability record before reuse

- any numeric value from drafts
- any sensor performance claim:
  - CPI / DPI
  - tracking IPS / acceleration
  - polling rate
  - latency
  - lift-off or surface performance
- any wireless capability claim:
  - Bluetooth version
  - 2.4 GHz protocol behavior
  - RF range
  - antenna performance
  - coexistence outcomes
- any power claim:
  - battery-life
  - charging speed
  - power-path behavior
  - thermal safety outcome
- any mechanical / assembly capability claim:
  - tolerances
  - placement accuracy
  - yield
  - lifecycle clicks
  - debounce timing
  - low-latency switch response
- any compliance or certification claim:
  - FCC
  - CE
  - Bluetooth qualification
  - USB-IF status
  - RoHS / REACH status for a specific product unless refreshed live
- any supplier-scoped capability claim about HIL:
  - lead time
  - volume readiness
  - exact process capability
  - testing coverage

## Candidate Future Fact / Source / Wiki Needs

- official mouse-sensor vendor sources if future work needs optical-sensor architecture or capability vocabulary
- official Bluetooth SIG / USB-IF / FCC / CE source layer if future work needs interface or certification statements beyond boundary language
- a small peripheral RF-layout boundary card for low-power 2.4 GHz / Bluetooth devices
- a peripheral battery / charger boundary card for single-cell mouse charging and use-while-charge wording
- a switch / debounce boundary card separating architecture vocabulary from timing and lifecycle claims
- a mouse / peripheral rewrite map if this lane becomes recurring rather than one-off

## Completion Status

Complete for lane audit logging.

Disposition:

- current lane is `not_ready_for_mouse-specific_fact_reuse`
- current lane is `usable_for_conservative_process_only_retrieval`
- future work should add source-backed peripheral subfacts before any mouse article, wiki page, or evidence pack tries to recover capability claims

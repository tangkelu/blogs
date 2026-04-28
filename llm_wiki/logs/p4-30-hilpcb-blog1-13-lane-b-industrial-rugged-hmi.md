# P4-30 Lane B Audit: HILPCB-blog1-13 Industrial / Rugged / HMI Keyboard Lane

## Purpose

Audit the `HILPCB-blog1-13` industrial/rugged/HMI keyboard draft lane as claim inventory only, then record what `llm_wiki` can safely reuse as data and what remains blocked pending stronger source support.

## Input Files

- `/code/blogs/tmps/HILPCB-blog1-13/en/industrial-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/heavy-duty-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/rugged-keyboard-pcb-for-industrial-use.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/ip67-keyboard-pcb-for-harsh-environments.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/industrial-panel-mount-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/custom-industrial-keyboard-design.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/automation-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/hmi-control-panel-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/medical-keyboard-pcb.md`
- `/code/blogs/tmps/HILPCB-blog1-13/en/military-grade-keyboard-pcb.md`

## Baseline Finding

`llm_wiki` already has partial support for this lane, but mostly at boundary-control and manufacturing-workflow level, not at finished-keyboard capability level.

Existing useful support:

- Industrial control / robotics process posture:
  `wiki/processes/industrial-robotics-control-rewrite-readiness-map.md`
- Review-gate boundary:
  `facts/methods/industrial-robotics-control-review-gates-and-claim-boundary.md`
- Test/inspection vs reliability boundary:
  `facts/methods/pcba-industrial-robotics-control-test-inspection-vs-reliability-boundary.md`
- Conformal coating as protection workflow, not proof:
  `wiki/processes/conformal-coating-protection-workflow-and-application-boundaries.md`
- General traceability / NPI / inspection stacks:
  `wiki/processes/pcba-npi-to-mass-production-flow.md`
  `wiki/testing/pcba-quality-gates-and-test-strategy.md`
- Medical and defense metadata only:
  FDA / ISO 13485 / AS9100 / MIL-PRF / traceability source records exist, but they do not prove HIL capability, certification, or product qualification.

Baseline conclusion:

- Lane is `partially covered for workflow vocabulary only`.
- Drafts are mostly not reusable as factual content.
- Safe reuse is limited to application framing and guarded process language around industrial-control context, inspection/test separation, traceability posture, and conformal-coating workflow.

## Per-Draft Disposition

| Draft | Topic intent | Status | Safe reuse as data | Blocked / rejected content |
| --- | --- | --- | --- | --- |
| `industrial-keyboard-pcb.md` | factory-floor keyboard framing | `partial` | industrial-control context; harsh-environment framing; review-gate / inspection / traceability posture | temperature ranges, MTBF, service life, cycle life, IP claims, protocol support, HIL capability claims |
| `heavy-duty-keyboard-pcb.md` | high-wear durability narrative | `mostly_blocked` | general idea that keyboard builds may emphasize mechanical robustness and mixed THT/SMT integration | keystroke counts, impact/drop claims, connector mating cycles, ESS/burn-in outcomes, long-life sourcing claims |
| `rugged-keyboard-pcb-for-industrial-use.md` | extreme-environment / ruggedization | `mostly_blocked` | rugged context as scenario label only; coating/potting as workflow vocabulary | MIL-STD-810/461 performance, IP68, salt fog/humidity/temp ranges, ATEX/IECEx, maritime approval, Class 3 as qualification proof |
| `ip67-keyboard-pcb-for-harsh-environments.md` | sealed/washdown keyboard | `mostly_blocked` | IP-rating topic intent; gasket/sealing/coating as design/workflow nouns | any IP67/IP68 proof, IEC 60529 test outcome, immersion depth/time, IP69K, leak-test capability, HIL verification claims |
| `industrial-panel-mount-keyboard-pcb.md` | cabinet/panel integration | `partial` | panel-mount context; cutout/mounting/gasket/interface planning as generic design topics | panel tolerance numbers, board flatness numbers, seal compression numbers, dimensional capability claims |
| `custom-industrial-keyboard-design.md` | custom OEM / NPI pathway | `partial` | custom-layout / requirements / DFM / prototype-stage intent; NPI workflow framing | build-vs-buy economics, expedite times, capability breadth, compliance-readiness, production scaling claims |
| `automation-keyboard-pcb.md` | PLC/CNC/SCADA input devices | `mostly_blocked` | industrial-control application framing; macros/function keys as product-category vocabulary | Profinet, EtherNet/IP, Modbus, RS-485, E-stop integration, protocol verification, EMC/isolation claims |
| `hmi-control-panel-pcb.md` | operator panel / touchscreen HMI | `mostly_blocked` | HMI/operator-panel context; display/touch/control integration as broad architecture theme | processor/platform specifics, DDR/layer-count norms, LVDS/MIPI implementation claims, industrial protocol support, display integration capability claims |
| `medical-keyboard-pcb.md` | hygienic healthcare keyboard | `mostly_blocked` | hygiene / cleanable-surface topic intent only | antimicrobial efficacy, disinfectant compatibility, ISO 13485 status, FDA framing, IEC 60601, medical traceability, clean manufacturing claims |
| `military-grade-keyboard-pcb.md` | defense / mil-spec keyboard | `mostly_blocked` | military/defense application label only; traceability/governance vocabulary from official metadata | MIL-STD-810/461 compliance, MIL-PRF flows as HIL capability, AS9100, ITAR, counterfeit-control execution, Class 3/space-military proof |

## Claim-Family Rules

### Can be consumed as data with conservative wording

- Industrial-control / robotics / HMI / panel / factory-automation as application context labels
- Keyboard, panel, enclosure, gasket, seal, coating, potting, traceability, inspection, FAI, NPI, DFM, DFT, DFA as workflow vocabulary
- General statement that industrial-control assemblies need coordinated manufacturability, test-access, inspection, and first-build review
- General statement that conformal coating is a post-assembly protection workflow around moisture/contamination/chemical exposure, masking, and test-access handoff
- General statement that inspection, electrical test, and reliability are separate evidence lanes

### Requires official source or dated capability record before use

- Any numeric values:
  temperature, cycle life, MTBF, thickness, tolerances, compression ratios, impedance, voltage, depth, time, hours, years, percentages
- Any capability or commercial claim tied to HIL:
  lead time, yield, AOI/X-ray/test coverage, coating execution, screening, verification, dimensional precision, display integration, sourcing continuity
- Any compliance / certification / qualification / approval claim:
  IP67/IP68/IP69K proof, IEC 60529, MIL-STD-810, MIL-STD-461, AS9100, ITAR, ISO 13485, FDA, IEC 60601, ATEX, IECEx, Coast Guard, classification society
- Any protocol-support claim:
  Profinet, EtherNet/IP, Modbus TCP/RTU, CANopen, DeviceNet, RS-232/485, USB/PS2 dual support, safety-bus integration
- Any durability / reliability / environmental-pass claim:
  shock, vibration, salt fog, humidity, washdown, immersion, drop, burn-in benefit, field life, uptime, service life
- Any medical or defense supplier-role claim:
  regulated traceability, DMR/DHR ownership, FDA registration, defense-qualified sourcing, counterfeit-control execution, export-control readiness

## Candidate Future Fact / Source / Wiki Needs

- Official source records for `IEC 60529`, `MIL-STD-810`, `MIL-STD-461`, `IEC 60601`, and named industrial Ethernet protocol families if this lane will be written later
- A boundary fact for `IP-rating language vs proof-of-test language`
- A boundary fact for `panel gasket / sealing / mounting workflow without dimensional overreach`
- A boundary fact for `industrial HMI / operator panel context vs unsupported processor/protocol claims`
- A boundary fact for `medical keyboard hygiene context vs antimicrobial / regulatory overclaim`
- A boundary fact for `defense keyboard context vs MIL / AS9100 / ITAR supplier-proof overclaim`
- If HIL intends to claim real protocol support, environmental screening, or regulated-sector manufacturing posture, add dated capability records first

## Completion Status

- Reviewed all 10 drafts as claim inventories.
- Checked `llm_wiki` for industrial control, HMI, ruggedization, IP/sealing/coating, military, medical, protocol, testing, and traceability coverage.
- Result: lane is not blog-write ready from current wiki coverage; it is only partially reusable for guarded workflow/context language.

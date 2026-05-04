---
topic_id: "applications-defense-ew-surveillance-targeting-pcb-review-boundaries"
title: "Defense EW Surveillance Targeting PCB Review Boundaries"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
activated_at: "2026-05-03"
activation_notes: "P4-176 re-review and repair: Added structured Must-Refresh List (11 items: MIL-STDs, DLA, export control, EO/IR, MIPI, laser, PX4/MAVLink/ELRS, RF validation, fire control, deployment) and Cross-Lane Routing Table (10 routes). Retained strong Slug Classification (3 slugs with status labels), Shared Blocked Claim Classes, Drafting Use Notes, and 13 fact cards. Promoted to active."
fact_ids:
  - "methods-internal-application-scenario-coverage-map"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "methods-fire-control-platform-interface-boundary"
  - "methods-laser-time-of-flight-pulsed-driver-and-safety-boundary"
  - "methods-rf-validation-capability"
  - "methods-rf-impedance-sparameter-pdn-ota-boundaries"
  - "methods-phased-array-source-coverage"
  - "methods-remote-control-and-drone-control-stack-boundary"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "standards-military-environmental-and-emi-qualification-boundary"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "sony-security-camera-image-sensor-products-page"
  - "lynred-about-our-technologies-page"
  - "mipi-csi-2-spec-page"
  - "mipi-d-phy-spec-page"
  - "mipi-dsi-2-spec-page"
  - "mipi-display-command-set-page"
  - "ti-lvds-overview-page"
  - "mil-std-1553-data-bus-page"
  - "mil-hdbk-1553-multiplex-application-handbook-page"
  - "bosch-can-protocols-page"
  - "ti-tdc7200-product-page"
  - "ti-lmh13000-product-page"
  - "noaa-lidar-basics-page"
  - "fda-laser-products-and-instruments-page"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "analog-devices-phased-array-radar"
  - "px4-basic-concepts-guide"
  - "mavlink-overview-page"
  - "expresslrs-getting-started"
  - "mil-std-461-emi-control-standard-page"
  - "mil-std-810-environmental-engineering-tests-page"
  - "faa-ac-20-152a-page"
  - "as9102c-first-article-inspection-page"
tags: ["defense", "electronic-warfare", "surveillance", "targeting", "uav", "rf-validation", "qualification-boundary", "review-boundary"]
---

# Definition

> Defense-adjacent PCB writing is only safe when it stays inside board-level review boundaries: application context, RF or mixed-signal partitioning, shield and transition planning, timing and isolation review, staged validation, and release-governance language. The current corpus does not support turning these slugs into jammer, ISR, laser, weapon, or mission-authority proof.

## Why This Topic Matters

- The `2026.4.27/en` defense lane repeatedly mixes real board-review pressure with unsupported program, qualification, performance, and supplier-proof claims.
- Existing `llm_wiki` layers are already strong enough to explain why EW, surveillance, and targeting boards need tighter RF partitioning, packaging, shielding, timing discipline, and validation staging.
- Without one aggregation page, rewrites drift into ungrounded `EW`, `SIGINT`, `SAR`, `laser designator`, `fire control`, `MIL-STD`, or fielded-program language that the current source base cannot safely support at finished-board claim level.

## Stable Facts

- The internal application layer already supports aerospace-defense, drone-UAV, and security-equipment hardware as real scenario families rather than as generic marketing labels.
- The current PCBA review and release layers support early review, inspection, traceability, first-build confirmation, and staged validation language for dense mixed-signal and RF-heavy assemblies.
- The existing RF boundary and validation layers support guarded use of low-loss material, hybrid stackup, shielding, transitions, impedance, S-parameters, OTA workflow, TDR, and VNA vocabulary when a draft crosses into radar, data-link, or EW front-end context.
- The new laser ToF boundary layer supports guarded `time-of-flight`, pulsed-driver, and laser safety-control vocabulary only at subsystem timing and review level.
- The new EO/IR detector boundary layer supports guarded owner-backed naming for `image intensifier tube`, `STARVIS` CMOS image sensor, and cooled / uncooled infrared-detector families only at detector identity and optical-sensor-interface level.
- The new imaging serial-interface boundary layer supports guarded `LVDS`, `MIPI CSI-2`, and generic display-interface-family vocabulary only at optical sensor and compact-display interface level.
- The current phased-array coverage layer supports radar and beam-steering language only as RF-system context plus board-execution consequences, not as performance or deployment proof.
- The current drone-control-stack layer supports UAV, telemetry, and control-link vocabulary only at architecture level.
- The new military environmental and EMI standards boundary supports guarded `MIL-STD-461` and `MIL-STD-810` vocabulary only at standards-context level, not as mission-readiness or supplier-qualification proof.
- The current regulated-application boundary layer supports aerospace and defense-sensitive vocabulary only as system or program boundary, not as supplier-readiness proof.

## Slug Classification

### `electronic-warfare-pcb.md`

- Status:
  `go_now_conservative`
- Safe article frame:
  RF front-end partitioning, shielding and cavity planning, hybrid material and transition review, power-versus-receiver coexistence, guarded `MIL-STD-461` or `MIL-STD-810` standards-context wording where needed, and staged validation workflow.
- Required posture:
  treat `EW`, `ESM`, `EA`, `jammer`, or `wideband receiver` as system-context labels that explain board-review pressure, not as supplier authority.
- Blocked claims:
  exact bandwidth, threat-detection, waveform-generation, receiver sensitivity, jammer output, self-interference rejection, military qualification, or defense-program proof.

### `surveillance-pcb.md`

- Status:
  `go_now_conservative`
- Safe article frame:
  multi-sensor interface and processing-board context, owner-backed EO/IR detector-family naming where needed, guarded imaging serial-interface vocabulary where needed, RF or data-link coexistence, UAV or fixed-site integration posture, packaging pressure, and validation plus release workflow.
- Required posture:
  treat `surveillance`, `ISR`, `video processing`, `sensor fusion`, and `data link` as application context, and keep exact optical-detector nouns at owner-backed identity level only.
- Blocked claims:
  exact EO/IR detector performance or optics claims, `SAR` authority, encrypted-link authority, COMSEC / TEMPEST proof, endurance outcomes, platform performance, or named defense-program history.

### `targeting-pcb.md`

- Status:
  `needs_refresh_then_go`
- Why:
  the current corpus now supports guarded laser time-of-flight, pulsed-driver, sensor-input segregation, platform-bus / interface vocabulary, and owner-backed EO/IR detector-family naming, but the draft still leans heavily on fire-control and weapon-accuracy claims that the current source layer does not directly prove.
- Safe article frame:
  timing-sensitive control-board context, platform-bus / network interface vocabulary, owner-backed EO/IR detector-family naming, guarded `LVDS` / `MIPI CSI-2` or generic display-interface vocabulary, high-voltage or isolated-section review, optical sensor interface posture, staged validation, and documentation-aware release workflow.
- Blocked claims:
  exact laser-driver topology, pulse-current claims, rangefinding accuracy, ballistic or fire-control authority, EO/IR detector performance or architecture claims, lane counts, `Gbps`, latency, named output-video standards, weapon-program proof, and environmental-qualification outcomes used as supplier proof.

## Shared Blocked Claim Classes

- exact jammer, radar, surveillance, laser, fire-control, targeting, optics, or mission-subsystem authority claims beyond current owner or standards sources
- exact bandwidth, range, timing, jitter, pulse-current, isolation, endurance, tracking, detection, or environmental-test numerics
- `MIL-STD-461`, `MIL-STD-810`, `DO-160`, export-control, defense-prime, mission, or deployment claims used as supplier or board-readiness proof
- HILPCB capability, customer, deployment, or program-history claims

## Must-Refresh List

| Item | Refresh Trigger |
|---|---|
| MIL-STD-461 revision/status | Before any "compliant", "certified", or "tested" claim |
| MIL-STD-810 revision/status | Before any environmental qualification claim |
| DLA Quick Search source validity | Before any DLA-sourced standard citation |
| Export control (ITAR/EAR) status | Before any export-controlled technology claim |
| EO/IR detector owner page recency | Before citing Exosens, Sony, Lynred product pages |
| MIPI/TI interface specification | Before any CSI-2, D-PHY, DSI-2, LVDS protocol claim |
| Laser safety (FDA/CDRH) | Before any laser class, safety interlock, or eye-safety claim |
| PX4/MAVLink/ExpressLRS version | Before any drone control-stack version claim |
| Phased array/RF validation source | Before any beam-steering, radar, or antenna performance claim |
| Fire control/platform interface | Before any MIL-1553, CAN, or platform bus claim |
| Deployment/program history | Before any named customer, program, lab, or defense-prime claim |

---

## Cross-Lane Routing Table

| Content Type | Route To |
|---|---|
| RF front-end / radar / phased array | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| EO/IR detector / imaging sensor | `facts/methods/eo-ir-detector-owner-identity-and-interface-boundary` |
| Laser / ToF / pulsed driver | `facts/methods/laser-time-of-flight-pulsed-driver-and-safety-boundary` |
| Fire control / platform interface | `facts/methods/fire-control-platform-interface-boundary` |
| UAV / drone control stack | `facts/methods/remote-control-and-drone-control-stack-boundary` |
| MIL-STD environmental/EMI | `facts/standards/military-environmental-and-emi-qualification-boundary` |
| Imaging serial interface (MIPI/LVDS) | `facts/standards/embedded-imaging-serial-interface-boundary` |
| RF validation / TDR / VNA | `facts/methods/rf-validation-capability` |
| DFM/DFT/DFA review gates | `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning` |
| FAI vs high-speed validation | `facts/methods/pcba-first-article-inspection-vs-high-speed-validation-boundary` |

---

## Drafting Use Notes

- If a rewrite starts from `what the mission system does`, stop and reframe around board partitioning, shielding, packaging, timing, and staged validation pressure.
- If a rewrite needs UAV, telemetry, or data-link vocabulary, keep it at system-architecture or control-stack context level.
- If a rewrite needs radar, phased-array, RF validation, or antenna wording, keep the measured layer explicit and avoid finished-system performance claims.
- If a rewrite needs exact `MIL-STD-461` or `MIL-STD-810` wording, keep it at standards-context level and do not convert it into board qualification, pass-status, or supplier-readiness proof.
- If a rewrite needs aerospace, defense, or qualification language, keep it at program-boundary vocabulary level and do not convert it into supplier qualification proof.

## Related Fact Cards

- `methods-internal-application-scenario-coverage-map`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-eo-ir-detector-owner-identity-and-interface-boundary`
- `methods-fire-control-platform-interface-boundary`
- `methods-laser-time-of-flight-pulsed-driver-and-safety-boundary`
- `methods-rf-validation-capability`
- `methods-rf-impedance-sparameter-pdn-ota-boundaries`
- `methods-phased-array-source-coverage`
- `methods-remote-control-and-drone-control-stack-boundary`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `standards-military-environmental-and-emi-qualification-boundary`
- `standards-embedded-imaging-serial-interface-boundary`
- `standards-automotive-medical-aerospace-application-qualification-boundary`

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/aerospace-defense-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/drone-uav-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/security-equipment-pcb.json
- https://www.exosens.com/products/image-intensifier-tube
- https://www.sony-semicon.com/en/technology/security/index.html
- https://www.sony-semicon.com/en/products/is/security/index.html
- https://www.lynred.com/about-our-technologies
- https://www.mipi.org/specifications/csi-2
- https://www.mipi.org/specifications/d-phy
- https://www.mipi.org/specifications/dsi-2
- https://www.mipi.org/specifications/display-command-set
- https://www.ti.com/product-category/interface/lvds/overview.html
- https://www.ti.com/product/TDC7200
- https://www.ti.com/product/LMH13000
- https://oceanservice.noaa.gov/geodesy/lidar.html
- https://www.fda.gov/radiation-emitting-products/home-business-and-entertainment-products/laser-products-and-instruments
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/npi-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://www.analog.com/en/solutions/aerospace-and-defense/phased-array.html
- https://docs.px4.io/main/en/getting_started/px4_basic_concepts.html
- https://mavlink.io/en/about/overview.html
- https://www.expresslrs.org/quick-start/getting-started/
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35978
- https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements

# P4-33 Full `/code/blogs/tmps` Source Gap Register

## Purpose

This register consolidates source gaps discovered during the P4-33 lane-agent intake. It is the queue for moving batches beyond claim-family learning into source-backed facts and topic wiki pages.

This file does not add facts. It defines which source recovery lanes must run before draft-originated claims can be reused as real PCB / PCBA data.

## Source Gap Priority Model

- `P0`: blocks many batches or high-risk claims; recover first.
- `P1`: unlocks a major topic family but is less urgent than P0.
- `P2`: useful for niche application pages or later wiki expansion.
- `dated_record_required`: cannot be solved by public official sources alone; needs dated internal capability or commercial record.

## Gap Register

| priority | gap lane | source need | blocks | required evidence type |
|---|---|---|---|---|
| P0 | material PDF extraction and provenance | Convert local `/tmps/materias_pdf` PDFs into traceable source records only after source identity and extraction scope are verified | Rogers variants, AGC, Shengyi, Ventec, Taconic, TUC, specialty laminates | official vendor PDF or preserved local PDF with provenance; extracted values must preserve test conditions |
| P0 | exact-product laminate coverage | Product-level facts for AGC / Shengyi / Ventec / Taconic / TUC families that appear in local PDFs and material drafts | material selector, RF/high-speed, FR-4/high-Tg, low-loss, IMS, automotive and telecom material claims | vendor datasheet / official product page |
| P0 | finish chemistry and finish limits | HASL, lead-free HASL, OSP, immersion silver, immersion gold, ENIG, ENEPIG scope and limitations | surface-finish drafts, 2-layer finish variants, RF finish selection, solderability claims | IPC public metadata where available, official finish chemistry/vendor guides, dated internal process records for supplier capability |
| P0 | PCBA and PCB testing standards metadata | Electrical test, functional test, FAI, X-ray / AXI, ICT, flying probe, solderability, burn-in, thermal cycling, thermal shock, vibration | `2025.7.28`, `2025.8.1`, PCBA application batches, quality and reliability claims | IPC / IEC / JEDEC / ASTM / equipment-vendor official metadata; supplier claims require dated capability record |
| P0 | dynamic commercial claim gate | Price, quote, cost, lead time, MOQ, stock, delivery, logistics, supply chain, inventory, quality rate, yield | commercial/service batches and many supplier/manufacturer drafts | dated commercial record or current official company page; otherwise blocked / refresh-required |
| P0 | supplier capability and certification records | Factory capability, equipment, scale, certification, qualification, compliance, inspection stack, acceptance status | nearly every manufacturer/supplier/service/application page | dated internal capability record with scope/date; official certificate metadata if public and current |
| P1 | RF / high-speed / impedance performance boundaries | Prevent material facts from becoming board-level insertion loss, antenna, radar, satellite, telecom, mmWave, channel-budget, or impedance-geometry promises | `2025.8.12`, `2025.8.30`, `2026.1.6`, `2026.3`, `2025.10.25` RF set | official material datasheets, standards/system-context anchors, equipment-vendor measurement docs; finished-board outcomes require dated test records |
| P1 | LED / MCPCB / IMS thermal evidence | LED thermal design, MCPCB reliability, aluminum substrate, heat dissipation, driver board claims | `2025.8.22`, `2026.1.27`, `2025.10.20`, LED solution pages | material/vendor datasheets, thermal-interface / LED vendor docs, dated capability/test records |
| P1 | ceramic / alumina / AlN / HTCC / thin-film evidence | Al2O3, AlN, LTCC, HTCC, thin-film, ceramic metallization, thermal and dielectric claims | `2025.7.23`, `2025.10.25`, `2025.11.17`, ceramic application pages | official ceramic vendor pages/datasheets; process claims require vendor/process docs or dated capability records |
| P1 | flex / rigid-flex / dynamic-flex evidence | Dynamic flex, bend radius, cyclic bend, polyimide, Kapton, LCP, flex connector, foldable/rollable claims | `2025.10.20`, `2025.10.25`, input-device and wearable pages | IPC public metadata, material vendor docs, dated reliability/capability records |
| P1 | HDI / via / edge-feature evidence | Microvia, blind/buried via, VIPPO, edge plating, gold finger, castellated, cavity, copper-core, thick copper, ultra-thin | `2025.07.13`, `2025.7.14`, `2025.7.22`, `2025.10.25`, `2026.4.24` | IPC metadata, vendor process guides, dated capability records for geometry / plating / acceptance values |
| P1 | USB / consumer-interface vocabulary | USB-C, USB4, Thunderbolt, PD, PPS, HDMI, Bluetooth, Wi-Fi, FCC, CE / RED | `2025.11.3`, `2025.12.20`, `2026.1.13`, consumer application drafts | USB-IF, HDMI LA, Bluetooth SIG, Wi-Fi Alliance, FCC / EU official metadata; product claims require dated records |
| P1 | regulated-sector boundaries | Automotive, medical, aerospace, military, high-reliability, functional safety, IP rating, FDA / IEC / ISO claims | automotive, ADAS, EV, medical, wearable, rugged, military, high-reliability drafts | official regulator / standards metadata; supplier proof requires dated capability/certificate record |
| P1 | power / inverter / BMS / motor-control sources | MPPT, BMS, inverter, gate driver, IGBT/MOSFET, PFC, DC/DC, VFD, servo, motor driver | `2025.12.29`, `2026.1.27`, `2025.11.17`, solar/power solution pages | semiconductor/vendor app notes, standards metadata, component datasheets; performance claims require test records |
| P2 | maker and smart-home platform sources | ESP32, Raspberry Pi, Matter, Thread, Zigbee, DIY drone, remote control, smart-home automation | `2025.11.3`, smart-home application drafts | official platform/vendor docs and standards/alliance pages |
| P2 | transparent / optical / specialty PCB sources | Transparent PCB, optical PCB, clear PCB, waterproof, biodegradable, stretchable, peelable mask, insulation, copper foil | `2025.7.22`, `2025.7.23`, `2025.12.17` | vendor/material official docs, process guides, academic/standards support only if authoritative and scoped |
| P2 | EDA / electronics basics sources | KiCad vs Eagle, schematic symbols, Ohm's law, watts-to-amps, ferrite bead, encoder circuit, protoboard vs breadboard | `2025.11.3`, `2025.11.10`, `2025.11.17` | official tool docs, educational references from authoritative institutions, component vendor docs |
| P2 | legal-sensitive service topics | PCB copying, cloning, replication, reverse engineering, repair/rework legality | `2025.10.1`, service taxonomy drafts | legal review / official legal sources; do not make legal claims from draft prose |

## Dated Record Requirements

Public official sources cannot prove these supplier-specific claim classes:

- HIL / APT can manufacture a named board type to a specific limit.
- HIL / APT has a specific machine, inspection method, certificate, factory workflow, capacity, lead time, MOQ, stock, yield, or quality rate.
- HIL / APT is qualified, approved, certified, listed, accepted, or production-ready for a regulated program.
- HIL / APT can deliver a named RF, mmWave, high-speed, medical, automotive, military, solar, power, or consumer device result.

For these claims, create dated capability or commercial records before facts are written.

## Next Recovery Order

1. `material-pdf-provenance-and-extraction`
2. `testing-and-quality-standards-metadata`
3. `finish-chemistry-and-selection-boundaries`
4. `rf-high-speed-performance-boundaries`
5. `dynamic-commercial-and-supplier-capability-gates`
6. `led-mcpcb-thermal-and-power-control`
7. `regulated-application-boundaries`
8. `usb-hdmi-wireless-interface-vocabulary`
9. `ceramic-flex-hdi-special-structure-followon`
10. `maker-specialty-legal-and-electronics-basics-followon`

## Recovery Progress

### 2026-04-28 Material PDF Round 1

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `RF-60TC`
  - AGC `RF-35TC`
  - AGC `METEORWAVE 4000`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-1.md`
  - `sources/registry/materials/agc-rf-60tc-datasheet.md`
  - `sources/registry/materials/agc-rf-35tc-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-4000-datasheet.md`
  - `facts/materials/agc-rf-60tc.md`
  - `facts/materials/agc-rf-35tc.md`
  - `facts/materials/agc-meteorwave-4000.md`
- candidate planning support:
  - `logs/p4-33-material-pdf-candidate-inventory-round-2.md`
- remaining status:
  - The material PDF lane remains open. The three AGC cards unlock source-backed material parameters for those exact products only.
  - They do not unlock finished-board RF / SI / thermal performance, supplier capability, price, lead time, certification, qualification, yield, or application-readiness claims.
  - Next high-value candidates include AGC `METEORWAVE 8000`, `N4000-13SI`, `N7000-3`, `NF-30`; Rogers `RO4360G2`, `RO4830 Plus`, `RO4835IND LoPro`, `RT/duroid 6002`, `RT/duroid 6202`; Shengyi `mmWaveG`, `AeroWave 300`, `LNB33C`, `S1170G`; Ventec `VT-901`, `VT-6880`; and Taconic `RF-35`.

### 2026-04-28 Material PDF Round 2

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `METEORWAVE 8000`
  - AGC `N4000-13 SI`
  - AGC `N7000-3`
  - AGC `NF-30`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-2.md`
  - `sources/registry/materials/agc-meteorwave-8000-datasheet.md`
  - `sources/registry/materials/agc-n4000-13si-datasheet.md`
  - `sources/registry/materials/agc-n7000-3-datasheet.md`
  - `sources/registry/materials/agc-nf-30-datasheet.md`
  - `facts/materials/agc-meteorwave-8000.md`
  - `facts/materials/agc-n4000-13si.md`
  - `facts/materials/agc-n7000-3.md`
  - `facts/materials/agc-nf-30.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 AGC source-backed upgrade now covers `7` exact-product rows.
  - The new AGC rows unlock exact-product material parameters only; they do not unlock finished-board RF / SI / mmWave / severe-condition performance, supplier process capability, certification, qualification, price, lead time, yield, or application-readiness claims.
  - Next high-value source-backed candidates should shift to Rogers scout rows if official URLs can be verified, then Shengyi / Ventec / Taconic follow-on rows.

### 2026-04-28 Material PDF Round 3

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Rogers `RO4360G2`
  - Rogers `RO4830 Plus`
  - Rogers `RO4835IND LoPro`
  - Rogers `RT/duroid 6002`
  - Rogers `RT/duroid 6202`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-3.md`
  - `sources/registry/materials/rogers-ro4360g2-datasheet.md`
  - `sources/registry/materials/rogers-ro4830-plus-datasheet.md`
  - `sources/registry/materials/rogers-ro4835ind-lopro-datasheet.md`
  - `sources/registry/materials/rogers-rt-duroid-6002-datasheet.md`
  - `sources/registry/materials/rogers-rt-duroid-6202-datasheet.md`
  - `facts/materials/rogers-ro4360g2.md`
  - `facts/materials/rogers-ro4830-plus.md`
  - `facts/materials/rogers-ro4835ind-lopro.md`
  - `facts/materials/rogers-rt-duroid-6002.md`
  - `facts/materials/rogers-rt-duroid-6202.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `7` AGC exact-product rows plus `5` Rogers exact-product rows.
  - The Rogers rows unlock exact-product material parameters only; they do not unlock finished-board insertion loss, radar performance, antenna performance, impedance tolerance, supplier capability, certification, qualification, price, lead time, yield, or application-readiness claims.
  - Next source-backed candidates should move to Shengyi / Ventec / Taconic rows or aggregate the new AGC / Rogers rows into selector wiki pages.

### 2026-04-28 Material PDF Round 4

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Ventec `VT-901`
  - Ventec `VT-6880`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-4.md`
  - `sources/registry/materials/ventec-vt-901-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-6880-datasheet.md`
  - `facts/materials/ventec-vt-901.md`
  - `facts/materials/ventec-vt-6880.md`
- scout-only support:
  - `logs/p4-33-shengyi-material-pdf-extraction-scout-round-4.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `7` AGC exact-product rows, `5` Rogers exact-product rows, and `2` Ventec exact-product rows.
  - Taconic `RF-35` remains `blocked_pending_official_source`; local old PDF text exists but was not promoted without a current official source URL.
  - At the end of round 4, Shengyi `mmWaveG`, `AeroWave 300`, `LNB33C`, and `S1170G/S1170GB` remained `extraction_scout_only` pending official-source verification and layout-sensitive value review. Round 5 later upgraded `AeroWave 300` only.
  - The Ventec rows do not unlock finished-board radar, aerospace, military, flight-control, burn-in, downhole, antenna, insertion-loss, supplier capability, certification, price, lead time, yield, or application-readiness claims.

### 2026-04-28 Material PDF Round 5

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Shengyi `AeroWave 300`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-5.md`
  - `sources/registry/materials/shengyi-aerowave-300-datasheet.md`
  - `facts/materials/shengyi-aerowave-300.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `7` AGC exact-product rows, `5` Rogers exact-product rows, `2` Ventec exact-product rows, and `1` Shengyi exact-product row.
  - At the end of round 5, Shengyi `mmWaveG`, `LNB33C`, and `S1170G/S1170GB` remained `extraction_scout_only` pending exact official download URL and layout-sensitive review. Round 6 later upgraded `mmWave G`, `LNB33C`, and `S1170G` only.
  - Taconic `RF-35` remains `blocked_pending_official_source`.
  - The Shengyi `AeroWave 300` row does not unlock finished-board PIM, antenna efficiency, base-station qualification, insertion loss, supplier capability, certification, price, lead time, yield, or application-readiness claims.

### 2026-04-28 Material PDF Round 6

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Shengyi `mmWave G`
  - Shengyi `LNB33C`
  - Shengyi `S1170G`
- outputs:
  - `logs/p4-33-shengyi-remaining-official-source-mapping-scout.md`
  - `logs/p4-33-material-pdf-source-recovery-round-6.md`
  - `sources/registry/materials/shengyi-mmwaveg-product-page.md`
  - `sources/registry/materials/shengyi-lnb33c-product-page.md`
  - `sources/registry/materials/shengyi-s1170g-product-page.md`
  - `facts/materials/shengyi-mmwaveg.md`
  - `facts/materials/shengyi-lnb33c.md`
  - `facts/materials/shengyi-s1170g.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `7` AGC exact-product rows, `5` Rogers exact-product rows, `2` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - Shengyi `mmWaveGB` and `S1170GB` remain blocked as separate companion / prepreg identities until official-source and layout-level verification supports them.
  - Taconic `RF-35` remains `blocked_pending_official_source`.
  - The Shengyi rows do not unlock finished-board PIM, antenna efficiency, base-station, WiMAX, automotive radar, satellite, insertion-loss, supplier capability, certification, price, lead time, yield, or application-readiness claims.

### 2026-04-28 Material PDF Round 7

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `METEORWAVE 1000`
  - AGC `METEORWAVE 1000NF`
  - AGC `METEORWAVE 2000`
  - AGC `METEORWAVE 3000`
  - AGC `METEORWAVE 4000M`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-7.md`
  - `sources/registry/materials/agc-meteorwave-1000-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-1000nf-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-2000-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-3000-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-4000m-datasheet.md`
  - `facts/materials/agc-meteorwave-1000.md`
  - `facts/materials/agc-meteorwave-1000nf.md`
  - `facts/materials/agc-meteorwave-2000.md`
  - `facts/materials/agc-meteorwave-3000.md`
  - `facts/materials/agc-meteorwave-4000m.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `12` AGC exact-product rows, `5` Rogers exact-product rows, `2` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new AGC rows unlock exact-product material parameters and guarded material-positioning context only.
  - They do not unlock finished-board high-speed / radar / antenna / insertion-loss / impedance / CAF / IST performance, lamination recipes, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 8

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `METEORWAVE 8300`
  - AGC `METEORWAVE M1`
  - AGC `N4000-13`
  - AGC `N4000-13 EP`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-8.md`
  - `sources/registry/materials/agc-meteorwave-8300-datasheet.md`
  - `sources/registry/materials/agc-meteorwave-m1-datasheet.md`
  - `sources/registry/materials/agc-n4000-13-datasheet.md`
  - `sources/registry/materials/agc-n4000-13ep-datasheet.md`
  - `facts/materials/agc-meteorwave-8300.md`
  - `facts/materials/agc-meteorwave-m1.md`
  - `facts/materials/agc-n4000-13.md`
  - `facts/materials/agc-n4000-13ep.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `16` AGC exact-product rows, `5` Rogers exact-product rows, `2` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new AGC rows unlock exact-product material parameters and guarded material-positioning context only.
  - They do not unlock finished-board high-speed / RF / radar / antenna / insertion-loss / impedance / channel performance, supplier lamination recipes, lead-free assembly proof, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 9

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `N4000-13 EP SI`
  - AGC `N4000-29`
  - AGC `N4000-29NF`
  - AGC `N7000-2HT`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-9.md`
  - `sources/registry/materials/agc-n4000-13epsi-datasheet.md`
  - `sources/registry/materials/agc-n4000-29-datasheet.md`
  - `sources/registry/materials/agc-n4000-29nf-datasheet.md`
  - `sources/registry/materials/agc-n7000-2ht-datasheet.md`
  - `facts/materials/agc-n4000-13epsi.md`
  - `facts/materials/agc-n4000-29.md`
  - `facts/materials/agc-n4000-29nf.md`
  - `facts/materials/agc-n7000-2ht.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `20` AGC exact-product rows, `5` Rogers exact-product rows, `2` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new AGC rows unlock exact-product material parameters, no-flow prepreg / bond-ply material-form context, and guarded lead-free / high-temperature material-positioning context only.
  - They do not unlock finished-board high-speed / RF / backplane / telecom / automotive / burn-in performance, supplier lamination recipes, lead-free assembly proof, CAF / IST / high-layer reliability, rigid-flex bonding success, heat-sink attachment success, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 10

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Ventec `VT-481`
  - Ventec `VT-463H`
  - Ventec `VT-6735`
  - Ventec `VT-770 / VT-770(LK)`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-10.md`
  - `sources/registry/materials/ventec-vt-481-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-463h-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-6735-datasheet.md`
  - `sources/registry/materials/ventec-vt-770-vt-770lk-datasheet-page.md`
  - `facts/materials/ventec-vt-481.md`
  - `facts/materials/ventec-vt-463h.md`
  - `facts/materials/ventec-vt-6735.md`
  - `facts/materials/ventec-vt-770-vt-770lk.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `20` AGC exact-product rows, `5` Rogers exact-product rows, `6` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new Ventec rows unlock exact-product material parameters and guarded product-positioning context only.
  - They do not unlock finished-board high-speed / RF / satellite / navigation / GPS / LTE / IC-packaging performance, lead-free assembly proof, CAF / IST / high-layer reliability, supplier process recipes, generic process windows, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Follow-On Scout Disposition

- status: `scout_disposition_only`
- outputs:
  - `logs/p4-33-material-pdf-followon-scout-disposition-round-10.md`
- remaining status:
  - Ventec and TUC next-candidate recommendations are deletion-safe in `llm_wiki`, but scout-only candidates remain not learned.
  - TUC rows remain blocked until exact official page / PDF binding resolves metadata/title collision risk.
  - Ventec second-tier rows remain pending controller extraction and tracker updates.

### 2026-04-28 Material PDF Round 11

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Ventec `VT-462S`
  - Ventec `VT-464GS`
  - Ventec `VT-90H`
  - Ventec `VT-4B5H`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-11.md`
  - `sources/registry/materials/ventec-vt-462s-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-464gs-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-90h-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-4b5h-datasheet-page.md`
  - `facts/materials/ventec-vt-462s.md`
  - `facts/materials/ventec-vt-464gs.md`
  - `facts/materials/ventec-vt-90h.md`
  - `facts/materials/ventec-vt-4b5h.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `20` AGC exact-product rows, `5` Rogers exact-product rows, `10` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new Ventec rows unlock exact-product SI, IC-packaging, polyimide, and IMS material parameters plus guarded product-positioning context only.
  - They do not unlock finished-board high-speed / RF / satellite / navigation / GPS / LTE / IC-packaging / military / aerospace / flight-control / downhole / LED / motor-drive / power-module performance, supplier process recipes, generic process windows, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 12

- status: `source_backed_fact_layer_partial`
- completed scope:
  - Ventec `VT-441V`
  - Ventec `VT-441`
  - Ventec `VT-42`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-12.md`
  - `sources/registry/materials/ventec-vt-441v-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-441-datasheet-page.md`
  - `sources/registry/materials/ventec-vt-42-datasheet-page.md`
  - `facts/materials/ventec-vt-441v.md`
  - `facts/materials/ventec-vt-441.md`
  - `facts/materials/ventec-vt-42.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `20` AGC exact-product rows, `5` Rogers exact-product rows, `13` Ventec exact-product rows, and `4` Shengyi exact-product rows.
  - The new Ventec rows unlock exact-product halogen-free mid-Tg FR-4 and standard FR-4 material parameters only.
  - They do not unlock finished-board automotive / LED / high-power / phone / communication-equipment / LCD / TV / instrumentation performance, CAF lifetime, generic FR-4 defaults, supplier process windows, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 13

- status: `source_backed_fact_layer_partial`
- completed scope:
  - TUC `TU-901`
  - TUC `TU-787 LK`
  - TUC `TU-872 LK`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-13.md`
  - `sources/registry/materials/tuc-tu-901-datasheet-page.md`
  - `sources/registry/materials/tuc-tu-787-lk-datasheet-page.md`
  - `sources/registry/materials/tuc-tu-872-lk-datasheet-page.md`
  - `facts/materials/tuc-tu-901.md`
  - `facts/materials/tuc-tu-787-lk.md`
  - `facts/materials/tuc-tu-872-lk.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `20` AGC exact-product rows, `5` Rogers exact-product rows, `13` Ventec exact-product rows, `4` Shengyi exact-product rows, and `3` TUC exact-product rows.
  - The new TUC rows unlock exact-product high-Tg halogen-free, mobile / telecom low-loss, and modified-epoxy FR-4 low-loss material parameters only.
  - They do not unlock finished-board insertion loss, impedance, SI, RF, backplane, server, telecom, base-station, substrate, HDI, ELIC, aerospace, military, harsh-environment, mobile-device, office-router performance, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.
  - TUC `TU-865S` remains pending preliminary-revision binding before numeric extraction.
  - `SCGA-500 GF220` remains blocked pending exact live official TUC source recovery.

### 2026-04-28 Material PDF Round 14

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `TSM-DS3`
  - AGC `TSM-DS3b`
  - AGC `TSM-DS3M`
  - AGC `TLX-8`
  - AGC `TLY-5`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-14.md`
  - `sources/registry/materials/agc-tsm-ds3-datasheet.md`
  - `sources/registry/materials/agc-tsm-ds3b-datasheet.md`
  - `sources/registry/materials/agc-tsm-ds3m-datasheet.md`
  - `sources/registry/materials/agc-tlx-8-datasheet.md`
  - `sources/registry/materials/agc-tly-5-datasheet.md`
  - `facts/materials/agc-tsm-ds3.md`
  - `facts/materials/agc-tsm-ds3b.md`
  - `facts/materials/agc-tsm-ds3m.md`
  - `facts/materials/agc-tlx-8.md`
  - `facts/materials/agc-tly-5.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `25` AGC exact-product rows, `5` Rogers exact-product rows, `13` Ventec exact-product rows, `4` Shengyi exact-product rows, and `3` TUC exact-product rows.
  - The new AGC rows unlock exact-product low-loss microwave and PTFE material parameters only.
  - They do not unlock finished-board insertion loss, RF, mmWave, radar, antenna, aerospace, military, avionics, space, OEM-equivalence, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 15

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `TLY-3`
  - AGC `TLY-5A`
  - AGC `TLY-5Z`
  - AGC `TLE-95`
  - AGC `TLC-32`
- outputs:
  - `logs/p4-33-material-pdf-source-recovery-round-15.md`
  - `sources/registry/materials/agc-tly-3-datasheet.md`
  - `sources/registry/materials/agc-tly-5a-datasheet.md`
  - `sources/registry/materials/agc-tly-5z-datasheet.md`
  - `sources/registry/materials/agc-tle-95-datasheet.md`
  - `sources/registry/materials/agc-tlc-32-datasheet.md`
  - `facts/materials/agc-tly-3.md`
  - `facts/materials/agc-tly-5a.md`
  - `facts/materials/agc-tly-5z.md`
  - `facts/materials/agc-tle-95.md`
  - `facts/materials/agc-tlc-32.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `30` AGC exact-product rows, `5` Rogers exact-product rows, `13` Ventec exact-product rows, `4` Shengyi exact-product rows, and `3` TUC exact-product rows.
  - The new AGC rows unlock exact-product very-low-Dk PTFE, microwave, and high-speed digital material parameters only.
  - They do not unlock 77 GHz / OEM drop-in, finished-board RF / microwave / satellite / cellular / aerospace / PTH / SMT reliability, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

### 2026-04-28 Material PDF Round 16

- status: `source_backed_fact_layer_partial`
- completed scope:
  - AGC `METEORWAVE ELL`
  - AGC `TLF-35A`
- outputs:
  - `logs/p4-33-agc-tail-scout-round-16.md`
  - `logs/p4-33-material-pdf-source-recovery-round-16.md`
  - `sources/registry/materials/agc-meteorwave-ell-datasheet.md`
  - `sources/registry/materials/agc-tlf-35a-datasheet.md`
  - `facts/materials/agc-meteorwave-ell.md`
  - `facts/materials/agc-tlf-35a.md`
- remaining status:
  - The material PDF lane remains open. The cumulative P4-33 material PDF source-backed upgrade now covers `32` AGC exact-product / exact-family rows, `5` Rogers exact-product rows, `13` Ventec exact-product rows, `4` Shengyi exact-product rows, and `3` TUC exact-product rows.
  - `METEORWAVE ELL` is modeled as one family card with explicit `ELL 101` versus `ELL 102 / 103` variant rows.
  - The new AGC rows unlock low-loss high-speed laminate / prepreg and Dk 3.5 RF laminate parameters only.
  - They do not unlock 112 Gb, telecom, AI, cloud, router, automotive-radar, aerospace, PIMD, PTH, attenuation, price/performance, supplier capability, certification, qualification, price, lead time, yield, stock, or application-readiness claims.

## Completion Requirement For Source-Backed Upgrade

A gap lane can upgrade a batch beyond claim-family level only when it creates or reuses:

- valid source records under `sources/registry/`
- scoped fact cards under `facts/`
- topic wiki aggregation when multiple facts need prompt consumption
- tracker updates that distinguish new source-backed facts from draft inventory

Without those outputs, the correct status remains `completed_at_claim_family_level`.

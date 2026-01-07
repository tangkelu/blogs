---
title: "soldermask exposure tutorial: white paper su PCB manufacturing e quality management"
description: "soldermask exposure tutorial dettagliato su process capability, yield improvement, quality tools, test coverage e traceability—con checklist DFM/DFT/DFR per una collaborazione efficace."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 9
tags: ["soldermask exposure tutorial", "smt stencil design tutorial", "x ray inspection checklist", "pcb fabrication process steps"]
---
## 1. Executive summary: quality goals e metriche

In HILPCB la qualità è un pilastro operativo, non un’ispezione isolata. Questo white paper descrive il nostro sistema end‑to‑end di qualità su fabrication, assembly e test, e mostra come usiamo controllo data‑driven, quality tools e collaborazione DFM/DFT/DFR per superare le aspettative cliente.

Come un **soldermask exposure tutorial** definisce energia/allineamento/tempo per ottenere protezione delle trace e aperture pad precise, la nostra qualità applica lo stesso livello di controllo a ogni fase. Obiettivo: “zero defect”, misurato con:

* **FPY:** > 99.5%  
* **CPK:** processi chiave > 1.67  
* **PPM:** < 100  
* **OTD:** > 98%

<div class="div-type-1">
    <h3>Core capability highlights</h3>
    <p>Il sistema qualità HILPCB è anche cultura: investiamo in automazione, digitalizzazione e formazione, integrando lean manufacturing e Industry 4.0 per stabilità e prevedibilità dal prototype al volume.</p>
</div>

---

## 2. Manufacturing capability: dal disegno alla PCB reale

| Process Step | Key Capability | Process Control Metrics | Mass Production Case |
| :--- | :--- | :--- | :--- |
| **Inner-layer imaging** | Min line/space: 2.5/2.5 mil | Post-etch width tolerance: ±10% | 5G base-station RF unit |
| **Drilling** | Min mechanical drill: 0.15mm; laser: 0.075mm | Hole position: ±0.025mm; wall roughness: < 25μm | Medical endoscope sensor board |
| **PTH & plating** | Hole copper: > 20μm; uniformity: > 90% | Plating CPK > 1.67; panel uniformity < 15% | Automotive ADAS controller |
| **Outer-layer imaging** | Registration: ±12.5μm | AOI coverage: 100%; false-call rate < 5% | HPC server motherboard |
| **Soldermask** | LDI exposure, min dam: 0.05mm | Mask thickness: 10–20μm (pads); alignment CPK > 2.0 | Consumer wearable device |
| **Surface finish** | ENIG/HASL/OSP/ImmAg/ImmSn | ENIG Au: 0.03–0.08μm; salt spray > 48h | Industrial PLC module |
| **Profiling** | Dim tolerance: ±0.1mm | V-Cut: ±0.05mm; CNC outline: ±0.075mm | Drone flight-control system |

Su soldermask seguiamo i principi del **soldermask exposure tutorial**: LDI elimina errori da film expansion/shrinkage e migliora l’apertura su fine‑pitch BGA/QFN, riducendo il rischio di bridging.

---

## 3. Quality tools: ottimizzazione data-driven

- **SPC** su plating/etch/lamination.
- **CPK** interno >1.67 per parametri critici.
- **MSA** (GR&R) per validare misure.
- **8D** + FMEA per miglioramento continuo.
- dashboard digitali FPY/PPM/OEE.

<div class="div-type-6">
    <h3>Our manufacturing strength</h3>
    <p>Combinando quality tools e sistemi digitali costruiamo una piattaforma che identifica, predice e previene problemi, minimizzando i quality risks.</p>
</div>

---

## 4. SMT/assembly: capability e defect control

La nostra guida DFM è dettagliata come uno **smt stencil design tutorial**: supporto su aperture, thickness e step stencil per massimizzare paste print quality.

**Key controls:**
SPI 3D al 100%, pick&place per 01005 e 0.3mm pitch BGA/CSP, reflow profile dedicati, AOI pre/post, X‑ray 2D/3D con **x ray inspection checklist** (Voiding <25%, bridging, Head‑in‑Pillow, alignment).

---

## 5. Test coverage: validazione completa

| Test Type | Description | Coverage | Target Defects |
| :--- | :--- | :--- | :--- |
| **ICT** | Probes test points; checks opens/shorts and values. | 85%–95% component-level defects | Opens, shorts, wrong/missing parts, wrong values |
| **FPT** | Flying probes without nail bed. | 80%–90% component-level defects | Similar to ICT with higher flexibility |
| **FCT** | End-use simulation; validates functions. | 100% functional modules | Functional failures, out-of-spec, logic errors |
| **Hipot** | High-voltage insulation/clearance test. | Safety-critical power paths | Breakdown, insufficient clearance |
| **Burn-in** | Long run under harsh conditions. | 100% finished products | Early-life failures, latent solder defects |
| **Reliability tests** | Temp cycling, vibration, drop, salt spray. | Sampling or per customer | Insufficient margin, poor robustness |

---

## 6. Traceability: record di ciclo vita

Serial/barcode dalla bare board; binding lotti materiali; raccolta parametri SPI/placement/reflow/AOI; integrazione risultati ICT/FCT; data lake + visualizzazione per indagini rapide e recall preciso.

---

## 7. Checklist DFM/DFT/DFR: collaborazione design

| Category | Checkpoint | Recommendation |
| :--- | :--- | :--- |
| **DFM (Fabrication)** | Material selection | FR-4/Rogers/Teflon per rate/temp/costo. |
| | Stackup | Simmetrico/bilanciato; Core/PP adeguati. |
| | Minimum line/space | ≥15% margin. |
| | Copper-to-edge | ≥0.2mm; evitare V-Cut/CNC. |
| | Soldermask dam | >0.075mm. |
| | Via type & size | Through-hole preferito; annular ring adeguato. |
| | Via-in-Pad | Resin plug + planarization. |
| | Panelization | Rail + fiducial + fixture. |
| | Silkscreen | No su pad; leggibile. |
| | Impedance control | Mark nets + stackup/targets. |
| **DFA (Assembly)** | Spacing | Rework/inspection clearance. |
| | Orientation | Wave-solder friendly. |
| | Pad design | IPC-7351. |
| | Large parts | Ridurre stress. |
| | Heat-sensitive | Lontano da hot spots. |
| | Fiducials | ≥2/board, 3/rail. |
| | Stencil | Riduzione BGA/QFN; precisione 0201/01005. |
| | Test points | >0.8mm; >2.54mm pitch. |
| | Connectors | Edge + strain relief. |
| | Cleaning | Definire flux type. |
| **DFT (Testability)** | Coverage | >90% critical nets. |
| | Distribution | Uniforme. |
| | Unobstructed | No mask/silk; lontano da tall parts. |
| | JTAG/SWD | Standard. |
| | Isolation | Resistors/jumpers. |
| | Power tests | Test point per rail. |
| | Mechanical | Fixture clearance. |
| | FCT interface | Robusta e anti‑errore. |
| **DFR (Reliability)** | Thermal | Thermal Vias/copper/heatsink. |
| | ESD | ESD devices. |
| | Decoupling | Near pins. |
| | SI | Match/length tune. |
| | PI | Wide/short, no sharp corners. |
| | Anti-vibration | Glue/screws. |
| | Moisture/corrosion | Finish + conformal coating. |

<div class="div-type-3">
    <h3>Collaborative improvement path</h3>
    <p><strong>Early design involvement:</strong> prima dei Gerber, possiamo fare un DFM/DFT/DFR assessment su schematic/ME e eliminare rischi in anticipo.</p>
</div>

---

## 8. Case study e call to action

Caso medical PCBA: voiding BGA >30% + crosstalk → FCT <80%. Interventi: Via-in-Pad resin plug + planarization, ottimizzazione stencil, SI sim + reroute/stackup + ground vias, +3 test points RF. Risultati: voiding <5%, FPY **99.7%**, -6 settimane.

[**Contatta il team engineering per un DFM review gratuito**](/contact-us)

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Questo paper descrive capability indices, yield improvement, quality tools, test coverage e traceability, con checklist DFM/DFT/DFR. Coinvolgere presto il team DFM/DFA di HILPCB accelera prototype e volume mantenendo qualità e compliance.

> Supporto fabrication/assembly: [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) o [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).


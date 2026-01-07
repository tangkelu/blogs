---
title: "soldermask exposure tutorial: Whitepaper zu PCB Manufacturing und Quality Management"
description: "Detailliertes soldermask exposure tutorial zu Prozessfähigkeit, Yield-Verbesserung, Quality Tools, Test Coverage und Traceability—inkl. DFM/DFT/DFR Checklist für die Zusammenarbeit."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 9
tags: ["soldermask exposure tutorial", "smt stencil design tutorial", "x ray inspection checklist", "pcb fabrication process steps"]
---
## 1. Executive Summary: Quality Goals und Business Metrics

Bei HILPCB ist Quality ein Fundament des Betriebs—nicht nur ein Inspektionsschritt. Dieses Whitepaper beschreibt unser End‑to‑End Quality Management über fabrication, assembly und test und zeigt, wie wir über data-driven process control, moderne Quality Tools und DFM/DFT/DFR‑Zusammenarbeit jede PCB über Kundenerwartung liefern.

Wie ein präzises **soldermask exposure tutorial** die Schlüsselparameter der Soldermask‑Exposure (Energy, Alignment, Time) definiert, um Traces zu schützen und Pads korrekt zu öffnen, überträgt HILPCB dieselbe Präzision auf jeden Schritt von Inbound Material bis Shipment. Unser Ziel ist “zero defect”, messbar über:

* **FPY:** > 99.5%  
* **CPK:** key processes > 1.67  
* **PPM:** < 100  
* **OTD:** > 98%

<div class="div-type-1">
    <h3>Core capability highlights</h3>
    <p>HILPCB Quality ist nicht nur Prozess—sondern Kultur. Wir investieren kontinuierlich in Automation, digitale Systeme und Training und verbinden Lean Manufacturing mit Industry 4.0, um Stabilität und Vorhersagbarkeit von Prototype bis Volume sicherzustellen.</p>
</div>

---

## 2. Manufacturing capability data: vom Drawing zur physischen PCB

Bare-board fabrication ist der Startpunkt der Wertschöpfung; Qualität bestimmt Performance und Reliability. HILPCB deckt Standard Multilayer bis High‑Frequency/High‑Speed, HDI und Rigid‑Flex ab.

| Process Step | Key Capability | Process Control Metrics | Mass Production Case |
| :--- | :--- | :--- | :--- |
| **Inner-layer imaging** | Min line/space: 2.5/2.5 mil | Post-etch width tolerance: ±10% | 5G base-station RF unit |
| **Drilling** | Min mechanical drill: 0.15mm; laser: 0.075mm | Hole position: ±0.025mm; wall roughness: < 25μm | Medical endoscope sensor board |
| **PTH & plating** | Hole copper: > 20μm; uniformity: > 90% | Plating CPK > 1.67; panel uniformity < 15% | Automotive ADAS controller |
| **Outer-layer imaging** | Registration: ±12.5μm | AOI coverage: 100%; false-call rate < 5% | HPC server motherboard |
| **Soldermask** | LDI exposure, min dam: 0.05mm | Mask thickness: 10–20μm (pads); alignment CPK > 2.0 | Consumer wearable device |
| **Surface finish** | ENIG/HASL/OSP/ImmAg/ImmSn | ENIG Au: 0.03–0.08μm; salt spray > 48h | Industrial PLC module |
| **Profiling** | Dim tolerance: ±0.1mm | V-Cut: ±0.05mm; CNC outline: ±0.075mm | Drone flight-control system |

Im Soldermask‑Prozess folgen wir den Prinzipien der **soldermask exposure tutorial**. LDI ersetzt Film‑Exposure, entfernt Alignment‑Fehler durch Film‑Dehnung und stellt sicher, dass Fine‑Pitch BGA/QFN Soldermask‑Openings korrekt sind—und Bridging verhindert wird.

---

## 3. Quality tools: data-driven Prozessoptimierung

* **SPC:** Echtzeit‑Charts (X-bar/R) auf plating/etch/lamination; frühzeitige Intervention.
* **CPK:** interner Standard CPK > 1.67 (über 1.33); Six‑Sigma‑Stabilität.
* **MSA:** GR&R für Messsysteme; nur validierte Daten fließen in SPC/CPK.
* **8D:** strukturierte RCA + CAPA; Lessons Learned in FMEA.
* **Digital dashboards:** FPY/PPM/OEE sichtbar für Transparenz und Ownership.

<div class="div-type-6">
    <h3>Our manufacturing strength</h3>
    <p>Durch die Kombination aus Quality Tools und digitalen Systemen entsteht eine Plattform mit Selbstdiagnose/Selbstoptimierung. So erkennen wir Probleme nicht nur—wir können sie vorhersagen und verhindern.</p>
</div>

---

## 4. SMT/Assembly capability und Defect Control

SMT bestimmt PCBA‑Performance. Unsere DFM‑Guidance ist so detailliert wie ein **smt stencil design tutorial**: frühe Beratung zu apertures, thickness und step stencil für optimale paste volume/shape/position.

**Key controls:**
* **SPI:** 100% 3D SPI; Defekte außerhalb ±50% Threshold werden gestoppt.
* **Pick & Place:** 01005 und 0.3mm pitch BGA/CSP; Kamera + Library‑Check.
* **Reflow:** dedizierte Profile; tägliche Verifikation (KIC); Prozessfenster kontrolliert.
* **AOI:** vor/nach Reflow 100% Inspection.
* **X-Ray:** 2D/3D für BGA/LGA/QFN; **x ray inspection checklist** inkl. Voiding < 25%, Bridging, Head‑in‑Pillow, Alignment.

---

## 5. Test coverage: vollständige Qualitätsvalidierung

| Test Type | Description | Coverage | Target Defects |
| :--- | :--- | :--- | :--- |
| **ICT** | Probes test points; checks opens/shorts and values. | 85%–95% component-level defects | Opens, shorts, wrong/missing parts, wrong values |
| **FPT** | Flying probes without nail bed. | 80%–90% component-level defects | Similar to ICT with higher flexibility |
| **FCT** | End-use simulation; validates functions. | 100% functional modules | Functional failures, out-of-spec, logic errors |
| **Hipot** | High-voltage insulation/clearance test. | Safety-critical power paths | Breakdown, insufficient clearance |
| **Burn-in** | Long run under harsh conditions. | 100% finished products | Early-life failures, latent solder defects |
| **Reliability tests** | Temp cycling, vibration, drop, salt spray. | Sampling or per customer | Insufficient margin, poor robustness |

---

## 6. Traceability: Lebenszyklusakte von Komponenten bis Produkt

Barcode/Serial ab bare board; Material lots in SMT gebunden; Prozessdaten von SPI/Placement/Reflow/AOI erfasst; ICT/FCT Daten integriert; alles in Data Lake + Visualisierung. Das ermöglicht präzise Recall‑Scopes und datengetriebene Prozessverbesserung.

---

## 7. DFM/DFT/DFR Checklist: Customer Collaboration

| Category | Checkpoint | Recommendation |
| :--- | :--- | :--- |
| **DFM (Fabrication)** | Material selection | FR-4/Rogers/Teflon nach Rate/Temp/Cost wählen. |
| | Stackup | Symmetrisch/balanced; Core/PP passend. |
| | Minimum line/space | ≥15% Margin. |
| | Copper-to-edge | ≥0.2mm; nicht auf V-Cut/CNC routen. |
| | Soldermask dam | >0.075mm empfohlen. |
| | Via type & size | Through-holes bevorzugen; annular ring ausreichend. |
| | Via-in-Pad | Resin plug + planarization. |
| | Panelization | Rails + fiducials + Fixture‑Gedanken. |
| | Silkscreen | Nicht auf Pads; lesbar. |
| | Impedance control | Nets markieren; Stackup+Targets liefern. |
| **DFA (Assembly)** | Spacing | Rework/Inspection‑Clearance. |
| | Orientation | Wave‑solder alignment. |
| | Pad design | IPC-7351. |
| | Large parts | Stress reduzieren. |
| | Heat-sensitive | Away from hot spots. |
| | Fiducials | ≥2/board, 3/tooling rail. |
| | Stencil apertures | BGA/QFN reduction; präzise 0201/01005. |
| | Test points | >0.8mm dia; >2.54mm pitch. |
| | Connector placement | Edge + strain relief. |
| | Cleaning | Flux type definieren. |
| **DFT (Testability)** | Coverage | >90% critical nets. |
| | Distribution | Für bed-of-nails. |
| | Unobstructed | Kein mask/silk; fern von tall parts. |
| | JTAG/SWD | Standard interfaces. |
| | Isolation design | Resistors/jumpers. |
| | Power tests | Pro rail test points. |
| | Mechanical | Fixture clearance. |
| | FCT interface | Robust, fool-proof. |
| **DFR (Reliability)** | Thermal design | Thermal Vias/copper/heatsink. |
| | ESD | ESD devices. |
| | Decoupling | Near pins. |
| | SI | Match/length tune. |
| | PI | Wide/short, no sharp corners. |
| | Anti-vibration | Glue/screws. |
| | Moisture/corrosion | Finish + conformal coating. |

<div class="div-type-3">
    <h3>Collaborative improvement path</h3>
    <p><strong>Early design involvement:</strong> Vor Gerber‑Release kann HILPCB ein DFM/DFT/DFR Review anhand von Schaltplan/Mechanik liefern und Risiken früh eliminieren.</p>
</div>

---

## 8. Collaboration case + call to action

**Case: Medical PCBA**

* Challenge: BGA voiding >30% + crosstalk → FCT pass <80%.  
* Actions: Via-in-Pad auf resin plug + planarization umgestellt; Stencil optimiert (**smt stencil design tutorial**‑Style); SI‑Sim + Reroute/Stackup + GND vias; 3 RF test points ergänzt.  
* Results: voiding <5%, FPY **99.7%**, Zertifizierung bestanden, 6 Wochen schneller.

[**Contact our engineering team for a free DFM review**](/contact-us)

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Dieses Paper beschreibt Capability Indices, Yield‑Verbesserung, Quality Tools, Test Coverage und Traceability nach soldermask exposure tutorial‑Logik, plus DFM/DFT/DFR Checklist. HILPCB DFM/DFA früh einbinden beschleunigt Prototype und Volume bei Qualität und Compliance.

> Für fabrication/assembly: [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).


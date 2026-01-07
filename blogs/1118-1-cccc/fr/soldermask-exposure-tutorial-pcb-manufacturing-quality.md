---
title: "soldermask exposure tutorial : livre blanc de quality management pour PCB manufacturing"
description: "soldermask exposure tutorial détaillé : process capability, yield improvement, quality tools, test coverage et traceability—avec checklist DFM/DFT/DFR pour une collaboration efficace."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 9
tags: ["soldermask exposure tutorial", "smt stencil design tutorial", "x ray inspection checklist", "pcb fabrication process steps"]
---
## 1. Executive summary : objectifs qualité et metrics

Chez HILPCB, la qualité est un pilier opérationnel, pas une inspection isolée. Ce livre blanc décrit notre système end‑to‑end (fabrication, assembly, test) et comment nous utilisons le contrôle data‑driven, des quality tools et une collaboration DFM/DFT/DFR pour dépasser les attentes.

Comme un **soldermask exposure tutorial** définit énergie/alignement/temps pour protéger les traces et ouvrir correctement les pads, notre qualité applique le même niveau de précision sur toute la chaîne. Objectif “zero defect” via :

* **FPY:** > 99.5%  
* **CPK:** key processes > 1.67  
* **PPM:** < 100  
* **OTD:** > 98%

<div class="div-type-1">
    <h3>Core capability highlights</h3>
    <p>La qualité HILPCB est aussi une culture : investissements continus en automation, systèmes digitaux et formation, en combinant lean manufacturing et Industry 4.0 pour stabilité/prédictibilité du prototype au volume.</p>
</div>

---

## 2. Manufacturing capability data

| Process Step | Key Capability | Process Control Metrics | Mass Production Case |
| :--- | :--- | :--- | :--- |
| **Inner-layer imaging** | Min line/space: 2.5/2.5 mil | Post-etch width tolerance: ±10% | 5G base-station RF unit |
| **Drilling** | Min mechanical drill: 0.15mm; laser: 0.075mm | Hole position: ±0.025mm; wall roughness: < 25μm | Medical endoscope sensor board |
| **PTH & plating** | Hole copper: > 20μm; uniformity: > 90% | Plating CPK > 1.67; panel uniformity < 15% | Automotive ADAS controller |
| **Outer-layer imaging** | Registration: ±12.5μm | AOI coverage: 100%; false-call rate < 5% | HPC server motherboard |
| **Soldermask** | LDI exposure, min dam: 0.05mm | Mask thickness: 10–20μm (pads); alignment CPK > 2.0 | Consumer wearable device |
| **Surface finish** | ENIG/HASL/OSP/ImmAg/ImmSn | ENIG Au: 0.03–0.08μm; salt spray > 48h | Industrial PLC module |
| **Profiling** | Dim tolerance: ±0.1mm | V-Cut: ±0.05mm; CNC outline: ±0.075mm | Drone flight-control system |

Sur la soldermask, l’LDI supprime les erreurs d’alignement dues au film et sécurise les ouvertures fine pitch BGA/QFN, réduisant le bridging.

---

## 3. Quality tools

SPC, CPK > 1.67, MSA (GR&R), 8D + FMEA, et dashboards FPY/PPM/OEE.

<div class="div-type-6">
    <h3>Our manufacturing strength</h3>
    <p>En combinant quality tools et systèmes digitaux, nous construisons une plateforme capable de détecter, prédire et prévenir les dérives—réduisant le risque qualité.</p>
</div>

---

## 4. SMT/assembly : capability et defect control

Notre DFM guide est aussi détaillé qu’un **smt stencil design tutorial**. Contrôles clés : SPI 3D 100%, pick&place 01005/0.3mm pitch BGA, reflow profiles dédiés, AOI pre/post, X‑ray 2D/3D avec **x ray inspection checklist** (Voiding <25%, bridging, Head‑in‑Pillow, alignment).

---

## 5. Test coverage

| Test Type | Description | Coverage | Target Defects |
| :--- | :--- | :--- | :--- |
| **ICT** | Probes test points; checks opens/shorts and values. | 85%–95% component-level defects | Opens, shorts, wrong/missing parts, wrong values |
| **FPT** | Flying probes without nail bed. | 80%–90% component-level defects | Similar to ICT with higher flexibility |
| **FCT** | End-use simulation; validates functions. | 100% functional modules | Functional failures, out-of-spec, logic errors |
| **Hipot** | High-voltage insulation/clearance test. | Safety-critical power paths | Breakdown, insufficient clearance |
| **Burn-in** | Long run under harsh conditions. | 100% finished products | Early-life failures, latent solder defects |
| **Reliability tests** | Temp cycling, vibration, drop, salt spray. | Sampling or per customer | Insufficient margin, poor robustness |

---

## 6. Traceability

Serial/barcode dès la bare board, binding lots matière, capture des paramètres SPI/placement/reflow/AOI, intégration ICT/FCT, data lake + visualisation pour RCA rapide et recall précis.

---

## 7. Checklist DFM/DFT/DFR

La checklist suivante aide à intégrer fabrication/test/reliability dès le design (materials/stackup, soldermask dam, via-in-pad, panelization, fiducials, stencil, test points, JTAG/SWD, thermal, ESD, etc.).

<div class="div-type-3">
    <h3>Collaborative improvement path</h3>
    <p><strong>Early design involvement:</strong> avant Gerber, nos ingénieurs peuvent faire une évaluation DFM/DFT/DFR basée sur schéma + mécanique pour éliminer les risques tôt.</p>
</div>

---

## 8. Case study & call to action

Cas medical PCBA : voiding BGA >30% + crosstalk → FCT <80%. Actions : Via-in-Pad resin plug + planarization, optimisation stencil, SI sim + reroute/stackup + ground vias, +3 test points RF. Résultats : voiding <5%, FPY **99.7%**, -6 semaines.

[**Contact our engineering team for a free DFM review**](/contact-us)

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Ce papier décrit process capability, yield improvement, quality tools, test coverage et traceability, avec checklist DFM/DFT/DFR. Impliquer tôt l’équipe DFM/DFA de HILPCB accélère prototype et volume tout en maintenant qualité et compliance.

> Support fabrication/assembly : [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).


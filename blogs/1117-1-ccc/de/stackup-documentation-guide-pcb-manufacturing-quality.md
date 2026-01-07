---
title: "stackup documentation guide: Ein prozessgetriebenes Playbook für PCB Manufacturing und Testing"
description: "Mit einer stackup documentation guide als Backbone führt dieser End-to-End-Walkthrough durch Manufacturing-Details, Quality-Control Checkpoints und DFM/DFT Tipps – von Materials und Imaging bis Soldermask, SMT und Test Validation."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["stackup documentation guide", "soldermask exposure tutorial", "smt stencil design tutorial", "pcb fabrication process steps", "yield improvement roadmap", "surface finish selection tips"]
---
Hallo, ich bin Dozent an der HILPCB Manufacturing Academy. In der täglichen Praxis sehe ich häufig, dass viele Design Engineers eine `stackup documentation guide` als „nur“ ein Dokument behandeln, das Laminationsaufbau und Impedance Control definiert. Aus Manufacturing- und Test-Perspektive ist sie jedoch der „Genesis Blueprint“ und die „Execution Constitution“ des gesamten Production Flows. Sie bestimmt nicht nur die elektrische Performance, sondern beeinflusst Yield, Reliability und Cost in jeder Phase – von Incoming Materials bis zum finalen Functional Testing.

Heute nutzen wir dieses Kerndokument als roten Faden, um den kompletten PCB-Manufacturing- und Test-Flow durchzugehen. Das ist nicht nur ein **pcb manufacturing tutorial**, sondern auch eine **yield improvement roadmap**, die Design Intent mit Manufacturing Reality verbindet. Wir brechen komplexe Prozesse in SOP-ähnliche Schritte und Checklists herunter, damit dein Team DFM (Design for Manufacturability) und DFT (Design for Testability) wirklich verinnerlicht.

## Manufacturing flow overview: vom Stackup-Dokument zum physischen Produkt

Eine detaillierte `stackup documentation guide` ist der Startpunkt der Fabrication. Sie definiert Materials, Thickness, Copper Weight und Tolerances – Parameter, die das Process Window auf der Produktionslinie setzen. Die Tabelle zeigt, wie zentrale Manufacturing Steps direkt auf Informationen aus dem Stackup-Dokument abgebildet werden.

| Process Step | Core Objective | Key Control Parameters | Related Stackup Info |
| :--- | :--- | :--- | :--- |
| **Laminate preparation** | Sicherstellen, dass Materials den Design-Anforderungen entsprechen | Material type, board thickness, copper thickness, dimensional accuracy | Core- und prepreg (PP) types, Dk/Df, Tg, CAF resistance |
| **Inner-layer imaging** | Inner-Layer-Patterns exakt replizieren | Exposure energy, develop time, registration (±25 µm) | Inner-layer copper thickness (z. B. 0.5 oz, 1 oz), minimum line/space |
| **Lamination** | Multilayer-Struktur zu einem Verbund pressen | Temperature/pressure/time profile, resin-flow control | Stack order, PP type/quantity, overall thickness tolerance (±10%) |
| **Drilling** | Through Holes und Mounting Holes erzeugen | Spindle speed, feed rate, hole-position accuracy (±50 µm) | Hole size, hole type (PTH/NPTH/blind/buried), hole density, minimum annular ring |
| **Plating** | Interlayer Electrical Connection aufbauen | Rectifier current density, bath chemistry, copper thickness (>20 µm) | Aspect ratio, copper thickness requirements |
| **Outer-layer imaging** | Outer-Layer-Patterns exakt replizieren | Registration, etch-factor control | Outer-layer copper thickness, impedance-trace width, BGA/QFN pad sizes |
| **Soldermask** | Traces schützen und solderable areas definieren | Ink type/thickness, exposure accuracy, curing conditions | Soldermask color, minimum Solder Mask Dam width |
| **Surface finish** | Solderability und Schutz bereitstellen | Plating thickness (z. B. ENIG: Au 0.03–0.08 µm), flatness | [Surface Finish](/blog/pcb-surface-finish/) (HASL, ENIG, OSP, etc.) |
| **SMT assembly** | Components platzieren und löten | Paste volume, placement accuracy, reflow profile | BOM, packages, pad design |
| **Test & validation** | Electrical Function und Reliability sicherstellen | Coverage, fault-diagnosis accuracy | Test-point layout, net connectivity |

## Präzisionskontrolle von Imaging, Etching und Soldermask

Trace Width und Spacing hängen direkt an Signal Integrity und Impedance Control – und sind im Stackup-Dokument eng definiert. Die Manufacturing Challenge ist, diese Zahlen auf realen Boards exakt zu reproduzieren.

### Etch process window: Zahlen in Realität übersetzen

Etching ist ein subtraktiver Prozess: Unerwünschtes Copper wird entfernt, Traces bleiben stehen. Der Etchant greift jedoch nicht nur nach unten an, sondern auch lateral – es entsteht Undercut. Zur Kompensation wenden wir „Etch Compensation“ auf die Design Data an, indem Traces im Phototool vorab verbreitert werden.

<div class="div-style-1">

#### Process window: trace etching

- **Target**: ±10% Toleranz auf die designte Trace Width erreichen.
- **Input**: Stackup-definierte Copper Thickness (z. B. 1 oz HTE Copper).
- **Key parameters**:
    - **Etch compensation**: 1 oz Copper benötigt typischerweise 25–35 µm Compensation.
    - **Etch rate**: 1.2–1.8 m/min, gesteuert über Chemistry Concentration und Temperature.
    - **Undercut control**: High-Precision Spray Systems und dedizierte Etchants halten Undercut innerhalb von 12 µm.
- **Inspection method**: 100% AOI, mit Cross-Section Analysis für kritische Linien zur Messung von line/space.
- **DFM tip**: Bei [impedance control design](/blog/what-is-impedance-control-in-pcb/) mit deinem Fabricator Etch-Tolerance-Capability abstimmen und ausreichend Design Margin vorsehen.

</div>

### soldermask exposure tutorial: mehr als „grüne Farbe“

Solder mask ist die „Outer Layer“ der PCB, aber die Rolle geht weit über Ästhetik hinaus. Sie definiert solderable areas und verhindert Solder Bridging während der Assembly. HILPCB nutzt LDI (Laser Direct Imaging), das eine höhere Genauigkeit bietet als klassische Film Exposure.

<div class="div-style-3">

#### Soldermask LDI process steps

1.  **Surface pretreatment**: Chemical Cleaning plus Mechanical Brushing, um Surface Roughness zu erhöhen und Ink Adhesion sicherzustellen.
2.  **Ink coating**: In einem Cleanroom Liquid Photoimageable Soldermask gleichmäßig via Automated Screen Printing oder Spray aufbringen. Thickness auf Pads 8–15 µm und auf Traces 20–30 µm kontrollieren.
3.  **Pre-curing**: Kurzes Bake bei 75–85°C, um die Ink für LDI Exposure anzutrocknen.
4.  **LDI exposure**: Laser scannt die Soldermask direkt (ohne Film); Registration erreicht ±15 µm. Das ist kritisch, um Soldermask Dams zwischen Fine-Pitch Parts (z. B. 0.4 mm BGA) zu bilden.
5.  **Developing**: Im Developer waschen; unexposed areas werden entfernt und Pads freigelegt.
6.  **Final curing**: Langes Bake im Tunnel Oven bei ~150°C, um die Soldermask vollständig auszuhärten und starke physische/chemische Performance zu erzielen.

Das ist ein klassisches **soldermask exposure tutorial** – der Kern ist die Kontrolle von Energy und Accuracy, damit Soldermask Dams nicht cracken oder sich verschieben.

## Drilling, Plating und PTH Quality Control

Vias sind die „vertical highways“ von Multilayer Boards – ihre Reliability ist kritisch. Das Stackup-Dokument definiert Via Types (through, blind, buried) und Sizes, die Drilling- und Plating-Entscheidungen direkt beeinflussen.

### Drilling: Accuracy und Hole-Wall Quality

High Aspect-Ratio Holes (Board Thickness / Hole Diameter) sind sowohl fürs Drilling als auch fürs Plating herausfordernd. Beispiel: Ein 0.2 mm Hole durch eine 2.0 mm Board Thickness ergibt ein Aspect Ratio von 10:1.

- **Drilling control**: HILPCB nutzt High-Speed Pneumatic Spindles (>150k RPM) und X-Ray-assisted Registration, um accurate Inner-Layer Pad Alignment in Multilayer Boards sicherzustellen. Für Microvias (<0.15 mm) wird Laser Drilling genutzt.
- **Plasma de-smear**: Drilling Heat kann Resin schmelzen und Smear erzeugen, das Inner-Layer Copper bedeckt und Electrical Connection verschlechtert. Plasma De-smear entfernt Resin Residue von Hole Walls und stellt zuverlässige Copper Adhesion im folgenden Plating sicher.

### PTH copper: das Fundament der Reliability

Copper Thickness und Uniformity in Holes bestimmen maßgeblich, ob eine PCB Thermal Shock (z. B. beim Soldering) und Long-Term Operation übersteht. Industriestandards wie IPC-6012 verlangen typischerweise eine durchschnittliche PTH Copper Thickness ≥ 20 µm.

- **Control method**: Wir bauen eine leitfähige Base Layer mit Electroless Copper auf und verdicken PTH und Surface Copper mit Pattern Plating. HILPCB Plating Lines nutzen Advanced Dynamic Current Control und High-Circulation Filtration, um dichte, uniforme Deposits selbst in High-Aspect-Ratio Holes zu gewährleisten.
- **Inspection**: Regelmäßige Cross-Section Analysis mit Metallography Microscopes misst PTH Copper Thickness und prüft Hole-Wall Quality, damit keine Voids, Cracks oder verwandte Defects vorliegen.

## SMT soldering und Assembly Essentials

Nach der Bare-Board-Fabrication geht der Prozess in PCBA (Printed Circuit Board Assembly) über. Pad Design, Soldermask Definition und Component Placement – alles im Stackup-Dokument verankert – beeinflussen den SMT-Erfolg direkt.

### Stencil design: Ursprung der Solder-Paste-Printing-Qualität

Solder Paste Printing ist der erste SMT Step und verursacht mehr als 60% der Soldering Defects. Ein gutes **smt stencil design tutorial** betont, dass Stencil Design entscheidend ist.

- **Aperture design**: Aperture Size/Shape bestimmt das Paste Volume. Wir folgen Area Ratio (>0.66) und Aspect Ratio (>1.5) Regeln, um unvollständiges Paste Release zu vermeiden. Für Fine Parts wie 0201 und 0.4 mm BGA werden Electropolished oder Nano-Coated Stencils genutzt, um Release zu verbessern.
- **Thickness selection**: Stencil Thickness (typischerweise 100–150 µm) wird basierend auf den kleinsten Pitch Components auf dem Board gewählt – ein klassisches Beispiel, wie Design Intent an Process Constraints gekoppelt wird.

### Reflow soldering: die Kunst des Temperature Profiling

Reflow Soldering verbindet Components dauerhaft mit der PCB. Der Kern ist präzise Profile Control, um Flux zu aktivieren, Solder zu schmelzen und zuverlässige IMC zu bilden.

<div class="div-style-1">

#### Process window: lead-free reflow temperature profile

- **Target**: Helle, volle Solder Joints ohne Cold Joints, Opens, Tombstoning usw.
- **Input**: Solder Paste Datasheet (z. B. SAC305), PCB Laminate/Thickness, maximale Component Thermal Mass.
- **Key parameters**:
    - **Preheat**: 150–180°C, 60–90 s; sanft rampen, um Thermal Shock zu vermeiden.
    - **Soak**: 180–210°C, 60–120 s; Flux aktivieren und Board Temperature ausgleichen.
    - **Reflow**: Peak 240–250°C; Time above liquidus (217°C) 45–75 s.
    - **Cooldown**: Cooling Rate < 4°C/s, um feinkörnige Struktur zu bilden und Joint Strength sicherzustellen.
- **Inspection method**: HILPCB nutzt 3D SPI, 3D AOI und X-Ray Inspection für 100% Monitoring der Soldering-Qualität.

</div>

## Cleaning, Conformal Coating und Reliability Protection

Für High-Reliability Applications (Medical, Automotive, Aerospace) sind Post-Solder Cleanliness und Schutz kritisch.

- **Cleaning**: Selbst bei „no-clean“ Flux können Residues in Humid- oder High-Voltage Environments Electrochemical Migration (ECM) verursachen und Shorts auslösen. HILPCB bietet Aqueous Cleaning und nutzt Ion Chromatography (IC), um Cleanliness zu verifizieren und sicherzustellen, dass Ionic Residue unter Industry Limits liegt (z. B. verlangt IPC J-STD-001 <1.56 µg/cm² NaCl Equivalent).
- **Conformal coating**: Nach Cleaning und Drying bietet selektives Sprühen eines transparenten Conformal Coating starken Schutz gegen Humidity, Salt Fog und Mold und verlängert die Lebensdauer in Harsh Environments deutlich.

## Testing matrix: sicherstellen, dass jeder Node korrekt ist

DFT muss end-to-end angewendet werden. Wenn ein Produkt nicht ausreichend getestet werden kann, ist Quality nicht garantiert. Wir nutzen eine gestufte Testing Matrix, um Coverage sicherzustellen.

| Test Stage | Test Method | Primary Goal | Coverage / defect types |
| :--- | :--- | :--- | :--- |
| **After bare-board fab** | Flying Probe Test (FPT) / Bed of Nails | Opens/Shorts validieren | 100% net connectivity; etch/drill defects |
| **After SMT** | 3D AOI | Soldering Appearance inspizieren | Wrong/missing parts, polarity, cold joints, bridging, tombstoning |
| **SMT critical parts** | 3D X-Ray | Hidden Joints (BGA, QFN) inspizieren | BGA shorts, voids, Head-in-Pillow (HoP) |
| **PCBA circuit level** | ICT | Component Parameters und Nets prüfen | Wrong values, opens/shorts, digital logic functions |
| **PCBA functional level** | FCT | End Use simulieren und Functions validieren | Firmware programming, I/O, interfaces, power |
| **System level** | SLT / Burn-in | Stabilität und Performance unter Real Conditions validieren | Compatibility issues, intermittent faults, early failures |
| **Reliability validation** | HALT/HASS, temp-humidity cycling, vibration | Long-Term Reliability und Margin bewerten | Weak points, potential failure modes |

Diese **testing matrix** ist das Rückgrat unserer Quality Assurance – von mikroskopischen Solder Joints bis zur System-Level Functionality.

## Quality und Traceability: die Power von Data

In modernem Manufacturing wird Quality nicht „hineininspectiert“, sondern „hineingebaut“ und „hineingemanagt“.

- **SPC (Statistical Process Control)**: Wir setzen SPC Monitoring Points über Key Steps wie Etching, Plating und Reflow ein, um Process Parameters (z. B. Chemistry Concentration, Oven Temperature) in Echtzeit zu tracken. Driften Trends, alarmiert das System sofort, damit Engineers eingreifen, bevor Defects systemisch werden.
- **MES (Manufacturing Execution System)**: HILPCB Lines werden vollständig über MES gemanagt. Jede PCB/PCBA hat einen eindeutigen QR Code als „ID Card“. Von Incoming Materials (verwaltet über unser Smart Warehousing System) bis zum finalen Shipment werden alle Process Data, Equipment Parameters, Personnel Information und Test Results an diesen QR Code gebunden. Das ermöglicht echte End-to-End Traceability: Werden Issues gefunden, lässt sich der Impact innerhalb von Minuten lokalisieren – ob es ein bestimmtes Component Lot ist oder ein Equipment-Parameter-Anomaly in einem Zeitfenster.

<div class="cta-box">
    <p>Ein perfektes Stackup Design braucht einen ebenso starken Manufacturing- und Test-Partner, um real zu werden. HILPCB MES System und umfassende Test Capability stellen sicher, dass dein Design Intent präzise umgesetzt wird und liefern voll transparente Traceability Data. Willst du sehen, wie dein nächstes Projekt profitieren kann?</p>
    Upload deine Gerber Files jetzt, um eine DFM/DFT Evaluation zu erhalten
</div>

## HILPCB’s integrierte Manufacturing + Test Capability

Eine `stackup documentation guide` in ein High-Reliability Electronic Product zu übersetzen erfordert Advanced Equipment, strikte Prozesse und spezialisierte Expertise. HILPCB bietet mehr als Fabrication – wir liefern eine One-Stop Solution von Design Optimization bis Test Validation.

<div class="div-style-6">

#### HILPCB core manufacturing and test capabilities

- **Advanced PCB fabrication**:
    - **Materials**: Unterstützt High-Frequency/High-Speed Materials wie Rogers, Taconic und Isola.
    - **Processes**: 20+ layers, 0.15 mm mechanical microvias, laser blind/buried vias, step copper/step slots, backdrilling, gold fingers und weitere Complex Builds.
    - **Precision control**: LDI exposure, plasma cleaning, X-Ray registration, um Yield für [HDI](/blog/what-is-hdi-pcb/) Builds sicherzustellen.

- **Smart PCBA assembly**:
    - **Automated lines**: Vollautomatisierte Paste Printers, High-Speed Placement und 12-Zone Reflow Ovens; unterstützt 01005 Placement.
    - **Closed-loop inspection**: 3D SPI + 3D AOI + 3D X-Ray schließen den Data Loop und optimieren Printing/Placement Parameters in Echtzeit.
    - **Smart storage**: Temperatur-/Humidity-kontrollierte Intelligent Storage zum Schutz von Components – besonders MSD Parts.

- **Comprehensive test lab**:
    - **In-house test capability**: ICT/FCT Development plus Flying Probe Testers, High-Resolution X-Ray, Environmental Chambers (Temperature/Humidity), Vibration Tables, Salt-Spray Chambers usw.
    - **Reliability services**: Vollständige **reliability checklist** Validation, inklusive Thermal Shock, Mechanical Shock, Vibration Tests und HALT/HASS Accelerated Life Testing.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

`stackup documentation guide` ist die Brücke zwischen Design und Manufacturing. Zu verstehen, wie sie jeden Downstream Step beeinflusst – von Etch Compensation und Reflow Profiles bis zu Test-Point Planning – ist eine Pflichtkompetenz für jeden Great Engineer. Bei HILPCB sind wir nicht nur der Executor deines Dokuments, sondern auch dein DFM/DFT Partner. Mit prozessgetriebenen, datengesteuerten und intelligenten Manufacturing- und Test-Systemen stellen wir sicher, dass dein Design Intent präzise und zuverlässig umgesetzt wird – und sich letztlich in Produkte mit starker Market Competitiveness verwandelt.

> Need fabrication and assembly support? Kontaktiere HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) für DFM/DFT Recommendations.


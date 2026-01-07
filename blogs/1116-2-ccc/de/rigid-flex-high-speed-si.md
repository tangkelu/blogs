---
title: "Rigid-flex PCB: Ultra-High-Speed Links und Low-Loss Challenges für High-Speed SI"
description: "Vertiefung zu Rigid-flex PCB – High-Speed SI, Thermal Management und Power-/Interconnect-Design – für High-Performance High-Speed SI PCBs."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["Rigid-flex PCB", "Copper coin", "ENIG/ENEPIG/OSP", "Backdrill quality control", "Hybrid stack-up (Rogers+FR-4)", "Microvia/stacked via"]
---
Als Measurement- und Consistency-Validation-Engineer (TDR/VNA, S-Parameter) weiß ich: In Ultra-High-Speed/High-Density Designs entscheidet die Wahl der Interconnect-Technologie oft über Erfolg oder Misserfolg. **Rigid-flex PCB** liefert 3D-Routing-Flexibilität und hohe Zuverlässigkeit und wird zum Kernwerkzeug gegen komplexe High-Speed-SI-Probleme. Es ist nicht nur Träger – es ist der Schlüssel für Channel-Consistency vom Chip bis zum Connector.

Dieser Beitrag erklärt aus SI-Validierungs-Sicht Vorteile und Herausforderungen von Rigid-flex PCB und wie Materialien, Stackups und Fertigungsprozesse Attenuation, Crosstalk und Impedance Discontinuities bei 28G/56G/112G+ adressieren. Fokus: Hybrid stackups, Microvia/stacked via, Surface Finish, Backdrill, und Copper coin Thermals.

### Warum Rigid-flex PCB für High-Speed entscheidend ist

Klassisch verbinden Kabel/Steckverbinder mehrere Rigid Boards. Bei Gbps-Raten erzeugen diese Interfaces starke Discontinuities und Loss. Jede Konversion ist wie ein „Speed Bump“ für Eye Opening und Jitter Budget.

Rigid-flex PCB integriert Rigid und Flex nahtlos und eliminiert mechanische Interconnects. Vorteile:
1) bessere SI (geringere IL/RL, glattere TDR Profile),
2) 3D Packaging und Integration (kürzere kritische Pfade),
3) höhere Reliability (keine Connector-Failures),
4) geringere System-TCO durch weniger Teile/Assembly.

### SI und Kosten via Hybrid stack-up optimieren

Low Dk/Df reduziert Loss, aber Voll-Rogers/Megtron ist teuer. **Hybrid stack-up (Rogers+FR-4)** kombiniert Materialien nach Funktionsbedarf:
- High-Speed Layers: Rogers RO4350B/RO4835, Tachyon 100G etc.
- Power/Low-Speed: High-Tg FR-4.

Wichtige Punkte:
1) Symmetrischer Stackup gegen Warpage,
2) Material-Kompatibilität in der Lamination,
3) korrekte Dk/Df Werte in Impedance-Modellen.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#000000; text-align:center;">Hybrid Stackup: Performance vs Kosten</h3>
<table style="width:100%; border-collapse: collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Stackup</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Use Case</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">SI</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Relative Kosten</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Fertigungs-Komplexität</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All FR-4</td>
<td style="padding:12px; border:1px solid #ccc;">&lt; 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">ok</td>
<td style="padding:12px; border:1px solid #ccc;">★</td>
<td style="padding:12px; border:1px solid #ccc;">niedrig</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Hybrid stack-up (Rogers+FR-4)</td>
<td style="padding:12px; border:1px solid #ccc;">5 - 56 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">sehr gut</td>
<td style="padding:12px; border:1px solid #ccc;">★★★</td>
<td style="padding:12px; border:1px solid #ccc;">hoch</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All Rogers/Megtron</td>
<td style="padding:12px; border:1px solid #ccc;">&gt; 56 Gbps / RF</td>
<td style="padding:12px; border:1px solid #ccc;">Top</td>
<td style="padding:12px; border:1px solid #ccc;">★★★★★</td>
<td style="padding:12px; border:1px solid #ccc;">mittel</td>
</tr>
</tbody>
</table>
</div>

### Microvia/stacked via im Rigid-flex

Mit 0.5mm-BGA-Pitch und darunter sind Through-Holes limitierend. **Microvia/stacked via** ist Standard:
- Microvia (Laser, <150µm): geringe Parasiten, mehr Fanout.
- Stacked via: direkte Vertikal-Interconnects, kurze Wege.

Erfordert Laser Drilling und Plated-filled Prozess, plus Microsection-Validation. HILPCB kann die Reliability für [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) absichern.

### SI-Challenges in Flex Zones

Flex Transition/Bend Zones sind am schwierigsten:
1) Impedance Control durch Polyimide/Coverlay Toleranzen,
2) Bending verändert Geometrie/Delay; Differential Symmetrie und Neutral Axis wichtig,
3) Hatched Ground erzeugt Return-Path-Discontinuity → Crosstalk/EMI Trade-off.

<div style="background: #ffffff; border: 1px solid #d1c4e9; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(103,58,183,0.08);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 40px 0; font-size: 1.8em; font-weight: 800; border-bottom: 4px solid #9575cd; padding-bottom: 15px; display: inline-block; width: 100%;">🌀 Flex Zone: Design-Matrix für High-Speed SI & Reliability</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">01. Circular Traces & Impedance</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">In Bend Areas <strong>Circular Traces</strong> erzwingen und 90°/45° vermeiden.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">02. Teardrop</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Teardrop</strong> an Pad-Trace Junctions erhöht Fläche und reduziert Stress.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">03. Stiffener</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>FR-4/PI Stiffener</strong> an Connectors/SMT zur Stress-Entkopplung.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">04. No-Via in Bending Radius</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Keine Vias im <strong>Bending Radius</strong>; Layer Transitions in Rigid/Static Zones.</p>
</div>
</div>
<div style="margin-top: 30px; background: #311b92; color: #ffffff; padding: 25px; border-radius: 16px; border-left: 8px solid #9575cd;">
<strong style="color: #b39ddb; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 HILPCB: Balanced Copper Design</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Staggered Traces</strong> reduzieren Twist (I-Beam Effect) und halten Impedance Variation nach Millionen Bends niedrig.</p>
</div>
</div>

### Surface Finish vs High-Speed Loss

OSP ist bei HF lossarm, aber limitierte Reflow-Zyklen. ENIG/ENEPIG sind solderability-stark, aber Nickel erhöht High-Frequency Loss (v. a. >10GHz). Für 28Gbps+ wenn möglich OSP oder nickel-freies Immersion Gold; ansonsten SI durch Stackup/Routing kompensieren.

### Backdrill quality control

Via Stubs resonieren (¼-Wavelength) und erzeugen S21 Notches. Backdrilling entfernt Stubs; Qualität hängt an Z-Depth Control (±2 mil typisch) und Stub-Verifikation via TDR/Microsection. Ohne sauberes **Backdrill quality control** drohen Overdrill und Link-Failure.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#FFFFFF; text-align:center;">HILPCB High-Precision Capability</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; text-align: center;">
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Max Layer</h4>
<p style="margin: 0; font-size: 1.2em;">64L (Rigid), 20L (Rigid-flex)</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Min Trace/Space</h4>
<p style="margin: 0; font-size: 1.2em;">2.5 / 2.5 mil</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Impedance Tolerance</h4>
<p style="margin: 0; font-size: 1.2em;">±5%</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Backdrill Depth Tol.</h4>
<p style="margin: 0; font-size: 1.2em;">±0.05mm</p>
</div>
</div>
</div>

### Copper coin für lokale Thermals

**Copper coin** ist ein eingebetteter Cu-Block, der direkt am Thermal Pad sitzt und über Thermal Vias Wärme effizient ableitet. Vorteile: hohe Cu-K (≈400 W/m·K), kein extra Volumen, mechanisch stabil. Erfordert präzise Fertigung (Lamination/CNC), um Delamination/Voids zu vermeiden.

### Manufacturing & Test Consistency bei HILPCB

DFM + Simulation, präzise **Microvia/stacked via**, stabile **ENIG/ENEPIG/OSP**, striktes **Backdrill quality control**, sowie VNA/TDR Validierung (S-Parameters, Impedance Coupons). Zusätzlich One-Stop Service inkl. [SMT assembly](https://hilpcb.com/en/products/smt-assembly).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

**Rigid-flex PCB** ist Mainstream für Miniaturisierung, Integration und High-Speed. Erfolgreich wird es durch fundiertes Verständnis von Material, EM und Fertigung – plus gezielte Umsetzung von **Hybrid stack-up (Rogers+FR-4)**, **Microvia/stacked via**, **ENIG/ENEPIG/OSP**, **Backdrill quality control** und **Copper coin**. Mit einem erfahrenen Partner wie HILPCB lassen sich komplexe Designs sicher in High-Performance-Produkte überführen.


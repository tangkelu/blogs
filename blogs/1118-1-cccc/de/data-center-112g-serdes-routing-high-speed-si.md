---
title: "data-center 112G SerDes routing: Ultra-High-Speed-Links und Low-Loss-SI-Constraints"
description: "Deep Dive zu data-center 112G SerDes routing: Channel Budget, Materialien, Stack-up, Impedance Control, Via/Connector-Transitions, DFM und Validierung für High-Speed-SI-PCBs."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---
Mit dem explosiven Wachstum von AI, ML und Cloud Computing steigt der Traffic in Data Centern rasant. Um das zu bedienen, migriert die Industrie schnell von 56G NRZ/PAM4 auf 112G PAM4 SerDes. Das verdoppelt nicht nur die Lane‑Rate, sondern verschärft die SI‑Anforderungen drastisch. Erfolgreiches **data-center 112G SerDes routing** ist kein „nur verbinden“ mehr, sondern System Engineering aus Materialkunde, EM‑Theorie, Thermik und Precision Manufacturing. Aus Sicht von Messung und Compliance beleuchtet dieser Artikel die Kernprobleme und Gegenmaßnahmen für 112G‑Channels.

Vom Package‑BGA‑Pad über PCB‑Traces/Vias, Connector/Backplane bis zum Rx: die physikalische Channel‑Performance entscheidet, ob 112G sauber wiederhergestellt wird. Kleine Impedance‑Diskontinuitäten, zu hohe Dielectric Loss oder unoptimierte Vias können den Budget‑Spielraum zerstören und BER explodieren lassen. Eine vollständige **high-speed 112G SerDes routing**‑Strategie muss Material, Stack-up, Impedance Control und Fertigungstoleranzen früh integrieren, damit das Ergebnis performant, zuverlässig und fertigungssicher ist.

### Warum ist das 112G‑Channel‑Budget so hart?

Der Sprung von 56G auf 112G ist mehr als „doppelte Frequenz“. Bei 112G PAM4 liegt Nyquist bei 28 GHz; Loss und Noise werden deutlich kritischer. Gegenüber NRZ ist die PAM4‑Eye‑Höhe nur ein Drittel, SNR‑Margin sinkt. Deshalb ist das Insertion‑Loss‑Budget (IL) eine der härtesten Constraints in **data-center 112G SerDes routing**.

Ein typischer 112G‑LR‑Channel ist oft auf ~30–35 dB @ 28GHz Gesamtverlust begrenzt – verteilt auf Package, PCB‑Traces, Vias, Connector und Rx‑Packaging.

- **Insertion Loss (IL):** Hauptproblem. FR-4 ist bei 28 GHz zu verlustreich; die Eye schließt.
- **Return Loss (RL):** durch Impedance‑Diskontinuitäten (Vias, Connector, BGA Pads). Reflections erzeugen ISI.
- **Crosstalk:** hohe Dichte → starke Kopplung; NEXT/FEXT senken SNR.
- **COM:** Channel Operating Margin kombiniert IL/RL/Crosstalk und Equalizer‑Capability; COM‑Optimierung ist Standard in 112G.

Budget‑Einhaltung erfordert exakte End‑to‑End‑Modelle und enge Zusammenarbeit mit erfahrenen Herstellern (z. B. HILPCB), damit Simulation und Fertigung übereinstimmen.

### Low-Loss-Materialien: das Fundament für 112G

Materialien setzen die physikalische Basis. Bei 28 GHz bestimmen Dk/Df die Dämpfung. Die richtige Materialwahl ist Schritt eins für **data-center 112G SerDes routing**.

- **Dk und Df:** Df ist der zentrale Loss‑Indikator. Für 112G werden häufig Ultra Low Loss Materialien benötigt (z. B. Df < 0.004 @ 10GHz): Tachyon 100G, Megtron 6/7/8, Rogers RO4000. Dk‑Stabilität ist kritisch für **112G SerDes routing impedance control**.
- **Skin Effect:** Strom fließt bei 28 GHz an der Oberfläche → höhere effektive R → Conductor Loss.
- **Copper Roughness:** raue Oberfläche verlängert Strompfad und verschärft Loss; VLP/HVLP wird empfohlen.
- **Fiber Weave Effect:** Glas (Dk≈6) vs Resin (Dk≈3) → lokale Effective‑Dk‑Variation, Impedance Ripple und Skew. Gegenmaßnahmen: Spread Glass und Routing um 1–5° gedreht.

Material ist auch ein Cost/DFM/Supply‑Trade‑off. Ein gutes **112G SerDes routing guide** empfiehlt frühe Abstimmung mit dem Hersteller.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Materialvergleich für High-speed PCB</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Materialklasse</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Typische Materialien</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Df @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dk @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Typische Rate</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standard Loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Medium Loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Low Loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra Low Loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Präzises Impedance Control und Routing‑Disziplin

Impedanzkontrolle ist der Kern von High‑Speed‑SI. In **high-speed 112G SerDes routing** erzeugt jede Abweichung von der Zielimpedanz (typisch 90Ω/100Ω diff) Reflections, Jitter und ISI. **112G SerDes routing impedance control** braucht Design‑ und Fertigungsmaßnahmen.

**Design:**
1.  **Stack-up präzise berechnen:** 2D‑Solver (z. B. Polar Si9000) mit Material‑Dk, Dielectric‑Thickness, Trace‑Width/Spacing und Cu‑Thickness; Toleranzen berücksichtigen und mit dem Hersteller abgleichen.
2.  **Geometrie‑Regeln:**
    *   **In‑Pair‑Match:** P/N‑Längen strikt matchen; bei 112G oft 1–2 mil.
    *   **Keine scharfen Ecken:** Bögen/45° statt 90°.
    *   **Kontinuierliche Reference Plane:** keine Splits queren.

**Fertigung:**
Process Control entscheidet über Impedanzgenauigkeit:
- **Etching‑Präzision:** L/S‑Toleranz ±5% oder besser.
- **Lamination‑Control:** stabile Core/PP‑Dicken.
- **TDR‑Tests:** Coupon‑Messungen, z. B. ±7% Spec‑Check.

### Vias und Connector‑Transitions: kritische Diskontinuitäten

Vias sind oft die größten Diskontinuitäten in **data-center 112G SerDes routing**. Unoptimierte Vias können einen 112G‑Channel zerstören.

- **Via Stub:** ungenutzter Barrel‑Teil resoniert und erzeugt Notches in S21. Bei 28 GHz sind schon wenige 10 mil kritisch. **Back-drilling** auf 5–10 mil Stub.
- **Via‑Optimierung:** Pad/Anti-pad/Barrel‑Geometrie per 3D‑EM (HFSS, CST) optimieren, Anti-pad anpassen, Reflections reduzieren.
- **Connector Footprint:** QSFP-DD/OSFP‑Transitions co‑optimieren; Non-Circular Pads und lokale Ground‑Clearances sind typische **112G SerDes routing layout**‑Techniken.

Microvias und Blind/Buried Vias in [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) reduzieren Parasiten und unterstützen High‑Density‑**high-speed 112G SerDes routing**.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes PHY: Regeln für Vias und Transitions</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Impedanzkontinuität und Common‑Mode‑Suppression unter PAM4</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Stub‑Eliminierung & Back-drill‑Genauigkeit</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regel:</strong> 112G ist extrem sensibel auf <strong>Stub‑Resonanzen</strong>. Full‑Depth‑Back-drill und Stub strikt **&lt;8 mil** halten, um die erste Resonanz über 40GHz zu schieben.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Antipad‑Kompensation per 3D‑EM</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regel:</strong> keine Heuristiken. Antipad‑Durchmesser und Pad‑Geometrie via <strong>3D Full‑Wave EM</strong> co‑optimieren, parasitäre C kompensieren und diff‑Impedanzvariation innerhalb **±5%** halten.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Shadowing Vias</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regel:</strong> um jedes diff‑Via‑Pair symmetrisch **2–4 Ground‑Return‑Vias** platzieren; Loop‑Area reduzieren und Inter‑Layer‑Crosstalk‑Isolation besser als **-40dB** erzielen.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. BGA‑Breakout & Prozesswahl</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regel:</strong> bei 0.8mm‑Pitch und kleiner **VIPPO** bevorzugen. Bei Dog‑Bone‑Breakout die kurze Segmentbreite kompensieren, um lokale HF‑Diskontinuitäten zu vermeiden.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>HILPCB‑Hinweis:</strong> 112G steht und fällt mit <strong>Back-drill Tolerance</strong>. Neben Gerber‑Checks sollte die Capability für <strong>Laser Back-drilling</strong> bzw. kontrollierte Tiefe (T-Control) bestätigt werden, damit Serienabweichungen keine unerwarteten Notches erzeugen.
</div>
</div>

### Layout‑Kernpunkte für 112G SerDes

Ein gutes **112G SerDes routing layout** ist Timing‑/Isolation‑Kunst. In dichten Designs ist Crosstalk nach IL die zweitgrößte Constraint.

- **Abstand:** „3W/5W“‑Rule (W = Trace‑Width) als Baseline. In Engstellen Guard Trace (Ground) zwischen Pairs.
- **Stack-up/Routing:**
    *   **Stripline vs. Microstrip:** Stripline in Innenlagen bietet bessere EMI‑Abschirmung/Isolation und ist für lange 112G‑Runs bevorzugt; Microstrip kann etwas weniger Loss haben, ist aber störanfälliger.
    *   **Orthogonal Routing:** benachbarte Signal‑Lagen orthogonal routen (L3 horizontal, L4 vertikal).
- **BGA‑Breakout:** höchste Dichte; Via‑Platzierung, Layer‑Assignment und Reference‑Plane‑Splits sorgfältig planen. Ein **112G SerDes routing guide** ist hier praktisch Pflicht.
- **Power Integrity (PI):** PDN‑Noise wird zu Clock Jitter. Decaps und PDN‑Impedanz‑Simulation sind nötig, um Low‑Impedance über Band zu halten.

### Equalization und Jitter: Co‑Design von Chip bis Channel

Auch mit besten Materialien bleibt bei langen Channels ISI. SerDes kompensiert Loss über DSP/Equalization.

- **Tx EQ:** FFE mit Pre-emphasis/De-emphasis.
- **Rx EQ:** CTLE (HF‑Boost) und DFE (Post‑Cursor‑ISI‑Cancel), mit Risiko der Error‑Propagation.

Ziel ist ein „gutartiger“ Channel, den Equalizer leicht kompensiert, nicht ein extrem verlustreicher Channel mit Over‑Reliance. Für optimale COM‑Margin sollten SI‑Engineers IBIS-AMI nutzen und Channel + Equalizer gemeinsam optimieren.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4 Channel Simulation Sign‑off</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">COM‑Analyse – Summary</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Insertion Loss (IL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">COM</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Status: PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE target: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ILD</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Ripple: good</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ERL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Reflection: compliant</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
💡 <strong>Engineering note:</strong> IL is -32dB, only 3dB from the -35dB floor. Considering Dk/Df tolerances, run Monte Carlo on <strong>HVLP copper roughness</strong> before mass production.
</div>
</div>

### Vom Prototyp zur Serie: DFM

Simulation ohne wirtschaftliche/reliable Fertigung ist wertlos. Design–Manufacturing‑Co‑Optimization ist zentral für **data-center 112G SerDes routing**, egal ob **112G SerDes routing low volume** oder Serie.

- **Toleranzen:** Etch‑ und Laminations‑Variation verschieben Impedanz. Process Capability Guide nutzen und früh Monte Carlo fahren.
- **Surface Finish:** ENIG ist oft bevorzugt, aber Black‑Pad‑Risiko; ENEPIG bietet bessere Reliability. Trade‑off aus Kosten/Performance/Soldering.
- **DFM Checks:** vor Gerber/ODB++‑Release DFM (Drills, Annular Ring, Acid Traps etc.) – Rework vermeiden.

One‑Stop‑Partner mit Equipment und Prozesskontrolle sichern First‑Build‑Performance und Lot‑Consistency; z. B. HILPCB von [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) bis Assembly.

### Compliance‑Tests: Performance nachweisen

„No measurement, no truth.“ 112G‑Validation braucht professionelle Methoden:

1.  **S‑Parameter:** VNA‑Messung, Sdd21/Sdd11/Crosstalk, Vergleich zur Simulation und COM.
2.  **TDR:** Impedanzprofile für Traces/Vias zur Verifikation von **112G SerDes routing impedance control**.
3.  **Eye/BER:** Pattern‑Gen + BERT, Eye Diagram und BER (z. B. BER < 1E-6).

Diese Tests sind in R&D und Production‑QC essenziell.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Erfolgreiches **data-center 112G SerDes routing** ist anspruchsvolles System Engineering. Ultra Low Loss‑Materialien, präzises Stack-up/Impedance Control sowie Via/Connector‑Optimierung sind entscheidend. Den Channel als Gesamtsystem betrachten, früh EM‑Simulation nutzen, Equalization verstehen und DFM priorisieren – so entsteht der beste Trade‑off aus Performance, Cost und Reliability.

Für 112G und darüber hinaus ist ein Partner wie Highleap PCB Factory (HILPCB) – mit Design‑Verständnis und Fertigungs‑Exzellenz – ein praktischer Beschleuniger. One‑Stop‑Support von Materialberatung und DFM bis High‑Precision‑Build und Validation macht aus dem Blueprint ein robustes, leistungsfähiges Produkt.


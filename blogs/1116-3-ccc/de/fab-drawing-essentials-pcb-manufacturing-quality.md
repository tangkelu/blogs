---
title: "Fab drawing essentials: 20 häufige Fragen aus Fertigung und Test"
description: "Übersicht zu 20 typischen fab drawing essentials Problemen in Manufacturing/Assembly/Testing—Symptome, Root Causes und Lösungen—inkl. Defect-Countermeasure-Matrix und Quality-Audit-Checklist."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["fab drawing essentials", "smt stencil design tutorial", "soldermask exposure tutorial", "stackup documentation guide", "surface finish selection tips", "yield improvement roadmap"]
---
## Einleitung: warum Fab Drawing das Fundament der PCB-Produktion ist

In einem komplexen PCB-Manufacturing-Ökosystem ist **Fab Drawing** das einzige „Legal Document“ und die Single Source of Truth für technische Kommunikation. Ein detailliertes, korrektes Fab Drawing ist der Startpunkt für hohen Yield und hohe Reliability—und der Kern jeder **yield improvement roadmap**. Umgekehrt kann jede Unklarheit, Mehrdeutigkeit oder ein Fehler in der Zeichnung eine Kettenreaktion in Fertigung, Assembly und Test auslösen: Cost Overruns, Schedule Slips oder sogar Field Failures.

Rund um **fab drawing essentials** fasst dieser Beitrag 20 häufige Probleme entlang des gesamten Flows zusammen. Für jedes Thema betrachten wir Symptome, messbare Kennzahlen, Root Causes sowie praktikable Corrective/Preventive Actions—damit Ihre Fab Drawing „keine Fragen offen lässt“.

---

## Teil 1: Manufacturing FAQ

Probleme in der Fertigung hängen oft direkt mit physikalischen/chemischen Prozessen zusammen—und lassen sich häufig auf Material-, Stack-up- und Toleranzdefinitionen in der Fab Drawing zurückführen.

### 1. Problem: warum tritt nach Reflow starkes Warpage auf?

-   **Symptome**: Die Leiterplatte biegt oder verdreht sich nach dem Aufheizen; Placement wird schwierig; BGA kann Open/Short zeigen.
-   **Kennzahlen**: Warpage > 0,75% (IPC-A-610 Class 2/3). Formel: (max. Verformung / PCB-Diagonale) × 100%.
-   **Root Causes**:
    1.  **Asymmetrischer Stack-up**: Unausgewogene Copper Distribution im Stackup führt zu CTE-Mismatch.
    2.  **Falsche Materialwahl**: High Tg Material nicht spezifiziert oder Materialien mit unterschiedlichem CTE gemischt.
    3.  **Große Copper Areas**: Große Copper Pours ohne Cross-hatching/Mesh erhöhen interne Spannungen.
-   **Lösung**: Bake + Press-Flatting als Rework—aber mit begrenzter Wirkung.
-   **Prevention**:
    -   Im **stackup documentation guide** symmetrischen, copper-balanced Stack-up verbindlich fordern.
    -   Alle Core- und PP-Typen inkl. Dicke und Supplier spezifizieren.
    -   Copper Areas > 500 mm² als Mesh/Cross-hatch ausführen und in Notes definieren.

### 2. Problem: unzureichende PTH-Copper-Thickness oder Voids im Hole?

-   **Symptome**: Schlechte Via-Kontinuität, hoher Widerstand, Opens nach Thermal Shock oder Vibration.
-   **Kennzahlen**: IPC-6012 Class 2: durchschnittliche Hole Copper Thickness < 20 μm; Class 3 typischerweise ≥ 25 μm. Void Count > 1 oder Void Length > 5% des Hole Diameter.
-   **Root Causes**:
    1.  **Unklare Anforderungen**: Fab Drawing spezifiziert weder IPC Class (2/3) noch numerische Targets.
    2.  **High Aspect Ratio**: Aspect Ratio > 10:1 erschwert Plating, ohne spezielle Prozessanforderung in der Zeichnung.
    3.  **Schwache Drill Quality**: Raue Hole Wall/Smear reduziert Copper Deposition.
-   **Lösung**: Micro-section Analyse des Lots; bei Fail meist Scrap.
-   **Prevention**:
    -   In Drill Table + Notes klar definieren: „Hole Copper Thickness gemäß IPC-6012 Class 3, Average ≥ 25 μm“.
    -   Für Aspect Ratio > 10:1 Enhanced Processes wie Pulse Plating fordern.

### 3. Problem: Solder Mask Bridge löst sich oder ist zu ungenau?

-   **Symptome**: Solder Mask Dams zwischen Fine-Pitch Pads (z. B. QFP, BGA) reißen ab—Solder Bridging/Shorts.
-   **Kennzahlen**: Solder Mask Dam Width < 75 μm (3 mil) oder physisches Peeling im SMT/Reflow.
-   **Root Causes**:
    1.  **Solder Mask Opening falsch definiert**: Opening ist relativ zum Pad zu groß (typisch +2–3 mil je Seite empfohlen).
    2.  **Mask-Prozess nicht spezifiziert**: High-Precision LDI nicht gefordert, klassische Belichtung reicht bei Fine Pitch nicht.
-   **Lösung**: Manuelles Repair (teuer/geringe Reliability) oder Paste-Reduktion via Stencil.
-   **Prevention**:
    -   Solder Mask Opening Rules klar definieren oder präzise Solder Mask Gerber mitliefern.
    -   Gemäß **soldermask exposure tutorial** in Notes: „Bei Pitch ≤ 0,4 mm ist LDI zwingend.“

### 4. Problem: Cleanliness nicht ausreichend, Ion Residues vorhanden?

-   **Symptome**: Unter High Temp/Humidity treten Leakage, ECM oder Dendrites auf—bis zum Circuit Failure.
-   **Kennzahlen**: Ion Chromatography > 0,65 μg/cm² (NaCl äquivalent), nicht konform zu IPC-J-STD-001.
-   **Root Causes**: Fab Drawing definiert keinen Cleanliness Grade; es wird nur Standard-Cleaning gefahren, ohne Fokus auf kritische Zonen (z. B. unter BGA).
-   **Lösung**: Plasma Cleaning oder Ultrasonic Cleaning am fertigen Board.
-   **Prevention**: In Fab Drawing festlegen: „Finished Boards erfüllen IPC-J-STD-001 Class 3 Cleanliness und liefern Ion-Contamination Report.“

### 5. Problem: ungleichmäßige/oxidierte Surface Finish Plating Thickness?

-   **Symptome**: Schlechte Solderability, geringe Joint Strength, Gold Fingers mit Contact Issues. Bei ENIG tritt „Black Pad“ auf.
-   **Kennzahlen**: ENIG Au < 1,27 μm (0,05 mil) oder Ni < 2,54 μm (0,1 mil). OSP-Film degradiert nach mehreren Reflows.
-   **Root Causes**:
    1.  **Standard nicht angegeben**: Fab Drawing nennt „ENIG“, aber keinen Standard/Thickness (z. B. IPC-4552).
    2.  **Falsche Prozesswahl**: Laut **surface finish selection tips** ungeeignete Surface Finish für High-Frequency/Fine-Pitch (z. B. HASL).
-   **Lösung**: Nicht reparabel; meist Scrap.
-   **Prevention**:
    -   Surface Finish + Standard definieren, z. B.: „ENIG gemäß IPC-4552A, Au 0,05–0,1 μm, Ni 3–6 μm“.
    -   Für kritische Bereiche (Gold Fingers) separate Hard-Gold Anforderungen spezifizieren.

### 6. Problem: Back Drilling Depth Control ungenau, Stub zu lang?

-   **Symptome**: Schlechte SI bei High-Speed Links, starke Reflections und Insertion Loss.
-   **Kennzahlen**: Stub Length nach Backdrill > 10 mil.
-   **Root Causes**: Backdrill Definition in Fab Drawing ist unklar.
    1.  **Depth nicht definiert**: Start (Top/Bottom) und Stop Layer fehlen.
    2.  **Stub Tolerance fehlt**: Max. erlaubter Stub ist nicht angegeben.
-   **Lösung**: Nach Fertigung nicht reparabel.
-   **Prevention**:
    -   Separaten Backdrill Layer + Backdrill Table bereitstellen.
    -   Für jedes Hole „Start Layer“, „Stop Layer“ und „Max Stub“ (z. B. 8 mil) definieren.

<div class="custom-block-type-6">
    <h4>HILPCB Capability Showcase</h4>
    <p>HILPCB verfügt über moderne LDI-Exposure, Pulse-Plating Lines und Depth-Control Drilling Equipment, um strenge Fab-Drawing-Anforderungen präzise umzusetzen. Von High-Aspect-Ratio Holes bis 20:1 bis zu Backdrill Depth Control innerhalb ±5 mil: unsere automatisierten Prozesse stellen sicher, dass jede PCB exakt Ihrer Design-Intention entspricht—für maximale Performance-Sicherheit.</p>
</div>

---

## Teil 2: Assembly FAQ

Assembly Defects hängen eng mit Pad Design, Solder Mask Opening und Stencil Design zusammen—und sollten bereits in der Fab Drawing standardisiert werden.

### 7. Problem: viele Solder Balls nach SMT?

-   **Symptome**: Kleine Solder Balls rund um Chip Components (C/R), mit Short-Risiko.
-   **Kennzahlen**: In 6,5 cm² > 5 Solder Balls mit Ø > 0,13 mm (IPC-A-610).
-   **Root Causes**:
    1.  **Solder Mask Opening zu groß**: Paste fließt beim Reflow auf die Mask und bildet Balls.
    2.  **Stencil Apertures ungeeignet**: Widerspricht **smt stencil design tutorial** Best Practices.
    3.  **Moisture im Laminat**: Fab Drawing spezifiziert Packaging/Storage nicht.
-   **Lösung**: Manuell entfernen und reinigen.
-   **Prevention**:
    -   NSMD oder SMD Regeln festlegen und Opening-Toleranzen exakt definieren.
    -   Vacuum Packaging gemäß MSL Anforderungen verlangen.

### 8. Problem: Tombstoning bei Chip Components?

-   **Symptome**: Eine Seite von 0402/0201 richtet sich auf („Tombstone“).
-   **Kennzahlen**: Eine Seite löst sich vollständig vom Pad.
-   **Root Causes**:
    1.  **Asymmetrische Pads**: Unterschiedliche Pad-Größe oder stark unterschiedliche Copper Areas verursachen unbalancierte Surface Tension.
    2.  **Mask auf dem Pad**: Solder Mask Precision ist unzureichend, Pad wird teilweise bedeckt.
-   **Lösung**: Rework des Bauteils.
-   **Prevention**:
    -   Interne Footprint Library oder IPC-7351 in Fab Drawing referenzieren.
    -   Mask-Residues auf Pads verbieten und Min Clearance definieren.

### 9. Problem: viele Voids nach BGA/QFN Soldering?

-   **Symptome**: X-Ray zeigt Voids in BGA Balls oder unter QFN Thermal Pad—Thermal/Long-Term Reliability leiden.
-   **Kennzahlen**: Void Area > 25% pro Joint (IPC-7095B).
-   **Root Causes**:
    1.  **Via-in-Pad nicht sauber definiert**: VIP ohne Fill/Capping Vorgabe; Outgassing erzeugt Voids.
    2.  **Stencil Design**: Große Thermal Pads ohne Window/Grid Aperture—Entgasung schlecht.
-   **Lösung**: Praktisch nicht reparabel; Component Replacement ist teuer.
-   **Prevention**:
    -   In Fab Drawing festlegen: „Alle Via-in-Pad werden mit Conductive/Non-Conductive Resin gefüllt und plated capped; Flatness < 1 mil.“
    -   In Assembly Notes gemäß **smt stencil design tutorial** Windowpane/Dot-Matrix Apertures für QFN Thermal Pads empfehlen.

### 10. Problem: Head-in-Pillow (HIP) bei BGA?

-   **Symptome**: BGA Balls wirken kontaktierend, coalescen aber nicht vollständig—schwacher „Pillow“-Joint, stress-anfällig.
-   **Kennzahlen**: 3D X-Ray oder Micro-section zeigt Delamination an der Ball/Paste Interface.
-   **Root Causes**:
    1.  **PCB Warpage**: siehe Problem 1; Gap im BGA Center.
    2.  **Uneven Surface Finish**: ENIG Ni Corrosion oder OSP Oxidation—Solderability sinkt.
-   **Lösung**: Reballing oder Austausch.
-   **Prevention**:
    -   Stack-up Symmetry/Material Selection strikt einhalten, Warpage an der Quelle senken.
    -   Surface Finish Standards spezifizieren und Outgoing Solderability Reports anfordern.

<div class="custom-block-type-4">
    <h4>Risk Warning: eine unklare Fab Drawing ist eine „Zeitbombe“</h4>
    <p>Ein scheinbar kleiner Fehler—z. B. fehlende Via-in-Pad Fill Definition—kann eine komplette BGA-Lot-Failure verursachen und schnell zehntausende Euro kosten. Zeit in <strong>fab drawing essentials</strong> in der Designphase zu investieren, ist die effektivste Versicherung gegen spätere Großrisiken.</p>
</div>

### 11. Problem: Teardrops oder Solder Spikes nach Selective Soldering?

-   **Symptome**: Nach Selective Soldering von THT ist der Joint nicht voll, wirkt teardrop-förmig oder zeigt Spikes—nicht IPC-A-610-konform.
-   **Kennzahlen**: Wetting Angle < 270° oder sichtbare Solder Spikes.
-   **Root Causes**:
    1.  **Thermal Design schwach**: THT Holes direkt an große GND Planes gekoppelt—zu starke Heat Sinking.
    2.  **Mask Opening zu klein**: Solder Flow/Wetting wird behindert.
-   **Lösung**: Manuelle Nacharbeit, aber schlechte Optik/Consistency.
-   **Prevention**:
    -   Thermal Relief Pads für THT Holes an großen Copper Areas fordern.
    -   Mask Openings größer als THT Pads auslegen, damit Solder fließen kann.

<div class="cta-container">
    <p>Ist Ihre Fab Drawing wirklich vollständig? HILPCB bietet kostenlose DFM/DFA Analyse. Unsere Engineers prüfen Ihre Files aus Manufacturing-, Assembly- und Testing-Perspektive, um Risiken vor Release zu erkennen und zu eliminieren. <strong>Laden Sie jetzt Ihre Gerber hoch und erhalten Sie einen professionellen Assessment Report!</strong></p>
</div>

---

## Teil 3: Testing FAQ

Testing-Probleme sind oft das Endergebnis von Manufacturing/Assembly-Issues—manche lassen sich aber direkt durch bessere Fab Drawing vermeiden.

### 12. Problem: ICT Probe Contact schlecht, False-Fail Rate hoch?

-   **Symptome**: Viele False Opens im ICT, manuell jedoch OK—Test-Effizienz sinkt.
-   **Kennzahlen**: ICT False-Fail > 5%.
-   **Root Causes**:
    1.  **Test Points nicht spezifiziert**: Fab Drawing definiert keine Min Size/Spacing/Shape; Pads zu klein/zu nah/zu nah am Edge.
    2.  **Surface Finish auf Test Pads**: Bei OSP kann der Film nach mehrfacher Kontaktierung leiden—Contact Issues.
-   **Lösung**: Probes reinigen, Fixture anpassen, Test Speed reduzieren.
-   **Prevention**:
    -   Dedizierten Test-Point Layer anlegen und notieren: „ICT Test Points: min Ø ≥ 0,8 mm, Pitch ≥ 1,27 mm; Surface plan, kein Solder Mask Cover.“
    -   Bei High-Density Testing: Gold oder Tin Plating für Test Pads spezifizieren.

### 13. Problem: FCT Scripts decken nicht alle Funktionen ab?

-   **Symptome**: FCT bestanden, aber beim Kunden treten Function Failures auf—bestimmte Module wurden nie getestet.
-   **Kennzahlen**: Coverage < 95%.
-   **Root Causes**: Fab Drawing enthält keine Test-Assists (z. B. Jumpers/Interfaces für Test Modes).
-   **Lösung**: Scripts/Fixtures aktualisieren; ggf. Recall/Field Upgrade.
-   **Prevention**:
    -   In Assembly Drawing alle Debug/Test Interfaces, Jumpers und Switch-Funktionen klar markieren.
    -   „Test Instruction“ beilegen: wie das Produkt in unterschiedliche Test Modes gesetzt wird.

### 14. Problem: Kriterien für Reliability Tests (z. B. Thermal Shock) unklar?

-   **Symptome**: Nach 500 Thermal Cycles (-40°C to 125°C) Streit über Pass/Fail bei Micro-Cracks oder Resistance Drift.
-   **Kennzahlen**: Keine klaren Accept/Reject Criteria.
-   **Root Causes**: Fab Drawing referenziert keine Reliability Standards oder definiert keine Grenzwerte.
-   **Lösung**: Temporäre Criteria zwischen Quality/Design/Customer.
-   **Prevention**:
    -   Conditions + Acceptance definieren, z. B.: „1000 Cycles -40°C bis 125°C; danach Via-Resistance Change < 10%“.
    -   Standards referenzieren, z. B.: „Reliability Anforderungen gemäß IPC-TM-650“.

### 15. Problem: Hipot False Trips oder Breakdown?

-   **Symptome**: Beim Dielectric-Withstand Test Alarm wegen Leakage, aber kein echter Breakdown.
-   **Kennzahlen**: Leakage > 10 mA (typisch) oder Arcing unterhalb der Spec Voltage.
-   **Root Causes**:
    1.  **Clearance/Creepage zu klein**: HV/LV Spacing nicht in Fab Drawing betont, nur Gerber-Defaults.
    2.  **Materialauswahl**: CTI Grade nicht nach Working Voltage gewählt.
-   **Lösung**: Alarmstelle analysieren: echter Breakdown vs. Surface Arcing durch Moisture/Contamination.
-   **Prevention**:
    -   HV-Zonen markieren und Min Clearance/Creepage definieren (z. B. „>3 mm for 500V AC“).
    -   CTI im Material List spezifizieren (z. B. CTI ≥ 400V).

---

## Teil 4: Quality FAQ

Quality Issues sind systemisch. Als Startpunkt bestimmt die Vollständigkeit der Fab Drawing die Robustheit des gesamten Quality Systems.

### 16. Problem: SPC Alarme triggern häufig?

-   **Symptome**: Bei Drilling, Line Width, Impedance etc. häufige Punkte außerhalb UCL/LCL.
-   **Kennzahlen**: Cpk < 1,33.
-   **Root Causes**:
    1.  **Toleranzen unrealistisch**: Zu strikte Fab-Drawing-Toleranzen gegenüber natürlicher Capability.
    2.  **CTQ nicht markiert**: Kritische Merkmale werden nicht identifiziert, daher kein Fokus im Shopfloor.
-   **Lösung**: Out-of-Control Points analysieren und Special/Common Causes unterscheiden.
-   **Prevention**:
    -   Toleranzen mit Supplier und **yield improvement roadmap** abstimmen.
    -   CTQ Merkmale mit Symbolen (z. B. `[CTQ]`) markieren (Impedance Trace Width, BGA Pad Dia etc.).

### 17. Problem: 8D Report lässt sich nach Complaint nicht schließen?

-   **Symptome**: Root Cause wird nicht schnell gefunden; 8D stoppt bei D4; Corrective Actions fehlen.
-   **Kennzahlen**: 8D Closure > 30 Tage.
-   **Root Causes**: Fab Drawing unvollständig—Traceability bricht. Beispiel: Material Model fehlt; bei Delamination ist Material vs. Prozess unklar.
-   **Lösung**: Umfangreiche DPA (Micro-section, SEM/EDX) zur Ursachenbestimmung.
-   **Prevention**:
    -   Vollständige Material List, Stack-up, Surface Finish Standards und Special Processes in der Fab Drawing.
    -   HILPCB mappt Fab-Drawing-Parameter auf Produktionsdaten (Lamination Profile, Plating Current). Im Fall eines Problems korreliert das 8D Data System Design Requirements mit Prozessparametern und lokalisiert Root Causes schneller.

<div class="custom-block-type-5">
    <h4>HILPCB Value: data-driven Quality Assurance</h4>
    <p>Wir sind mehr als ein Hersteller. HILPCB digitalisiert Ihre Fab Drawing und integriert sie tief in unser MES. Von Incoming Materials bis Shipment werden alle Key Parameters erfasst und überwacht. Für Traceability liefern wir ein vollständiges 8D Data Package von Design Specs bis realen Produktionsdaten—Root Cause Analysis wird deutlich effizienter.</p>
</div>

### 18. Problem: Quality Issue, aber Traceability Chain hat Lücken?

-   **Symptome**: Defect Batch erkannt, aber betroffene Boards/Shifts/Material Lots nicht präzise identifizierbar.
-   **Kennzahlen**: Kein vollständiger bidirektionaler Traceability Report innerhalb 24 h.
-   **Root Causes**: Fab Drawing fordert Traceability Markings nicht klar.
    1.  **Keine Unique Serial**: Kein QR/Serial pro PCB vorgeschrieben.
    2.  **Uneinheitliches Format**: Date Code, UL Mark, Part Number Position/Format nicht definiert.
-   **Lösung**: Recall Scope vergrößern, hoher Waste.
-   **Prevention**:
    -   Silkscreen muss enthalten: Part Number, Revision, UL Mark, Lead-free Symbol, Week Code (WW/YY).
    -   Für High-Reliability: Unique QR an definierter Position inkl. Encoding Rules.

### 19. Problem: Konsistenz zwischen unterschiedlichen PCB-Suppliern schlecht?

-   **Symptome**: Gleiche Gerber + Fab Drawing bei zwei Suppliern ergeben unterschiedliche Farbe, Impedance, Mechanik.
-   **Kennzahlen**: Key Electrical Params (z. B. TDR Impedance) unterscheiden sich > 10%.
-   **Root Causes**: „Interpretation Space“ in der Fab Drawing. Beispiel: nur „FR-4“ ohne S1141 vs IT-180A; „green solder mask“ ohne Color Code.
-   **Lösung**: Zusätzliche Tests/Screening je Lot.
-   **Prevention**:
    -   Material List so präzise wie möglich: „Manufacturer + Model“ oder AVL.
    -   Pantone Color Code für Solder Mask und Silkscreen Ink.
    -   Performance Requirements (Impedance, Dk/Df etc.) numerisch mit Toleranz definieren.

### 20. Problem: Final Certification (z. B. UL, CE) schlägt fehl?

-   **Symptome**: Zertifizierungsstelle lehnt ab wegen Flame Rating, Clearance/Creepage oder Materials.
-   **Kennzahlen**: Certification Fail → Redesign + Resubmission.
-   **Root Causes**: Safety/Compliance Anforderungen fehlen in Fab Drawing.
-   **Lösung**: Design ändern, neu mustern, neu testen—starke Verzögerung.
-   **Prevention**:
    -   Auf Seite 1 Standards prominent angeben: „UL 94V-0“, „RoHS Compliant“.
    -   Sicherstellen, dass Materialien/Mask Ink UL Yellow Card konform sind.
    -   Supplier-Qualification bestätigen; UL Mark + Factory Code auf dem Board verlangen.

---

## Zusatzinhalte

### Defect-Countermeasure-Matrix

Die folgende Tabelle fasst häufige Defects, Prozessschritte, Kennzahlen und Gegenmaßnahmen zusammen—ein Tool für schnelles Troubleshooting.

| Defect | Process step | Key metric | Corrective/Preventive action |
| :--- | :--- | :--- | :--- |
| **Warpage** | Stack-up, lamination | Warpage < 0.75% | **Prevention**: symmetrischen Stack-up und copper balance in Fab Drawing erzwingen. |
| **PTH Void** | Plating | Average hole copper thickness > 25 μm (Class 3) | **Prevention**: IPC Class klar definieren, Special Process für High Aspect Ratio Holes. |
| **Solder mask dam peeling** | Solder mask, exposure | Min dam width > 75 μm | **Prevention**: LDI fordern und Mask Opening Rules präzise definieren. |
| **BGA voids** | SMT, reflow | Void ratio < 25% | **Prevention**: Via-in-Pad Resin Fill + plated capping fordern. |
| **ICT contact issues** | Test | Test pad dia > 0.8 mm | **Prevention**: eigener Test-Point Layer + Design Rules in Fab Drawing. |
| **Traceability break** | Silkscreen, laser marking | Unique serial readability | **Prevention**: Unique QR an definierter Stelle + Format definieren. |
| **Impedance out of spec** | Etching, lamination | Impedance tolerance ±10% | **Prevention**: Stack-up Parameter (Dk, Df, Thickness) + Impedance Model angeben. |
| **Black Pad** | ENIG | Ni phosphorus content 7–9% | **Prevention**: ENIG gemäß IPC-4552A + XRF Report verlangen. |

### Fab Drawing Quality-Audit-Checklist

Vor dem Versand an den Hersteller prüfen Sie anhand der folgenden Liste, ob alle **fab drawing essentials** abgedeckt sind.

| # | Audit item | Status (Y/N) | Notes |
| :-- | :--- | :--- | :--- |
| 1 | Part number und Revision klar enthalten? | | |
| 2 | Board outline dimensions + tolerances definiert? | | |
| 3 | Detaillierte Stack-up Zeichnung vorhanden? | | Layer thickness, material model, copper weight |
| 4 | Alle Laminate Manufacturer/Model spezifiziert? | | oder AVL bereitgestellt |
| 5 | Final board thickness + tolerance definiert? | | |
| 6 | Vollständige Drill Table vorhanden? | | hole size, tolerance, hole type (PTH/NPTH) |
| 7 | Hole copper thickness Requirement (IPC class) definiert? | | |
| 8 | Special holes (blind/buried/backdrill) dokumentiert? | | |
| 9 | Min trace/space definiert? | | |
| 10 | Solder mask color/type/thickness spezifiziert? | | z. B. LPI, green, matte |
| 11 | Solder mask opening rules definiert? | | |
| 12 | Silkscreen color + min text height spezifiziert? | | |
| 13 | Surface finish type + standard definiert? | | z. B. ENIG per IPC-4552A |
| 14 | Impedance control Requirement? | | falls ja: values/tolerances/test method? |
| 15 | CTQ dimensions/features markiert? | | |
| 16 | Warpage requirement definiert? | | |
| 17 | Safety/environment markings enthalten? | | UL, RoHS, CE, etc. |
| 18 | Traceability markings (date code, serial) definiert? | | |
| 19 | Via-in-Pad Fill/Capping Requirements definiert? | | |
| 20 | Extra Requirements für Special Areas (gold fingers)? | | z. B. beveling, thicker gold |
| 21 | Electrical test requirements (flying probe/fixture) definiert? | | 100% E-Test |
| 22 | ICT test-point design rules vorhanden? | | |
| 23 | Cleanliness/Ionic contamination Requirements spezifiziert? | | |
| 24 | Packaging/shipping/storage Requirements spezifiziert? | | z. B. MSL level |
| 25 | Alle Notes klar, unambiguous, nicht veraltet? | | |

---

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Eine exzellente Fab Drawing ist weit mehr als ein Add-on zu Gerber Files: Sie ist die präzise Übersetzung der Design-Intention, die klare Definition der Manufacturing Constraints und ein starker Quality Backstop. Wenn Sie die 20 typischen Probleme systematisch adressieren und **fab drawing essentials** Best Practices in Ihren Prozess integrieren, erhöhen Sie Yield und Reliability deutlich und schaffen eine effiziente, transparente Zusammenarbeit in der Supply Chain—das Fundament einer erfolgreichen **yield improvement roadmap**.

<div class="cta-container">
    <p>Bereit, Ihr PCB Design auf das nächste Level zu bringen? Das Expertenteam von HILPCB unterstützt Sie gern. Wir liefern nicht nur Top-Manufacturing, sondern agieren als Design-Stage Partner—damit Ihre Fab Drawing von Anfang an „wasserdicht“ ist. <strong>Kontaktieren Sie uns jetzt und starten Sie Ihre High-Reliability PCB Journey!</strong></p>
</div>

> Für Manufacturing- und Assembly-Support kontaktieren Sie HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) für DFM/DFT Guidance.

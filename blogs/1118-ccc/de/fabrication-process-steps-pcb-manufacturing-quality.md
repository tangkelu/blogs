---
title: "PCB-Fertigungsprozessschritte: Praktischer Arbeitsablauf für PCB-Fertigung und Tests"
description: "Tiefgehende Analyse der Kerntechnologien für PCB-Fertigungsprozessschritte, die hochfrequente Signalintegrität, Wärmeverwaltung und Stromversorgung/Verbindungsdesign abdecken, um Ihnen bei der Erstellung hochperformanter PCBs zu helfen."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["PCB-Fertigungsprozessschritte", "PCB-Fertigungsprozess", "PCB-Qualitätskontrolle", "PCB-Testverfahren", "PCB-Zuverlässigkeit", "PCB-Massenproduktion"]
---

Als Dozent der HILPCB Manufacturing Academy werde ich häufig von Entwicklungsingenieuren und Projektmanagern mit einer Kernfrage konfrontiert: „Mein Design ist in der Software perfekt – warum gibt es in der Produktion trotzdem ständig Probleme?“ Die Antwort liegt in der engen Verzahnung von Design und Fertigung. **pcb fabrication process steps** zu verstehen, ist nicht nur Aufgabe von Prozessingenieuren, sondern Pflichtwissen für jeden Produktentwickler.

Dieses Tutorial führt Sie im Stil von SOPs und Checklisten durch den kompletten Weg – von der Kupferkaschierten Platte bis zur voll funktionsfähigen PCBA. Wir beleuchten Prozessfenster, Qualitätskontrollpunkte sowie DFM und DFT, um Risiken früh zu eliminieren und Ausbeute sowie Zuverlässigkeit zu erhöhen.

## 1. Überblick über PCB‑Fertigung und -Montage: vom Basismaterial zum Endprodukt

Bevor wir in Details gehen, brauchen wir eine Gesamtkarte. Die folgende Tabelle fasst die wichtigsten Phasen der PCB‑Fertigung und der anschließenden Montage/Tests zusammen. Das ist das Grundgerüst zum Verständnis der `pcb fabrication process steps`.

| Prozessphase (Process Stage) | Kernziel (Core Objective) | Schlüsselprozess/-Equipment (Key Process/Equipment) | Qualitätskontrollpunkt (Quality Control Point) |
| :--- | :--- | :--- | :--- |
| **Rohmaterialvorbereitung** | Sicherstellen, dass das Basismaterial den Designanforderungen entspricht | Copper‑Clad Laminate (CCL) Zuschnitt, Backen | Materialtyp, Kupferdicke, Tg‑Wert, Maßhaltigkeit |
| **Innenlagen‑Patterning** | Leiterbild auf innerer Kupferfolie bilden | Dry‑Film‑Lamination, Exposure, Development, Etching | Leiterbahnbreite/‑abstand, Open/Short, Etch‑Uniformity |
| **Lamination** | Innenlagen‑Core mit Prepreg verpressen | Lay‑up, Laminationspresse, Browning/Blackening | Alignment, Gesamtdicke, Dielektrik‑Dicke, keine Delamination/Voids |
| **Drilling** | Vias und Bauteillöcher erzeugen | Mechanical Drilling, Laser Drilling | Lochlagegenauigkeit, Lochwand‑Rauheit, kein Burr/Smear |
| **PTH** | Leitfähige Kupferschicht auf Lochwand aufbauen | Desmear, Electroless Copper, Electroplating | Lochkupferdicke (>20µm), Voids, Haftfestigkeit |
| **Außenlagen‑Patterning** | Außenlagen‑Leiterbild und Pads definieren | analog Innenlage, aber höhere Präzision | Impedance Control, Pad Definition, Leiterbild‑Integrität |
| **Solder Mask** | Leiterbild schützen und Lötbereiche definieren | LPI, Exposure, Development, Curing | Solder Mask Dam (>4mil), Alignment, keine Blasen/Peeling |
| **Surface Finish** | Kupfer schützen und Lötbarkeit bereitstellen | HASL, ENIG, OSP, Immersion Silver/Tin | Schichtdicke, Ebenheit, Lötbarkeit, Shelf Life |
| **E‑Test** | Open/Short auf dem Bare Board prüfen | Flying Probe Test (FPT), Fixture (ICT) | 100% Net‑Continuity |
| **SMT Assembly** | Bauteile auf PCB montieren | Solder Paste Printing, SPI, Placement, Reflow | Paste‑Volumen, Placement‑Offset/Polarity, Lötqualität |
| **Testing & Verification** | PCBA‑Funktion und Zuverlässigkeit sicherstellen | AOI, X‑Ray, ICT, FCT, Burn‑in | Lötdefekte, Bauteilfunktion, System‑Performance, Langzeitzuverlässigkeit |

---

## 2. Patterning, Etching und Solder Mask: drei Basissäulen für Präzision

Das Herz einer PCB sind die leitfähigen Strukturen. Ihre Präzision bestimmt direkt die elektrische Performance – insbesondere bei High‑Frequency und High‑Density.

### Pattern Transfer: das Design auf Kupfer replizieren

Ziel ist, das Leiterbild aus dem CAD möglichst exakt auf die Kupferfläche zu übertragen.

<div class="div-style-3">
    <h4>Standard Operating Procedure (SOP)</h4>
    <ol>
        <li><strong>Oberflächenvorbereitung:</strong> Durch Bürsten/Schleifen und chemische Reinigung Oxide und Verunreinigungen entfernen, Dry‑Film‑Adhäsion erhöhen.</li>
        <li><strong>Dry‑Film‑Lamination:</strong> Fotoempfindlichen Dry Film unter kontrollierter Temperatur und Druck gleichmäßig auflaminieren.</li>
        <li><strong>Exposure:</strong> UV‑Belichtung durch Film oder LDI (Laser Direct Imaging), damit die Leiterbildbereiche polymerisieren und aushärten.</li>
        <li><strong>Development:</strong> Unbelichteten Dry Film (z. B. mit Natriumcarbonat‑Lösung) auswaschen, Kupfer für das Etching freilegen.</li>
    </ol>
</div>

**DFM‑Empfehlungen:**
*   **Minimum Line Width/Spacing:** 1–2 mil Reserve zur Prozessgrenze des Herstellers einplanen, um Yield zu erhöhen.
*   **Sharp Corners/Acid Traps vermeiden:** Ecken als Radius oder 45° ausführen, um lokale Überätzung durch Ätzmittel‑Stau zu verhindern.

### Etching: die finalen Kupferleiter „herausarbeiten“

Beim Etching wird das nach dem Development freiliegende Kupfer (typisch CuCl2/FeCl3‑Systeme) entfernt – übrig bleibt das vom Dry Film geschützte Leiterbild.

<div class="div-style-1">
    <h4>Prozessfenster: Alkalisches Etching</h4>
    <ul>
        <li><strong>Parameter:</strong> Ätzmittel‑Konzentration, Temperatur, Sprühdruck, Fördergeschwindigkeit.</li>
        <li><strong>Ziel:</strong> Leiterbahnbreite präzise kontrollieren, Toleranz oft <strong>±12µm</strong>.</li>
        <li><strong>Herausforderung:</strong> Undercut. Ideales Etching ist vertikal; seitliche Erosion verjüngt Leiterbahnen. Über „Etch Factor“ und Parameteroptimierung werden steilere Seitenwände erzielt.</li>
    </ul>
</div>

### Solder Mask: die grüne „Rüstung“ der PCB

Solder Mask definiert nicht nur die Farbe, sondern hat kritische Funktionen:
1.  **Isolation/Schutz:** schützt nicht zu lötende Kupferflächen vor Oxidation und Short.
2.  **Lötdefinition:** legt Pads frei und verhindert Bridges bei Reflow/Wave.

**DFM‑Empfehlungen:**
*   **Solder Mask Dam:** Zwischen dichten Pins (QFP, BGA) ausreichend Dam‑Breite vorsehen; typisch ≥ 4 mil (0,1mm), um Shorts zu verhindern.
*   **Solder Mask Opening:** Öffnung typischerweise 1–2 mil pro Seite größer als Pad, damit das Pad vollständig frei liegt, ohne benachbarte Leiterbahnen zu exponieren.

## 3. Drilling und PTH: Z‑Achsen‑Verbindungen aufbauen

Die „Seele“ von Multilayern ist die vertikale Verbindung – sie hängt direkt von Drilling und PTH‑Qualität ab.

### Drilling: Synergie aus Mechanik und Laser

*   **Mechanical Drilling:** für Through‑hole und größere Blind/Buried Vias. Wichtige Parameter sind Drehzahl, Vorschub und Hit Count, um glatte Lochwände ohne Burrs zu erhalten.
*   **Laser Drilling:** für Microvias als Kerntechnologie von HDI; ermöglicht sehr kleine Durchmesser und hohe Interconnect‑Dichte.

**DFT‑Empfehlung:**
*   **Aspect Ratio:** Verhältnis Bohrtiefe zu Durchmesser. Für Standardprozesse typischerweise ≤ 10:1, sonst erhöhtes Risiko für unzureichende Lochkupferdicke oder Voids.

### PTH: isolierende Lochwände leitfähig machen

Nach dem Drilling bestehen Lochwände aus Harz/Glasfaser. PTH baut eine gleichmäßige Kupferschicht auf, um Layer elektrisch zu verbinden.

<div class="div-style-3">
    <h4>PTH – Kernschritte</h4>
    <ol>
        <li><strong>Desmear:</strong> Harzrückstände (drill smear) entfernen, innere Kupferringe freilegen.</li>
        <li><strong>Electroless Copper:</strong> Dünne, leitfähige Startschicht auf der gesamten Lochwand abscheiden.</li>
        <li><strong>Electroplating:</strong> Kupfer in Tankanlage auf Leiterbild und Lochwand verdicken. Typisch werden <strong>20–25µm</strong> gefordert, um Stromtragfähigkeit und Zuverlässigkeit sicherzustellen.</li>
    </ol>
</div>

Zur Qualitätssicherung wird regelmäßig **Cross‑section** gefahren (Mikroskop), um Lochkupferdicke, Gleichmäßigkeit und Anbindung zu bewerten.

## 4. SMT‑Assembly und Reflow: Design in Realität überführen

Nach dem Bare‑Board geht es in die [PCBA assembly](/pcb-assembly-services/)‑Phase, in der [surface mount technology (SMT)](/surface-mount-technology/) der Standard ist.

### Solder Paste Printing & SPI

Das ist der erste SMT‑Schritt und Quelle von >60% der Lötdefekte.
*   **Stencil:** Öffnungen, Dicke und Geometrie bestimmen das Paste‑Volumen.
*   **3D SPI:** Inline‑Inspektion von Volumen/Fläche/Höhe/Offset, um Paste‑Probleme (zu viel/zu wenig, Bridging, Offset) früh zu stoppen.

### Reflow Soldering

Nach Placement läuft die PCB durch den Reflow‑Ofen.

<div class="div-style-1">
    <h4>Prozessfenster: Lead‑Free Reflow‑Temperaturprofil</h4>
    <ul>
        <li><strong>Parameter:</strong> Preheat, Soak (Activation), Reflow, Cooling – Zeit & Temperatur.</li>
        <li><strong>Ziel:</strong> Passende Aufheizrate für unterschiedliche Wärmekapazitäten, vollständige Benetzung und zuverlässige IMC‑Bildung.</li>
        <li><strong>Typische Werte:</strong> Für SAC305 Peak <strong>240–250°C</strong>, TAL 45–90s.</li>
    </ul>
</div>

Falsche Profile verursachen Cold Solder, Weak Joints, Bauteilschäden oder Tombstoning.

## 5. Cleaning, Conformal Coating und Reliability‑Processing

In High‑Reliability‑Anwendungen (Medical, Automotive, Aerospace) ist die Nachbehandlung entscheidend.

*   **Cleaning:** Flux‑Residues entfernen, sonst Risiko für Electromigration/Corrosion. Sauberkeit wird über **ionic contamination testing** quantifiziert (typisch < **1.56µg/cm² NaCl‑Äquivalent**).
*   **[Conformal Coating](/conformal-coating-services/):** Dünner Polymerfilm gegen Feuchte/Salz/Staub. No‑Coat‑Areas (Connector, Test Points) müssen im Design markiert werden.

## 6. Test Matrix: von Fertigungsdefekten zur Funktionsverifikation

Testing ist die letzte und wichtigste Qualitätsbarriere. Eine einzelne Methode reicht nicht – es braucht eine gestufte Test Matrix.

| Test Type | Test Stage | Objective | Defects Detected | DFT Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **SPI** | nach Solder‑Paste‑Printing | Paste‑Qualität prüfen | zu viel/zu wenig Paste, Bridging, Offset | - |
| **AOI** | nach Reflow/Wave | Bauteile & sichtbare Joints | Missing/Offset, Polarity, Wrong Part, Opens, Shorts | klare Silkscreen‑Markierungen, Platz für Optik |
| **X‑Ray** | nach Reflow | unsichtbare Joints prüfen | BGA/QFN Voids, Shorts, HIP | um BGA keine extrem dichten Bauteile |
| **ICT** | nach PCBA | Netze & Bauteilwerte | Opens/Shorts, R/C/L‑Wertfehler | Test Pads vorsehen, Abstand >1.27mm |
| **FCT** | nach PCBA | Funktion im Use‑Case | Firmware, SI, Power‑Mgmt, Interfaces | gut zugängliche Test‑Interfaces/Burn‑Ports |
| **Reliability Test** | Sample/FAI | Langzeit & Umwelt | latente Design/Prozess‑Defekte | High‑Tg wählen, Hot‑Parts sinnvoll platzieren |

### X‑Ray: die „Fire Eyes“ für BGA/QFN‑Lötstellen

Für BGA/QFN ist X‑Ray die wichtigste zerstörungsfreie Methode. 3D X‑Ray kann Voiding auch quantitativ auswerten.

**X‑Ray Inspection Checklist (Kernpunkte):**
*   [ ] **Shorts:** Unerwartete Verbindungen zwischen Solder Balls?
*   [ ] **Opens/HIP:** Sind Balls vollständig mit Pads verschmolzen?
*   [ ] **Voiding:** Bubble‑Anteil im Ball unter Grenzwert (typ. <25%)?
*   [ ] **Ball Size/Shape:** gleichmäßig nach Reflow?
*   [ ] **Alignment:** Ball‑Array zu Pad‑Array ausgerichtet?

## 7. Qualität & Traceability: datengetriebene Fertigung

Moderne PCB‑Fertigung ist datengetriebene Präzisionsingenieurarbeit.

*   **SPC:** Kritische Prozesse (Etching, Plating, Reflow) werden statistisch überwacht, um Trends früh zu erkennen.
*   **MES:** Jede PCB/PCBA erhält einen eindeutigen Barcode; Prozessparameter, Operator und Inspektionsergebnisse werden pro Station protokolliert – vollständige Traceability.
*   **8D:** Bei Abweichungen werden 8D‑Reports für Root Cause, Corrective/Preventive Actions erstellt und mit Kunden geteilt.

<div class="cta-div">
    <h3>Suchen Sie einen zuverlässigen Partner für PCB‑Fertigung und Test?</h3>
    <p>Das Verständnis der pcb fabrication process steps ist der erste Schritt zum Projekterfolg. HILPCB bietet One‑Stop‑Service von DFM‑Analyse über PCB‑Fertigung bis zur vollständigen PCBA‑Testabdeckung. Unser MES und moderne Inspektionsgeräte sichern höchste Qualität und Traceability. Laden Sie Ihre Gerber‑Daten hoch und erhalten Sie ein Sofortangebot – unsere Experten unterstützen Ihr Projekt end‑to‑end.</p>
    Professionelles DFM‑Review anfordern
</div>

## 8. HILPCB – integrierte Fertigungs‑ und Test‑Capabilities

Die Umsetzung in die Praxis erfordert Equipment und Engineering‑Know‑how.

<div class="div-style-6">
    <h4>HILPCB Core Manufacturing Capability</h4>
    <ul>
        <li><strong>Automatisierte Produktionslinien:</strong> Von LDI Exposure über automatisierte Plating‑Lines bis High‑Speed SMT‑Lines – minimiert manuelle Varianz.</li>
        <li><strong>Präzisions‑Inspektionsmatrix:</strong> 3D SPI, 3D AOI, 3D X‑Ray, Flying Probe und mehrere FCT‑Plattformen bilden eine durchgängige Prüf‑Firewall.</li>
        <li><strong>Smart Warehousing & MES:</strong> Klimatisierte Bauteillager und durchgängiges MES sichern Materialmanagement und vollständige Rückverfolgbarkeit.</li>
        <li><strong>Interne Reliability‑Labs:</strong> Thermal Shock, Temperature Cycling, Vibration, Salt Spray zur Verifikation vor Release.</li>
    </ul>
</div>

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Wer die **pcb fabrication process steps** beherrscht, macht aus „perfektem CAD“ ein robustes Produkt. Wenn Sie DFM und DFT bereits im Design integrieren, verkürzen Sie Entwicklungszyklen, senken Kosten und steigern Yield.

Bei HILPCB sind wir nicht nur Hersteller, sondern Ihr Partner im Fertigungsprozess. Mit transparenter Kommunikation und technischem Support helfen wir, exzellente Designs in hochwertige Realität umzusetzen.

> Benötigen Sie Fertigungs‑ und Montageunterstützung, kontaktieren Sie HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) für DFM/DFT‑Empfehlungen.

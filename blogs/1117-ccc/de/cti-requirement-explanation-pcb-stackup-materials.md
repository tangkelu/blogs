---
title: "cti requirement explanation: Whitepaper zu Material- und Stackup-Strategien"
description: "Rund um cti requirement explanation: Materialauswahl-Entscheidungsbaum, Stackup-Template-Bibliothek, Impedanz-/Thermik-/Mechanik-Modellierung sowie Fertigungsvalidierung, ergänzt durch DFM/DFT/DFR-Checklisten zur Standardisierung des Stackup-Designs."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 9
tags: ["cti requirement explanation", "thermal reliability stackup", "hdi stackup tutorial", "surface finish comparison", "hdmi pcb stackup guide"]
---

## 1. Zusammenfassung: Szenario, Herausforderungen und Nutzen

**Szenario:** In der modernen Elektronikentwicklung – von Hochgeschwindigkeits-Rechenzentren bis zu Leistungs-/BMS-Modulen in Elektrofahrzeugen – ist die Leiterplatte nicht mehr nur Bauteilträger, sondern Fundament für Systemperformance sowie elektrische Sicherheit über den gesamten Lebenszyklus.

**Herausforderung:** Der Kern liegt in der Strategie für Material und Stackup. Falsche Materialentscheidungen verursachen Signaldämpfung, Impedanzfehlanpassung und können unter rauen Bedingungen (z. B. Hochspannung, hohe Feuchte) zu katastrophalen Durchschlägen führen. Dabei gewinnt **CTI (Comparative Tracking Index, relativer Kriechstromfestigkeitsindex)** als zentraler Sicherheitsindikator an Bedeutung, wird aber in frühen Designphasen häufig übersehen. Eine vollständige `cti requirement explanation` ist daher nicht nur Compliance, sondern beeinflusst direkt die Langzeitzuverlässigkeit.

**Nutzen:** Dieses Whitepaper liefert einen systematischen Lösungsweg. Als offizieller Leitfaden des HILPCB Materiallabors stellt es eine vollständige Strategie von der Materialauswahl bis zur Fertigungsvalidierung bereit. Mit standardisierten Entscheidungsbäumen, einer Template‑Bibliothek, Modellierungsmethoden und DFM/DFR‑Checklisten hilft es Ihrem Team:

- **Designrisiko zu senken:** datengetriebene Materialentscheidungen auf Basis klarer CTI‑Anforderungen.
- **Entwicklungszyklen zu beschleunigen:** schneller Projektstart mit vorvalidierten Stackup‑Templates.
- **Zuverlässigkeit zu erhöhen:** `thermal reliability stackup` und elektrische Sicherheit über Modellierung und Verifikation.
- **Kosten zu optimieren:** Performance vs. Kosten balancieren und teure Nacharbeit vermeiden.

---

## 2. Material-Entscheidungsbaum: Systematischer Pfad von Kennwerten zur Auswahl

Die Auswahl des richtigen PCB‑Materials ist der erste und kritischste Schritt im Stackup‑Design. CTI ist der Startpunkt für Sicherheitsüberlegungen, muss aber gemeinsam mit weiteren Leistungskennwerten (Dk, Tg, CTE usw.) entschieden werden.

<div class="div-type-1">

### CTI Requirement Explanation: zentraler Sicherheitskennwert

CTI bewertet die Fähigkeit eines Isoliermaterials, unter elektrischem Feld und elektrolytischer Verschmutzung der Bildung von Leckstrompfaden (Tracking) auf der Oberfläche zu widerstehen. Die Einstufung erfolgt über PLC (Performance Level Category). Je höher der Wert, desto höher die Tracking‑Festigkeit.

- **PLC 0:** CTI ≥ 600V (höchste Klasse; Industrie/Leistung/Automotive‑HV)
- **PLC 1:** 400V ≤ CTI < 600V
- **PLC 2:** 250V ≤ CTI < 400V
- **PLC 3:** 175V ≤ CTI < 250V (Standard‑FR‑4 liegt typischerweise in diesem Bereich)

Für Hochspannungs- oder sicherheitskritische Produkte muss die erforderliche CTI‑Klasse klar definiert und das Material entsprechend gewählt werden.

</div>

### Materialauswahl-Entscheidungsbaum

| Schlüsselmetrik (Key Metric) | Empfohlene Materialien/Klasse | Typische Anwendungen | Design-Limitierungen/Überlegungen |
| :--- | :--- | :--- | :--- |
| **CTI ≥ 600V (PLC 0)** | High‑CTI FR‑4 (z. B. S1170G), Phenolharz, teilweise Polyimid (PI) | Industrie‑Netzteile, Inverter, EV BMS/OBC, Medizintechnik | Höhere Kosten; weniger Materialoptionen – Verfügbarkeit vorab mit HILPCB klären. |
| **Low Dk/Df** | Rogers (RO4350B, Dk≈3.48), Megtron 6 (Dk≈3.6), Isola FR408HR | 5G/6G RF, Server (≥25Gbps), `hdmi pcb stackup guide` | Hohe Prozessanforderungen (z. B. Plasma‑Desmear); deutlich teurer als Standard‑FR‑4. |
| **High Tg > 170°C** | S1000-2M, IT-180A, TU-768 | Automotive, hohe Leistungsdichte, dicke Kupfer‑Mehrlagen | Spröder; Bohrparameter optimieren; Press‑Temperatur typ. 190–210°C. |
| **Low Z-CTE** | Low‑CTE FR‑4, Polyimid | HDI, dichte BGA/LGA, dicke Boards (>3.0mm) | Verbessert PTH‑Zuverlässigkeit, reduziert Via‑Risse in Thermozyklen. |
| **Hohe Wärmeleitfähigkeit** | MCPCB (Al, 1–3 W/m·K), Keramik (AlN, >150 W/m·K) | LED, Power‑MOSFET‑Module, IGBT‑Treiber | Oft 1–2 Lagen, Routing begrenzt; spezielles `thermal reliability stackup` nötig. |
| **Flexibilität/Biegen** | Polyimid (PI) | Wearables, Rigid‑Flex, dynamische Biegeanwendungen | Impedanzkontrolle komplexer; Stiffener‑Design berücksichtigen. |

---

## 3. Stackup-Template-Bibliothek: Ausgangspunkt für standardisiertes Design

Das HILPCB Labor hat auf Basis von tausenden Serienprojekten Standard‑Stackup‑Templates zusammengefasst. Diese wurden per Simulation und Messung validiert und eignen sich als zuverlässige Ausgangsbasis.

### Standard-Mehrlagen-Stackup-Templates

| Lagen | Struktur (Beispiel) | Beschreibung | Schlüsselanwendungen |
| :--- | :--- | :--- | :--- |
| **4 Lagen** | SIG/GND/PWR/SIG | `Core(0.76mm) + PP + Core(0.76mm)` | Consumer, IoT. Kosteneffizient, EMI erfordert Sorgfalt. |
| **6 Lagen** | SIG/GND/SIG/SIG/PWR/SIG | `Core + PP + Core + PP + Core` | Balance aus Kosten und Performance; gute Signal-/Power‑Isolation. |
| **8 Lagen** | SIG/GND/SIG/PWR/GND/SIG/PWR/SIG | `Core + PP + PP + Core + PP + PP + Core` | High‑Speed (PCIe, USB 3.0). Mehrere Referenzebenen, 50Ω/100Ω leichter realisierbar. |
| **10 Lagen** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | `Core + PP...` | Komplexe Systeme, Server‑Mainboards; beste EMI‑Abschirmung und PI. |

### Spezial-Strukturen

<div class="div-type-3">

#### HDI (High-Density Interconnect) Stackup Tutorial

Beispiel **1+N+1 (N=6) HDI** als typische `hdi stackup tutorial` Struktur:

- **L1 (SIG):** Microvia (L1-L2)
- **L2 (GND):**
- **L3 (SIG):** Buried Via (L3-L6)
- **L4 (PWR):**
- **L5 (GND):**
- **L6 (SIG):**
- **L7 (GND):**
- **L8 (SIG):** Microvia (L8-L7)

**Kernprozess:** Sequenzielles Laminieren. Zuerst wird der innere Kern L2-L7 gefertigt, Buried‑Vias werden gebohrt und metallisiert. Anschließend werden auf beiden Seiten L1 und L8 laminiert, danach werden Microvias per Laser gebohrt. Diese Struktur erhöht die Routing‑Dichte erheblich.

</div>

#### Rigid-Flex und MCPCB

- **Rigid‑Flex:** Struktur `Rigid (FR‑4) – Flex (PI) – Rigid (FR‑4)`. Kritisch ist der Übergangsbereich: Spannungen müssen weich übergehen, um Kupferbruch beim Biegen zu verhindern.
- **MCPCB (Aluminium-Substrat):** Struktur `Circuit Layer (Cu) – Insulation (high‑thermal) – Metal Base (Al)`. Kernparameter sind Wärmeleitfähigkeit und Durchschlagsfestigkeit – entscheidend für `thermal reliability stackup`.

---

## 4. Impedanz-/Thermik-/Mechanik-Modellierung

Präzise Modellierung stellt sicher, dass die Design‑Intention in der Fertigung erreicht wird. Das HILPCB Simulationsteam nutzt folgende Modelle für die Voranalyse.

### Impedanzmodellierung (Impedance Modeling)

Für High‑Speed‑Signale (HDMI, DDR) ist Impedanzkontrolle kritisch. Toleranzen liegen typischerweise bei **±10%**, in strengen Fällen bei **±5%**.

- **Microstrip (Außenlage):**
$$ Z_0 \approx \frac{87}{\sqrt{\epsilon_r + 1.41}} \ln\left(\frac{5.98H}{0.8W + T}\right) $$
- **Stripline (Innenlage):**
$$ Z_0 \approx \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{4B}{0.67\pi(0.8W + T)}\right) $$
*Dabei:*
- $Z_0$: Wellenwiderstand (Ω)
- $\epsilon_r$: Dielektrizitätskonstante (Dk)
- $H$: Dielektrikumsdicke
- $W$: Leiterbahnbreite
- $T$: Kupferdicke
- $B$: Abstand der Referenzebenen

**Beispiel:** In einem `hdmi pcb stackup guide` werden für 100Ω Differenzialimpedanz bei FR‑4 (Dk=4.2), Dielektrikum 0.1mm und 1oz Cu (0.035mm) per Simulation etwa 0.12mm Leiterbahnbreite ermittelt.

### Thermische Modellierung (Thermal Modeling)

Kern der thermischen Zuverlässigkeitsanalyse ist die Berechnung der thermischen Widerstandskette.

- **1D stationärer Wärmewiderstand (Rth):**
$$ R_{th} = \frac{L}{k \cdot A} $$
*Dabei:*
- $R_{th}$: Wärmewiderstand (°C/W)
- $L$: Wärmeweg‑Länge (m)
- $k$: Wärmeleitfähigkeit (W/m·K)
- $A$: Querschnittsfläche (m²)

Durch Summation der Widerstände vom Chip‑Junction über die PCB‑Schichten bis zum Kühlkörper lässt sich die Betriebstemperatur prognostizieren – Basis für `thermal reliability stackup`.

### Mechanische Modellierung

Fokus ist die Spannung durch Z‑CTE‑Mismatch. In Temperaturzyklen von −40°C bis 125°C kann bei zu hohem Z‑CTE (>50 ppm/°C) die PTH‑Kupferhülse hohe Zugspannung aufnehmen – es entstehen Mikrorisse oder Brüche. Materialien mit Z‑CTE < 50 ppm/°C sind Schlüssel für High‑Reliability‑Designs.

---

## 5. Hybrid-Lamination / Back-Drilling / Spezialstrukturen

Um Kosten und Performance optimal zu balancieren, unterstützt HILPCB mehrere fortgeschrittene Fertigungsprozesse.

<div class="div-type-6">

### Hybrid Stack

**Rogers + FR‑4 Hybrid:** der häufigste `hybrid stack` Ansatz.

- **Struktur:** Teures Rogers (z. B. RO4350B) nur für RF‑Signale außen; digitale/power Lagen innen mit kostengünstigerem High‑Tg FR‑4.
- **Herausforderung:** Unterschiedliche CTE‑ und Pressparameter erfordern spezielle Laminationsprogramme. Die Haftung FR‑4↔Rogers ist schwächer; nach dem Bohren ist oft Plasma Treatment nötig.
- **Nutzen:** 30–50% Materialkosteneinsparung bei gleichbleibender RF‑Performance.

</div>

### Back-Drilling

- **Ziel:** Entfernen von Via‑Stubs in High‑Speed‑Pfaden, um Reflexion und Dämpfung zu reduzieren – besonders bei Datenraten >10Gbps.
- **Prozess:** Nach Lamination und PTH‑Plating wird von der Gegenseite mit größerem Bohrer die überflüssige Via‑Länge entfernt; hohe Tiefenpräzision erforderlich.
- **Anwendungen:** Server‑Backplanes, High‑Speed‑Switches, optische Module.

### Oberflächenfinish-Vergleich (Surface Finish Comparison)

Das Oberflächenfinish beeinflusst Lötzuverlässigkeit und Signalintegrität.

| Surface Finish | Vorteile | Nachteile | Empfohlene Anwendungen |
| :--- | :--- | :--- | :--- |
| **HASL (Heißluftverzinnen)** | geringe Kosten, gute Lötbarkeit | schlechte Planarität, ungeeignet für Fine‑Pitch | allgemeine Consumer‑Produkte ohne strenge Planaritätsanforderung |
| **ENIG (chemisch Nickel/Gold)** | sehr plan, korrosionsbeständig, gut für BGA | teurer; mögliches „Black‑Pad“-Risiko | High‑Speed‑Boards, BGA/CSP, Kontaktflächen |
| **OSP** | niedrige Kosten, extrem plan, umweltfreundlich | begrenzte Lagerfähigkeit, nach mehrfachem Reflow schlechter | Consumer, schnelle Umläufe, niedrige Kosten |
| **Immersion Silver** | gute Planarität, sehr gute elektrische Eigenschaften | oxidationsanfällig; strenge Lager-/Handling‑Anforderungen | HF‑Signale, Kommunikation |

---

## 6. Verifikationsprozess: von Wareneingang bis zur Endzuverlässigkeit

Eine robuste `stackup strategy` benötigt einen geschlossenen Validierungsprozess.

1. **IQC (Incoming Quality Control):** Abgleich CTI/Dk/Tg‑Datenblatt und Prüfberichte; kritische Materialien stichprobenartig testen.
2. **Laminationsprozess-Monitoring:** Temperatur-/Druckprofile der Presse überwachen und mit Materialspezifikation abgleichen; Standard‑FR‑4‑Press‑Temperatur ca. **180°C**.
3. **Coupon‑Test (Charakteristische Impedanz):** Jede Charge enthält Impedanz‑Coupons; per TDR werden 50Ω/100Ω etc. gemessen und die Abweichung innerhalb **±10%** bestätigt (Kern von `coupon test`).
4. **Warpage‑Analyse:** Optische Methoden (z. B. Shadow Moiré) messen Warpage vor/nach Reflow; Ziel < 0.75%.
5. **Zuverlässigkeitstests:**
    - **Thermal Shock:** z. B. 1000 Zyklen −40°C ↔ 125°C, danach Schliffanalyse von PTH/Microvias.
    - **IST:** Coupon wird schnell aufgeheizt und mit Strom belastet, um thermomechanische Spannungen zu beschleunigen und Via‑Zuverlässigkeit zu bewerten.

---

## 7. DFM/DFR/DFT-Checkliste

Diese Checkliste (≥35 Punkte) hilft, typische Risiken in Fertigung, Zuverlässigkeit und Testbarkeit bereits im Design zu vermeiden.

| Kategorie | Regel/Checkpoint | Empfehlung/Hinweis | Verifikationsmethode |
| :--- | :--- | :--- | :--- |
| **Material & Stackup** | Erfüllt CTI die Sicherheitsanforderung? | PLC 0–3 nach Anwendungsspannung | Design‑Review |
|  | Dk/Df/Tg/CTE klar angegeben? | Materialtypen im Stackup dokumentieren | Design‑Review |
|  | Stackup symmetrisch? | Symmetrie von Cu/Dielektrikum gegen Warpage | CAM‑Analyse |
|  | Core/PP‑Kombination sinnvoll? | Einzelnes dickes PP vermeiden | CAM‑Analyse |
| **Bohren** | Min. mechanischer Bohrdurchmesser | ≥ 0.20mm | DFM |
|  | Min. Laserbohrdurchmesser (HDI) | ≥ 0.10mm | DFM |
|  | Aspect Ratio | < 10:1 (empf.), < 12:1 (Limit) | DFM |
|  | Hole‑to‑Copper (Line/Plane) | ≥ 0.20mm | DRC |
|  | NPTH‑to‑Copper | ≥ 0.25mm | DRC |
| **Routing** | Min. Line/Space | 3.5/3.5mil (inner), 4/4mil (outer) | DFM |
|  | Scharfe Winkel vermeiden | 45° oder Bögen | DRC |
|  | BGA‑Fanout | Dog‑bone oder Via‑in‑Pad bevorzugt | Layout‑Review |
|  | Diff‑Pair Längenausgleich | Längenfehler < 5mil (datenratenabhängig) | CAD/Layout |
| **Kupferflächen** | Via unter BGA/QFN‑Pads? | Via‑in‑Pad empfohlen (Resin Plug) | DFM |
|  | Thermal Relief | Stegbreite ≥ 50% Padbreite | DFM |
|  | Abstand Pad ↔ große Kupferfläche | ≥ 0.25mm | DRC |
|  | Copper Islands entfernen | unverbundene Inseln entfernen | CAM |
|  | Stitching‑Via Dichte | am Rand und bei HS‑Leitungen, Pitch < λ/20 | Layout‑Review |
| **Solder Mask** | Solder‑Mask‑Stegbreite | ≥ 0.10mm (4mil) | DFM |
|  | Maskenöffnung | +0.05mm (2mil) pro Seite gegenüber Pad | DFM |
|  | Tenting/Plugging von Vias | nach Testbedarf, default tent | Design‑Spec |
| **Silkscreen** | Linienstärke | ≥ 0.15mm (6mil) | DFM |
|  | Abstand Silkscreen‑to‑Pad | ≥ 0.15mm (6mil) | DFM |
|  | RefDes/Polarity klar? | Lesbarkeit sicherstellen | Layout‑Review |
| **DFR** | Creepage/Clearance HV‑Bereich | IEC‑62368‑1 etc. | Design‑Review |
|  | Metall nahe Leiterplattenkante | Abstand zur Kante ≥ 0.4mm | DFM |
|  | Gold‑Finger‑Fase | 30° oder 45° | Design‑Spec |
|  | Stamp Holes / V‑Cut | sauber trennbar ohne Bauteilschaden | DFM |
| **DFT** | Testpunkt Größe/Abstand | Ø ≥ 0.8mm, Pitch ≥ 1.27mm | DFM |
|  | Fiducials | ≥3 pro Board, diagonal verteilt | DFM |
|  | ICT‑Punkte unter Bauteilen? | vermeiden | Layout‑Review |
|  | JTAG/SWD herausgeführt? | Debug-freundlich | Design‑Review |
| **Sonstiges** | Board‑Dicken‑Toleranz | ±10% | Design‑Spec |
|  | Impedanz‑Toleranz | ±10% (Standard), ±5% (streng) | Design‑Spec |
|  | End‑Cu‑Dicke | erfüllt Stromtragfähigkeit | Current‑Density‑Simulation |

---

## 8. HILPCB Service-Loop: Partner von Theorie bis Serie

Dieses Whitepaper ist nicht nur Theorie, sondern Praxiswissen aus vielen Projekten. HILPCB bietet einen geschlossenen Service‑Loop:

- **Materiallager & Labor:** breite Materialverfügbarkeit (FR‑4 bis Rogers/Megtron) und schnelle CTI/Dk‑Verifikation.
- **Stackup‑Simulation & Design‑Service:** Impedanz-, Thermik- und SI‑Simulationen zur frühen Optimierung.
- **Advanced Prozessfähigkeit:** `hybrid stack`, präzises Back‑Drilling, HDI und Rigid‑Flex in Serienqualität.
- **Fertigungsdaten‑Feedback:** kontinuierliche Auswertung von Produktions- und `coupon test` Daten zur Verbesserung von DFM‑Regeln und Templates.

<div class="div-type-1">

**Handlungsaufforderung (CTA)**

Ihr nächstes Projekt verdient eine zuverlässigere und optimierte Basis. Kontaktieren Sie das HILPCB Materiallabor und **erhalten Sie ein kostenloses Stackup-Design-Review**. Unsere Experten geben maßgeschneiderte Empfehlungen basierend auf Ihrem `cti requirement explanation` und Ihren Zielkennwerten.

**[Kontaktieren Sie unsere technischen Experten und starten Sie die Projektoptimierung](#contact)**

</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Zusammenfassend liefert dieser Artikel rund um `cti requirement explanation` einen Materialauswahl-Entscheidungsbaum, eine Stackup‑Template‑Bibliothek, Methoden zur Impedanz-/Thermik-/Mechanik‑Modellierung sowie einen Fertigungs‑Validierungsprozess, ergänzt durch DFM/DFT/DFR‑Checklisten. Wenn Sie die Checklisten und Prozessfenster konsequent anwenden und das HILPCB DFM/DFA Team früh einbinden, können Sie Prototyping und Serienanlauf beschleunigen – bei gesicherter Qualität und Compliance.

> Für Herstellungs- und Montageunterstützung kontaktieren Sie HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) für DFM/DFT-Empfehlungen.

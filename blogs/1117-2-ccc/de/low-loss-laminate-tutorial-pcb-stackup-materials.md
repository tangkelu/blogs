---
title: "low loss laminate tutorial: Materialparameter und Stackup-Planung verstehen – die erste Lektion"
description: "low loss laminate tutorial zu Materialparametern, Stackup-Planung, Impedanz-/Thermik-/Kosten-Trade-offs und Fertigungsaspekten – mit Vergleichstabellen und Beispielen, um eine standardisierte Stackup-Library aufzubauen."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["low loss laminate tutorial", "hdI stackup tutorial", "hdmi pcb stackup guide", "surface finish comparison", "cti requirement explanation", "thermal reliability stackup"]
---
Hallo, ich bin Dozent der HILPCB Stackup‑ & Materials‑Academy. In Gesprächen mit Engineering‑Teams sehe ich immer wieder denselben Pain Point: Bei einem High‑Speed‑Design – wie wählt man aus Hunderten PCB‑Materialien das passende low loss laminate aus und plant einen Stackup, der Performance erreicht und gleichzeitig Kosten sowie Manufacturability berücksichtigt?

Viele Teams sind entweder zu konservativ (Megtron 6 für 5Gbps) oder zu aggressiv (Standard‑FR‑4 für 28Gbps) – und landen dann bei Signal‑Integrity‑Problemen (SI). Dieses **low loss laminate tutorial** ist die erste Lektion für dich und dein Team: Wir übersetzen abstrakte Parameter wie Dk/Df, CTI und Fiber Weave Effect in umsetzbare Stackup‑Planungs‑Schritte – ergänzt durch HILPCB Production‑Erfahrung, damit ihr bessere Entscheidungen trefft.

## 1. Startpunkt der Stackup‑Entwicklung: Inputs und erwartete Outputs klären

Ein professioneller Stackup ist kein „Bauchgefühl“, sondern ein systematischer Prozess auf Basis klarer Requirements. Vor dem Start diese Inputs sammeln:

*   **Signal‑Performance‑Requirements:**
    *   Maximale Datenrate? (z. B. 5Gbps, 10Gbps, 28Gbps+)
    *   Impedanz‑Targets? (z. B. 50Ω single‑ended, 90Ω/100Ω differential)
    *   Gesamtes Insertion‑Loss‑Budget (dB)?
*   **Power Integrity (PI) Requirements:**
    *   Strombedarf des Core‑Chips? (bestimmt Copper Thickness der Power‑Planes)
    *   PDN‑Target‑Impedanz? (beeinflusst Power/GND‑Coupling)
*   **Thermal Requirements:**
    *   Leistung/Position der Hauptwärmequellen?
    *   Umgebungstemperatur und Cooling‑Konzept? Das bestimmt, ob ein **thermal reliability stackup** nötig ist.
*   **Safety und Reliability:**
    *   Müssen Standards erfüllt werden? (z. B. UL, CE)
    *   **CTI requirement explanation**: Gibt es klare Anforderungen an Comparative Tracking Index? Z. B. benötigen Industrial-/Power‑Produkte oft CTI ≥ 175V (PLC=2) oder höher.
    *   Ziel‑Lebensdauer und Umgebung? (bestimmt, ob High‑Tg nötig ist)
*   **Mechanik und Kosten:**
    *   Maximale Board‑Dicke?
    *   Ziel‑Kostenrahmen?

**Als Output sollte ein professionelles Stackup‑File mindestens enthalten:**

1.  Layer‑Funktionsdefinitionen (Signal, Ground, Power).
2.  Konkrete Materialtypen pro Layer (Core & Prepreg).
3.  Dielektrik‑Dicken und Kupferdicken (inner/outer).
4.  Gesamt‑Dicke inkl. Toleranz.
5.  Impedanz‑Targets und vorgeschlagene Linewidth/Spacing je Layer.
6.  Special‑Process‑Hinweise (Backdrill, Resin Fill etc.).

## 2. Materialparameter‑Cheatsheet: von FR‑4 bis Low Loss Laminate

Das richtige Material ist „die halbe Miete“. Um schnell ein Gefühl zu bekommen, haben wir häufig genutzte Laminates aus dem HILPCB‑Materialpool nach Loss‑Klassen zusammengefasst. Das ist eine vereinfachte `dk df table`; reale Werte variieren mit Frequenz und Resin Content.

<div class="div-type-1">
    <div class="div-type-1-title">Vergleich: PCB‑Materialperformance</div>
    <div class="div-type-1-content">
        <p>Die Tabelle enthält Schlüsselparameter von Standard‑FR‑4 bis Extremely‑Low‑Loss‑Materialien, um je nach Projektanforderung (Datenrate, Temperatur, Safety) eine erste Auswahl zu treffen.</p>
    </div>
</div>

| Materialklasse | HILPCB‑gängige Optionen | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Typische Anwendungen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard FR‑4** | S1141, KB-6160 | ~4.2 | ~0.020 | 140 | 315 | 175 | Low‑Frequency digital/analog, Consumer |
| **Mid Tg FR‑4** | IT-158, S1155 | ~4.1 | ~0.018 | 150 | 330 | 175 | Multilayer, Lead‑Free Assembly |
| **High Tg FR‑4** | IT-180A, S1000 | ~4.0 | ~0.015 | 180 | 345 | 175 | Server, Automotive, High‑Reliability |
| **Medium Loss** | TU-768, S7439 | ~3.8 | ~0.009 | 190 | 360 | 175 | < 10Gbps High‑Speed, Storage |
| **Low Loss (Low Loss)** | TU-872SLK, S1000-2M | ~3.6 | ~0.005 | 190 | 360 | 175 | 10-25Gbps, Server‑Backplane, **hdmi pcb stackup guide** |
| **Very Low Loss (Very Low Loss)** | I-Speed, M4S | ~3.3 | ~0.003 | 200 | 380 | 175 | 25-56Gbps, HF‑Comms, Test‑Equipment |
| **Ultra Low Loss (Ultra Low Loss)** | Megtron 6, Tachyon 100G | ~3.0 | ~0.002 | 210 | 400 | 175 | > 56Gbps, Core‑Networking, Optical Modules |
| **RF** | Rogers RO4350B | 3.48 | 0.0037 | 280 | 390 | 600 | RF/Microwave, Antennen |

**Interpretation zentraler Parameter:**

*   **Dk (dielectric constant):** Niedrigeres Dk bedeutet oft höhere Ausbreitungsgeschwindigkeit und ermöglicht breitere Traces bei gleichem Impedanz‑Target. Dk‑Konsistenz ist wichtiger als der absolute Wert.
*   **Df (dissipation factor):** Schlüsselparameter für Dämpfung. Für >5Gbps ist Df < 0.01 eine sinnvolle Basisschwelle.
*   **Tg (glass transition temperature):** Übergang von „hart“ zu „gummiartig“. High‑Tg (≥170°C) bedeutet bessere thermische Stabilität, bevorzugt bei Lead‑Free und High‑Reliability.
*   **Td (thermal decomposition temperature):** Temperatur bei 5% Gewichtsverlust – Indikator für Langzeit‑Thermal‑Reliability.
*   **CTI (Comparative Tracking Index):** Widerstand gegen Tracking auf der Oberfläche. Standard‑FR‑4 typischerweise 175V (PLC=2); spezielle Anwendungen brauchen ggf. 600V (PLC=0).

## 3. Core‑Stackup‑Patterns: 4/6/8/10‑Layer‑Templates

Theorie trifft Praxis: Hier sind mehrere production‑validierte Templates. Sie sind gute Startpunkte und können je nach Requirement feinjustiert werden.

| Layer count | Stackup (Funktion) | Core | PP | Board‑Dicke (mm) | Typischer Einsatz |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4‑Layer** | SIG/GND/PWR/SIG | 1.0mm Core | 2x 1080 | 1.2 | IoT, MCU‑Control, Low‑Cost |
| **6‑Layer** | SIG/GND/SIG/PWR/GND/SIG | 0.5mm Core | 3x 2116 | 1.6 | Embedded, DDR3/4‑Boards |
| **8‑Layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | 0.2mm Core | 4x 2116/1080 | 1.6 | PCIe, USB3.x, HDMI, HPC |
| **10‑Layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | 0.15mm Core | 5x 1080/106 | 1.6 | Server‑Mainboards, komplexe **hdI stackup tutorial**‑Cases |

**Design‑Notes:**

*   **4‑Layer:** Kosteneffizient, aber EMI und SI sind schwächer – für High‑Speed meist ungeeignet.
*   **6‑Layer:** Inner‑Signals + solide Reference Planes – sehr gutes Cost/Performance‑Verhältnis.
*   **8‑Layer:** Mehr Reference Planes ermöglichen hervorragende Stripline‑Strukturen – klassisch empfohlen für **hdmi pcb stackup guide**.
*   **10‑Layer+**: Für High‑Density‑Designs mit vielen Power‑Domains. Mehr Ground Planes verbessern Isolation und PI; bei HDI bieten zusätzliche Lagen Platz für microvias.

## 4. Prinzipien für Signal/Power/GND und Copper Thickness

Die „Seele“ eines guten Stackups ist das Zusammenspiel der Lagen.

<div class="div-type-3">
    <div class="div-type-3-title">Golden Rules für Stackup‑Planung</div>
    <ol>
        <li>
            <h6>Reference‑Plane‑Integrität zuerst</h6>
            <p>High‑Speed‑Signal‑Lagen müssen an eine durchgehende Ground‑ oder Power‑Plane angrenzen. Plane‑Splits sind eine Hauptursache für Crosstalk und EMI.</p>
        </li>
        <li>
            <h6>High‑Speed lieber innen routen</h6>
            <p>Stripline (GND‑SIG‑GND) ist meist besser abgeschirmt und impedanzstabiler als Microstrip (SIG‑GND).</p>
        </li>
        <li>
            <h6>Power und Ground eng koppeln</h6>
            <p>Power‑ und Ground‑Planes adjacent platzieren, plane capacitance nutzen und den Return‑Path für HF‑Ströme niederimpedant halten – PI verbessert sich.</p>
        </li>
        <li>
            <h6>Trade‑offs bei Copper Thickness</h6>
            <p>Signal‑Lagen typischerweise 0.5oz (18μm) oder 1oz (35μm). 0.5oz unterstützt feinere line/space. Power‑Lagen für High Current benötigen ggf. 2oz (70μm) oder mehr – häufig mit Anforderungen an einen <strong>thermal reliability stackup</strong>.</p>
        </li>
        <li>
            <h6>Symmetrie gegen Warpage</h6>
            <p>Stackup möglichst top‑bottom symmetrisch halten (Materialien, Copper Thickness, Copper Distribution). Asymmetrie erzeugt Stress in Lamination und Reflow und erhöht Warpage‑Risiko.</p>
        </li>
    </ol>
</div>

## 5. Hybrid Lamination und Spezialmaterialien: wenn Standard nicht reicht

Manchmal reicht ein Materialsystem nicht – etwa wenn RF‑Signale und digitale Steuerung zusammenkommen. Dann ist Hybrid Lamination sinnvoll.

| Option | Vorteile | Nachteile | HILPCB Empfehlung |
| :--- | :--- | :--- | :--- |
| **All Low Loss** | Konsistente Performance, reifer Prozess | Höhere Kosten | Für Kommunikations-/Server‑Produkte mit maximalen SI‑Zielen. |
| **Rogers + FR‑4 Hybrid** | RF‑Performance + niedrigere Digitalkosten | Komplexe Lamination, Reliability‑Risiko, CTE‑Mismatch | Für Antenna‑Integration. HILPCB optimiert Press Cycles für Reliability. |
| **MCPCB (Metal Core)** | Sehr gute Wärmeabfuhr | Meist 1–2 Lagen; komplexes Routing schwierig | High‑Power LED, Power‑Module, thermisch kritische Anwendungen. |
| **Rigid‑Flex** | 3D‑Interconnect; hohe Reliability | Sehr komplex; sehr teuer | Wearables, Aerospace, Space‑constrained High‑Reliability‑Systeme. |

## 6. Manufacturing‑Einfluss: die „letzte Meile“ vom Drawing zur echten PCB

Ein theoretisch perfekter Stackup kann ohne DFM Kosten explodieren lassen oder Yield drücken.

<div class="div-type-6">
    <div class="div-type-6-title">HILPCB Capability gekoppelt an Stackup‑Entscheidungen</div>
    <div class="div-type-6-content">
        <ul>
            <li><strong>Resin Flow und Press Cycle:</strong> Laminations‑Temperatur/Druckprofile werden an die gewählte PP‑Art angepasst. Für high‑resin 106‑PP ist präzise Kontrolle nötig, um HDI‑Laser‑microvias zu füllen und Resin‑Loss zu vermeiden (Dielektrikdicke bleibt stabil).</li>
            <li><strong>Fiber Weave Effect:</strong> Für 25Gbps+ können offene Weaves (z. B. 7628) lokale Dk‑Inhomogenität erzeugen. HILPCB empfiehlt und lagert Flat‑Glass‑Low‑Loss‑Laminates, die Signalqualität deutlich verbessern.</li>
            <li><strong>Back‑drilling:</strong> Via‑Stubs sind „High‑Speed‑Killer“. Für >10Gbps bieten wir präzises Depth‑Controlled‑Backdrill, das Insertion Loss typischerweise um 1–2 dB reduziert.</li>
            <li><strong>Impedance Coupons und TDR:</strong> Jedes Lot enthält Coupons; HILPCB misst per TDR, damit Impedanz im definierten Toleranzfenster liegt (+/- 10% oder strenger).</li>
            <li><strong>Surface finish comparison:</strong> Surface Finish beeinflusst High‑Speed ebenfalls. ENIG ist flach und HF‑geeignet, aber teurer und mit „black pad“‑Risiko. OSP ist günstiger, hat aber begrenzte Solderability‑Shelf‑Life. Wir empfehlen die beste [internal link: PCB surface finish]‑Option je nach Anwendung/Kosten.</li>
        </ul>
    </div>
</div>

## 7. Wie hilft HILPCB bei Stackup‑Design?

Nach diesem **low loss laminate tutorial** wirkt Stackup‑Design vielleicht immer noch komplex – genau deshalb gibt es die HILPCB Stackup‑ & Materials‑Academy. Wir sind nicht nur Hersteller, sondern Engineering‑Partner.

Wir bieten den Service **„Stackup Quick Claim“**, um Materialauswahl und Stackup‑Berechnung für Sie zu vereinfachen.

<div class="cta-container">
    <div class="cta-text">
        <h5>Unsicher, wie du starten sollst? Lass HILPCB Engineers deinen Stackup maßschneidern</h5>
        <p>Teile deine Requirements (Datenrate, Lagenzahl, Impedanz etc.). Unsere Senior Engineers liefern innerhalb von 24 Stunden einen DFM‑validierten, inventory‑optimierten Stackup‑Vorschlag inklusive Impedance‑Calculation‑Report – kostenlos.</p>
    </div>
    Stackup‑Anfrage jetzt senden
</div>

**Warum HILPCB?**

*   **200+ in‑stock materials:** von Standard‑FR‑4 bis Rogers und Megtron – keine Verzögerungen durch MOQ und lange Lead Times.
*   **Erfahrenes Engineering‑Team:** Tausende High‑Speed/High‑Frequency/High‑Density‑Projekte – schnelle Risikoerkennung und Cost/Performance‑Optimierung.
*   **Advanced Impedance Test Lab:** Wir „versprechen“ nicht nur Impedanz – wir verifizieren sie strikt per TDR, damit jede PCB den Specs entspricht.

### Zusammenfassung

Gutes Stackup‑Design ist ein Balanceakt zwischen Performance, Kosten und Manufacturability. Startet mit klaren Inputs, nutzt die Parameter‑Tabellen für die Vorauswahl, setzt auf bewährte Patterns und haltet engen Kontakt zu eurem Hersteller (z. B. HILPCB). So baut ihr eine standardisierte, zuverlässige Stackup‑Library und beschleunigt Produktentwicklung.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Dieses low loss laminate tutorial erklärt Materialparameter, Stackup‑Planung, Impedanz-/Thermik-/Kosten‑Trade‑offs und Manufacturing‑Aspekte – mit Tabellen und Beispielen – damit Teams eine standardisierte Stackup‑Library aufbauen und Risiken über Design, Materialien und Tests systematisch kontrollieren. Wer Checklisten und Prozessfenster konsequent umsetzt und HILPCBs DFM/DFA‑Team früh einbindet, beschleunigt Prototyping und Serienlieferung bei gesicherter Qualität und Compliance.

> Für Fertigungs‑ und Assembly‑Support: HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) kontaktieren (DFM/DFT‑Empfehlungen).


---
title: "HDI stackup tutorial: Die erste Lektion zum Verständnis von Materialparametern und Stackup-Design"
description: "Mit HDI stackup tutorial als Hauptlinie werden Materialparameter, Stackup-Planung, Impedanz-/Wärme-/Kostenabwägungen und Fertigungsaspekte mit Vergleichstabellen und Fallstudien erläutert, um Teams beim Aufbau einer Standard-Stackup-Bibliothek zu helfen."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["HDI stackup tutorial", "HDMI PCB stackup guide", "thermal reliability stackup"]
---

Hallo, ich bin ein Dozent der HILPCB Stackup- und Materialwissenschaftsakademie. In meiner täglichen Arbeit stelle ich fest, dass viele Ingenieure verwirrt sind, wenn sie mit kalten Parametern wie Dk/Df, CTI und Tg konfrontiert werden, und unsicher sind, wie sie diese in ein zuverlässiges, massenproduzierbares PCB-Stackup umwandeln. Ein schlechtes Stackup-Design kann leichte Signalintegritätsprobleme verursachen oder schwerwiegende Zuverlässigkeitsprobleme in der Massenproduktion auslösen.

Heute wird dieser **HDI stackup tutorial** Ihre erste Lektion sein und Sie von Grund auf systematisch beim Aufbau von Stackup-Designdenkweisen führen. Wir werden zusammen abstrakte Materialwissenschaft in konkrete Engineeringentscheidungen umwandeln, sodass Sie nicht nur Stackups entwerfen können, die Leistungsanforderungen erfüllen, sondern auch Fallstricke in der Fertigung vorhersehen und vermeiden können. Egal ob Sie einen hochfrequenten `HDMI PCB stackup guide` entwerfen oder an einem Projekt mit extremen `thermal reliability stackup`-Anforderungen arbeiten – das Wissen hier wird Ihre solide Grundlage sein.

## Der Ausgangspunkt des Stackup-Designs: Klären Sie Ihre "Randbedingungen"

Bevor Sie das erste Leiterbahn in Ihrem EDA-Tool zeichnen, beginnt ein professionelles Stackup-Design mit einer umfassenden Überprüfung der Projektanforderungen. Das ist wie ein Architekt, der vor dem Entwerfen von Blaupausen die Gebäudenutzung, das Budget und die geologischen Bedingungen verstehen muss. Die Eingabebedingungen für das Stackup-Design umfassen hauptsächlich folgende Aspekte:

- **Signalintegritäts- (SI) Anforderungen**:
  - **Maximale Geschwindigkeit**: Wie hoch ist die höchste Signalgeschwindigkeit in Ihrem Design? Ist es PCIe 3.0 mit 10 Gbps oder 28 Gbps SerDes? Die Geschwindigkeit bestimmt Ihre Toleranz für Materialverluste (Df).
  - **Impedanzsteuerung**: Welche Impedanzen müssen gesteuert werden? Ist es 50Ω Single-Ended oder 90/100Ω Differential? Präzise Impedanz ist die Voraussetzung für stabile Hochgeschwindigkeitssignalübertragung.

- **Stromversorgungsintegritäts- (PI) Anforderungen**:
  - **Kernstrom**: Wie groß ist der transiente Strom von Kerngeräten wie CPUs und FPGAs? Dies bestimmt die Kupferdicke und das Layout der Stromversorgungsebene sowie ob niedrige Induktivitätspfade erforderlich sind.
  - **Ebenenkapazität**: Ist es notwendig, benachbarte Stromversorgungs-/Massebenen zu nutzen, um Ebenenkapazität für hochfrequente Entkopplung zu erzeugen?

- **Wärmeverwaltungs- und Zuverlässigkeitsanforderungen**:
  - **Leistung und Umgebung**: Wie hoch ist die Gesamtleistung der Leiterplatte, wo befinden sich kritische Wärmequellen und welche Umgebungstemperatur wird das Endprodukt haben? Dies bezieht sich direkt auf die Auswahl der Glasübergangstemperatur (Tg) und Zersetzungstemperatur (Td) des Materials.
  - **Sicherheitsanforderungen**: Hat das Produkt Hochspannungsteile? Gibt es klare Anforderungen an CTI (Comparative Tracking Index) (z.B. >400V)? Dies ist in Industrie- und Stromanwendungen entscheidend.

- **Kosten und Lieferkette**:
  - **Zielkosten**: Wie hoch ist das Budget pro Platine? Dies beeinflusst direkt, ob Sie innerhalb des Standard-FR-4-Bereichs optimieren oder hochleistungsfähige Materialien wie Rogers in Betracht ziehen können.
  - **Produktionsmenge und Zyklus**: Die geschätzte Jahresproduktion und Lieferfrist des Projekts bestimmen, ob die gewählten Materialien leicht verfügbar sind und ob es Mindestbestellmengen (MOQ) gibt.

Diese Eingabebedingungen führen letztendlich zu einem klaren, an den PCB-Hersteller lieferbaren Stackup-Strukturdiagramm mit allen kritischen Informationen für jede Schicht wie Typ, Material, Dicke, Kupferdicke und Impedanzanforderungen.

## "Materialsprache" verstehen: Schnellreferenztabelle für Schlüsselparameter

Die Auswahl geeigneter Materialien ist das Herzstück des Stackup-Designs. Angesichts von Hunderten von Plattentypen müssen wir lernen, Schlüsselparameter zu erfassen. Die folgende Tabelle fasst die Kernmetriken mehrerer repräsentativer Materialien aus der HILPCB-Materialbibliothek zusammen.

<div class="div-style-1">
    <h4>Materialparameterabwägung: Es gibt kein perfektes Material, nur die richtige Wahl</h4>
    <p>Bei der Materialauswahl sind Leistung und Kosten immer ein Widerspruch. Beispielsweise bedeutet die Verfolgung eines extrem niedrigen Df (Dielektrizitätsverlust) normalerweise höhere Materialkosten. Ebenso bieten High-Tg-Materialien bessere Wärmestabilität, aber ihre Verarbeitungsfenster (Press Cycle) sind auch strenger. Der Wert eines Ingenieurs liegt darin, basierend auf Projektanforderungen den optimalen Gleichgewichtspunkt zwischen diesen Parametern zu finden. Beispielsweise kann für ein kostenempfindliches Verbraucherelektronikprodukt die Verwendung von S1141 oder IT-180A ausreichend sein; für eine Kernplatine einer Kommunikationsbasisstation kann jedoch S1000-2M oder sogar höherwertige Materialien erforderlich sein.</p>
</div>

| Materialmodell | Hersteller | Kategorie | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Kernapplikationen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S1141** | Shengyi | Standard FR-4 | 4.2 | 0.020 | 140 | 315 | >175 | Verbraucherelektronik, Low-Frequency-Steuerplatinen |
| **IT-180A** | ITEQ | High-Tg FR-4 | 3.9 | 0.012 | 175 | 345 | >400 | Server, Industriesteuerung, Automobil |
| **S1000-2M** | Shengyi | Mid-Loss | 3.6 | 0.009 | 190 | 360 | >400 | Hochgeschwindigkeitscomputing, Rechenzentren |
| **EM-827** | EMC | Low-Loss | 3.4 | 0.006 | 200 | 370 | >600 | 25Gbps+ SerDes, Netzwerkgeräte |
| **RO4350B** | Rogers | RF/Mikrowelle | 3.48 | 0.0037 | 280 | 390 | >400 | RF-Module, Antennen, 5G |

**Parameterinterpretation:**

- **Dk (Dielektrizitätskonstante)**: Beeinflusst Signalausbreitungsgeschwindigkeit und Impedanz. Je niedriger und stabiler Dk, desto besser für Hochgeschwindigkeitssignale. Eine Dk-Änderung von 3,66 zu 3,2 kann die Leiterbahnbreite für 100Ω Differenzimpedanz um über 10% beeinflussen.
- **Df (Dielektrizitätsverlustfaktor)**: Der Grad, in dem Signalenergie im Medium in Wärme umgewandelt wird. Für Langstrecken-, Hochfrequenzsignale ist niedriger Df entscheidend.
- **Tg (Glasübergangstemperatur)**: Die Temperatur, bei der Material von starrem Glaszustand zu flexiblem Gummizustand übergeht. Hoher Tg (normalerweise >170°C) bedeutet bessere Hochtemperatur-Dimensionsstabilität und Zuverlässigkeit, besonders nach mehrfachem Reflow-Löten.
- **Td (Zersetzungstemperatur)**: Die Temperatur, bei der Material durch Hochtemperaturzersetzung 5% Gewichtsverlust erleidet. Td ist ein Schlüsselindikator für die langfristige Wärmefestigkeit des Materials.
- **CTI (Comparative Tracking Index)**: Die Fähigkeit der Materialoberfläche, Oberflächenleckverschmutzung zu widerstehen. Hoher CTI (wie 600V) ist für Hochspannungs- und strenge Sicherheitsanforderungen notwendig.

## Von 4 bis 10+ Schichten: Klassische Stackup-Strukturparadigmen

Nachdem wir Materialien beherrschen, schauen wir uns an, wie wir sie "zusammenbauen". Das Stackup-Strukturdesign ist keine willkürliche Kombination, sondern folgt grundlegenden Prinzipien der elektromagnetischen Verträglichkeit (EMC) und Signalintegrität.

<div class="div-style-3">
    <h4>Drei-Schritte-Stackup-Planungsmethode</h4>
    <ol>
        <li><strong>Schichtzahl und Funktion bestimmen</strong>: Basierend auf Verdrahtungsdichte, Stromversorgungsteilungsanforderungen und Kostenbudget die Gesamtschichtzahl vorläufig bestimmen. Jeder Schicht eine anfängliche Funktion zuweisen (Signal, Masse, Stromversorgung).</li>
        <li><strong>Referenzebenen konstruieren</strong>: Priorität auf vollständige, kontinuierliche GND-Ebenen legen. Sie sind Rückführungspfade für Hochgeschwindigkeitssignale und natürliche Abschirmungsschichten. Kritische Signalschichten direkt neben GND-Ebenen platzieren.</li>
        <li><strong>Optimieren und Symmetrie</strong>: Dielektrikumdicke und Kupferdicke anpassen, um Impedanzanforderungen zu erfüllen. Stackup-Struktur oben und unten symmetrisch halten, um Verformung durch ungleichmäßige Wärmespannung während der Produktion zu vermeiden.</li>
    </ol>
</div>

Nachfolgend sind mehrere klassische Stackup-Paradigmen und ihre Anwendungsszenarien aufgeführt, die auch häufig verwendete Vorlagen sind, wenn HILPCB-Ingenieure Stackup-Lösungen für Kunden bereitstellen.

| Schichtzahl | Klassische Struktur (von oben nach unten) | Typische Applikationen | Vorteile | Nachteile |
| :--- | :--- | :--- | :--- | :--- |
| **4 Schichten** | SIG/GND/PWR/SIG | IoT-Module, einfache Controller | Extrem niedrige Kosten, einfache Struktur | Schlechte EMC-Leistung, instabile Impedanzsteuerung |
| **6 Schichten** | SIG/GND/SIG/SIG/PWR/SIG | Verbraucherelektronik, Industriehauptplatinen | Führt vollständige Massebene ein, verbesserte EMC | Schlechte Referenzebene für innere Signalschichten |
| **6 Schichten (empfohlen)** | SIG/GND/PWR/GND/SIG/SIG | HDMI/USB3.0-Applikationen | Ausgezeichnete EMC- und SI-Leistung, angemessene Kosten | Opfert eine Verdrahtungsschicht |
| **8 Schichten** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | Server, Hochleistungscomputing | Mehrschichtige Abschirmung, präzise Impedanzsteuerung, geeignet für hochfrequente Differenzleitungen | Höhere Kosten, etwas längere Fertigungszyklen |
| **10 Schichten** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | Kern-Netzwerkgeräte, komplexe FPGA-Platinen | Ausgezeichnete Stromversorgungs-/Massetrennung, ausreichender Verdrahtungsplatz | Hohe Kosten, hohe Anforderungen an Fertigungsgenauigkeit |

## Schicht-zu-Schicht "Symphonie": Goldene Regeln für Signal, Stromversorgung, Masse und Kupferdicke

Ein ausgezeichnetes Stackup ist wie eine Symphonie, bei der interne Elemente harmonisch und ordnungsgemäß kombiniert werden.

### Signalschichten: Mikrostreifenleitungen vs. Streifenleitungen

- **Mikrostreifenleitungen (Microstrip)**: Leiterbahnen auf der Oberflächenschicht, eine Seite ist Luft, die andere ist Dielektrikum und Referenzebene. Vorteile sind einfache Verarbeitung und einfaches Debugging; Nachteile sind Anfälligkeit für externe Störungen und starke Strahlung.
- **Streifenleitungen (Stripline)**: Leiterbahnen in inneren Schichten, eingebettet zwischen zwei Referenzebenen. Vorteile sind ausgezeichnete EMC-Leistung und stabile Impedanz; Nachteile sind etwas niedrigere Verdrahtungsdichte und schwierige Änderungen.
- **HILPCB-Empfehlung**: Für kritische Signale mit Geschwindigkeiten über 5 Gbps Streifenleitungsstrukturen bevorzugen und die Vollständigkeit ihrer Referenzebenen sicherstellen.

### Referenzebenen: Die "Herrschaft" von GND

Eine solide, kontinuierliche GND-Ebene ist der Grundstein des Hochgeschwindigkeitsdesigns. Sie bietet den kürzesten Rückführungspfad für Signale und unterdrückt wirksam Übersprechen und Strahlung. Vermeiden Sie, Massebenen unter Hochgeschwindigkeitssignalpfaden zu teilen. Falls notwendig, verwenden Sie Überbrückungskondensatoren, um die Kontinuität des Rückführungspfads sicherzustellen.

### Kupferdicke: Abwägung zwischen 1 oz und 2 oz

Die Wahl der Kupferdicke beeinflusst direkt die Stromtragfähigkeit und die Impedanz-Leiterbahnbreite.

- **Stromtragfähigkeit**: Die Stromtragfähigkeit von 2 oz (70µm) Kupfer ist etwa 1,5-1,8 mal höher als die von 1 oz (35µm) Kupfer. Für Stromversorgungsschichten mit großem Strom ist die Verwendung von dickem Kupfer notwendig.
- **Impedanzauswirkung**: Bei gleicher Dielektrikumdicke und Impedanzziel benötigt dickes Kupfer breitere Leiterbahnen. Beispielsweise kann die Realisierung von 50Ω Impedanz auf 4mil Kernmaterial mit 1 oz Kupfer 7,2mil Leiterbahnbreite erfordern, während 2 oz Kupfer 9,5mil benötigt, was wertvollen Verdrahtungsplatz belegt.
- **Fertigungsüberlegungen**: Dickes Kupfer ist schwieriger zu ätzen und beeinflusst die Ausbeute feiner Leiterbahnen. Beim Entwerfen von [hochdichten Interconnect (HDI) Platinen](/technology/what-is-hdi-pcb/) werden innere Schichten normalerweise mit 0,5 oz oder 1 oz Kupfer verwendet.

## Jenseits von FR-4: Anwendungen von Hybrid-Stackup, Metallsubstraten und flexiblen Materialien

Wenn Standard-FR-4 extreme Leistungsanforderungen nicht erfüllen kann, müssen wir spezielle Materialien und Prozesse einführen.

### Hybrid-Stackup

Hybrid-Stackup bedeutet die Verwendung von zwei oder mehr verschiedenen Materialtypen in einer PCB, häufig in RF-Designs. Beispielsweise wird Rogers RO4350B für den RF-Teil verwendet, während der digitale Steuerungsteil kostengünstiger IT-180A verwendet.

| Hybrid-Stackup-Lösung | Vorteile | Herausforderungen und Überlegungen |
| :--- | :--- | :--- |
| **Rogers + FR-4** | Hochleistung in kritischen Bereichen, insgesamt kontrollierbare Kosten | CTE (Wärmeausdehnungskoeffizient) Nichtübereinstimmung kann zu Delaminierung oder Zuverlässigkeitsproblemen führen; komplexe Pressparameter (Press Cycle), erfordert erfahrene Fabriken. |
| **Hochgeschwindigkeitsmaterial + Standardmaterial** | Erfüllt Anforderungen an niedrige Verluste für Hochgeschwindigkeitskanäle, reduziert Gesamtkosten | Unterschiede in der Harzfließfähigkeit (Resin Flow) zwischen Materialien können die Gleichmäßigkeit der Dielektrikumdicke beeinflussen. |

HILPCB hat umfangreiche Hybrid-Stackup-Produktionserfahrung und kann durch präzise Presszyklussteuerung und Materialcharakterisierungsanalyse die Zuverlässigkeit von Hybrid-Stackup-Platinen gewährleisten.

### Metallsubstrate (MCPCB) und flexible Platinen

- **MCPCB**: Verwendet normalerweise Aluminium- oder Kupferbasis, deren Kernvorteil ausgezeichnete Wärmeleistung ist. Dies ist entscheidend für Anwendungen wie High-Power-LEDs und Stromversorgungsmodule, die hohe `thermal reliability stackup`-Anforderungen haben.
- **Flexible/Rigid-Flex-Platinen**: Ermöglichen dreidimensionale Verbindungen und dynamische Biegungen. Ihr Stackup-Design ist komplexer und muss Biegespannungen, Klebstoffauswahl und Deckschichtdicke berücksichtigen.

## Von Design zu Massenproduktion: Nicht zu übersehende Fertigungsprozessauswirkungen

Ihr Stackup-Designblatt ist nur ein "theoretisches Modell"; die endgültige physische Entität wird tiefgreifend von Fertigungsprozessen beeinflusst.

<div class="div-style-6">
    <h4>HILPCB Fertigungssteuerungsfähigkeiten</h4>
    <p>Bei HILPCB empfangen wir nicht nur Ihre Designdateien. Unsere CAM-Ingenieure führen basierend auf unserer großen Materialdatenbank und ausgereiften Pressmodellen eine Produktionsdurchführbarkeitanalyse Ihres Stackups durch. Durch Simulation von Harzfluss und Dickenvariationen während des Pressvorgangs können wir vorhersagen und kompensieren, um sicherzustellen, dass die endgültige Impedanzgenauigkeit des Produkts auf ±5% kontrolliert wird, weit besser als der Industriestandard von ±10%.</p>
</div>

- **Harzfluss (Resin Flow)**: Während des Pressvorgangs schmilzt das Harz in Halbfertigharz (PP) unter Hitze und füllt die Lücken in der Kupferfoliengrafik. Dieser Fluss führt dazu, dass die endgültige Dielektrikumdicke kleiner ist als die ursprüngliche PP-Dicke. Erfahrene Fabriken kompensieren basierend auf der Kupferfolienbelegung präzise.
- **Presszyklus (Press Cycle)**: Verschiedene Materialien erfordern verschiedene Presstemperatur-, Druck- und Zeitkurven. Beispielsweise liegt die Presstemperatur für Standard-Tg-Materialien normalerweise um 185°C, während High-Tg-Materialien über 200°C erfordern. Unsachgemäße Pressung führt zu Delaminierung, Plattenverformung und anderen Problemen.
- **Verformung (Warpage)**: Asymmetrische Stackup-Struktur und ungleichmäßige Kupferfolienbelegung sind Hauptursachen für Verformung. Das Design sollte Stackup-Struktur symmetrisch halten und Netzwerk-Kupfer in großen verdrahtungsfreien Bereichen hinzufügen.
- **Back-Drilling**: Für Signale über 10 Gbps wirken ungenutzte Teile in Vias (Stubs) wie Antennen und erzeugen Resonanzen, die Signalqualität ernsthaft beeinflussen. Back-Drilling kann diese überschüssigen Stubs präzise entfernen und ist eine Schlüsseltechnologie zur Gewährleistung der Hochgeschwindigkeitssignalintegrität.
- **Impedanz Coupon**: Es ist ein "Teststreifen" auf demselben Produktions-Panel wie die Hauptplatine, der verwendet wird, um die tatsächliche Leiterbahnimpedanz durch Time Domain Reflectometry (TDR) zu messen. Jede Impedanzplatine von HILPCB wird mit einem detaillierten Coupon-Testbericht geliefert.

## HILPCB Stackup- und Materialwissenschaftsakademie: Ihr Engineering-Partner

Der ultimative Zweck des theoretischen Lernens ist die Lösung praktischer Probleme. HILPCB ist nicht nur Ihr PCB-Hersteller, sondern auch Ihr technischer Kooperationspartner. Wir verstehen die Wichtigkeit und Komplexität des Stackup-Designs und bieten daher eine Reihe von Diensten zur Vereinfachung dieses Prozesses:

- **200+ Materialbibliothek**: Wir lagern über 200 Arten von Platinen von weltweit führenden Lieferanten, von Standard-FR-4 bis zu speziellen Materialien wie Hochgeschwindigkeit, RF und Metallbasis, alle mit detaillierten Leistungscharakterisierungsdaten für die umfassendste Auswahl.
- **Impedanz-Testlabor**: Unser eigenes Testlabor ist mit fortschrittlicher TDR-Testausrüstung ausgestattet und stellt sicher, dass jede Impedanzplatinen-Charge streng verifiziert wird, um zuverlässige Datenstützung zu bieten.

## Erhalten Sie sofort Ihren maßgeschneiderten Stackup-Plan

Anstatt in einer Flut von Materialdatenblättern zu kämpfen, lassen Sie sich von professionellen Ingenieuren leiten. HILPCB bietet den "Stackup Quick Claim"-Service, um Ihnen in der frühen Projektphase einen verifizierten, massenproduzierbaren Stackup-Plan zu bieten.

<div class="cta-box">
    <h3>Haben Sie immer noch Probleme mit dem Stackup-Design?</h3>
    <p>Laden Sie Ihre Projektanforderungen hoch (wie Schichtzahl, Geschwindigkeit, Impedanzanforderungen, spezielle Materialien usw.), und HILPCB-Stackup-Ingenieure mit umfangreicher Erfahrung werden Ihnen innerhalb von 24 Stunden kostenlos ein detailliertes, professionelles Stackup-Empfehlungsschreiben mit Materialauswahl, Dickenbergechnung und Impedanzsimulationsergebnissen bereitstellen. Lassen Sie Ihr Design von Anfang an auf solider Grundlage aufbauen!</p>
    Kostenlosen Stackup-Plan jetzt erhalten
</div>

## Zusammenfassung: Ein erfolgreiches Stackup ist ein Konsens zwischen Design und Fertigung

Ich hoffe, dieser **HDI stackup tutorial** öffnet Ihnen eine neue Tür. Denken Sie daran, dass ein erfolgreiches Stackup-Design niemals eine einseitige "Heimarbeit" des Ingenieurs ist, sondern eine tiefe Integration von Designabsicht und Fertigungsfähigkeit. Es beginnt mit klarer Anforderungsdefinition, durchzieht sich durch tiefes Verständnis von Materialparametern und endet schließlich mit Respekt vor Fertigungsprozessen.

Wenn Sie das nächste Mal ein neues Projekt starten, hoffe ich, dass Sie über einfaches Schicht-Stacking hinausgehen und von mehreren Dimensionen wie SI, PI, Wärmezuverlässigkeit und Kosten denken und aktiv mit erfahrenen Herstellern wie HILPCB kommunizieren. Denn ein ausgezeichnetes Stackup ist der Ausgangspunkt Ihres ausgezeichneten Produkts.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit

Zusammenfassend erläutert dieser Artikel mit HDI stackup tutorial als Hauptlinie Materialparameter, Stackup-Planung, Impedanz-/Wärme-/Kostenabwägungen und Fertigungsaspekte mit Vergleichstabellen und Fallstudien, um Teams beim Aufbau einer Standard-Stackup-Bibliothek zu helfen und Teams dabei zu unterstützen, Risiken in Design-, Material- und Testphasen systematisch zu kontrollieren. Solange Sie den Checklisten und Prozessfenstern in diesem Artikel folgen und das DFM/DFA-Team von HILPCB frühzeitig einbeziehen, können Sie Prototyp- und Massenproduktionslieferungen unter Gewährleistung von Qualität und Compliance beschleunigen.

> Für Fertigungs- und Montageunterstützung kontaktieren Sie bitte HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) für DFM/DFT-Empfehlungen.

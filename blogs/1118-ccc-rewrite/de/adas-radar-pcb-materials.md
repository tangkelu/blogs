---
title: "Wie man ADAS-Radar-PCB-Material auswählt: 77/79GHz-Performance, Hybrid-Stackups und Automotive-Zuverlässigkeit"
description: "Eine direkte Antwort auf die Punkte zu Low-Loss-Verhalten, Kupferrauheit, Hybrid-Laminations-Kompatibilität, Oberflächenfinish und Validierung, die bei ADAS-Radar-PCB-Materialien zuerst geprüft werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["ADAS radar PCB", "Automotive PCB", "High-frequency PCB", "PCB materials", "77GHz radar PCB", "mmWave PCB"]
---

# Wie man ADAS-Radar-PCB-Material auswählt: 77/79GHz-Performance, Hybrid-Stackups und Automotive-Zuverlässigkeit

- **Zuerst auf Materialstabilität schauen, nicht nur auf einen niedrigen nominellen Verlustwert.** Bei 77/79GHz-Radarboards entscheiden Dk-Toleranz, TCDk, Feuchteverhalten und Lot-Konsistenz oft stärker über Phasen- und Impedanzstabilität als ein einzelner Df-Wert.
- **Kupferrauheit verstärkt Millimeterwellenverlust und Phasenabweichung direkt.**
- **Der übliche richtige Weg für ADAS-Radar ist nicht "überall PTFE", sondern ein Hybrid aus HF-Material und FR-4.**
- **Material, Kupferfolie und Finish müssen zusammen bewertet werden.**
- **Ein erfolgreiches Muster ist noch keine serientaugliche Materialstrategie.**

> **Quick Answer**  
> Der Kern der Materialauswahl für ADAS-Radar-PCBs ist nicht einfach das "verlustärmste Laminat" zu finden. Entscheidend ist, Dk/Df-Stabilität bei 76-81GHz, Kupferrauheit, Hybrid-Stackup-Kompatibilität, Finish-Einfluss und Automotive-Validierung gemeinsam zu schließen. Robust ist die Lösung erst dann, wenn elektrische Performance, Fertigungsfenster und Zuverlässigkeit gleichzeitig stimmen.

## Inhaltsverzeichnis

- [Was sollte man bei ADAS-Radar-PCB-Material zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum ist Low-Loss nicht der einzige Maßstab?](#low-loss)
- [Warum verstärken Kupferrauheit, Finish und dünne Dielektrika den Verlust gemeinsam?](#copper-finish)
- [Wie erkennt man, ob ein Hybrid-Stackup serienreif ist?](#hybrid-stackup)
- [Wie sollte die Materialstrategie vor der Serie validiert werden?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei ADAS-Radar-PCB-Material zuerst prüfen?

Zuerst **Arbeitsband, Dk/Df-Stabilität, Kupferrauheit, Hybrid-Kompatibilität und Validierungsmethode**.

Die Frage bedeutet weder "welches HF-Material ist das beste" noch "77GHz heißt immer PTFE". Öffentliche Rogers-Unterlagen zeigen, dass Automotive-Radar längst bei 77GHz, 79GHz und 76-81GHz angekommen ist. Auf diesem Niveau zählen nicht nur niedrige Verluste, sondern auch Phasenkonsistenz, Materialgleichmäßigkeit und wiederholbare Fertigung.

Früh zu trennen sind meist:

1. **Welche Lagen echte RF- oder Antennenlagen sind und welche digital, Steuerung oder Leistung tragen**
2. **Ob minimale Verluste, minimale Phasenabweichung oder ein ausgewogeneres Kosten-Prozess-Fenster wichtiger sind**
3. **Ob ein RF-plus-FR-4-Hybrid-Stackup nötig ist**
4. **Ob Kupferrauheit, Finish und Mikrovia-Prozess den Millimeterwellengewinn wieder aufzehren**
5. **Ob der Lieferant Lot-Rückverfolgbarkeit, Hybrid-Review und repräsentative Validierungsdaten liefern kann**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Methode | Warum wichtig | Wie prüfen | Wenn ignoriert |
|---|---|---|---|---|
| Arbeitsband | Klären, ob 24GHz, 77GHz, 79GHz oder 76-81GHz | Mit steigender Frequenz wachsen Verlust- und Phasenempfindlichkeit | Anforderung, RF-Budget, Antennenmodell | Falsches Materialfenster wird gewählt |
| Dk-Stabilität | Nicht nur typischen Dk, sondern auch Toleranz und Drift prüfen | Bestimmt Impedanz, Phase und Array-Gleichlauf | Datenblatt, TCDk, Lot-Review | Kanal-zu-Kanal-Streuung steigt |
| Df / Einfügedämpfung | Immer zusammen mit Dicke, Kupfertyp und Liniengeometrie bewerten | Derselbe Df verhält sich je nach Struktur anders | S-Parameter, Coupon | Nominal low-loss, real aber zu hoher Verlust |
| Kupferrauheit | RF-Lagen bevorzugt mit rolled copper oder VLP / LoPro prüfen | Leiterverlust und Phasenfehler wachsen bei mmWave | Materialspezifikation, Kupferfolienspezifikation | Höherer Verlust und größere Lot-Streuung |
| Hybrid-Kompatibilität | Prüfen, ob RF-Cap-Layer plus FR-4-Multilayer unterstützt wird | Die meisten Radarboards nutzen nicht ein Material für alles | Stackup-Review, Laminations- und Bohrreview | Verzug, Registrierung, Lochwand- oder Zuverlässigkeitsprobleme |
| Oberfläche | Finish in RF-Zonen nicht als späte CAM-Entscheidung behandeln | Nickel und Finish-Schwankung beeinflussen Verlust und Phase | Finish-Review, Coupon-Vergleich | Zusätzlicher Kanalverlust |
| Automotive-Zuverlässigkeit | Feuchte, Temperaturwechsel und Lead-free-Kompatibilität bewerten | Fahrzeugumgebung und Montagebelastung sind härter | IPC-Methoden, Temperatur- und Feuchttest | Labormuster läuft, Serie driftet |

<a id="low-loss"></a>
## Warum ist Low-Loss nicht der einzige Maßstab?

Fazit: **Bei ADAS-Radarboards kommt meist zuerst stabile und vorhersagbare Performance, dann der niedrigste nominelle Verlust.**

Rogers zeigt öffentlich, dass 77GHz- und 79GHz-Automotive-Radar nicht nur HF-Verluste, sondern auch Temperaturänderung und Umwelteinfluss beherrschen muss. RO3003 wird unter anderem mit Dk 3,00 ±0,04, niedrigem Df, gutem TCDk und geringer Feuchteaufnahme beschrieben. Die Aussage dahinter lautet nicht nur "verlustarm", sondern vor allem "stabil unter realen Betriebsbedingungen".

Ein anderes öffentliches Beispiel ist Isola Astra MT77. Auch dort steht nicht "immer besser", sondern ein Kompromiss zwischen HF-Leistung, Kosten und Prozesskompatibilität. Die richtige Entscheidung hängt also von Antennenlänge, Feed-Loss-Budget, Lagenzahl, Digitalanteil und Fertigungsroute ab.

<a id="copper-finish"></a>
## Warum verstärken Kupferrauheit, Finish und dünne Dielektrika den Verlust gemeinsam?

Fazit: **Bei Millimeterwellen sind Kupferfolie und Oberfläche keine Nebenthemen der Nachbearbeitung, sondern Teil der Materialstrategie selbst.**

Rogers erklärt öffentlich, dass raue Kupferoberflächen Leiterverlust erhöhen und die Welle so verhalten lassen, als läge ein höheres effektives Dk vor. Besonders sichtbar wird das bei dünnen Dielektrika. Gleichzeitig zeigen Rogers-Unterlagen Beispiele für Standard-ED-Kupfer, rolled copper und VLP ED copper, um den Einfluss auf 77GHz-Verlust und Phasenverhalten zu verdeutlichen.

Auch das Finish darf nicht isoliert betrachtet werden. Nickelhaltiges ENIG kann bei mmWave zusätzlichen Verlust und Phasenabweichung bringen. Deshalb sollte man zusammen bewerten:

- Leiterbreite und Stromverteilung in der RF-Struktur
- Ob die Struktur Microstrip oder GCPW ist
- Wie empfindlich das Design auf Phasenkonsistenz reagiert
- Welche Montage- und Zuverlässigkeitsanforderungen das Finish erzwingen

<a id="hybrid-stackup"></a>
## Wie erkennt man, ob ein Hybrid-Stackup serienreif ist?

Fazit: **Die eigentliche Frage ist meist nicht, ob sich ein Muster bauen lässt, sondern ob RF-Lagen und FR-4-Lagen dauerhaft stabil hybrid verpressbar sind.**

Rogers RO4830 und RO4830 Plus werden öffentlich genau in diesem Kontext dargestellt: als Cap-Layer-Material für FR-4-Multilayer im 76-81GHz-Automotive-Radarbereich. Das ist attraktiv, weil:

- **RF-Lagen** ein verlustärmeres und glatteres Materialsystem bekommen
- **Digital-, Steuer- und Leistungslagen** bei besser beherrschbaren FR-4-Typen bleiben
- **Die Gesamtfertigung** näher am bekannten FR-4-Fenster bleibt

Aber Hybrid-Build ist nicht automatisch risikolos. Deshalb sollte man den Lieferanten gezielt fragen:

- Ob das RF-Material mit dem vorgesehenen FR-4-Core und Prepreg schon validiert wurde
- Ob Erfahrung mit Bohren, Desmear, Mikrovia und Finish in Hybrid-Multilayern vorliegt
- Ob die Serie ein engeres Laminations- und Bohrfenster braucht als normale FR-4-Jobs
- Ob Material-Lots zwischen Muster, NPI und Serie rückverfolgbar und konsistent gehalten werden können

<a id="validation"></a>
## Wie sollte die Materialstrategie vor der Serie validiert werden?

Fazit: **Validierung soll nicht nur beweisen, dass ein Material theoretisch gut aussieht, sondern dass es nach echter Fertigung weiter Millimeterwellenleistung und Strukturstabilität hält.**

IPC TM-650 liefert den allgemeinen Rahmen für Dk-, Df-, TDR-, Signal-Loss- und Temperaturwechselmethoden. Für ADAS-Radar ist meist eine kombinierte Validierung am wertvollsten:

| Validierungspunkt | Wofür er besonders geeignet ist | Beobachtungspunkt |
|---|---|---|
| Dk/Df- und Loss-Coupons | Ob das Material den RF-Budgetpfad wirklich erfüllt | Gleiche Geometrie, gleiches Finish, gleiche Kupferbedingung |
| RF-Coupon oder Leitungsprobe | Reale Feedline-Verluste und Phasenstabilität | Dünnes Dielektrikum, verschiedene Rauheit, verschiedene Finishs |
| Hybrid-Struktur-Review | Ob Lamination und Bohren gesund bleiben | Verzug, Lagenregistrierung, Lochwand, Mikrovia-Bildung |
| Umwelt- und Montagevalidierung | Eignung für Fahrzeugumgebung und Lead-free-Montage | Temperaturwechsel, Feuchte, Reflow-Nachverhalten |
| Lot-Konsistenztest | Eignung für NPI und SOP | Lot-zu-Lot-Veränderung bei Verlust, Phase und Yield |

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- RF-Lagen und Antennen-Feeds zuerst über [High-Frequency PCB](https://hilpcb.com/en/products/high-frequency-pcb) bewerten.
- Wenn Rogers oder ein ähnliches HF-Laminat gesetzt ist, Hybrid-Lamination, Bohren und Finish parallel über [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) prüfen.
- Beim Übergang von Muster zu Validierungslosen Stackup, Materialtyp, Kupfertyp und Finish gemeinsam in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) geben.
- Sind Material, Struktur und Validierungspunkte geklärt, diese sauber in [Quote / RFQ](https://hilpcb.com/en/quote/) bündeln.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Muss ein ADAS-Radar-PCB komplett aus PTFE bestehen?

Nein. Viele 76-81GHz-Radarboards setzen verlustärmeres Material nur in RF-Cap-Layern oder kritischen Feed-Strukturen ein, während andere Lagen FR-4-Typen nutzen.

### Warum reicht Df allein für die Materialwahl nicht aus?

Weil Millimeterwellenverhalten auch von Dk-Toleranz, TCDk, Kupferrauheit, Finish, Dicke und Prozessschwankung abhängt.

### Ist Kupferrauheit bei Radarboards wirklich so wichtig?

Ja. Öffentliche mmWave-Unterlagen zeigen klar, dass raue Kupferoberflächen Verlust erhöhen und das effektive Dk- und Phasenverhalten verschieben.

### Ist ENIG für ADAS-Radar geeignet?

Nur mit Vorsicht. Nickelhaltiges ENIG kann in RF-Zonen bei mmWave zusätzlichen Verlust und Phasenabweichung einbringen.

### Wann gilt ein Hybrid-Radarboard als serienreif?

Erst wenn repräsentative RF-Coupons, Hybrid-Strukturqualität und Verhalten nach Temperatur-, Feuchte- oder Lead-free-Tests zusammen stabil sind.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [Rogers Automotive Radar Design Considerations for Autonomous and Safety Systems](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/technical-articles/automotive-radar-design-considerations-for-autonomous-and-safety-systems.pdf)  
   Stützt den Kontext zu 77/79GHz-Radar sowie die Relevanz von Dk-Stabilität, TCDk und Feuchteverhalten.

2. [Rogers RO3003 Laminates](https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates)  
   Stützt die öffentlichen Materialdaten zu RO3003.

3. [Rogers RO3003G2 Data Sheet](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3003g2--data-sheet.pdf)  
   Stützt den Hinweis auf automotive-radar-optimiertes Material und VLP ED copper.

4. [Rogers RO4830 Plus Laminates Data Sheet](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4830-plus-laminates-data-sheet.pdf)  
   Stützt die Aussagen zu 76-81GHz-Cap-Layern, FR-4-Hybrid, Laserbohren und Lead-free-Kompatibilität.

5. [Rogers PCB Design and Fabrication Concerns for Millimeter-Wave Circuits](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/pcb-design-and-fabrication-concerns-for-millimeter-wave-circuits.pdf)  
   Stützt die technischen Schlussfolgerungen zu Kupferrauheit, Finish und mmWave-Konsistenz.

6. [Rogers Steering Circuit Materials for 77 GHz Automotive Radar](https://rogerscorp.com/en/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/steering-circuit-materials-for-77-ghz-automotive-radar.pdf)  
   Stützt den Vergleich von ED copper, rolled copper und VLP ED copper bei 77GHz.

7. [Isola Astra MT77 Laminate and Prepreg Data Sheet](https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg.pdf)  
   Stützt das Beispiel eines alternativen öffentlichen Radar-Materialpfads.

8. [IPC TM-650 Test Methods Manual](https://www.electronics.org/test-methods)  
   Stützt den allgemeinen Methodenrahmen für Dk, Df, TDR, Signalverlust und Temperaturwechsel.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für Hochfrequenz und Automotive-Elektronik
- Technische Prüfung: Teams für PCB-Prozess und RF-Stackup-Engineering
- Letzte Aktualisierung: 2025-11-18

---
title: "Wie man PCB-Differenzpaare routet: Praxistaugliche Regeln für Impedanz, Referenzebenen, Skew und Via-Strukturen"
description: "Eine direkte Antwort auf Zielimpedanz, Referenzebenen-Kontinuität, Symmetrie, Längenausgleich, Via-Stub und Fertigungsvalidierung, die bei PCB-Differenzpaaren zuerst geprüft werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# Wie man PCB-Differenzpaare routet: Praxistaugliche Regeln für Impedanz, Referenzebenen, Skew und Via-Strukturen

- **Bei Differenzpaaren muss zuerst nicht die absolute Gleichlänge festgelegt werden, sondern welches Ziel laut Standard oder Datenblatt überhaupt gilt.** NXP fordert für PTN3222 eUSB2 **85 Ohm differentielle Impedanz**, während AN13335 für Automotive Ethernet das MDI mit **100 Ohm** als edge-coupled Microstrip oder Stripline routet.
- **Symmetrie ist wichtiger als bloß enger Leitungsabstand.** Intel AN528 zeigt klar, dass beide Leiter elektrisch gleich aussehen müssen, sonst entsteht differential-to-common-mode conversion.
- **Kontinuität der Referenzebene und Layer-Wechsel beschädigen die Verbindung oft schneller als die gerade Strecke.** NXP AN13462 fordert, High-Speed-Differenzpaare nicht über plane splits zu führen und Vias zu minimieren; Intel weist zusätzlich auf ausreichend nahe und symmetrische GND-Vias für den Rückstrom hin.
- **Serpentinen, Anti-Pads und Via-Stubs dürfen nicht mechanisch aus Vorlagen kopiert werden.** Intel zeigt beim P/N de-skew, dass Trombone-Strukturen Impedanzwelligkeit und mode conversion erzeugen können.
- **Serientauglichkeit entsteht nur, wenn Stackup, Toleranzen, Breakout und Validierung gemeinsam definiert werden.** Genau diesen Punkt wiederholen Intel 82566 und NXP in ihren Layout-Hinweisen.

> **Quick Answer**  
> Das Kernziel beim Routing von PCB-Differenzpaaren ist eine symmetrische Ausbreitungsumgebung in realem Stackup, realer Kupferdicke und realen Übergangsstrukturen. Erst Zielimpedanz und Skew-Budget einfrieren, dann gleichlagiges Routing, kontinuierliche Referenzebenen, symmetrische Vias und disziplinierten Längenausgleich umsetzen und das Ergebnis anschließend mit Coupon, TDR oder Systemtest verifizieren.

## Inhaltsverzeichnis

- [Was sollte man bei PCB-Differenzpaaren zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum muss man Differenzpaare zuerst aus Standard und Stackup definieren?](#standards-stackup)
- [Warum werden Symmetrie, Skew und Serpentinen so oft falsch benutzt?](#symmetry-skew)
- [Warum sind Referenzebenen, Layer-Wechsel und Via-Stubs Hochrisikozonen?](#planes-vias)
- [Wie validiert man Differenzpaarrouting vor der Fertigung?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei PCB-Differenzpaaren zuerst prüfen?

Zuerst **Schnittstellenziel, Stackup, Referenzebene, Symmetrie und Layer-Wechsel-Strategie**.

Die Aufgabe bedeutet weder "zwei Leitungen einfach parallel ziehen" noch "erst routen und später Impedanz rechnen lassen". Unterschiedliche Protokolle, PHYs und Steckverbinder verlangen unterschiedliche Regeln. NXP AN13462 setzt eUSB2 auf **85 Ohm differentiell** und verbietet plane splits im High-Speed-Pfad. NXP AN13335 verlangt für Automotive Ethernet **100 Ohm** und begrenzt die Paarabweichung zwischen Steckverbinder und Choke auf **1 mm**. Intel 82566 ergänzt für Gigabit Ethernet **100 Ohm differentiell (±20%)** und weniger als **50 mil** Paarabweichung.

Darum sollte man zuerst klären:

1. **Ob das Interface 85, 90, 95 oder 100 Ohm differentiell fordert**
2. **Woher das zulässige intra-pair skew budget kommt**
3. **Ob die Leitung als Microstrip oder Stripline geführt wird und die Referenzebene durchgängig bleibt**
4. **Ob Layer-Wechsel erlaubt sind und wie Rückstrom und Stubs dabei behandelt werden**
5. **Ob der Hersteller die Zielgeometrie im gewünschten Stackup stabil fertigen kann**

Wenn mehrere High-Speed-Schnittstellen auf der Platine liegen, sollte man [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) und den [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) vor dem Layout gemeinsam schließen.

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Methode | Warum wichtig | Wie prüfen | Wenn ignoriert |
|---|---|---|---|---|
| Zielimpedanz | Zuerst aus Standard oder Datenblatt ableiten | Differenzpaare sind nicht pauschal 100 Ohm | Standard, Datenblatt, Stackup-Review | Breite und Abstand starten falsch |
| Symmetrie | Querschnitt, Referenzumgebung und Übergänge angleichen | Asymmetrie erzeugt mode conversion | Layout-Review, 3D-Übergänge | Mehr Gleichtaktrauschen, schlechteres Auge |
| Gleichlagiges Routing | Paar möglichst vollständig auf einer Lage halten | Layer-Wechsel bringen Diskontinuitäten | Post-Route-Review, Via-Zahl | Mehr Skew, Reflexion und Debug-Aufwand |
| Referenzebene | Durchgehend, nah und möglichst einheitlich halten | Plane splits stören den Rückstrom | Plane-Review, Layer-Review | EMI und mode conversion verschlechtern sich |
| Längenausgleich | Nur nach Interface-Budget und nahe der Fehlstelle | Falsche Serpentinen erzeugen Impedanzwelligkeit | Skew-Review, TDR, Simulation | Ausgleich erzeugt neue Probleme |
| Via / Stub | Vias minimieren; bei Wechsel symmetrische Signal- und GND-Vias | Via discontinuity ist ein Kernrisiko | TDR, Schliff, Backdrill-Review | Lokale Reflexion, ISI, Rückstrom-Umweg |

| Interface-Beispiel | Typische öffentliche Vorgabe | Designhinweis |
|---|---|---|
| eUSB2 | NXP AN13462: 85 Ohm, gleiche Lage, <20 mil Paarfehler, kein plane split | Auch "kleinere" High-Speed-Links brauchen harte Regeln |
| Automotive Ethernet MDI | NXP AN13335: 100 Ohm, 1 mm Abgleich von Connector bis Choke, symmetrische GND-Vias | Referenz und Gleichtaktkontrolle sind so wichtig wie Impedanz |
| Gigabit Ethernet MDI | Intel 82566: 100 Ohm ±20%, <50 mil Paarfehler, GND-Vias binnen 40 mil | Serienboards leben von Prozessdetails |
| FPGA True Differential I/O | Intel Agilex: 100 Ohm, ggf. Backdrill gegen Stub-Effekte | Mit steigender Datenrate wird die Via-Struktur zum Hauptobjekt |

<a id="standards-stackup"></a>
## Warum muss man Differenzpaare zuerst aus Standard und Stackup definieren?

Fazit: **Zielimpedanz und Geometrie sind kein Universaltemplate, sondern das Ergebnis aus Interface-Anforderung und realem Fertigungs-Stackup.**

NXP und Intel zeigen das klar: eUSB2 liegt bei **85 Ohm**, Automotive Ethernet MDI bei **100 Ohm**, und auch Intels True Differential I/O arbeitet im **100-Ohm**-Kontext. Der richtige Ablauf ist deshalb meist:

1. **Zielimpedanz aus Standard, Datenblatt oder Referenzdesign festlegen**
2. **Microstrip oder Stripline passend zu Verlust, Steckverbinder und EMI wählen**
3. **Mit dem Hersteller Material, Dielektrikumsdicke, Kupferdicke und Kompensation abstimmen**
4. **Danach erst Breite, Abstand und Toleranz in die Layout-Regeln schreiben**

Intel 82566 erinnert zusätzlich daran, dass zwei 50-Ohm-Einzelleitungen nicht automatisch 100 Ohm differentiell ergeben. Genau deshalb muss die Theorie in fertigungstaugliche Geometrie übersetzt werden.

<a id="symmetry-skew"></a>
## Warum werden Symmetrie, Skew und Serpentinen so oft falsch benutzt?

Fazit: **Weil viele Teams Gleichlänge mit Korrektheit verwechseln und strukturelle Symmetrie sowie lokale Kopplung ignorieren.**

Intel AN528 fordert für das ideale Differenzpaar elektrische Gleichheit und möglichst null Skew. Daraus folgt:

- **Symmetrie umfasst nicht nur Länge, sondern auch Querschnitt, Dielektrikum, Nachbarkupfer und Übergänge**
- **Skew ist an Veränderungen der Referenzumgebung gekoppelt**
- **Schlecht platzierte Serpentinen können lokal eine schlechtere Impedanz als die Hauptstrecke erzeugen**

Intel AN875 zeigt zusätzlich, dass Trombone-Strukturen locker gekoppelte Abschnitte und abweichende Verzögerung pro Länge erzeugen können. NXP empfiehlt deshalb, Ausgleich möglichst nahe der eigentlichen Fehlstelle vorzunehmen.

Der robustere Weg ist meist:

- Asymmetrien aus Bauteilanordnung und Breakout zuerst beseitigen
- Nur den wirklich budgetrelevanten Skew ausgleichen
- Kompensationsabschnitte sanft und locker gekoppelt halten
- Bei langen FR-4-Strecken auch fiber-weave-Risiken mitdenken

<a id="planes-vias"></a>
## Warum sind Referenzebenen, Layer-Wechsel und Via-Stubs Hochrisikozonen?

Fazit: **Sobald ein Differenzpaar Lagen wechselt, Splits kreuzt oder Stubs hinterlässt, sitzt das erste Risiko fast immer im Rückstrompfad und in lokalen Diskontinuitäten.**

NXP verbietet plane splits im High-Speed-Differenzpfad und empfiehlt gleiche Lage, wenige Vias und keine unnötigen Stubs. Intel ergänzt:

- Restliche Via-Barrel-Segmente wirken als kapazitive Stubs
- Beim Layer-Wechsel braucht der Rückstrom nahe GND-Vias
- Beide Leiter des Paars müssen symmetrische Via-Strukturen behalten

Intel 82566 macht es konkret: Bei einem Layer-Wechsel sollten GND-Vias innerhalb von **40 mil** zu den Signal-Vias liegen. Bei Wechsel zwischen unterschiedlicher Referenz kann zusätzlich ein naher Decoupling-Kondensator nötig sein.

Typische Hochrisikozonen sind:

1. **BGA-Breakout am Ursprung**
2. **Connector-Launch**
3. **Bereiche bei AC-Koppelkondensatoren und Common-Mode-Bauteilen**
4. **Layer-Transition-Vias und Anti-Pad-Zonen**
5. **Unbehandelte Through-Via-Stubs in dickeren Boards**

<a id="validation"></a>
## Wie validiert man Differenzpaarrouting vor der Fertigung?

Fazit: **Wertvolle Validierung beweist nicht nur, dass CAD ein Paar fertig geroutet hat, sondern dass Geometrie und Systemverhalten nach der Fertigung noch stimmen.**

Ein brauchbarer Pfad enthält meist:

| Validierungspunkt | Welche Frage wird beantwortet | Beobachtungspunkt |
|---|---|---|
| Stackup- / Impedanzreview | Passt die Zielgeometrie zur Fertigbarkeit? | Breite, Abstand, Kupferdicke, Dielektrikum, Toleranz |
| Coupon / TDR | Liegen reale Impedanz und Übergänge nahe am Ziel? | Impedanzplateau, lokale Diskontinuitäten, Via-Effekt |
| Schliffbild | Haben Pressen und Ätzen die Struktur verschoben? | Reale Leiterbreite, Kupferdicke, Dielektrikum, Anti-Pad |
| Systemtest | Ist das Paar mit realem Bauteil und Connector gesund? | Eye Diagram, Training, BER, EMI |
| Vergleich mehrerer Boards | Kommt das Risiko aus dem Design oder aus Build-Schwankung? | Board-Streuung, Lot-Konsistenz, Rework-Aufwand |

Der gemeinsame Punkt bei Intel und NXP: Zielimpedanz, Paarabweichung, plane continuity, symmetrische GND-Vias, Stub-Behandlung und Teststrategie müssen vor der Freigabe an die Fertigung klar dokumentiert sein.

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Zuerst mit [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) und [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) Stackup, Lagen und Referenzstrategie schließen.
- Den [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) vor dem Routing verwenden.
- Bei dichterem Breakout parallel das Via- und Fanout-Fenster von [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) prüfen.
- Definierte Stackups, Impedanztabellen, Schlüsselpaare und Validierung direkt in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) oder [Quote / RFQ](https://hilpcb.com/en/quote/) geben.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Sind Differenzpaare standardmäßig immer 100 Ohm?

Nein. eUSB2 liegt zum Beispiel bei 85 Ohm, während Automotive Ethernet MDI oft 100 Ohm nutzt. Immer zuerst Standard oder Chip-Dokumentation prüfen.

### Reicht Gleichlänge allein aus?

Nein. Ohne elektrische Symmetrie bei Referenz, Nachbarkupfer, Vias und Anti-Pads kann trotz Gleichlänge mode conversion entstehen.

### Darf ein Differenzpaar nie die Lage wechseln?

Doch, aber möglichst selten. Jeder Wechsel muss als komplette Struktur mit Signal-Via, GND-Via, Anti-Pad und Rückstrompfad betrachtet werden.

### Ist zentral gebündelter Serpentinen-Ausgleich sinnvoll?

Meist nicht. Ausgleich gehört möglichst nah an die Stelle des Fehlers und darf keine neue Diskontinuität erzeugen.

### Warum stören plane splits auch bei Differenzpaaren?

Weil auch Differenzpaare nicht ohne Referenz arbeiten. Splits, Aussparungen oder asymmetrische GND-Vias verändern den Rückstrompfad und erhöhen Gleichtaktrauschen.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   Stützt die Aussage zu elektrischer Symmetrie, geringem Skew und fiber-weave-Einfluss.

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   Stützt die Bewertung von Trombone-Kompensation als potenzielle Quelle für Impedanzwelligkeit und mode conversion.

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   Stützt die Beschreibung von Via-Stub, symmetrischen Signal-Vias und GND-Vias für den Rückstrom.

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   Stützt die Serien-Checkpunkte zu 100 Ohm, Paarfehler, GND-Via-Abstand und Stub-Vermeidung.

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   Stützt die eUSB2-Vorgaben zu 85 Ohm, Symmetrie, Matching, plane split, Via-Reduktion und Stub-Vermeidung.

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   Stützt die Aussagen zu 100 Ohm MDI, Ground-Symmetrie, Connector-to-Choke-Matching und Common-Mode-Risiko.

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   Stützt den 100-Ohm-Kontext und die Empfehlung, Stub-Effekte bei Bedarf mit Backdrill zu reduzieren.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für High-Speed-Interconnect und SI
- Technische Prüfung: Teams für PCB-Prozess, Signalintegrität und Steckverbinder-Engineering
- Letzte Aktualisierung: 2025-11-18

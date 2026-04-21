---
title: "Bei Mixed-Signal-PCBs nicht zu früh die Masse auftrennen: Was man bei Rückstrompfaden, ADC-Disziplin und Testbarkeit zuerst prüfen sollte"
description: "Praxisleitfaden zu Noise-Zoning, Rückstrompfaden, ADC-/Referenz-/Treiber-Lokalsystem, Decoupling, Stackup und Testbarkeit, die auf einer Mixed-Signal-PCB zuerst eingefroren werden sollten."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["Mixed-signal PCB", "ADC layout", "PCB grounding", "Decoupling", "EMC design", "DFM"]
---

# Bei Mixed-Signal-PCBs nicht zu früh die Masse auftrennen: Was man bei Rückstrompfaden, ADC-Disziplin und Testbarkeit zuerst prüfen sollte

- **Auf einer Mixed-Signal-Platine sollte man meist nicht zuerst fragen, ob Analog- und Digitalmasse in zwei Inseln getrennt wurden, sondern wie die entscheidenden Ströme tatsächlich zurückfließen.** Analog Devices beschreibt in MT-031 ausdrücklich, dass es in Datenwandler-Systemen bei AGND und DGND um das Verständnis der Rückstrompfade geht und nicht um ein mechanisches Zerschneiden der Massefläche.
- **Viele ADC-Rauschprobleme beginnen nicht auf den Hauptleitungen, sondern dort, wo ADC, Referenz, Treiber und Decoupling nicht als ein lokales System behandelt werden.** ADIs Layout-Hinweise für Mixed Signal empfehlen ausdrücklich, Steckverbinder an den Rand zu setzen und Decoupling-Kondensatoren sowie Quarze nahe am Mixed-Signal-Baustein zu platzieren.
- **Decoupling bedeutet nicht einfach "mehr Kondensatoren". Es bedeutet, die Hochfrequenzschleife so klein wie möglich zu halten.** MT-101 betont, dass Decoupling-Kondensatoren so nah wie möglich an die Versorgungs-Pins gesetzt werden müssen, um die Schleifeninduktivität zu minimieren.
- **Partitionierung sollte dem Rauschverhalten und der Rückstromlogik folgen, nicht nur Modulnamen im Blockdiagramm.** Ein Layout mit "Analog links" und "Digital rechts" verdeckt oft die eigentlichen high-di/dt-Schleifen, hochohmigen Knoten und Takt-Rauschbeziehungen.
- **Ein wertvolles erstes Layout ist nicht nur rauscharm, sondern auch fertigbar, messbar und reparierbar.** Genau das entscheidet, ob der Entwurf vom Prototyp sauber in Pilot und Serie übergeht.

> **Quick Answer**  
> Der Kern eines Mixed-Signal-PCB-Layouts ist nicht, zuerst die Massefläche zu trennen. Entscheidend ist, dass Rückstrompfade, das lokale ADC-System, die Decoupling-Schleifen, die Noise-Partitionierung sowie Debug- und Testzugänge gleichzeitig sauber aufgesetzt werden. Bei ADC/DAC-, Sensorerfassungs- und Steuerungsplatinen entscheidet meist weniger die Frage "wurden die Massen getrennt?" als die Frage, ob Stromfluss, Rauschverhalten und die Beziehungen der lokalen Bauteile richtig behandelt wurden.

## Inhaltsverzeichnis

- [Was sollte man bei einer Mixed-Signal-PCB zuerst prüfen?](#overview)
- [Wichtige Regeln und Parameterübersicht](#rules)
- [Warum sollte Partitionierung dem Rauschverhalten statt Funktionsnamen folgen?](#partition)
- [Warum ist Rückstromkontinuität wichtiger als "Massen trennen"?](#return-path)
- [Warum müssen ADC, Referenz, Treiber und Decoupling als lokales System geprüft werden?](#adc-local)
- [Warum müssen auch Stackup, DFM und Testbarkeit früh eingefroren werden?](#dfm)
- [Nächste Schritte mit HILPCB](#next-steps)
- [FAQ](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfinformationen](#author)

<a id="overview"></a>
## Was sollte man bei einer Mixed-Signal-PCB zuerst prüfen?

Zuerst **Noise-Partitionierung, Rückstrompfade, das lokale ADC-System, Decoupling, Stackup und Testbarkeit**.

Es reicht nicht, einen Analogbereich und einen Digitalbereich zu definieren und die Sache damit für erledigt zu halten, und es ist auch nichts, was man nach dem Schaltplan später irgendwie "im Layout rettet". ADIs MT-031 ist in diesem Punkt eindeutig: In Datenwandler-Systemen geht es bei AGND / DGND vor allem um Rückstrompfade und Massegrenzen, nicht um ein einfaches Aufschneiden der Ebenen. MT-101 geht noch weiter und betont, dass Hochfrequenz-Bypass- und Decoupling-Kondensatoren so nah wie möglich an die Versorgungspins gehören, um die Schleifenfläche zu verkleinern. Ein weiterer ADI-Artikel zum Mixed-Signal-Layout empfiehlt ausdrücklich, Steckverbinder an den Platinrand zu setzen und Decoupling-Bauteile sowie Quarze dicht an den Mixed-Signal-Baustein heranzuführen.

Eine belastbarere Layout-Review-Reihenfolge ist meist:

1. **Zuerst high-di/dt-Schleifen, hochohmige Knoten, Taktquellen und empfindliche analoge Frontends identifizieren.**
2. **Dann prüfen, ob die entscheidenden Rückstrompfade kurz und kontinuierlich sind.**
3. **ADC, Referenz, Treiber, Filter und Decoupling als ein lokales System behandeln.**
4. **Stackup, Ground-Reference-Logik und Steckverbinderstrategie am Boardrand früh einfrieren.**
5. **Testpunkte, Rework-Flächen und Assembly-Zugänglichkeit prüfen, bevor das Layout als geschlossen gilt.**

Wenn das Projekt analoge Frontends mit dichter Schnittstellenbelegung kombiniert, ist es meist sinnvoll, die Randbedingungen von [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) und [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) schon in die erste Board-Review einzubeziehen, statt DFM später das Layout rückwärts ändern zu lassen.

<a id="rules"></a>
## Wichtige Regeln und Parameterübersicht

| Regel / Parameter | Empfohlener Ansatz | Warum wichtig | Wie verifizieren | Risiko bei Ignorieren |
|---|---|---|---|---|
| Noise-Partitionierung | Nach high di/dt, Takt, hoher Impedanz und empfindlichen Frontends partitionieren | Funktionsnamen definieren keine Rauschgrenzen | Layout-Review, Rückstromanalyse | Layout wirkt sauber, Rauschpfade bleiben vermischt |
| Rückstrompfad | Unter kritischen Knoten und Leitungen durchgängige Referenzflächen halten | Unterbrochene Rückstrompfade erzeugen EMI und höheren Noise Floor | Ebenenprüfung, Near-Field-Scan, Messung | ADC-Rauschen, Crosstalk und EMC verschlechtern sich gemeinsam |
| ADC-Lokalsystem | ADC, Referenz, Treiber, Filter und Decoupling gemeinsam prüfen | Der empfindlichste Bereich ist oft die kürzeste lokale Schleife | Platzierungsreview, lokale Messung | Stammrouting sieht gut aus, Lokalverhalten ist schlecht |
| Decoupling-Position | Hochfrequenz-Decoupling nahe an die Versorgungspins | Decoupling wirkt zuerst über Schleifenfläche, nicht Stückzahl | First-Article-Check, Oszilloskop, EMI-Beobachtung | Viele Kondensatoren, wenig Wirkung |
| Stackup und Ground Reference | Stackup muss Rückstromqualität und Fertigungsstabilität zugleich stützen | Nur auf Impedanz optimierter Stackup erhöht Board-Form- und Prozessrisiko | Stackup-Review, Board-Form-Bewertung | Prototyp funktioniert, Pilot streut stärker |
| Testbarkeit | Schlüssel-Testzugänge und Rework-Flächen schon in Rev A vorsehen | Mixed-Signal-Debug hängt stark an Beobachtbarkeit | Probe-Zugänglichkeit, Erst-Board-Bring-up | Probleme treten auf, Ursache bleibt verborgen |

| Öffentlicher Mixed-Signal-Kontext | Direkte Bedeutung für das Layout |
|---|---|
| MT-031: Rückstrom zuerst | "Massen trennen" ist keine Standardantwort; Rückstrom ist das Hauptthema |
| MT-101: Decoupling an den Pin | Decoupling ist eine Frage von Position und Schleifengröße, nicht nur Stückzahl |
| ADI Mixed-Signal-Layout-Guide | Steckverbinder an den Rand, Hilfsbauteile nahe an den Mixed-Signal-IC |

<div style="background: linear-gradient(135deg, #eef6f3 0%, #eef3fb 100%); border: 1px solid #d7e1de; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7a68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #385f50; font-weight: 700;">Return Paths Before Ground Myths</div>
      <div style="margin-top: 8px; color: #23342e;">Die erste Frage auf einer Mixed-Signal-Platine lautet, wie der Strom zurückfließt, nicht ob die Massen "hart genug" getrennt wurden.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7392; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38576f; font-weight: 700;">ADC Area Is a Local System</div>
      <div style="margin-top: 8px; color: #243441;">ADC, Referenz, Treiber und Decoupling-Netzwerk sind keine isolierten Teile, sondern das kürzeste und empfindlichste Lokalsystem auf dem Board.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6948; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Decoupling Is Geometry</div>
      <div style="margin-top: 8px; color: #392f26;">Die Wirkung von Decoupling kommt aus Schleifenlänge, Kondensatorplatzierung und Via-Struktur, nicht aus der Kondensatorzahl in der BOM.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8b5d73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #70495c; font-weight: 700;">DFM Protects Analog Performance</div>
      <div style="margin-top: 8px; color: #392733;">Testpunkte, Rework-Flächen, AOI-Zugänglichkeit und Panel-Grenzen sind keine Nebensache. Sie entscheiden, wie schnell Probleme auf der ersten Platine geschlossen werden.</div>
    </div>
  </div>
</div>

<a id="partition"></a>
## Warum sollte Partitionierung dem Rauschverhalten statt Funktionsnamen folgen?

Weil **der eigentliche Konflikt auf einer Mixed-Signal-Platine zwischen Rauschquellen und empfindlichen Knoten besteht und nicht zwischen Bezeichnungen im Blockdiagramm**.

ADIs Mixed-Signal-Layout-Hinweise sagen ausdrücklich, dass Layout mit der Bauteilplatzierung beginnt, Steckverbinder an den Rand gehören und Hilfsbauteile wie Decoupling oder Quarze nahe an den Mixed-Signal-Baustein gesetzt werden sollten. Die dahinterliegende Logik ist einfach: Partitionierung muss dem Rauschverhalten und der Rückstromlogik folgen, nicht dem Schaltplan-Namen.

Eine wirksamere Partitionierung bedeutet meist:

- **Sensor-Frontend, Referenzquelle und Low-Level-Analogsignale als Low-Noise-Zone behandeln**
- **Taktquellen, Schaltregler und schnelle Digitalschnittstellen als aktive Rauschzonen behandeln**
- **ADC, DAC und Isolationsbauteile als Grenzknoten statt als einfache Modulkästen sehen**
- **Steckverbinder-Eintritt, Schutzbauteile und empfindliche Frontends mit kontrolliertem Abstand anordnen**

Wenn das Layout nur "Analog links, Digital rechts" abbildet, bleiben reale Probleme oft verborgen, etwa Digitale-Rückströme durch die Referenzzone, Takte direkt neben hochohmigen Eingängen oder Störungen, die vom Steckverbinder aus sofort in die empfindlichste Zone gelangen. Für Boards mit Schnittstellen plus analoger Erfassung hilft auch der Quercheck mit dem Interface-Zonen-Denken aus [Was man bei einem EtherCAT-Interface-PCB-Prototyp zuerst validieren sollte](/code/blogs/blogs/1119-1-ccc/de/ethercat-interface-pcb-prototype.md).

<a id="return-path"></a>
## Warum ist Rückstromkontinuität wichtiger als "Massen trennen"?

Weil **die meisten Mixed-Signal-Probleme nicht daraus entstehen, dass "zu wenig Masse" vorhanden ist, sondern daraus, dass der Strom keinen sauberen Rückweg hat**.

Genau das ist der Kern von MT-031: In Datenwandler-Systemen schafft ein aggressives Trennen von AGND und DGND oft mehr Probleme, als es löst. Zuerst bestätigt werden muss:

1. **ob kritische Signale und Decoupling-Schleifen unter sich eine durchgängige Referenzfläche haben**
2. **ob digitaler Rückstrom Referenz- oder empfindliche Analogbereiche kreuzt**
3. **ob Layerwechsel und Grenzknoten weiterhin einen lokalen niederimpedanten Rückweg bieten**

Wenn Rückströme über Slots, verengte Kupferstellen oder schlecht gewählte Grenzen springen müssen, entsteht meist nicht ein einzelner Fehler, sondern ADC-Rauschen, Crosstalk, EMI und Synchronisationsprobleme steigen gemeinsam. Auf Boards mit schnellen Digitalschnittstellen, ADCs und isolierten Versorgungen lohnt es sich meist mehr, diesen Punkt zuerst einzufrieren als die Frage, ob Massen getrennt werden sollen.

<a id="adc-local"></a>
## Warum müssen ADC, Referenz, Treiber und Decoupling als lokales System geprüft werden?

Weil **der empfindlichste Teil einer Mixed-Signal-Platine meist nicht das Haupt-Routing ist, sondern die kürzeste lokale Schleife rund um den ADC selbst**.

MT-101 betont, dass der Decoupling-Kondensator so nah wie möglich an den Versorgungspins sitzen muss. ADIs Mixed-Signal-Layout-Hinweise sagen ebenfalls, dass die Hilfsbauteile rund um einen Mixed-Signal-Baustein nah am Baustein bleiben müssen. Zusammengenommen ergibt sich daraus praktisch zwingend: ADC, Referenz, Treiber, Filter und Decoupling-Netzwerk müssen als ein lokales System geprüft werden.

Für die fokussierte Review sollte man typischerweise herausziehen:

- **ob der Pfad zwischen ADC und Frontend-Treiber so kurz und direkt wie möglich ist**
- **ob die Referenzquelle von offensichtlichen Wärme- und Rauschquellen fern bleibt**
- **ob das Decoupling die Schleife wirklich am Pin schließt**
- **ob Eingangsschutz und Filter den Eintrittspunkt schützen, ohne selbst Rauschen hereinzuholen**

Viele laute erste Muster scheitern nicht an der Systemarchitektur, sondern daran, dass das kürzeste und empfindlichste Lokalsystem um den ADC von Anfang an auseinandergezogen wurde. Wenn das Board zusätzlich schnelle Digital- oder synchrone Schnittstellen trägt, lohnt sich die erneute Prüfung von Rückstrom und Boundary-Logik mit dem Stackup-Denken aus [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) und [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).

<a id="dfm"></a>
## Warum müssen auch Stackup, DFM und Testbarkeit früh eingefroren werden?

Weil **ein Mixed-Signal-Board, das nur als elektrische Idee und nicht als baubares, debugbares Produkt betrachtet wird, im Pilot schnell teuer wird**.

ADIs Applikationsmaterial weist immer wieder darauf hin, dass Multilayer-Boards, niederimpedante Referenzflächen und korrektes Decoupling Grundvoraussetzungen für die spezifizierte Performance sind. In der Praxis bedeutet das:

- **das Stackup muss Rückstromqualität und Fertigungsstabilität gleichzeitig stützen**
- **Testpunkte, Debug-Zugänge und Rework-Flächen müssen in der ersten Revision vorhanden sein**
- **Panel-Rails, Prozesskanten, AOI-Zugänglichkeit und empfindliche Analogbereiche dürfen sich nicht gegenseitig stören**

Wenn diese Inputs auf später verschoben werden, ist das Ergebnis oft eine Platine, die zwar funktioniert, aber schwer zu messen, schwer zu reparieren und schwer zu reproduzieren ist. Für Projekte mit schnellem Pilot-Ziel ist es meist sinnvoller, die Randbedingungen von [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) und [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) schon in die Vorab-Review zu ziehen, statt Pilot-Builds Probleme entdecken zu lassen, die das Layout hätte vermeiden können.

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie an einer Erfassungsplatine, Steuerungsplatine, Sensor-Frontend oder einem anderen Mixed-Signal-Elektronikdesign arbeiten, besteht der nächste Schritt meist darin, "Layout-Prinzipien" in fertigungstauglichen Input zu übersetzen:

- Wenn Rückstrompfad, ADC-Lokalbereich und Ground Reference das Hauptthema sind, zuerst mit [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) Stackup und Referenzebenen-Logik zusammenführen.
- Wenn das Design zusätzlich schnelle Digitalschnittstellen oder synchrone Links trägt, Layerzuordnung und Grenzen mit [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) gegenprüfen.
- Wenn der Prototyp Noise, Decoupling und Testbarkeit absichern soll, die Schlüsselprüfpunkte früh in die [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/)‑Phase einziehen.
- Wenn Lokalsystem, Ground Reference und Testzugänge bereits konvergiert sind, den vollständigen Anforderungssatz in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) oder [Quote / RFQ](https://hilpcb.com/en/quote/) überführen.

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Braucht eine Mixed-Signal-Platine immer eine harte Trennung zwischen Analog- und Digitalmasse?

Nicht immer. MT-031 sagt nicht "immer trennen", sondern stellt Rückstromkontinuität, Grenzdefinition und die richtige Verbindung der Massen in den Vordergrund.

### Warum kann die Simulation gut aussehen, während die erste Platine trotzdem stark rauscht?

Häufige Gründe sind unterbrochene Rückstrompfade, ein zerrissenes ADC-Lokalsystem, schlecht platzierte Decoupling-Bauteile oder Rauschquellen zu nah an empfindlichen Knoten.

### Warum lösen viele Decoupling-Kondensatoren das Problem trotzdem nicht?

Weil MT-101 wiederholt auf Position und Schleifenfläche hinweist. Die Kondensatorzahl ist nicht der primäre Hebel, die Schleifengeometrie ist es.

### Warum führen viele ADC-Probleme auf das lokale Layout und nicht auf die Hauptleitungen zurück?

Weil der ADC-Bereich das empfindlichste Lokalsystem ist. Wenn Referenz, Treiber, Filter, Decoupling und Masseführung dort nicht stimmen, rettet sauberes Stammrouting das Ergebnis nicht.

### Welches Serienproblem wird auf Mixed-Signal-Boards am leichtesten übersehen?

Testpunkt-Zugänglichkeit, Rework-Fläche, AOI-Zugänglichkeit und Fixture-Pfade werden oft übersehen. Sie bestimmen direkt die Pilot-Effizienz und die Geschwindigkeit der Fehlersuche.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [MT-031: Grounding Data Converters and Solving the Mystery of “AGND” and “DGND” | Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/mt-031.pdf)  
   Belegt, dass Mixed-Signal- und Datenwandler-Systeme mit dem Verständnis von Rückstrompfaden und AGND / DGND beginnen sollten und nicht mit mechanischem Auftrennen von Ebenen.

2. [MT-101: Decoupling Techniques | Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/mt-101.pdf)  
   Belegt, dass Hochfrequenz-Decoupling nahe an den Versorgungspins sitzen muss, um Induktivität und Schleifenfläche klein zu halten.

3. [What Are the Basic Guidelines for Layout Design of Mixed-Signal PCBs? | Analog Devices](https://www.analog.com/en/resources/analog-dialogue/articles/what-are-the-basic-guidelines-for-layout-design-of-mixed-signal-pcbs.html)  
   Belegt die öffentliche Empfehlung, Steckverbinder an den Rand zu setzen, Hilfsbauteile nahe am Mixed-Signal-IC zu halten und das Layout über die Platzierung zu lösen statt über spätere Korrekturen.

4. [AN-1142: Techniques for High Speed ADC PCB Layout | Analog Devices](https://www.analog.com/en/resources/app-notes/an-1142.html)  
   Ergänzt den öffentlichen Hintergrund zu Power-/Ground-Planes, Decoupling und Stackup auf High-Speed-ADC-Boards und zeigt, dass die Frage "Massen trennen oder nicht?" vom realen System und nicht von einer festen Regel abhängt.

<a id="author"></a>
## Autoren- und Prüfinformationen

- Autor: HILPCB Content-Team für Mixed Signal und Data Acquisition
- Technische Prüfung: Engineering-Team für PCB-Prozess, EMC, Analog-Frontend und Test
- Letzte Aktualisierung: 2025-11-19

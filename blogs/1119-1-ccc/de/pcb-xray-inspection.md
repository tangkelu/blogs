---
title: "Worauf PCB-X-Ray-Inspektion wirklich schauen sollte: Es geht nicht nur darum, Void-Bilder aufzunehmen"
description: "Praxisleitfaden zu Geltungsbereich, Defektinterpretation, Sampling-Logik, Prozessrückführung und Traceability-Kette, die bei PCB-X-Ray-Inspektion zuerst definiert werden sollten."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# Worauf PCB-X-Ray-Inspektion wirklich schauen sollte: Es geht nicht nur darum, Void-Bilder aufzunehmen

- **Das erste Problem, das X-Ray-Inspektion lösen sollte, ist nicht, ob ein verstecktes Defektbild aufgenommen wurde, sondern ob die Qualität verdeckter Lötstellen wirklich auf den Assembly-Prozess, die Sampling-Regeln und die Traceability-Kette zurückgeführt werden kann.** Die öffentlichen Titel von IPC-7095E und IPC-7093 stellen Design- und Assembly-Process-Guidance in den Mittelpunkt. Das zeigt bereits, dass X-Ray nicht nur als nachträgliche Bildbeurteilung gedacht ist.
- **X-Ray sollte nicht auf das Wort "Void" reduziert werden.** Bei BGA-, BTC-, QFN-, LGA- und großen Bottom-Pad-Packages sind Wetting, Bridging, Offset, Head-in-Pillow, Joint-Konsistenz und Void-Verteilung unterschiedliche Risikodimensionen.
- **Der größte Nutzen von X-Ray ist nicht, eine einzelne schlechte Leiterplatte zu finden, sondern das Bild auf Stencil-Design, Solder Paste, Pad-Geometrie, Reflow-Profil und Feuchtebelastung zurückführen zu können.** Wenn das Bild nicht in den Prozess zurückspielt, bleibt Qualitätsverbesserung langsam.
- **Die Sampling-Strategie muss an Package-Risiko, Lot-Änderung und Ausfallkosten gebunden werden.** Neue Packages, neue Stencils, neue Paste oder ein neues Reflow-Fenster sollten nicht automatisch die alte Sampling-Dichte übernehmen.
- **X-Ray-Bilder ohne Lot-Nummer, Equipment-, Programm- und Bewertungsdaten sind schwache Evidenz für spätere Root-Cause-Arbeit und Kundenreklamationen.**

> **Quick Answer**  
> Der Kern der PCB-X-Ray-Inspektion ist nicht, ein klares Bild zu erzeugen. Entscheidend ist, im Voraus festzulegen, welche Packages geprüft werden müssen, welche Hidden-Joint-Risiken pro Package relevant sind, wie Bildbefunde in den Prozess zurückgeführt werden und wie das Ergebnis in die Traceability-Kette eingeht. Bei BGA-, BTC- und reliability-kritischen PCBA ist X-Ray ein Prozesskontrollwerkzeug und nicht nur ein Abnahmeschritt.

## Inhaltsverzeichnis

- [Was sollte man bei PCB-X-Ray-Inspektion zuerst prüfen?](#overview)
- [Wichtige Regeln und Parameterübersicht](#rules)
- [Welche Produkte und Package-Typen sollten X-Ray in die Routinekontrolle aufnehmen?](#scope)
- [Nach welchen Defekten und Signalen sollte X-Ray tatsächlich suchen?](#defects)
- [Warum ist der größte Wert von X-Ray die Prozessrückführung und nicht die Bildaufnahme?](#process)
- [Warum müssen Sampling-Strategie und Traceability-Kette gemeinsam entworfen werden?](#sampling)
- [Nächste Schritte mit HILPCB](#next-steps)
- [FAQ](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfinformationen](#author)

<a id="overview"></a>
## Was sollte man bei PCB-X-Ray-Inspektion zuerst prüfen?

Zuerst **Package-Typ, Hidden-Joint-Risiko, Defektinterpretationslogik, Sampling-Strategie und Traceability-Methode**.

Es geht dabei weder nur darum, ob die Maschine ein Bild erzeugen kann, noch darum, ob die Void-Rate einen einzelnen Grenzwert überschreitet. IPC-7095E für BGA und IPC-7093 für Bottom Termination Components verankern Design- und Assembly-Process-Guidance in ihrem öffentlichen Scope. IPC hat in der J-STD-001J-Release-Meldung außerdem hervorgehoben, dass zusätzliche Illustrationen zu Bubbles in X-Ray-Bildern ergänzt wurden. Zusammengenommen zeigen diese öffentlichen Fakten bereits, dass X-Ray Design, Assembly, Inspection und Reliability unterstützen soll und nicht nur eine bildbasierte Gut-/Schlecht-Entscheidung.

Was man typischerweise vor dem Pilot einfrieren sollte:

- **welche Packages und welche Lots Teil der Routine-X-Ray-Kontrolle sein müssen**
- **welche Hidden-Joint-Risiken für jede Package-Familie relevant sind**
- **ob die Bewertung auf Voiding, Wetting, Bridging, Offset oder Konsistenz fokussiert**
- **wie die Sampling-Dichte sich bei neuen Packages, neuen Prozessfenstern und unterschiedlichen Risikostufen ändert**
- **wie Bilder, Bewertungen und Prozessdaten in die Traceability-Kette eingehen**

Bei Projekten mit vielen verdeckten Lötstellen ist es meist sinnvoll, die Prozessfenster von [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) und [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) gleichzeitig zu prüfen, statt Inspektionsstrategie und Assembly-Strategie auseinanderlaufen zu lassen.

<a id="rules"></a>
## Wichtige Regeln und Parameterübersicht

| Regel / Parameter | Empfohlener Ansatz | Warum wichtig | Wie verifizieren | Risiko bei Ignorieren |
| --- | --- | --- | --- | --- |
| Prüfungsumfang | Zuerst definieren, welche Package-Typen und welche Ausfallkostenfälle X-Ray verlangen | Hochrisiko-Lötstellen sollten nicht erst nach Feldfehler geprüft werden | NPI-Review, Package-Liste, Qualitätsplan | Kritische Hidden-Joint-Risiken werden übersehen |
| Bewertungsfokus | Unterschiedliche Packages brauchen unterschiedliche Defektfoki und nicht nur Void-Betrachtung | BGA, BTC und QFN fallen nicht auf dieselbe Weise aus | First-Article-Bildreview, Package-Klassifizierung | Bilder sind da, Schlussfolgerungen sind schwach |
| Prozessrückführung | Jedes Bild muss auf Stencil, Paste, Pad und Reflow zurückgeführt werden können | Der Wert der Inspektion liegt in der Prozessverbesserung | Bilddaten mit Prozessparametern verknüpfen | Probleme werden gefunden, aber nicht verbessert |
| Sampling-Strategie | Sampling dynamisch an Risiko, Prozessänderung und Lot-Zustand anpassen | Starres Template-Sampling kann neues Risiko verdecken | First-Article- und Serien-Samplingplan | Hochrisiko-Änderungen werden verpasst |
| Traceability-Kette | Bild, Board-ID, Programm, Schicht und Bewertung gemeinsam archivieren | Notwendig für Fehleranalyse und Reklamationsbearbeitung | MES-/Log-Review, Lot-Bindung | Root Cause wird später zur Vermutung |
| Design-Abstimmung | Pad-Design, Via in Pad und Bottom-Pad-Öffnungen früh prüfen | Viele X-Ray-Befunde beginnen schon im Layout und Package-Design | DFM-Review, Package-Check | Assembly-Fenster erweist sich nach Bestückung als zu eng |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">Zuerst definieren, welche Packages und Lotsituationen Routine-X-Ray verlangen. Ohne Scope wird Inspektion reaktiv.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">Unterschiedliche Packages reagieren auf unterschiedliche Hidden-Joint-Defekte. Voiding, Bridging, Offset und Head-in-Pillow brauchen keine gemeinsame Vorlage.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">Wenn das Bild nicht auf Stencil, Solder Paste, Pad-Design und Reflow zurückgeführt werden kann, bleibt Yield-Verbesserung langsam.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">Ohne Board-ID, Lot, Programm und Bewertungsdaten sind X-Ray-Bilder eine schwache Stütze für Reklamationen und Fehleranalyse.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Welche Produkte und Package-Typen sollten X-Ray in die Routinekontrolle aufnehmen?

Als Grundregel gilt: **Packages mit verdeckten Lötstellen, hohen Rework-Kosten, Bottom-Pad-Thermopfad oder hohen Feldfehlerkosten eignen sich am ehesten für Routine-X-Ray**.

IPC-7095E ist auf BGA ausgerichtet, IPC-7093 auf BTC / Bottom Termination Components. Allein das deutet schon darauf hin, dass diese Packages keine guten Kandidaten für Freigabe nur auf Basis von AOI oder optischer Sichtprüfung sind. Die praktischere Engineering-Frage lautet deshalb nicht "haben wir ein X-Ray-System?", sondern "können wir es uns leisten, eine schlechte Lötung dieses Packages erst im Funktionstest oder im Feld zu entdecken?"

Typische Kandidaten für Routine-X-Ray sind:

- **BGA, CSP und andere Hidden-Ball-Packages**
- **QFN, LGA und Bauteile mit großen freiliegenden Bottom Pads**
- **Power-Bauteile, bei denen Thermopfad und Joint-Konsistenz wichtig sind**
- **hochlagige, Fine-Pitch- oder dichte PCBA mit teurem Rework**
- **Automotive-, Medizin-, Industrie- und Kommunikationsboards mit höherem Reliability-Anspruch**

Wenn das Projekt bereits in Richtung Serienassembly geht, ist es meist besser, diese Packages direkt in die Vorkontrollliste für [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) oder [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) aufzunehmen, statt erst nach dem First Article zu entscheiden, "welche man jetzt prüfen sollte".

<a id="defects"></a>
## Nach welchen Defekten und Signalen sollte X-Ray tatsächlich suchen?

Weil **der eigentliche Zweck von X-Ray nicht darin liegt zu fragen "gibt es einen Void?", sondern die Hidden-Joint-Ausfallarten des jeweiligen Packages zu erkennen**.

BTC und BGA tragen nicht dieselben Risiken. Genau deshalb behandelt IPC sie in unterschiedlichen Standards. Bei BGA sind Wetting, Collapse, Offset, Bridging und Head-in-Pillow-artige Risiken oft relevanter. Bei BTC, QFN und großen Bottom-Pad-Bauteilen liegt der Fokus stärker auf Bottom-Joint-Verteilung, Void-Lage, Joint-Abdeckung und Konsistenz.

Die nützlichsten Beobachtungen sind typischerweise:

- **ob sich eine vernünftige, kontinuierliche Wetting-Geometrie gebildet hat**
- **ob Hidden Joints Bridging oder lokale Anomaliecluster zeigen**
- **ob Voids sich in kritischen thermischen oder mechanischen Bereichen konzentrieren**
- **ob dasselbe Bauteil im selben Lot eine auffällige Geometriestreuung zeigt**
- **ob eine lokale Anomalie auf Design-, Printing- oder Reflow-Verhalten zurückweist**

Wenn die Platine außerdem große Thermal Pads, komplexe Power-Bereiche oder hohe Wärmedichte trägt, lohnt sich auch die gemeinsame Review von Pad- und Wärmepfadstruktur mit [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb), statt X-Ray nur als Post-Assembly-Aktion zu behandeln.

<a id="process"></a>
## Warum ist der größte Wert von X-Ray die Prozessrückführung und nicht die Bildaufnahme?

Weil **die entscheidende Frage nicht lautet, dass es ein schlechtes Board gibt, sondern warum sich dieselbe Anomalie wiederholt**.

IPC-7093 und IPC-7095 sind beides Dokumente mit Fokus auf Design and Assembly Process Guidance und keine reinen Bildatlanten. Das bedeutet: Das Bild muss zusammen mit Stencil-Aperture-Strategie, Zustand der Solder Paste, Pad-Design, Via-in-Pad-Ausführung, Feuchtezustand der Bauteile und Reflow-Profil gelesen werden. Ohne diese Verknüpfung kann X-Ray nur sagen "hier ist ein Problem", aber nicht "warum dasselbe Problem immer wieder auftaucht".

Die Prozessfaktoren, die man am ehesten zurückverfolgen sollte, sind:

- **ob Stencil-Dicke und Aperture-Strategie zum Package passen**
- **ob Typ, Lot, Lagerung und Nutzung der Solder Paste stabil sind**
- **ob Pad-Design, Solder-Mask-Definition und Via-in-Pad-Ausführung geeignet sind**
- **ob das Reflow-Profil zu Bauteil und Board-Bedingungen passt**
- **ob Feuchtebelastung von Package oder PCB, Warpage oder Board-Form-Änderungen übersehen wurden**

Wenn sich das Projekt noch in Prototype oder Pilot befindet, ist es meist besser, diese Feedback-Schleifen zusammen mit [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) zu planen, statt X-Ray zu einem isolierten Sperrbericht zu machen.

<a id="sampling"></a>
## Warum müssen Sampling-Strategie und Traceability-Kette gemeinsam entworfen werden?

Weil **der Kontrollwert von X-Ray davon abhängt, wann geprüft wird, wie viel geprüft wird und ob das Ergebnis in den Prozess zurückverfolgt werden kann**.

Der öffentliche J-STD-001J-Kontext zeigt bereits, dass X-Ray-Bildinterpretation innerhalb der Assembly-Akzeptanz klarer formalisiert wird. In Engineering-Sprache heißt das: Eine Sampling-Strategie kann kein starres Template bleiben. Sie muss sich mit Package-Risiko, Prozessreife, Prozessänderung und Ausfallkosten verändern.

Ein robusterer Ansatz umfasst typischerweise:

1. **Die Prüfquote bei ersten Lots mit neuen Packages, neuen Stencils, neuer Paste oder neuen Reflow-Programmen erhöhen.**
2. **Fine-Pitch-BGA, große Bottom Pads und kritische Thermal-Bauteile höher priorisieren.**
3. **Sampling-Ergebnisse mit Board-ID, Schicht, Programm, Paste-Lot und Equipment-Einstellungen verknüpfen.**
4. **Eskalationsregeln für höhere Prüfdichte oder 100%-Prüfung festlegen, wenn sich Anomalien wiederholen.**
5. **Bildbewertung zusammen mit Korrekturmaßnahmen archivieren und nicht getrennt davon.**

Ohne Traceability-Kette unterstützen X-Ray-Bilder nur die momentane Entscheidung. Mit Traceability-Kette unterstützen sie Reklamationsbearbeitung, Fehleranalyse und kontinuierliche Prozessverbesserung. Für Projekte nahe an der Serie ist es meist besser, diese Erwartungen direkt in [Quote / RFQ](https://hilpcb.com/en/quote/) oder frühe Qualitätsanweisungen zu schreiben.

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie BGA, QFN, große Bottom-Pad-Bauteile oder ein anderes Projekt mit vielen verdeckten Lötstellen einführen, besteht der nächste Schritt meist darin, "Inspektion" in "Prozesskontroll-Input" zu übersetzen:

- Wenn Hidden-Joint-Assembly-Qualität das Hauptthema ist, zuerst kritische Packages und Kontrollpunkte in die Review von [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) einziehen.
- Wenn PCB-Fertigung, Beschaffung, Bestückung und Test als ein Prozess geschlossen werden müssen, über [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) die Workflow-Grenzen zusammenführen.
- Wenn das Board High-Heat-Density-Bauteile oder große Thermal Pads enthält, Pad- und Wärmepfadstruktur mit [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb) gegenprüfen.
- Wenn Package-Wahl, Pad-Design und Prozessfenster früh belegt werden müssen, diese Prüfpunkte zuerst in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) bringen.
- Wenn Scope, Sampling-Logik, Bewertungsmethode und Traceability-Erwartung definiert sind, den vollständigen Anforderungssatz in [Quote / RFQ](https://hilpcb.com/en/quote/) überführen.

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Geht es bei X-Ray-Inspektion hauptsächlich um die Void-Rate?

A: Nein. Voids sind nur eine Risikokategorie. Bei vielen Produkten sind Wetting, Bridging, Offset, Head-in-Pillow, Joint-Abdeckung und Lot-zu-Lot-Konsistenz genauso wichtig oder wichtiger.

### Welche Produkte sollten X-Ray in einen Routineprozess aufnehmen?

A: Produkte mit vielen verdeckten Lötstellen, hohen Rework-Kosten, Bottom-Pad-Thermopfad oder hohem Reliability-Anspruch sind die stärksten Kandidaten für Routine-X-Ray.

### Warum reicht AOI allein nicht aus?

A: Weil viele kritische Lötstellen unter dem Package-Körper liegen, wo AOI nichts sieht, und genau diese Stellen oft Thermopfade und Langzeitzuverlässigkeit bestimmen.

### Warum sehen manche Teams viele X-Ray-Bilder, verbessern den Prozess aber trotzdem nur langsam?

A: Der häufigste Grund ist, dass die Bilder nie mit Stencil, Solder Paste, Reflow, Pad-Design und Lot-Daten verknüpft wurden. So erkennt man Anomalien, schließt aber die Root Cause nicht.

### Was sollte man vor Produktionsstart am ehesten einfrieren?

A: Prüfungsumfang, Defektinterpretationslogik, Sampling-Strategie, Eskalationstrigger und Traceability-Kette zuerst einfrieren. Diese Entscheidungen formen die Langzeit-Qualitätskontrolle stärker als ein einzelnes Prüfergebnis.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   Belegt, dass IPC-7095E als Design- und Assembly-Process-Guidance für BGA gerahmt ist.

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   Belegt, dass IPC-7093 auf Bottom Termination Components ausgerichtet ist und X-Ray Usage, Repair und Reliability-nahe Kapitel enthält.

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   Belegt den öffentlichen Kontext, dass J-STD-001J ergänzende Illustration zu Bubbles in X-Ray-Bildern aufgenommen hat.

<a id="author"></a>
## Autoren- und Prüfinformationen

- Autor: HILPCB Content-Team für PCBA-Qualität
- Technische Prüfung: Engineering-Team für Assembly-Prozess, Inspektion und Reliability
- Letzte Aktualisierung: 2025-11-19

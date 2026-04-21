---
title: "Was bei der Chiplet-Bridge-Substratmontage zuerst festgelegt werden muss: Bridge-Zone, Verzug, Underfill und gestufte Tests"
description: "Praxisleitfaden zu den ersten Punkten, die bei der Montage von Chiplet-Bridge-Substraten eingefroren werden sollten, darunter Bridge-Zonen-Geometrie, Verzug, Underfill, Inspektion und Thermozyklus-Strategie für UCIe- und EMIB-Projekte."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["chiplet packaging", "Bridge substrate", "Advanced packaging assembly", "UCIe", "EMIB", "Underfill"]
---

# Was bei der Chiplet-Bridge-Substratmontage zuerst festgelegt werden muss: Bridge-Zone, Verzug, Underfill und gestufte Tests

- **Die erste Frage bei Chiplet-Bridge-Substraten ist nicht die Leitungsdichte, sondern ob die Bridge-Zone ein wiederholbares Montagefenster hat.** Die UCIe-Spezifikationen definieren UCIe als offenen Package-Level-Standard für Die-to-Die-Interconnect mit Physical Layer, Protocol Stack, Software Stack und Compliance Testing.
- **Eine Bridge-Struktur ist nicht einfach ein dichteres BGA-Substrat.** Intel beschreibt EMIB als kleinen, in das Substrat eingebetteten Silizium-Bridge-Chip für ultra-hochdichte Die-to-Die-Verbindungen ohne vollflächigen Silizium-Interposer.
- **Ein Muster, das hochfährt, ist noch kein serientauglicher Prozess.** Intel Foundry führt Wafer Sort, Die Sort, Burn-in, Final Test und System Level Test als getrennte Stufen auf. Genau das zeigt, dass Fehler schichtweise ausgesiebt werden müssen.
- **Bridge-Zone, Underfill, Thermozyklen und Fehler-Rückverfolgbarkeit müssen gemeinsam bewertet werden.** Das teuerste Risiko ist meist nicht der Totalausfall, sondern schleichende Instabilität unter thermo-mechanischer Last ohne saubere Root-Cause-Spur.
- **Ein stabiles Bridge-Substrat ist kein einzelnes Muster, das läuft, sondern ein Bridge-Bereich, Materialaufbau, Assembly-Flow und Testkonzept, die über mehrere Lots reproduzierbar bleiben.**

> **Quick Answer**  
> Im Kern geht es bei der Chiplet-Bridge-Substratmontage darum, lokale Bridge-Struktur, Bestückreihenfolge, Underfill-Prozess, Verzugsbeherrschung und gestufte Tests in ein gemeinsames, wiederholbares Fertigungsfenster zu bringen. Für UCIe- und EMIB-Projekte zählt nicht, ob ein Sample startet, sondern ob sich die Bridge-Zone reproduzierbar montieren, prüfen, zurückverfolgen und nach Thermozyklen stabil halten lässt.

## Inhaltsverzeichnis

- [Was sollte bei einem Chiplet-Bridge-Substrat zuerst geprüft werden?](#overview)
- [Wichtige Regeln und Parameterübersicht](#rules)
- [Warum muss das Substratdesign um das Montagefenster der Bridge-Zone aufgebaut werden?](#bridge-window)
- [Warum müssen Verzug, Underfill und Thermozyklen als ein Problem behandelt werden?](#warpage-underfill)
- [Warum sollten Known Good Die, gestufte Tests und Rückverfolgbarkeit früh geplant werden?](#kgd-test)
- [Wie validiert man die Montage von Chiplet-Bridge-Substraten vor Serienanlauf?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [FAQ](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfinformationen](#author)

<a id="overview"></a>
## Was sollte bei einem Chiplet-Bridge-Substrat zuerst geprüft werden?

Zuerst **Bridge-Zone, lokale Ebenheit, Verzug, Underfill, gestufte Tests und Thermozyklus-Validierung**.

Es geht hier nicht einfach darum, mehr Signale in weniger Fläche zu pressen. UCIe betrachtet Package-Level-Interconnect, Software-Modell und Compliance Testing als zusammengehöriges System. Die öffentlichen EMIB-Unterlagen von Intel machen klar, dass die Kopplung über eine kleine, eingebettete Silizium-Bridge erfolgt. Intel Foundry zeigt zusätzlich die Trennung in Die Sort, Burn-in, Final Test und System Level Test.

Eine belastbare frühe Review-Reihenfolge ist deshalb meist:

1. **Prüfen, ob Geometrie, Bestückfolge und lokale Ebenheit der Bridge-Zone in einem reproduzierbaren Fenster liegen.**
2. **Verzug, Underfill-Fluss und Aushärtespannung gemeinsam mit der Bridge-Zone bewerten.**
3. **Sicherstellen, dass Teststufen Die-Fehler von Montagefehlern in der Bridge-Zone trennen können.**
4. **Thermozyklen und Fehleranalyse von Anfang an in den Pilotplan aufnehmen.**
5. **Inspektionspunkte, Schliffmuster und Lot-Traceability vor dem Anlauf definieren.**

Wenn das Design bereits einen ultradichten Bridge-Bereich mit Microvias und Fine-Pitch-Strukturen enthält, sollte man die Fertigungsgrenzen von [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) und [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) früh in die Bewertung einbeziehen.

<a id="rules"></a>
## Wichtige Regeln und Parameterübersicht

| Regel / Parameter | Empfohlener Ansatz | Warum wichtig | Wie verifizieren | Risiko bei Ignorieren |
|---|---|---|---|---|
| Bridge-Zone-Fenster | Lokale Geometrie und Ebenheit separat prüfen | Höchstes Risiko liegt lokal, nicht im Flächenmittel | Strukturreview, lokale Sichtprüfung, Coplanarity | Erstmuster funktionieren, Pilotserie streut stark |
| Verzugsbeherrschung | Board-Form nach Laminieren, Platzieren, Underfill und Reflow verfolgen | Mehrmaterial-Strukturen reagieren stark auf Verzug | Warpage-Tracking, Prozessvergleich | Yield bricht zuerst bei Coplanarity und Bridge-Placement ein |
| Underfill-Verhalten | Flussvollständigkeit, Voids und Cure Stress prüfen | Underfill kann schützen, aber auch neue Spannung eintragen | X-Ray, Schliff, Vorher/Nachher-Thermozyklus | Frühe Muster ok, Lebensdauer driftet |
| Gestufte Tests | Die-Test, Assembly-Test und Systemtest trennen | Trennt Die-Fehler schnell von Bridge-Fehlern | Die Sort, Burn-in, Final Test, SLT | Root Cause wird vermischt |
| Rückverfolgbarkeit | Materiallots, Reflow-Historie, Underfill und Samples verknüpfen | Viele Bridge-Defekte sind versteckt | Lot-Daten, Sample-ID, FA-Flow | Fehler lassen sich kaum rekonstruieren |
| Thermozyklus-Validierung | Thermozyklus als Hauptpfad behandeln | Lebensdauerrisiko ist oft thermo-mechanisch getrieben | Thermozyklen, Schliffe, Strukturvergleich | Bring-up gut, Haltbarkeit instabil |

| Projektszenario | Typischer Montagefokus |
|---|---|
| UCIe-Bridge auf Package-Level | Bridge-Ausrichtung, lokale Ebenheit, Teststufung |
| EMIB-ähnliche Embedded-Bridge | Substrat-Cavity, Spannungen an der Bridge, Underfill und Inspektion |
| Multi-Die / Multi-Chiplet-Substrat | Bestückreihenfolge, Last auf der Bridge, Thermozyklen, Lot-Traceability |

<div style="background: linear-gradient(135deg, #eef2fb 0%, #f7f0ea 100%); border: 1px solid #dcdfee; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #6d59a0; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #56457f; font-weight: 700;">Bridge Zone Is the Real Product</div>
      <div style="margin-top: 8px; color: #2f2941;">Bei Bridge-Substraten ist nicht die Durchschnittsqualität der ganzen Fläche das eigentliche Prozessziel, sondern ob die Bridge-Zone lokal montierbar, prüfbar und reproduzierbar bleibt.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6849; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b5239; font-weight: 700;">Warpage Comes Early</div>
      <div style="margin-top: 8px; color: #382e24;">Mit dünnen Substratkernen, gemischten Materialien und lokaler Hochdichte wird Verzug oft früher zum Yield-Killer als die Elektrik.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4d7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a5f51; font-weight: 700;">Underfill Is a Reliability Process</div>
      <div style="margin-top: 8px; color: #23342d;">Underfill ist kein kosmetischer Schritt, sondern ein Zuverlässigkeitsprozess. Unvollständiger Fluss oder falscher Cure Stress verkürzen die Lebensdauer direkt.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7393; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38586f; font-weight: 700;">Testing Must Be Layered</div>
      <div style="margin-top: 8px; color: #243440;">Ohne getrennte Die-, Package- und Systemtests lassen sich Bridge-Defekte später kaum sauber von Die-Defekten abgrenzen.</div>
    </div>
  </div>
</div>

<a id="bridge-window"></a>
## Warum muss das Substratdesign um das Montagefenster der Bridge-Zone aufgebaut werden?

Weil **die Bridge-Zone der empfindlichste, am wenigsten reproduzierbare und zuerst ausfallende lokale Bereich des gesamten Substrats ist**.

Intel beschreibt EMIB öffentlich als kleinen Silizium-Bridge-Chip, der im Substrat eingebettet ist und die hochdichte Verbindung zwischen Dies übernimmt. Genau diese Architektur verschiebt den Fokus vom Flächenmittel auf das lokale Prozessfenster der Bridge.

Früh zu klären sind vor allem:

- **Verstärkt die lokale Kupferverteilung um die Bridge mechanische Spannung?**
- **Trägt die Bestückfolge zusätzliche thermische Historie in die Bridge-Zone ein?**
- **Reichen Ebenheit und Coplanarity nahe der Bridge für wiederholbare Montage aus?**
- **Bleiben Microvia-, Pad- und Cavity-Randstrukturen im realen Prozessfenster?**

Wenn die Bridge-Zone nicht als eigener Prozessgegenstand behandelt wird, scheitern Pilotbauten selten spektakulär. Häufiger wird das Fenster einfach extrem schmal und stark vom manuellen Nachstellen abhängig. Deshalb lohnt es sich meist, [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) und [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) schon in der Konzeptphase einzubeziehen.

<a id="warpage-underfill"></a>
## Warum müssen Verzug, Underfill und Thermozyklen als ein Problem behandelt werden?

Weil **das Lebensdauerrisiko auf Bridge-Substraten selten aus einem Einzelereignis entsteht. Meist ist es das Ergebnis kumulierter thermischer Historie und Materialspannungen.**

Bridge-Substrate durchlaufen typischerweise Laminieren, bridgebezogene Assembly-Schritte, Die Attach, Underfill, Reflow und weitere thermische Tests. Jeder Schritt kann den lokalen Spannungszustand verändern. Underfill hilft nicht automatisch. Er kann Spannungen verteilen, aber unvollständiger Fluss, hoher Void-Anteil oder falscher Cure-Mismatch schaffen neue Fehlerquellen.

Deshalb sollten mindestens diese Punkte gemeinsam bewertet werden:

1. **Lokale Verzugsänderung vor und nach dem Underfill**
2. **Integrität der Bridge-Zone vor und nach dem Thermozyklus**
3. **Ob Voids, Kontamination oder schlechter Fluss in dichten Bereichen konzentriert sind**
4. **Ob nach Thermozyklen neue Risse oder Delaminationssignale auftreten**

Wer Underfill nur optisch bewertet und nicht mit Thermozyklusdaten und Bridge-Struktur verknüpft, überschätzt die Lebensdauer fast immer. Bei Engineering Samples sollte dieser Prüfpfad früh an den [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) gekoppelt werden.

<a id="kgd-test"></a>
## Warum sollten Known Good Die, gestufte Tests und Rückverfolgbarkeit früh geplant werden?

Weil **der teuerste Fehler im Advanced Packaging nicht der Defekt selbst ist, sondern der Verlust der Fähigkeit, Die-, Bridge- und Prozessprobleme sauber auseinanderzuhalten**.

Intel Foundry führt im Advanced-Chiplet-Test öffentlich Wafer Sort, Die Sort, Burn-in, Final Test und System Level Test auf und betont die Lieferung von Known Good Die vor der Endmontage. Für Bridge-Substrate heißt das praktisch:

- **Tests müssen gestuft werden und dürfen sich nicht auf das finale Einschalten beschränken**
- **Die Sort und Known Good Die reduzieren Störrauschen in der Fehleranalyse**
- **Burn-in und Systemtests decken grenzwertige thermo-mechanische Fehler besser auf**
- **Lot-Traceability und Sample-Verknüpfung müssen vor dem Pilotlauf existieren**

Ohne diese Grundlagen zeigen sich spätere Fehler oft als sporadische Muster-Ausfälle, vereinzelte Thermozyklus-Anomalien oder Lot-zu-Lot-Unterschiede, ohne dass klar wird, ob Die, Bridge, Underfill oder Assembly-Historie die Ursache waren. Wenn das Produkt später mit einem Server- oder Accelerator-System zusammenspielt, hilft auch der Systemblick aus [Why AI Server Motherboards Can Power Up but Still Fail in Production](/code/blogs/blogs/1119-1-ccc/de/ai-server-motherboard-reliability.md).

<a id="validation"></a>
## Wie validiert man die Montage von Chiplet-Bridge-Substraten vor Serienanlauf?

Das eigentliche Ziel ist, **Bridge-Zone, Underfill, Thermozyklen und Lot-Konsistenz in einer geschlossenen Validierungskette zusammenzubringen**.

Ein belastbarer Validierungspfad enthält meist:

| Validierungspunkt | Hauptfrage | Empfohlene Beobachtung |
|---|---|---|
| Lokale Struktur- / Coplanarity-Prüfung | Liegt die Bridge-Zone im Montagefenster? | Ebenheit um die Bridge, lokale Board-Form, Platzierzustand |
| X-Ray / Schliff | Sind Underfill und versteckte Strukturen vollständig? | Voids, Flussvollständigkeit, Defektschwerpunkte |
| Vorher-/Nachher-Vergleich nach Thermozyklus | Bleibt die Bridge-Zone unter Lebensdauerstress stabil? | Risse, Delamination, optische und elektrische Drift |
| Gestufte Tests | Lassen sich Die-, Montage- und Systemeffekte trennen? | Auffälligkeiten in Die Sort, Burn-in, Final Test und SLT |
| Multi-Lot-Vergleich | Ist das Prozessfenster breit genug für Serie? | Board-to-Board-Streuung, Parameterdrift, Lot-Signaturen |

Wenn das Projekt bereits auf die Pilotserie zuläuft, sollten diese Checks direkt in den Fertigungs- und Testplan geschrieben werden. Sobald Bridge-Fenster, Underfill-Verhalten, Thermozyklus-Nachweise und Teststufung sauber stehen, lässt sich der Anforderungssatz deutlich sauberer in eine [Quote / RFQ](https://hilpcb.com/en/quote/) überführen.

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie an einem UCIe-, EMIB- oder anderen Chiplet-Bridge-Substrat arbeiten, ist der nächste sinnvolle Schritt meist, "Advanced Packaging Assembly" in fertigungstaugliche Eingaben zu übersetzen:

- Wenn Bridge-Zone, Microvias und lokale Feinstrukturen das Hauptthema sind, zunächst mit [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) und [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) die lokalen Prozessgrenzen schließen.
- Wenn der Pilotlauf vor allem Bridge-Fenster, Verzug und Underfill verifizieren soll, diese Punkte früh in die [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) Review nehmen.
- Wenn Lot-Konsistenz und Fehlerrekonstruktion wichtig sind, Schliffe, X-Ray, Materiallots und Parameter-Traceability von Anfang an definieren.
- Wenn Bridge-Fenster, Teststufen und Thermozyklus-Anforderungen stabil sind, das Gesamtpaket in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) oder [Quote / RFQ](https://hilpcb.com/en/quote/) überführen.

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Ist Routing-Dichte die Hauptschwierigkeit bei Chiplet-Bridge-Substraten?

Nicht allein. Schwieriger sind meist das lokale Montagefenster der Bridge-Zone, Verzug, Underfill, Thermozyklen und die gestufte Testlogik.

### Warum machen EMIB-ähnliche Strukturen die Montage empfindlicher?

Weil EMIB eine kleine, im Substrat eingebettete Silizium-Bridge für ultra-dichte lokale Verbindungen nutzt. Dadurch werden lokale Ebenheit, Bestückfolge, Brückenspannungen und Underfill kritischer.

### Verbessert Underfill die Zuverlässigkeit automatisch?

Nein. Unvollständiger Fluss, Voids oder ungünstige Aushärtungsspannungen können selbst neue Fehlerquellen erzeugen.

### Warum Teststufung und Rückverfolgbarkeit so früh planen?

Weil viele Defekte auf Bridge-Substraten versteckte Defekte sind. Ohne getrennte Die-, Package- und Systemtests plus Lot-Traceability wird Root Cause langsam und unscharf.

### Was sollte vor Fertigung oder Pilotlauf zuerst eingefroren werden?

Zuerst Bridge-Zonen-Montagefenster, Verzugsstrategie, Underfill-Strategie, Teststufung, Thermozyklus-Validierung und Fehler-Rückverfolgbarkeit festlegen.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [Specifications | UCIe Consortium](https://www.uciexpress.org/specifications)  
   Grundlage für die Aussagen zu UCIe als offenem Package-Level-Die-to-Die-Standard mit Physical Layer, Protocol Stack, Software Stack und Compliance Testing.

2. [Intel® Stratix® 10 FPGAs Overview - Intel EMIB Packaging Technology](https://www.intel.com/content/www/us/en/products/details/fpga/stratix/10/article.html)  
   Grundlage für die Aussage, dass EMIB einen kleinen, in das Substrat eingebetteten Silizium-Bridge-Chip ohne großflächigen Silizium-Interposer nutzt.

3. [Advanced Packaging Innovations | Intel Foundry Packaging](https://www.intel.com/content/www/us/en/foundry/packaging.html)  
   Grundlage für die Diskussion über gestufte Advanced-Chiplet-Tests mit Wafer Sort, Die Sort, Burn-in, Final Test, System Level Test und Known Good Die vor der Endmontage.

4. [EMIB Technology Brief | Intel](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf)  
   Ergänzt die Aussagen zu eingebetteten Bridge-Strukturen in Substrat-Cavities, standardnahen Package-Assembly-Flows und lokal engerem Microbump-Pitch.

<a id="author"></a>
## Autoren- und Prüfinformationen

- Autor: HILPCB Content-Team für Advanced Packaging und High-Density Assembly
- Technische Prüfung: Engineering-Team für PCB-Prozess, Assembly, Thermo-Mechanik und Failure Analysis
- Letzte Aktualisierung: 2025-11-19

---
title: "Worauf es bei der GaN-Leistungsstufen-PCB-Bestückung ankommt: Schleifeninduktivität, Thermalpads und Serienkonsistenz"
description: "Eine direkte Antwort zu Leistungsschleife, Kelvin-Source, Voids im Thermalpad, dickem Kupfer und Verifikationsmethoden, die bei der GaN-Leistungsstufen-PCB-Bestückung zuerst geprüft werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["GaN power PCB", "Power electronics PCB", "Thermal management", "PCB assembly", "GaN half bridge", "Kelvin source"]
---

# Worauf es bei der GaN-Leistungsstufen-PCB-Bestückung ankommt: Schleifeninduktivität, Thermalpads und Serienkonsistenz

- **Bei GaN gerät meist nicht zuerst das Bauteil außer Kontrolle, sondern die parasitäre Induktivität und der Wärmepfad auf der Platine.**
- **Ein "richtiges Layout" muss sich in einem fertigungstauglichen Stackup bewähren, nicht nur im CAD gut aussehen.**
- **Thermalpads und Vias sind keine Nebensache, sondern zentrale Prozessvariablen.**
- **Dickes Kupfer und große Kupferflächen bringen Nutzen, verändern aber auch Ätzen, Planheit und Reflow-Fenster.**
- **GaN-Validierung darf nicht bei einem schönen Wellenscreenshot enden.**

> **Quick Answer**  
> Der Kern der GaN-Leistungsstufen-PCB-Bestückung ist nicht nur das Auflöten der Bauteile, sondern das gleichzeitige Umsetzen einer Schleife mit niedriger Induktivität, eines stabilen Gate-Rückwegs, einer thermisch wirksamen Pad-Struktur und eines reproduzierbaren Montagefensters. Serienreif ist eine GaN-Platine erst dann, wenn Wellenform, Wärme, Lötqualität und Chargenkonsistenz gemeinsam stabil bleiben.

## Inhaltsverzeichnis

- [Was sollte man bei der GaN-Leistungsstufen-PCB-Bestückung zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum reagieren GaN-Platinen so empfindlich auf parasitäre Induktivität und unkontrollierte Rückwege?](#loop-control)
- [Warum müssen Thermalpads, VIPPO und dickes Kupfer gemeinsam bewertet werden?](#thermal-pads)
- [Warum müssen Gate-Drive-Layout und Bestückungskonstanz zusammen betrachtet werden?](#gate-drive)
- [Wie sollte man GaN-Bestückung vor der Serie validieren?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei der GaN-Leistungsstufen-PCB-Bestückung zuerst prüfen?

Zuerst **Hauptleistungsschleife, Gate-Schleife, Kelvin-Source-Pfad, Thermalpad-Struktur und Verifikationsmethode**.

Das ist nicht einfach "etwas höhere Schaltfrequenz". EPC zeigt klar, dass bei höherer Geschwindigkeit und Leistungsdichte die parasitäre Induktivität in Leistungs- und Gate-Schleife minimiert werden muss. Empfohlen wird oft die erste Innenlage als Rückstrompfad, sodass Top-Layer-Strompfad und Rückstromebene die kleinste physische Schleife bilden.

Eine robuste Reihenfolge ist meist:

1. **Die reale physische Beziehung zwischen Halbbrücke und Zwischenkreiskondensator prüfen**
2. **Sicherstellen, dass die Rückstromebene direkt unter den Bauteilen schließt**
3. **Kelvin Source und Gate-Return auf Geometrie und Entkopplung prüfen**
4. **Thermalpad, Via-Struktur und Kupferdicke gemeinsam für Löten und Kühlung bewerten**
5. **Wellenformprüfung, Röntgen und Thermik als gemeinsame Vorserien-Gates definieren**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Beurteilung | Warum wichtig | Wie prüfen | Wenn ignoriert |
|---|---|---|---|---|
| Hauptleistungsschleife | Top-Strompfad eng an erste Rückstrom-Innenlage koppeln | Bestimmt Overshoot, Ringing und EMI | Layoutreview, Doppelimpulstest | Größerer Overshoot, schlechteres Schalten |
| Gate-Schleife | ON/OFF-Widerstände, Treiber-Rückweg und Gate/Source kompakt halten | GaN reagiert stark auf Gate-Parasiten | Gate-Wellenform, False-Turn-On-Prüfung | Fehlansteuerung und höhere Bauteilbelastung |
| Kelvin Source | Nah am Source-Pad und vom Leistungspfad entkoppelt | Reduziert common source inductance | Geometrieprüfung, Wellenformvergleich | Referenzpunkt des Treibers wird verschmutzt |
| Thermalpad und Vias | Erst Pad-Lötung, dann Via-Lage und Anzahl bewerten | Beeinflusst Wärme und Lötfenster | Röntgen, Temperaturtest, Schliff | Höhere Wärmewiderstände und instabile Lötung |
| Kupferdicke und Verteilung | Dickes Kupfer nur zusammen mit Rückstrom und Verzug betrachten | Senkt Widerstand, verändert aber den Prozess | Stackupreview, Reflow-Konsistenz, Planheit | Verzug, ungleichmäßige Erwärmung |
| Validierungsstrategie | Wellenform, Wärme, Lötung und Mehrplatinen-Konsistenz gemeinsam prüfen | GaN-Probleme sind oft kombinierte Fehlanpassungen | DPT, Thermografie, Röntgen, Chargenvergleich | Demo gut, Serie instabil |

<div style="background: linear-gradient(135deg, #eef3f8 0%, #f7f2ea 100%); border: 1px solid #d8dde5; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4f79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3b5d7d; font-weight: 700;">Loop First</div>
      <div style="margin-top: 8px; color: #243746;">Bei GaN zählt zuerst der reale Schließpfad von Leistungs- und Gate-Schleife. Ohne niedrige parasitäre Schleife werden gute Bauteilparameter sofort durch Overshoot und Ringing aufgezehrt.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #7b6346; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #624e38; font-weight: 700;">Kelvin Matters</div>
      <div style="margin-top: 8px; color: #352c23;">Kelvin Source ist keine Zierde im Layout. Wird der Treiber-Referenzpunkt vom Leistungspfad beeinflusst, kippt das Gate-Verhalten von kontrollierbar zu schwer reproduzierbar.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4c7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395e51; font-weight: 700;">Thermal Pad Is Process Logic</div>
      <div style="margin-top: 8px; color: #23352e;">Thermalpad, VIPPO, Schablonenöffnung und dickes Kupfer müssen gemeinsam definiert werden. Funktioniert der Wärmepfad nur in der Simulation, bleiben Temperaturanstieg und Lötqualität in der Serie nicht stabil.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #8d5a5a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #704646; font-weight: 700;">Production Beats Demo</div>
      <div style="margin-top: 8px; color: #3d2626;">Erfolg bei GaN heißt nicht ein schönes Demo-Board, sondern stabile Kontrolle von Overshoot, Wärme und Lötqualität über mehrere Boards und Chargen hinweg.</div>
    </div>
  </div>
</div>

<a id="loop-control"></a>
## Warum reagieren GaN-Platinen so empfindlich auf parasitäre Induktivität und unkontrollierte Rückwege?

Fazit: **Weil die hohe Schaltgeschwindigkeit von GaN selbst kleine parasitäre Induktivitäten direkt in sichtbare Spannungsspitzen und Gate-Probleme umsetzt.**

EPC betont, dass die erste Innenlage als Leistungsrückweg dienen sollte und dass der Zwischenkreiskondensator so platziert wird, dass sich die Hauptschleife direkt unter den Bauteilen schließt. Mit dem sogenannten inner vertical layout kann der Overshoot gegenüber einem Referenz-Si-MOSFET-Layout um etwa **40%** sinken.

Entscheidend ist nicht nur eine breite Leiterbahn, sondern dass auf der realen Platine gleichzeitig gilt:

- Der Strompfad zwischen Bus-Kondensator und Halbbrücke ist kurz
- Die Rückstromebene liegt direkt unter dem Leistungspfad
- Die Gate-Schleife bleibt von der Leistungsschleife getrennt
- Die Kelvin-Source-Referenz bleibt nahe am echten Source-Rückweg

<a id="thermal-pads"></a>
## Warum müssen Thermalpads, VIPPO und dickes Kupfer gemeinsam bewertet werden?

Fazit: **Weil Wärmeprobleme und Lötprobleme bei GaN oft aus demselben Pad und derselben Kupfer-/Via-Struktur entstehen.**

EPC AN031 zeigt konkrete Zahlen:

- Ohne Vias liegt Rtheta,JMA bei etwa **45 K/W**
- Mit seitlichen Vias bei etwa **35 K/W**
- Mit **VIPPO** unter dem Bauteil bei etwa **30 K/W**

Außerdem kann die thermische Resistenz durch kombinierte Optimierungen um fast **30%** sinken, wobei Vias unter dem Bauteil und **2 oz** Kupfer zu den wirksamsten Maßnahmen zählen. Das bedeutet:

- **Via-Positionen im Thermalpad** beeinflussen Wärme und Pastenverhalten
- **Mehr Kupferdicke** verbessert die Wärmeverteilung, verändert aber Reflow und Planheit
- **Bauteilabstand und Bus-Cap-Lage** beeinflussen sowohl Elektrik als auch Co-Heating

<a id="gate-drive"></a>
## Warum müssen Gate-Drive-Layout und Bestückungskonstanz zusammen betrachtet werden?

Fazit: **Weil die Gate-Schleife bei GaN nicht nur "irgendwie schalten" darf, sondern geometrisch und im Rückweg hochstabil sein muss.**

EPC empfiehlt, Leistungs- und Gate-Schleife möglichst orthogonal zu halten und den Kelvin-Rückweg des Treibers über Vias nahe am Source-Pad zu führen. Bei parallelen Bauteilen soll jedes GaN-FET einen eigenen Gate-Widerstand bekommen.

Direkte Montageanforderungen sind:

- Gate-Widerstände und Treiber dürfen sich durch Nacharbeit nicht unkontrolliert verschieben
- Kelvin Source und Treiber-Referenz dürfen nicht in Hochstromkupfer "mit hineingezogen" werden
- Kleine Widerstände, Sense- und Schutzbauteile am Treiber müssen kompakt und symmetrisch bleiben
- Bestandenes Röntgen oder Sichtprüfung heißt nicht automatisch, dass die Gate-Geometrie passt

<a id="validation"></a>
## Wie sollte man GaN-Bestückung vor der Serie validieren?

Fazit: **Serienvalidierung bei GaN muss Wellenform, Wärme und Lötqualität gemeinsam prüfen.**

Ein nützlicher Prüfpfad beantwortet meist diese Punkte:

| Validierungspunkt | Was beantwortet er? | Wichtige Beobachtungspunkte |
|---|---|---|
| Doppelimpuls- oder Schaltwellenformtest | Sind Haupt- und Gate-Schleife gesund? | Overshoot, Ringing, Abschaltverhalten, False-Turn-On |
| Thermischer Test | Funktionieren Thermalpad und Kupferstruktur wirklich? | Stationärer Temperaturanstieg, Delta-T, Co-Heating |
| Röntgen / Lötprüfung | Sind Bottom-Pad und versteckte Lötstellen reproduzierbar? | Benetzung, Void-Verteilung, Pastenfreigabe |
| Mehrplatinenvergleich | Ist das Prozessfenster breit genug? | Streuung von Wellenform und Temperatur |
| Planheits- und Struktur-Retest | Erzeugt dickes Kupfer Montage-Nebeneffekte? | Verzug, lokale Überhitzung, Nachbarlötungen |

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Wenn zuerst Thermalpad-Struktur, Kupferdicke und Wärmepfad eingefroren werden müssen, bietet sich [High Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb) an.
- Bei hohen Strömen und hohen Wärmestromdichten sollten Kupferdicke, Ätzfenster und Planheit zusammen mit [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb) geprüft werden.
- Vor Prototyp- oder Validierungsbuilds sollten Thermalpad-Design, Röntgenkriterien, Doppelimpulstests und Nacharbeitsgrenzen in die [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) Phase einfließen.
- Sobald Stackup, Bus-Cap-Lage, Thermalpads und Validierungspunkte stehen, sollten sie direkt in [Quote / RFQ](https://hilpcb.com/en/quote/) oder die Anforderungen für [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) aufgenommen werden.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Warum reagieren GaN-Leistungsstufen stärker auf Layout- und Montageabweichungen als MOSFET-Platinen?

Weil GaN schneller schaltet und kleine parasitäre Änderungen sofort zu Overshoot, Ringing und instabilem Gate-Verhalten führen.

### Braucht jede GaN-Platine dickes Kupfer?

Nicht unbedingt. Dickes Kupfer hilft elektrisch und thermisch, verändert aber auch Prozessfenster, Verzug und Reflow-Verhalten.

### Sind mehr Vias unter dem Thermalpad immer besser?

Nein. Via-Lage, VIPPO, Schablonenöffnung und Pad-Struktur müssen zusammen ausgelegt werden.

### Ist Röntgen bei GaN zwingend?

Bei Bottom-Thermalpads, verdeckten Lötstellen oder kritischen thermischen Interfaces ist Röntgen oft sehr wertvoll, weil viele Defekte optisch nicht sicher erkennbar sind.

### Warum kann ein einzelnes Musterboard gut aussehen, während die Serie scheitert?

Weil ein Muster nur zeigt, dass Design und Prozess einmal zusammen funktioniert haben. Serienfähigkeit bedeutet geringe Streuung über mehrere Boards und Lose.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [EPC GaN First Time Right: Schematic and Recommended Layout](https://epc-co.com/epc/design-support/gan-first-time-right/schematic-and-layout)  
   Stützt die Aussagen zu Leistungsschleife, Gate-Schleife, erster Innenlage als Rückweg und Kelvin Connection.

2. [EPC AN031: PCB Design Guidelines to Maximize Cooling of eGaN FETs](https://epc-co.com/epc/Portals/0/epc/documents/product-training/AN031_PCB_Design_Guidelines_to_Maximize_Cooling_of_eGaN_FETs.pdf)  
   Stützt die Daten zu VIPPO, Kupferdicke und thermischer Verbesserung.

3. [EPC2092 Datasheet](https://epc-co.com/epc/documents/datasheets/EPC2092_datasheet.pdf)  
   Stützt die Hinweise zu inner vertical layout, orthogonalen Schleifen und Kelvin Source.

4. [TI LMG3410R050 Datasheet](https://www.ti.com/lit/ds/symlink/lmg3410r050.pdf)  
   Stützt den Kontext zu Bottom-Thermalpad und empfohlenem Boardaufbau.

5. [TI E2E: LMG3410R050 Layout Modeling Problem of LMG3410](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/919688/lmg3410r050-layout-modeling-problem-of-lmg3410)  
   Stützt die Beziehung zwischen Thermalpad, Thermal Vias und empfohlenem Footprint.

6. [How to Design an eGaN FET-Based Power Stage with an Optimal Layout](https://epc-co.com/epc/home/post/15048/how-to-design-an-egan-fet-based-power-stage-with-an-optimal-layout)  
   Stützt den Kontext zu reduziertem Overshoot bei optimiertem Layout.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für Leistungselektronik und hochdichte Bestückung
- Technische Prüfung: Teams für PCB-Prozess, Thermik und Leistungshalbleiter
- Letzte Aktualisierung: 2025-11-18

---
title: "Wann sich VIPPO auf Optikmodul-PCBs lohnt: Wie man HDI-Escape, Pad-Ebenheit und Wärmeweg ausbalanciert"
description: "Eine direkte Antwort darauf, wann VIPPO auf Optikmodul-PCBs sinnvoll ist und wie es HDI-Escape-Routing, Pad-Ebenheit, SMT-Löten, Wärmewege und Serienvalidierung beeinflusst. So lässt sich beurteilen, ob das Verfahren wirklich den Aufwand wert ist."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO", "Optical module PCB", "HDI PCB", "High-speed PCB", "Via in pad plated over", "PCB assembly"]
---

# Wann sich VIPPO auf Optikmodul-PCBs lohnt: Wie man HDI-Escape, Pad-Ebenheit und Wärmeweg ausbalanciert

- **VIPPO gehört in dichte Bereiche, in denen das Via wirklich im Pad sitzen muss. Es ist kein Verfahren, das man nur aus Imagegründen über die ganze Platine zieht.**
- **Auf Optikmodul-PCBs liegt der Nutzen von VIPPO vor allem in mehr Escape-Raum, kürzerem vertikalem Übergang und besserem Wärmeeintrag in innere Kupferlagen.**
- **Das erste Risiko von VIPPO ist nicht der Preis, sondern der Verlust eines Pads, das sich wie ein wiederholbar lötbares Pad verhält.**
- **VIPPO muss auf Optikmodul-Boards immer zusammen mit HDI-Stackup, Microvia-Strategie, Impedanzpfad und Montagevalidierung bewertet werden.**
- **Die richtige Frage ist nicht "kann man es einmal herstellen?", sondern "kann man es in Muster, Pilot und Serie gleich herstellen?"**

> **Quick Answer**  
> VIPPO bedeutet via-in-pad plated over. Auf einem Optikmodul-PCB lohnt es sich nur dann, wenn normales HDI-Fanout nicht mehr wirtschaftlich oder ausreichend ist und gleichzeitig stabiles Löten sowie ein flacher Wärmeweg durch den Pad-Bereich gebraucht werden. Entscheidend sind Routing-Nutzen, Pad-Ebenheit, Montagefenster und Serienwiederholbarkeit, nicht das Etikett "fortschrittlicher Prozess".

## Inhaltsverzeichnis

- [Was sollte man bei VIPPO auf Optikmodul-PCBs zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum wird VIPPO nicht standardmäßig auf dem ganzen Optikmodul-Board eingesetzt?](#scope)
- [Warum lautet die eigentliche Fertigungsfrage nicht "kann das Loch gefüllt werden?", sondern "arbeitet das Pad danach noch wie ein normales Lötpad"?](#fabrication)
- [Warum müssen Montage und Thermik immer zusammen mit VIPPO bewertet werden?](#assembly-thermal)
- [Wie sollte ein VIPPO-Optikmodul-PCB vor der Serie validiert werden?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufige Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfinformationen](#author)

<a id="overview"></a>
## Was sollte man bei VIPPO auf Optikmodul-PCBs zuerst prüfen?

Zuerst **Pitch, Escape-Dichte, geforderte Pad-Ebenheit, HDI-Struktur, Wärmeweg und Montagevalidierung** prüfen.

Das ist nicht gleichbedeutend mit "High-End-Platinen sollten VIPPO haben", und auch nicht damit, dass jede Optikmodul-Platine automatisch via-in-pad braucht. IPC-4761 zeigt im öffentlichen Kontext, dass Via-Schutzmethoden dazu dienen, Fertigbarkeit bei akzeptabler Ausbeute und Kosten sicherzustellen und Vorteile sowie Risiken verschiedener Schutzarten abzuwägen. Auf einem Optikmodul-PCB sollte man deshalb zuerst fragen:

1. **Sind normale Dog-Bone-, Offset-via- oder Microvia-Fanouts bereits ausgeschöpft?**
2. **Muss das Via wirklich im SMD-Pad sitzen, damit das Routing überhaupt aufgeht?**
3. **Muss das Pad nach SMT besonders eben und gleichmäßig benetzbar bleiben?**
4. **Dient VIPPO hier SI/thermischen Zielen oder nur einer dichteren Optik im Layout?**
5. **Sind Schliffbild, X-Ray und Thermozyklus bereits im Musterplan vorgesehen?**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Sinnvolle Beurteilung | Warum wichtig | Wie prüfen | Folge bei Vernachlässigung |
|---|---|---|---|---|
| Einsatzbereich | VIPPO nur in dichten Escape-Zonen oder kritischen Thermalpads | VIPPO hat Wert, aber breite Nutzung erhöht Kosten und Montage-Risiko | Layout- und Dichte-Review | Kosten und Montageprobleme steigen gemeinsam |
| Pad-Ebenheit | Die lötbare Oberfläche nach Füllen, Capping und Planarisierung bewerten | Fine-Pitch-Gehäuse sind sehr sensibel auf Oberflächenkonsistenz | Schliffbild, Sichtprüfung, X-Ray, Erstlötung | Lötzinnabzug, starved joints, schlechtere Coplanarity |
| Via-Struktur | Immer zusammen mit HDI, Microvia und Sequential Lamination prüfen | VIPPO ist kein isoliertes Drill-Feature | Stackup-Review, Fertigungs-DFM | Routing funktioniert knapp, Prozessfenster bleibt eng |
| Wärmeweg | VIPPO nur dort für Wärme nutzen, wo lokale Wärme wirklich nach unten muss | Es hilft thermisch, ersetzt aber kein Gesamtkonzept | Thermalsimulation, Wärmebild, Boardvergleich | Lokaler Wärmepfad wird mit kompletter Thermik verwechselt |
| SMT-Interaktion | Schablonenöffnung, Pastenvolumen und Reflow-Profil gemeinsam bewerten | Die Pad-Struktur ändert das Montagefenster direkt | Erstbemusterung, X-Ray, Rework-Review | Muster lötbar, Serie schwankt |
| Serienvalidierung | Schliffbild, Thermozyklus und Multi-Board-Vergleich von Anfang an definieren | Zuverlässigkeitsprobleme sieht man nicht nur im CAD | Coupon, Thermozyklus, Mehrfachboards | Instabilität zeigt sich erst in der Pilotserie |

| Entscheidungsfrage | Eher geeignet für VIPPO | Eher ohne VIPPO |
|---|---|---|
| Fine-Pitch-BGA-Escape | Nachbarkanäle sind praktisch verschwunden | Normales Fanout reicht noch für Routing und Lagenwechsel |
| Wärmeabfuhr über Thermalpad | Lokale Wärme muss schnell in innere Kupferlagen gezogen werden | Wärme wird primär über Top-Copper oder externe Kühlteile gelöst |
| Doppelseitige Montage | Unbehandeltes via-in-pad würde starken Lötzinnabzug verursachen | Einseitige oder unkritische Pads tolerieren Offset-vias |
| Kosten / Prozessfenster | Das Projekt akzeptiert höhere Prozesskosten für Dichte und Pad-Stabilität | Kostenkritisch, andere HDI-Optionen reichen aus |

<div style="background: linear-gradient(135deg, #eef6f2 0%, #f7f1ea 100%); border: 1px solid #d7e1da; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #467566; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #35584d; font-weight: 700;">Density Is the Trigger</div>
      <div style="margin-top: 8px; color: #23342e;">VIPPO ist dann sinnvoll, wenn gewöhnliche Escape-Kanäle ausgereizt sind, nicht weil es "höherwertig" klingt.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6b48; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5238; font-weight: 700;">Pad Quality Is the Real Risk</div>
      <div style="margin-top: 8px; color: #392f26;">Die Schwierigkeit ist nicht nur das Füllen des Vias, sondern ein Pad zu erhalten, das nach Füllen, Capping und Planarisierung noch wie ein normales SMD-Land lötet.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4c7289; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395969; font-weight: 700;">HDI Context Matters</div>
      <div style="margin-top: 8px; color: #243640;">VIPPO muss zusammen mit Microvias, Sequential Lamination, Impedanzlagen und Lagenwechseln gelesen werden. Lokale Optimierung verschiebt das Risiko schnell in die Fertigung.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #93595f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #74474b; font-weight: 700;">Validate Before Scale</div>
      <div style="margin-top: 8px; color: #3d262a;">Serientauglichkeit von VIPPO beweist man mit Schliffbild, X-Ray, Thermozyklus und Multi-Board-Konsistenz, nicht mit einem gelungenen Einzelmuster.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Warum wird VIPPO nicht standardmäßig auf dem ganzen Optikmodul-Board eingesetzt?

Fazit: **Weil VIPPO ein Werkzeug für dichte Escapes und spezielle Pad-Probleme ist, kein allgemeines Upgrade für die ganze Platine.**

Altium beschreibt öffentlich, dass via-in-pad typischerweise dort auftaucht, wo die Bauteildichte so hoch wird, dass normale Fanout-Kanäle schnell verschwinden. Erst wenn Routing massiv in innere Lagen ausweichen muss, wird via-in-pad von "praktisch" zu "notwendig". Das passt gut zu Optikmodul-PCBs, weil DSPs, Retimer, Treiber und Steuer-BGAs oft in sehr kleinem Raum sitzen.

<a id="fabrication"></a>
## Warum lautet die eigentliche Fertigungsfrage nicht "kann das Loch gefüllt werden?", sondern "arbeitet das Pad danach noch wie ein normales Lötpad"?

Fazit: **Die Herausforderung von VIPPO ist nicht das Stopfen des Lochs, sondern ein ebenes, lötbares und wiederholbares Pad nach dem Füllen.**

IPC-4761 macht öffentlich klar, dass Via-Schutz mit Produktionsfragen, Langzeitzuverlässigkeit und Materialwahl verknüpft ist. Multi Circuit Boards beschreibt Type VII so, dass nach Füllen, Capping, Planarisierung und Metallisierung eine **flat and solderable** Oberfläche entstehen soll. Genau das macht diese Struktur für via-in-pad so relevant.

Auf der Fertigungsseite muss man daher vor allem beobachten:

- **bleiben Senken, Wölbungen oder lokale Unebenheiten nach dem Füllen zurück**
- **benetzt das planarisierte Pad beim Löten noch gleichmäßig**
- **passt das Surface Finish zur Pad-Struktur**
- **ist die Konsistenz zwischen benachbarten Pads ausreichend**

<a id="assembly-thermal"></a>
## Warum müssen Montage und Thermik immer zusammen mit VIPPO bewertet werden?

Fazit: **Weil VIPPO sowohl das Lötverhalten des Pads als auch den lokalen Wärmeeintrag in die Platine verändert.**

Altium weist öffentlich darauf hin, dass bei unzureichend gefülltem und planarisiertem via-in-pad Lötzinn in den Via-Barrel abgezogen werden kann, was zu abgesenkten oder starved joints führt. Ein sauber bearbeitetes VIPPO-Pad verhält sich deutlich näher an einem normalen SMD-Land. Gerade auf Optikmodul-PCBs ist das kritisch, weil dort häufig zusammenkommen:

- Fine-Pitch-BGA-/LGA-Gehäuse
- große Bottom-Thermalpads
- doppelseitige oder lokal sehr dichte Montage
- High-Speed-Kanäle, die empfindlich auf Rework-Qualität reagieren

<a id="validation"></a>
## Wie sollte ein VIPPO-Optikmodul-PCB vor der Serie validiert werden?

Fazit: **Sinnvolle Validierung beweist, dass das VIPPO-Pad nach Fertigung, Montage und Thermozyklus noch wie erwartet funktioniert.**

| Validierungspunkt | Welche Frage er beantwortet | Typische Beobachtungspunkte |
|---|---|---|
| Schliffbild / Coupon | Sind Füllen, Capping und Planarisierung stabil? | Pad-Topografie, Füllgrad, Lagenstruktur |
| Erstmuster-SMT + X-Ray | Gibt es Lötzinnabzug, hohe Voids oder ungleichmäßige Lötstellen? | BGA-/LGA-Lötstellen, Konsistenz, große Thermalpads |
| Wärmebild / Board-Thermotest | Verbessert VIPPO die lokale Wärmeverteilung wirklich? | Delta-T, Wärmeflussrichtung, stabiler Betrieb |
| Multi-Board-Vergleich | Ist das Prozessfenster breit genug? | Streuung im Löt- und Thermoverhalten |
| Nachprüfung nach Thermozyklus | Bleiben Pad- und Via-Struktur stabil? | Lötzustand, Schliffbildänderung, Retest-Konsistenz |

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie aktuell ein Optikmodul-Board, DSP-Control-Board oder ein anderes dichtes High-Speed-Subboard entwickeln, sollte der nächste sinnvolle Schritt aus "brauchen wir VIPPO?" konkrete Fertigungsvorgaben machen:

- Wenn das Hauptproblem Fine-Pitch-BGA-Escape und Lagenwechsel sind, zuerst über [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) definieren, welche Pad-Bereiche VIPPO wirklich brauchen.
- Wenn gleichzeitig High-Speed-Differenzkanäle vorhanden sind, das Stackup und die Übergangsstruktur von [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) parallel prüfen.
- Bereits in Prototype-/EVT-Phase Schliffbild, X-Ray, Wärmebild und Rework-Grenzen in die [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/)-Review aufnehmen.
- Sobald VIPPO-Bereiche, Finish, Montageprüfpunkte und Batch-Validierung klar sind, diese direkt in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) oder [Quote / RFQ](https://hilpcb.com/en/quote/) übernehmen.

<a id="faq"></a>
## Häufige Fragen (FAQ)

<!-- faq:start -->

### Was ist der Hauptunterschied zwischen VIPPO und gewöhnlichem via-in-pad?

VIPPO endet nicht beim Via im Pad. Das Via wird gefüllt, gecappt und planarisiert, damit das Pad sich wie ein normales SMD-Land verhält.

### Braucht jedes Optikmodul-PCB VIPPO?

Nein. VIPPO ist meist nur dann sinnvoll, wenn Fine-Pitch-Escape extrem eng wird oder lokale Thermalpads einen vertikalen Wärmeweg durch Pad-Vias wirklich benötigen.

### Ist das Hauptrisiko von VIPPO einfach nur der höhere Preis?

Nein. Der Preis ist nur die Folge. Das eigentliche Risiko ist Pad-Ebenheit und Montagekonsistenz.

### Kann VIPPO thermische Probleme allein lösen?

Nein. Es hilft beim lokalen Wärmeeintrag in innere Kupferlagen, ersetzt aber weder vollständiges Thermalkonzept noch Mechanik oder Systemkühlung.

### Warum braucht man vor der Serie Schliffbild und X-Ray?

Weil viele VIPPO-Probleme im CAD nicht sichtbar werden und auch äußerlich nicht immer erkennbar sind. Schliffbild zeigt Füllung und Pad-Form, X-Ray zeigt verdeckte Lötstellen und Thermalpad-Zonen.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [IPC-4761 Table of Contents](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Stützt den öffentlichen Kontext zu Vorteilen, Risiken, Produktions- und Materialfragen verschiedener Via-Schutzmethoden.

2. [Increase Your Component and Trace High Density With Via-in-Pad Plated Over Technology | Altium](https://resources.altium.com/p/increase-your-component-and-trace-high-density-pad-technology)  
   Stützt die öffentliche Erklärung zu via-in-pad in dichten Layouts und Fine-Pitch-BGA-Anwendungen einschließlich Lötzinnabzug bei unbehandelten Pads.

3. [What via Types Are Described in IPC-4761? | Altium](https://resources.altium.com/p/what-types-are-described-ipc-4761-0)  
   Stützt den öffentlichen Kontext zu IPC-4761-Via-Schutzarten und den hier genutzten Type-VII-Rahmen.

4. [Via Covering | Multi Circuit Boards](https://www.multi-circuit-boards.eu/en/pcb-design-aid/surface/via-covering.html)  
   Stützt die öffentliche Erklärung, dass IPC-4761 Type VII auf eine flache und lötbare Oberfläche abzielt und häufig bei via-in-pad sowie Sequential Build-up genutzt wird.

5. [Download IPC 4761 In PDF | IPC WebStore Mirror](https://www.ipcemarket.com/product/ipc-4761/)  
   Stützt den öffentlichen Überblick zu Tenting, Plugging, Filling, Capping und Zuverlässigkeit im Kontext von IPC-4761.

<a id="author"></a>
## Autoren- und Prüfinformationen

- Autor: HILPCB Content-Team für HDI und Optikmodul-Fertigung
- Technische Prüfung: Engineering-Team für PCB-Prozess, HDI, SMT und Thermik
- Letzte Aktualisierung: 2025-11-18

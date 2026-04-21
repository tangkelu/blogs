---
title: "Wie man ein VIPPO-PCB auslegt: Wann Via-in-Pad sinnvoll ist und wann es nur Assemblierungsrisiko erhöht"
description: "Eine direkte Antwort darauf, welche Einsatzkriterien, Via-Protection-Definitionen, Pad-Planarität, Assemblierungsfenster und Validierungsmethoden bei VIPPO-PCBs früh eingefroren werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO PCB", "Via-in-Pad Design", "Via in Pad", "HDI PCB", "SMT Assembly"]
---

# Wie man ein VIPPO-PCB auslegt: Wann Via-in-Pad sinnvoll ist und wann es nur Assemblierungsrisiko erhöht

- **Die erste Frage ist nicht, ob man ein Via in ein Pad setzen kann, sondern ob normales Fanout, normale Via-Protection und der aktuelle Pitch Routing und Assemblierung nicht mehr gleichzeitig erfüllen.**
- **VIPPO ist keine einzelne CAD-Aktion, sondern eine kombinierte Struktur aus Via-Protection, Verfüllung, Kupferkappe, Pad-Planarität und Reflow-Verhalten.**
- **Bei Fine-Pitch-BGAs zeigt sich das Hauptrisiko oft erst in der Assemblierung statt im Bare-Board-Test.**
- **VIPPO ist stark mit HDI, Microvias und lokaler Kupferverteilung gekoppelt.**
- **Eingefroren werden sollte eine serientaugliche Struktur, nicht nur eine erstmusterfähige.**

> **Quick Answer**  
> Der Kern eines VIPPO-PCBs ist nicht nur das Via im Pad, sondern der Nachweis, dass Breakout, Löten und Wärmepfad wirklich profitieren und gleichzeitig Verfüllung, Kupferkappe, Planarität und Reflow stabil reproduzierbar bleiben.

## Inhaltsverzeichnis

- [Was sollte man bei einem VIPPO-PCB zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Wann ist VIPPO wirklich die richtige Wahl?](#need)
- [Warum müssen Via-Protection-Definition und Filled-Via-Struktur klar beschrieben werden?](#structure)
- [Warum entscheiden Pad-Planarität und Assemblierungsfenster über das Serienergebnis?](#assembly)
- [Warum muss VIPPO über einen Zuverlässigkeitskreislauf verifiziert werden?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei einem VIPPO-PCB zuerst prüfen?

Zuerst **Einsatzgrund, Via-Protection-Definition, Verfüll- und Kupferkappenstruktur, Pad-Planarität, Assemblierungsfenster und Validierungsmethode**.

Vorab zu klären:

- **Erzwingen Pitch und Breakout-Druck wirklich Via-in-Pad?**
- **Muss Lot-Wicking unterdrückt oder der Fanout außerhalb des Pads deutlich verkürzt werden?**
- **Ist die Zone auch mit HDI, Microvias oder hohem lokalem Wärmestrom gekoppelt?**
- **Lassen sich Pad-Planarität, Lötstopplack und Stencil-Strategie gemeinsam stabil festlegen?**
- **Ist das Fertigungspaket für PCB-Hersteller und Assemblierung eindeutig genug?**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Methode | Warum wichtig | Wie verifizieren | Was passiert, wenn es ignoriert wird |
| --- | --- | --- | --- | --- |
| Einsatzkriterien | Nachweisen, dass normales Fanout Dichte und Assemblierung nicht mehr erfüllt | VIPPO ist teuer und riskant | Fanout-Review, Package-Review | Mehr Kosten ohne echten Gewinn |
| Via-Protection-Definition | Via-Protection, Verfüllung, Abdeckung und Oberfläche klar definieren | Via-in-Pad darf nicht implizit bleiben | Fabrication Note, Gerber-Review | PCB-Fertiger und Assemblierung lesen Unterschiedliches |
| Pad-Planarität | Konsistenz im Array statt Einzel-Pad betrachten | Beeinflusst Drucken, Platzieren, Reflow | Erstmuster, Coplanarity, X-Ray | Head-in-Pillow, kalte Lötstellen, Yield-Drift |
| Strukturkopplung | VIPPO gemeinsam mit Microvias, Buried Vias und Kupferdicke bewerten | Gestapelte Strukturen erhöhen Stress | Schliff, DFM, Post-Reflow-Check | Erstmuster okay, Serie nicht |
| Assemblierungsfenster | Stencil, Paste, Lötstopplackbrücke und Rework-Grenzen zusammen einfrieren | VIPPO-Risiko zeigt sich oft zuerst in SMT | SMT DOE, Erstmuster | Bare Board besteht, Assembly nicht |
| Validierungsloop | Coupon, Schliff, X-Ray und Post-Reflow gemeinsam sehen | Erstboard-Erfolg ist nicht Wiederholbarkeit | Multi-Board-Prüfung, Lot-Traceability | Latente Fehler zeigen sich später |

| Frühe Frage | Bessere Engineering-Aktion |
| --- | --- |
| Nur lokal enges Routing | Dog-Bone-Fanout gegen VIPPO real vergleichen |
| BGA-Pitch sehr eng und Lot-Wicking unzulässig | Pad-Via-Struktur und Assembly-Bedingungen früh einfrieren |
| Projekt nutzt HDI oder Microvias | Via-in-Pad und Microvia-Struktur gemeinsam reviewen |
| Zeichnungsklarheit schnell prüfen | Erst [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/) nutzen |

<div style="background: linear-gradient(135deg, #f3f5fb 0%, #eef6f2 100%); border: 1px solid #d8dfe7; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #536f94; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405a79; font-weight: 700;">Need Before Structure</div>
      <div style="margin-top: 8px; color: #243545;">Erst Notwendigkeit beweisen, dann Geometrie diskutieren. Ohne klare Notwendigkeit wandert das Risiko nur in die Padmitte.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #55715d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #45614d; font-weight: 700;">Structure Must Be Explicit</div>
      <div style="margin-top: 8px; color: #27352b;">Wenn Verfüllung, Kupferkappe und Oberflächenzustand nicht klar beschrieben sind, arbeiten Fertigung und Assembly nach unterschiedlichen Annahmen.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6a4e; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f543d; font-weight: 700;">Assembly Fails First</div>
      <div style="margin-top: 8px; color: #372c24;">Viele VIPPO-Probleme tauchen nicht im Bare-Board-Test auf, sondern erst bei Drucken, Reflow und X-Ray.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a5e73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #70485c; font-weight: 700;">Repeatability Matters</div>
      <div style="margin-top: 8px; color: #392833;">VIPPO wird erst dann serienreif, wenn mehrere Boards, Reflows und Assemblierungszustände stabil bleiben.</div>
    </div>
  </div>
</div>

<a id="need"></a>
## Wann ist VIPPO wirklich die richtige Wahl?

Fazit: **VIPPO lohnt sich erst dann, wenn normales Fanout bereits Routingraum, Lotkontrolle oder Wärmepfad opfert und einfachere Strukturen das Problem nicht mehr lösen.**

Vorab zu bestätigen:

- **Ist das Package-Array wirklich durch Breakout-Raum blockiert?**
- **Macht ein normales Via-Schema das Pad-Design schon unbrauchbar?**
- **Benötigt der lokale Wärmepfad tatsächlich ein Via im Pad?**
- **Brauchen nur wenige kritische Packages VIPPO statt die ganze Platine?**

<a id="structure"></a>
## Warum müssen Via-Protection-Definition und Filled-Via-Struktur klar beschrieben werden?

Fazit: **Weil das VIPPO-Fertigungsergebnis stark davon abhängt, was explizit gefordert wurde, nicht davon, was ein Werk üblicherweise annimmt.**

Explizit zu schreiben:

- **Welche Pads Via-in-Pad brauchen**
- **Ob diese Vias Breakout, Wärmetransport oder Assemblierung dienen**
- **Wie Verfüllung, Abdeckung und Oberflächenplanarität aussehen sollen**
- **Ob zugleich Microvias, Buried Vias oder Sonder-Stackups auftreten**
- **Wo Coupon, Schliff oder Zusatzverifikation nötig sind**

<a id="assembly"></a>
## Warum entscheiden Pad-Planarität und Assemblierungsfenster über das Serienergebnis?

Fazit: **Weil VIPPO bei BGA, LGA und Fine-Pitch am Ende wie ein stabiles Pad funktionieren muss, nicht wie eine nur theoretisch lötbare Sonderstelle.**

Gemeinsam einzufrieren:

- **Konsistenz über das ganze Pad-Array statt Einzelfläche**
- **Ob die Lötstopplackdefinition das echte Pastenfenster zusammendrückt**
- **Ob das Stencil auf die reale Pad-Oberfläche nach VIPPO abgestimmt ist**
- **Ob kritische BGA-Zonen gezielte X-Ray-Stichproben brauchen**

<a id="validation"></a>
## Warum muss VIPPO über einen Zuverlässigkeitskreislauf verifiziert werden?

Fazit: **Weil das eigentliche Risiko nicht immer „nicht herstellbar“ ist, sondern „einmal machbar, später unter Reflow, Loswechsel oder Stress driftend“.**

Ein sinnvoller Release-Pfad enthält meist:

1. **Einsatzgrund einfrieren.**
2. **Fertigungsdefinition einfrieren.**
3. **Assembly-Input einfrieren.**
4. **Physische Verifikation einfrieren.**
5. **Los-Traceability einfrieren.**

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Für dichtes Breakout und lokale Layerwechsel zuerst den [HDI PCB](https://hilpcb.com/en/products/hdi-pcb)-Pfad nutzen.
- Für Vergleich Standard vs. High-Density [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) und VIPPO gemeinsam reviewen.
- Für Pad-, Stencil- und Reflow-Risiko [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) früh einbinden.
- Für Klarheitsprüfung der Fertigungsunterlagen zuerst [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/) nutzen.
- Für Muster- oder Pilotstart Schlüsselpunkte in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) und [Quote / RFQ](https://hilpcb.com/en/quote/) vorziehen.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Sollte jede BGA-Platine VIPPO standardmäßig verwenden?

A: Nein. Nur wenn normales Fanout nicht mehr tragfähig ist oder klare Vorteile bei Lotkontrolle und Wärmepfad bestehen.

### Warum zeigen sich VIPPO-Probleme oft erst in SMT?

A: Weil die Struktur das reale Lötverhalten des Pads verändert. Sichtbar wird das oft erst bei Drucken, Reflow und X-Ray.

### Reicht es, wenn in der Zeichnung nur „filled via“ steht?

A: Nein. Via-Protection, Abdeckart, Planaritätsanforderung, Validierung und Assembly-Grenzen müssen ebenfalls klar definiert sein.

### Warum sollten VIPPO und HDI zusammen reviewt werden?

A: Weil Via-in-Pad oft mit Microvias, dichter Layerwechselstruktur, Stackup und mehrfachen Reflows gekoppelt ist.

### Was sollte man vor der Fertigung zuerst einfrieren?

A: Einsatzgrund, Pad/Via-Definition, Planaritäts- und Assembly-Bedingungen, physische Validierungsmethode und Los-Traceability.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [IPC-4761 Design Guide for Protection of Printed Board Via Structures](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Stützt die Aussage, dass VIPPO als Via-Protection-Struktur explizit spezifiziert werden muss.

2. [IPC Board Design Standards](https://www.ipc.org/ipc-board-design-standards)  
   Stützt die Einordnung von IPC-4761, IPC-2221, IPC-2226 und IPC-6012 in einen gemeinsamen Designkontext.

3. [IPC Releases IPC-6012F, Qualification and Performance Specification for Rigid Printed Boards](https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed)  
   Stützt die Vorverlagerung von Coupon- und Leistungsvalidierung komplexer Interconnect-Strukturen.

4. [IPC Issues Electronics Industry Warning on Printed Board Microvia Reliability for High Performance Products](https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high)  
   Stützt den Hinweis auf latente Fehler in Microvia- und Via-in-Pad-Kombinationen nach Reflow oder Stress.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für HDI und Assemblierung
- Technische Prüfung: PCB-Prozess-, DFM- und SMT-Engineering-Team
- Letzte Aktualisierung: 2025-11-18

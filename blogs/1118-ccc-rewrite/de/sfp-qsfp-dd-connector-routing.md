---
title: "Was man bei SFP- und QSFP-DD-Steckverbinder-Routing zuerst prüfen sollte: 112G-Breakout, Backdrill und Übergangskontrolle auf dem Host-Board"
description: "Eine direkte Antwort auf Schnittstellenform, Breakout, Referenzebenen, Backdrill, Materialwahl sowie Montage- und Thermikthemen, die beim SFP- und QSFP-DD-Routing auf 112G zuerst geprüft werden sollten, damit High-Speed-Host-Boards und Backplanes ihre Kanalreserve im Steckverbinderbereich behalten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["QSFP-DD routing", "SFP routing", "High-speed connector PCB", "Signal integrity", "Low-loss PCB", "112G PAM4"]
---

# Was man bei SFP- und QSFP-DD-Steckverbinder-Routing zuerst prüfen sollte: 112G-Breakout, Backdrill und Übergangskontrolle auf dem Host-Board

- **Bei 112G PAM4 entscheidet die "letzte Zollstrecke" am Steckverbinder oft früher über den Link als die lange Hauptleitung.**
- **Die Schwerpunkte bei QSFP-DD und SFP112 sind nicht identisch, aber in beiden Fällen hängt das Ergebnis an Launch, Breakout und stabilem Rückstrompfad.**
- **QSFP-DD ist nicht nur wegen der Datenrate schwierig, sondern weil die 8-Lane-Schnittstelle Dichte, Thermik und SI-Druck auf derselben Host-Platine bündelt.**
- **Besseres Material hilft beim Einfügungsverlust, rettet aber keinen schlechten Breakout.**
- **Steckverbinder-Routing muss immer zusammen mit Cage, Kühlkörper und Montagekonzept bewertet werden.**

> **Quick Answer**  
> Die eigentliche Aufgabe beim Routing von SFP- und QSFP-DD-Steckverbindern besteht nicht nur darin, Differenzpaare vom ASIC bis zur Platinenkante zu ziehen. Auf einem 112G-Host-Board müssen Breakout-Geometrie, Pad-Übergang, Via-/Backdrill-Strategie, Referenzebenen und die Montage des Steckverbinders gemeinsam funktionieren. Reserve entsteht nicht durch die schönste Hauptleitung, sondern dadurch, dass die letzte Zollstrecke noch fertigungstauglich, montierbar und reproduzierbar bleibt.

## Inhaltsverzeichnis

- [Was sollte man bei SFP- und QSFP-DD-Routing zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum setzt der Breakout-Bereich oft die Untergrenze eines 112G-Kanals?](#breakout)
- [Warum müssen Vias, Backdrill und Referenzebenen im Launch-Bereich gemeinsam konvergieren?](#launch-via)
- [Warum dürfen Material, Cage und Thermik nicht getrennt vom Routing bewertet werden?](#thermal-materials)
- [Wie sollte das Host-Board-Routing vor der Serie validiert werden?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufige Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfinformationen](#author)

<a id="overview"></a>
## Was sollte man bei SFP- und QSFP-DD-Routing zuerst prüfen?

Zuerst **Bauform der Schnittstelle, Lane-Zahl und Datenrate, Breakout-Struktur, Via-/Backdrill-Strategie sowie das thermische und mechanische Fenster** prüfen.

Es geht nicht einfach darum, ein High-Speed-Differenzpaar bis zum Steckverbinder zu führen. Und QSFP-DD ist nicht bloß "SFP mit mehr Lanes". TE zeigt öffentlich SFP bis **112G** Lane-Rate, während QSFP-DD als **56-112G** mit **8-Lane-PAM4-Architektur** beschrieben wird. Auf dem Host-Board sollte man deshalb zuerst klären:

1. **Handelt es sich um einen SFP112-Launch mit wenigen Lanes oder um einen 8-Lane-QSFP-DD-Launch?**
2. **Hat der Breakout genug Lagen, Fanout-Raum und kontinuierliche Referenzebenen?**
3. **Sind Backdrill, Blind/Buried Vias oder aggressivere Via-Strukturen nötig?**
4. **Verändern Cage, Kühlkörper oder gestapelte Ports den Platz und den Rückstrompfad auf der Platine?**
5. **Wurden Montage und Thermik bereits in derselben Review-Runde betrachtet?**

Für Switches, NICs, Serverboards oder Backplanes sollte das Stackup und die Bohrfähigkeit von [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) und [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) in der Regel vor Abschluss des Layouts abgestimmt werden.

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Sinnvolle Beurteilung | Warum wichtig | Wie prüfen | Folge bei Vernachlässigung |
|---|---|---|---|---|
| Schnittstellenform | Erst SFP112-Kontext und QSFP-DD-8-Lane-Kontext sauber trennen | Dichte und Thermikgrenzen unterscheiden sich stark | Datenblatt, Systemreview | Stackup und Breakout-Strategie passen nicht |
| Breakout-Pfad | Paare schnell aus dem Pad-Feld herausführen, mit wenig Neck-down und Verzug | Die letzte Zollstrecke frisst Margin am schnellsten | 3D/2.5D-Simulation, Layout-Review | Gute Hauptleitung kompensiert Launch-Verlust nicht |
| Via / backdrill | Through-via-Stub an High-Speed-Lanes minimieren, Backdrill bei Bedarf | Stub-Resonanzen werden bei 112G stark verstärkt | TDR, Schliffbild, Bohrfähigkeitsreview | Return Loss schlechter, Training instabil, BER steigt |
| Referenzebenen | Unter Launch und Breakout kontinuierliche Rückstrompfade halten | Connector-PCB-Interaktion ist nicht mehr vernachlässigbar | Plane-Review, 3D-Feldsimulation | Mode-Conversion und Common-Mode-Rauschen steigen |
| Material / Kupfer | Gegen Gesamtlänge und Verlustbudget bewerten, nicht als Reparaturwerkzeug | Low-loss-Material löst nur einen Teil des Problems | Stackup-Review, IL-Simulation, Coupon | Materialupgrade, aber Link weiterhin instabil |
| Cage / Kühlkörper / Montage | Cage, Kühlkörper, Coplanarity und Montagespannung gemeinsam prüfen | Der Steckverbinderbereich ist auch montagekritisch | Montage- und Thermikreview, X-Ray / Sichtprüfung | Muster läuft, Pilotserie schwankt |

| Schnittstellenbeispiel | Öffentlich genannter Kernpunkt | Designhinweis |
|---|---|---|
| SFP | TE guide: 1-112G Lane Rate | Weniger Lanes, aber Launch bleibt empfindlich |
| QSFP-DD | TE page: acht elektrische Lanes, 28G/56G/112G, bis 800 Gbps | Dichte, Thermik und Breakout-Risiko addieren sich |
| 112G Host Connection | Cadence: Connector und final inch nicht getrennt betrachten | Board und Steckverbinder gemeinsam modellieren |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef6f1 100%); border: 1px solid #d5e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365c7c; font-weight: 700;">Final Inch First</div>
      <div style="margin-top: 8px; color: #233546;">Auf einem 112G-Host-Board sitzt das Hauptrisiko oft in den ersten Millimetern von Breakout und Pad-Übergang, nicht in der langen Trunk-Leitung.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7b72; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a6159; font-weight: 700;">Backdrill Is a Routing Decision</div>
      <div style="margin-top: 8px; color: #223630;">Im 112G-Breakout ist Backdrill keine späte Korrektur, sondern eine Routing-Grundregel, die bei Via-Struktur und Lagenwechsel beginnt.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #886847; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Material Cannot Fix Launch Errors</div>
      <div style="margin-top: 8px; color: #3a2f25;">Low-loss-Material senkt den Gesamtverlust, kann aber Reflexionen und Mode-Conversion aus Stub, Anti-Pad oder gebrochenem Rückstrompfad nicht heilen.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5f7d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c4960; font-weight: 700;">Cage and Thermal Change the Board</div>
      <div style="margin-top: 8px; color: #392733;">QSFP-DD-Cage, Kühlkörper und gestapelte Ports verändern Platz, Luftstrom und Montagefenster auf dem Host-Board. Das lässt sich nicht von SI trennen.</div>
    </div>
  </div>
</div>

<a id="breakout"></a>
## Warum setzt der Breakout-Bereich oft die Untergrenze eines 112G-Kanals?

Fazit: **Weil bei 112G der empfindlichste Abschnitt meist die Kombination aus Steckerpads, Vias, Anti-Pads und den ersten Millimetern Host-Routing ist.**

Cadence formuliert es direkt: Bei älteren Datenraten konnten Steckverbinder und Referenzboard oft getrennt analysiert und später kombiniert werden. Bei **112G PAM4** gilt das nicht mehr, weil die Interaktion zwischen Breakout-Region und Steckverbinder nicht mehr vernachlässigbar ist. Das bedeutet für SFP- und QSFP-DD-Host-Boards:

- **Launch-Verlust und Reflexion sind keine Nebeneffekte mehr**
- **lokales Übersprechen und Mode-Conversion treten früher auf als Trunk-Verlust**
- **instabile Breakout-Geometrie lässt sich durch Equalization nicht vollständig reparieren**

QSFP-DD ist vor allem deshalb kritischer, weil TE die Bauform ausdrücklich als **eight-lane electrical interface** beschreibt. Mehr Lanes, dichtere Pins, größerer Cage und mehr Thermik machen den Breakout zum echten Flaschenhals.

<a id="launch-via"></a>
## Warum müssen Vias, Backdrill und Referenzebenen im Launch-Bereich gemeinsam konvergieren?

Fazit: **Weil im 112G-Breakout Via-Struktur und Rückstrompfad selbst Teil der Steckverbinderleistung sind.**

Ein häufiger Fehler ist, Vias als Nebenpunkt zu behandeln und die Backdrill-Diskussion zu verschieben. In Wirklichkeit bestimmen Through-via, Reststub, Anti-Pad-Geometrie, GND-via-Pitch und Plane-Keep-out gemeinsam:

- ob der Return Loss noch akzeptabel ist
- ob der Einfügungsverlust schon zu Beginn zu hoch wird
- ob die Lane-zu-Lane-Konsistenz ausreicht
- ob Common-Mode-Rauschen und Übersprechen verstärkt werden

Praktisch heißt das bei 112G: **Via-Struktur, Backdrill und Öffnungen in der Referenzebene müssen in derselben Review-Runde modelliert und bewertet werden.**

<a id="thermal-materials"></a>
## Warum dürfen Material, Cage und Thermik nicht getrennt vom Routing bewertet werden?

Fazit: **Weil ein 112G-Host-Board-Kanal nicht nur eine Leiterbahn ist, sondern ein System aus Material, Steckverbinder, Cage, Thermik und Montage.**

TE positioniert QSFP-DD als **8-lane PAM4 architecture** für HPC, AI/ML und High-Density-Networking. Die QSFP-DD-Seite betont außerdem, dass gestapelte 2x1-Varianten mehr Höhe für gleichmäßigeren Luftstrom und größere ASIC-Kühlkörper schaffen können. Amphenol kombiniert 1x1-/2x1-SMT-Connectoren, gestapelte Cage-Assemblies und mehrere Kühlkörperoptionen in derselben Produktdefinition.

Damit können folgende Punkte nicht getrennt bewertet werden:

- **ob das Material das Verlustbudget trägt**
- **ob Cage und Kühlkörper die mechanische und thermische Randbedingung am Port verschieben**
- **ob Coplanarity, Montagespannung und Sitz des Connectors stabil bleiben**
- **ob Luftstrom und Erdungsstruktur bei mehreren benachbarten Ports konsistent bleiben**

<a id="validation"></a>
## Wie sollte das Host-Board-Routing vor der Serie validiert werden?

Fazit: **Sinnvolle Validierung beweist, dass Launch-Zone und Hauptkanal auch nach realer Fertigung und Montage noch funktionieren.**

| Validierungspunkt | Welche Frage er beantwortet | Typische Beobachtungspunkte |
|---|---|---|
| 3D-/2.5D-Kosimulation | Funktionieren Connector und Breakout als Gesamtstruktur? | Launch, Anti-Pad, GND-Vias, Cage-Interaktion |
| Coupon / TDR | Sind Stub und lokale Unstetigkeiten beherrscht? | Impedanzplateau, Reststub, lokale Reflexion |
| Schliffbild / Bohrkontrolle | Trifft Backdrill nach Galvanik noch das Ziel? | Stub-Länge, Lochgeometrie, Kupferdicke, Konsistenz |
| System-Link-Test | Behalten reale Module und Host-Board genug Margin? | Training, BER, Lane-Konsistenz |
| Multi-Board-/Montagecheck | Sind Löten und Cage-Montage reproduzierbar? | Coplanarity, Voids, Thermostress, Board-Streuung |

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie aktuell ein SFP112- oder QSFP-DD-112G-Host-Board vorantreiben, ist der nächste sinnvolle Schritt, High-Speed-Routing in fertigungstaugliche Vorgaben für die Connector-Zone zu übersetzen:

- Über [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) und [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) zuerst Stackup, Material und Kanalausrichtung für 112G zusammenführen.
- Für dichtere Breakouts und engere Lagenwechsel das Via-/Backdrill-Fenster von [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) oder [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) parallel prüfen.
- Connector, Cage, Thermik und Montageprüfpunkte bereits in der [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/)-Phase zusammen bewerten.
- Sobald Launch, Backdrill, Material und Montageweg stehen, diese Bedingungen direkt in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) oder [Quote / RFQ](https://hilpcb.com/en/quote/) übernehmen.

<a id="faq"></a>
## Häufige Fragen (FAQ)

<!-- faq:start -->

### Ist Materialverlust die Hauptschwierigkeit bei QSFP-DD-112G-Routing?

Nein. Materialverlust ist wichtig, aber bei 112G zeigen sich die ersten Probleme meist in Breakout-Geometrie, Launch, Via-Stub, Anti-Pad und Rückstrompfad.

### Ist SFP112 wegen weniger Lanes deutlich einfacher als QSFP-DD?

Der Dichtedruck ist kleiner, die Grundregeln bleiben aber gleich. Auch SFP112 muss den 112G-Übergang, Stub-Kontrolle, Materialwahl und Montagekonsistenz beherrschen.

### Kann man Backdrill erst entscheiden, wenn der erste Prototyp schlecht misst?

Meist nein. Im 112G-Connector-Bereich ist Backdrill eher eine Entwurfsrandbedingung als eine Nachbesserung.

### Warum beeinflussen Cage und Kühlkörper die Routing-Review?

Weil Cage, Kühlkörper, gestapelte Ports sowie Platz, Luftstrom und Erdung des Host-Boards gekoppelt sind.

### Warum reicht reine 2D-Simulation im 112G-Steckverbinderbereich nicht?

Weil Cadence ausdrücklich sagt, dass die elektromagnetische Interaktion zwischen Breakout und Connector bei 112G nicht mehr vernachlässigbar ist.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [TE High-Speed Input/Output Interconnect Selection Guide](https://www.te.com/content/dam/te-com/documents/datacomm/global/ddn-hsio-guide-en-2026.pdf)  
   Stützt den öffentlichen Kontext, dass SFP bis 1-112G reicht und QSFP-DD im Bereich 56-112G als 8-Lane-PAM4-Architektur geführt wird.

2. [TE QSFP-DD Interconnects](https://www.te.com/en/products/connectors/high-speed-pluggable-io-connectors-and-cages/qsfp-dd.html)  
   Stützt die Erklärung zu acht elektrischen Lanes, 28G NRZ, 56G PAM4, 112G PAM4, bis 800 Gbps pro Port sowie der Kopplung von Cage/Kühlkörper und Host-Board.

3. [Cadence White Paper: Overcoming Signal Integrity Challenges of 112G Connections](https://www.cadence.com/ko_KR/home/resources/white-papers/overcoming-signal-integrity-challenges-of-112g-connections-wp.html)  
   Stützt die Engineering-Aussage, dass Connector und final-inch-Breakout bei 112G gemeinsam modelliert werden müssen.

4. [Amphenol ExtremePort™ QSFP DD 112G Connectors Datasheet](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/datasheet/inputoutput/hsio_cn_extremeport_qsfp_dd_112g.pdf)  
   Stützt die öffentliche Einordnung von 112G-QSFP-DD-Connector, gestapeltem Cage und Kühlkörperoptionen als gemeinsames Host-Interconnect-System.

5. [QSFP-DD MSA Specification Page](https://www.qsfp-dd.com/specification/)  
   Stützt den öffentlichen Standardkontext rund um 8 High-Speed Electrical Interfaces bei QSFP-DD.

<a id="author"></a>
## Autoren- und Prüfinformationen

- Autor: HILPCB Content-Team für High-Speed-Interconnect und Steckverbinder
- Technische Prüfung: Engineering-Team für PCB-Prozess, SI und High-Speed-Montage
- Letzte Aktualisierung: 2025-11-18

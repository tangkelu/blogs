---
title: "Wie man einen HDMI-PCB-Stackup festlegt: 100 Ohm Differenzial, Loss Budget und Steckverbinder-Übergänge"
description: "Eine direkte Antwort zu Zielversion, 100-Ohm-Differenzialimpedanz, Referenzebenen, Materialverlusten und Connector-Transitions, die beim HDMI-PCB-Stackup zuerst geprüft werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# Wie man einen HDMI-PCB-Stackup festlegt: 100 Ohm Differenzial, Loss Budget und Steckverbinder-Übergänge

- **Beim HDMI-Stackup geht es nicht zuerst um die Lagenzahl, sondern darum, wie viel Fertigungsmarge der Link bei der Zielrate noch hat.**
- **100 Ohm Differenzial bleibt das Grundziel, aber die eigentliche Schwierigkeit ist, ob die Serie diesen Wert hält.**
- **Kontinuität der Referenzebene und Launch-Übergänge verbrauchen Margin oft früher als die geraden Leiterbahnen.**
- **Nicht jedes HDMI-Board braucht Premium-Low-Loss-Material, aber auch nicht jedes Projekt ist mit normalem FR-4 sicher.**
- **Validierung braucht echte Fertigungsdaten.**

> **Quick Answer**  
> Ziel des HDMI-PCB-Stackup-Designs ist, 100-Ohm-Differenzialpaare, kontinuierliche Referenzebenen, verlustarme Geometrie und Steckverbinderübergänge bei der Zielversion und Lane-Rate gemeinsam funktionsfähig zu machen. Ein Stackup ist erst dann wirklich brauchbar, wenn er nach Lamination, Ätzen und Assembly noch Link-Margin hält.

## Inhaltsverzeichnis

- [Was sollte man beim HDMI-PCB-Stackup zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum sollte HDMI-Stackup mit einem Loss Budget aus Rate und Länge beginnen?](#loss-budget)
- [Warum muss 100 Ohm Differenzialimpedanz an die reale Fertigung gebunden werden?](#impedance)
- [Warum sind Steckverbinder, Lagenwechsel und Stubs gefährlicher als gerade Leiterbahnen?](#transitions)
- [Wie sollte man HDMI-Stackups vor der Serie validieren?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man beim HDMI-PCB-Stackup zuerst prüfen?

Zuerst **Zielversion, Lane-Rate, Leiterbahnlänge auf dem Board, Referenzebenen und Connector-Transitions**.

Es reicht nicht, einfach Standard-High-Speed-Regeln auf Differentialpaare anzuwenden. HDMI 2.1b erhöht die Systembandbreite auf **48Gbps**, und TI nennt für HDMI 2.1 FRL Lane-Raten von **3/6/8/10/12Gbps**. Daher sind die ersten Fragen:

1. **Ist der Link HDMI 2.0 TMDS oder HDMI 2.1 FRL?**
2. **Erzwingen Länge und Connector-Position Lagenwechsel oder lange Stubs?**
3. **Reicht FR-4 noch aus oder ist ein Low-Loss-System nötig?**
4. **Bleibt die Referenzebene entlang des gesamten Pfads kontinuierlich?**
5. **Kann die Fabrik 100 Ohm Differenzial wiederholbar fertigen?**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Beurteilung | Warum wichtig | Wie prüfen | Wenn ignoriert |
|---|---|---|---|---|
| HDMI-Version und Rate | TMDS bis 6Gbps oder FRL bis 12Gbps/lane sauber trennen | Die Rate definiert Loss Budget und Materialfenster | Spezifikation, Chip-Datenblatt, Protokolleinstellung | Falscher Stackup, knappe Eye- und EMI-Marge |
| Differenzialimpedanz | HDMI-Paare auf ca. 100 Ohm Differenzial auslegen | Grundanforderung der Übertragungsstruktur | Impedanzrechnung, Coupon, TDR | Mehr Reflexion und engeres Eye |
| Referenzebene | Paar entlang des gesamten Pfads neben einer kontinuierlichen Ebene führen | Rückstromkontinuität beeinflusst SI und EMI | Layoutreview, Lagenwechselprüfung | Mehr Mode Conversion und Abstrahlung |
| Material und Kupfer | Materialfamilie aus Länge, Rate und Rauheit gemeinsam bewerten | Verlust und Fertigungsstreuung steigen mit der Rate | Stackupreview, Schliff, Insertion-Loss-Test | Prototyp geht, Serie wird kritisch |
| Connector-/Via-Transition | Launch, Anti-Pad, Stub und Lagenwechsel separat prüfen | Übergänge fallen oft vor den Geraden aus | 3D-Modell, TDR, Messwellenform | Schwarzer Bildschirm, Bildfehler, Instabilität |
| Fertigungskonsistenz | Designwerte müssen zur realen Geometrie der Fabrik passen | Lamination und Ätzen verschieben die Maße | Schliff, Coupon, Chargenvergleich | Link-Margin driftet zwischen Losen |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 und 2.1 sollten nicht mit demselben unscharfen Stackup-Ansatz behandelt werden. Erst Lane-Rate festlegen, dann Material, Lagen und Längenbudget.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100 Ohm Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100 Ohm ist nicht nur ein Eingabewert in Software. Der Wert muss auch nach Lamination, Ätzen und Kupferoberfläche im realen Produkt erhalten bleiben.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">Bei HDMI-Boards fällt Margin oft zuerst in Steckverbinder-Launches, Lagenwechseln und Stubs und nicht in den langen geraden Segmenten.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">Ein reifer HDMI-Stackup wird durch Coupons, Schliffe und TDR-/Insertion-Loss-Daten belegt, nicht nur durch ein gutes Layoutreview.</div>
    </div>
  </div>
</div>

<a id="loss-budget"></a>
## Warum sollte HDMI-Stackup mit einem Loss Budget aus Rate und Länge beginnen?

Fazit: **Weil Materialfamilie und Stackup von realer Lane-Rate, Leiterbahnlänge und Zahl der Übergänge abhängen und nicht von üblichen Gewohnheiten für diese Schnittstelle.**

HDMI 2.1b erhöht die Gesamtbandbreite auf **48Gbps**. TI nennt für FRL bis zu **12Gbps** pro Lane und für HDMI 2.0b / TMDS bis zu **6Gbps**. Entscheidend sind daher:

- **Wie lang ist der Pfad auf dem Board?**
- **Wie viele Steckverbinder, ESD-Bauteile, Re-Driver und Lagenwechsel gibt es?**
- **Bleibt mit FR-4 noch ausreichend Margin?**
- **Ist schon ein Bereich erreicht, in dem geringere Verluste und strengere Dielektrikkontrolle nötig sind?**

<a id="impedance"></a>
## Warum muss 100 Ohm Differenzialimpedanz an die reale Fertigung gebunden werden?

Fazit: **Weil 100 Ohm bei HDMI kein abstrakter Sollwert ist, sondern das reale Ergebnis aus Lamination, Ätzkompensation und echter Kupfergeometrie.**

TI nennt 100 Ohm Differenzial in mehreren HDMI-Dokumenten explizit. In der Serie verschiebt sich dieser Wert jedoch durch:

- reale Dielektrikdicke nach Lamination
- geätzte statt gezeichnete Leiterbahnbreite
- Kupferrauheit
- Lötstopp, Referenzebenenform und benachbartes Kupfer

Ein robuster Ablauf ist meist:

1. Mit echten Fabrikparametern zurückrechnen  
2. Mit Feldlöser oder [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) vorprüfen  
3. Im Prototyp über Coupon, TDR und Schliff verifizieren  
4. Fabrikkompensation in den finalen Stackup zurückschreiben

<a id="transitions"></a>
## Warum sind Steckverbinder, Lagenwechsel und Stubs gefährlicher als gerade Leiterbahnen?

Fazit: **Weil gerade HDMI-Segmente oft beherrschbar sind, Launches, Vias und Lagenwechsel aber sehr leicht lokale Impedanzsprünge, Mode Conversion und Zusatzverlust erzeugen.**

Besonders separat zu prüfen sind:

- ob unter dem Connector-Launch eine kontinuierliche Referenzebene bleibt
- ob Pad- und Anti-Pad-Geometrie der Vias zum Zielaufbau passt
- ob Ground-Vias den Rückstrom beim Lagenwechsel schließen
- ob Through-Hole-Stubs gekürzt oder backdrilled werden müssen
- ob das Paar nach dem Breakout noch symmetrisch bleibt

<a id="validation"></a>
## Wie sollte man HDMI-Stackups vor der Serie validieren?

Fazit: **Gute HDMI-Validierung beweist nicht nur, dass im Layout 100 Ohm gezeichnet wurden, sondern dass die gefertigte Platine den Zielwert noch hält.**

Ein praktischer Prüfpfad umfasst meist:

| Validierungspunkt | Was beantwortet er? | Wichtige Beobachtungspunkte |
|---|---|---|
| Impedanz-Coupon | Baut die Fabrik die Zielgeometrie wiederholbar? | 100-Ohm-Ziel und Losstreuung |
| Schliff | Haben Lamination und Ätzen die Struktur verschoben? | Dielektrikdicke, Leiterbahnbreite, Kupferprofil |
| TDR oder Insertion-Loss-Test | Sind Übergänge und Gesamtpfad gesund? | Lokale Diskontinuitäten, Gerade vs. Übergang |
| Mehrplatinenvergleich | Ist das Prozessfenster breit genug? | Konsistenz von Eye, Impedanz und Verlust |
| Systemtest | Funktioniert der Stackup mit echten Steckverbindern und Bauteilen? | Auflösung, Bildfehler, Black-Screen-Grenze, EMI |

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Material, Kupfer und Stackup-Richtung zuerst über [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) eingrenzen.
- Den [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) früh für die 100-Ohm-Geometrie verwenden.
- Wenn Connector-Breakout, Lagenwechsel und dichteres Fan-out vorhanden sind, parallel [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) oder [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) mitprüfen.
- Sind Stackup, Coupon-Plan und Launch-Review stabil, diese Punkte direkt in [Quote / RFQ](https://hilpcb.com/en/quote/) oder [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) schreiben.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Braucht jedes HDMI-2.1-Board Premium-Low-Loss-Material?

Nicht unbedingt. Ausschlaggebend sind reale Lane-Rate, Länge und Übergangsanzahl.

### Reicht es aus, das Paar einfach auf 100 Ohm zu zeichnen?

Nein. Das reale Ergebnis hängt zusätzlich von Lamination, Ätzkompensation, Rauheit und Referenzebene ab.

### Brauchen HDMI-Differenzialpaare trotzdem eine kontinuierliche Referenzebene?

Ja. Differenzialführung beseitigt nicht den Bedarf an einem stabilen Rückstrompfad.

### Treten HDMI-Probleme häufiger in der Leiterbahn oder im Connector-Übergang auf?

Oft im Connector-Launch, Via-Lagenwechsel oder Stub.

### Warum sind Coupon oder TDR bei HDMI so wichtig?

Weil sie zeigen, ob die gefertigte Geometrie dem Modell noch entspricht.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   Stützt den offiziellen Kontext zu 48Gbps und höheren Auflösungen / Bildraten.

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   Stützt die Daten zu FRL-Raten von 3/6/8/10/12Gbps.

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   Stützt den Kontext zu HDMI 2.0b / 6Gbps TMDS.

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   Stützt die Aussagen zu 100 Ohm HDMI, Layout an Schutz-/Connector-Bauteilen und Transition-Kontrolle.

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   Stützt die gekoppelte Betrachtung von Layer Stack, Controlled Impedance, Referenzebenen und Vias.

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   Stützt die offizielle Formulierung zu 100 Ohm ±10% Differenzialimpedanz.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für High-Speed-Interfaces und Stackup
- Technische Prüfung: Teams für PCB-Prozess, SI und High-Speed-Connector-Engineering
- Letzte Aktualisierung: 2025-11-18

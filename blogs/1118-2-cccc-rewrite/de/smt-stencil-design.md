---
title: "Wie man ein SMT-Stencil auslegt: Was man bei Öffnungen, Dicke und Druckfenster zuerst einfrieren sollte"
description: "Eine direkte Antwort darauf, welche Öffnungslogik, Dickenwahl, Fine-Pitch-Kontrolle, PCB-Pad-Kopplung und Produktions-Feedbackschleife bei der SMT-Stencil-Auslegung zuerst festgelegt werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["SMT Stencil Design", "Stencil Design", "Lotpastendruck", "SMT Assembly", "PCBA DFM"]
---

# Wie man ein SMT-Stencil auslegt: Was man bei Öffnungen, Dicke und Druckfenster zuerst einfrieren sollte

- **Zuerst eingefroren werden sollte nicht nur die Stencildicke, sondern welche Bauteile am schwersten zu drucken sind und am ehesten Brücken oder zu wenig Paste erzeugen.**
- **Eine Stencil-Öffnung ist keine mechanische 1:1-Kopie des Pads.**
- **Fine-Pitch-Bauteile, zentrale Thermal-Pads und BGAs brauchen unterschiedliche Öffnungslogik.**
- **Viele scheinbare Bestück- oder Reflowfehler entstehen, weil PCB-Pads, Lötstopplack und Stencil nie gemeinsam abgestimmt wurden.**
- **Ein gutes Serien-Stencil lebt von SPI-, AOI- und X-Ray-Feedback, nicht nur von einer einmal funktionierenden Pilotserie.**

> **Quick Answer**  
> Der Kern des SMT-Stencil-Designs ist nicht eine universelle Dicke für alle Gehäuse, sondern eine gemeinsame Definition von Öffnungsform, Freigabefenster, Stencildicke, Pad-Bedingungen und Datenrückführung rund um die kritischsten Strukturen.

## Inhaltsverzeichnis

- [Was sollte man bei der SMT-Stencil-Auslegung zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum steuert die Öffnungsstrategie eigentlich Pastenvolumen und Freigabe?](#aperture)
- [Warum muss die Stencildicke vom empfindlichsten Bereich ausgehen?](#thickness)
- [Warum muss ein Stencil zusammen mit PCB-Pads, Lötstopplack und Assemblierungsparametern geprüft werden?](#pcb-dfm)
- [Warum braucht ein Serien-Stencil eine Datenrückführung?](#feedback)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei der SMT-Stencil-Auslegung zuerst prüfen?

Zuerst **kritische Gehäuse, Öffnungsgeometrie, Stencildicke, Pad-Bedingungen, Druckparameter und Validierungsdaten**.

Entscheidend vor dem Release sind meist:

- **Welche Gehäusefamilie die kleinste Öffnung und das schwächste Release-Fenster vorgibt**
- **Welche Pads Sonderbehandlung statt Default-Template brauchen**
- **Ob die Basisdicke zum schwierigsten Bauteil passt**
- **Ob Pad-, Lötstopplack- und Via-Definition das Druckfenster schon vor dem Drucken zerstören**
- **Welche Pilotdaten in die nächste Stencil-Version zurückgeschrieben werden**

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Methode | Warum wichtig | Wie verifizieren | Was passiert, wenn es ignoriert wird |
| --- | --- | --- | --- | --- |
| Kritischstes Bauteil finden | Kleinste Öffnung, feinster Pitch und komplexestes Thermal-Pad zuerst suchen | Diese Strukturen definieren die Grenze | Package-Review, BOM-Prüfung | Dicke und Öffnungen werden von großen Teilen fehlgeleitet |
| Öffnungsstrategie | Nach Gehäusetyp trennen statt 1:1 zu übernehmen | Steuert Pastenvolumen und Release | SPI, Probedruck, Fehlervergleich | Brücken, zu wenig Paste, Slump |
| Dickenwahl | Zuerst empfindliche Struktur schützen | Dicke bestimmt das Release-Fenster direkt | Erstdruck, Transfer-Effizienz | Fine-Pitch verliert zuerst die Kontrolle |
| PCB-Kopplung | Pad, Lötstopplack und Via-Behandlung gemeinsam prüfen | Viele Fehler starten auf PCB-Seite | DFM-Review, Gerber-Vergleich | Stencil-Tuning heilt die Ursache nicht |
| Sonderstrukturen | QFN-Zentralpad, BGA, PoP und Step-Stencil separat bewerten | Dort kippt der Prozess zuerst | X-Ray, SPI, Reflow-Bild | Voids, Head-in-Pillow, Drift |
| Datenrückführung | SPI/AOI/X-Ray an Revision binden | Nur so konvergiert die Serie | Versionshistorie, Pareto | Gleiches Problem taucht wieder auf |

| Öffentliche Faustregel | Engineering-Bedeutung |
| --- | --- |
| IPC-7525C: Keine feste Einheitsregel für alle Stencils | Öffnung und Dicke müssen projektspezifisch bewertet werden |
| Indium StencilCoach: Rechteck-Öffnungen oft mit `W/t > 1.5` vorgeprüft | Gut für frühe Machbarkeitsprüfung |
| Indium StencilCoach: Runde/Quadrat-Öffnungen oft mit `> 0.66` vorgeprüft | Besonders nützlich für BGA/CSP |

<div style="background: linear-gradient(135deg, #f7f4ef 0%, #f3f8f2 100%); border: 1px solid #e2ddd4; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6448; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f513b; font-weight: 700;">Aperture Controls Volume</div>
      <div style="margin-top: 8px; color: #382d24;">Die Öffnung steuert Pastenvolumen, Freigabepfad und Druckstabilität zugleich.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #59745f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #47604c; font-weight: 700;">Thickness Follows The Weakest Link</div>
      <div style="margin-top: 8px; color: #29352c;">Die Stencildicke sollte zuerst die schwierigste Struktur schützen.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #506d91; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405978; font-weight: 700;">PCB And Stencil Are Coupled</div>
      <div style="margin-top: 8px; color: #253544;">Ohne Abstimmung von Pad, Lötstopplack und Via kann selbst ein gutes Stencil nur lokal kompensieren.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6174; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #714b5e; font-weight: 700;">Data Must Update The Stencil</div>
      <div style="margin-top: 8px; color: #392833;">Ohne Rückführung aus SPI, AOI und X-Ray kehren Fehler als angebliche Zufallsprobleme zurück.</div>
    </div>
  </div>
</div>

<a id="aperture"></a>
## Warum steuert die Öffnungsstrategie eigentlich Pastenvolumen und Freigabe?

Fazit: **Weil die Öffnung definiert, wie Lotpaste das Stencil verlässt und als kontrollierte Lötstelle entsteht.**

Wichtige Prüfpunkte sind:

- **Brauchen QFP/QFN-Pins reduzierte oder modifizierte Öffnungen?**
- **Erfüllen BGA/CSP-Zonen ein sinnvolles Area-Ratio-Fenster?**
- **Soll das zentrale Thermal-Pad als Window-Pane segmentiert werden?**
- **Müssen verschiedene Bauteilklassen in getrennte Öffnungsfamilien aufgeteilt werden?**

<a id="thickness"></a>
## Warum muss die Stencildicke vom empfindlichsten Bereich ausgehen?

Fazit: **Weil die Druckgrenze fast immer von der kleinsten Öffnung oder der schwächsten Freigabestelle bestimmt wird.**

Vor dem Freeze sollte geprüft werden:

- **Wo die kleinsten Öffnungen und kritischsten Release-Stellen liegen**
- **Ob eine globale Basisdicke die Fine-Pitch-Zonen noch schützt**
- **Ob ein Step-Stencil nötig ist**
- **Ob große Pads eher über Aperturform als über mehr Dicke kompensiert werden sollten**

<a id="pcb-dfm"></a>
## Warum muss ein Stencil zusammen mit PCB-Pads, Lötstopplack und Assemblierungsparametern geprüft werden?

Fazit: **Weil viele Druckfehler keine isolierten Stencil-Probleme sind, sondern aus Pad-, Lötstopplack-, Via- und Package-Definition stammen.**

Gemeinsam zu prüfen:

- **Passen Pad-Größen zum empfohlenen Land Pattern?**
- **Verkleinert der Lötstopplack das echte Pastenfenster?**
- **Verändern Via-in-Pad, Verfüllung oder Oberflächenfinish das Druckverhalten?**
- **Braucht das Thermal-Pad eine eigene Void-Strategie?**

<a id="feedback"></a>
## Warum braucht ein Serien-Stencil eine Datenrückführung?

Fazit: **Weil ein gutes Serien-Stencil nicht nur einmal druckt, sondern über Lose hinweg ähnliche Ergebnisse liefert.**

Ein sinnvoller Regelkreis umfasst meist:

1. **Kritische Bauteilfamilien klassifizieren.**
2. **Fehler an Apertur-Familien binden.**
3. **Dicke mit Bauteilmix verknüpfen.**
4. **X-Ray und SPI gemeinsam lesen.**
5. **Revisionen in kontrollierte Dokumente zurückschreiben.**

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Für Öffnungsstrategie und Package-Klassifizierung zuerst [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) einbeziehen.
- Wenn Beschaffung, Assemblierung und Reflow-Fenster zusammenlaufen, die Stencil-Strategie mit [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) gemeinsam einfrieren.
- Für frühe Zeichnungsprüfung [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/) nutzen.
- Für Muster- und Serienkonvergenz kritische Strukturen früh in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) ziehen.
- Oberflächenfinish mit [PCB Surface Finish](https://hilpcb.com/en/services/pcb-surface-finish/) früh mitbewerten.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Reicht ein 1:1-Verhältnis von Apertur zu Pad meistens aus?

A: Nein. Unterschiedliche Gehäuse brauchen unterschiedliche Balance zwischen Pastenvolumen, Release und Benetzung.

### Warum kann die Stencildicke nicht nur nach dem größten Bauteil gewählt werden?

A: Weil die Druckgrenze meist von der kleinsten, am schwersten freigebbaren Öffnung ausgeht.

### Warum brauchen BGAs und zentrale Thermal-Pads immer Sonderbehandlung?

A: Weil sie Voids, Head-in-Pillow, ungleiches Collapse-Verhalten und Bauteildrift leichter verstärken.

### Warum werden Stencil-Probleme so oft auf PCB-Pads zurückgeführt?

A: Weil Pad, Lötstopplack, Via-Behandlung und Land Pattern das Druckverhalten direkt bestimmen.

### Was sollte man vor der Fertigung zuerst einfrieren?

A: Bauteilklassifizierung, Öffnungsstrategie, Basisdicke bzw. Step-Stencil-Entscheidung, PCB-Pad-Kopplung und den SPI/AOI/X-Ray-Feedbackpfad.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [IPC-7525C TOC, Stencil Design Guidelines](https://www.ipc.org/TOC/IPC-7525C_TOC.pdf)  
   Stützt die Einordnung von Stencil Design als eigene Richtlinie und die Aussage, dass keine Einheitsregel für alle Projekte existiert.

2. [StencilCoach Standard Apertures | Indium Corporation](https://software.indium.com/stencil-coach/standard-apertures.php)  
   Stützt Aspect-Ratio- und Area-Ratio-Faustregeln wie `W/t > 1.5` und `ArR > 0.66`.

3. [IPC Standards](https://www.ipc.org/ipc-standards)  
   Stützt die gemeinsame Betrachtung von Stencil-, PCB- und Assemblierungsstandards.

4. [Meet Your Standards | IPC-A-610](https://www.ipc.org/meet-your-standards)  
   Stützt die Aussage, dass am Ende die Lötstellen-Akzeptanz des Endprodukts zählt.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für PCBA und Assemblierung
- Technische Prüfung: SMT-Prozess-, DFM- und Qualitätsengineering-Team
- Letzte Aktualisierung: 2025-11-18

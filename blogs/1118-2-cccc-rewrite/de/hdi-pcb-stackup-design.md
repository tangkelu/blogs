---
title: "Wie man ein HDI-PCB-Stackup entwirft: Wann Buildup sinnvoll ist statt einfach mehr konventionelle Lagen hinzuzufügen"
description: "Eine direkte Antwort darauf, welche Entscheidungen im HDI-PCB-Stackup zuerst eingefroren werden sollten, darunter Einführungsbedingungen, Material- und Laminationslogik, Microvia-Strategie, Impedanzgeometrie und Montagevalidierung, damit HDI-Projekte in einem herstellbaren Komplexitätsfenster bleiben."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDI-Stackup-Design", "HDI PCB", "Microvia-Design", "Impedanzkontrolle", "PCB DFM"]
---

# Wie man ein HDI-PCB-Stackup entwirft: Wann Buildup sinnvoll ist statt einfach mehr konventionelle Lagen hinzuzufügen

- **Die erste Frage im HDI-Stackup-Design ist nicht, ob sich noch mehr Leiterbahnen hineinquetschen lassen, sondern ob Packaging-Dichte, Platinenstärke und Lagenwechsel bereits Microvias und Buildup zwingend machen.** Wenn ein konventioneller Multilayer-Aufbau noch konvergiert, erhöht ein zu früher HDI-Einsatz nur Laminations-, Bohr- und Zuverlässigkeitsrisiken.
- **HDI ist nicht einfach "ein normales Board mit mehr Lagen", sondern eine High-Density-Interconnect-Lösung, bei der Stackup, Microvias, Impedanz und Montage gemeinsam konvergieren müssen.**
- **Die Materialauswahl muss elektrische Leistung und sequentielle Laminierung gleichzeitig tragen.** Ein passendes nominelles Dk/Df bedeutet noch nicht, dass Buildup-Dicke, Harzfluss und Kupferverteilung langfristig stabil reproduzierbar sind.
- **Die Microvia-Strategie ist der zentrale Risikopunkt des HDI-Stackups.** IPC hat eine Branchenwarnung zur Microvia-Zuverlässigkeit veröffentlicht. Gestapelte Microvias, Zielpad-Interfaces und Post-Reflow-Ausfallmechanismen können nicht durch "haben wir schon ähnlich gemacht" ersetzt werden.
- **Ein wirklich belastbares Freigabekriterium ist nicht, dass ein Musterboard gefertigt werden kann, sondern dass Coupon, Impedanzprotokoll, Schliffbild und Zustand nach Montage konsistent bleiben.**

> **Quick Answer**  
> Der Kern des HDI-PCB-Stackup-Designs besteht nicht nur darin, mehr Lagen hinzuzufügen oder auf höherwertiges Material zu wechseln. Entscheidend ist, ob High-Density-Breakout, Microvia-Anzahl, Laminationsreihenfolge, Impedanzgeometrie und Montagefenster gemeinsam in einem stabilen Prozessfenster liegen. Bei Fine-Pitch-BGA-, platzkritischen und gemischt hochgeschwindigkeitsfähigen Projekten ist frühe Komplexitätskontrolle meist wirksamer als spätere Rettungsversuche.

## Inhaltsverzeichnis

- [Was sollte man in einem HDI-PCB-Stackup zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Wann ist HDI wirklich die richtige Wahl?](#need)
- [Warum müssen Materialsystem und Laminationslogik gemeinsam festgelegt werden?](#materials)
- [Warum bestimmt die Microvia-Strategie die Obergrenze von Kosten und Zuverlässigkeit?](#microvia)
- [Warum sollten Impedanz, Kupferbalance und Montagefenster gemeinsam eingefroren werden?](#impedance-assembly)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man in einem HDI-PCB-Stackup zuerst prüfen?

Zuerst **Einführungsgrund für HDI, Materialien und Laminierung, Microvia-Strategie, Impedanzgeometrie, Kupferbalance und Montagevalidierung**.

Die Frage bedeutet nicht: "Wenn normaler Multilayer knapp wird, einfach noch ein paar Lagen hinzufügen." Sie bedeutet auch nicht: "Wenn der Hersteller Microvias fertigen kann, ist der Aufbau automatisch sinnvoll." IPC listet IPC-2226 separat als HDI-Designstandard, und die öffentliche Beschreibung zu IPC-6012F nennt complex interconnected via structures, Microvia-Zuverlässigkeit und Test-Coupons ausdrücklich als relevante Aktualisierungen. Das zeigt: HDI-Stackup ist zuerst eine Frage nachhaltiger Herstellbarkeit, nicht der CAD-Zeichnbarkeit.

Vor dem Stackup-Freeze sind meist diese Fragen am wichtigsten:

- **Erfordert die aktuelle Breakout-Dichte wirklich Microvias und Buildup?**
- **Kann konventioneller [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) Boarddicke, Lagenzahl und Routingrestriktionen nicht mehr gleichzeitig erfüllen?**
- **Trägt das Materialsystem sowohl Impedanzziele als auch sequentielle Laminierung und lokale Kupferverteilung?**
- **Bleiben Microvias, Via-in-Pad und lokale Lagenwechsel noch in einem verifizierbaren Fenster?**
- **Werden Montage-, Rework- und Ebenheitsanforderungen das Stackup später wieder kippen?**

Bei Fine-Pitch-BGA-, High-I/O-Modul-, AI-Server-Subboard- oder platzkritischen Steuerboards sollte das Stackup-Fenster von [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) früh zusammen mit dem realen Breakout geprüft werden.

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Empfohlene Methode | Warum wichtig | Wie verifizieren | Was passiert, wenn es ignoriert wird |
| --- | --- | --- | --- | --- |
| HDI-Einführung | Erst belegen, dass konventioneller Multilayer Dichte, Dicke und Lagenwechsel nicht mehr gemeinsam erfüllt | Verhindert unnötige Komplexität | Breakout-Review, Stackup-Vergleich | Kosten und Risiko steigen mit wenig Zusatznutzen |
| Material und Laminierung | Materialdaten zusammen mit Buildup-Dicke, Harzfluss und sequentieller Laminierung reviewen | Gutes Nennmaterial garantiert kein stabiles Endprodukt | Stackup-Review, Datenblätter, Probe-Lamination | Impedanz und Verzug lassen sich schlecht reproduzieren |
| Microvia-Strategie | Stacked/Staggered, Füllung, Capture Pad und Laminationslogik früh festlegen | Microvias sind die zentrale Zuverlässigkeitsvariable | Coupon, Schliff, Post-Reflow-Inspektion | Muster ok, aber latente Fehler nach Reflow |
| Impedanzgeometrie | Fertiggeometrie statt reiner CAD-Nenngeometrie bewerten | HDI ist empfindlicher gegenüber Ätzung, Galvanik und Dielektriktoleranz | Impedanzprotokoll, Geometrieprüfung, Modellabgleich | Simulation und Serienfertigung driften stärker auseinander |
| Kupferbalance | Lokale Kupfer-, Schirm- und Großpad-Bereiche regional prüfen | Beeinflusst Verzug, Lagenversatz und Laminationsstabilität | CAM-Review, Symmetrieprüfung | Ebenheit und Boardform verschlechtern sich |
| Montagefenster | Via-in-Pad, Lötstopplack-Stege, Coplanarity und Rework früh festlegen | Montage deckt Stackup-Schwächen direkt auf | Erstmuster, Ebenheitsprüfung nach Reflow | Blankplatine ok, Montage instabil |

| Früher Bewertungspunkt | Bessere Engineering-Aktion |
| --- | --- |
| Nur lokale Routing-Engstelle | Erst Nutzen von Multilayer versus lokalem HDI vergleichen |
| Fine-Pitch-BGA braucht stabiles Breakout | Microvia-Lagenpaare und Fanout-Logik zuerst festlegen |
| High-Speed-Links plus dichte Packages | Impedanzgeometrie und sequentielle Laminierung zusammen einfrieren |
| Via-in-Pad oder mehrfaches Reflow | Montage- und Ebenheitsanforderungen zuerst in DFM schreiben |

<div style="background: linear-gradient(135deg, #f4f7fb 0%, #eef6f3 100%); border: 1px solid #d7e2e8; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #4f6f8f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3f5b76; font-weight: 700;">Need First</div>
      <div style="margin-top: 8px; color: #243545;">HDI sollte von echtem Breakout-Druck getrieben werden und nicht vom Wunsch, "fortschrittlicher" zu sein.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #587760; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #44604b; font-weight: 700;">Laminate With Process</div>
      <div style="margin-top: 8px; color: #29362c;">Materialwahl muss zusammen mit Laminations- und Harzflussverhalten bewertet werden. Sonst existiert der Aufbau nur nominell, nicht prozesssicher.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6a4e; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f543d; font-weight: 700;">Microvia Risk</div>
      <div style="margin-top: 8px; color: #372c24;">Microvias sind keine automatisch sichere Option. Mit steigender Strukturkomplexität braucht Zuverlässigkeit Coupon-, Schliff- und Post-Reflow-Nachweise.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a5f73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #704a5c; font-weight: 700;">Assembly Matters</div>
      <div style="margin-top: 8px; color: #392933;">Wenn das HDI-Stackup Pad-Ebenheit, Lötstopplack-Stege und Rework nicht trägt, treten Serienprobleme früher auf als bei Standardboards.</div>
    </div>
  </div>
</div>

<a id="need"></a>
## Wann ist HDI wirklich die richtige Wahl?

Fazit: **HDI ist dann sinnvoll, wenn konventioneller Multilayer Package-Breakout, Dickenlimit, Impedanzlagenplanung und lokale Lagenwechsel-Effizienz nicht mehr gleichzeitig erfüllen kann.**

HDI schafft mit kürzeren Interlayer-Pfaden, höherer lokaler Interconnect-Dichte und flexibleren Buildup-Strukturen Routing-Lösungen für feine Packages und engen Raum. Der Preis sind engere Fenster bei Laminationsanzahl, Microvia-Zuverlässigkeit, Formstabilität und Montage. Die richtige erste Frage lautet daher nicht "kann man HDI einsetzen", sondern "gibt es ohne HDI noch eine akzeptable Lösung?"

Früh eingefroren werden sollte:

- **Ob BGA-Breakout schon durch Standard-Bohrungen und normale Lagenpaare blockiert ist**
- **Ob Boarddicke und Impedanz außer Kontrolle geraten, wenn weiter konventionelle Lagen addiert werden**
- **Ob lokale dichte Bereiche kürzere Lagenwechsel und weniger Fläche brauchen**
- **Ob Vollflächen-HDI oder lokales HDI im dichten Bereich sinnvoller ist**

Bei Platz- und Termin­druck lohnt sich oft, [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) früh einzubeziehen, um per Muster zu prüfen, welcher Aufbau dem realen Fertigungsfenster näher kommt.

<a id="materials"></a>
## Warum müssen Materialsystem und Laminationslogik gemeinsam festgelegt werden?

Fazit: **Weil Material auf HDI-Boards nicht nur elektrischer Parameterträger ist, sondern die Grundlage für mehrfache Laminierung, Harzfüllung und Formstabilität bildet.**

Viele HDI-Projekte laufen später nicht wegen schlechter Datenblätter aus dem Ruder, sondern weil Materialwahl, Buildup-Dicke und sequentielle Laminierung getrennt entschieden wurden. In HDI beeinflussen Kompatibilität zwischen Core und Buildup, Harzfluss in dichten Kupferzonen und lokale Dickenänderungen das Ergebnis oft früher als Dk/Df allein.

Nach IPCs öffentlichem Standardrahmen ist HDI eine eigenständige Designkategorie. Gleichzeitig nennt IPC-6012F Test-Coupons und komplexe Via-Strukturen als Kernthemen. Ein Stackup reicht also nicht, wenn es nur theoretisch pressbar ist. Es muss verifizierbar reproduzierbar sein.

Gemeinsam geprüft werden sollte:

- **Ob Core- und Buildup-Material dieselbe Laminationslogik unterstützen**
- **Ob Ziel-Dielektrikdicke und Kupferdicke das Impedanzfenster langfristig halten**
- **Ob dichte Kupferzonen, Thermal-Bereiche und große Pads den Harzfluss aus dem Gleichgewicht bringen**
- **Ob Materiallot-Schwankungen Hochgeschwindigkeits- oder High-Density-Lagen spürbar verschieben**

Wenn High-Density-Interconnect und High-Speed-Links zusammenkommen, sollten das Stackup-Fenster von [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) und der Einfluss von [PCB Surface Finish](https://hilpcb.com/en/services/pcb-surface-finish/) auf die Montage gemeinsam betrachtet werden.

<a id="microvia"></a>
## Warum bestimmt die Microvia-Strategie die Obergrenze von Kosten und Zuverlässigkeit?

Fazit: **Weil Microvias zugleich der Hauptnutzen von HDI und die Komponente mit dem größten Beweisbedarf für Zuverlässigkeit sind.**

IPC veröffentlichte 2019 eine Branchenwarnung zur Microvia-Zuverlässigkeit in Hochleistungsprodukten und wies darauf hin, dass Fehler nach Reflow, im Umwelttest oder sogar im Feldeinsatz sichtbar werden können, obwohl sie bei Raumtemperatur zunächst latent bleiben. Für HDI bedeutet das: Entscheidungen zu stacked microvia, target pad, Kupferfüllung und sequentieller Laminierung dürfen nicht nur aus Gewohnheit getroffen werden.

Früh festgelegt werden sollte:

- **Ob stacked oder staggered microvia besser geeignet ist**
- **Ob capture pad, Landgröße und Lagenpaar genügend Serienmarge haben**
- **Ob via-in-pad wirklich nötig ist und wie Füllung und Kappung definiert werden**
- **Ob lokale Routing-Dichte zu viele Laminationszyklen erzwingt**

Wird das zu spät geklärt, lautet das typische Problem nicht "nicht herstellbar", sondern "herstellbar und montierbar, aber instabil nach Reflow oder zwischen Losen". Bei Projekten mit Via-in-Pad und Ebenheitsanforderungen sollte das Fenster von [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) direkt in die Stackup-Review geschrieben werden.

<a id="impedance-assembly"></a>
## Warum sollten Impedanz, Kupferbalance und Montagefenster gemeinsam eingefroren werden?

Fazit: **Weil die reale Endgeometrie eines HDI-Boards aus Ätzung, Galvanik, Laminierung und Montage gemeinsam entsteht und nicht aus dem nominalen CAD-Wert.**

Ein häufiger Fehler im HDI-Design ist, Impedanz nur aus nominaler Leiterbahnbreite, Abstand und Dielektrikdicke zu berechnen und Kupferbalance, große Kupferfelder, Lötstopplack-Stege und Pad-Ebenheit später zu behandeln. Tatsächlich verändern diese Punkte Referenzflächen-Kontinuität, lokale Harzdicke, Warpage und Coplanarity und wirken damit direkt auf High-Speed- und High-Density-Bereiche zurück.

Gemeinsam eingefroren werden sollte:

- **Die Fertiggeometrie kritischer Impedanzlagen und nicht nur die Nenngeometrie**
- **Ob lokale große Kupferbereiche und dichte Bereiche genügend symmetrisch sind**
- **Ob BGA-, Steckverbinder- und Schirmzonen lokale Dickenungleichgewichte erzeugen**
- **Ob Lötstopplack-Stege, Pad-Ebenheit und Rework-Bedingungen weiter eingehalten werden**

Für schnelle nominale Vergleiche kann früh der [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) genutzt werden. Die Freigabe muss aber auf Stackup, Toleranzen und Verifikationsdaten beruhen.

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

Wenn Sie an Fine-Pitch-BGA-Boards, AI-Server-Subboards, dichten Industrie-Steuerboards oder anderen Designs mit möglichem lokalem HDI arbeiten, sollte der nächste Schritt meist sein, "kann man es bauen?" in "lohnt es sich, genau dieses Stackup zu bauen?" zu verwandeln.

- Bei dichtem Breakout und Dickenlimit zuerst den [HDI PCB](https://hilpcb.com/en/products/hdi-pcb)-Pfad nutzen, um Buildup-Struktur und Microvia-Strategie zusammenzuführen.
- Wenn die Frage noch zwischen mehr Lagen und weiter optimiertem Standardaufbau steht, [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) und HDI auf derselben Review-Tabelle vergleichen.
- Wenn Impedanz und Materialkonsistenz kritischer sind, das Stackup-Fenster von [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) parallel prüfen.
- Wenn Stackup, Coupons und Montagegrenzen früh validiert werden sollen, Schlüsselprüfungen in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) vorziehen.
- Wenn Stackup, Microvias, Montage und Validierungspfad eingefroren sind, alles in [Quote / RFQ](https://hilpcb.com/en/quote/) bündeln.

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Ist HDI immer besser als normaler Multilayer?

A: Nicht unbedingt. Nur wenn konventioneller Multilayer dichten Breakout, Boarddicke und Lagenwechsel-Effizienz nicht mehr gemeinsam schafft, bringt HDI klaren Nutzen.

### Wo versteckt HDI-Stackup am ehesten Risiko?

A: Meist in Microvia-Strategie, sequentieller Laminierung, lokaler Kupfer-Unwucht und Montagefenster. Diese Punkte zeigen sich oft erst nach Reflow oder zwischen Losen.

### Warum kann Materialauswahl nicht nur auf Dk/Df basieren?

A: Weil das fertige HDI-Board auch von Harzfluss, Laminierung, Toleranzen und lokaler Kupferverteilung geprägt wird. Gute elektrische Kennwerte allein garantieren kein stabiles, reproduzierbares Stackup.

### Wann sollte Via-in-Pad festgelegt werden?

A: In derselben Review-Runde wie Stackup und Montage, weil es Microvia-Struktur, Füllung, Pad-Ebenheit und SMT-Risiko gleichzeitig beeinflusst.

### Was sollte vor der Fertigung am dringendsten eingefroren werden?

A: HDI-Einführungsgrund, Material- und Laminationssystem, Microvia-Strategie, Impedanzgeometrie, Montagegrenzen und Verifikationsmethoden.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [IPC Board Design Standards](https://www.ipc.org/ipc-board-design-standards)  
   Stützt die Aussage, dass IPC IPC-2226 als eigenen Designstandard für HDI-Boards listet.

2. [IPC Design Standards](https://www.ipc.org/ipc-design-standards)  
   Stützt die Aussage, dass IPC HDI im öffentlichen Designrahmen als eigenständige Kategorie behandelt.

3. [IPC Releases IPC-6012F, Qualification and Performance Specification for Rigid Printed Boards](https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed)  
   Stützt die Aussage, dass IPC-6012F Anforderungen zu komplexen Via-Strukturen, Microvia-Zuverlässigkeit und Test-Coupons erweitert.

4. [IPC Issues Electronics Industry Warning on Printed Board Microvia Reliability for High Performance Products](https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high)  
   Stützt die Aussage, dass Microvia-Ausfälle bei Hochleistungsprodukten erst nach Reflow oder späteren Belastungen sichtbar werden können.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB HDI- und Stackup-Content-Team
- Technische Prüfung: PCB-Prozess-, DFM- und Montage-Engineering-Team
- Letzte Aktualisierung: 2025-11-18

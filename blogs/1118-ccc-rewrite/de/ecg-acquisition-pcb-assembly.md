---
title: "Worauf es bei der ECG-Erfassungs-PCB-Bestückung ankommt: rauscharme Montage, Sauberkeit und Wearable-Zuverlässigkeit"
description: "Eine direkte Antwort zu Gleichtaktunterdrückung, Eingangsleckstrom, Sauberkeit, Flex-Stress und Funktionsverifikation, die bei der Bestückung von ECG-Erfassungs-PCBs zuerst geprüft werden sollten."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Medical PCB assembly", "ECG acquisition PCB", "Wearable device PCB", "Low-noise PCB design", "ECG patch", "Clinical wearable"]
---

# Worauf es bei der ECG-Erfassungs-PCB-Bestückung ankommt: rauscharme Montage, Sauberkeit und Wearable-Zuverlässigkeit

- **Das Ziel einer ECG-Erfassungsplatine ist nicht nur "sie startet", sondern "die rauscharme Signalkette funktioniert auch in der Serie noch".**
- **Gleichtaktunterdrückung und RLD-Schleife dürfen nicht nur im Schaltplan existieren.** Elektrodenimpedanz, Kabel, Schutznetzwerk und 50/60Hz-Störungen bestimmen die CMR gemeinsam.
- **Hochimpedante Eingangsbereiche reagieren besonders empfindlich auf Rückstände, Feuchte und manuelle Berührung.**
- **Flex- und Starrflex-Strukturen können mechanischen Stress direkt in die Analogkette eintragen.**
- **Funktionsprüfung muss reale Signalkettenverifikation und rückverfolgbare Aufzeichnungen einschließen.**

> **Quick Answer**  
> Der Kern der ECG-Erfassungs-PCB-Bestückung besteht darin, ein hochimpedantes, rauscharme Analog-Frontend auch nach Bestückung, Reinigung, Nacharbeit, Flex-Stress und Systemintegration stabil zu halten. Kritisch sind nicht einzelne Lötstellen, sondern Gleichtaktunterdrückung, Eingangsleckströme, Sauberkeit, mechanische Belastung und rückverfolgbare Funktionsverifikation.

## Inhaltsverzeichnis

- [Was sollte man bei der ECG-Erfassungs-PCB-Bestückung zuerst prüfen?](#overview)
- [Übersicht der wichtigsten Regeln und Parameter](#rules)
- [Warum ist das Risiko bei ECG-Platinen mehr als nur ein Lötfehler?](#assembly-risk)
- [Warum müssen Sauberkeit, Rückstände und Hochimpedanz-Eingänge gemeinsam betrachtet werden?](#cleanliness)
- [Wie koppeln Flex, Funk und Stromversorgung Störungen in den ECG-Kanal zurück?](#mechanics-noise)
- [Wie sollte man die ECG-Bestückung vor Serienstart validieren?](#validation)
- [Nächste Schritte mit HILPCB](#next-steps)
- [Häufig gestellte Fragen (FAQ)](#faq)
- [Öffentliche Referenzen](#references)
- [Autoren- und Prüfhinweise](#author)

<a id="overview"></a>
## Was sollte man bei der ECG-Erfassungs-PCB-Bestückung zuerst prüfen?

Zuerst **Elektrodentyp, CMR-Pfad, Schutz hochimpedan­ter Knoten, mechanische Belastung und Verifikationsmethode**.

Das ist nicht nur eine Frage von "etwas besser bestücken". Laut TI entsteht 50/60Hz-Störeinkopplung in ECG-Systemen über Haut, Elektrodenkabel, Schutznetzwerke und RC-Mismatch auf der Platine. RLD, Faraday-Schirmung, Isolation und Nachverarbeitung helfen, ersetzen aber keine saubere Bestückungs- und Prozesskontrolle.

Eine robuste Reihenfolge ist meist:

1. **Zuerst klären, ob Nass-, Trocken- oder Patch-Elektroden verwendet werden**
2. **Dann die montagekritischen Punkte rund um AFE, RLD, Lead-off und Eingangsschutz identifizieren**
3. **Dann No-Clean vs. reinigbaren Prozess und Nacharbeitsgrenzen festlegen**
4. **Dann prüfen, ob Flex, Bluetooth, Akku und Ladestrukturen Störungen in den Analogbereich zurückspeisen**
5. **Am Ende Funktionstest und Rückverfolgbarkeit gemeinsam definieren**

Wenn das Projekt bereits im Prototyp- oder NPI-Stadium ist, sollte man die Prozessfenster von [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) und die Testgrenzen von [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) früh gemeinsam prüfen.

<a id="rules"></a>
## Übersicht der wichtigsten Regeln und Parameter

| Regel / Parameter | Beurteilung | Warum wichtig | Wie prüfen | Wenn ignoriert |
|---|---|---|---|---|
| Elektrodentyp | Nass, trocken, Patch oder Mehrkanal zuerst sauber trennen | Impedanz und Empfindlichkeit ändern sich stark | Lastenheft, AFE-Auswahl, Mechanikreview | Rausch- und Sauberkeitsbudget werden falsch angesetzt |
| Gleichtaktpfad | RLD, Schutzwiderstände, RC-Mismatch und Schirmung zusammen bewerten | Netzstörungen entstehen entlang des gesamten Pfads | Schaltplanreview plus Rauschtest nach Bestückung | 50/60Hz-Störung steigt |
| Schutz hochimpedan­ter Knoten | Rückstände, Feuchte und wiederholte Nacharbeit im Eingang vermeiden | Hochimpedanz reagiert stark auf Leckpfade | Sauberkeitsprüfung, Nacharbeitsgrenzen, Vergleichsmessung | Baseline-Drift und sporadisches Rauschen |
| Flexzone und Stecker | Bauteile, Stiffener, Biegebereich und Lötstellen zusammen prüfen | Mechanik beeinflusst die Niederfrequenzstabilität | Biegetest, Sichtprüfung, Funktionstest | Drift, Bruch oder Kontaktprobleme |
| Funk- und Power-Module | Bluetooth, Laden und PMIC als Rauschquellen betrachten | Schalt- und Digitalrauschen kann in das AFE zurückkoppeln | Tests in verschiedenen Betriebszuständen | Im Labor gut, im Gerät verrauscht |
| Funktionstest und Traceability | Ergebnisse müssen auf Board-ID und Los zurückführbar sein | Spätere Fehleranalyse ist sonst langsam | MES / Testlog / Losdaten | Root Cause bleibt unscharf |

<div style="background: linear-gradient(135deg, #f3f7f6 0%, #eef2f8 100%); border: 1px solid #d6dce8; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #5a8ca8; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #41697f; font-weight: 700;">CMR Is Assembly-Sensitive</div>
      <div style="margin-top: 8px; color: #243640;">Die Gleichtaktunterdrückung eines ECG wird nicht nur vom IC bestimmt. Elektroden, Kabel, Schutznetzwerk und Mismatch machen Bestückungsschwankungen direkt als Netzbrummen sichtbar.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4f7d6b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #375a4d; font-weight: 700;">Cleanliness Protects Input Leakage</div>
      <div style="margin-top: 8px; color: #23352f;">Im hochimpedanten ECG-Eingangsbereich müssen Rückstände, Feuchte und Nacharbeitszyklen gemeinsam kontrolliert werden. Gerade bei Trocken­elektroden werden daraus schnell sichtbare Driftprobleme.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #7d6d56; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #635543; font-weight: 700;">Wearables Add Mechanics</div>
      <div style="margin-top: 8px; color: #3a3127;">Ein hautnah getragenes Gerät ist nicht nur ein PCB-Thema. Wenn Flexzonen, Stiffener, Stecker und Ladeaufbau nicht früh eingefroren werden, kommt später mechanischer Stress in die Signalkette zurück.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #8c5f7c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6d4961; font-weight: 700;">Test What Ships</div>
      <div style="margin-top: 8px; color: #3d2535;">AOI und Einschaltprüfung reichen nicht. Verifiziert werden müssen Rauschen, Baseline und Lead-off unter realen Bedingungen mit Versorgung, Funk und angeschlossenen Elektroden.</div>
    </div>
  </div>
</div>

<a id="assembly-risk"></a>
## Warum ist das Risiko bei ECG-Platinen mehr als nur ein Lötfehler?

Fazit: **Die eigentliche Schwierigkeit ist nicht, ob Bauteile gelötet sind, sondern ob die komplette rauscharme Kette nach der Bestückung noch intakt ist.**

TI zeigt in `Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier`, dass die Umwandlung von Gleichtakt in Differenzsignal gemeinsam von Elektrodenimpedanz, Kabelimpedanz und dem Widerstands-, Kondensator- und Diodennetzwerk am Eingang bestimmt wird. Selbst mit 1%-Bauteilen kann die CMR durch Mismatch deutlich sinken.

Direkte Folgen für die Bestückung:

- **Jede Nacharbeit nahe am AFE kann die Symmetrie verändern**
- **Eingangsschutz, RLD-Pfad und Lead-off-Netzwerk müssen am bestückten Board bewertet werden**
- **Uneinheitlich montierte Schirme, Stecker oder Kabelerdungen führen zu lotabhängigem Netzbrummen**

Bei AFEs wie TI AFE4960 ist die Chip-Funktionalität öffentlich gut dokumentiert. Ob diese Leistung im Produkt ankommt, entscheidet jedoch die Montagequalität.

<a id="cleanliness"></a>
## Warum müssen Sauberkeit, Rückstände und Hochimpedanz-Eingänge gemeinsam betrachtet werden?

Fazit: **Weil ECG-Eingänge meist hochimpedant, niederfrequent und amplitudenarm sind, sodass schon kleine Leckpfade oder Verunreinigungen sichtbar werden.**

Analog Devices beschreibt für Trocken­elektroden eine nützliche Größenordnung: Nass­elektroden liegen oft im Bereich von **10kOhm**, Trocken­elektroden können **100 bis 1000 Mal** höher liegen, zum Beispiel bei **10MOhm**. Dann werden Bias-Ströme, Rückstände und Feuchte wesentlich kritischer.

Für die Montage heißt das konkret:

- Flussmittel- oder Ionenrückstände im Eingangsbereich vermeiden
- Sicherstellen, dass Reinigungsmedien unter dichten Bauteilen wirklich wirken
- Trocknung und Lagerung gegen Feuchterückkehr absichern
- Nacharbeit am hochimpedanten Bereich streng begrenzen

Ein projektbezogener Ansatz ist meist sinnvoller als ein pauschaler Sauberkeitsgrenzwert:

| Szenario | Geeignete Prozesslogik | Wichtige Prüfpunkte |
|---|---|---|
| Nass­elektrode, wenige Kanäle, Prototyp | Einfachere Reinigung kann reichen, aber mit Rausch-Retest | Nacharbeitszahl im Eingang, Baseline nach Reinigung |
| Trocken­elektrode, Wearable | Prozess aus Sicht des Hochimpedanz-Eingangs definieren | Eingangsleckstrom, Feuchte-Rauschen, Wiederholbarkeit |
| Flex- oder Starrflex-Version | Reinigung und Trocknung mit Mechanik zusammen betrachten | Stiffener-Grenzen, Steckerbereich, Retest nach Biegen |

<a id="mechanics-noise"></a>
## Wie koppeln Flex, Funk und Stromversorgung Störungen in den ECG-Kanal zurück?

Fazit: **Bei Wearable-ECG sitzt die Rauschquelle oft nicht nur am AFE-Eingang. Akku, Bluetooth, Laden, Schirmung und Flex-Aufbau können das Problem über die Montage zurückbringen.**

Typische zusätzliche Baugruppen sind:

- Bluetooth-RF und Antenne
- Ladeelektronik oder Wireless Charging
- PMIC / DCDC / LDO
- Flex-Steckverbinder oder FPC
- Gehäuse, Schirme und leitfähige Kontaktteile

WCT/RLD- und Shield-Drive-Hinweise von Analog Devices zeigen außerdem, dass ein getriebener Schirm in Wearables stabil kompensiert werden muss. Schirmung ist also kein später Universal-Fix.

Für die Prozessfreigabe sollten mindestens diese Punkte eingefroren werden:

1. **Dürfen AFE-, RLD- oder Schirmpfad später noch umplatziert oder ersetzt werden?**
2. **Bleiben Flexzonen, Stecker und Stiffener von empfindlichen Lötstellen und Hochimpedanz-Knoten fern?**
3. **Wurden Rausch-Retests unter Bluetooth-, Lade- und Anzeigeaktivität durchgeführt?**
4. **Sind Schirme, Federkontakte und leitfähige Verbindungen in der Serie reproduzierbar?**

<a id="validation"></a>
## Wie sollte man die ECG-Bestückung vor Serienstart validieren?

Fazit: **Entscheidend ist nicht die größte Anzahl an Tests, sondern dass die Bedingungen dem Auslieferungszustand entsprechen.**

Die öffentliche IEC-60601-2-47-Kontextbeschreibung verweist auf Sicherheit und essential performance von ambulanten ECG-Systemen. Für die Montage bedeutet das: Nicht bei AOI, Röntgen oder ICT stehen bleiben, sondern die reale Leistungsfähigkeit unter Nutzungsbedingungen prüfen.

Ein sinnvoller Vorserienpfad umfasst meist:

| Validierungspunkt | Was beantwortet er? | Wichtige Beobachtungspunkte |
|---|---|---|
| Einschalten und Grundfunktion | Ist die Basisbestückung vollständig? | AFE-Kommunikation, Lead-off, Referenzspannung, Ruhestrom |
| Analograuschen und Baseline | Hat die Montage die rauscharme Kette beschädigt? | Offeneingangsrauschen, Netzbrummen, Baseline-Stabilität |
| Kombinierter Betriebstest | Koppeln Systemmodule Störungen zurück? | Bluetooth, Laden, Display, Vibration |
| Mechanischer Retest | Entstehen durch Tragen, Biegen, Verbinden neue Fehler? | Flexzone, Stecker, Stiffener, Gehäusezustand |
| Traceability-Aufzeichnung | Lässt sich später eine Chargenanalyse durchführen? | Board-ID, Bauteillose, Prozessparameter, Testresultate |

Vor einem Validierungslos sollten Fertigung und Test mindestens diese Eingaben erhalten:

1. ECG-Lead-Struktur, AFE-Typ und RLD / Lead-off-Konzept  
2. Elektrodentyp und Trageform  
3. Ob Bluetooth, Laden, Flexzone oder Starrflex vorhanden sind  
4. Kriterien für Rauschen, Baseline und Funktion  
5. Rückverfolgbarkeit für Board-ID, Los, Reinigung / Nacharbeit und Funktionstest

<a id="next-steps"></a>
## Nächste Schritte mit HILPCB

- Wenn zuerst AFE-Bereich und Bestückungsfenster eingefroren werden müssen, lohnt sich der Einstieg über [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Bei Flexzonen, hautnahen Bauformen oder Starrflex-Versionen sollten Stiffener, Biegefenster und Montage gemeinsam mit [Rigid-Flex PCB](https://hilpcb.com/en/products/rigid-flex-pcb) bewertet werden.
- Vor Prototyp- und Validierungslose sollten Hochimpedanz-Eingänge, Sauberkeitsstrategie und Rausch-Retest in die [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) Phase hinein definiert werden.
- Wenn Bestückung, Materialeingang, Funktionstest und Rückverfolgbarkeit in einem Loop geschlossen werden sollen, gehören die Anforderungen direkt in [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) oder [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Häufig gestellte Fragen (FAQ)

<!-- faq:start -->

### Warum reichen AOI und Einschaltprüfung bei ECG-Platinen nicht aus?

Weil viele ECG-Probleme keine simplen Kurzschlüsse oder Unterbrechungen sind, sondern Netzstörungen, Baseline-Drift, Leckpfade oder mechanisch induzierte Instabilität.

### Warum reagieren Trocken­elektroden-ECGs empfindlicher auf die Montage?

Weil ihre Impedanz deutlich höher sein kann als bei Nass­elektroden. Dadurch werden Bias-Ströme, Rückstände, Feuchte und Leckpfade stärker verstärkt.

### Muss jede ECG-Platine gereinigt werden?

Nicht zwingend. No-Clean ist aber kein automatischer Sicherheitsstandard. Entscheidend sind Elektrodentyp, Hochimpedanz-Layout, Gehäuseunterseiten, Wearable-Umgebung und Nacharbeitsstrategie.

### Kann eine gute RLD-Auslegung Montageprobleme bei 50/60Hz vollständig kompensieren?

Nein. RLD verbessert die CMR, aber Verunreinigung, schlechter Schirmkontakt und Montageabweichungen können Netzbrummen trotzdem erhöhen.

### Warum sollte die Rückverfolgbarkeit bei medizinischem oder Wearable-ECG bis zur Platine reichen?

Weil viele Probleme aus kleinen Abweichungen zwischen Losen, Nacharbeit oder Mechanikänderungen entstehen und ohne Board-Level-Daten nur langsam eingegrenzt werden können.

<!-- faq:end -->

<a id="references"></a>
## Öffentliche Referenzen

1. [TI AFE4960 Datasheet](https://www.ti.com/lit/ds/symlink/afe4960.pdf)  
   Stützt den hier verwendeten Kontext zu ECG-, Respiration- und Pace-Detection sowie zum Bezug zu IEC 60601-2-47 / 60601-2-27.

2. [TI Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier](https://www.ti.com/lit/pdf/sbaa188)  
   Stützt die Aussagen zu 50/60Hz-Störquellen, RLD, Faraday-Schirmung, Isolation und CMR-Verlust durch Mismatch.

3. [TI Understanding Lead-Off Detection in ECG](https://www.ti.com/lit/pdf/sbaa196)  
   Stützt die Einordnung von Lead-off als Teil der ECG-Verifikationskette.

4. [Analog Devices: How to Add Wilson’s Central Terminal/Right Leg Drive Functions to the MAX30001/MAX30003 ECG AFEs in a Medical Wearable](https://www.analog.com/en/resources/design-notes/how-to-add-wilsons-central-terminalright-leg-drive-functions.html)  
   Stützt die Aussagen zu WCT / RLD, 50Hz / 60Hz-Unterdrückung und stabiler Shield-Drive-Kompensation.

5. [Analog Devices: High-Impedance and Low-Noise Op Amps Enable Dry Electrodes in Medical Systems](https://www.analog.com/en/resources/design-notes/highimpedance-and-lownoise-op-amps-enable-dry-electrodes-in-medical-systems.html)  
   Stützt den Kontext zu hoher Trocken­elektrodenimpedanz und den Anforderungen an Eingangsimpedanz, Bias-Strom und Rauscharmut.

6. [IEC 60601-2-47 Standard Listing](https://standards.iteh.ai/catalog/standards/iec/e9f39061-7265-48e4-9bda-3b71d1af3eba/iec-60601-2-47-2001)  
   Stützt den öffentlichen Kontext zu Sicherheit, essential performance, EMC und Genauigkeit bei ambulanten ECG-Systemen.

<a id="author"></a>
## Autoren- und Prüfhinweise

- Autor: HILPCB Content-Team für Medizinelektronik und Wearables
- Technische Prüfung: Team für PCB-Bestückungsprozess und rauscharme Hardware
- Letzte Aktualisierung: 2025-11-18

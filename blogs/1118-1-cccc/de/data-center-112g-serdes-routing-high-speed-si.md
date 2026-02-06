---
title: "Data-Center 112G SerDes Routing: Meistern der Herausforderungen von Ultra-High-Speed-Signalintegrität und verlustarmen PCBs"
description: "Tiefgehende Analyse der Kerntechnologie des Data-Center 112G SerDes Routing, umfassend High-Speed-Signalintegrität, thermisches Management und Power/Interconnect-Design, um Ihnen bei der Erstellung leistungsstarker PCBs mit hoher Signalintegrität zu helfen."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---

Mit dem explosionsartigen Wachstum von künstlicher Intelligenz (KI), maschinellem Lernen (ML) und Cloud Computing wächst der Datenverkehr in Rechenzentren mit beispielloser Geschwindigkeit. Um diese Nachfrage zu befriedigen, migriert die Branche rasch von der 56G NRZ/PAM4-Technologie zu 112G PAM4 SerDes. Dieser Sprung verdoppelt nicht nur die Rate pro Kanal, sondern bringt auch beispiellose Herausforderungen an die Signalintegrität (SI) bei Design und Fertigung von PCBs mit sich. Erfolgreiches **data-center 112G SerDes routing** ist nicht mehr nur eine einfache "Verbindung", sondern eine Systemtechnik, die Materialwissenschaft, elektromagnetische Feldtheorie, Thermodynamik und Präzisionsfertigung integriert. Als Ingenieur für Mess- und Konformitätsvalidierung werde ich die Kernschwierigkeiten und Reaktionsstrategien für das Design von 112G-SerDes-Verbindungen aus praktischer Sicht eingehend analysieren.

Von den BGA-Pads des Chip-Gehäuses über die PCB-Leiterbahnen, durch Steckverbinder und Backplane bis hin zum Empfänger – die Leistung dieses gesamten physikalischen Kanals bestimmt direkt, ob das 112G-Signal genau wiederhergestellt werden kann. Jede noch so kleine Impedanzdiskontinuität, übermäßiger dielektrischer Verlust oder nicht optimierte Via-Strukturen können zu einer drastischen Verschlechterung des Link-Budgets führen und letztendlich eine katastrophale Bitfehlerrate (BER) verursachen. Daher muss eine umfassende **high-speed 112G SerDes routing**-Strategie von Beginn des Designs an Faktoren wie Materialauswahl, Stackup-Design, Impedanzkontrolle und Fertigungstoleranzen berücksichtigen, um sicherzustellen, dass das Endprodukt nicht nur die elektrische Leistung erfüllt, sondern auch eine hohe Zuverlässigkeit und Herstellbarkeit aufweist.

### Warum ist das 112G SerDes Kanal-Budget so streng?

Beim Upgrade von 56G auf 112G stehen wir nicht nur vor einer Verdoppelung der Taktfrequenz. Die Nyquist-Frequenz des 112G PAM4-Signals (Pulsamplitudenmodulation mit vier Pegeln) erreicht 28 GHz, was bedeutet, dass das Signal während der Übertragung wesentlich empfindlicher auf Kanalverluste und Rauschen reagiert. Im Vergleich zu herkömmlichen NRZ-Signalen (Non-Return-to-Zero) ist das Augendiagramm des PAM4-Signals vertikal auf ein Drittel komprimiert, was den Signal-Rausch-Verhältnis-Spielraum (SNR) erheblich reduziert. Dies macht das Budget für die gesamte Einfügedämpfung (Insertion Loss, IL) zur kritischsten Einschränkung beim Design von **data-center 112G SerDes routing**.

Ein typisches Gesamtverlustbudget für einen 112G-Langstrecken-Link (LR) könnte auf weniger als 30-35 dB @ 28 GHz begrenzt sein. Dieses Budget muss auf jede Komponente im Kanal verteilt werden: Chip-Gehäuse, PCB-Leiterbahnen, Vias, Steckverbinder und Empfängergehäuse.

- **Einfügedämpfung (IL)**: Dies ist die größte Herausforderung. Bei 28 GHz haben herkömmliche Materialien wie FR-4 enorme Verluste und können die Anforderungen nicht erfüllen. Die Signalenergie wird im Dielektrikum als Wärme abgeführt, was zu einer Dämpfung der Signalamplitude und zum Schließen des Auges führt.
- **Rückflussdämpfung (RL)**: Verursacht durch Impedanzdiskontinuitäten im Kanal, wie Vias, Steckverbinder, BGA-Pads usw. Das reflektierte Signal überlagert sich mit dem Hauptsignal und bildet Intersymbolinterferenz (ISI), was die Signalqualität weiter verschlechtert.
- **Übersprechen (Crosstalk)**: Die hohe Verdrahtungsdichte macht die elektromagnetische Kopplung zwischen benachbarten Kanälen extrem schwerwiegend. Nahnebensprechen (NEXT) und Fernnebensprechen (FEXT) reduzieren direkt das Signal-Rausch-Verhältnis am Empfänger.
- **Kanalbetriebsspielraum (COM)**: Als fortschrittlicherer Link-Bewertungsindikator berücksichtigt COM umfassend Einfügedämpfung, Rückflussdämpfung, Übersprechen und die Fähigkeit des Equalizers (Entzerrer) und liefert schließlich einen Skalarwert, der die Link-Qualität misst. Im 112G-Design ist die Optimierung des Kanaldesigns durch COM-Simulation zum Industriestandard geworden.

Um das strenge Kanalbudget einzuhalten, müssen Designer den gesamten Link bereits in der Simulationsphase genau modellieren und eng mit erfahrenen Herstellern wie Highleap PCB Factory (HILPCB) zusammenarbeiten, um sicherzustellen, dass das Simulationsmodell in hohem Maße mit den tatsächlichen Fertigungsergebnissen übereinstimmt.

### Auswahl verlustarmer Materialien: Der Grundstein für 112G-Links

Materialien sind die physikalische Basis, die die Leistung von Hochgeschwindigkeitsverbindungen bestimmt. Bei einer Frequenz von 28 GHz spielen die Dielektrizitätskonstante (Dk) und der Verlustfaktor (Df) von PCB-Materialien eine entscheidende Rolle bei der Signaldämpfung. Die Wahl des richtigen verlustarmen Materials für **data-center 112G SerDes routing** ist der erste Schritt zu einem erfolgreichen Design.

- **Dielektrizitätskonstante (Dk) und Verlustfaktor (Df)**: Df ist ein Schlüsselindikator, der die Fähigkeit des Materials misst, elektromagnetische Energie zu absorbieren. Je niedriger der Df, desto geringer ist der dielektrische Verlust des Signals während der Übertragung. Für 112G-Links ist es im Allgemeinen erforderlich, Materialien mit extrem niedrigem Verlust (Ultra Low Loss oder Extremely Low Loss) mit einem Df von weniger als 0,004 @ 10 GHz zu wählen, wie z.B. Tachyon 100G, Megtron 6/7/8, Rogers RO4000-Serie usw. Gleichzeitig sind die Stabilität und Konsistenz von Dk entscheidend für **112G SerDes routing impedance control**.
- **Skin-Effekt (Skin Effect)**: Bei einer so hohen Frequenz wie 28 GHz neigt der Strom dazu, auf der Oberfläche des Leiters zu fließen, anstatt sich gleichmäßig über den gesamten Querschnitt zu verteilen. Dies führt zu einer Erhöhung des effektiven Widerstands des Leiters und erzeugt zusätzlichen Leiterverlust.
- **Kupferfolienrauheit (Copper Roughness)**: Eine raue Kupferfolienoberfläche erhöht die Länge des Übertragungspfades des Hochfrequenzstroms, verschärft dadurch den Skin-Effekt und führt zu größeren Verlusten. Daher wird im 112G-Design empfohlen, Kupferfolien mit extrem niedrigem Profil (VLP) oder hyper-niedrigem Profil (HVLP) zu verwenden, um den Leiterverlust zu minimieren.
- **Glasfasergewebe-Effekt (Fiber Weave Effect)**: Das PCB-Basismaterial ist ein Verbundwerkstoff aus Glasfasergewebe und Harz. Aufgrund der unterschiedlichen Dielektrizitätskonstanten von Glasgewebe (Dk≈6) und Harz (Dk≈3) ändert sich die effektive Dk, die die Leiterbahn "sieht", lokal, wenn sie parallel zu den Glasfaserbündeln verläuft, was zu Impedanzschwankungen und Timing-Abweichungen (Skew) führt. Um dieses Problem zu mildern, kann abgeflachtes Glasgewebe (Spread Glass) verwendet oder die Leiterbahnen mit einem winzigen Winkel (wie 1-5 Grad) verlegt werden.

Die Wahl der richtigen Materialkombination betrifft nicht nur die Leistung, sondern auch Kosten und Herstellbarkeit. Ein exzellenter **112G SerDes routing guide** sollte Designern raten, frühzeitig im Projekt mit PCB-Herstellern (wie HILPCB) zu kommunizieren, um Leistung, Kosten und Risiken in der Lieferkette auszugleichen.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Leistungsvergleich von Hochgeschwindigkeits-PCB-Materialien</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Materialklasse</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Typisches Material</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Verlustfaktor (Df @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dielektrizitätskonstante (Dk @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Anwendbare Rate</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standardverlust</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Mittlerer Verlust</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Niedriger Verlust</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra-niedriger Verlust</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Präzise Impedanzkontrolle und Routing-Strategie

Impedanzkontrolle ist der Kern der Signalintegrität bei hohen Geschwindigkeiten. Beim **high-speed 112G SerDes routing** führt jede Abweichung von der Zielimpedanz (normalerweise 90 oder 100 Ohm differentiell) zu Signalreflexionen, was Jitter und Intersymbolinterferenz erhöht. Die Realisierung einer präzisen **112G SerDes routing impedance control** erfordert Maßnahmen sowohl auf Design- als auch auf Fertigungsebene.

**Design-Ebene:**
1.  **Präzises Stackup-Design**: Verwenden Sie einen 2D-Feldlöser (wie Polar Si9000) oder einen in EDA-Tools integrierten Löser, um die differentielle Impedanz basierend auf dem Dk-Wert des gewählten Materials, der Schichtdicke, der Linienbreite, dem Linienabstand und der Kupferdicke genau zu berechnen. Fertigungstoleranzen müssen berücksichtigt und mit dem Hersteller hinsichtlich seiner Prozessfähigkeitsreichweite bestätigt werden.
2.  **Leiterbahngeometrie**:
    *   **Differentielle Intra-Pair-Anpassung**: Die Länge der beiden Leiterbahnen (P/N) des differentiellen Paares muss streng angepasst werden, um Gleichtaktrauschen-Umwandlung und Timing-Abweichungen zu vermeiden. Bei einer Geschwindigkeit von 112G liegt die erforderliche Anpassungsgenauigkeit normalerweise unter 1-2 mil.
    *   **Vermeidung spitzer Winkel**: Leiterbahnkurven sollten Bögen oder 45-Grad-Winkel verwenden und rechte Winkel (90 Grad) vermeiden, um Impedanzdiskontinuitäten zu reduzieren.
    *   **Kontinuität der Referenzebene**: Hochgeschwindigkeits-Differentialpaare müssen eine kontinuierliche Referenzmasse- oder Stromversorgungsebene haben. Das Routing über geteilte Bereiche verursacht abrupte Impedanzänderungen und schwerwiegende Signalintegritätsprobleme.

**Fertigungsebene:**
Die Prozesskontrollfähigkeit des Herstellers bestimmt direkt die endgültige Impedanzgenauigkeit. Führende Hersteller wie Highleap PCB Factory (HILPCB) gewährleisten Impedanzkonsistenz durch folgende Technologien:
- **Fortschrittlicher Ätzprozess**: Kontrolle der Toleranzen für Linienbreite und -abstand innerhalb eines Bereichs von ±5% oder sogar weniger.
- **Präzise Laminierungskontrolle**: Gewährleistung einer gleichmäßigen und konsistenten Dicke von Kern (Core) und Prepreg (PP).
- **TDR-Test**: Verwendung eines Zeitbereichsreflektometers (TDR) während der Produktion zur stichprobenartigen oder vollständigen Prüfung von Testcoupons, um zu überprüfen, ob die Impedanz der fertigen Platine innerhalb der Spezifikationen liegt (z. B. ±7%).

### Vias und Steckverbinder-Übergänge: Kritische Diskontinuitätspunkte im Link

In Mehrschicht-PCBs sind Vias (Durchkontaktierungen) unersetzliche Strukturen zur Realisierung der Verbindung zwischen Schichten, aber sie sind auch einer der Hauptpunkte für Impedanzdiskontinuitäten im **data-center 112G SerDes routing**. Ein nicht optimiertes Via, das Reflexionen und Verluste einführt, reicht aus, um den gesamten 112G-Link zum Scheitern zu bringen.

- **Via Stub (Via-Stichleitung)**: Wenn das Signal von der Oberflächenschicht zur Innenschicht übertragen wird, bildet der ungenutzte Teil des Vias einen "Stub". Dieser Stub schwingt bei hohen Frequenzen mit und verursacht bei bestimmten Frequenzen eine starke Signaldämpfung, die sich als offensichtliche "Kerbe" (Notch) auf der S21-Kurve der S-Parameter zeigt. Für ein 28-GHz-Signal ist selbst ein Stub von wenigen zehn Mil fatal. Die Lösung ist **Back-drilling (Rückbohren)**, d.h. das Wegbohren der überschüssigen Kupfersäule des Vias von der Rückseite der PCB, wobei die Stub-Länge auf unter 5-10 mil kontrolliert wird.
- **Via-Impedanzoptimierung**: Das Via selbst ist eine komplexe 3D-Struktur, deren Impedanz von der Größe des Pads, des Anti-Pads und des Via-Zylinders (Barrel) beeinflusst wird. 3D-Elektromagnetfeldsimulations-Tools (wie Ansys HFSS, CST) können verwendet werden, um die Via-Struktur zu optimieren, indem die Größe des Anti-Pads angepasst wird, um sie an die Leiterbahnimpedanz anzupassen und Reflexionen zu reduzieren.
- **Steckverbinder-Footprint-Optimierung**: Der Board-to-Board-Steckverbinder (wie QSFP-DD, OSFP) ist ein weiterer kritischer Übergangsbereich. Das Layout der BGA- oder SMT-Pads des Steckverbinders muss in Zusammenarbeit mit den PCB-Leiterbahnen optimiert werden, um einen glatten Impedanzübergang zu realisieren. Dies beinhaltet oft nicht-kreisförmige Pads (Non-Circular Pad) und fortschrittliche **112G SerDes routing layout**-Techniken wie lokales Aushöhlen der Referenzmasseebene.

Für komplexe Backplanes und Systemboards kann die [HDI PCB](https://hilpcb.com/en/products/hdi-pcb)-Technologie mit Microvias und Blind/Buried Vias kürzere Verbindungswege und geringere parasitäre Effekte bieten und ist ein wirksames Mittel zur Realisierung von hochdichtem **high-speed 112G SerDes routing**.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes Physical Layer Optimierung: Leitlinien für Vias und Übergangsstrukturen</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Für Impedanzkontinuität unter PAM4-Modulation und Optimierung der Gleichtaktunterdrückung</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Stub-Eliminierung und Back-drill Präzision</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Grundregel:</strong> Das 112G-Signal ist extrem empfindlich gegenüber **Stub-Resonanz**. Es muss ein vollständiges Back-drilling implementiert werden, wobei die Stub-Länge streng auf **&lt;8 mil** kontrolliert wird (besser als die im Branchenstandard üblichen 10 mil), um den ersten Resonanzpunkt über das nicht aktive Band von 40 GHz hinaus zu verschieben.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Elektromagnetische Feldkompensation des Anti-Pads</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Grundregel:</strong> Die Verwendung empirischer Werte ist verboten. Der Anti-Pad-Durchmesser und die Signal-Pad-Größe müssen durch **vollständige 3D-EM-Simulation** kooperativ optimiert werden, um die parasitäre Kapazität des Vias zu kompensieren und die differentielle Impedanzschwankung am Via innerhalb eines Bereichs von **±5%** des Zielwerts zu halten.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Konfiguration von Abschirm-Vias (Shadowing Vias)</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Grundregel:</strong> Symmetrische Anordnung von **2-4 Masse-Rückstrom-Vias** um das differentielle Via-Paar. Durch Verkürzung der Magnetfluss-Schleifenfläche des Rückstrompfades wird die Verbindungsinduktivität reduziert und eine Übersprechisolierung zwischen den Schichten von mehr als **-40dB** für empfindliche Kanäle bereitgestellt.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. BGA-Bereich Fan-out und Prozessauswahl</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Grundregel:</strong> Für BGAs mit einem Raster von 0,8 mm und weniger wird der **VIPPO (Via-in-Pad Plated Over)**-Prozess empfohlen, um Platz zu sparen und induktive Reaktanz zu reduzieren. Wenn ein "Dog-Bone"-Fan-out verwendet wird, muss für kurze Leiterbahnsegmente ein spezielles Breitenkompensationsdesign durchgeführt werden, um die Bildung lokaler hochfrequenter Diskontinuitätspunkte zu verhindern.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>HILPCB Fertigungstipp:</strong> Der Erfolg des 112G-Designs liegt in der <strong>Resttoleranz des Back-Drillings (Back-drill Tolerance)</strong>. Wir empfehlen, nicht nur die Gerber-Parameter in der Designphase zu überprüfen, sondern auch mit der Fabrik deren Feedback-Fähigkeit zum <strong>Laser-Back-Drilling</strong> oder tiefenkontrollierten Bohren (T-Control) zu bestätigen, um sicherzustellen, dass Abweichungen in der realen Produktion nicht zu unerwarteten Notch-Punkten im Frequenzbereich führen.
</div>
</div>

### Zentrale Überlegungen für das 112G SerDes Routing-Layout

Ein erfolgreiches **112G SerDes routing layout** ist nicht nur eine Frage des Verbindens von Drähten, es ist eine Kunst des Raums, der Isolation und des Timings. In Designs mit hoher Dichte ist Übersprechen nach der Einfügedämpfung die zweitgrößte Herausforderung.

- **Kanalabstand und Übersprechkontrolle**: Je größer der Abstand zwischen differentiellen Paaren, desto geringer das Übersprechen. Eine gängige Designregel ist die "3W"- oder "5W"-Regel (wobei W die Breite einer einzelnen Leiterbahn ist), d.h. der Mittenabstand der differentiellen Paare sollte mehr als das 3- oder 5-fache der Breite einer einzelnen Leiterbahn betragen. In Bereichen mit begrenztem Platz kann die Isolation durch Einfügen von Masse-Abschirmleitungen (Guard Trace) zwischen differentiellen Paaren verstärkt werden.
- **Stackup-Design und Verdrahtungsstrategie**:
    *   **Stripline vs. Microstrip**: Die Stripline-Struktur der inneren Schichten, die von zwei Referenzebenen oben und unten umgeben ist, bietet eine bessere EMI-Abschirmung und Signalisolation und ist die erste Wahl für das 112G-SerDes-Routing über lange Distanzen. Obwohl die Microstrip der Oberflächenschicht etwas geringere Verluste aufweist (da ein Teil der Feldlinien in der Luft liegt), ist sie anfälliger für externe Störungen.
    *   **Orthogonale Verdrahtung**: Die Verdrahtungsrichtung benachbarter Signalschichten sollte orthogonal sein (z.B. L3 ist horizontal, L4 ist vertikal), um das Übersprechen zwischen den Schichten zu reduzieren.
- **BGA-Bereich Fan-out (Breakout)**: Der BGA-Bereich von ASIC- oder FPGA-Chips mit hoher Pin-Anzahl ist der Bereich mit der höchsten Verdrahtungsdichte. Die Fan-out-Strategie beeinflusst direkt die Signalintegrität und Herstellbarkeit. Es ist notwendig, die Position der Vias, die Leiterbahnwege und die Schichtzuweisung sorgfältig zu planen, um zu vermeiden, dass dichte Via-Arrays die Referenzebene schwerwiegend teilen. Das Design dieses Teils erfordert normalerweise einen detaillierten **112G SerDes routing guide**, um Ingenieure anzuleiten.
- **Power Integrity (PI)**: Ein stabiles und rauscharmes Stromverteilungsnetzwerk (PDN) ist die Grundlage für den normalen Betrieb von SerDes-Transceivern. PDN-Rauschen wird direkt in Takt-Jitter umgewandelt und verschlechtert die Signalqualität. Daher ist es notwendig, eine ausreichende Anzahl und Vielfalt von Entkopplungskondensatoren zu platzieren und eine PDN-Impedanzsimulation durchzuführen, um eine niedrige Impedanz des Stromnetzes über den gesamten Frequenzbereich sicherzustellen.

### Entzerrung und Jitter: Co-Design vom Chip zum Kanal

Selbst mit den besten Materialien und optimalem Routing erzeugt ein PCB-Kanal von mehreren zehn Zoll Länge immer noch schwerwiegende Intersymbolinterferenzen (ISI). Moderne SerDes-Transceiver enthalten leistungsstarke digitale Signalverarbeitungs- (DSP) und Entzerrungsschaltungen (Equalization), um Kanalverluste zu kompensieren.

- **Sendeseitige Entzerrung (Tx EQ)**: Verwendet typischerweise Feed-Forward-Entzerrung (FFE), die hochfrequente Signalkomponenten durch Pre-Emphasis und De-Emphasis verstärkt und die Tiefpasscharakteristik des Kanals im Voraus kompensiert.
- **Empfangsseitige Entzerrung (Rx EQ)**:
    *   **Continuous Time Linear Equalizer (CTLE)**: Ein programmierbarer analoger Hochpassfilter, der verwendet wird, um hochfrequente Signale zu verstärken und das geschlossene Auge anfänglich zu "öffnen".
    *   **Decision Feedback Equalizer (DFE)**: Ein nichtlinearer Entzerrer, der die Interferenz des vorherigen Bits auf das aktuelle Bit (Rückwärts-ISI) basierend auf zuvor entschiedenen Bits eliminiert. DFE ist ein leistungsstarkes Werkzeug zur Bewältigung starker Reflexionen und ISI, ist jedoch empfindlich gegenüber Entscheidungsfehlern, was zu Fehlerfortpflanzung führen kann.

Das Ziel des PCB-Designs ist es, einen "gutartigen" Kanal zu schaffen, der es dem SerDes-Entzerrer ermöglicht, ihn leicht zu kompensieren, anstatt einen Kanal mit enormen Verlusten zu entwerfen und sich übermäßig auf die Fähigkeiten des Entzerrers zu verlassen. Ein zu komplexes Entzerrungsschema erhöht den Stromverbrauch, die Latenz und die Designkomplexität. Daher müssen SI-Ingenieure eng mit Chipherstellern zusammenarbeiten, um das IBIS-AMI-Modell ihres SerDes zu erhalten und das Kanaldesign und die Entzerrereinstellungen in der Simulation gemeinsam zu optimieren, um den besten COM-Spielraum zu erreichen.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4 Link-Simulationsvalidierungsbericht</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">Zusammenfassung der Channel Operating Margin (COM) Analyse</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Einfügedämpfung (IL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Zielgrenzwert: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Kanalbetriebsspielraum (COM)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Status: PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE Ziel: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Verlustabweichung (ILD)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Welligkeitskontrolle: Exzellent</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Zielgrenzwert: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Effektive Rückflussdämpfung (ERL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Reflexionsunterdrückung: Konform</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Zielgrenzwert: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
189: 💡 <strong>Ingenieurvorschlag:</strong> Der aktuelle IL beträgt -32dB, es verbleiben nur 3dB bis zur Budgetgrenze (-35dB). Angesichts der Dk/Df-Toleranzen in der Massenproduktion wird empfohlen, vor der Serienproduktion eine spezielle Monte-Carlo-Simulation für die <strong>HVLP-Kupferfolienrauheit</strong> des Materials durchzuführen.
</div>
</div>

### Vom Prototyp zur Massenproduktion: Analyse der Herstellbarkeit (DFM)

Selbst die perfekteste Designsimulation ist wertlos, wenn sie nicht wirtschaftlich und zuverlässig hergestellt werden kann. Die Design-Fertigungs-Zusammenarbeit ist der Schlüssel zum Erfolg von **data-center 112G SerDes routing**, insbesondere bei der Verarbeitung von **112G SerDes routing low volume**-Prototypen oder der groß angelegten Massenproduktion.

- **Einfluss von Fertigungstoleranzen**: Toleranzen im PCB-Herstellungsprozess, wie z.B. Ätzvariationen von Linienbreite/-abstand, Dickenvariationen während des Laminierungsprozesses, führen zu einer Abweichung der Impedanz des Endprodukts vom Designwert. Ein zuverlässiger Hersteller wie HILPCB stellt seinen detaillierten Prozessfähigkeitsleitfaden (Process Capability Guide) zur Verfügung, und Designer sollten diese Toleranzen bereits im frühen Designstadium in das Simulationsmodell integrieren und eine Monte-Carlo-Analyse durchführen, um die Leistung im Worst-Case-Szenario zu bewerten.
- **Oberflächenbehandlung**: Unterschiedliche Oberflächenbehandlungsprozesse haben unterschiedliche Auswirkungen auf Hochfrequenzsignale. Chemisch Nickel/Gold (ENIG) ist aufgrund seiner flachen Oberfläche und guten Leitfähigkeit die erste Wahl für Hochgeschwindigkeitsanwendungen. Aber Vorsicht vor dem "Black Pad"-Problem. ENEPIG bietet eine bessere Zuverlässigkeit. Die Wahl des Prozesses erfordert ein Abwägen von Kosten, Leistung und Lötzuverlässigkeit.
- **DFM-Prüfung**: Vor dem Senden der Design-Dateien (Gerber/ODB++) an den Hersteller ist es entscheidend, eine umfassende DFM-Prüfung (Design for Manufacturability) durchzuführen. Dies hilft, potenzielle Fertigungsprobleme wie zu kleine Bohrlöcher, zu schmale Kupferringe, Säurefallen (Acid Traps) usw. zu entdecken und teure Nacharbeiten zu vermeiden. Viele fortschrittliche PCB-Anbieter bieten kostenlose DFM-Analysedienste an.

Ob für die **112G SerDes routing low volume**-Prototypenvalidierung oder die Massenproduktion, die Wahl eines Partners mit fortschrittlicher Ausrüstung und strenger Prozesskontrolle ist entscheidend. Dies gewährleistet nicht nur die Leistung des ersten Produkts, sondern auch die Konsistenz von Charge zu Charge. Wir empfehlen die Wahl eines Anbieters wie HILPCB, der einen umfassenden Service von der [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb)-Fertigung bis zur Montage bietet, um die Lieferkette zu vereinfachen und Qualität zu sichern.

### Konformitätstest und Validierung: Sicherstellen, dass die Link-Leistung dem Standard entspricht

Als Messingenieur glaube ich, dass "ohne Messung kein Mitspracherecht" besteht. Das ultimative Ziel von Design und Simulation ist die Validierung durch physikalische Tests. Die Validierung von 112G SerDes-Links ist ein komplexer Prozess, der professionelle Ausrüstung und Methoden erfordert.

1.  **S-Parameter-Messung**: Verwenden Sie einen Vektor-Netzwerkanalysator (VNA), um Messungen im Frequenzbereich am PCB-Testboard oder dem gesamten Link durchzuführen und dessen S-Parameter zu extrahieren (einschließlich Einfügedämpfung Sdd21, Rückflussdämpfung Sdd11, Übersprechen usw.). Die gemessenen S-Parameter können mit den Simulationsergebnissen verglichen werden, um die Modellgenauigkeit zu überprüfen, und für die COM-Berechnung verwendet werden.
2.  **TDR-Impedanzmessung**: Verwenden Sie ein Zeitbereichsreflektometer (TDR), um die Impedanzkurven von differentiellen Leiterbahnen und Vias zu messen. Dies ermöglicht die intuitive Identifizierung von Ort und Schwere von Impedanzdiskontinuitäten im Link und ist ein leistungsstarkes Werkzeug zur Validierung der **112G SerDes routing impedance control**.
3.  **Augendiagramm- und BER-Test**: Schließen Sie einen Mustergenerator und einen Bitfehlerraten-Tester (BERT) an beide Enden des Links an, um die Link-Leistung unter realen Arbeitsbedingungen zu testen. Durch Beobachtung des Öffnungsgrades (Höhe und Breite) des Augendiagramms (Eye Diagram) am Empfangsende und Messung der Bitfehlerrate kann schließlich festgestellt werden, ob der Link die Designspezifikationen erfüllt (z.B. BER < 1E-6).

Diese Tests sind nicht nur in der F&E-Phase entscheidend, sondern auch für die Qualitätskontrolle in der Produktionsphase. Durch Stichprobentests an Produkten der Produktionslinie kann eine kontinuierliche Fertigungskonsistenz gewährleistet werden.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Fazit: Umfassende Zusammenarbeit ist der Schlüssel zum Erfolg

Zusammenfassend lässt sich sagen, dass erfolgreiches **data-center 112G SerDes routing** eine extrem herausfordernde Systemtechnik ist, die vom Designteam fundiertes Wissen in mehreren Bereichen und eine nahtlose Zusammenarbeit mit Fertigungspartnern erfordert. Von der Auswahl der richtigen Materialien mit extrem geringem Verlust über ein präzises Stackup-Design und Impedanzkontrolle bis hin zur sorgfältigen Optimierung von Diskontinuitäten wie Vias und Steckverbindern ist jedes Glied entscheidend.

Wir müssen über das traditionelle PCB-Design-Denken hinausgehen und den gesamten Link als ein einheitliches System betrachten. Nur durch frühzeitige Analyse mit fortschrittlichen Elektromagnetfeld-Simulationstools, kombiniert mit einem tiefen Verständnis der SerDes-Entzerrungsfähigkeiten und indem die Herstellbarkeit (DFM) immer an erster Stelle steht, können wir die beste Balance zwischen Leistung, Kosten und Zuverlässigkeit finden.

Für Unternehmen, die im Bereich 112G und höheren Geschwindigkeiten erfolgreich sein wollen, ist die Wahl eines Partners wie Highleap PCB Factory (HILPCB), der sowohl Design versteht als auch in der Fertigung exzellent ist, Ihre kluge Wahl, um die Herausforderungen von Ultra-High-Speed-Links zu meistern und die Markteinführung von Produkten zu beschleunigen. Wir bieten eine umfassende Lösung von der Materialauswahlberatung, DFM-Analyse bis hin zur hochpräzisen Fertigung und Testvalidierung, um sicherzustellen, dass Ihr **data-center 112G SerDes routing**-Design vom Entwurf zu einem leistungsstarken, zuverlässigen Produkt wird.

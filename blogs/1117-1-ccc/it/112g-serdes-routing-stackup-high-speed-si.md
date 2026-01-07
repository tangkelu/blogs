---
title: "112G SerDes routing stackup: affrontare stabilità dei link ultra-high-speed e sfide low-loss per PCB high-speed SI"
description: "Un deep dive su 112G SerDes routing stackup—Channel Budget, selezione materiali low-loss, impedance e crosstalk control, via/connector transitions, equalization/jitter e trade-off DFM per PCB high-speed SI."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["112G SerDes routing stackup", "112G SerDes routing reliability", "112G SerDes routing low volume", "low-loss 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing quick turn"]
---
Con la crescita esplosiva della domanda di banda in data center, AI e 5G communications, i data rate sono entrati nell’era dei 112Gbps/s. In questo contesto, la tecnologia 112G SerDes è diventata un core enabler per il high-speed interconnect di nuova generazione. Ma a queste velocità, PCB design e manufacturing affrontano sfide senza precedenti. Un **112G SerDes routing stackup** ben progettato non è più “solo lamination”: è systems engineering che combina materials science, teoria elettromagnetica e precision fabrication. Determina direttamente signal integrity, stabilità del link e, in ultima analisi, il successo del prodotto.

Questo articolo è un dettagliato **112G SerDes routing guide** dal punto di vista del design di connector e via-transition. Copriamo tutto: Channel Budget, selezione materiali, fino alla manufacturability, per aiutarti a gestire un dominio tecnico complesso. Per i team che sviluppano [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb) all’avanguardia, padroneggiare un **112G SerDes routing stackup** ottimizzato è un prerequisito. Highleap PCB Factory (HILPCB) sfrutta una profonda esperienza high-speed per supportare i clienti dal prototype al volume.

### Perché il 112G SerDes Channel Budget è così stretto?

Nel design 112G SerDes, tutto parte dal Channel Budget. Il Channel Budget definisce la massima perdita di segnale consentita e il noise margin lungo il link fisico dal transmitter (Tx) al receiver (Rx). Rispetto alle generazioni precedenti (28G/56G), il budget 112G è estremamente stretto—principalmente perché usa PAM4 signaling.

PAM4 trasporta 2 bit per symbol, dimezzando la baud rate e alleviando parte della pressione di banda, ma riduce la SNR di ~9.5dB e aumenta drasticamente la sensibilità a noise e attenuation. La frequenza di Nyquist del 112G PAM4 arriva a 28 GHz. A questa frequenza, PCB traces, vias e connectors introducono Insertion Loss (IL) significativa.

Un tipico canale 112G include più parti, ognuna delle quali consuma prezioso loss budget:
*   **ASIC package:** Substrate traces e vias nel BGA package sono i primi contributori di loss.
*   **PCB traces:** La principale fonte di loss—guidata da dielectric loss, conductor loss (skin effect e copper roughness) e lunghezza delle trace.
*   **Vias:** Through/blind/buried vias sono importanti impedance discontinuities che aggiungono reflection e loss extra, soprattutto su grandi [backplane PCB](https://hilpcb.com/en/products/backplane-pcb).
*   **Connectors:** Connettori high-speed come QSFP-DD e OSFP devono essere modellati con precisione, inclusa la PCB launch region.
*   **Cable assembly (opzionale):** Nei collegamenti rack-to-rack, anche il cable e i relativi connectors fanno parte del canale.

Il total channel insertion loss è tipicamente vincolato a ~30–35dB (@28GHz). Una perdita eccessiva in un singolo elemento può impedire il link bring-up o portare il BER fuori specifica. Per questo, channel modeling accurato e budget allocation sono il primo—e più critico—passo nel design di **112G SerDes routing stackup**.

### Come scegliere i materiali low-loss giusti?

La selezione dei materiali è la base del **low-loss 112G SerDes routing**. A 28GHz, la perdita dei tradizionali FR-4 è inaccettabile, quindi servono low-loss o ultra-low-loss laminates progettati per applicazioni high-speed. Le metriche core sono Dk e Df.

*   **Dk:** Influenza propagation speed e characteristic impedance. In high-speed design, serve un Dk stabile con la frequenza per ridurre dispersion. Un Dk più basso consente anche trace più larghe, riducendo conductor loss.
*   **Df:** Quantifica direttamente la dielectric loss. Per 112G SerDes, il Df a 28GHz dovrebbe essere sotto 0.004—spesso più vicino a 0.002.

Oltre a Dk/Df, due fattori sono altrettanto importanti:

1.  **Fiber Weave Effect:** La struttura periodica del fiberglass weave crea non-uniformità locale del Dk. Quando la lunghezza delle trace diventa comparabile al weave pitch, variazioni di impedenza e skew possono degradare il differential signaling. Mitigazioni comuni:
    *   Usare glass styles più “flat” (es. 1078, 1067).
    *   Usare Mechanically Spread Glass.
    *   Instradare con un piccolo angolo (es. 1–5°) rispetto al weave per evitare l’allineamento parallelo.

2.  **Copper Roughness:** Ad alta frequenza, lo skin effect forza la corrente sulla superficie del conduttore. Copper ruvido aumenta la lunghezza del percorso effettivo e il conductor loss. Usa copper molto smooth come VLP o ULP; tipicamente Rq dovrebbe essere sotto 2 µm.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#000000;">Confronto prestazioni materiali per high-speed PCB</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Classe materiale</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Dk tipico (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Df tipico (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Target data rate</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Indice costo</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Standard FR-4</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">4.2 - 4.8</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.015 - 0.020</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">1x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Mid-loss materials</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.6 - 4.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.008 - 0.012</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">10 - 28 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">2x - 3x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Low-loss (e.g., Megtron 6)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.2 - 3.6</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.002 - 0.004</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">28 - 112 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">5x - 8x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Ultra-low-loss (e.g., Tachyon 100G)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 3.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">112 Gbps and above</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">> 10x</td>
</tr>
</tbody>
</table>
</div>

### Quali sono le strategie chiave per impedance control e gestione crosstalk?

In **112G SerDes routing stackup**, impedance control precisa e forte soppressione del crosstalk sono due pilastri fondamentali della qualità del segnale.

**Impedance control:**
La differential impedance è tipicamente 100Ω o 90Ω, con tolleranze anche ±7% o persino ±5%. Ogni deviazione geometrica dall’impedenza target causa reflections, aumentando insertion loss e jitter. Fattori chiave:
*   **Trace width and thickness:** L’etch accuracy in manufacturing determina la linewidth finale.
*   **Dielectric thickness:** Il controllo dello spessore PP (Prepreg) post-lamination è critico.
*   **Material Dk:** La simulazione deve usare il Dk fornito dal laminate supplier che considera resin content e lamination conditions.

**Crosstalk management:**
Il crosstalk è rumore causato da EM coupling tra trace adiacenti. Nei sistemi 112G PAM4, dove la SNR è già bassa, il crosstalk è spesso il killer #1. Strategie comuni:
*   **Aumentare lo spacing:** Spacing differential-pair-to-pair spesso consigliato a 3W o più; sui link critici potrebbe servire 5W o più.
*   **Reference-plane continuity:** Assicurare reference GND/power planes continui sotto il high-speed routing; evitare crossing di plane splits.
*   **Routing ortogonale tra signal layer adiacenti:** Le direzioni di routing dovrebbero essere perpendicolari per ridurre broadside coupling.
*   **Ground-via shielding:** Posizionare Stitching Vias strategicamente attorno ai differential pair per creare un effetto Faraday-cage e isolare il rumore.

Un controllo efficace del crosstalk deve iniziare nella fase di stackup planning, usando 3D full-wave EM simulators (es. Ansys HFSS, CST) per previsione e ottimizzazione accurate.

### Quanto conta l’ottimizzazione delle transizioni di connector e vias?

Da specialista di design delle transizioni connector/via posso dirlo chiaramente: a 112G, la qualità delle transizioni stabilisce il limite superiore della channel performance. Una via o un connector pad non ottimizzati possono consumare facilmente diversi dB del budget in via loss e reflection.

**Via optimization:**
Una via è una struttura 3D complessa. La sua capacitance e inductance parassite creano severe impedance discontinuities a 28GHz. Tattiche chiave:
*   **Back-drilling:** Una delle tecniche più importanti. Rimuovendo l’unused via stub dal lato opposto, elimini risonanze a quarter-wavelength e migliori significativamente insertion loss e reflection. Il controllo della profondità di backdrill è un indicatore chiave della capability del produttore.
*   **Anti-pad optimization:** Aumentare l’apertura anti-pad nei reference planes riduce la capacitance parassita della via e porta l’impedenza più vicino alla transmission line.
*   **Remove NFP:** Rimuovere Non-Functional Pads sui layer interni riduce la capacitance parassita e migliora ulteriormente le prestazioni.
*   **Usare tecnologia [HDI PCB](https://hilpcb.com/en/products/hdi-pcb):** Microvias e pad più piccoli riducono drasticamente dimensioni fisiche e parassiti.
*   **Ground-via co-design:** Mettere 1–2 anelli di ground vias vicino alla signal via per fornire un low-inductance return path e sopprimere il coupling.

**Connector optimization (Launch Tuning):**
Gli array di pin dei connector high-speed (es. QSFP-DD) sono estremamente densi, rendendo difficile il design di pad e fan-out. Serve 3D simulation per fine-tuning di pad shapes, trace widths e reference-plane openings, in modo da matchare la connector impedance e ottenere una transizione smooth.

<div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(49, 27, 146, 0.1);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🧬 Via transitions: matrice di ottimizzazione per collegamenti verticali high-speed</h3>
<p style="text-align: center; color: #673ab7; font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Eliminare impedance jump e parassiti per proteggere la signal integrity 112G+</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">01. Mandatory Backdrill e stub removal</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Rimuovere completamente i via stubs per eliminare punti di risonanza ad alta frequenza. Per data rate sopra 28Gbps, mantenere la stub length rigorosamente entro <strong>< 10 mil</strong> per preservare la linearità di banda.</p>
</div>
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">02. Remove Non-functional Pads</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Rimuovere pad inutili dei layer interni. Ridurre la capacitance parassita migliora il comportamento TDR e abbassa la reflection nella transizione via.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">03. Anti-pad design preciso</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Usare un 3D full-wave solver per ottimizzare le dimensioni dell’Anti-pad. Fine-tuning di via-to-plane spacing per compensare l’induttanza locale e garantire <strong>impedance continuity</strong> nella transizione verticale.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">04. Ground-via enclosure tipo coassiale</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Posizionare <strong>GND Stitching Vias</strong> simmetricamente attorno alle signal vias per formare un return path tipo coassiale, isolando il via crosstalk e riducendo la return-loop inductance.</p>
</div>
</div>
<div style="margin-top: 30px; padding: 25px; background: #f1f5f9; border-radius: 16px; border-left: 8px solid #334155;">
<strong style="color: #1e293b; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 Connector Launch Tuning:</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;">Fine-tuning della fanout region per un connector specifico (es. QSFP-DD o PCIE 6.0). Regolando pad edges e lamination gaps rispetto al reference plane, assicurare una transition impedance smooth dal routing orizzontale al connector verticale e minimizzare la <strong>Total Insertion Loss</strong>.</p>
</div>
<div style="margin-top: 20px; padding: 20px; background: linear-gradient(90deg, #311b92, #673ab7); border-radius: 12px; color: #ffffff; text-align: center; font-size: 0.92em;">
💡 <strong>HILPCB manufacturing note:</strong> La backdrill depth tolerance impatta direttamente il comportamento del link 112G. Usiamo un advanced laser depth-control system per mantenere la <strong>Backdrill Tolerance entro ±2 mil</strong>, riducendo molto la reflection loss ad alta frequenza.
</div>
</div>

### Come influenzano equalization e jitter le prestazioni del link SerDes?

Anche con un **112G SerDes routing stackup** ottimizzato, una parte di channel loss rimane. I moderni SerDes includono circuiti di Equalization potenti per compensare. Blocchi comuni:
*   **Tx FFE:** La pre-emphasis aumenta le componenti high-frequency per contrastare il comportamento low-pass del channel.
*   **Rx CTLE:** Un amplificatore programmabile che boosta selettivamente l’high-frequency per appiattire la channel response.
*   **Rx DFE:** Equalizer non lineare che cancella ISI dai symbol precedenti.

L’obiettivo del PCB è fornire un channel “smooth e prevedibile”. Una risposta piena di risonanze e discontinuità brusche rende difficile la convergenza degli equalizer—o porta al failure.

Il jitter è una deviazione nel time domain ed è un altro grande nemico dei link high-speed. Sorgenti di jitter lato PCB includono:
*   **Fiber weave effects nel materiale.**
*   **Reflections da impedance discontinuities.**
*   **Power Supply Noise:** Il PDN noise si accoppia attraverso i SerDes power pins nel segnale e crea jitter—evidenziando l’importanza del co-design tra SI e PI.

Un stackup robusto riduce jitter e ISI al physical layer, riducendo la dipendenza dall’equalization del SerDes e migliorando la **112G SerDes routing reliability** complessiva.

### Come bilanciare DFM tra prestazioni e costo?

Un **112G SerDes routing stackup** teoricamente perfetto è inutile se non può essere prodotto in modo economico e affidabile. DFM va considerato presto. Gli ingegneri HILPCB sottolineano il coinvolgimento early per evitare manufacturability traps.

Considerazioni chiave DFM:
*   **Line width/spacing control:** I design 112G richiedono spesso 3/3mil (~75/75μm) o più fine, con richieste elevate su imaging ed etching.
*   **Drilling accuracy:** PCB ad alto layer count e alto Aspect Ratio richiedono allineamento molto accurato in mechanical e laser drilling.
*   **Backdrill depth control:** La backdrill depth tolerance influisce direttamente sulla stub length e richiede equipment avanzato di controllo Z-axis.
*   **Stackup symmetry:** Per ridurre lamination warpage, mantenere lo stackup il più simmetrico possibile.
*   **Surface finish:** A 28GHz, ENEPIG spesso supera ENIG grazie a migliore flatness, corrosion resistance e comportamento legato allo skin effect.

Nelle fasi iniziali—soprattutto con esigenze di **112G SerDes routing quick turn**—una collaborazione stretta con un produttore avanzato e una DFM review aiutano a evitare redesign tardivi e costosi e ad accelerare il time to market.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#FFFFFF;">Panoramica capability HILPCB per high-speed PCB manufacturing</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Process parameter</th>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max layer count</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Min line width/spacing</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">2.5 / 2.5 mil</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max Aspect Ratio</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Backdrill depth tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">+/- 2 mil (50μm)</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">±5%</td>
</tr>
</tbody>
</table>
</div>

### Come garantire la long-term reliability per 112G SerDes routing?

La **112G SerDes routing reliability** include non solo il rispetto dei target elettrici, ma anche operatività stabile lungo tutta la product life. Punti chiave:

*   **Thermal management:** Dispositivi 112G SerDes e optical modules dissipano potenza significativa; lo stackup deve fornire heat paths efficaci. Aggiungere thermal reference planes, usare materiali con migliore conducibilità termica e posizionare thermal vias in modo strategico aiuta a controllare la temperatura e prevenire performance drop o danni permanenti.
*   **Power Integrity (PI):** Un PDN a bassa impedenza e stabile è fondamentale. Decoupling placement corretto, power planes ampi e low-inductance via design sopprimono supply noise e forniscono “clean power” al SerDes.
*   **CAF resistance:** In PCB ad alta densità con gradienti elevati di campo elettrico, CAF è un potenziale failure mode. Selezionare materiali con alta CAF resistance e usare processi ottimizzati di drilling/plating è essenziale.
*   **Consistency testing:** Per volume production, creare test flow rigorosi—campionare la characteristic impedance con TDR e misurare S-parameters con VNA per garantire consistenza lot-to-lot.

### Come supporta HILPCB prototipi low-volume e quick-turn?

Sappiamo che iterazione rapida e prototype validation sono critiche per lo sviluppo 112G SerDes. Molti progetti partono con necessità **112G SerDes routing low volume**. HILPCB ha costruito un sistema produttivo flessibile, dal singolo prototype fino al full-scale volume.

Per progetti **112G SerDes routing quick turn**, offriamo:
*   **Expert DFM support:** Stackup recommendation gratuite e DFM analysis prima dell’ordine per bilanciare prestazioni e manufacturability.
*   **Strong material inventory:** Stock di laminates mainstream **low-loss 112G SerDes routing** (Isola, Rogers, Panasonic Megtron series, ecc.) per evitare lunghi lead time di approvvigionamento.
*   **Dedicated prototype line:** Una linea rapid-turn per consegnare high-speed PCB di alta qualità nel minor tempo possibile.
*   **One-stop service:** Oltre a PCB fabrication, supportiamo component sourcing e PCBA. La nostra [turnkey assembly](https://hilpcb.com/en/products/turnkey-assembly) può gestire la supply chain così puoi concentrarti su R&amp;D.

Che tu abbia bisogno di schede di validazione **112G SerDes routing low volume** o di ordini volume impegnativi, HILPCB ha capability ed esperienza per essere un partner affidabile.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Costruire un **112G SerDes routing stackup** robusto e affidabile è systems engineering complesso e richiede trade-off delicati tra SI, PI, thermal management e manufacturing. Dall’analisi rigorosa del Channel Budget, alla scelta accurata di materiali low-loss, fino all’ottimizzazione micron-level di via e connector transitions—ogni dettaglio conta.

Man mano che la tecnologia evolve verso 224G e oltre, questi principi e sfide diventeranno ancora più intensi. Scegliere un partner come HILPCB—che comprende sia la fisica di design sia un manufacturing top-tier—può essere un vantaggio decisivo. Non siamo solo un produttore, ma un compagno nell’innovazione tecnica, trasformando i blueprint più difficili in prodotti fisici ad alte prestazioni. Se stai lanciando il tuo prossimo programma high-speed e ti serve una soluzione affidabile di **112G SerDes routing stackup**, contatta i nostri esperti tecnici.


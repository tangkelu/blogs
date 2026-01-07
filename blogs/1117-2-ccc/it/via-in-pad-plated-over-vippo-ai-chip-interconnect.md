---
title: "Via-in-Pad plated over (VIPPO): affrontare packaging e high-speed interconnect per AI chip interconnect e substrate PCBs"
description: "Deep dive su Via-in-Pad plated over (VIPPO): Signal Integrity, Power Integrity, percorsi termici, controlli di processo e strategie di design costo‑efficaci per AI interconnect e IC substrate PCBs ad alte prestazioni."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad plated over (VIPPO)", "Copper pillar", "Hybrid stack-up (Rogers+FR-4)", "Backdrill quality control", "Heavy copper 3oz+", "Controlled impedance"]
---
Con la crescita esplosiva di AI, HPC e workload data center, i requisiti per l’hardware di base sono saliti a livelli senza precedenti. Power e throughput di AI accelerator, GPU e ASIC aumentano continuamente, imponendo sfide severe su IC substrate e PCB in design e manufacturing. In questo contesto, **Via-in-Pad plated over (VIPPO)** è passata da opzione a processo core: impatta direttamente SI, stabilità del PDN e efficienza del thermal management. Da una prospettiva di thermal interface design engineer, analizziamo l’essenza tecnica di **Via-in-Pad plated over (VIPPO)** e come risponde alle sfide di packaging e high‑speed interconnect per AI chip interconnect e substrate.

Nel design di HDI, soprattutto con BGA a 0.4 mm (o meno) di pitch, il classico fanout Dog‑bone non regge più la densità di routing. **Via-in-Pad plated over (VIPPO)** posiziona il via sotto il pad, lo riempie con materiale conduttivo o non conduttivo e poi placca la superficie per ottenere un pad planare e saldabile. Questo non solo libera spazio di routing, ma crea la base fisica per prestazioni elettriche e termiche estreme. Capire come HILPCB può ottimizzare il vostro design AI interconnect/substrate è un vantaggio competitivo.

### Cos’è Via-in-Pad plated over (VIPPO)?

In sintesi, **Via-in-Pad plated over (VIPPO)** è un processo avanzato di fabbricazione PCB che risolve la congestione di routing dovuta alla densità componenti. Il flusso standard include:

1.  **Drilling:** forare un via al centro del pad di BGA, LGA o altri SMD.
2.  **Via-wall plating:** placcare rame sulla parete del via per creare connessione interlayer.
3.  **Filling:** riempire completamente il via con epoxy dedicata conduttiva o non conduttiva. Step critico: i void possono espandersi in reflow e causare failure del giunto.
4.  **Planarization:** grinding o CMP per rendere la superficie del via a filo con il rame circostante.
5.  **Plated-over cap:** una seconda placcatura rame su via e pad per una superficie continua e liscia.
6.  **Surface finish:** ENIG, ImAg, OSP, ecc.

Rispetto al Dog‑bone, **Via-in-Pad plated over (VIPPO)** elimina la fan‑out trace tra pad e via, accorcia il percorso del segnale e permette di avvicinare i decoupling capacitors ai pin di alimentazione dell’IC. Per i substrate AI moderni, questo è un requisito abilitante.

### Come VIPPO migliora la Signal Integrity sui substrate AI?

I sistemi AI lavorano a decine/centinaia di Gbps (es. PCIe 6.0, HBM3e). A queste frequenze, micro‑difetti geometrici possono generare gravi problemi SI. **Via-in-Pad plated over (VIPPO)** è un “guardiano” della SI.

Primo: eliminando la fan‑out trace del Dog‑bone, VIPPO riduce molto la lunghezza dal solder ball BGA al routing interno, abbassando induttanza/capacità parassita e discontinuità d’impedenza. Per coppie differenziali con **Controlled impedance**, VIPPO rende la transizione più prevedibile e riduce riflessioni e jitter.

Secondo: VIPPO riduce l’impatto dei via stub. Nei multilayer tradizionali un through‑via attraversa tutti i layer; le porzioni non usate diventano stub che possono risuonare. **Backdrill quality control** rimuove lo stub ma aggiunge costo e processi. VIPPO combinata con blind/buried vias può evitare gli stub già in design, creando canali più puliti per SerDes e memory bus.

<div style="background-color:#F5F7FA;padding:20px;border-radius:8px;margin:20px 0;">
<h3 style="color:#000000;text-align:center;border-bottom:3px solid #64B5F6;padding-bottom:10px;">Confronto prestazioni tra tecnologie di via</h3>
<table style="width:100%;border-collapse:collapse;text-align:center;color:#000000;">
<thead style="background-color:#F5F5F5;color:#000000;">
<tr>
<th style="padding:12px;border:1px solid #ddd;">Caratteristica</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #4CAF50;">Via-in-Pad plated over (VIPPO)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #FFC107;">Dog-bone via (Dog-Bone Via)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #F44336;">Open via-in-pad (Via-in-Pad Open)</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Densità di routing</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Estremamente alta</b></td>
<td style="padding:12px;border:1px solid #ddd;">Bassa</td>
<td style="padding:12px;border:1px solid #ddd;">Alta</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Lunghezza percorso segnale</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Minima</b></td>
<td style="padding:12px;border:1px solid #ddd;">Lunga</td>
<td style="padding:12px;border:1px solid #ddd;">Corta</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Induttanza parassita</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Minima</b></td>
<td style="padding:12px;border:1px solid #ddd;">Alta</td>
<td style="padding:12px;border:1px solid #ddd;">Bassa</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Prestazioni termiche</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Eccellenti</b></td>
<td style="padding:12px;border:1px solid #ddd;">Scarse</td>
<td style="padding:12px;border:1px solid #ddd;">Medie</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Complessità di produzione</td>
<td style="padding:12px;border:1px solid #ddd;">Alta</td>
<td style="padding:12px;border:1px solid #ddd;">Bassa</td>
<td style="padding:12px;border:1px solid #ddd;">Media</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Affidabilità di saldatura</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Alta (void‑free)</b></td>
<td style="padding:12px;border:1px solid #ddd;">Alta</td>
<td style="padding:12px;border:1px solid #ddd;">Bassa (rischio solder wicking)</td>
</tr>
</tbody>
</table>
</div>

### Qual è il ruolo di VIPPO nel thermal management?

I chip AI moderni possono superare facilmente centinaia di watt di TDP e arrivare oltre 1000 W. Se il calore non viene smaltito, il chip throttle o si danneggia. **Via-in-Pad plated over (VIPPO)** funziona come canale termico micro.

Con filling termicamente conduttivo (o anche con epoxy non conduttiva dove domina il plated copper), VIPPO crea un percorso a bassa resistenza termica dal pad del chip verso piani GND/power interni. Questi piani agiscono da heat spreader. Per dispositivi ad alta potenza, spesso si usa un array VIPPO sotto la sorgente calda, formando una matrice di “thermal pillars”.

Questa soluzione board‑level lavora insieme a soluzioni package‑level (vapor chamber) e system‑level (fan, liquid cooling). Con piani **Heavy copper 3oz+**, la conduzione e distribuzione termica migliorano ulteriormente. Come produttore [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb), Highleap PCB Factory (HILPCB) può controllare incisione e lamination per integrare VIPPO con heavy copper in modo affidabile.

### Come VIPPO migliora la Power Integrity (PI)?

I chip AI richiedono PDN a impedenza bassissima per gestire grandi transitori di corrente (di/dt). **Via-in-Pad plated over (VIPPO)** aiuta PI in più modi.

Primo: connessioni power/ground più corte e dirette riducono l’induttanza dal piano al pin dell’IC. Con V = L * (di/dt), L più bassa significa meno rumore di alimentazione.

Secondo: VIPPO permette di posizionare i decoupling capacitors dietro il BGA quasi “back‑to‑back” ai pin power/ground, riducendo l’induttanza di loop e aumentando l’efficacia in alta frequenza.

Inoltre, VIPPO è sinergica con **Copper pillar** in advanced packaging: **Copper pillar** offre minore resistenza, maggiore capacità di corrente e migliore termica rispetto ai bump tradizionali ed è comune nel Flip‑Chip. VIPPO fornisce pad ad alta densità e bassa impedenza sul lato substrate, mantenendo basso il percorso di corrente fino al die.

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: -0.5px;">🚀 HILPCB: metriche chiave di produzione per substrate AI di nuova generazione</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Abilitare la potenza dei large model: densità estrema e architetture power ad alta corrente</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Capacità lamination ultra‑alta</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">56 <span style="font-size: 16px; font-weight: 600; color: #64748b;">Layers</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Competenza in **Any-layer HDI** e mixed lamination per stabilità strutturale su 800G switch e compute card.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">VIPPO &amp; microvia process</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">0.15 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mm</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Supporto a **Via-in-Pad** filling e plated‑over. Ottimizza fanout BGA e routing escape per AI con pin count elevatissimo.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Controllo impedenza estremo e SI</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">±5 <span style="font-size: 20px; font-weight: 600; color: #64748b;">%</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Allineamento rigoroso a **PCIe 6.0/7.0** con etch compensation ad alta precisione.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Gestione alta corrente e alta potenza</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">12 <span style="font-size: 20px; font-weight: 600; color: #64748b;">oz</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Soluzioni thick‑copper power layer per AI core fino a 1000W+ per ridurre drop e temperature rise del PDN.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Integrazione materiali avanzati</strong>
<p style="font-size: 1.1em; font-weight: 800; margin: 15px 0; color: #1e3a8a; line-height: 1.4;">ABF / Megtron 8 / Rogers</p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Supporto completo a **Ajinomoto Build-up Film (ABF)** e materiali RF Ultra‑Low Loss.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Tecnologia fine‑line e substrate</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">2/2 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mil</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Con **mSAP**, routing ultra‑fine per interconnect ad alta densità in architetture Chiplet.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #3b82f6; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Nota HILPCB:</strong> per substrate AI da 56 layer in su, la compatibilità <strong>Z-axis CTE</strong> è critica. Introdurre simulazione **Warpage** già in fase stackup per garantire coplanarità in reflow BGA.
</div>
</div>

### Impatto di VIPPO su stackup complessi

**Via-in-Pad plated over (VIPPO)** è fondamentale per HDI ultra‑dense e design complessi di [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb). Permette fanout BGA fine‑pitch senza aumentare layer count, importante per costi e spessore.

Nei sistemi mixed‑signal con RF e digitale high‑speed, **Hybrid stack-up (Rogers+FR-4)** è comune: usare [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) per RF e FR‑4/ABF‑like per digitale. VIPPO si adatta bene, garantendo densità e transizioni layer controllate per SI/PI.

VIPPO si combina con microvias (stacked/staggered) creando una rete 3D: portare segnali dalla superficie e poi trasferirli rapidamente tra layer via microvia, minimizzando connessioni Z‑axis.

### Punti di quality control nella fabbricazione VIPPO

**Via-in-Pad plated over (VIPPO)** è più complessa dei via standard; qualsiasi errore può creare problemi di reliability. I punti core:

1.  **Qualità del filling:** vacuum‑assisted filling per evitare void. I void possono espandersi in reflow e causare pad lifting, opens BGA o Head‑in‑Pillow.
2.  **Planarità:** grinding/polishing devono garantire coplanarità elevata (spesso ±0.5 mil). Non planarità impatta stampa pasta e soldering.
3.  **Adesione della copper cap:** la cap deve avere peel strength adeguata; altrimenti delaminazione sotto shock termico.
4.  **Precisione dimensionale:** controllo di diametro, posizione e dimensione pad.

Rispetto a **Backdrill quality control**, che si concentra su profondità e rimozione stub, la QC VIPPO attraversa filling, planarization e re‑plating e richiede Cpk più elevato. HILPCB usa AOI, X‑ray e micro‑section per monitorare i passaggi critici e mirare a IPC‑6012 Class 3 o superiore.

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.75em; font-weight: 800; letter-spacing: -0.5px;">🎯 Processo VIPPO: punti di sign‑off per high‑density design e manufacturing</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Guida core per ottimizzare densità fanout BGA e Signal Integrity</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">01. Void-free filling</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> filling completamente denso. Le bolle residue si espandono in reflow causando pad lifting o cracking del giunto.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">02. Surface planarity</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> la planarità determina lo yield di saldatura. Controllare etch‑back e grinding per minimizzare recess/protrusion ed evitare opens o HoP.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">03. Aspect ratio e plating challenges</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> via ad alto aspect ratio aumentano la difficoltà di penetrazione chimica e filling. Per thick boards, concordare parametri vacuum con il produttore per evitare underfill.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">04. Cost effectiveness e uso selettivo</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> VIPPO aumenta i costi; usarla solo dove serve: BGA core sotto 0.8 mm pitch o zone critiche per termica e return path/SI.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #2563eb; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Tip HILPCB:</strong> per pad VIPPO consigliamo una linea dedicata di cap plating <strong>POFV</strong> per aumentare peel strength e ridurre delaminazione in thermal cycling severo.
</div>
</div>

### VIPPO e advanced packaging (es. Copper Pillar)

Tecniche come 2.5D/3D (CoWoS, Foveros) sono cruciali: i chip si connettono tramite interposer o direct bonding in SiP. **Via-in-Pad plated over (VIPPO)** fa da ponte tra package complessi e main PCB.

Con **Copper pillar** l’impatto è ancora più evidente: rispetto ai solder bump, **Copper pillar** offre minore resistenza, maggiore corrente e migliore termica, ed è comune per Flip‑Chip. Il pitch ridotto richiede pad ad altissima densità e precisione. VIPPO crea pad planari che si accoppiano bene ai pillar, migliorando uniformità e performance dei canali, in particolare per HBM. Questo supporta obiettivi di [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Bilanciare benefici VIPPO e costi di produzione

**Via-in-Pad plated over (VIPPO)** è un processo value‑added più costoso dei via standard, per via di resin fill e step aggiuntivi (filling, planarization, seconda placcatura). La strategia migliore è l’uso selettivo: non tutti i componenti richiedono VIPPO.

Applicarla solo dove è essenziale: BGA ultra‑fine pitch, regioni fanout high‑speed, dispositivi che richiedono rafforzamento termico. Altrove, usare tecniche meno costose. Con un produttore esperto come HILPCB, il DFM anticipato aiuta a decidere dove VIPPO massimizza il ritorno prestazionale e dove microvia o altre soluzioni riducono il costo, anche in scenari **Hybrid stack-up (Rogers+FR-4)**. La nostra capacità [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) copre l’intero set di soluzioni.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione: VIPPO è una via obbligata per l’hardware AI del futuro

**Via-in-Pad plated over (VIPPO)** è passata da “nice‑to‑have” a tecnologia abilitante per AI e HPC di nuova generazione. Offre densità, SI superiore, percorsi termici efficaci e PDN stabile, risolvendo sfide chiave dei chip AI. Senza VIPPO, molti substrate design moderni sarebbero difficili da realizzare.

Per sfruttarne il potenziale, serve collaborazione stretta tra progettisti e produttore: regole di design, vincoli di manufacturing e checkpoint QC. Con HILPCB, potete contare su controllo **Controlled impedance**, esperienza **Heavy copper 3oz+** e competenza su interfacce come **Copper pillar** per passare dal design a una produzione affidabile.

Contattate HILPCB per un preventivo rapido e avviare il vostro progetto substrate AI: costruiamo insieme la prossima ondata tecnologica.


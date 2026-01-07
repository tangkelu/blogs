---
title: "THT/through-hole soldering: gestire le sfide high-speed interconnect per AI server backplane PCBs"
description: "Approfondimento su THT/through-hole soldering: SI, thermal management e power/interconnect design per aiutarti a realizzare AI server backplane PCBs ad alte prestazioni."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["THT/through-hole soldering", "AI server motherboard PCB mass production", "AI server motherboard PCB reliability", "AI server motherboard PCB stackup", "AI server motherboard PCB routing", "AI server motherboard PCB quick turn"]
---
Con la crescita esponenziale della domanda di calcolo AI e ML, l’hardware degli AI server affronta sfide senza precedenti. Come hub che collega compute, storage e network, il design e la produzione delle backplane PCBs determinano direttamente performance e stabilità del sistema. Sebbene l’SMT sia dominante, per connector che devono gestire high current, molti cicli di inserzione e forti stress meccanici, **THT/through-hole soldering** resta indispensabile per la sua affidabilità superiore.

Tuttavia, con PCIe 5.0/6.0 e oltre, il THT tradizionale diventa un SI bottleneck. Gestire le sfide di THT/through-hole soldering e bilanciare mechanical strength, PI e high-speed SI è un problema che tutti gli AI hardware engineer e i PCB manufacturer devono risolvere. Serve un’ottimizzazione end-to-end, dai materiali e stackup fino al processo di saldatura. HILPCB offre servizi avanzati di manufacturing e assembly per le esigenze della prossima generazione di AI server.

### Perché THT/through-hole soldering è ancora indispensabile nelle backplane degli AI server

L’SMT eccelle per densità e automazione, ma nelle backplane degli AI server il THT offre vantaggi fisici che l’SMT non può eguagliare, rendendolo la scelta preferita per il montaggio dei connector critici.

1.  **Mechanical strength e durabilità superiori:** i connector di backplane (es. Orthogonal Midplane Connectors, OCP NIC 3.0) sono grandi, con molti pin, e devono resistere a inserzioni frequenti. I pin THT attraversano il PCB e sono completamente bagnati dalla saldatura, creando un legame molto più robusto dei pad SMT. Questo è fondamentale per la **AI server motherboard PCB reliability** e riduce guasti da vibrazioni o urti.

2.  **Eccellente capacità di corrente:** accelerator cards (GPU, TPU) possono superare 1000W, richiedendo centinaia di ampere sulla backplane. Pin THT e barrel PTH hanno sezione maggiore dei pad SMT e portano corrente con minore resistenza e meno calore. Ciò stabilizza la PDN, riduce IR Drop e fornisce alimentazione “pulita” ai chip.

3.  **Percorsi termici semplificati:** i pin THT sono anche buoni conduttori di calore e trasferiscono il calore dei connector nei layer PWR/GND interni, che fungono da heat spreader.

Per questo, nel design AI server orientato alle prestazioni, THT/through-hole soldering non è una tecnologia “legacy”, ma una scelta strategica per high-reliability e high-power interconnect.

### High-speed SI: sfide dei THT vias e ottimizzazione

Nell’era 56/112 Gbps PAM4, il via del connector THT è una sfida SI principale. Via non ottimizzati degradano pesantemente il segnale.

*   **Via stub effect:** in multilayer PCBs, il segnale attraversa solo alcuni layer; la parte inutilizzata del via forma uno stub che risuona, causando riflessioni e Insertion Loss, fino a chiudere l’occhio.
*   **Impedance discontinuity:** la geometria a “barrel” del via crea un salto di impedenza, aumentando Return Loss e introducendo Jitter.
*   **Via-to-via Crosstalk:** nelle zone dense dei connector, i THT vias adiacenti si accoppiano elettromagneticamente, causando crosstalk, critico per le coppie differenziali.

Per risolvere serve **AI server motherboard PCB routing** e strategia di produzione di precisione. La tecnica più importante è **Back-drilling/Controlled Depth Drilling**, che rimuove lo stub dalla faccia opposta. Un processo efficace controlla lo stub residuo entro 10mil (~254μm), richiedendo alta accuratezza di profondità. Anche Anti-pad optimization, tuning dei reference planes e ground-via shielding aiutano a migliorare matching e ridurre crosstalk.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Confronto SI prima/dopo ottimizzazione THT via (simulazione @ 28 GHz)</h3>
<table style="width:100%; border-collapse:collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Metrica</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Standard THT via (unoptimized)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Optimized THT via (with back-drill)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Miglioramento</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Insertion Loss</td>
<td style="padding:12px; border:1px solid #ccc;">-4.5 dB (severe attenuation)</td>
<td style="padding:12px; border:1px solid #ccc;">-1.2 dB (significantly improved)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Improved 73%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Return Loss</td>
<td style="padding:12px; border:1px solid #ccc;">< -10 dB (strong reflection)</td>
<td style="padding:12px; border:1px solid #ccc;">< -18 dB (good match)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Reflection reduced > 8 dB</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Stub resonance point</td>
<td style="padding:12px; border:1px solid #ccc;">~15 GHz (limits bandwidth)</td>
<td style="padding:12px; border:1px solid #ccc;">> 40 GHz (moved out of band)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Resonance shifted > 160%</td>
</tr>
</tbody>
</table>
</div>

### Come lo stackup influisce sulla performance THT nelle backplane

Un **AI server motherboard PCB stackup** ben progettato è la base per THT ad alte prestazioni. Lo stackup definisce proprietà elettriche e impatta manufacturability e cost.

La scelta materiali è critica: per high-speed, le backplane usano spesso Ultra-Low Loss materials come Megtron 6/7 e Tachyon 100G, con Dk e Df molto bassi. Copper foils piatte (HVLP) e Spread Glass riducono il Fiber Weave Effect e migliorano l’uniformità d’impedenza delle coppie differenziali.

Layer count e spessore sono parametri chiave: tipicamente 20–40 layer e spessore >6mm. Questo rende il THT più difficile, soprattutto per l’Aspect Ratio. Fori ad alto aspect ratio (18:1+) richiedono plating di rame estremamente uniforme; punti sottili possono causare open o problemi di reliability.

Infine, la continuità dei reference planes garantisce un return path pulito. Nell’area connector, ogni via di segnale deve avere un piano di riferimento GND/PWR vicino e continuo. Split e void interrompono il ritorno e aumentano EMI e crosstalk. Il team HILPCB può supportare con esperienza su [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Power integrity (PI): sfide high current dei THT connector

Le backplane devono alimentare centinaia/migliaia di core in modo stabile. I THT connector sono elementi chiave e la PI influenza direttamente la stabilità di sistema.

La sfida principale è gestire la corrente elevata e l’IR Drop. Un connector per GPU può trasportare >500A a 12V o 48V. Anche con bassa resistenza dei pin, si crea un drop su tracce, vias e pin. Un drop eccessivo porta undervoltage, throttling o crash.

Soluzioni:
*   **Heavy copper / ultra-heavy copper:** usare rame 3oz+ su PWR/GND per ridurre la resistenza dei piani. HILPCB offre [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb).
*   **Ottimizzare il power path:** tracce power ampie e corte e più THT pins/vias in parallelo per ridurre la resistenza.
*   **Decoupling preciso:** decoupling vicino al power connector per transients e riduzione del noise.

Un PDN robusto è la base per yield e stabilità di **AI server motherboard PCB mass production**.

<div style="background:linear-gradient(135deg, #E1BEE7, #CE93D8); color:#311B92; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#311B92;">Key points for THT power integrity design</h3>
<ul style="list-style-type: none; padding-left: 0;">
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Minimize loop inductance:</strong> PWR e GND adiacenti e return path corto.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Control IR Drop:</strong> calcolare con PI simulation e ottimizzare con heavy copper o più planes.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Strategic decoupling:</strong> rete multi-livello tra connector e load (es. VRM).</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Electro-thermal co-design:</strong> valutare Joule heating nei percorsi high current e proteggere **AI server motherboard PCB reliability**.</li>
</ul>
</div>

### Thermal management e reliability per THT soldering

La saldatura è l’ultimo step e il più critico. Per backplane spesse e ad alta thermal mass, Wave Soldering è difficile: la PCB assorbe calore e la zona di saldatura può rimanere fredda, generando cold joint o open.

Per questo i processi moderni usano spesso:
*   **Selective Soldering:** nozzle mini che salda solo l’area dei pin THT, controllando il calore ed evitando thermal shock agli SMT; ideale per SMT+THT.
*   **Pin-in-Paste / Intrusive Reflow:** stampare pasta nei fori, inserire i pin e refloware l’intera scheda. La pasta fonde e riempie il barrel, formando giunti affidabili. Compatibile con SMT, semplifica il flusso e favorisce **AI server motherboard PCB quick turn**.

La reliability a lungo termine richiede conformità IPC-A-610 sul Barrel Fill (tipicamente 75%+). Per evitare void o crack, è necessario X-Ray come ispezione non distruttiva.

### DFM: manufacturability e yield delle THT backplane

Anche un [backplane PCB](https://hilpcb.com/en/products/backplane-pcb) perfetto in teoria può fallire in produzione se DFM è ignorato. Per backplane THT complesse, DFM è cruciale.

*   **Aspect Ratio:** spessore / diametro di foratura minimo. Troppo alto riduce la qualità del plating al centro del foro. Serve rispettare la capability del produttore.
*   **Annular Ring:** anello di rame attorno al foro. Deve essere sufficiente per tolleranze di drilling secondo class IPC.
*   **Spacing e tolerances:** hole-to-copper, hole-to-hole e back-drill depth tolerance influenzano performance elettrica e yield.

HILPCB offre DFM analysis gratuita: review dei file prima della produzione, identificazione rischi e suggerimenti di ottimizzazione per supportare **AI server motherboard PCB mass production**.

<div style="background-color:#1A237E; color:white; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:white;">HILPCB high-complexity backplane manufacturing capability</h3>
<table style="width:100%; border-collapse:collapse; color:white;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">Process parameter</th>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">HILPCB capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max layer count</td>
<td style="padding:12px; border:1px solid #7986CB;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max PCB thickness</td>
<td style="padding:12px; border:1px solid #7986CB;">10.0 mm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max drill aspect ratio</td>
<td style="padding:12px; border:1px solid #7986CB;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Back-drill depth control</td>
<td style="padding:12px; border:1px solid #7986CB;">± 50 µm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #7986CB;">± 5%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Supported materials</td>
<td style="padding:12px; border:1px solid #7986CB;">Megtron 6/7, Rogers, Tachyon 100G, etc.</td>
</tr>
</tbody>
</table>
</div>

### Come HILPCB realizza THT/through-hole soldering ad alta affidabilità

HILPCB integra advanced equipment, controllo di processo rigoroso e competenza ingegneristica per assicurare che ogni operazione di THT/through-hole soldering raggiunga standard elevati.

1.  **Advanced manufacturing & assembly equipment:** drilling meccanico/laser di precisione, plating lines avanzate e automazione per selective soldering e intrusive reflow, garantendo consistenza.
2.  **Controllo qualità rigoroso:** AOI per inner-layer, X-Ray per registrazione multilayer e barrel fill THT. Test elettrici e di reliability (es. thermal shock) assicurano che ogni [backplane PCB](https://hilpcb.com/en/products/backplane-pcb) sia robusta.
3.  **One-stop solution:** dall’ottimizzazione di **AI server motherboard PCB stackup** e **AI server motherboard PCB routing**, al quick turn e alla produzione di massa, fino al servizio [through-hole assembly](https://hilpcb.com/en/products/through-hole-assembly), HILPCB offre una consegna end-to-end che migliora qualità e riduce time-to-market per **AI server motherboard PCB quick turn**.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione

In sintesi, **THT/through-hole soldering** resta cruciale nelle moderne backplane AI server. Non è più “semplice saldatura a inserzione”, ma un engineering complesso che unisce high-speed SI, PI, thermal management e precision manufacturing. Il successo richiede collaborazione stretta tra designer e produttori esperti come HILPCB.

Con back-drilling avanzato, stackup ben progettato, PDN robusto e processi di saldatura controllabili, possiamo combinare l’affidabilità del THT con i requisiti di trasmissione high-speed. Se stai sviluppando AI server, switch o HPC di nuova generazione e cerchi un partner che sappia risolvere le sfide THT/through-hole soldering, HILPCB è la scelta ideale.


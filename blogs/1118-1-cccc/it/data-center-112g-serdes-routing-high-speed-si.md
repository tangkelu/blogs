---
title: "data-center 112G SerDes routing: Vincoli SI per link ultra‑veloci e low‑loss"
description: "Analisi di data-center 112G SerDes routing: channel budget, materiali, stack-up, Impedance Control, transizioni via/connector, DFM e validazione per PCBs high-speed SI."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---
Con la crescita esplosiva di AI, ML e cloud computing, il traffico nei data center sta aumentando a velocità mai viste. Per reggere, il settore sta migrando rapidamente da 56G NRZ/PAM4 a 112G PAM4 SerDes. Questo salto non è solo “raddoppiare la rate”: cambia completamente le regole della SI. Una **data-center 112G SerDes routing** di successo è system engineering che unisce materiali, elettromagnetismo, termica e precision manufacturing. Da prospettiva measurement e compliance, qui analizziamo le sfide principali e le strategie pratiche per i canali 112G.

Dal BGA pad del package, alle tracce PCB, alle vias, ai connettori/backplane, fino al ricevitore: la qualità del canale fisico determina se il segnale 112G può essere recuperato. Discontinuità d’impedenza, eccesso di loss o via non ottimizzate possono distruggere il budget e portare a BER disastrosi. Una strategia **high-speed 112G SerDes routing** deve includere da subito materiali, stack-up, Impedance Control e tolleranze di fabbricazione per ottenere prestazioni, affidabilità e producibilità.

### Perché il channel budget 112G è così severo?

Passare da 56G a 112G non è solo raddoppiare il clock. Con 112G PAM4, Nyquist arriva a 28 GHz, quindi loss e noise sono molto più critici. Rispetto a NRZ, l’occhio PAM4 è compresso a un terzo in verticale e la SNR margin cala. Il budget di Insertion Loss (IL) è quindi uno dei vincoli più stringenti in **data-center 112G SerDes routing**.

Un canale 112G long‑reach (LR) tipico può essere limitato a ~30–35 dB @ 28GHz, distribuiti tra package, tracce PCB, vias, connettori e ricevitore.

- **Insertion Loss (IL):** il problema principale; FR-4 è troppo loss a 28 GHz.
- **Return Loss (RL):** da discontinuità (vias, connector, BGA). Le riflessioni generano ISI.
- **Crosstalk:** alta densità → NEXT/FEXT aumentano e riducono SNR.
- **COM:** Channel Operating Margin integra IL/RL/crosstalk e capacità Equalizer; COM è lo standard per l’ottimizzazione 112G.

Servono modelli end‑to‑end accurati in simulazione e collaborazione stretta con un produttore esperto (es. HILPCB) per allineare modello e realtà.

### Materiali low‑loss: la base del link 112G

Il materiale è il limite fisico del canale. A 28 GHz, Dk e Df dominano l’attenuazione. La scelta del materiale giusto è il primo passo per **data-center 112G SerDes routing**.

- **Dk e Df:** per 112G spesso servono materiali Ultra Low Loss (Df < 0.004 @ 10GHz), come Tachyon 100G, Megtron 6/7/8, Rogers RO4000. Stabilità Dk = chiave per **112G SerDes routing impedance control**.
- **Skin Effect:** corrente superficiale → maggiore resistenza efficace → loss.
- **Copper Roughness:** rame ruvido aumenta percorso e loss; usare VLP/HVLP.
- **Fiber Weave Effect:** vetro (Dk≈6) vs resina (Dk≈3) → variazioni di Dk effettivo, ripple d’impedenza e skew; mitigare con Spread Glass e routing inclinato 1–5°.

La scelta materiale è anche un trade‑off cost/DFM/supply; un buon **112G SerDes routing guide** suggerisce allineamento early con il produttore.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Confronto materiali per high-speed PCB</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Classe materiale</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Materiali tipici</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Df @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dk @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Rate tipica</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standard loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Medium loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Impedance Control e disciplina di routing

Impedance Control è il cuore della SI. In **high-speed 112G SerDes routing**, qualsiasi deviazione dalla target impedance (tipicamente 90Ω o 100Ω diff) aumenta riflessioni, jitter e ISI. Servono azioni di design e manufacturing.

**Design:**
1.  **Stack-up accurato:** 2D solver (es. Polar Si9000) con Dk, spessori, width/spacing e copper thickness; includere tolleranze e allinearsi col produttore.
2.  **Geometria:**
    *   **Match P/N:** tipicamente entro 1–2 mil.
    *   **Evitare 90°:** archi o 45°.
    *   **Reference plane continuo:** evitare split.

**Manufacturing:**
- **Etching avanzato:** tolleranze L/S strette.
- **Controllo lamination:** spessori Core/PP uniformi.
- **Test TDR:** coupon in produzione per verificare ±7% ecc.

### Vias e transizioni con connettori

Le vias sono spesso la principale discontinuità in **data-center 112G SerDes routing**.

- **Via Stub:** risonanze e notch in S21; usare **Back-drilling** per stub 5–10 mil.
- **Ottimizzazione via:** 3D EM (HFSS, CST) per pad/antipad/barrel e riduzione riflessioni.
- **Footprint connettore:** QSFP-DD/OSFP richiedono co‑ottimizzazione; Non-Circular Pad e local ground clearances sono tecniche **112G SerDes routing layout**.

Microvias e blind/buried vias in [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) riducono parasitiche e aiutano il high-density routing.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes PHY: regole per vias e transizioni</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Continuità d’impedenza e soppressione common-mode in PAM4</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Eliminazione stub e precisione Back-drill</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> 112G è estremamente sensibile alle <strong>risonanze stub</strong>. Back-drill full‑depth e stub **&lt;8 mil** per spostare la prima risonanza oltre 40GHz.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Compensazione Antipad via 3D EM</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> niente euristiche: usare <strong>3D full-wave EM</strong> per co‑ottimizzare diametro antipad e pad, compensando la capacità parassita e tenendo la variazione di impedenza diff entro **±5%**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Shadowing Vias</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> posizionare **2–4 ground return vias** simmetriche attorno a ogni coppia via diff, riducendo loop area e ottenendo isolamento &lt; **-40dB**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. Breakout BGA e scelta processo</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Regola:</strong> per BGA 0.8mm e sotto, preferire **VIPPO**. Se si usa dog‑bone, compensare la width del breve segmento per evitare discontinuità HF locali.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Nota HILPCB:</strong> il successo 112G dipende spesso dalla <strong>Back-drill Tolerance</strong>. Oltre ai parametri Gerber, confermare capacità di <strong>Laser Back-drilling</strong> o controllo profondità (T-Control) per evitare notch inattesi in frequenza.
</div>
</div>

### Considerazioni layout per 112G SerDes

Un **112G SerDes routing layout** efficace è un equilibrio tra spazio, isolamento e timing; in high density, il crosstalk è la seconda sfida dopo IL.

- **Spacing:** regola 3W/5W; in aree strette, usare Guard Trace a massa.
- **Stack-up e strategia:**
    *   **Stripline vs Microstrip:** Stripline interna offre migliore schermatura EMI; Microstrip può avere loss leggermente minore ma è più sensibile.
    *   **Routing ortogonale:** layer adiacenti con direzioni ortogonali.
- **Breakout BGA:** pianificare vias/percorsi/layer senza frammentare reference planes; serve un **112G SerDes routing guide**.
- **Power Integrity (PI):** rumore PDN → jitter; decoupling e PDN impedance simulation per mantenere impedenza bassa su tutta la banda.

### Equalization e jitter: co‑design chip‑channel

Anche con ottimi materiali, canali lunghi generano ISI. I SerDes moderni compensano con DSP/Equalization.

- **Tx EQ:** FFE con Pre-emphasis/De-emphasis.
- **Rx EQ:** CTLE e DFE (potente ma sensibile a error propagation).

L’obiettivo PCB è un canale “ben comportato” che l’equalizer compensa facilmente. Con IBIS-AMI si ottimizza in simulazione canale ed equalizer per massimizzare COM margin.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4: report di sign-off simulazione</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">Sintesi Channel Operating Margin (COM)</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Insertion Loss (IL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">COM</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Status: PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE target: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ILD</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Ripple: good</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ERL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Reflection: compliant</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
💡 <strong>Nota:</strong> IL = -32dB, solo 3dB dal limite -35dB. Considerate le tolleranze Dk/Df in produzione, eseguire Monte Carlo sulla <strong>HVLP copper roughness</strong>.
</div>
</div>

### Dal prototipo alla produzione: DFM

Un design simulato perfetto vale poco se non è producibile. Per **data-center 112G SerDes routing** è cruciale co‑ottimizzare design e manufacturing, sia in **112G SerDes routing low volume** sia in volume.

- **Tolleranze manufacturing:** etching e lamination spostano impedenza; usare Process Capability Guide e Monte Carlo.
- **Surface finish:** ENIG è spesso preferito ma attenzione a “black pad”; ENEPIG migliora reliability. Trade‑off tra costo, performance e saldabilità.
- **DFM check:** prima di Gerber/ODB++ eseguire DFM (drill, annular ring, Acid Traps) per evitare rework.

Partner con equipment e process control (es. HILPCB) garantisce prestazioni e consistenza tra lotti, con servizio one‑stop da [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) a assembly.

### Test e validazione

1.  **S‑parameters:** VNA, Sdd21/Sdd11/crosstalk; confronto con simulazione e COM.
2.  **TDR:** profilo impedenza di tracce e vias per verificare **112G SerDes routing impedance control**.
3.  **Eye e BER:** pattern generator + BERT; Eye Diagram e BER (es. BER < 1E-6).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione

La **data-center 112G SerDes routing** è system engineering: materiali ultra low‑loss, stack-up e Impedance Control precisi, ottimizzazione di vias e connector. Serve trattare il canale come un unico sistema, usare EM simulation early, capire Equalization e mettere DFM al primo posto per bilanciare performance/costo/reliability.

Scegliere un partner come Highleap PCB Factory (HILPCB) accelera lo sviluppo: supporto one‑stop da consulenza materiali e DFM a produzione ad alta precisione e validazione, per trasformare il progetto **data-center 112G SerDes routing** in un prodotto affidabile e ad alte prestazioni.


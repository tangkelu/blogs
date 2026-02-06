---
title: "Via-in-Pad Plated Over (VIPPO): Padroneggiare le sfide di collaborazione opto-elettronica e consumo termico nei PCB del modulo ottico del data center"
description: "Analisi approfondita delle tecnologie essenziali per Via-in-Pad Plated Over (VIPPO), coprendo l'integrità dei segnali ad alta velocità, la gestione termica e la progettazione dell'alimentazione/interconnessione per aiutarti a costruire PCB del modulo ottico del data center ad alte prestazioni."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad Plated Over (VIPPO)", "Microvia/via impilata", "Rame pesante 3oz+", "Stackup ibrido (Rogers+FR-4)", "Impedenza controllata", "Pilastro di rame"]
---

Con il traffico del data center che cresce esponenzialmente, le richieste di soluzioni di interconnessione a larghezza di banda più elevata e consumo energetico inferiore diventano urgenti. La tecnologia Co-Packaged Optics (CPO), che integra i motori ottici e gli ASIC di commutazione sullo stesso substrato, è considerata il breakthrough chiave che supera i colli di bottiglia dei moduli ottici plug-in tradizionali. Tuttavia, questa integrazione senza precedenti porta anche gravi sfide di progettazione e fabbricazione PCB.

Come ingegnere CPO, comprendo profondamente che nella collaborazione opto-elettronica e nei compromessi di consumo termico, la tecnologia di interconnessione PCB avanzata è la base del successo. Tra questi, la tecnologia **via-in-pad plated over (VIPPO)** è il nucleo per padroneggiare questa complessità. Non è semplicemente la chiave della realizzazione del routing ultra-alta densità, ma il punto di appoggio dell'efficienza dell'integrità del segnale e della gestione termica.

## Routing a livello di board CPO e collaborazione dell'interfaccia opto-elettronica: Valore essenziale di VIPPO

Nell'architettura CPO, i percorsi di segnale elettrico ad alta velocità (come 224G PAM4) dall'ASIC al motore ottico sono drasticamente accorciati, ma richiedono substrati PCB con densità di routing e integrità del segnale senza precedenti.

La tecnologia **via-in-pad plated over (VIPPO)** posiziona i vias direttamente sotto i cuscinetti di saldatura, riempiendo completamente con materiale conduttore (tipicamente rame), eseguendo infine la placcatura di planarizzazione, risolvendo completamente questi problemi.

**I vantaggi essenziali si manifestano come:**

1. **Densità di routing estrema:** VIPPO elimina le tracce di fan-out esterne ai cuscinetti e i cuscinetti dei vias, consentendo ai pin del dispositivo BGA ad alta densità il routing inter-diretto.

2. **Percorsi di segnale più brevi:** I segnali direttamente dai cuscinetti del dispositivo attraverso le strutture VIPPO nelle tracce del livello interno, percorsi più brevi, riducono efficacemente l'induttanza parassita e la capacità.

3. **Integrità dell'alimentazione ottimizzata (PI):** Attraverso l'uso esteso di VIPPO sui piani di alimentazione e massa, riducono significativamente l'impedenza della rete di distribuzione dell'alimentazione (PDN).

In HILPCB, possediamo processi di fabbricazione VIPPO maturi, realizzando il riempimento di micro-fori preciso e la planarizzazione perfetta, assicurando l'affidabilità dell'assemblaggio SMT successivo, fornendo una base di fabbricazione solida [Interconnessione ad alta densità (HDI) PCB](https://hilpcb.com/en/products/hdi-pcb) per i tuoi progetti CPO.

## Progettazione termica: Distribuzione dell'alimentazione CPO e struttura di raffreddamento

CPO posiziona ASIC di potenza massiva (raggiungendo centinaia di watt) e motori ottici sensibili alla temperatura (laser, modulatori) in stretta prossimità, formando gravi sfide di "punti caldi". La gestione termica non è più semplicemente un problema a livello di sistema, ma una collaborazione multi-livello che copre chip, substrati fino ai dissipatori.

- **Percorsi di conduzione termica verticale:** Le strutture VIPPO riempite di rame sono essenzialmente colonne termiche efficienti, conducendo rapidamente il calore dai fondi del dispositivo ai piani termici interni PCB o direttamente ai dissipatori posteriori.

- **Collaborazione con livelli di rame pesante:** Per gestire correnti enormi e calore, i substrati CPO utilizzano generalmente la tecnologia **rame pesante 3oz+**. VIPPO si connette senza soluzione di continuità con questi livelli di rame spessi, formando reti di dissipazione termica tridimensionali ed efficienti.

- **Tecnologie di raffreddamento supplementari:** Sotto richieste di raffreddamento estreme, la tecnologia **pilastro di rame** (copper pillar) viene utilizzata per l'interconnessione e il raffreddamento a livello di chip.

## CTE basso e impilamento dei materiali: Affidabilità e controllo della deformazione

L'affidabilità a lungo termine del modulo CPO dipende in gran parte dalla stabilità meccanica durante i cicli di temperatura di funzionamento.

**Pertanto, la selezione dei materiali del substrato CPO e la progettazione dello stackup sono critiche:**

- **Stackup ibrido (Rogers+FR-4):** Strategia equilibrata costo-prestazioni comune. Vicino ai livelli di segnale critici dei chip CPO, utilizzare materiali speciali a basso CTE e bassa perdita (come la serie Rogers o Tachyon).

- **Materiali di base a basso CTE e prepregs:** La selezione di substrati con migliore abbinamento CTE ai chip è una soluzione fondamentale.

- **Impilamento simmetrico e controllo della deformazione:** La progettazione delle strutture **stackup ibrido (Rogers+FR-4)** deve rigorosamente rispettare i principi di simmetria.

## Test/calibrazione CPO e monitoraggio online

La complessità del modulo CPO determina che i processi di test e verifica superino di gran lunga i PCB tradizionali.

1. **Test di loopback (Loopback):** Durante la fase di progettazione PCB, devi riservare percorsi di test di loopback elettrico e ottico.

2. **Monitoraggio online e CMIS:** I moduli CPO devono rispettare le specifiche dell'interfaccia di gestione del modulo comune, segnalando in tempo reale lo stato di salute del modulo attraverso le interfacce I2C.

3. **Interfacce di test ad alta frequenza:** Per i test di diagramma oculare e BER precisi, devi estrarre i segnali che raggiungono 112GHz dai substrati CPO.

4. **Compatibilità ATE (Automated Test Equipment):** La progettazione PCB deve considerare la compatibilità della stazione di sonda ATE.

## Fattibilità di fabbricazione: Tolleranze, accessori e processi di assemblaggio

I progetti eccellenti sono inutili se non sono fabbricati economicamente e in modo affidabile. La progettazione della fattibilità di fabbricazione del substrato CPO (DFM) e la progettazione di assemblaggio (DFA) sono le chiavi del successo del progetto.

- **Tolleranze di fabbricazione:** I substrati CPO impongono requisiti estremamente rigorosi sulla larghezza della traccia/spaziature, allineamento tra i livelli, precisione di foratura.

- **Allineamento dell'array di fibre:** Realizzare l'allineamento di precisione sub-micron tra gli array di fibre e i circuiti integrati fotonici è il passo di assemblaggio CPO più difficile.

- **Accessori di assemblaggio e polimerizzazione:** Dopo il completamento dell'allineamento, utilizzare adesivi di polimerizzazione ultravioletta (UV) o termica per fissare definitivamente gli array di fibre.

- **Soluzioni chiavi in mano:** La complessità CPO rende i costi di comunicazione tra le fasi di progettazione, fabbricazione e assemblaggio estremamente elevati. La selezione di partner come HILPCB che forniscono la fabbricazione PCB tramite servizi di [assemblaggio PCBA chiavi in mano](https://hilpcb.com/en/products/turnkey-assembly) semplifica notevolmente le catene di approvvigionamento.

<div style="background: linear-gradient(135deg, #020617 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a5b4fc; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🚀 Packaging CPO: Linee guida della layer fisica di integrità del segnale (SI) dell'era 224G</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Affrontare le sfide estreme del budget di collegamento nel packaging co-progettato di motori fotonici silicio e ASIC</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">01. Controllo estremo della tolleranza dell'impedenza (Z-Accuracy)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logica essenziale:</strong>A tassi di 224Gbps, i cali di impedenza chiudono direttamente i diagrammi oculari. Deve controllare l'impedenza differenziale entro <strong>±5%</strong>. Utilizza i modelli di compensazione di incisione di secondo ordine precisi di HILPCB, eliminando gli effetti di variazione della larghezza della traccia di fabbricazione sulla riflessione del segnale.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">02. Sistema di materiale ultra-bassa perdita (UL-Loss)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logica essenziale:</strong>Selezionare i materiali dielettrici Megtron 8 o Rogers <strong>Ultra-Low Loss</strong>, abbinati alla foglia di rame HVLP3 (hyper-low profile). Assicurati che la perdita di inserzione del collegamento al millimetro (IL) rispetti gli standard di efficienza energetica rigorosi di CPO.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">03. Struttura VIPPO e soppressione della risonanza</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logica essenziale:</strong>Utilizza la tecnologia <strong>VIPPO (Via-in-Pad Plated Over)</strong> combinata con il back-drilling a profondità completa, eliminando completamente i stubs dei vias (Stub). Riduci la capacità parassita, sposta i punti di risonanza al di fuori della banda passante di lavoro.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">04. Simulazione di crosstalk 3D a onda intera (X-Talk)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logica essenziale:</strong>Nelle aree di routing ad alta densità, devi eseguire una simulazione elettromagnetica 3D a onda intera. Ottimizza gli array di <strong>schermatura GND</strong> via e gli spazi delle coppie differenziali, sopprimendo FEXT e NEXT sotto -40dB.</p>
</div>
</div>

<div style="margin-top: 35px; padding: 25px; background: rgba(165, 180, 252, 0.1); border-radius: 16px; border-right: 8px solid #818cf8; font-size: 0.95em; line-height: 1.7; color: #c7d2fe;">💡 <strong>Raccomandazione esperto HILPCB:</strong>Nella progettazione CPO, i via termici sotto i motori ottici spesso entrano in conflitto con i percorsi di segnale ad alta velocità. Raccomandiamo la tecnica di layout <strong>Griglia non uniforme (Non-uniform Grid)</strong>, assicurando la conduttività termica mentre la simulazione 3D ottimizza i percorsi di ritorno del segnale, prevenendo danni all'integrità di riferimento del piano di massa.</div>
</div>

## Linee guida della layer fisica di integrità del segnale (SI) dell'era CPO 224G

| Linea guida | Logica essenziale | Implementazione |
| :--- | :--- | :--- |
| **01. Controllo estremo della tolleranza dell'impedenza (Z-Accuracy)** | A tassi di 224Gbps, i cali di impedenza chiudono direttamente i diagrammi oculari. Deve controllare l'impedenza differenziale entro **±5%**. | Utilizza i modelli di compensazione di incisione di secondo ordine precisi di HILPCB, eliminando gli effetti di variazione della larghezza della traccia di fabbricazione sulla riflessione del segnale. |
| **02. Sistema di materiale ultra-bassa perdita (UL-Loss)** | Selezionare i materiali dielettrici Megtron 8 o Rogers di livello **Ultra-Low Loss**, abbinati alla foglia di rame HVLP3 (hyper-low profile). | Assicurati che la perdita di inserzione del collegamento al millimetro (IL) rispetti gli standard di efficienza energetica rigorosi di CPO. |
| **03. Struttura VIPPO e soppressione della risonanza** | Utilizza la tecnologia **VIPPO (via-in-pad plated over)** combinata con il back-drilling a profondità completa, eliminando completamente i stubs dei vias (Stub). | Riduci la capacità parassita, sposta i punti di risonanza al di fuori della banda passante di lavoro. |
| **04. Simulazione di crosstalk 3D a onda intera (X-Talk)** | Nelle aree di routing ad alta densità, devi eseguire una simulazione elettromagnetica 3D a onda intera. | Ottimizza gli array di **schermatura GND** via e gli spazi delle coppie differenziali, sopprimendo FEXT e NEXT sotto -40dB. |

<div style="background-color: #1A237E; color: #ffffff; padding: 25px; border-radius: 10px; margin: 30px 0;">
    <h3 style="color: #ffffff; text-align: center; border-bottom: 2px solid #42A5F5; padding-bottom: 10px;">Capacità di fabbricazione di base del substrato CPO HILPCB</h3>
    <table style="width: 100%; margin-top: 15px; border-collapse: collapse; color: #000000;">
        <thead style="background-color: #42A5F5;">
            <tr>
                <th style="padding: 12px; text-align: left;">Parametro tecnico</th>
                <th style="padding: 12px; text-align: left;">Capacità HILPCB</th>
                <th style="padding: 12px; text-align: left;">Valore per CPO</th>
            </tr>
        </thead>
        <tbody style="background-color: #ffffff;">
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Via-in-Pad Plated Over</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Riempimento rame/resina elettrolitico, planarità &lt; 15µm</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Raggiunge la densità di routing massima, ottimizza i percorsi segnale/termico</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Microvia/Via impilata</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Supporta fino a 4+N+4 stadi vias impilati/interlacciati ciechi sepolti</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Costruisce interconnessioni 3D complesse, abbrevia i percorsi di segnale</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Rame pesante 3oz+</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Livelli interni/esterni supportano 3-10oz spessore di rame</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Porta correnti elevate, dissipazione termica efficiente, migliora l'integrità dell'alimentazione</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Stackup Ibrido</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Esperto in stratificazione ibrida Rogers/Megtron/Tachyon con FR-4</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Bilancia costi, prestazioni e affidabilità, controlla la disadattamento CTE</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Impedenza controllata</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Controllo tolleranza ±5%, fornisce rapporti di test TDR</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Garantisce la qualità di trasmissione del segnale ad alta velocità, riduce il tasso di errore bit</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione

La tecnologia **via-in-pad plated over (VIPPO)** non è semplicemente un singolo processo di fabbricazione dei vias; è un punto di appoggio per l'intero ecosistema CPO. Fornendo una densità di routing incomparabile, un'eccellente integrità del segnale, efficienti canali di conduzione termica, affronta perfettamente le sfide essenziali della collaborazione opto-elettronica e del consumo termico di CPO.

Sul percorso verso 800G, 1.6T e larghezza di banda più elevata, i requisiti della tecnologia PCB non fanno che aumentare. Come tuo partner di fiducia, HILPCB, sfruttando l'accumulo profondo nella fabbricazione di PCB a [rame pesante](https://hilpcb.com/en/products/heavy-copper-pcb) e schede ad alta frequenza complesse, si impegna a fornire soluzioni di substrato CPO all'avanguardia ai clienti globali.

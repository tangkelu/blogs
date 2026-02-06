---
title: "Tutorial di stackup HDI: Comprendere i parametri dei materiali e la progettazione dello stackup"
description: "Un tutorial completo sullo stackup HDI che spiega i parametri dei materiali, la pianificazione dello stackup, i compromessi tra impedenza, termica e costi, nonché i punti chiave della fabbricazione."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["hdI stackup tutorial", "hdmi pcb stackup guide", "thermal reliability stackup"]
---

Buongiorno a tutti, sono un docente dell'accademia dello stackup e dei materiali di HILPCB. Nel mio lavoro quotidiano, noto che molti ingegneri si sentono spaesati di fronte a parametri tecnici come Dk/Df, CTI o Tg, non sapendo come trasformarli in uno stackup PCB affidabile e producibile. Una cattiva progettazione dello stackup può, nel migliore dei casi, causare problemi di integrità del segnale e, nel peggiore, provocare una catastrofe di affidabilità durante la produzione di massa.

Oggi, questo **hdI stackup tutorial** fungerà da prima lezione per aiutarvi a costruire sistematicamente un pensiero di progettazione dello stackup. Insieme trasformeremo la scienza dei materiali astratta in decisioni ingegneristiche concrete, permettendovi non solo di progettare uno stackup performante, ma anche di anticipare ed evitare le trappole della fabbricazione. Che stiate lavorando su una `hdmi pcb stackup guide` ad alta velocità o su un progetto che richiede un `thermal reliability stackup` di alto livello, queste conoscenze costituiranno la vostra solida base.

## Il punto di partenza del design dello stackup: Definire i vostri \"vincoli\"

Prima di aprire lo strumento di progettazione CAD (EDA) per tracciare la prima pista, una progettazione dello stackup professionale inizia con un'analisi completa delle esigenze del progetto. È come un architetto che deve comprendere l'uso dell'edificio, il budget e la natura del suolo prima di disegnare i piani. Le condizioni di ingresso per la progettazione dello stackup comprendono principalmente:

*   **Esigenze di integrità del segnale (SI)**:
    *   **Velocità massima**: Qual è la velocità di segnale più elevata nel vostro design? Si tratta di PCIe 3.0 a 10 Gbps o di SerDes a 28 Gbps? La velocità determina la vostra tolleranza alle perdite di materiali (Df).
    *   **Controllo dell'impedenza**: Quali impedenze bisogna controllare? 50Ω asimmetrica (single-ended) o 90/100Ω differenziale? Un'impedenza precisa è il prerequisito per una trasmissione stabile.
*   **Esigenze di integrità dell'alimentazione (PI)**:
    *   **Corrente di core**: Qual è l'intensità della corrente transitoria per i componenti critici (CPU, FPGA)? Questo definisce lo spessore del rame e la disposizione dei piani di alimentazione.
    *   **Capacità di piano**: Bisogna utilizzare piani di alimentazione e massa adiacenti per creare una capacità di piano e fornire un disaccoppiamento ad alta frequenza?
*   **Gestione termica e affidabilità**:
    *   **Consumo e ambiente**: Qual è la potenza totale della scheda, l'ubicazione dei componenti che scaldano e la temperatura di funzionamento finale? Questo impatta direttamente sulla scelta della temperatura di transizione vetrosa (Tg) e della temperatura di decomposizione termica (Td).
    *   **Norme di sicurezza**: Il prodotto comporta parti ad alta tensione? Ci sono requisiti CTI (indice di resistenza al tracciamento) specifici (es: >400V)? Cruciale per l'industria e l'energia.
*   **Costi e catena di fornitura**:
    *   **Costo target**: Qual è il budget per scheda? Questo determina se dovete ottimizzare nella gamma standard FR-4 o se potete considerare materiali ad alte prestazioni come Rogers.
    *   **Volumi e tempi**: Il volume annuo stimato e i tempi di consegna influiscono sulla disponibilità dei materiali e sulle quantità minime d'ordine (MOQ).

Queste condizioni porteranno a un piano dello stackup preciso per il produttore di PCB, includendo il tipo di strato, il materiale, lo spessore, lo spessore del rame e i requisiti di impedenza.

## Comprendere il \"linguaggio dei materiali\": Tabella riepilogativa dei parametri chiave

Scegliere il materiale giusto è il cuore del design dello stackup. Di fronte a centinaia di riferimenti, bisogna saper identificare i parametri essenziali. Ecco una tabella che riassume gli indicatori chiave di alcuni materiali rappresentativi della biblioteca HILPCB.

<div style="background-color: #f0f7ff; border-left: 5px solid #007bff; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #0056b3; margin-top: 0;">Compromesso tra i parametri: Non esiste il materiale perfetto, solo scelte adattate</h4>
    <p style="margin-bottom: 0;">Nella scelta dei materiali, prestazioni e costi sono sempre in conflitto. Ad esempio, puntare a un Df (perdita dielettrica) estremamente basso implica generalmente un costo più elevato. Allo stesso modo, un materiale ad alta Tg offre una migliore stabilità termica ma la sua finestra di pressatura è più complessa. Il valore dell'ingegnere risiede nella sua capacità di trovare il punto di equilibrio ottimale. Per l'elettronica di consumo sensibile ai costi, l'S1141 o l'IT-180A sono spesso sufficienti; per una scheda madre di una stazione radio base, sarà necessario l'S1000-2M.</p>
</div>

| Modello | Fornitore | Categoria | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Applicazione Core |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S1141** | Shengyi | FR-4 Standard | 4.2 | 0.020 | 140 | 315 | >175 | Elettronica di consumo, controllo bassa frequenza |
| **IT-180A** | ITEQ | FR-4 Alta Tg | 3.9 | 0.012 | 175 | 345 | >400 | Server, controllo industriale, auto |
| **S1000-2M** | Shengyi | Mid-Loss | 3.6 | 0.009 | 190 | 360 | >400 | Calcolo ad alta velocità, data center |
| **EM-827** | EMC | Low-Loss | 3.4 | 0.006 | 200 | 370 | >600 | SerDes 25Gbps+, apparati di rete |
| **RO4350B** | Rogers | RF/Microonde | 3.48 | 0.0037 | 280 | 390 | >400 | Moduli RF, antenne, 5G |

**Interpretazione dei parametri:**
*   **Dk (Costante dielettrica)**: Influenza la velocità di propagazione e l'impedenza. Più è bassa e stabile, meglio è per i segnali veloci.
*   **Df (Fattore di perdita)**: Quantità di energia trasformata in calore nel materiale. Cruciale per i lunghi percorsi ad alta frequenza.
*   **Tg (Temperatura di transizione vetrosa)**: Passaggio dallo stato rigido allo stato flessibile. Una Tg elevata (>170°C) garantisce la stabilità dimensionale durante i passaggi in forno.
*   **Td (Temperatura di decomposizione)**: Temperatura in cui il materiale perde il 5% del suo peso. Indica la resistenza termica a lungo termine.
*   **CTI**: Resistenza alle perdite elettriche di superficie. Vitale per l'alta tensione.

## Da 4 a 10+ strati: Modelli di strutture dello stackup classiche

Vediamo ora come \"assemblare\" questi materiali. Uno stackup non si fa a caso, segue i principi di compatibilità elettromagnetica (EMC) e di integrità del segnale.

<div style="background-color: #fff4e5; border-left: 5px solid #ff9800; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #e65100; margin-top: 0;">Metodo di pianificazione in tre fasi</h4>
    <ol>
        <li><strong>Determinare il numero di strati</strong>: Basato sulla densità di routing, i piani di alimentazione e il budget. Assegnare una funzione (segnale, massa, alim) a ogni strato.</li>
        <li><strong>Costruire i piani di riferimento</strong>: Posizionare in priorità piani GND (massa) continui. Sono i percorsi di ritorno dei segnali e schermature naturali.</li>
        <li><strong>Ottimizzare e simmetrizzare</strong>: Regolare gli spessori per l'impedenza. Mantenere una struttura simmetrica (alto/basso) per evitare l'imbarcamento (warpage) durante la fabbricazione.</li>
    </ol>
</div>

| Strati | Struttura classica (Dall'alto al basso) | Applicazione tipo | Vantaggi | Svantaggi |
| :--- | :--- | :--- | :--- | :--- |
| **4 strati** | SIG/GND/PWR/SIG | Moduli IoT, controllori semplici | Costo molto basso, semplice | EMC mediocre, impedenza instabile |
| **6 strati** | SIG/GND/SIG/SIG/PWR/SIG | Elettronica di consumo, schede industriali | Piano di massa completo inserito, EMC migliorato | Piani di riferimento mediocri per segnali interni |
| **6 strati (Consigliata)** | SIG/GND/PWR/GND/SIG/SIG | Applicazioni HDMI/USB3.0 | Eccellente EMC e SI, costo moderato | Si perde uno strato di routing |
| **8 strati** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | Server, calcolo ad alta velocità | Schermatura multistrato, impedenza precisa | Costo più elevato, fabbricazione più lunga |
| **10 strati** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | Apparati di rete, schede FPGA | Eccellente isolamento alim/massa | Costo elevato, precisione di fabbricazione richiesta |

## La \"Sinfonia\" degli strati: Segnale, Alimentazione, Massa e spessore del rame

Un buon stackup è un'orchestrazione armoniosa dei suoi elementi.

### Strato di segnale: Microstrip vs Stripline
*   **Microstrip**: Piste in superficie, un lato all'aria, l'altro sul dielettrico. Vantaggi: semplice da fabbricare e testare. Svantaggi: sensibile ai disturbi, maggiore radiazione.
*   **Stripline**: Piste interne tra due piani di riferimento. Vantaggi: eccellente EMC, impedenza stabile. Svantaggi: routing più complesso.
*   **Consiglio HILPCB**: Per segnali >5Gbps, preferite lo stripline.

### Piani di riferimento: La supremazia del GND
Un piano GND solido è la base del design ad alta velocità. Offre il percorso di ritorno più breve e limita la diafonia. Evitate di tagliare i piani di massa sotto i segnali veloci.

### Spessore del rame: Arbitraggio 1 oz vs 2 oz
*   **Capacità di corrente**: Il rame da 2 oz (70µm) supporta circa 1,5 - 1,8 volte più corrente rispetto a quello da 1 oz (35µm). Necessario per gli strati di alimentazione.
*   **Impatto impedenza**: Un rame più spesso richiede piste più larghe per la stessa impedenza, occupando più spazio.
*   **Fabbricazione**: Il rame spesso è più difficile da incidere con precisione. Per le schede [HDI](/technology/what-is-hdi-pcb/), si usa spesso 0.5 oz o 1 oz internamente.

## Oltre l'FR-4: Ibridi, basi metalliche e materiali flessibili

### Stackup ibrido (Hybrid Stackup)
Utilizzare più materiali diversi, comune in RF. Ad esempio, Rogers per la parte radio e IT-180A per la parte digitale. Questo permette di concentrare le prestazioni dove serve controllando i costi.

| Schema Ibrido | Vantaggi | Sfide e Considerazioni |
| :--- | :--- | :--- |
| **Rogers + FR-4** | Alte prestazioni nelle zone critiche, costo complessivo controllato | Disadattamento del CTE (Coefficiente di Espansione Termica), possibile delaminazione o problemi di affidabilità; ciclo di pressatura complesso, richiede fabbrica esperta. |
| **Materiali Alta Velocità + Standard** | Soddisfa i requisiti di bassa perdita per canali veloci, riduce il costo totale | Differenza di flusso di resina (Resin Flow) tra materiali, può influenzare l'uniformità dello spessore dielettrico. |

### Basi metalliche (MCPCB) e Flex
*   **MCPCB**: Base alluminio o rame per una dissipazione termica massima (LED alta potenza, alimentatori).
*   **Flex / Rigid-Flex**: Per connessioni 3D. Design complesso che richiede attenzione alle sollecitazioni di piegatura.

## Dal design alla produzione: Gli impatti inevitabili del processo

Il vostro piano dello stackup è solo un modello teorico. La realtà fisica dipende dalla fabbrica.

<div style="background-color: #e8f5e9; border-left: 5px solid #2e7d32; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #1b5e20; margin-top: 0;">Capacità di controllo HILPCB</h4>
    <p style="margin-bottom: 0;">Presso HILPCB, analizziamo la fattibilità del vostro stackup tramite i nostri modelli di pressatura. Simulando il flusso di resina, compensiamo gli spessori per garantire una precisione di impedenza del ±5%, molto migliore rispetto allo standard industriale del ±10%.</p>
</div>

*   **Flusso di resina (Resin Flow)**: Durante la pressatura, la resina del preimpregnato (PP) fonde e riempie i vuoti del rame. Lo spessore finale è quindi inferiore allo spessore iniziale del PP.
*   **Ciclo di pressatura**: Ogni materiale ha la sua curva di temperatura/pressione. Un ciclo errato causa delaminazioni.
*   **Imbarcamento (Warpage)**: Spesso dovuto a mancanza di simmetria o distribuzione ineguale del rame.
*   **Back-drilling**: Per il >10Gbps, rimuovere gli \"stub\" di via inutilizzati per evitare l'effetto antenna.
*   **Coupon di impedenza**: Una barretta di test sul pannello di produzione per verificare l'impedenza reale al TDR.

## HILPCB: Il vostro partner tecnico

HILPCB non è solo un produttore, è il vostro partner. Semplifichiamo i vostri design:
*   **Libreria di oltre 200 materiali**: Scorte permanenti per tutte le esigenze (FR-4, High-speed, RF, MCPCB).
*   **Laboratorio di test di impedenza**: Validazione rigorosa di ogni lotto.

## Ottenete il vostro piano dello stackup personalizzato

Non lottate più da soli con le schede tecniche. HILPCB offre un servizio di consulenza rapido per fornirvi uno stackup validato e pronto per la produzione.

<div style="background-color: #f8f9fa; border: 1px solid #dee2e6; padding: 25px; margin: 30px 0; border-radius: 10px; text-align: center;">
    <h3 style="margin-top: 0;">Serve aiuto per il vostro stackup?</h3>
    <p>Inviateci le vostre esigenze (strati, velocità, impedenza, materiali speciali). I nostri esperti vi risponderanno entro 24 ore con una proposta dettagliata: scelta dei materiali, calcoli degli spessori e simulazioni di impedenza.</p>
    <a href="#" style="display: inline-block; background-color: #007bff; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Ottieni il mio piano dello stackup gratuito</a>
</div>

## Riassunto: Uno stackup riuscito è un consenso tra design e fabbricazione

Un buon stackup non è una semplice sovrapposizione di strati. È la fusione della vostra intenzione di design e delle capacità della fabbrica. Inizia con esigenze chiare e finisce con il rispetto dei vincoli di fabbricazione. Comunicate presto con esperti come HILPCB per fare del vostro stackup la base del vostro successo.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione

Seguendo i consigli di questo **hdI stackup tutorial**, ora padroneggiate le basi per progettare stackup performanti e affidabili. Non dimenticate di coinvolgere il team DFM di HILPCB fin dall'inizio per mettere in sicurezza la vostra produzione.

> Per supporto alla produzione e assemblaggio, contatta HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) o [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) per consigli DFM/DFT.

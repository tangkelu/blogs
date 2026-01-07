---
title: "low loss laminate tutorial: la prima lezione su parametri materiali e pianificazione stackup"
description: "Un low loss laminate tutorial che spiega parametri chiave dei materiali, pianificazione stackup, trade-off impedenza/termica/costo e aspetti produttivi—con tabelle di confronto ed esempi per aiutare i team a costruire una libreria stackup standard."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["low loss laminate tutorial", "hdI stackup tutorial", "hdmi pcb stackup guide", "surface finish comparison", "cti requirement explanation", "thermal reliability stackup"]
---
Ciao, sono un docente della HILPCB Stackup & Materials Academy. Nelle conversazioni quotidiane con gli ingegneri vedo spesso lo stesso pain point: quando si affronta un design high-speed, come si sceglie il giusto low loss laminate tra centinaia di materiali PCB e si pianifica uno stackup che rispetti i target prestazionali bilanciando costo e manufacturability?

Molti team fanno over-spec (ad esempio Megtron 6 per 5Gbps) o under-spec (provano a spingere FR-4 standard fino a 28Gbps) e finiscono con problemi di Signal Integrity (SI). Questo **low loss laminate tutorial** è la “prima lezione” per te e per il tuo team: traduciamo parametri astratti come Dk/Df, CTI e fiber weave effect in passi operativi di stackup planning, supportati da dati di produzione HILPCB, per fare trade-off più intelligenti.

## 1. Punto di partenza dello stackup design: definire input e output attesi

Uno stackup professionale non è “a intuito”: è un processo sistematico basato su requisiti ingegneristici chiari. Prima di iniziare, raccogli questi input:

*   **Requisiti di segnale:**
    *   Qual è il data rate massimo? (es. 5Gbps, 10Gbps, 28Gbps+)
    *   Quali target di impedance control servono? (es. 50Ω single-ended, 90Ω/100Ω differential)
    *   Qual è il budget totale di insertion loss (dB)?
*   **Requisiti di Power Integrity (PI):**
    *   Quanta corrente serve al core device? (guida lo spessore rame delle power plane)
    *   Qual è la PDN target impedance? (influenza il coupling power/ground)
*   **Requisiti termici:**
    *   Potenza e posizione delle principali sorgenti di calore?
    *   Temperatura ambiente e approccio di raffreddamento? Questo determina direttamente se serve un **thermal reliability stackup**.
*   **Requisiti di safety e affidabilità:**
    *   Il prodotto deve soddisfare standard specifici? (es. UL, CE)
    *   **CTI requirement explanation**: serve un requisito specifico di Comparative Tracking Index? Per esempio, prodotti industriali o di potenza richiedono spesso CTI ≥ 175V (PLC=2) o superiore.
    *   Vita utile target e ambiente operativo? (influenza la necessità di high Tg)
*   **Vincoli meccanici e di costo:**
    *   Limite massimo di spessore PCB?
    *   Range costo target?

**L’output finale dovrebbe essere un file stackup professionale che includa:**

1.  Definizione funzioni per layer (signal, ground, power).
2.  Material part number specifici per layer (Core & Prepreg).
3.  Spessore dielettrico e spessore rame per layer (inner/outer).
4.  Spessore finale complessivo e tolleranza.
5.  Target d’impedenza più raccomandazioni di width/spacing per layer.
6.  Note di processo speciali (backdrill, resin fill, ecc.).

## 2. Material parameter cheat sheet: da FR-4 a low loss laminate

Scegliere il materiale giusto è metà del lavoro. Per costruire un modello mentale rapido, abbiamo sintetizzato laminati comuni dalla libreria HILPCB per classe di perdita. Questa è una `dk df table` semplificata; i valori reali variano con frequenza e contenuto resina.

<div class="div-type-1">
    <div class="div-type-1-title">Confronto prestazioni materiali PCB</div>
    <div class="div-type-1-content">
        <p>La tabella copre parametri chiave dal FR-4 standard a materiali extremely low-loss, per una prima selezione in base alle esigenze del progetto (data rate, temperatura operativa, requisiti di safety).</p>
    </div>
</div>

| Classe materiale | Opzioni comuni HILPCB | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Applicazioni tipiche |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard FR-4** | S1141, KB-6160 | ~4.2 | ~0.020 | 140 | 315 | 175 | Digitale/analogico low-frequency, consumer electronics |
| **Mid Tg FR-4** | IT-158, S1155 | ~4.1 | ~0.018 | 150 | 330 | 175 | Multilayer, lead-free assembly |
| **High Tg FR-4** | IT-180A, S1000 | ~4.0 | ~0.015 | 180 | 345 | 175 | Server, automotive, high-reliability |
| **Medium loss** | TU-768, S7439 | ~3.8 | ~0.009 | 190 | 360 | 175 | < 10Gbps high-speed, storage |
| **Low Loss (Low Loss)** | TU-872SLK, S1000-2M | ~3.6 | ~0.005 | 190 | 360 | 175 | 10-25Gbps, server backplane, **hdmi pcb stackup guide** |
| **Very Low Loss (Very Low Loss)** | I-Speed, M4S | ~3.3 | ~0.003 | 200 | 380 | 175 | 25-56Gbps, RF communications, test equipment |
| **Ultra Low Loss (Ultra Low Loss)** | Megtron 6, Tachyon 100G | ~3.0 | ~0.002 | 210 | 400 | 175 | > 56Gbps, core networking, optical module |
| **RF** | Rogers RO4350B | 3.48 | 0.0037 | 280 | 390 | 600 | Circuiti RF/microonde, antenne |

**Interpretazione dei parametri chiave:**

*   **Dk (dielectric constant):** Dk più basso in genere significa propagazione più veloce e rende più facile usare tracce più larghe a parità di impedenza. La consistenza del Dk conta più del valore assoluto.
*   **Df (dissipation factor):** parametro chiave; determina direttamente l’attenuazione. Per segnali >5Gbps, Df < 0.01 è una soglia base.
*   **Tg (glass transition temperature):** temperatura a cui il materiale passa da rigido a “gommoso”. High Tg (≥170°C) significa migliore resistenza termica e stabilità dimensionale—preferibile per lead-free assembly e prodotti high-reliability.
*   **Td (thermal decomposition temperature):** temperatura alla quale il materiale perde il 5% di peso; riflette la thermal reliability nel lungo periodo.
*   **CTI (Comparative Tracking Index):** resistenza al tracking superficiale. FR-4 standard tipicamente 175V (PLC=2); applicazioni speciali possono richiedere 600V (PLC=0).

## 3. Core stackup patterns: template 4/6/8/10 layer

La teoria deve incontrare la pratica. Qui sotto trovi template “production-proven” ottimi come punto di partenza; puoi fine-tunarli in base ai requisiti.

| Layer count | Stackup (funzione) | Core | PP | Spessore finito (mm) | Uso tipico |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4-layer** | SIG/GND/PWR/SIG | 1.0mm Core | 2x 1080 | 1.2 | IoT, MCU control, consumer low-cost |
| **6-layer** | SIG/GND/SIG/PWR/GND/SIG | 0.5mm Core | 3x 2116 | 1.6 | Embedded system, motherboard DDR3/4 |
| **8-layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | 0.2mm Core | 4x 2116/1080 | 1.6 | PCIe, USB3.x, HDMI, HPC |
| **10-layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | 0.15mm Core | 5x 1080/106 | 1.6 | Server motherboard, casi complessi **hdI stackup tutorial**, multi high-speed bus |

**Design notes:**

*   **4-layer:** costo minimo ma EMI e SI più deboli—generalmente non adatto a high-speed.
*   **6-layer:** aggiunge layer di segnale interni + reference plane solidi; ottimo cost/performance. I layer di segnale sono schermati dai ground plane, migliorando significativamente l’EMI.
*   **8-layer:** aggiunge due reference plane e abilita eccellenti strutture Stripline—raccomandazione classica per **hdmi pcb stackup guide**. Supporta isolamento di più power domain e tight impedance control.
*   **10-layer e oltre:** per design ad alta densità e multi power-domain. Più ground plane migliorano isolamento e PI; per HDI, layer aggiuntivi possono ospitare più microvia.

## 4. Principi per coordinare signal/power/ground/copper thickness

L’“anima” di un ottimo stackup è come i layer lavorano insieme.

<div class="div-type-3">
    <div class="div-type-3-title">Golden rules per lo stackup planning</div>
    <ol>
        <li>
            <h6>Prioritizza reference plane continui</h6>
            <p>I layer di segnale high-speed devono essere adiacenti a un ground o power plane solido. Evita routing sopra split: è una causa primaria di crosstalk ed EMI.</p>
        </li>
        <li>
            <h6>Instrada i segnali high-speed su layer interni</h6>
            <p>Stripline su layer interni (GND-SIG-GND) offre in genere migliore schermatura EMI e impedenza più stabile rispetto al Microstrip su layer esterni (SIG-GND).</p>
        </li>
        <li>
            <h6>Accoppia strettamente power e ground plane</h6>
            <p>Metti i principali power e ground plane adiacenti per sfruttare la plane capacitance, creando un return path a bassa impedenza per corrente ad alta frequenza e migliorando la PI.</p>
        </li>
        <li>
            <h6>Trade-off nella scelta dello spessore rame</h6>
            <p>I layer di segnale tipicamente usano rame 0.5oz (18μm) o 1oz (35μm). 0.5oz supporta line/space più fine per routing ad alta densità. I power plane ad alta corrente possono richiedere 2oz (70μm) o più—spesso imponendo un solido <strong>thermal reliability stackup</strong>.</p>
        </li>
        <li>
            <h6>Usa simmetria per prevenire warpage</h6>
            <p>Mantieni lo stackup il più simmetrico possibile (materiali, spessore rame, distribuzione rame). L’asimmetria crea stress in laminazione e reflow e aumenta il rischio di warpage.</p>
        </li>
    </ol>
</div>

## 5. Hybrid lamination e materiali speciali: quando le opzioni standard non bastano

Talvolta un singolo sistema materiale non soddisfa tutto—for example, quando coesistono segnali RF e controllo digitale. In questi casi conviene valutare hybrid lamination.

| Opzione | Pro | Contro | Raccomandazione HILPCB |
| :--- | :--- | :--- | :--- |
| **All Low Loss material** | Prestazioni consistenti, processo maturo | Costo più alto | Ideale per communications/server con requisiti SI stringenti. |
| **Rogers + FR-4 hybrid** | Prestazioni RF + costo digitale più basso | Laminazione complessa, rischio reliability, CTE mismatch | Ideale per design con integrazione antenna. HILPCB ha molta esperienza su hybrid e può ottimizzare press cycle per reliability. |
| **MCPCB (metal core)** | Eccellente dissipazione termica | Tipicamente limitato a 1–2 layer; routing complesso difficile | High-power LED, power module e applicazioni thermal-critical. |
| **Rigid-Flex** | Abilita interconnessioni 3D; alta affidabilità | Design complesso; costo molto alto | Wearable, aerospace e prodotti con vincoli speciali di spazio/affidabilità. |

## 6. Impatto manufacturing: l’“ultimo miglio” dal disegno al PCB fisico

Uno stackup teoricamente perfetto può comunque aumentare i costi o ridurre lo yield se si ignora il DFM.

<div class="div-type-6">
    <div class="div-type-6-title">Capacità HILPCB legate alle decisioni di stackup</div>
    <div class="div-type-6-content">
        <ul>
            <li><strong>Resin Flow e Press Cycle:</strong> ottimizziamo i profili temperatura/pressione di laminazione in base al prepreg (PP) scelto. Per esempio, PP 106 ad alto contenuto di resina richiede controllo stretto per riempire microvia laser HDI evitando eccessiva perdita di resina che destabilizza lo spessore dielettrico.</li>
            <li><strong>Fiber Weave Effect:</strong> per segnali 25Gbps+, weave “loose” (es. 7628) possono creare non uniformità locali del Dk e degradare l’impedenza. HILPCB raccomanda e mantiene a stock Flat Glass low loss laminates per migliorare significativamente la qualità del segnale.</li>
            <li><strong>Back-drilling:</strong> i via stub sono un “killer” per l’high-speed. Per segnali >10Gbps, offriamo backdrilling depth-controlled di precisione per rimuovere stub inutilizzati e ridurre l’insertion loss di 1–2 dB.</li>
            <li><strong>Impedance coupon e test TDR:</strong> ogni lotto di produzione include impedance coupon. HILPCB misura con TDR per assicurare che l’impedenza finale resti entro la tua finestra di tolleranza (+/- 10% o più stretta).</li>
            <li><strong>Surface finish comparison:</strong> il surface finish impatta anche il comportamento high-speed. ENIG è flat e adatto ad alta frequenza, ma ha rischio “black pad” e costo superiore. OSP è low cost ma ha shelf-life limitata per la saldabilità. Raccomandiamo la migliore opzione [internal link: PCB surface finish] in base ad applicazione e cost target.</li>
        </ul>
    </div>
</div>

## 7. Come HILPCB ti supporta nello stackup design?

Dopo questo **low loss laminate tutorial**, lo stackup planning può sembrare ancora impegnativo. È proprio per questo che esiste la HILPCB Stackup & Materials Academy: non siamo solo un produttore, siamo il tuo partner engineering.

Offriamo un servizio **“Stackup quick claim”** per liberarti da selezione materiali e calcoli stackup ripetitivi.

<div class="cta-container">
    <div class="cta-text">
        <h5>Non sai da dove partire? Lascia che gli ingegneri HILPCB personalizzino il tuo stackup</h5>
        <p>Condividi i tuoi requisiti (data rate, layer count, impedenza, ecc.). I nostri senior engineer ti consegneranno entro 24 ore una proposta stackup professionale DFM-validata e ottimizzata in base all’inventario—più un report dettagliato di calcolo impedenza. Totalmente gratuito.</p>
    </div>
    Invia ora la tua richiesta stackup
</div>

**Perché scegliere HILPCB?**

*   **200+ materiali a stock:** da FR-4 standard a Rogers e Megtron, evitando ritardi da MOQ e lead time di settimane per materiali speciali.
*   **Engineering team esperto:** migliaia di progetti high-speed/high-frequency/high-density—identificazione rapida dei rischi e ottimizzazione costo/prestazioni.
*   **Impedance test lab avanzato:** non promettiamo solo l’impedenza; la verifichiamo con test TDR rigorosi perché ogni board rispetti la tua specifica.

### Summary

Uno stackup eccellente è un bilanciamento tra prestazioni, costo e manufacturability. Parti da input chiari, usa la tabella parametri per una prima selezione, riusa pattern collaudati e mantieni una comunicazione stretta con il tuo PCB manufacturer (come HILPCB). Portare i vincoli di produzione “a monte” aiuta il team a costruire una libreria stackup standardizzata e affidabile e ad accelerare lo sviluppo prodotto.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

In sintesi, questo low loss laminate tutorial spiega parametri materiali, stackup planning, trade-off impedenza/termica/costo e considerazioni di manufacturing—con tabelle e esempi—per aiutare i team a costruire una libreria stackup standard e gestire il rischio tra design, materiali e test. Seguendo checklist e process window descritti qui—e coinvolgendo presto il team DFM/DFA di HILPCB—puoi accelerare prototipi e volumi mantenendo qualità e compliance.

> Per supporto di fabrication e assembly, contatta HILPCB tramite [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) o [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) per suggerimenti DFM/DFT.

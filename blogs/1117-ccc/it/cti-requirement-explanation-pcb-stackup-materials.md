---
title: "Spiegazione dei requisiti CTI: Documento strategico su materiali e stackup"
description: "Fornitura di un albero decisionale completo per la selezione dei materiali, modelli di stackup, metodi di modellazione dell'impedenza/termica e processi di verifica della produzione con liste di controllo DFM/DFT/DFR."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 9
tags: ["cti requirement explanation", "thermal reliability stackup", "hdi stackup tutorial", "surface finish comparison", "hdmi pcb stackup guide"]
---

## 1. Sintesi: scenario, sfide e benefici

**Scenario:** Nella progettazione di prodotti elettronici moderni — dai data center ad alta velocità fino alle unità di power management nei veicoli a nuova energia — il PCB non è più soltanto un supporto per componenti, ma la base fisica delle prestazioni del sistema e della sicurezza elettrica sull’intero ciclo di vita.

**Sfida:** Il nucleo della sfida è la strategia di materiali e stackup. Una scelta errata può portare ad attenuazione del segnale, disadattamento d’impedenza e persino a guasti elettrici catastrofici in ambienti severi (alta tensione, alta umidità). Tra gli indicatori di sicurezza, **CTI (Comparative Tracking Index, indice comparativo di resistenza al tracking)** è sempre più importante ma spesso sottovalutato nelle fasi iniziali. Una `cti requirement explanation` completa non riguarda solo la conformità: impatta direttamente l’affidabilità a lungo termine.

**Benefici:** Questo whitepaper fornisce una soluzione sistematica. Come guida ufficiale del laboratorio materiali HILPCB, consegna una strategia completa dalla selezione materiali alla validazione di produzione. Tramite un albero decisionale standardizzato, una libreria di template di stackup, metodi di modellazione e check‑list DFM/DFR, aiuta il team a:

- **Ridurre il rischio di progetto:** decisioni data‑driven sui materiali basate su requisiti CTI espliciti.
- **Accelerare i cicli di sviluppo:** avvio rapido con template di stackup pre‑validati.
- **Migliorare l’affidabilità:** garantire `thermal reliability stackup` e sicurezza elettrica via modellazione e verifica.
- **Ottimizzare i costi:** bilanciare performance e costo, evitando over‑design e rilavorazioni.

---

## 2. Albero decisionale materiali: percorso sistematico

La scelta del materiale PCB corretto è il primo passo e il più critico nella progettazione dello stackup. CTI è il punto di partenza per la sicurezza, ma deve essere co‑ottimizzato con altri indicatori (Dk, Tg, CTE, ecc.).

<div class="div-type-1">

### CTI Requirement Explanation: indicatore di sicurezza fondamentale

Il CTI misura la capacità di un materiale isolante di resistere alla formazione di percorsi conduttivi di perdita sulla superficie sotto campo elettrico e contaminazione elettrolitica. La classe è definita da PLC (Performance Level Category): valori più alti indicano maggiore resistenza al tracking.

- **PLC 0:** CTI ≥ 600V (massimo livello; industria/energia/automotive HV)
- **PLC 1:** 400V ≤ CTI < 600V
- **PLC 2:** 250V ≤ CTI < 400V
- **PLC 3:** 175V ≤ CTI < 250V (FR‑4 standard tipicamente in questo intervallo)

Nei prodotti ad alta tensione o con requisiti di sicurezza stringenti, occorre definire chiaramente il livello CTI richiesto e selezionare materiali conformi.

</div>

### Albero decisionale di selezione dei materiali

| Indicatore chiave (Key Metric) | Materiali/livelli raccomandati | Scenari tipici | Vincoli/considerazioni |
| :--- | :--- | :--- | :--- |
| **CTI ≥ 600V (PLC 0)** | FR‑4 ad alto CTI (es. S1170G), resine fenoliche, alcuni poliimmidi (PI) | alimentatori industriali, inverter, EV BMS/OBC, medicale | costo più alto; meno opzioni — verificare disponibilità HILPCB. |
| **Bassi Dk/Df (Low Dk/Df)** | Rogers (RO4350B, Dk≈3.48), Megtron 6 (Dk≈3.6), Isola FR408HR | RF 5G/6G, server ≥25Gbps, `hdmi pcb stackup guide` | requisiti di processo elevati (es. plasma); costo superiore al FR‑4. |
| **Tg alto (High Tg > 170°C)** | S1000-2M, IT-180A, TU-768 | automotive, moduli ad alta densità di potenza, multicouche rame spesso | materiale più fragile; parametri di foratura da ottimizzare; pressatura ≈190–210°C. |
| **Z‑CTE basso (Low Z‑CTE)** | FR‑4 low‑CTE, Polyimide | HDI, BGA/LGA densi, schede spesse (>3.0mm) | migliora la affidabilità PTH, riduce cricche via in termocicli. |
| **Alta conducibilità termica** | MCPCB (Al, 1–3 W/m·K), ceramica (AlN, >150 W/m·K) | LED, moduli MOSFET, driver IGBT | spesso 1–2 strati; routing limitato; serve `thermal reliability stackup` dedicato. |
| **Flessibilità / piegatura** | Polyimide (PI) | wearables, rigid‑flex, flessione dinamica | controllo impedenza più complesso; considerare stiffener. |

---

## 3. Libreria di template stackup: punto di partenza per la standardizzazione

Il laboratorio HILPCB ha consolidato template standard sulla base di migliaia di progetti in produzione, validati con simulazione e misure.

### Template standard per schede multistrato

| Numero strati | Struttura (esempio) | Descrizione | Applicazioni chiave |
| :--- | :--- | :--- | :--- |
| **4 strati** | SIG/GND/PWR/SIG | `Core(0.76mm) + PP + Core(0.76mm)` | consumer, IoT. Economico ma attenzione all’EMI. |
| **6 strati** | SIG/GND/SIG/SIG/PWR/SIG | `Core + PP + Core + PP + Core` | buon compromesso costo/prestazioni; buona separazione segnale/power. |
| **8 strati** | SIG/GND/SIG/PWR/GND/SIG/PWR/SIG | `Core + PP + PP + Core + PP + PP + Core` | high‑speed (PCIe, USB 3.0); più reference plane, 50Ω/100Ω più facile. |
| **10 strati** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | `Core + PP...` | sistemi complessi, server; massimo EMI shielding e PI. |

### Template per strutture speciali

<div class="div-type-3">

#### HDI (High‑Density Interconnect) 叠层教程

Esempio di stackup **1+N+1 (N=6) HDI**, tipica struttura `hdi stackup tutorial`:

- **L1 (SIG):** Microvia (L1‑L2)
- **L2 (GND):**
- **L3 (SIG):** Buried Via (L3‑L6)
- **L4 (PWR):**
- **L5 (GND):**
- **L6 (SIG):**
- **L7 (GND):**
- **L8 (SIG):** Microvia (L8‑L7)

**Processo chiave:** laminazione sequenziale. Prima si realizza il core interno L2‑L7 con buried vias, poi si laminano L1 e L8 e infine si eseguono microvias laser. Questa struttura aumenta significativamente la densità di routing.

</div>

#### Rigid‑Flex e MCPCB

- **Rigid‑Flex:** struttura `zona rigida (FR‑4) – zona flessibile (PI) – zona rigida (FR‑4)`. La zona di transizione è critica: la tensione deve cambiare in modo graduale per evitare rotture del rame.
- **MCPCB (substrato in alluminio):** struttura `strato circuito (Cu) – strato isolante (alto k) – base metallica (Al)`. Conducibilità e tenuta dielettrica dell’isolante sono fondamentali per `thermal reliability stackup`.

---

## 4. Modellazione: impedenza / termica / meccanica

Una modellazione accurata è la garanzia che l’intento di progetto sia raggiungibile in produzione. Il team HILPCB usa modelli di primo principio.

### Modellazione dell’impedenza (Impedance Modeling)

Per segnali high‑speed (HDMI, DDR), il controllo d’impedenza è critico: tolleranza tipica **±10%**, talvolta **±5%**.

- **Microstrip (strato esterno):**
$$ Z_0 \approx \frac{87}{\sqrt{\epsilon_r + 1.41}} \ln\left(\frac{5.98H}{0.8W + T}\right) $$
- **Stripline (strato interno):**
$$ Z_0 \approx \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{4B}{0.67\pi(0.8W + T)}\right) $$

*Dove:*

- $Z_0$: impedenza caratteristica (Ω)
- $\epsilon_r$: costante dielettrica (Dk)
- $H$: spessore dielettrico
- $W$: larghezza traccia
- $T$: spessore rame
- $B$: distanza tra reference plane

**Esempio:** In un `hdmi pcb stackup guide`, per 100Ω differenziale con FR‑4 Dk=4.2, dielettrico 0.1mm e rame 1oz (0.035mm), la simulazione porta a una larghezza traccia ~0.12mm.

### Modellazione termica (Thermal Modeling)

Il cuore dell’analisi di affidabilità termica è il calcolo della catena di resistenze termiche.

- **Resistenza termica stazionaria 1D (Rth):**
$$ R_{th} = \frac{L}{k \cdot A} $$

*Dove:*

- $R_{th}$: resistenza termica (°C/W)
- $L$: lunghezza del percorso termico (m)
- $k$: conducibilità termica (W/m·K)
- $A$: area di sezione (m²)

Sommando le resistenze dal junction del chip alla superficie PCB e poi al dissipatore si può predire la temperatura di esercizio — base di `thermal reliability stackup`.

### Modellazione meccanica

Focus sulle tensioni dovute al mismatch di Z‑CTE. In termocicli −40°C…125°C, se Z‑CTE è troppo alto (>50 ppm/°C), il rame dei PTH subisce forte trazione con rischio di micro‑cricche o rotture. Scegliere materiali con Z‑CTE < 50 ppm/°C è chiave per l’alta affidabilità.

---

## 5. Hybrid stack / back‑drilling / strutture speciali

Per bilanciare costo e prestazioni, HILPCB supporta processi avanzati.

<div class="div-type-6">

### Stack ibrido (Hybrid Stack)

**Rogers + FR‑4:** la soluzione `hybrid stack` più comune.

- **Struttura:** Rogers (es. RO4350B) solo per gli strati RF esterni; strati interni digitali/power in FR‑4 high‑Tg più economico.
- **Sfide:** CTE e parametri di pressatura diversi; programma di laminazione dedicato. Adesione FR‑4↔Rogers più debole; spesso serve Plasma Treatment dopo foratura.
- **Beneficio:** risparmio 30–50% sul costo materiale mantenendo la performance RF.

</div>

### Back‑drilling

- **Obiettivo:** rimuovere i via stub nei canali high‑speed riducendo riflessioni e perdite, molto efficace oltre 10Gbps.
- **Processo:** dopo laminazione e metallizzazione, si fora dal lato opposto con punta di diametro maggiore per rimuovere la parte inutile; alta precisione di profondità.
- **Applicazioni:** backplane server, switch high‑speed, moduli ottici.

### Confronto surface finish (Surface Finish Comparison)

Il trattamento superficiale influenza direttamente l’affidabilità di saldatura e l’integrità del segnale.

| Trattamento | Pro | Contro | Applicazioni consigliate |
| :--- | :--- | :--- | :--- |
| **HASL** | basso costo, buona saldabilità | planarità scarsa, non ideale per fine‑pitch | consumer generalista |
| **ENIG** | superficie piana, resistente alla corrosione, ottimo per BGA | più costoso; rischio “black pad” | high‑speed, BGA/CSP, aree contatto |
| **OSP** | economico, molto piano, eco | scarsa conservazione; peggiora con reflow multipli | consumer, rotazione rapida |
| **Immersion Silver** | planarità buona, ottime proprietà elettriche | ossidazione; storage/handling severi | RF, telecom |

---

## 6. Validazione: dal controllo materiali alla affidabilità finale

Una `stackup strategy` robusta deve avere un processo di validazione in anello chiuso.

1. **IQC (controllo materiali in ingresso):** verifica CTI/Dk/Tg da datasheet e report; test a campione per materiali critici.
2. **Monitoraggio laminazione:** controllare profili temperatura/pressione secondo specifica; FR‑4 standard ≈ **180°C**.
3. **Coupon test d’impedenza:** coupon dedicati per lotto; misure TDR di 50Ω/100Ω ecc.; variazione entro **±10%** (core di `coupon test`).
4. **Analisi warpage:** misure ottiche (Shadow Moiré) prima/dopo reflow, target < 0.75%.
5. **Test di affidabilità:**
    - **Thermal Shock:** es. 1000 cicli −40°C ↔ 125°C e poi microsezioni PTH/microvia.
    - **IST:** riscaldamento rapido e carico di corrente sul coupon per accelerare stress termomeccanici e valutare affidabilità via.

---

## 7. Check‑list DFM/DFR/DFT

Questa check‑list (≥35 punti) aiuta a evitare problemi comuni di produzione, affidabilità e testabilità già in fase di design.

| Categoria | Regola / controllo | Parametri raccomandati / note | Metodo di verifica |
| :--- | :--- | :--- | :--- |
| **Materiali & stackup** | livello CTI conforme alla sicurezza? | scegliere PLC 0–3 in base alla tensione | design review |
|  | Dk/Df/Tg/CTE chiaramente indicati? | indicare il materiale nel stackup | design review |
|  | stackup simmetrico? | simmetria rame/dielettrico contro warpage | CAM |
|  | core/PP adeguati? | evitare un PP unico molto spesso | CAM |
| **Foratura** | diametro minimo meccanico | ≥ 0.20mm | DFM |
|  | diametro minimo laser (HDI) | ≥ 0.10mm | DFM |
|  | aspect ratio | < 10:1 (cons.), < 12:1 (limite) | DFM |
|  | hole‑to‑copper (line/plane) | ≥ 0.20mm | DRC |
|  | NPTH‑to‑copper | ≥ 0.25mm | DRC |
| **Routing** | line/space minimo | 3.5/3.5mil (inner), 4/4mil (outer) | DFM |
|  | evitare angoli vivi | 45° o archi | DRC |
|  | fanout area BGA | Dog‑bone o Via‑in‑Pad | layout review |
|  | lunghezze diff pair | errore < 5mil (in base al data‑rate) | CAD/layout |
| **Piani rame** | via sotto pad BGA/QFN? | Via‑in‑Pad consigliato (resin plug) | DFM |
|  | thermal relief | collegamento ≥ 50% della larghezza pad | DFM |
|  | distanza grande piano ↔ pad | ≥ 0.25mm | DRC |
|  | copper islands rimosse? | rimuovere isole non connesse | CAM |
|  | densità stitching vias | bordo e vicino HS, passo < λ/20 | layout review |
| **Solder mask** | larghezza solder mask dam | ≥ 0.10mm (4mil) | DFM |
|  | apertura mask | +0.05mm (2mil) per lato | DFM |
|  | tenting/plugging via | secondo test; default tent | spec |
| **Serigrafia** | larghezza linea | ≥ 0.15mm (6mil) | DFM |
|  | distanza serigrafia‑pad | ≥ 0.15mm (6mil) | DFM |
|  | polarità/RefDes leggibili | garantire leggibilità | layout review |
| **DFR** | creepage/clearance HV | seguire IEC‑62368‑1 ecc. | design review |
|  | metallo vicino al bordo | distanza ≥ 0.4mm | DFM |
|  | smusso gold finger | 30° o 45° | spec |
|  | stamp holes / V‑cut | separazione facile senza danni | DFM |
| **DFT** | dimensione/passo test points | Ø ≥ 0.8mm, passo ≥ 1.27mm | DFM |
|  | fiducials | ≥3 per board, in diagonale | DFM |
|  | punti ICT sotto componenti | evitare | layout review |
|  | JTAG/SWD esposti | facilità debug | design review |
| **Altro** | tolleranza spessore board | ±10% | spec |
|  | tolleranza impedenza | ±10% (standard), ±5% (strict) | spec |
|  | rame finale | soddisfare corrente | simulazione densità corrente |

---

## 8. Servizi HILPCB a ciclo chiuso: partner dalla teoria alla serie

Questo whitepaper riassume anche l’esperienza pratica di HILPCB. I servizi HILPCB formano un ciclo completo:

- **Materiali a magazzino & supporto laboratorio:** copertura da FR‑4 standard a Rogers/Megtron e verifica rapida CTI/Dk.
- **Simulazione stackup & servizi di design:** strumenti per impedenza, termica e SI per ottimizzare in fase iniziale.
- **Capacità di processo avanzate:** `hybrid stack`, back‑drilling ad alta precisione, HDI e rigid‑flex con esperienza di serie.
- **Feedback dalla produzione:** raccolta continua dati e risultati `coupon test` per migliorare regole DFM e template.

<div class="div-type-1">

**Call to action (CTA)**

Il tuo prossimo progetto merita una base più affidabile e ottimizzata. Contatta il laboratorio materiali HILPCB e **ottieni una revisione gratuita del design di stackup**. I nostri esperti forniranno raccomandazioni personalizzate su materiali e stackup in base alla tua `cti requirement explanation` e ai target prestazionali.

**[Contatta un esperto tecnico e avvia l’ottimizzazione del progetto](#contact)**

</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusione

In sintesi, questo articolo intorno a `cti requirement explanation` fornisce un albero decisionale di selezione materiali, una libreria di template stackup, metodi di modellazione di impedenza/termica/meccanica e un processo di validazione produttiva, corredati da una check‑list DFM/DFT/DFR. Applicando le check‑list e le finestre di processo e coinvolgendo presto il team DFM/DFA di HILPCB, puoi accelerare prototipazione e avvio serie garantendo qualità e conformità.

> Per supporto di produzione e assemblaggio, contatta HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) o [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) per raccomandazioni DFM/DFT.

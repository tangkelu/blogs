---
title: "Su un PCB mixed-signal non dividere troppo presto le masse: cosa verificare prima su return path, disciplina ADC e testabilità"
description: "Guida pratica a noise zoning, return paths, sistema locale ADC/reference/driver, decoupling, stackup e testabilità da congelare per primi su un PCB mixed-signal."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["Mixed-signal PCB", "ADC layout", "PCB grounding", "Decoupling", "EMC design", "DFM"]
---

# Su un PCB mixed-signal non dividere troppo presto le masse: cosa verificare prima su return path, disciplina ADC e testabilità

- **Su una mixed-signal board la prima cosa da rivedere di solito non è se analog ground e digital ground siano stati separati in due isole, ma come i correnti importanti ritornano davvero.** In MT-031 Analog Devices afferma esplicitamente che nei sistemi data converter il tema di AGND e DGND è capire i return-current paths, non tagliare meccanicamente il ground plane.
- **Molti ADC noise problems non nascono sulle tracce principali, ma quando ADC, reference, driver e rete di decoupling non vengono trattati come un unico sistema locale.** Le linee guida ADI per il mixed-signal layout raccomandano esplicitamente di mettere i connectors sul bordo scheda e tenere decoupling capacitors e crystal vicini al dispositivo mixed-signal.
- **Decoupling non significa semplicemente "aggiungere più condensatori". Significa ridurre il più possibile la high-frequency loop.** MT-101 insiste sul fatto che i decoupling capacitors devono stare il più vicino possibile ai supply pins per minimizzare la loop inductance.
- **Il partitioning deve seguire noise behavior e logica del ritorno, non solo i nomi funzionali del diagramma a blocchi.** Un layout che mette semplicemente "analogico a sinistra" e "digitale a destra" spesso nasconde le vere high di/dt loops, gli high-impedance nodes e le relazioni fra clock e rumore.
- **Un first-pass layout davvero utile non è solo low-noise. Deve anche essere manufacturable, measurable e repairable.** È questo che decide se il design può passare dal prototype a un pilot stabile e poi alla produzione.

> **Quick Answer**  
> Il cuore del layout di un PCB mixed-signal non è dividere per primi i piani di massa. Bisogna far funzionare insieme key return paths, sistema locale ADC, decoupling loops, noise partitions e accessi di debug / test. Su schede ADC/DAC, sensor acquisition e controllo, il successo dipende di solito meno da "abbiamo separato le masse?" e più da come sono stati trattati corrente, rumore e relazioni locali fra componenti.

## Indice

- [Cosa bisogna verificare per prima cosa su un PCB mixed-signal?](#overview)
- [Regole chiave e tabella riassuntiva dei parametri](#rules)
- [Perché il partitioning deve seguire il comportamento del rumore invece dei nomi funzionali?](#partition)
- [Perché la continuità del return path è più importante del "separare le masse"?](#return-path)
- [Perché ADC, reference, driver e decoupling vanno rivisti come un sistema locale?](#adc-local)
- [Perché stackup, DFM e testability vanno congelati presto?](#dfm)
- [Passi successivi con HILPCB](#next-steps)
- [FAQ](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa bisogna verificare per prima cosa su un PCB mixed-signal?

Bisogna partire da **noise partitioning, return paths, sistema locale ADC, decoupling, stackup e testability**.

Questo non equivale a dichiarare un'area analogica e una digitale e considerare il lavoro chiuso, e non è nemmeno qualcosa che si "aggiusta" più tardi dopo lo schematico. MT-031 di ADI è molto chiaro: nei sistemi data converter, la gestione di AGND / DGND riguarda soprattutto return-current paths e grounding boundaries, non il semplice taglio dei piani. MT-101 aggiunge che high-frequency bypass e decoupling capacitors devono stare il più vicino possibile ai supply pins per ridurre la loop area. Un'altra guida ADI sul mixed-signal layout raccomanda esplicitamente di mettere i connectors al bordo della scheda e di tenere decoupling parts e crystals vicini al mixed-signal IC.

Un ordine di layout review più solido è di solito:

1. **Identificare prima high di/dt loops, high-impedance nodes, clock sources e analog front ends sensibili.**
2. **Verificare poi che i key return paths siano corti e continui.**
3. **Trattare ADC, reference, driver, filter e rete di decoupling come un unico sistema locale.**
4. **Congelare presto stackup, logica della ground reference e strategia dei connectors sul bordo.**
5. **Rivedere test points, rework space e accesso per assembly prima di considerare chiuso il layout.**

Se il progetto combina analog front ends e alta densità di interfacce, di solito conviene portare già nella prima board review i vincoli di [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) e [SMT Assembly](https://hilpcb.com/en/products/smt-assembly), invece di lasciare che il DFM costringa a cambiare il layout in seguito.

<a id="rules"></a>
## Regole chiave e tabella riassuntiva dei parametri

| Regola / parametro | Approccio consigliato | Perché conta | Come verificarlo | Cosa succede se viene ignorato |
|---|---|---|---|---|
| Noise partitioning | Partizionare per high di/dt, clock, alta impedenza e front end sensibili | Le etichette funzionali non definiscono i confini del rumore | Layout review, analisi del return path | Il layout appare pulito, i percorsi di rumore restano mischiati |
| Return path | Mantenere un piano di riferimento continuo sotto nodi e tracce critiche | Return path interrotti causano insieme EMI e peggioramento del noise floor | Ispezione dei piani, near-field scan, misure | Rumore ADC, crosstalk ed EMC peggiorano insieme |
| Sistema locale ADC | Rivedere insieme ADC, reference, driver, filter e decoupling | La parte più sensibile è spesso la più corta local loop | Review di placement, probing locale | Il routing principale sembra buono, il comportamento locale no |
| Posizione del decoupling | Mettere il high-frequency decoupling vicino ai supply pins | Il decoupling lavora prima di tutto tramite loop area, non tramite il numero di capacitors | First-article check, oscilloscopio, osservazione EMI | Molti capacitors montati, poco effetto |
| Stackup e ground reference | Lo stackup deve servire sia il return path sia la stabilità di produzione | Uno stackup pensato solo per l'impedance può peggiorare board form e process risk | Stackup review, valutazione forma scheda | Il prototype funziona, il pilot disperde di più |
| Testability | Lasciare accessi test chiave e rework space già in rev A | Il debug mixed-signal dipende molto dall'observability | Accesso sonde, bring-up prima scheda | I problemi emergono ma la root cause resta nascosta |

| Contesto mixed-signal pubblico | Significato diretto per il layout |
|---|---|
| MT-031: prima il return path | "Separare le masse" non è la risposta standard; il ritorno di corrente è il vero tema |
| MT-101: decoupling vicino al pin | Il decoupling riguarda posizione e dimensione della loop, non solo quantità |
| ADI mixed-signal layout guide | Connectors sul bordo, support components vicini al mixed-signal IC |

<div style="background: linear-gradient(135deg, #eef6f3 0%, #eef3fb 100%); border: 1px solid #d7e1de; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7a68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #385f50; font-weight: 700;">Return Paths Before Ground Myths</div>
      <div style="margin-top: 8px; color: #23342e;">La prima domanda su una mixed-signal board è come ritorna la corrente, non se le masse siano state separate "abbastanza".</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7392; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38576f; font-weight: 700;">ADC Area Is a Local System</div>
      <div style="margin-top: 8px; color: #243441;">ADC, reference, driver e rete di decoupling non sono parti isolate. Sono il sistema locale più corto e più sensibile della scheda.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6948; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Decoupling Is Geometry</div>
      <div style="margin-top: 8px; color: #392f26;">Le prestazioni del decoupling dipendono da lunghezza della loop, posizione dei capacitors e struttura dei vias, non dal numero in BOM.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8b5d73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #70495c; font-weight: 700;">DFM Protects Analog Performance</div>
      <div style="margin-top: 8px; color: #392733;">Test points, spazio di rework, accesso AOI e limiti di panel non sono dettagli secondari. Decidono quanto velocemente si chiudono i problemi della prima scheda.</div>
    </div>
  </div>
</div>

<a id="partition"></a>
## Perché il partitioning deve seguire il comportamento del rumore invece dei nomi funzionali?

Perché **il vero conflitto su una mixed-signal board è tra sorgenti di rumore e nodi sensibili, non tra nomi dei blocchi nel diagramma funzionale**.

La guida ADI sul mixed-signal layout dice esplicitamente che il layout parte dal placement, che i connectors vanno al bordo e che i componenti di supporto come decoupling e crystals devono stare vicino al mixed-signal device. La logica sottostante è semplice: il partitioning deve seguire noise behavior e return-current logic, non i nomi dei blocchi nello schematico.

Un partitioning più efficace in genere significa:

- **trattare sensor front end, sorgente di reference e low-level analog inputs come una low-noise zone**
- **trattare clock sources, switch-mode power e fast digital interfaces come noise zones attive**
- **trattare ADC, DAC e isolation components come boundary nodes e non solo come semplici moduli**
- **mantenere una distanza fisica controllata fra ingresso connector, dispositivi di protezione e front end sensibili**

Se il layout si limita a "analogico a sinistra, digitale a destra", molti problemi reali restano nascosti: digital return current che attraversa la zona reference, clock vicino a ingressi ad alta impedenza, oppure rumore che entra dal connector direttamente nella zona più sensibile. Per schede che combinano interfacce e acquisizione analogica, è utile anche incrociare il ragionamento con l'approccio all'interface zone descritto in [Cosa validare prima su un EtherCAT Interface PCB Prototype](/code/blogs/blogs/1119-1-ccc/it/ethercat-interface-pcb-prototype.md).

<a id="return-path"></a>
## Perché la continuità del return path è più importante del "separare le masse"?

Perché **la maggior parte dei mixed-signal problems non nasce da "troppa poca massa", ma dal fatto che la corrente non trova un percorso pulito per tornare**.

È esattamente questo il punto centrale di MT-031: nei sistemi data converter, separare in modo aggressivo AGND e DGND spesso crea più problemi di quanti ne risolva. Le cose da confermare per prime sono:

1. **se segnali critici e decoupling loops hanno sotto di sé una reference plane continua**
2. **se il digital return current attraversa reference o regioni analogiche sensibili**
3. **se layer changes e boundary nodes continuano a offrire un return path locale a bassa impedenza**

Quando la corrente di ritorno è costretta a saltare slots, strozzature di rame o boundary scelti male, il risultato di solito non è un solo difetto ma una crescita insieme di rumore ADC, crosstalk, EMI e problemi di sincronizzazione. Su schede con fast digital interfaces, ADC e alimentazioni isolate, questo punto di solito merita di essere fissato prima del dibattito se dividere o no le masse.

<a id="adc-local"></a>
## Perché ADC, reference, driver e decoupling vanno rivisti come un sistema locale?

Perché **la parte più sensibile di una mixed-signal board di solito non è il trunk routing, ma la local loop più corta attorno all'ADC**.

MT-101 insiste sul fatto che il decoupling capacitor deve stare il più vicino possibile ai supply pins. La guida ADI sul mixed-signal layout dice anche che i support components attorno a un mixed-signal device devono restare vicini al componente stesso. La conclusione pratica è chiara: ADC, reference, driver, filter e rete di decoupling vanno rivisti come un unico sistema locale.

I punti che vale la pena isolare per una review mirata sono in genere:

- **quanto è corto e diretto il percorso fra ADC e front-end driver**
- **se la reference source resta lontana da heat e noise sources evidenti**
- **se il decoupling chiude davvero la loop a livello del pin**
- **se input protection e filtering proteggono l'ingresso senza portare dentro ulteriore rumore**

Molte prime schede rumorose non falliscono perché l'architettura di sistema è sbagliata, ma perché il sistema locale più corto e sensibile attorno all'ADC è stato separato fin dall'inizio. Se la scheda porta anche fast digital o synchronous interfaces, vale la pena ricontrollare return path e boundary logic con il ragionamento di stackup di [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) e [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).

<a id="dfm"></a>
## Perché stackup, DFM e testability vanno congelati presto?

Perché **se una mixed-signal board viene rivista solo come concetto elettrico e non come prodotto da costruire e da debuggare, il costo del pilot cresce rapidamente**.

I materiali applicativi ADI ricordano più volte che multilayer boards, reference planes a bassa impedenza e decoupling corretto sono condizioni base per raggiungere la performance nominale. In pratica questo significa:

- **lo stackup deve supportare sia la qualità del return path sia la stabilità produttiva**
- **test points, debug access e rework space devono esistere già nella prima revisione**
- **panel rails, process edges, accesso AOI e regioni analogiche sensibili non devono andare in conflitto**

Se questi input vengono rinviati, spesso il risultato è una scheda che funziona ma è difficile da misurare, difficile da riparare e difficile da riprodurre. Per progetti che vogliono arrivare rapidamente al pilot, di solito è più efficace portare presto nella pre-review i vincoli di [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) e [SMT Assembly](https://hilpcb.com/en/products/smt-assembly), invece di lasciare che siano i pilot builds a scoprire problemi che il layout poteva evitare.

<a id="next-steps"></a>
## Passi successivi con HILPCB

Se stai lavorando su acquisition board, control board, sensor front end o altro design elettronico mixed-signal, il passo successivo di solito consiste nel trasformare i "principi di layout" in input producibile:

- Quando il tema principale è return path, area locale ADC e ground reference, usare prima [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) per convergere stackup e logica dei reference plane.
- Quando il design porta anche fast digital interfaces o synchronous links, ricontrollare assegnazione layer e boundaries con [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- Quando l'obiettivo del prototype è verificare rumore, decoupling e testability, portare presto i checkpoint chiave nella fase [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quando sistema locale, ground reference e test access sono già convergenti, trasferire il set completo di requisiti in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) o [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Una mixed-signal board richiede sempre una separazione netta fra analog ground e digital ground?

Non sempre. MT-031 non dice "separare sempre". Dice che le domande importanti riguardano continuità del return path, definizione dei boundary e punto di connessione delle masse.

### Perché la simulation può sembrare buona mentre la prima scheda mostra comunque rumore elevato?

Cause comuni sono return paths interrotti, sistema locale ADC frammentato, cattivo placement del decoupling o sorgenti di rumore troppo vicine ai nodi sensibili.

### Perché molti decoupling capacitors non risolvono comunque il problema?

Perché MT-101 insiste ripetutamente su placement e loop area. Il numero di capacitors non è il fattore principale. La geometria della loop sì.

### Perché molti problemi ADC tornano al layout locale più che alle tracce principali?

Perché l'area ADC è il sistema locale più sensibile. Se reference, driver, filter, decoupling e trattamento della massa lì sono sbagliati, un trunk routing ordinato non salva il risultato.

### Quale production issue è più facile trascurare su una mixed-signal board?

Accesso ai test points, rework space, accessibilità AOI e fixture paths vengono spesso trascurati. Influiscono direttamente su efficienza del pilot e velocità di root cause.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [MT-031: Grounding Data Converters and Solving the Mystery of “AGND” and “DGND” | Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/mt-031.pdf)  
   Supporta il punto secondo cui sistemi mixed-signal e data-converter devono partire dalla comprensione di return paths e relazione AGND / DGND, non dal taglio meccanico dei planes.

2. [MT-101: Decoupling Techniques | Analog Devices](https://www.analog.com/media/en/training-seminars/tutorials/mt-101.pdf)  
   Supporta il punto che il high-frequency decoupling va collocato vicino ai supply pins per minimizzare inductance e loop area.

3. [What Are the Basic Guidelines for Layout Design of Mixed-Signal PCBs? | Analog Devices](https://www.analog.com/en/resources/analog-dialogue/articles/what-are-the-basic-guidelines-for-layout-design-of-mixed-signal-pcbs.html)  
   Supporta le linee guida pubbliche sul mettere i connectors al bordo scheda, i support components vicino al mixed-signal IC e sul risolvere il layout partendo dal placement anziché da correzioni a posteriori.

4. [AN-1142: Techniques for High Speed ADC PCB Layout | Analog Devices](https://www.analog.com/en/resources/app-notes/an-1142.html)  
   Usato per aggiungere contesto pubblico su power / ground planes, decoupling e stackup per high-speed ADC boards, mostrando che il tema "dividere o no le masse" dipende dal sistema reale e non da una regola fissa.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per mixed-signal e data acquisition
- Revisione tecnica: team engineering per processo PCB, EMC, analog front-end e test
- Ultimo aggiornamento: 2025-11-19

---
title: "Assemblaggio di substrate bridge per chiplet: cosa bloccare per primo tra zona bridge, warpage, underfill e test stratificati"
description: "Guida pratica ai primi punti da congelare nell'assemblaggio di un substrate bridge per chiplet, inclusi geometria della zona bridge, warpage, underfill, ispezione e strategia di cicli termici per progetti UCIe ed EMIB."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["chiplet packaging", "Bridge substrate", "Advanced packaging assembly", "UCIe", "EMIB", "Underfill"]
---

# Assemblaggio di substrate bridge per chiplet: cosa bloccare per primo tra zona bridge, warpage, underfill e test stratificati

- **La prima domanda su un substrate bridge per chiplet non riguarda la densità di routing, ma l'esistenza di una finestra di assemblaggio ripetibile nella zona bridge.** Le specifiche UCIe definiscono UCIe come standard aperto di interconnessione die-to-die a livello package, comprendendo physical layer, protocol stack, software stack e compliance testing.
- **Una struttura bridge non è semplicemente un substrato BGA più denso.** Intel descrive EMIB come un piccolo bridge in silicio integrato nel substrate per realizzare un'interconnessione die-to-die ad altissima densità senza un interposer in silicio di grandi dimensioni.
- **Un prototipo che si accende non è ancora un processo pronto per la produzione.** Intel Foundry separa wafer sort, die sort, burn-in, final test e system-level test, confermando che i difetti devono essere filtrati per livelli.
- **Zona bridge, underfill, cicli termici e tracciabilità del guasto vanno valutati insieme.** Il rischio più costoso non è di solito il blocco totale, ma una perdita graduale di stabilità sotto stress termo-meccanico con scarsa visibilità sulla root cause.
- **Un substrate bridge stabile non è un singolo campione che funziona, ma una zona bridge, un set di materiali, un flusso di assemblaggio e un piano di test che restano ripetibili tra i diversi lotti.**

> **Quick Answer**  
> Il cuore dell'assemblaggio di un substrate bridge per chiplet è far convivere in un'unica finestra di processo la struttura locale della bridge, la sequenza di posizionamento, l'underfill, il controllo del warpage e i test stratificati. Nei progetti UCIe ed EMIB conta meno il fatto che un campione si avvii e molto di più la possibilità di assemblare, verificare, tracciare e mantenere stabile la zona bridge dopo i cicli termici.

## Indice

- [Cosa bisogna controllare per prima cosa su un substrate bridge per chiplet?](#overview)
- [Regole chiave e riepilogo parametri](#rules)
- [Perché il progetto del substrate deve ruotare attorno alla finestra di assemblaggio della zona bridge?](#bridge-window)
- [Perché warpage, underfill e cicli termici vanno trattati come un unico problema?](#warpage-underfill)
- [Perché known good die, test stratificati e tracciabilità dei guasti vanno pianificati presto?](#kgd-test)
- [Come si valida l'assemblaggio di un substrate bridge prima della produzione?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [FAQ](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa bisogna controllare per prima cosa su un substrate bridge per chiplet?

Per prima cosa bisogna guardare **zona bridge, planarità locale, warpage, underfill, test stratificati e validazione in cicli termici**.

Non è semplicemente un problema di mettere più segnali in meno spazio. UCIe colloca nello stesso quadro l'interconnessione package-level die-to-die, il modello software e il compliance testing. La documentazione pubblica Intel su EMIB chiarisce che l'interconnessione è basata su un piccolo bridge in silicio incorporato nel substrate. Intel Foundry mostra inoltre una chiara separazione tra die sort, burn-in, final test e system-level test.

Un ordine di review iniziale più solido è di solito questo:

1. **Verificare che geometria della zona bridge, sequenza di assemblaggio e planarità locale rientrino in una finestra ripetibile.**
2. **Valutare warpage, flusso dell'underfill e stress di curing insieme alla zona bridge.**
3. **Assicurarsi che la strategia di test separi i difetti del die da quelli di assemblaggio nella bridge.**
4. **Inserire cicli termici e failure analysis nel piano pilota fin dall'inizio.**
5. **Definire prima del lancio i gate di ispezione, i campioni per sezione e la lot traceability.**

Se il progetto include già un'area bridge ultra-densa con microvia e strutture fine-pitch, conviene portare presto in review i limiti di producibilità di [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) e [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<a id="rules"></a>
## Regole chiave e riepilogo parametri

| Regola / parametro | Approccio consigliato | Perché è importante | Come verificarlo | Cosa succede se lo si ignora |
|---|---|---|---|---|
| Finestra della zona bridge | Riesaminare separatamente geometria locale e planarità attorno alla bridge | Il rischio maggiore è concentrato localmente, non nella media della scheda | Review strutturale, ispezione locale, coplanarity | I primi campioni si fanno, ma il pilot non è ripetibile |
| Controllo del warpage | Tracciare la forma della scheda dopo laminazione, placement, underfill e reflow | Le strutture locali multi-materiale sono molto sensibili al warpage | Warpage tracking, confronto tra fasi di processo | Il rendimento cala prima su coplanarity e bridge placement |
| Comportamento dell'underfill | Controllare completezza di riempimento, void e stress di curing | L'underfill può proteggere ma anche introdurre nuove tensioni | X-ray, sezione, confronto prima/dopo cicli termici | I primi campioni passano, ma la vita utile deriva |
| Test stratificati | Separare test del die, test di assemblaggio e system test finale | Permette di isolare rapidamente difetti die e difetti bridge | Die sort, burn-in, final test, SLT | Le cause si mescolano |
| Catena di tracciabilità | Collegare material lots, storia reflow, underfill e campioni | Molti difetti della bridge sono difetti nascosti | Record di lotto, sample ID, flusso FA | Dopo il guasto è difficile ricostruire |
| Validazione termociclica | Considerare i cicli termici come asse principale | Il rischio di durata nasce spesso da stress termo-meccanici | Cicli termici, sezioni, confronto strutturale | Il bring-up va bene, la durata no |

| Scenario di progetto | Focus di assemblaggio più comune |
|---|---|
| UCIe package-level bridge | Allineamento bridge, planarità locale, strategia di test per livelli |
| Struttura tipo EMIB | Cavity nel substrate, stress vicino alla bridge, underfill e ispezione |
| Multi-die / multi-chiplet substrate | Sequenza di placement, carico sulla bridge, cicli termici, traceability |

<div style="background: linear-gradient(135deg, #eef2fb 0%, #f7f0ea 100%); border: 1px solid #dcdfee; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #6d59a0; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #56457f; font-weight: 700;">Bridge Zone Is the Real Product</div>
      <div style="margin-top: 8px; color: #2f2941;">In un bridge substrate il vero obiettivo di processo non è la qualità media dell'intera scheda, ma la capacità della zona bridge di restare assemblabile, ispezionabile e ripetibile.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6849; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b5239; font-weight: 700;">Warpage Comes Early</div>
      <div style="margin-top: 8px; color: #382e24;">Con core sottili, materiali misti e alta densità locale, il warpage spesso diventa un problema di yield prima ancora dei guasti elettrici.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4d7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a5f51; font-weight: 700;">Underfill Is a Reliability Process</div>
      <div style="margin-top: 8px; color: #23342d;">L'underfill non è un passaggio estetico ma un processo di affidabilità. Riempimento incompleto o stress di curing errati riducono direttamente la vita utile.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7393; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38586f; font-weight: 700;">Testing Must Be Layered</div>
      <div style="margin-top: 8px; color: #243440;">Senza separare test di die, package e system, diventa molto difficile distinguere in seguito i difetti della bridge dai difetti del die.</div>
    </div>
  </div>
</div>

<a id="bridge-window"></a>
## Perché il progetto del substrate deve ruotare attorno alla finestra di assemblaggio della zona bridge?

Perché **la zona bridge è l'area locale più sensibile, meno ripetibile e spesso la prima a degradare**.

Intel descrive pubblicamente EMIB come un piccolo bridge in silicio incorporato nel substrate per realizzare un'interconnessione molto densa tra die. Questa architettura sposta l'attenzione dalla media dell'intera scheda alla finestra locale della bridge.

I punti da congelare in anticipo sono soprattutto:

- **La distribuzione locale del rame attorno alla bridge amplifica gli stress?**
- **La sequenza di placement aggiunge storia termica extra alla zona bridge?**
- **Planarità e coplanarity vicino alla bridge sono sufficienti per un assemblaggio ripetibile?**
- **Microvia, pad e margini della cavity restano dentro una finestra di processo reale?**

Se la zona bridge non viene trattata come un oggetto di processo dedicato, i pilot build raramente falliscono in modo clamoroso. Più spesso la finestra diventa solo troppo stretta e dipendente da continue regolazioni manuali. Per questo è utile coinvolgere presto [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) e [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<a id="warpage-underfill"></a>
## Perché warpage, underfill e cicli termici vanno trattati come un unico problema?

Perché **il rischio di vita utile su un bridge substrate raramente nasce da un singolo evento. Nella maggior parte dei casi è il risultato cumulativo della storia termica e degli stress dei materiali.**

Un bridge substrate passa tipicamente attraverso laminazione, assembly relativo alla bridge, die attach, underfill, reflow e ulteriori esposizioni termiche di test. Ogni fase può cambiare lo stato locale di stress. L'underfill non è sempre positivo in automatico. Può distribuire gli stress, ma riempimento incompleto, alto contenuto di void o mismatch in curing possono introdurre un nuovo meccanismo di guasto.

Gli elementi più utili da legare in una stessa review sono:

1. **La variazione del warpage locale prima e dopo l'underfill**
2. **L'integrità della zona bridge prima e dopo i cicli termici**
3. **L'eventuale concentrazione di void, contaminazione o flusso insufficiente nelle aree dense**
4. **La comparsa di nuove cricche o segnali di delaminazione dopo i cicli termici**

Se si valuta l'underfill solo dall'aspetto esterno senza collegarlo al comportamento in termociclo e alla struttura bridge, l'affidabilità di vita viene quasi sempre sovrastimata. Per gli engineering sample è sensato legare presto questi controlli al piano [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="kgd-test"></a>
## Perché known good die, test stratificati e tracciabilità dei guasti vanno pianificati presto?

Perché **nell'advanced packaging il guasto più costoso non è il difetto in sé, ma la perdita della capacità di capire rapidamente se il problema viene dal die, dalla bridge o dal processo**.

Intel Foundry mostra pubblicamente nel suo advanced chiplet test wafer sort, die sort, burn-in, final test e system-level test, sottolineando la consegna di known good die prima dell'assemblaggio finale. Per i bridge substrate questo significa in pratica:

- **I test devono essere stratificati e non limitarsi al solo power-up finale**
- **Die sort e known good die riducono il rumore nell'analisi dei difetti bridge**
- **Burn-in e system-level test fanno emergere meglio i difetti termo-meccanici marginali**
- **Lot traceability e collegamento dei sample devono esistere prima del pilot**

Senza queste basi, i problemi successivi appaiono come scarti sporadici, anomalie dopo i cicli termici o differenze tra lotti, ma senza chiarezza sul fatto che la causa sia il die, la bridge, l'underfill o la storia di assemblaggio. Se il prodotto si collega poi a un livello server o accelerator, è utile allineare questa vista package con la logica di sistema descritta in [Why AI Server Motherboards Can Power Up but Still Fail in Production](/code/blogs/blogs/1119-1-ccc/it/ai-server-motherboard-reliability.md).

<a id="validation"></a>
## Come si valida l'assemblaggio di un substrate bridge prima della produzione?

L'obiettivo reale è **chiudere il loop tra zona bridge, underfill, cicli termici e coerenza tra lotti**.

Un percorso di validazione realmente utile include di solito:

| Elemento di validazione | Domanda principale | Osservazioni consigliate |
|---|---|---|
| Controllo struttura locale / coplanarity | La zona bridge rientra nella finestra di assemblaggio? | Planarità intorno alla bridge, forma locale della scheda, stato dopo il placement |
| X-ray / sezione | Underfill e strutture nascoste sono completi? | Void, completezza del riempimento, aree di concentrazione difetti |
| Confronto prima / dopo termociclo | La zona bridge resta stabile sotto stress di vita utile? | Cricche, delaminazione, deriva visiva ed elettrica |
| Test stratificati | Si riescono a separare effetti di die, assembly e system behavior? | Anomalie viste in die sort, burn-in, final test e SLT |
| Confronto multi-lot | La finestra di processo è abbastanza ampia per la serie? | Dispersione board-to-board, deriva parametri, firme dei lotti |

Se il progetto è già vicino al pilot build, questi controlli devono essere scritti direttamente nel piano di produzione e test. Quando finestra bridge, comportamento dell'underfill, evidenze da termociclo e struttura di test convergono, è molto più semplice trasformare il tutto in una [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="next-steps"></a>
## Prossimi passi con HILPCB

Se stai lavorando su un progetto UCIe, EMIB o altro bridge substrate per chiplet, il passo successivo è di solito convertire "advanced packaging assembly" in input realmente producibili:

- Quando il punto principale è la zona bridge, con microvia e dettagli locali molto fini, usare i percorsi [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) e [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) per chiudere prima i limiti di processo locali.
- Quando l'obiettivo del pilot è validare finestra bridge, warpage e underfill, portare questi controlli molto presto nella review [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quando contano coerenza tra lotti e ricostruzione dei guasti, definire in anticipo sezioni, X-ray, material lots e tracciabilità dei parametri.
- Quando finestra bridge, struttura di test e requisiti di ciclo termico sono stabili, trasferire il pacchetto completo a [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) o [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### La difficoltà principale di un bridge substrate per chiplet è la densità di routing?

Non da sola. Di solito sono più difficili la finestra di assemblaggio locale della zona bridge, il warpage, l'underfill, i cicli termici e la logica dei test stratificati.

### Perché le strutture tipo EMIB rendono l'assemblaggio più sensibile?

Perché EMIB usa un piccolo bridge in silicio integrato nel substrate per un'interconnessione locale ad altissima densità. Questo rende più critici planarità locale, sequenza di placement, stress sulla bridge e comportamento dell'underfill.

### L'underfill migliora automaticamente l'affidabilità?

No. Se il riempimento è incompleto, pieno di void o crea uno stato di stress sfavorevole dopo il curing, l'underfill può diventare esso stesso una sorgente di guasto.

### Perché pianificare così presto test stratificati e tracciabilità?

Perché molti difetti dei bridge substrate sono difetti nascosti. Senza una separazione die / package / system e senza lot traceability, arrivare rapidamente alla root cause diventa difficile.

### Cosa conviene congelare per prima cosa prima di fabbricazione o pilot?

Conviene fissare prima finestra di assemblaggio della zona bridge, controllo del warpage, strategia underfill, struttura dei test stratificati, validazione in cicli termici e catena di tracciabilità dei guasti.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [Specifications | UCIe Consortium](https://www.uciexpress.org/specifications)  
   Fonte usata per le affermazioni su UCIe come standard aperto package-level die-to-die che copre physical layer, protocol stack, software stack e compliance testing.

2. [Intel® Stratix® 10 FPGAs Overview - Intel EMIB Packaging Technology](https://www.intel.com/content/www/us/en/products/details/fpga/stratix/10/article.html)  
   Fonte usata per l'affermazione secondo cui EMIB impiega un piccolo bridge in silicio integrato nel substrate senza un grande interposer in silicio.

3. [Advanced Packaging Innovations | Intel Foundry Packaging](https://www.intel.com/content/www/us/en/foundry/packaging.html)  
   Fonte usata per la discussione sui test chiplet avanzati per livelli con wafer sort, die sort, burn-in, final test, system-level test e consegna di known good die prima dell'assemblaggio finale.

4. [EMIB Technology Brief | Intel](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf)  
   Usato per completare il tema delle bridge integrate in cavity del substrate, dei package-assembly flows standard e del microbump pitch più stretto localizzato nella zona bridge.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per advanced packaging e high-density assembly
- Revisione tecnica: team di ingegneria per PCB process, assembly, termo-meccanica e failure analysis
- Ultimo aggiornamento: 2025-11-19

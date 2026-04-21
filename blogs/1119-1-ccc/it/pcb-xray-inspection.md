---
title: "Cosa deve davvero guardare una PCB X-Ray inspection: non si tratta solo di produrre immagini di void"
description: "Guida pratica a scope, interpretazione dei difetti, logica di campionamento, process feedback e traceability chain da definire per primi in una PCB X-Ray inspection."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# Cosa deve davvero guardare una PCB X-Ray inspection: non si tratta solo di produrre immagini di void

- **Il primo problema che una X-Ray inspection deve risolvere non è se sia stata acquisita un'immagine di difetto nascosto, ma se la qualità degli hidden joints possa essere davvero ricondotta ad assembly process, sampling rules e traceability chain.** I titoli pubblici di IPC-7095E e IPC-7093 mettono entrambi design e assembly process guidance al centro, e questo già mostra che l'X-Ray non va trattato come un semplice giudizio ex post sull'immagine.
- **L'X-Ray non va ridotto alla sola parola "void".** Su package BGA, BTC, QFN, LGA e grandi bottom pads, wetting, bridging, offset, head-in-pillow, joint consistency e distribuzione dei void rappresentano categorie di rischio diverse.
- **Il risultato X-Ray più utile non è trovare una sola scheda difettosa, ma riuscire a riportare l'immagine a stencil design, solder paste, geometry dei pad, profilo di reflow ed esposizione all'umidità.** Se l'immagine non rientra nel process, il miglioramento della qualità resta lento.
- **La sampling strategy va legata al rischio del package, al cambio di lot e al costo del failure.** Nuovi package, nuovi stencil, nuova solder paste o una nuova finestra di reflow non dovrebbero ereditare automaticamente la vecchia densità di sampling.
- **Immagini X-Ray senza lot number, equipment, program e giudizi registrati offrono poco supporto per future root-cause analysis e customer complaints.**

> **Quick Answer**  
> Il cuore della PCB X-Ray inspection non è produrre un'immagine nitida. Bisogna definire in anticipo quali package vanno controllati, quali rischi hidden-joint contano per ogni package family, come i findings tornano al process e come il risultato entra nella traceability chain. Su PCBA BGA, BTC e ad alta richiesta di reliability, l'X-Ray è uno strumento di process control, non soltanto un passaggio di accettazione.

## Indice

- [Cosa bisogna verificare per prima cosa in una PCB X-Ray inspection?](#overview)
- [Regole chiave e tabella riassuntiva dei parametri](#rules)
- [Quali prodotti e package dovrebbero includere l'X-Ray nel controllo di routine?](#scope)
- [Quali defect e segnali l'X-Ray dovrebbe cercare davvero?](#defects)
- [Perché il valore principale dell'X-Ray è il process feedback e non solo l'immagine?](#process)
- [Perché sampling strategy e traceability chain vanno progettate insieme?](#sampling)
- [Passi successivi con HILPCB](#next-steps)
- [FAQ](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa bisogna verificare per prima cosa in una PCB X-Ray inspection?

Bisogna iniziare da **package type, hidden-joint risk, logica di interpretazione dei difetti, sampling strategy e metodo di traceability**.

Questo non coincide né con il semplice chiedersi se la macchina sappia generare un'immagine, né con il solo verificare se il void ratio abbia superato una soglia. IPC-7095E per BGA e IPC-7093 per Bottom Termination Components includono entrambi design e assembly process guidance già nel loro scope pubblico. IPC ha inoltre indicato nel rilascio di J-STD-001J l'aggiunta di illustrazioni relative a bubbles viste in immagini X-Ray. Presi insieme, questi fatti pubblici mostrano già che l'X-Ray deve servire design, assembly, inspection e reliability, non solo una decisione visiva di accept / reject.

Gli elementi da congelare prima del pilot includono normalmente:

- **quali package e quali lot devono entrare nel controllo X-Ray di routine**
- **quali hidden-joint risks sono critici per ogni family di package**
- **se l'interpretazione è focalizzata su voiding, wetting, bridging, offset o consistency**
- **come cambia la densità di sampling con nuovi package, nuove process windows e livelli di rischio diversi**
- **come immagini, giudizi e process data entrano nella traceability chain**

Per i progetti con molti hidden joints, di solito conviene rivedere nello stesso momento le process windows di [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) e [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), invece di lasciare inspection strategy e assembly strategy scollegate.

<a id="rules"></a>
## Regole chiave e tabella riassuntiva dei parametri

| Regola / parametro | Approccio consigliato | Perché conta | Come verificarlo | Cosa succede se viene ignorato |
| --- | --- | --- | --- | --- |
| Scope di ispezione | Definire per primi quali package types e quali casi ad alto costo di failure richiedono X-Ray | I joints ad alto rischio non devono aspettare un guasto sul campo per essere controllati | NPI review, lista package, quality plan | Un rischio hidden-joint critico viene perso |
| Focus di interpretazione | Package diversi richiedono defect focus diversi, non solo analisi dei void | BGA, BTC e QFN non falliscono nello stesso modo | First-article image review, classificazione package | Le immagini ci sono, ma le conclusioni sono deboli |
| Process feedback | Ogni immagine deve poter essere ricondotta a stencil, paste, pad e reflow | Il valore dell'ispezione è il miglioramento del process | Collegare immagini e process parameters | I problemi si trovano ma non si correggono |
| Sampling strategy | Adattare il sampling per livello di rischio, process change e condizione del lot | Un template fisso di sampling può nascondere nuovi rischi | Piano sampling per first article e produzione | Le modifiche ad alto rischio passano inosservate |
| Traceability chain | Archiviare insieme image, board ID, program, shift e giudizio | Necessaria per failure analysis e gestione reclami | Review MES / log, collegamento al lot | La root cause dopo diventa congettura |
| Coordinamento design | Rivedere presto pad design, via in pad e aperture dei bottom pad | Molti findings X-Ray nascono già da layout e package design | DFM review, check package | La assembly window si rivela troppo stretta dopo il montaggio |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">Definire prima quali package e quali situazioni di lot richiedono X-Ray routinario. Senza scope, l'ispezione resta reattiva.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">Package diversi sono sensibili a defect nascosti diversi. Voiding, bridging, offset e head-in-pillow non possono condividere un solo template di lettura.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">Se l'immagine non torna a stencil, solder paste, pad design e reflow, il miglioramento del yield resta lento.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">Senza board ID, lot, program e decision records, le immagini X-Ray aiutano poco in customer complaints e failure analysis.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Quali prodotti e package dovrebbero includere l'X-Ray nel controllo di routine?

Come regola generale, **i package con hidden joints, alto costo di rework, dipendenza termica dal bottom pad o alto costo di field failure sono i candidati migliori per routine X-Ray**.

IPC-7095E è costruito attorno ai BGA, mentre IPC-7093 è dedicato ai BTC / Bottom Termination Components. Questo già indica che tali package non sono buoni candidati per un rilascio basato solo su AOI o visual inspection. La domanda di engineering più utile non è quindi "abbiamo una macchina X-Ray?", ma "se questo package viene saldato male, possiamo permetterci di scoprirlo solo al functional test o sul campo?"

I package da includere tipicamente sono:

- **BGA, CSP e altri hidden-ball packages**
- **QFN, LGA e dispositivi con grandi exposed bottom pads**
- **power devices in cui contano thermal path e joint consistency**
- **PCBA high-layer-count, fine-pitch o dense con rework costoso**
- **schede automotive, medicali, industriali o di comunicazione con maggiore esigenza di reliability**

Se il progetto si sta già muovendo verso il batch assembly, di solito è meglio inserire questi package nella lista di pre-controllo di [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) o [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), invece di decidere dopo il first article "quali bisognerebbe radiografare".

<a id="defects"></a>
## Quali defect e segnali l'X-Ray dovrebbe cercare davvero?

Perché **il vero scopo dell'X-Ray non è chiedersi "c'è un void?", ma identificare i hidden-joint failure modes rilevanti per quel package**.

BTC e BGA non portano gli stessi rischi, ed è proprio per questo che IPC li tratta in standard differenti. Per BGA, i controlli più utili riguardano wetting, collapse, offset, bridging e rischi di tipo head-in-pillow. Per BTC, QFN e dispositivi con grandi bottom pads, il focus è più spesso su distribuzione dei joint sottostanti, posizione dei void, coverage dei joint e consistency.

Le osservazioni più utili in ispezione includono di solito:

- **se il joint ha formato una wetting shape ragionevole e continua**
- **se i hidden joints mostrano bridging o clustering anomalo localizzato**
- **se i void si concentrano in aree termiche o meccaniche critiche**
- **se lo stesso componente e lo stesso lot mostrano una chiara dispersione geometrica**
- **se un'anomalia locale rimanda a behavior di design, printing o reflow**

Se la scheda contiene anche grandi thermal pads, aree di potenza complesse o alta heat density, è utile rivedere struttura pad e heat path insieme a [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb), invece di trattare l'X-Ray come un'azione solo post-assembly.

<a id="process"></a>
## Perché il valore principale dell'X-Ray è il process feedback e non solo l'immagine?

Perché **la domanda importante non è che esista una scheda cattiva, ma perché la stessa anomaly si ripete**.

IPC-7093 e IPC-7095 sono entrambi documenti di design and assembly process guidance e non semplici atlanti di immagini. Questo significa che l'immagine va letta insieme a stencil aperture strategy, condizione della solder paste, pad design, trattamento via in pad, esposizione all'umidità dei componenti e reflow profile. Senza questo collegamento, l'X-Ray può solo dire "qui c'è un problema", ma non "perché lo stesso problema continua a tornare".

I process factors da riportare indietro più spesso sono di solito:

- **se stencil thickness e aperture strategy sono adatti al package**
- **se type, lot, storage e usage condition della solder paste sono stabili**
- **se pad design, definizione del solder mask e via in pad treatment sono corretti**
- **se il reflow profile corrisponde al package e alle condizioni della scheda**
- **se moisture exposure, warpage o variazioni di board form di package o PCB sono state trascurate**

Se il progetto è ancora in prototype o pilot, di solito è meglio pianificare questi feedback loops insieme a [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) invece di trasformare l'X-Ray in un report di scarto isolato.

<a id="sampling"></a>
## Perché sampling strategy e traceability chain vanno progettate insieme?

Perché **il valore di controllo dell'X-Ray dipende da quando si ispeziona, quanto si ispeziona e se il risultato può essere riportato nel process**.

Il contesto pubblico dell'aggiornamento J-STD-001J mostra già che l'interpretazione delle immagini X-Ray viene formalizzata più chiaramente nelle pratiche di accettazione assembly. In termini di engineering, questo significa che la sampling strategy non può restare un template fisso. Deve cambiare con package risk, process maturity, process changes e costo del failure.

Un approccio più robusto di solito include:

1. **Aumentare la densità di inspection sui primi lots con nuovi package, nuovi stencil, nuova paste o nuovi programmi di reflow.**
2. **Dare priorità più alta a fine-pitch BGA, grandi bottom pads e dispositivi termici critici.**
3. **Legare i risultati di sampling a board ID, shift, program, lot della solder paste e impostazioni equipment.**
4. **Definire escalation rules verso sampling rafforzato o 100% inspection quando pattern anomali si ripetono.**
5. **Archiviare i judgment delle immagini insieme alle corrective actions, non separatamente.**

Senza una traceability chain, le immagini X-Ray supportano solo la decisione immediata. Con una traceability chain, supportano complaint handling, failure analysis e miglioramento continuo del process. Per i progetti vicini alla produzione, di solito è meglio scrivere queste aspettative direttamente in [Quote / RFQ](https://hilpcb.com/en/quote/) o nelle prime quality instructions.

<a id="next-steps"></a>
## Passi successivi con HILPCB

Se stai introducendo BGA, QFN, grandi bottom pads o un altro progetto con molti hidden joints, il passo successivo di solito consiste nel trasformare "inspection" in "process control input":

- Quando il tema principale è la hidden-joint assembly quality, portare prima package critici e control points nella review [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Quando fabbricazione PCB, sourcing, placement e test devono chiudersi come un unico process, usare [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) per allineare i workflow boundaries.
- Quando la scheda contiene high-heat-density parts o grandi exposed thermal pads, rivedere pad e heat-path design insieme a [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb).
- Quando package choice, pad design e process window vanno dimostrati presto, spostare quei checkpoint prima in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quando scope, sampling logic, metodo di interpretazione e aspettative di traceability sono definiti, trasferire l'intero set di requisiti in [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### La X-Ray inspection riguarda soprattutto il void percentage?

A: No. I void sono solo una categoria di rischio. Su molti prodotti wetting, bridging, offset, head-in-pillow, coverage dei joint e consistency tra lots contano altrettanto o di più.

### Quali prodotti dovrebbero inserire l'X-Ray nel routine process?

A: I prodotti con molti hidden joints, alto costo di rework, dipendenza termica dal bottom pad o forte requisito di reliability sono i candidati più forti per il routine X-Ray control.

### Perché il solo AOI non basta?

A: Perché molti joints critici sono sotto il body del componente, dove AOI non vede, e proprio quegli stessi joints spesso definiscono thermal path e long-term reliability.

### Perché alcuni team guardano molte immagini X-Ray ma migliorano lentamente il process?

A: La ragione più comune è che le immagini non sono mai state collegate a stencil, solder paste, reflow, pad design e lot data. Si rilevano anomalie, ma non si chiude la root cause.

### Cosa conviene congelare prima della produzione?

A: Conviene congelare per primi scope di inspection, logica di interpretazione dei defect, sampling strategy, trigger di escalation e traceability chain. Queste decisioni modellano il quality control nel lungo periodo più di un singolo risultato di inspection.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   Supporta il punto che IPC-7095E è impostato come design and assembly process guidance per BGA.

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   Supporta il punto che IPC-7093 è impostato sui Bottom Termination Components e include sezioni su X-Ray usage, repair e reliability.

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   Supporta il contesto pubblico che J-STD-001J ha aggiunto materiale illustrativo relativo alle bubbles viste nelle immagini X-Ray.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per PCBA quality
- Revisione tecnica: team engineering per assembly process, inspection e reliability
- Ultimo aggiornamento: 2025-11-19

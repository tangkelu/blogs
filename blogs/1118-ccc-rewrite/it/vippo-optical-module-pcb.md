---
title: "Quando vale davvero la pena usare VIPPO su un PCB per modulo ottico: come bilanciare escape HDI, planarità del pad e percorso termico"
description: "Una risposta diretta su quando usare il VIPPO su un PCB per modulo ottico e su come questo processo influisca su HDI escape routing, planarità del pad, saldatura SMT, percorso termico e validazione di produzione, aiutando il team a capire se introdurlo abbia davvero senso."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO", "Optical module PCB", "HDI PCB", "High-speed PCB", "Via in pad plated over", "PCB assembly"]
---

# Quando vale davvero la pena usare VIPPO su un PCB per modulo ottico: come bilanciare escape HDI, planarità del pad e percorso termico

- **VIPPO serve per aree dense in cui il via deve davvero stare dentro il pad. Non è un processo da estendere a tutta la scheda solo perché sembra più avanzato.**
- **Su un PCB per modulo ottico, i vantaggi principali del VIPPO sono più canali di escape, una transizione verticale più corta e un trasferimento più rapido del calore locale verso il rame interno.**
- **Il primo rischio del VIPPO non è il costo, ma perdere un pad che si comporti come un pad saldabile in modo ripetibile.**
- **Su una scheda per modulo ottico, il VIPPO va rivisto insieme a stackup HDI, strategia microvia, percorsi d’impedenza e validazione di assembly.**
- **Il criterio corretto non è "si può costruire una volta?", ma "si può costruire allo stesso modo in prototipo, pilot e volume?".**

> **Quick Answer**  
> VIPPO significa via-in-pad plated over. Su un PCB per modulo ottico vale la pena solo quando il normale fanout HDI non è più sufficiente o efficiente e il progetto richiede ancora saldatura stabile e un percorso termico piatto attraverso l’area del pad. I punti decisivi sono valore per il routing, planarità del pad, finestra di assembly e ripetibilità in produzione.

## Indice

- [Che cosa bisogna valutare per primo per il VIPPO su un PCB per modulo ottico?](#overview)
- [Tabella riepilogativa di regole e parametri chiave](#rules)
- [Perché il VIPPO non viene usato di default su tutta la scheda del modulo ottico?](#scope)
- [Perché la vera domanda di fabbricazione non è "si riesce a riempire il foro?", ma "il pad si comporta ancora come un normale pad saldabile"?](#fabrication)
- [Perché assembly e termica vanno rivisti insieme al VIPPO?](#assembly-thermal)
- [Come validare un PCB per modulo ottico con VIPPO prima della produzione?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Che cosa bisogna valutare per primo per il VIPPO su un PCB per modulo ottico?

Bisogna partire da **pitch dei componenti, densità di escape, planarità del pad richiesta, struttura HDI, percorso termico e metodo di validation per l’assembly**.

Questo non significa che "le schede high-end debbano usare VIPPO", né che ogni scheda per modulo ottico richieda automaticamente via-in-pad. Il contesto pubblico di IPC-4761 mostra che i metodi di protezione via servono a mantenere il design manufacturable con yield e cost accettabili, permettendo a progettista e produttore di valutare benefici e criticità delle diverse soluzioni. Su un PCB per modulo ottico, quindi, bisogna prima chiedersi:

1. **I normali fanout dog-bone, via offset o microvia sono già arrivati al limite?**
2. **La zona richiede davvero un via dentro l’SMD pad per chiudere il routing?**
3. **Il pad deve restare particolarmente piatto e ben bagnabile dopo l’SMT?**
4. **Il VIPPO sta servendo obiettivi reali di SI / termica oppure solo una grafica più densa?**
5. **Nel piano di prototype sono già inclusi cross-section, X-ray e thermal-cycle checks?**

<a id="rules"></a>
## Tabella riepilogativa di regole e parametri chiave

| Regola / parametro | Modo corretto di valutarlo | Perché conta | Come verificarlo | Cosa succede se lo si ignora |
|---|---|---|---|---|
| Ambito d’uso | Applicare VIPPO solo in zone di escape dense o su thermal pad critici | VIPPO ha valore, ma l’uso esteso alza costi e rischio assembly | Review layout, review densità componenti | Costi e rischi di assembly aumentano insieme |
| Planarità del pad | Valutare la solderable surface dopo filling, capping e planarization | I package fine-pitch sono sensibili alla consistenza della superficie | Microsection, aspetto, X-ray, first-article soldering | Solder wicking, joint poveri, coplanarity peggiore |
| Struttura via | Rivederla insieme a HDI, microvia e sequential lamination | VIPPO non è una semplice funzione di foratura isolata | Review stackup, fabrication DFM | Il routing regge a fatica, ma la finestra di processo è stretta |
| Percorso termico | Usare VIPPO per la termica solo dove il calore deve davvero scendere | Aiuta il flusso termico, ma non è una soluzione completa | Simulazione termica, termografia, confronto board-level | Un vantaggio locale viene scambiato per intero progetto termico |
| Interazione SMT | Valutare insieme stencil opening, volume pasta e profilo di reflow | La struttura del pad cambia direttamente la finestra di assembly | First article, X-ray, review del rework | Il prototipo si salda, ma il volume produttivo oscilla |
| Validazione di produzione | Definire cross-section, thermal cycle e verifiche multi-board già dal prototype | I problemi di affidabilità non emergono solo nel CAD | Coupon, thermal cycle, validazione multi-board | L’instabilità appare solo in pilot build |

| Domanda decisionale | Caso più adatto a VIPPO | Caso più adatto senza VIPPO |
|---|---|---|
| Escape di BGA fine-pitch | I canali vicini sono ormai praticamente scomparsi | Il fanout standard basta ancora |
| Dissipazione tramite thermal pad | Il calore locale deve essere trasferito rapidamente al rame interno | Il calore è gestito soprattutto da rame superiore o raffreddamento esterno |
| Assembly double-side | Un via-in-pad non trattato creerebbe forte solder wicking | Pad non critici possono accettare vias offset |
| Costi e process window | Il progetto accetta un costo maggiore per densità e stabilità del pad | I costi sono stretti e altre opzioni HDI bastano |

<div style="background: linear-gradient(135deg, #eef6f2 0%, #f7f1ea 100%); border: 1px solid #d7e1da; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #467566; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #35584d; font-weight: 700;">Density Is the Trigger</div>
      <div style="margin-top: 8px; color: #23342e;">La ragione giusta per partire con VIPPO non è l’effetto premium, ma l’esaurimento dei normali canali di escape.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6b48; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5238; font-weight: 700;">Pad Quality Is the Real Risk</div>
      <div style="margin-top: 8px; color: #392f26;">La difficoltà vera non è riempire il via, ma ottenere un pad che dopo filling, capping e planarization si saldi ancora come un normale land SMD.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4c7289; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395969; font-weight: 700;">HDI Context Matters</div>
      <div style="margin-top: 8px; color: #243640;">Il VIPPO va letto insieme a microvia, sequential lamination, impedance layers e transizioni tra layer. Una piccola ottimizzazione locale può spostare il rischio in fabbricazione.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #93595f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #74474b; font-weight: 700;">Validate Before Scale</div>
      <div style="margin-top: 8px; color: #3d262a;">La maturità del VIPPO per la serie si dimostra con microsection, X-ray, thermal cycling e consistency tra più schede, non con un solo campione riuscito.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Perché il VIPPO non viene usato di default su tutta la scheda del modulo ottico?

Conclusione: **Perché il VIPPO è uno strumento per risolvere escape densi e problemi speciali di pad, non un upgrade universale dell’intera scheda.**

Altium spiega pubblicamente che il via-in-pad compare quando la densità dei componenti è tale che i normali canali di fanout spariscono rapidamente. Solo quando il routing è costretto a spostarsi pesantemente negli strati interni, il via-in-pad passa da "comodo" a "necessario". Questo descrive bene le schede dei moduli ottici, dove DSP, retimer, driver e control BGA si concentrano in spazi molto ridotti.

<a id="fabrication"></a>
## Perché la vera domanda di fabbricazione non è "si riesce a riempire il foro?", ma "il pad si comporta ancora come un normale pad saldabile"?

Conclusione: **Perché la difficoltà produttiva del VIPPO non è chiudere il foro, ma ottenere dopo il filling un pad piatto, saldabile e ripetibile.**

Il sommario pubblico di IPC-4761 chiarisce che la protezione dei vias è legata a production issues, affidabilità a lungo termine e scelta dei materiali. Multi Circuit Boards spiega inoltre che un IPC-4761 Type VII deve portare a una superficie **flat and solderable** dopo filling, capping, planarization e metallizzazione.

Sul lato fabrication bisogna quindi controllare soprattutto:

- **se dopo il filling restano avvallamenti, rigonfiamenti o irregolarità locali**
- **se il pad cap e planarizzato bagna ancora in modo stabile**
- **se il surface finish è compatibile con questa struttura**
- **se la consistency da pad a pad è sufficiente**

<a id="assembly-thermal"></a>
## Perché assembly e termica vanno rivisti insieme al VIPPO?

Conclusione: **Perché il VIPPO cambia sia il comportamento della saldatura sia il modo in cui il calore locale entra nella scheda.**

Altium osserva pubblicamente che, se il via nel pad non viene trattato correttamente con fill, cap e planarization, durante il reflow la saldatura può migrare nel via barrel e creare joint abbassati o poveri. Su schede per moduli ottici questo è ancora più critico perché spesso convivono:

- BGA / LGA fine-pitch
- grandi bottom thermal pad
- assembly double-side o montaggio locale molto denso
- link high-speed sensibili alla qualità del rework

<a id="validation"></a>
## Come validare un PCB per modulo ottico con VIPPO prima della produzione?

Conclusione: **Una validazione utile deve dimostrare che il VIPPO pad si comporta ancora come previsto dopo fabrication, assembly e thermal cycling.**

| Voce di validazione | A quale domanda risponde | Punti di osservazione consigliati |
|---|---|---|
| Microsection / coupon | Filling, capping e planarization sono stabili? | Topografia del pad, completezza del filling, struttura interlayer |
| First-article SMT + X-ray | Il pad causa solder wicking, high voiding o joint disomogenei? | Joint BGA / LGA, consistency, grandi aree thermal pad |
| Termografia / test termico board-level | Il VIPPO migliora davvero lo spread of heat locale? | Delta-T del componente, direzione del flusso termico, regime stabile |
| Confronto multi-board | La process window è sufficientemente ampia? | Dispersione di saldatura e comportamento termico nella stessa area |
| Ricontrollo dopo thermal cycle | Struttura di pad e via resta stabile dopo i cicli? | Stato dei joint, cambiamenti in sezione, consistency del retest |

<a id="next-steps"></a>
## Prossimi passi con HILPCB

Se stai progettando una scheda per modulo ottico, una DSP control board o un’altra sub-board high-speed ad alta densità, il passo più utile è trasformare "serve il VIPPO?" in input producibili:

- Se il problema principale è l’escape di un BGA fine-pitch e la transizione tra layer, usa prima [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) per definire esattamente quali zone di pad richiedono davvero VIPPO.
- Se la scheda porta anche canali differenziali high-speed, rivedi in parallelo stackup e transition structure di [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), così da non ottimizzare i pad rovinando il canale completo.
- In fase prototype o EVT, porta direttamente microsection, X-ray, termografia e limiti di rework nella review [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quando regioni VIPPO, finish, assembly checks e requisiti di batch validation sono chiari, trasferiscili in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) o [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### Qual è la differenza principale tra VIPPO e un normale via-in-pad?

La differenza principale è che il VIPPO non si ferma al via dentro il pad. Il via viene riempito, cappato e planarizzato in modo che il pad si comporti come un normale land SMD.

### Ogni PCB di modulo ottico ha bisogno del VIPPO?

No. In genere il VIPPO ha senso solo quando l’escape fine-pitch è già estremamente stretto o quando un thermal pad locale richiede davvero un percorso termico verticale attraverso i pad vias.

### Il rischio principale del VIPPO è semplicemente il costo più alto?

No. Il costo è una conseguenza. Il rischio primario è la planarità del pad e la stabilità dell’assembly.

### Il VIPPO può risolvere da solo i problemi termici?

No. Può aiutare a portare il calore locale nel rame interno, ma non sostituisce un progetto termico completo.

### Perché prima della serie servono microsection e X-ray?

Perché molti problemi VIPPO non emergono nel CAD e non sempre sono visibili all’esterno. La microsection mostra il filling e la forma del pad, mentre l’X-ray mostra la qualità dei joint nascosti.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [IPC-4761 Table of Contents](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Supporta il contesto pubblico di benefici, limiti, production issues e aspetti materiali dei diversi metodi di protezione via.

2. [Increase Your Component and Trace High Density With Via-in-Pad Plated Over Technology | Altium](https://resources.altium.com/p/increase-your-component-and-trace-high-density-pad-technology)  
   Supporta la spiegazione pubblica dell’uso del via-in-pad in layout densi e fine-pitch BGA, incluso il rischio di solder wicking sui pad non trattati.

3. [What via Types Are Described in IPC-4761? | Altium](https://resources.altium.com/p/what-types-are-described-ipc-4761-0)  
   Supporta il contesto pubblico delle categorie di via protection IPC-4761 e l’inquadramento del Type VII usato qui.

4. [Via Covering | Multi Circuit Boards](https://www.multi-circuit-boards.eu/en/pcb-design-aid/surface/via-covering.html)  
   Supporta la spiegazione pubblica che il Type VII di IPC-4761 mira a ottenere una superficie flat and solderable, spesso usata in via-in-pad e sequential build-up.

5. [Download IPC 4761 In PDF | IPC WebStore Mirror](https://www.ipcemarket.com/product/ipc-4761/)  
   Supporta il riepilogo pubblico della terminologia IPC-4761 su tenting, plugging, filling, capping e affidabilità di lungo termine.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per HDI e produzione di moduli ottici
- Revisione tecnica: team di ingegneria per processo PCB, HDI, SMT e termica
- Ultimo aggiornamento: 2025-11-18

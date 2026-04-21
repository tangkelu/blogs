---
title: "Che cosa guardare per primo nel routing di connettori SFP e QSFP-DD: breakout 112G, backdrill e controllo della transizione sulla host board"
description: "Una risposta diretta su formato d’interfaccia, breakout, reference planes, backdrill, materiali e vincoli di assembly/termica da valutare per primi nel routing SFP e QSFP-DD a 112G, così da preservare il margine di canale nella zona del connettore su host board e backplane ad alta velocità."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["QSFP-DD routing", "SFP routing", "High-speed connector PCB", "Signal integrity", "Low-loss PCB", "112G PAM4"]
---

# Che cosa guardare per primo nel routing di connettori SFP e QSFP-DD: breakout 112G, backdrill e controllo della transizione sulla host board

- **A 112G PAM4, l’"ultimo pollice" vicino al connettore decide spesso il successo del link prima ancora della lunga traccia principale.**
- **Il focus di progetto non è identico tra QSFP-DD e SFP112, ma in entrambi i casi il punto reale è la stabilità di launch, breakout e return path.**
- **QSFP-DD è difficile non solo per la velocità, ma perché l’interfaccia a 8 lanes somma densità, carico termico e problemi SI sulla stessa host board.**
- **Un materiale migliore riduce le perdite totali, ma non salva un breakout sbagliato.**
- **Il routing del connettore va rivisto insieme a cage, heatsink e metodo di assembly.**

> **Quick Answer**  
> Il vero compito nel routing SFP e QSFP-DD non è soltanto portare le coppie differenziali dall’ASIC al bordo scheda. A 112G, breakout geometry, transizione del pad, strategia via/backdrill, reference planes e assembly del connettore devono funzionare insieme sulla host board. Il margine reale non nasce dal trunk routing più elegante, ma da un "ultimo pollice" ancora producibile, assemblabile e ripetibile.

## Indice

- [Che cosa bisogna valutare per primo nel routing SFP e QSFP-DD?](#overview)
- [Tabella riepilogativa delle regole e dei parametri chiave](#rules)
- [Perché la zona di breakout imposta spesso il limite inferiore di un canale 112G?](#breakout)
- [Perché vias, backdrill e reference planes devono convergere insieme nella zona di launch?](#launch-via)
- [Perché materiali, cage e termica non possono essere valutati separatamente dal routing?](#thermal-materials)
- [Come validare il routing del connettore sulla host board prima della produzione?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Che cosa bisogna valutare per primo nel routing SFP e QSFP-DD?

Bisogna partire da **form factor dell’interfaccia, numero di lanes e data rate, struttura del breakout, strategia via/backdrill e finestra termico-meccanica di assembly**.

La questione non è semplicemente "portare la differential pair al connettore e finire lì". E QSFP-DD non è solo "un SFP con più lanes". I documenti pubblici TE mostrano SFP fino a **112G** lane rate e QSFP-DD nel range **56-112G** come **8-lane PAM4 architecture**. Sulla host board, le prime domande devono quindi essere:

1. **Si tratta di un launch SFP112 a una / poche lanes oppure di un host launch QSFP-DD a 8 lanes?**
2. **La regione di breakout ha abbastanza layer, spazio di fanout e continuità di piano?**
3. **Servono backdrill, blind/buried vias o strutture via più spinte?**
4. **Cage, heatsink o stacked ports cambiano spazio disponibile e comportamento del return current sulla scheda?**
5. **Assembly e thermal management sono già stati rivisti nello stesso ciclo di review?**

Per switch, NIC, server board o backplane, di solito conviene allineare stackup e capacità di foratura di [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) e [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) prima di chiudere il layout.

<a id="rules"></a>
## Tabella riepilogativa delle regole e dei parametri chiave

| Regola / parametro | Modo corretto di valutarlo | Perché conta | Come verificarlo | Cosa succede se lo si ignora |
|---|---|---|---|---|
| Forma dell’interfaccia | Distinguere subito contesto SFP112 e contesto QSFP-DD 8 lanes | Densità e limiti termici sono molto diversi | Datasheet del connettore, system review | Stackup e breakout strategy diventano incoerenti |
| Percorso di breakout | Uscire rapidamente dal pad field con poco neck-down e poca distorsione | L’ultimo pollice consuma margine più in fretta | Simulazione 3D/2.5D, layout review | Il buon trunk routing non recupera la perdita del launch |
| Via / backdrill | Minimizzare through-via stubs sulle lanes veloci; usare backdrill se serve | La risonanza degli stub si amplifica rapidamente a 112G | TDR, microsection, review della foratura | Return loss peggiore, training instabile, BER in aumento |
| Reference planes | Mantenere sotto launch e breakout un return path continuo e prevedibile | L’interazione connector-PCB non è più trascurabile | Review dei planes, campo 3D | Crescono mode conversion e common-mode noise |
| Materiale / rame | Valutare rispetto alla lunghezza del canale e al budget di insertion loss | Il low-loss material risolve solo una parte del problema | Stackup review, simulazione IL, coupon | Materiale migliore ma link ancora instabile |
| Cage / heatsink / assembly | Valutare insieme cage, heatsink, coplanarity e stress di assembly | La zona del connettore è critica anche per l’assembly | Assembly review, thermal review, X-ray / visual check | Il prototipo funziona, la pilot consistency no |

| Esempio di interfaccia | Punto chiave pubblico | Indicazione di design |
|---|---|---|
| SFP | TE guide: lane rate 1-112G | Meno lanes, ma host launch comunque sensibile |
| QSFP-DD | TE page: eight-lane electrical interface, 28G/56G/112G, fino a 800 Gbps | Densità, termica e breakout risk si sommano |
| 112G host connection | Cadence: connector e final inch non vanno separati | Board e connettore vanno modellati insieme |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef6f1 100%); border: 1px solid #d5e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365c7c; font-weight: 700;">Final Inch First</div>
      <div style="margin-top: 8px; color: #233546;">Su una host board 112G, il rischio principale spesso si trova nei primi millimetri di breakout e di pad transition, non nella lunga tratta sul PCB.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7b72; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a6159; font-weight: 700;">Backdrill Is a Routing Decision</div>
      <div style="margin-top: 8px; color: #223630;">In un breakout 112G, il backdrill non è una correzione tardiva, ma una regola di routing che nasce dalla struttura dei vias e dalla strategia di transizione tra layer.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #886847; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Material Cannot Fix Launch Errors</div>
      <div style="margin-top: 8px; color: #3a2f25;">Un materiale low-loss può ridurre la perdita totale del canale, ma non corregge riflessioni e mode conversion create da stub, anti-pad o return path interrotti.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5f7d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c4960; font-weight: 700;">Cage and Thermal Change the Board</div>
      <div style="margin-top: 8px; color: #392733;">Cage QSFP-DD, heatsink e porte stacked modificano spazio, airflow e finestra di assembly sulla host board. Non si possono separare dalla SI.</div>
    </div>
  </div>
</div>

<a id="breakout"></a>
## Perché la zona di breakout imposta spesso il limite inferiore di un canale 112G?

Conclusione: **Perché la parte più fragile di un canale 112G è spesso la combinazione di connector pads, vias, anti-pads e dei primi millimetri di host routing.**

Cadence lo dice in modo esplicito: a data rate più bassi, connettore e reference board potevano spesso essere analizzati separatamente e poi combinati. A **112G PAM4** questa ipotesi non regge più, perché l’interazione elettromagnetica tra breakout region e connettore è troppo forte per essere ignorata. Sulle host board SFP e QSFP-DD questo significa:

- **perdita e riflessione nel launch non sono più effetti secondari**
- **crosstalk locale e mode conversion compaiono prima delle perdite sul percorso lungo**
- **se la geometria del breakout è instabile, l’equalization non recupera tutto**

<a id="launch-via"></a>
## Perché vias, backdrill e reference planes devono convergere insieme nella zona di launch?

Conclusione: **Perché in un breakout 112G la struttura dei vias e il return path fanno parte della prestazione del connettore stesso.**

L’errore più comune è trattare i vias come dettagli secondari e rimandare la discussione sul backdrill. In realtà through-via, residual stub, forma dell’anti-pad, passo dei ground-via e keep-out dei planes determinano insieme:

- se il return loss resta accettabile
- se l’insertion loss parte già troppo alto
- se la lane-to-lane consistency è sufficiente
- se common-mode noise e crosstalk vengono amplificati

Sul piano pratico, a 112G questo significa: **struttura via, backdrill e aperture dei reference planes vanno modellati e rivisti nello stesso ciclo.**

<a id="thermal-materials"></a>
## Perché materiali, cage e termica non possono essere valutati separatamente dal routing?

Conclusione: **Perché un canale 112G su host board non è solo una traccia, ma un sistema formato da materiale, connettore, cage, termica e assembly.**

TE colloca QSFP-DD come **8-lane PAM4 architecture** per HPC, AI/ML e networking ad alta densità. La pagina QSFP-DD sottolinea anche che opzioni stacked 2x1 possono dare alla host board più altezza per un airflow più uniforme e heatsink ASIC più grandi. Il datasheet Amphenol mette insieme connettori SMT 1x1 / 2x1, cage assembly stacked 2x1 e più opzioni heatsink.

Di conseguenza non si possono separare:

- **la capacità del materiale di rispettare il budget di perdita**
- **l’effetto di cage e heatsink sul confine meccanico e termico della zona porta**
- **la stabilità di coplanarity, stress di assembly e seating del connettore**
- **la coerenza di airflow e grounding quando più porte sono affiancate**

<a id="validation"></a>
## Come validare il routing del connettore sulla host board prima della produzione?

Conclusione: **Una validazione utile deve dimostrare che launch e canale principale restano validi dopo produzione e assembly reali.**

| Voce di validazione | A quale domanda risponde | Punti di osservazione consigliati |
|---|---|---|
| Co-simulazione 3D / 2.5D | Connettore e breakout funzionano come struttura unica? | Launch, anti-pad, ground vias, interazione con cage |
| Coupon / TDR | Stub via e discontinuità locali sono sotto controllo? | Plateau di impedenza, residual stub, punti di riflessione |
| Microsection e controllo foratura | Il backdrill dopo plating resta vicino al target di progetto? | Lunghezza stub, geometria foro, rame, coerenza |
| System link test | Moduli reali e host board mantengono margine sufficiente? | Training success, BER, coerenza tra lanes |
| Verifica multi-board / assembly | Saldatura del connettore e montaggio cage sono ripetibili? | Coplanarity, voiding, stress termico, dispersione tra schede |

<a id="next-steps"></a>
## Prossimi passi con HILPCB

Se stai lavorando a una host board SFP112 o QSFP-DD 112G, il passo più utile è trasformare il "routing high-speed" in input producibili per la zona del connettore:

- Usare prima [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) e [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) per convergere su stackup, materiali e direzione del canale 112G.
- Per breakout più densi e layer transition più strette, verificare in parallelo la finestra via / backdrill di [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) o [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).
- Durante il prototipo, portare connettore, cage, termica e controlli di assembly direttamente nella review [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Una volta allineati launch, backdrill, materiali e metodo di assembly, trasferire queste condizioni direttamente in [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) o [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### La perdita del materiale è la difficoltà principale del routing QSFP-DD 112G?

No. Conta, ma i primi problemi di una host board 112G emergono di solito da breakout geometry, qualità del launch, via stub, anti-pad e continuità del return path.

### Poiché SFP112 ha meno lanes, è molto più semplice di QSFP-DD?

La pressione di densità è più bassa, ma le regole di base non cambiano. Anche SFP112 deve gestire transizione 112G, controllo degli stub, scelta del materiale e coerenza di assembly.

### Si può decidere il backdrill solo dopo che il primo prototipo ha misure scarse?

Di norma no. In una zona connettore 112G, il backdrill è più una condizione di progetto iniziale che una correzione tardiva.

### Perché cage e heatsink influenzano la review del routing?

Perché cage, heatsink, stacked ports, spazio host board, airflow e grounding strategy sono tutti accoppiati.

### Perché una sola simulazione 2D non basta per una zona connettore 112G?

Perché Cadence indica esplicitamente che l’interazione elettromagnetica tra breakout region e connettore non è più trascurabile a 112G.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [TE High-Speed Input/Output Interconnect Selection Guide](https://www.te.com/content/dam/te-com/documents/datacomm/global/ddn-hsio-guide-en-2026.pdf)  
   Supporta il contesto pubblico secondo cui SFP arriva a 1-112G e QSFP-DD copre 56-112G come architettura PAM4 a 8 lanes.

2. [TE QSFP-DD Interconnects](https://www.te.com/en/products/connectors/high-speed-pluggable-io-connectors-and-cages/qsfp-dd.html)  
   Supporta la spiegazione sull’eight-lane electrical interface, i modi 28G NRZ / 56G PAM4 / 112G PAM4, fino a 800 Gbps per porta, e il legame tra cage/heatsink e host-board design.

3. [Cadence White Paper: Overcoming Signal Integrity Challenges of 112G Connections](https://www.cadence.com/ko_KR/home/resources/white-papers/overcoming-signal-integrity-challenges-of-112g-connections-wp.html)  
   Supporta la conclusione tecnica che a 112G connettore e breakout final inch vanno modellati insieme.

4. [Amphenol ExtremePort™ QSFP DD 112G Connectors Datasheet](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/datasheet/inputoutput/hsio_cn_extremeport_qsfp_dd_112g.pdf)  
   Supporta la descrizione pubblica di connettori 112G QSFP-DD, cage stacked e opzioni heatsink come un’unica host-interconnect system.

5. [QSFP-DD MSA Specification Page](https://www.qsfp-dd.com/specification/)  
   Supporta il contesto pubblico della specifica QSFP-DD come sistema a 8 interfacce elettriche ad alta velocità.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per high-speed interconnect e connettori
- Revisione tecnica: team di ingegneria per processo PCB, SI e high-speed assembly
- Ultimo aggiornamento: 2025-11-18

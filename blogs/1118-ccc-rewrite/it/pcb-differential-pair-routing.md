---
title: "Come instradare le coppie differenziali su PCB: regole pratiche per impedenza, piani di riferimento, skew e strutture via"
description: "Una risposta diretta su impedenza target, continuità del piano di riferimento, simmetria, compensazione di lunghezza, via stub e validazione di produzione da controllare per prime."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# Come instradare le coppie differenziali su PCB: regole pratiche per impedenza, piani di riferimento, skew e strutture via

- **La prima cosa da bloccare non è la perfetta uguaglianza di lunghezza, ma quale target definito da standard o datasheet la coppia debba realmente rispettare.** NXP richiede **85 ohm differential impedance** per PTN3222 eUSB2, mentre AN13335 per automotive Ethernet instrada l’MDI a **100 ohm**.
- **La simmetria conta più del semplice tenere le piste vicine.** Intel AN528 chiarisce che le due linee devono apparire elettricamente uguali, altrimenti compare differential-to-common-mode conversion.
- **Continuità del reference plane e layer change spesso degradano il link prima del tratto rettilineo.**
- **Serpentine, anti-pad e via stub non vanno applicati come un template fisso.**
- **Una coppia differenziale diventa producibile in serie solo quando stackup, tolleranze, breakout e validazione vengono definiti insieme.**

> **Quick Answer**  
> Il cuore del routing di una coppia differenziale su PCB è mantenere un ambiente di propagazione simmetrico nel vero stackup, con il vero spessore di rame e le vere strutture di transizione. Prima si congelano impedenza target e skew budget, poi si controllano same-layer routing, reference plane continuo, vias simmetrici e compensazione di lunghezza disciplinata, e infine si verifica il risultato reale con coupon, TDR o test di sistema.

## Indice

- [Cosa va controllato per prima cosa nelle coppie differenziali PCB?](#overview)
- [Tabella riassuntiva di regole e parametri chiave](#rules)
- [Perché la coppia differenziale va definita prima da standard e stackup?](#standards-stackup)
- [Perché simmetria, skew e serpentine tuning vengono spesso usati male?](#symmetry-skew)
- [Perché reference plane, cambi di layer e via stub sono zone ad alto rischio?](#planes-vias)
- [Come validare il routing prima della produzione?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa va controllato per prima cosa nelle coppie differenziali PCB?

Si parte da **target di impedenza dell’interfaccia, stackup, piano di riferimento, simmetria e strategia di cambio layer**.

Il tema non significa né "tracciare due piste in parallelo" né "finire il routing e poi lasciare al produttore il calcolo dell’impedenza". Protocolli, PHY e connettori diversi richiedono regole diverse. NXP AN13462 fissa eUSB2 a **85 ohm differential impedance** e vieta di attraversare plane split. NXP AN13335 impone **100 ohm** per automotive Ethernet MDI e limita il mismatch interno a **1 mm** tra connector e choke. Intel 82566 aggiunge **100 ohm differential impedance (±20%)** e meno di **50 mil** di mismatch nella coppia.

Quindi bisogna prima chiarire:

1. **Se l’interfaccia richiede 85, 90, 95 o 100 ohm differential**
2. **Da dove arriva lo skew budget ammesso nella coppia**
3. **Se il percorso è microstrip o stripline e se il reference plane resta continuo**
4. **Se i layer change sono consentiti e come verranno gestiti return current e stub**
5. **Se il produttore può mantenere in modo stabile la geometria sullo stackup previsto**

<a id="rules"></a>
## Tabella riassuntiva di regole e parametri chiave

| Regola / Parametro | Metodo | Perché è importante | Come verificare | Cosa succede se si ignora |
|---|---|---|---|---|
| Impedenza target | Confermarla da standard o datasheet | Non tutte le coppie differenziali sono 100 ohm | Standard, datasheet, stackup review | Width e spacing partono sbagliati |
| Simmetria | Tenere coerenti sezione, ambiente di riferimento e transizioni | L’asimmetria genera mode conversion | Layout review, review 3D | Più common-mode noise |
| Same-layer routing | Tenere la coppia sulla stessa layer il più possibile | I cambi layer aggiungono discontinuità | Post-route review, conta dei via | Più skew e reflection |
| Reference plane | Mantenerlo continuo e vicino | Un plane split rompe il return path | Plane review | Peggiorano EMI e mode conversion |
| Compensazione lunghezza | Solo in base al budget e vicino al punto di mismatch | Un serpentine errato crea impedance ripple | Skew review, TDR, simulation | La compensazione crea nuovi problemi |
| Via / stub | Minimizzare i via; se serve cambio layer usare signal via + GND via simmetrici | Via discontinuity è un rischio tipico high-speed | TDR, cross-section, backdrill review | Local reflection, ISI, deviazione del ritorno |

<a id="standards-stackup"></a>
## Perché la coppia differenziale va definita prima da standard e stackup?

Conclusione: **impedenza target e geometria non sono un template universale, ma il risultato congiunto dei requisiti di interfaccia e dello stackup reale di produzione.**

I documenti NXP e Intel lo mostrano chiaramente. eUSB2 è a **85 ohm**, automotive Ethernet MDI a **100 ohm**, e anche le true differential I/O di Intel restano nel contesto **100 ohm**. L’ordine corretto di lavoro è quindi in genere:

1. **Congelare la target impedance da standard, datasheet o reference design**
2. **Scegliere microstrip o stripline in base a loss, connector ed EMI**
3. **Confermare con il produttore materiali, spessori dielettrici, rame e compensazioni**
4. **Solo dopo scrivere width, spacing e tolerance nelle regole di layout**

<a id="symmetry-skew"></a>
## Perché simmetria, skew e serpentine tuning vengono spesso usati male?

Conclusione: **perché molte squadre scambiano equal length per correttezza, ignorando simmetria strutturale e variazioni locali di coupling.**

Intel AN528 richiede per una coppia ideale linee elettricamente uguali e skew il più vicino possibile a zero. Questo implica:

- **La simmetria non riguarda solo la lunghezza ma anche sezione, dielettrico, rame vicino e transizioni**
- **Lo skew è legato ai cambiamenti dell’ambiente di riferimento**
- **Un serpentine mal posizionato può avere un’impedenza peggiore della tratta principale**

Intel AN875 mostra inoltre che il trombone compensation può creare zone loosely coupled e una delay per unit length diversa. NXP raccomanda quindi di fare il tuning vicino al punto reale di mismatch.

<a id="planes-vias"></a>
## Perché reference plane, cambi di layer e via stub sono zone ad alto rischio?

Conclusione: **quando una coppia cambia layer, attraversa uno split o lascia uno stub, il primo rischio si concentra quasi sempre in return path e discontinuità locale.**

NXP vieta plane split sul percorso high-speed e consiglia stessa layer, pochi via e niente stub inutili. Intel aggiunge che:

- Il tratto residuo del barrel del via si comporta come capacitive stub
- Un layer change richiede GND vias vicini per il return current
- Le strutture via delle due linee devono restare simmetriche

Le zone tipicamente più rischiose sono:

1. **La radice del breakout BGA**
2. **Il connector launch**
3. **Le aree con AC-coupling capacitors e common-mode parts**
4. **I via di layer transition e le anti-pad zones**
5. **I through-via stubs non trattati nelle board più spesse**

<a id="validation"></a>
## Come validare il routing prima della produzione?

Conclusione: **una validazione utile non prova solo che in CAD la coppia sia stata instradata come pair, ma che dopo la fabbricazione restino validi sia geometria sia comportamento di sistema.**

| Voce di validazione | Domanda principale | Punto di osservazione |
|---|---|---|
| Stackup / impedance review | La geometria target è producibile? | Width, spacing, copper, dielectric, tolerance |
| Coupon / TDR | Impedenza reale e transizioni restano vicine al target? | Impedance plateau, discontinuità locali, effetto via |
| Cross-section | Pressatura e incisione hanno spostato la struttura? | Larghezza reale, rame, dielettrico, anti-pad |
| Test di sistema | La coppia è sana con dispositivi e connettori reali? | Eye diagram, training, BER, EMI |
| Confronto multi-board | Il rischio deriva dal design o dalla build variation? | Dispersione board-to-board, coerenza di lotto |

<a id="next-steps"></a>
## Prossimi passi con HILPCB

- Chiudere prima stackup, layer e reference strategy con [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) e [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).
- Usare l’[Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) prima del routing.
- Se il breakout è denso, controllare anche fanout e via window di [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Quando stackup, tabella di impedenza, coppie chiave e metodo di validazione sono pronti, inviarli direttamente in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) o [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### Le coppie differenziali sono sempre da 100 ohm per default?

No. Per esempio eUSB2 usa 85 ohm, mentre molte interfacce Ethernet o I/O high-speed usano 100 ohm.

### Basta avere due piste della stessa lunghezza?

No. Senza simmetria elettrica di piano di riferimento, rame vicino, via e anti-pad può comparire mode conversion anche con lunghezza uguale.

### Una coppia differenziale non dovrebbe mai cambiare layer?

Non necessariamente, ma i cambi layer vanno ridotti e trattati come una struttura completa con signal via, GND via, anti-pad e return path.

### Conviene concentrare tutto il serpentine in un unico punto?

Di solito no. La compensazione va vicina al punto di mismatch e non deve trasformarsi in una nuova discontinuità.

### Perché anche una coppia differenziale teme il plane split?

Perché non lavora indipendentemente dal reference plane. Uno split cambia il return path e aumenta il common-mode noise.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   Supporta i punti su symmetry, skew ridotto e impatto del fiber weave.

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   Supporta il rischio di impedance ripple e mode conversion con compensazioni a trombone.

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   Supporta la discussione su via stub, signal via simmetrici e GND vias per il return current.

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   Supporta i controlli di produzione su 100 ohm, mismatch, distanza dai GND vias e riduzione degli stub.

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   Supporta i requisiti eUSB2 su 85 ohm, symmetry, matching ed evitamento dei plane split.

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   Supporta il contesto 100 ohm MDI, la ground symmetry e il rischio common-mode.

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   Supporta il contesto 100 ohm e l’uso del backdrill quando serve ridurre gli stub.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per high-speed interconnect e SI
- Revisione tecnica: team PCB process, signal integrity e connector engineering
- Ultimo aggiornamento: 2025-11-18

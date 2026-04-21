---
title: "Come definire un HDMI PCB stackup: 100 ohm differential, loss budget e connector transitions"
description: "Una risposta diretta su versione target, impedenza differenziale 100 ohm, reference planes, material loss e connector transitions da valutare per primi in un HDMI PCB stackup."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# Come definire un HDMI PCB stackup: 100 ohm differential, loss budget e connector transitions

- **Il punto chiave di un HDMI stackup non è il numero di layer, ma quanta margin di produzione rimane al link alla velocità target.**
- **Il target di base resta 100 ohm differential, ma la vera difficoltà è mantenerlo in produzione.**
- **La continuità del reference plane e le launch transitions consumano spesso margin prima dei tratti rettilinei.**
- **Non ogni scheda HDMI richiede premium low-loss materials, ma non tutti i progetti sono sicuri su FR-4 standard.**
- **La validation deve usare fabrication data reali.**

> **Quick Answer**  
> Lo scopo di un HDMI PCB stackup design è far funzionare insieme 100 ohm differential pairs, continuous reference planes, low-loss geometry e connector transitions alla versione e lane rate target. Uno stackup è davvero valido solo quando, dopo lamination, etching e assembly, la link margin resta ancora disponibile.

## Indice

- [Cosa va controllato per prima cosa in un HDMI PCB stackup design?](#overview)
- [Tabella riassuntiva di regole e parametri chiave](#rules)
- [Perché l’HDMI stackup deve partire da un loss budget basato su velocità e lunghezza?](#loss-budget)
- [Perché la 100 ohm differential impedance deve essere legata alla fabbricazione reale?](#impedance)
- [Perché connectors, layer changes e stubs sono più pericolosi dei tratti rettilinei?](#transitions)
- [Come validare un HDMI stackup prima della produzione?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa va controllato per prima cosa in un HDMI PCB stackup design?

Si parte da **versione HDMI target, lane rate, lunghezza delle trace sulla board, reference planes e connector transitions**.

Non basta applicare regole high-speed generiche a una differential pair. HDMI 2.1b porta la capacità totale a **48Gbps**, e TI indica per FRL lane rates di **3/6/8/10/12Gbps**. Le prime domande diventano quindi:

1. **Il link è davvero HDMI 2.0 TMDS o è già in HDMI 2.1 FRL?**
2. **Lunghezza e posizione del connettore impongono layer changes o stubs lunghi?**
3. **Il normale FR-4 lascia ancora abbastanza margin?**
4. **Il reference plane resta continuo lungo tutto il percorso?**
5. **La fabbrica riesce a costruire in modo ripetibile la geometry target da 100 ohm differential?**

<a id="rules"></a>
## Tabella riassuntiva di regole e parametri chiave

| Regola / parametro | Come valutarlo | Perché conta | Come verificarlo | Se ignorato |
|---|---|---|---|---|
| Versione HDMI e rate | Distinguere TMDS fino a 6Gbps e FRL fino a 12Gbps/lane | La velocità definisce loss budget e material window | Specifica, datasheet, protocol setting | Stackup sbagliato, eye ed EMI margin ridotte |
| Differential impedance | Tenere le pairs HDMI intorno a 100 ohm differential | Requisito base della transmission structure | Calcolo impedenza, coupon, TDR | Più reflection e eye opening più stretto |
| Reference plane | Tenere la pair vicino a un continuous reference plane | La return-path continuity influenza SI ed EMI | Layout review, controllo layer changes | Più mode conversion e radiation risk |
| Materiale e rame | Scegliere in base a lunghezza, velocità e copper roughness | Perdite e spread produttivo crescono con la frequenza | Stackup review, microsection, insertion-loss test | Il prototype va, la serie si stringe |
| Connector / via transition | Launch, anti-pad, stub e layer changes vanno valutati a parte | I transitions falliscono spesso prima dei tratti lineari | 3D modeling, TDR, waveform misurata | Black screen, artifacts, instabilità |
| Manufacturing consistency | I design values devono tradursi in vera geometry di fabbrica | Lamination ed etching spostano le dimensioni | Microsection, coupon, confronto lotti | La margin deriva da lotto a lotto |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 e HDMI 2.1 non dovrebbero condividere una logica di stackup vaga. Prima si fissa il lane rate, poi si scelgono materiale, layer e length budget.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100 Ohm Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100 ohm non è solo un software target value. Deve restare valido anche dopo lamination, etching e geometria reale della superficie di rame.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">Sulle board HDMI la margin si perde spesso prima nelle connector launches, nei layer changes e negli stubs, non nei tratti rettilinei lunghi.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">Uno stackup HDMI maturo si dimostra con coupons, microsections e dati TDR / insertion loss che mostrano una geometry costruita ancora vicina al modello.</div>
    </div>
  </div>
</div>

<a id="loss-budget"></a>
## Perché l’HDMI stackup deve partire da un loss budget basato su velocità e lunghezza?

Conclusione: **perché la scelta di material family e stackup dipende da lane rate reale, lunghezza della trace e numero di transitions, non dalle abitudini generiche per questa interfaccia.**

HDMI 2.1b porta la total bandwidth a **48Gbps**. TI indica fino a **12Gbps** per lane in FRL e fino a **6Gbps** per HDMI 2.0b TMDS. Le domande reali sono quindi:

- **Quanto è lungo il percorso sulla board?**
- **Quanti connectors, ESD, redrivers e layer changes ci sono?**
- **FR-4 lascia ancora abbastanza margin?**
- **Il progetto è già entrato in una zona che richiede lower-loss material e controllo dielettrico più stretto?**

<a id="impedance"></a>
## Perché la 100 ohm differential impedance deve essere legata alla fabbricazione reale?

Conclusione: **perché la 100 ohm HDMI non è un target astratto, ma il risultato fisico di lamination thickness, etch compensation e reale geometry del rame.**

TI indica esplicitamente 100 ohm differential in più documenti HDMI. In produzione questo valore cambia per effetto di:

- dielectric thickness reale dopo la lamination
- line width incisa rispetto a quella disegnata
- copper roughness
- solder mask, forma del reference plane e rame vicino

<a id="transitions"></a>
## Perché connectors, layer changes e stubs sono più pericolosi dei tratti rettilinei?

Conclusione: **perché i segmenti HDMI rettilinei sono spesso controllabili, mentre launches, vias e layer changes introducono molto più facilmente local impedance steps, mode conversion e perdita addizionale.**

Da controllare separatamente:

- presenza di continuous reference plane sotto la connector launch
- geometry di via pad e anti-pad rispetto al target
- supporto dei ground vias al return current nei cambi layer
- necessità di accorciare o backdrill dei through-hole stubs
- simmetria della pair dopo il breakout

<a id="validation"></a>
## Come validare un HDMI stackup prima della produzione?

Conclusione: **una buona validation HDMI non dimostra solo che sul disegno esiste una pair da 100 ohm, ma che la board costruita mantiene davvero il target.**

Un percorso pratico include di solito:

| Validation item | Quale domanda chiarisce | Cosa osservare |
|---|---|---|
| Impedance coupon | La fabbrica riesce a costruire in modo ripetibile la geometry target? | Obiettivo 100 ohm e spread tra lotti |
| Microsection | Lamination ed etching hanno spostato la struttura? | Dielectric thickness, line width, copper profile |
| TDR o insertion-loss test | Transitions e path completo sono sani? | Local discontinuities, straight vs transition |
| Confronto multi-board | La process window è abbastanza ampia? | Coerenza di eye / impedance / loss |
| System-level test | Lo stackup funziona con veri connectors e devices? | Resolution, artifacts, soglia black screen, EMI |

<a id="next-steps"></a>
## Prossimi passi con HILPCB

- Convergere prima material target, copper foil e direzione dello stackup tramite [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- Usare presto l’[Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) per stimare la geometry da 100 ohm differential.
- Se la board include connector breakout, layer changes e fan-out più denso, verificare anche [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) o [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Quando stackup, coupon plan e launch review sono stabili, inserirli direttamente in [Quote / RFQ](https://hilpcb.com/en/quote/) o [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### Ogni board HDMI 2.1 richiede premium low-loss materials?

Non necessariamente. Tutto dipende da lane rate reale, lunghezza e numero di transitions.

### Basta disegnare la pair a 100 ohm?

No. Il risultato reale dipende anche da lamination, etch compensation, roughness e reference plane.

### Le HDMI differential pairs richiedono ancora un continuous reference plane?

Sì. Il differential routing non elimina il bisogno di un return path stabile.

### I problemi HDMI compaiono più spesso nella traccia o nella transizione del connettore?

Molto spesso nella connector launch, nel via layer change o nello stub.

### Perché coupons o TDR sono importanti?

Perché mostrano se la geometry costruita è ancora coerente con il modello.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   Supporta il contesto ufficiale di 48Gbps e risoluzioni / refresh più elevati.

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   Supporta i dati FRL a 3/6/8/10/12Gbps.

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   Supporta il contesto HDMI 2.0b / 6Gbps TMDS.

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   Supporta le regole 100 ohm HDMI e il controllo delle transitions.

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   Supporta la review congiunta di layer stack, controlled impedance, reference planes e vias.

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   Supporta la formulazione ufficiale dei 100 ohm ±10%.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team HILPCB per high-speed interface e stackup content
- Revisione tecnica: team PCB process, SI e high-speed connector engineering
- Ultimo aggiornamento: 2025-11-18

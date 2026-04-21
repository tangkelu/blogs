---
title: "Come progettare uno stencil SMT: cosa congelare prima su aperture, spessore e finestra di stampa"
description: "Una risposta diretta su logica delle aperture, scelta dello spessore, controllo fine-pitch, accoppiamento con i pad PCB e loop di feedback di produzione da confermare per primi."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["SMT Stencil Design", "Stencil Design", "Stampa pasta saldante", "SMT Assembly", "PCBA DFM"]
---

# Come progettare uno stencil SMT: cosa congelare prima su aperture, spessore e finestra di stampa

- **La prima cosa da congelare non è solo lo spessore dello stencil, ma quali strutture della scheda sono più difficili da stampare e più esposte a bridging o pasta insufficiente.**
- **Un’apertura stencil non è una copia meccanica del pad.**
- **Fine pitch, thermal pad centrale e BGA non possono condividere una sola logica semplice.**
- **Molti difetti che sembrano problemi di placement o reflow nascono in realtà dal fatto che pad PCB, solder mask e stencil non sono mai stati fatti convergere insieme.**
- **Uno stencil di serie valido migliora tramite feedback SPI, AOI e X-ray, non solo grazie a un singolo prototipo riuscito.**

> **Quick Answer**  
> Il cuore dello stencil SMT non è scegliere uno spessore universale, ma definire forma aperture, finestra di release, spessore, condizioni del pad e feedback di produzione attorno alle strutture più critiche.

## Indice

- [Cosa guardare per prima cosa nello stencil SMT?](#overview)
- [Tabella riassuntiva di regole e parametri chiave](#rules)
- [Perché la strategia delle aperture controlla in realtà volume di pasta e release?](#aperture)
- [Perché lo spessore dello stencil deve partire dalla struttura più sensibile?](#thickness)
- [Perché lo stencil va rivisto insieme a pad PCB, solder mask e parametri di assembly?](#pcb-dfm)
- [Perché uno stencil di produzione ha bisogno di un feedback loop sui dati?](#feedback)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa guardare per prima cosa nello stencil SMT?

Si parte da **package più sensibile, geometria aperture, spessore stencil, condizioni dei pad PCB, parametri di stampa e dati di validazione**.

Le domande iniziali più utili sono:

- **Quale package impone la più piccola aperture**
- **Quali pad richiedono un trattamento specifico**
- **Se lo spessore base protegge davvero il componente più critico**
- **Se pad, solder mask e vias degradano già la finestra di stampa**
- **Quali dati del pilota devono rientrare nella revisione successiva**

<a id="rules"></a>
## Tabella riassuntiva di regole e parametri chiave

| Regola / Parametro | Metodo | Perché è importante | Come verificare | Cosa succede se si ignora |
| --- | --- | --- | --- | --- |
| Trovare il componente più critico | Cercare aperture più piccole, pitch più fine e thermal pad complesso | Queste strutture fissano il limite | Package review, BOM check | Lo spessore è guidato dai componenti grandi |
| Strategia aperture | Separare per tipo di package invece di usare 1:1 | Controlla volume e release | SPI, test print, confronto difetti | Bridging, pasta insufficiente, slump |
| Scelta dello spessore | Proteggere prima la struttura più sensibile | Lo spessore controlla direttamente la finestra di release | First article, studio trasferimento | Le zone fine pitch cedono per prime |
| Accoppiamento con PCB | Rivedere pad, solder mask e via treatment insieme allo stencil | Molti difetti partono dal lato PCB | DFM review, confronto Gerber | Il tuning stencil non cura la causa |
| Strutture speciali | Valutare separatamente QFN center pad, BGA, PoP e step stencil | Sono le zone più instabili | X-ray, SPI, aspetto post-reflow | Voids, head-in-pillow, drift |
| Feedback dati | Legare SPI/AOI/X-ray alla revisione stencil | Solo così la serie converge | Storico versioni, Pareto | Gli stessi difetti ritornano |

| Regola empirica pubblica | Significato tecnico |
| --- | --- |
| IPC-7525C: nessuna regola unica per tutti gli stencil | Aperture e spessore vanno giudicati per progetto |
| Indium StencilCoach: aperture rettangolari spesso filtrate con `W/t > 1.5` | Utile per uno screening iniziale |
| Indium StencilCoach: aperture rotonde/quadrate spesso filtrate con `> 0.66` | Molto utile per BGA/CSP |

<div style="background: linear-gradient(135deg, #f7f4ef 0%, #f3f8f2 100%); border: 1px solid #e2ddd4; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6448; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f513b; font-weight: 700;">Aperture Controls Volume</div>
      <div style="margin-top: 8px; color: #382d24;">L’apertura controlla insieme volume di pasta, percorso di release e stabilità di stampa.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #59745f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #47604c; font-weight: 700;">Thickness Follows The Weakest Link</div>
      <div style="margin-top: 8px; color: #29352c;">Lo spessore deve prima proteggere la struttura più difficile da stampare.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #506d91; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405978; font-weight: 700;">PCB And Stencil Are Coupled</div>
      <div style="margin-top: 8px; color: #253544;">Senza convergenza tra pad, solder mask e vias, anche un buon stencil compensa solo localmente.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6174; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #714b5e; font-weight: 700;">Data Must Update The Stencil</div>
      <div style="margin-top: 8px; color: #392833;">Se SPI, AOI e X-ray non aggiornano lo stencil, i difetti ritornano come falsi problemi sporadici.</div>
    </div>
  </div>
</div>

<a id="aperture"></a>
## Perché la strategia delle aperture controlla in realtà volume di pasta e release?

Conclusione: **perché l’apertura definisce come la pasta lascia lo stencil e diventa un giunto saldato controllato.**

Da congelare prima:

- **Se le zone QFP/QFN richiedono riduzione o forma speciale**
- **Se le zone BGA/CSP rispettano una finestra area ratio realistica**
- **Se il thermal pad centrale va segmentato**
- **Se servono famiglie aperture differenti**

<a id="thickness"></a>
## Perché lo spessore dello stencil deve partire dalla struttura più sensibile?

Conclusione: **perché il limite di stampabilità della scheda è quasi sempre imposto dalla più piccola aperture o dal punto di release più difficile.**

Prima del freeze conviene verificare:

- **Dove sono le aperture più piccole**
- **Se uno spessore unico protegge ancora le zone fine pitch**
- **Se serve uno step stencil**
- **Se i pad grandi vanno compensati con la forma aperture e non con più spessore**

<a id="pcb-dfm"></a>
## Perché lo stencil va rivisto insieme a pad PCB, solder mask e parametri di assembly?

Conclusione: **perché molti difetti di stampa non sono problemi isolati di stencil, ma problemi di pad, solder mask, vias e package recommendation mai fatti convergere.**

Nello stesso ciclo va verificato:

- **La coerenza tra dimensione pad e land pattern raccomandato**
- **La riduzione della vera finestra pasta da parte del solder mask**
- **L’effetto di via-in-pad, plugging e surface finish**
- **L’eventuale bisogno di una strategia specifica per i voids sul thermal pad**

<a id="feedback"></a>
## Perché uno stencil di produzione ha bisogno di un feedback loop sui dati?

Conclusione: **perché un buono stencil di serie non è quello che stampa un solo prototipo accettabile, ma quello che ripete risultati simili lotto dopo lotto.**

Un loop utile include in genere:

1. **Classificare le famiglie critiche di componenti.**
2. **Legare i difetti alle famiglie aperture.**
3. **Legare lo spessore al mix componenti.**
4. **Leggere insieme X-ray e SPI.**
5. **Riportare le revisioni in controlled documents.**

<a id="next-steps"></a>
## Prossimi passi con HILPCB

- Per strategy aperture e package classification, coinvolgere prima [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Se sourcing, assembly e finestra reflow avanzano insieme, congelare la strategia con [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly).
- Per il controllo anticipato dei file, usare [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/).
- Per anticipare i rischi, portare le strutture critiche in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Discutere presto anche [PCB Surface Finish](https://hilpcb.com/en/services/pcb-surface-finish/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### Di solito basta una regola 1:1 tra aperture e pad?

A: No. Package diversi richiedono equilibri diversi tra volume pasta, release e wetting.

### Perché non si può scegliere lo spessore solo dal componente più grande?

A: Perché il limite di stampa deriva quasi sempre dalla più piccola aperture e dal release più difficile.

### Perché BGA e thermal pad centrali richiedono quasi sempre un trattamento dedicato?

A: Perché amplificano più facilmente voids, head-in-pillow, collasso non uniforme e drift.

### Perché i problemi stencil vengono spesso ricondotti ai pad PCB?

A: Perché pad, solder mask, via treatment e land pattern determinano direttamente il comportamento di stampa.

### Cosa conviene congelare prima della produzione?

A: Classificazione componenti, strategy aperture, spessore base o scelta step stencil, regole di accoppiamento con i pad PCB e loop SPI/AOI/X-ray.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [IPC-7525C TOC, Stencil Design Guidelines](https://www.ipc.org/TOC/IPC-7525C_TOC.pdf)  
   Supporta il fatto che lo stencil design sia una disciplina dedicata e non esista una regola unica valida per tutti.

2. [StencilCoach Standard Apertures | Indium Corporation](https://software.indium.com/stencil-coach/standard-apertures.php)  
   Supporta le regole empiriche su aspect ratio e area ratio.

3. [IPC Standards](https://www.ipc.org/ipc-standards)  
   Supporta la lettura congiunta degli standard stencil, PCB e assembly.

4. [Meet Your Standards | IPC-A-610](https://www.ipc.org/meet-your-standards)  
   Supporta il fatto che il giudizio finale riguardi l’accettabilità del giunto saldato finito.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per PCBA e assembly
- Revisione tecnica: team engineering processo SMT, DFM e qualità
- Ultimo aggiornamento: 2025-11-18

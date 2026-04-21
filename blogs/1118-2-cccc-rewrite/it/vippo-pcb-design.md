---
title: "Come progettare una VIPPO PCB: quando il via-in-pad vale davvero la pena e quando aggiunge solo rischio di assembly"
description: "Una risposta diretta su criteri di adozione, definizione di via protection, planarità del pad, finestra di assembly e metodo di validazione da congelare presto in una VIPPO PCB."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO PCB", "Via-in-Pad Design", "Via in Pad", "HDI PCB", "SMT Assembly"]
---

# Come progettare una VIPPO PCB: quando il via-in-pad vale davvero la pena e quando aggiunge solo rischio di assembly

- **La prima domanda non è se si possa mettere un via dentro un pad, ma se fanout normale, via protection normale e pitch attuale non riescano più a soddisfare insieme routing e assembly.**
- **VIPPO non è una singola azione CAD, ma una struttura combinata di via protection, riempimento, copper cap, planarità del pad e comportamento al reflow.**
- **Nei BGA fine pitch il rischio principale emerge spesso in assembly più che nel bare-board test.**
- **VIPPO è fortemente accoppiata a HDI, microvias e distribuzione locale del rame.**
- **Va congelata una struttura di serie, non solo una struttura che si salda una volta sul primo campione.**

> **Quick Answer**  
> Il cuore di una VIPPO PCB non è solo mettere un via nel pad, ma dimostrare che breakout, soldering e thermal path migliorano davvero mantenendo ripetibili via fill, copper capping, flatness e comportamento al reflow.

## Indice

- [Cosa controllare per prima cosa in una VIPPO PCB?](#overview)
- [Tabella riassuntiva di regole e parametri chiave](#rules)
- [Quando VIPPO è davvero la scelta giusta?](#need)
- [Perché definizione di via protection e struttura filled-via devono essere scritte chiaramente?](#structure)
- [Perché planarità del pad e finestra di assembly decidono il risultato di serie?](#assembly)
- [Perché VIPPO va verificata attraverso un reliability loop?](#validation)
- [Prossimi passi con HILPCB](#next-steps)
- [Domande frequenti (FAQ)](#faq)
- [Riferimenti pubblici](#references)
- [Autore e revisione tecnica](#author)

<a id="overview"></a>
## Cosa controllare per prima cosa in una VIPPO PCB?

Si parte da **ragione d’adozione, definizione di via protection, struttura via fill e copper cap, planarità del pad, finestra di assembly e metodo di validazione**.

Da chiarire presto:

- **Il pitch attuale e la pressione di breakout obbligano davvero il via-in-pad?**
- **Serve davvero limitare il solder wicking o accorciare il breakout fuori dal pad?**
- **La zona è anche accoppiata a HDI, microvia o alto flusso termico locale?**
- **Possono convergere insieme planarità del pad, solder-mask definition e strategy stencil?**
- **Il manufacturing package è abbastanza esplicito per PCB fabrication e assembly?**

<a id="rules"></a>
## Tabella riassuntiva di regole e parametri chiave

| Regola / Parametro | Metodo | Perché è importante | Come verificare | Cosa succede se si ignora |
| --- | --- | --- | --- | --- |
| Criterio d’adozione | Dimostrare che il fanout normale non basta più per densità e assembly | VIPPO è costosa e rischiosa | Fanout review, package review | Crescono costi e rischi senza vero beneficio |
| Definizione via protection | Definire esplicitamente protection, fill, covering e stato superficiale | Via-in-pad non può restare implicito | Fabrication notes, Gerber review | PCB shop e assembly leggono strutture diverse |
| Planarità pad | Guardare la coerenza dell’array più che il singolo pad | Influenza printing, placement e reflow | First article, coplanarity, X-ray | Head-in-pillow, cold joint e drift del yield |
| Structural coupling | Valutare VIPPO con microvias, buried vias e spessore rame locale | Le strutture impilate amplificano lo stress | Cross-section, DFM review, post-reflow checks | Il prototipo va bene, la serie no |
| Finestra di assembly | Congelare insieme stencil, paste, ponte solder mask e limiti di rework | Il rischio VIPPO spesso appare prima in SMT | SMT DOE, first article | Bare-board test passa, assembly yield cala |
| Validation loop | Vedere insieme coupon, cross-section, X-ray e stato post-reflow | Il successo della prima scheda non è ripetibilità | Multi-board validation, lot traceability | I latent defects emergono più tardi |

| Domanda iniziale | Azione ingegneristica più corretta |
| --- | --- |
| Routing stretto solo in un’area locale | Confrontare il guadagno reale di dog-bone fanout contro VIPPO |
| Pitch BGA molto stretto e solder wicking non accettabile | Congelare presto struttura integrata pad+via e condizioni di assembly |
| Il progetto usa anche HDI o microvias | Rivedere insieme via-in-pad e microvia |
| Serve una verifica rapida della chiarezza dei file | Usare prima [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/) |

<div style="background: linear-gradient(135deg, #f3f5fb 0%, #eef6f2 100%); border: 1px solid #d8dfe7; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #536f94; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405a79; font-weight: 700;">Need Before Structure</div>
      <div style="margin-top: 8px; color: #243545;">Prima si dimostra la necessità, poi si discute la geometria. Senza necessità reale il rischio viene solo spostato al centro del pad.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #55715d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #45614d; font-weight: 700;">Structure Must Be Explicit</div>
      <div style="margin-top: 8px; color: #27352b;">Se fill, copper cap e stato finale della superficie non sono scritti chiaramente, fabrication e assembly lavoreranno con ipotesi diverse.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6a4e; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f543d; font-weight: 700;">Assembly Fails First</div>
      <div style="margin-top: 8px; color: #372c24;">Molti problemi VIPPO non si vedono nel bare-board test ma emergono con printing, reflow e X-ray.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a5e73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #70485c; font-weight: 700;">Repeatability Matters</div>
      <div style="margin-top: 8px; color: #392833;">VIPPO diventa pronta per la serie solo quando multiple boards, reflows e assembled states restano stabili.</div>
    </div>
  </div>
</div>

<a id="need"></a>
## Quando VIPPO è davvero la scelta giusta?

Conclusione: **VIPPO vale la pena solo quando il fanout normale sacrifica già spazio di routing, controllo della saldatura o thermal path e strutture più semplici non risolvono più il problema.**

Da confermare:

- **L’array package è davvero bloccato dallo spazio di breakout?**
- **Uno schema via normale rende già il pad non accettabile?**
- **Il thermal path locale richiede davvero un via nel pad?**
- **VIPPO serve solo a pochi package critici o all’intera scheda?**

<a id="structure"></a>
## Perché definizione di via protection e struttura filled-via devono essere scritte chiaramente?

Conclusione: **perché il risultato manufacturing di VIPPO dipende fortemente da ciò che il design richiede in modo esplicito, non da come “di solito lavora” la fabbrica.**

Da scrivere esplicitamente:

- **Quali pad richiedono via-in-pad**
- **Se questi via servono per breakout, thermal transfer o assembly control**
- **Quali sono i requisiti di fill, covering e flatness superficiale**
- **Se sono presenti anche microvias, buried vias o stackup speciali**
- **Dove servono coupon, cross-section o verifiche extra**

<a id="assembly"></a>
## Perché planarità del pad e finestra di assembly decidono il risultato di serie?

Conclusione: **perché per BGA, LGA e fine-pitch package VIPPO deve alla fine comportarsi come un pad stabile, non come una posizione speciale solo “teoricamente saldabile”.**

Da congelare insieme:

- **Coerenza di tutto l’array di pad**
- **Se lo stile solder mask comprime la vera finestra pasta**
- **Se lo stencil è progettato sulla superficie reale del pad dopo VIPPO**
- **Se le zone BGA critiche richiedono targeted X-ray sampling**

<a id="validation"></a>
## Perché VIPPO va verificata attraverso un reliability loop?

Conclusione: **perché il rischio reale spesso non è “impossibile da fare”, ma “fatto e saldato una volta, poi instabile sotto reflow, cambio lotto o stress”.**

Un release path pratico include di solito:

1. **Freeze della ragione d’adozione.**
2. **Freeze della manufacturing definition.**
3. **Freeze degli input assembly.**
4. **Freeze della physical validation.**
5. **Freeze della lot traceability.**

<a id="next-steps"></a>
## Prossimi passi con HILPCB

- Per dense breakout e local layer escape, partire dal percorso [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Per confrontare approccio standard e high-density, rivedere insieme [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) e VIPPO.
- Per i rischi su pad, stencil e reflow, coinvolgere [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Per verificare la chiarezza dei file manufacturing, usare prima [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/).
- Per sample o pilot build, anticipare i controlli chiave in [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) e [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Domande frequenti (FAQ)

<!-- faq:start -->

### Tutte le schede BGA dovrebbero usare VIPPO di default?

A: No. VIPPO vale solo se il fanout normale non è più accettabile o se il vantaggio su solder control e thermal path è chiaramente dimostrato.

### Perché i problemi VIPPO emergono spesso solo in SMT?

A: Perché la struttura cambia il vero solder behavior del pad, e questo si vede soprattutto in printing, reflow e X-ray.

### Basta scrivere “filled via” nel disegno?

A: No. Bisogna definire anche via protection, tipo di covering, requisito di flatness, validation method e assembly boundaries.

### Perché VIPPO e HDI vanno riviste insieme?

A: Perché via-in-pad è spesso accoppiata a microvias, transizioni dense, stackup complesso e multiple reflow cycles.

### Cosa conviene congelare prima della produzione?

A: La ragione d’adozione, la definizione pad/via, le condizioni di flatness e assembly, il metodo di physical validation e la lot traceability.

<!-- faq:end -->

<a id="references"></a>
## Riferimenti pubblici

1. [IPC-4761 Design Guide for Protection of Printed Board Via Structures](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Supporta il fatto che VIPPO debba essere esplicitamente specificata come via-protection structure.

2. [IPC Board Design Standards](https://www.ipc.org/ipc-board-design-standards)  
   Supporta il contesto comune di IPC-4761, IPC-2221, IPC-2226 e IPC-6012.

3. [IPC Releases IPC-6012F, Qualification and Performance Specification for Rigid Printed Boards](https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed)  
   Supporta l’anticipazione della validation di strutture interconnect complesse e coupon.

4. [IPC Issues Electronics Industry Warning on Printed Board Microvia Reliability for High Performance Products](https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high)  
   Supporta il rischio di latent failures in strutture microvia / via-in-pad dopo reflow o stress.

<a id="author"></a>
## Autore e revisione tecnica

- Autore: team contenuti HILPCB per HDI e assembly
- Revisione tecnica: team engineering processo PCB, DFM e SMT
- Ultimo aggiornamento: 2025-11-18

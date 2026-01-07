---
title: "stackup documentation guide: un playbook process-driven per PCB manufacturing e testing"
description: "Usando una stackup documentation guide come backbone, questo walkthrough end-to-end copre dettagli di manufacturing, checkpoint di quality control e consigli DFM/DFT: dai materiali e imaging a soldermask, SMT e test validation."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["stackup documentation guide", "soldermask exposure tutorial", "smt stencil design tutorial", "pcb fabrication process steps", "yield improvement roadmap", "surface finish selection tips"]
---
Ciao, sono un docente della HILPCB Manufacturing Academy. Nel lavoro quotidiano noto che molti design engineers trattano una `stackup documentation guide` come “solo” un documento che definisce struttura di laminazione e impedance control. Dal punto di vista manufacturing-and-test, però, è il “genesis blueprint” e la “execution constitution” dell’intero production flow. Non determina solo la performance elettrica: influenza profondamente yield, reliability e cost in ogni fase, dai materiali in ingresso fino al functional testing finale.

Oggi useremo questo documento core come filo conduttore per attraversare l’intero flusso di PCB manufacturing e test. Non è solo un **pcb manufacturing tutorial**, ma anche una **yield improvement roadmap** che collega design intent e manufacturing reality. Scomporremo processi complessi in step stile SOP e checklist, così il tuo team può interiorizzare davvero DFM (Design for Manufacturability) e DFT (Design for Testability).

## Manufacturing flow overview: dal documento di stackup al prodotto fisico

Una `stackup documentation guide` dettagliata è il punto di partenza della fabbricazione. Definisce materiali, thickness, copper weight e tolleranze: parametri che fissano la process window in produzione. La tabella sotto mostra come i principali process steps si mappano direttamente sulle informazioni del documento di stackup.

| Process Step | Core Objective | Key Control Parameters | Related Stackup Info |
| :--- | :--- | :--- | :--- |
| **Laminate preparation** | Assicurare che i materiali rispettino i requisiti di progetto | Material type, board thickness, copper thickness, dimensional accuracy | Core e prepreg (PP) types, Dk/Df, Tg, CAF resistance |
| **Inner-layer imaging** | Replicare con precisione i pattern degli inner layer | Exposure energy, develop time, registration (±25 µm) | Inner-layer copper thickness (es. 0.5 oz, 1 oz), minimum line/space |
| **Lamination** | Pressare la struttura multilayer in un unico pannello | Temperature/pressure/time profile, resin-flow control | Stack order, PP type/quantity, overall thickness tolerance (±10%) |
| **Drilling** | Creare fori passanti e fori di montaggio | Spindle speed, feed rate, hole-position accuracy (±50 µm) | Hole size, hole type (PTH/NPTH/blind/buried), hole density, minimum annular ring |
| **Plating** | Costruire la connessione elettrica tra layer | Rectifier current density, bath chemistry, copper thickness (>20 µm) | Aspect ratio, copper thickness requirements |
| **Outer-layer imaging** | Replicare con precisione i pattern degli outer layer | Registration, etch-factor control | Outer-layer copper thickness, impedance-trace width, BGA/QFN pad sizes |
| **Soldermask** | Proteggere le tracce e definire aree saldabili | Ink type/thickness, exposure accuracy, curing conditions | Soldermask color, minimum Solder Mask Dam width |
| **Surface finish** | Fornire solderability e protezione | Plating thickness (es. ENIG: Au 0.03–0.08 µm), flatness | [Surface Finish](/blog/pcb-surface-finish/) (HASL, ENIG, OSP, etc.) |
| **SMT assembly** | Posizionare e saldare i componenti | Paste volume, placement accuracy, reflow profile | BOM, packages, pad design |
| **Test & validation** | Garantire funzione elettrica e reliability | Coverage, fault-diagnosis accuracy | Test-point layout, net connectivity |

## Precision control di imaging, etching e soldermask

Trace width e spacing sono legati direttamente a signal integrity e impedance control, e nel documento di stackup sono definiti in modo stretto. La sfida di manufacturing è riprodurre quei numeri con accuratezza sulla scheda reale.

### Etch process window: trasformare numeri in realtà

L’etching è un processo sottrattivo: rimuove copper indesiderato e lascia le tracce. Ma l’etchant non attacca solo in verticale: etcha anche lateralmente, creando undercut. Per compensare, applichiamo “etch compensation” ai design data, allargando le tracce nel phototool in anticipo.

<div class="div-style-1">

#### Process window: trace etching

- **Target**: raggiungere ±10% di tolleranza sulla trace width di progetto.
- **Input**: copper thickness definita dallo stackup (es. 1 oz HTE Copper).
- **Key parameters**:
    - **Etch compensation**: 1 oz copper richiede tipicamente 25–35 µm di compensation.
    - **Etch rate**: 1.2–1.8 m/min, controllata da chemistry concentration e temperature.
    - **Undercut control**: spray systems ad alta precisione e etchants dedicati mantengono l’undercut entro 12 µm.
- **Inspection method**: 100% AOI, con cross-section analysis sulle linee critiche per misurare line/space.
- **DFM tip**: quando fai [impedance control design](/blog/what-is-impedance-control-in-pcb/), allineati con il tuo fabbricante sulla capability di etch tolerance e lascia design margin sufficiente.

</div>

### soldermask exposure tutorial: più di una “vernice verde”

La solder mask è lo “strato esterno” della PCB, ma il suo ruolo va ben oltre l’estetica. Definisce le aree saldabili e previene solder bridging durante l’assembly. HILPCB usa LDI (Laser Direct Imaging), che offre maggiore accuratezza rispetto all’esposizione a film tradizionale.

<div class="div-style-3">

#### Soldermask LDI process steps

1.  **Surface pretreatment**: pulizia chimica + spazzolatura meccanica per aumentare la roughness e garantire ink adhesion.
2.  **Ink coating**: in cleanroom, applicare liquid photoimageable soldermask in modo uniforme con screen printing automatizzato o spray. Controllare thickness: 8–15 µm sui pads e 20–30 µm sulle tracce.
3.  **Pre-curing**: bake breve a 75–85°C per tack-dry dell’inchiostro prima dell’LDI exposure.
4.  **LDI exposure**: il laser scansiona la soldermask direttamente (no film); la registration può arrivare a ±15 µm. Critico per formare soldermask dams tra componenti fine-pitch (es. 0.4 mm BGA).
5.  **Developing**: lavaggio in developer; le aree non esposte vengono rimosse e si rivelano i pads.
6.  **Final curing**: bake lungo in tunnel oven a ~150°C per curare completamente la soldermask e ottenere robuste performance fisiche/chimiche.

Questo è un classico **soldermask exposure tutorial**: il core è controllare energy e accuracy perché i soldermask dams non si crepino o si spostino.

## Drilling, plating e PTH quality control

Le vias sono le “vertical highways” delle multilayer boards, e la loro reliability è critica. Il documento di stackup definisce via types (through, blind, buried) e sizes, che impattano direttamente le scelte di drilling e plating.

### Drilling: accuracy e qualità della hole wall

Gli high aspect-ratio holes (board thickness / hole diameter) sono sfidanti sia per drilling sia per plating. Esempio: forare un hole da 0.2 mm in una board da 2.0 mm produce un aspect ratio 10:1.

- **Drilling control**: HILPCB usa high-speed pneumatic spindles (>150k RPM) e X-Ray-assisted registration per garantire inner-layer pad alignment accurato. Per microvias (<0.15 mm) si usa laser drilling.
- **Plasma de-smear**: il calore del drilling può fondere la resina e creare smear che copre l’inner-layer copper, degradando la connessione elettrica. Plasma De-smear rimuove residui di resina dalle hole walls e garantisce copper adhesion affidabile nel plating successivo.

### PTH copper: la base della reliability

Copper thickness e uniformity dentro i holes determinano in gran parte se una PCB sopravvive a thermal shock (es. saldatura) e a long-term operation. Standard come IPC-6012 richiedono tipicamente PTH copper thickness media ≥ 20 µm.

- **Control method**: costruiamo uno strato base conduttivo con Electroless Copper, poi ispessiamo PTH e surface copper con Pattern Plating. Le plating lines HILPCB usano dynamic current control avanzato e high-circulation filtration per depositi densi e uniformi anche in high-aspect-ratio holes.
- **Inspection**: cross-section analysis regolare con metallography microscopes misura la PTH copper thickness e controlla la hole-wall quality per assicurare assenza di voids, cracks o defect correlati.

## SMT soldering e assembly essentials

Dopo la fabbricazione della bare board, il processo passa alla PCBA (Printed Circuit Board Assembly). Pad design, soldermask definition e component placement—tutti definiti nello stackup document—impattano direttamente il successo SMT.

### Stencil design: origine della qualità di solder paste printing

Solder paste printing è il primo step SMT e pesa per oltre il 60% dei soldering defects. Un buon **smt stencil design tutorial** enfatizza che lo stencil design è decisivo.

- **Aperture design**: size/shape delle aperture determina il paste volume. Seguiamo regole di area ratio (>0.66) e aspect ratio (>1.5) per prevenire paste release incompleto. Per parti fini come 0201 e 0.4 mm BGA, si usano stencil elettrolucidati o nano-coated per migliorare il release.
- **Thickness selection**: lo stencil thickness (tipicamente 100–150 µm) si sceglie in base ai componenti a pitch più piccolo sulla board: un esempio classico di accoppiare design intent e process constraints.

### Reflow soldering: l’arte del temperature profiling

Il reflow soldering lega permanentemente i componenti alla PCB. Il core è controllare con precisione il profilo per attivare flux, fondere la solder e formare IMC affidabile.

<div class="div-style-1">

#### Process window: lead-free reflow temperature profile

- **Target**: solder joints brillanti e pieni senza cold joints, opens, tombstoning, ecc.
- **Input**: solder paste datasheet (es. SAC305), PCB laminate/thickness, maximum component thermal mass.
- **Key parameters**:
    - **Preheat**: 150–180°C, 60–90 s, ramp delicato per evitare thermal shock.
    - **Soak**: 180–210°C, 60–120 s, attivare flux e uniformare la temperatura della scheda.
    - **Reflow**: peak 240–250°C; time above liquidus (217°C) 45–75 s.
    - **Cooldown**: cooling rate < 4°C/s per formare struttura a grana fine e garantire joint strength.
- **Inspection method**: HILPCB usa 3D SPI, 3D AOI e X-Ray inspection per monitoraggio 100% della qualità di saldatura.

</div>

## Cleaning, conformal coating e reliability protection

Per applicazioni ad alta reliability (medical, automotive, aerospace), la pulizia post-solder e la protezione sono critiche.

- **Cleaning**: anche con flux “no-clean”, i residui possono causare electrochemical migration (ECM) in ambienti umidi o ad alta tensione e portare a shorts. HILPCB offre aqueous cleaning e usa ion chromatography (IC) per verificare la pulizia, assicurando che l’ionic residue sia sotto limiti di settore (es. IPC J-STD-001 richiede <1.56 µg/cm² NaCl equivalente).
- **Conformal coating**: dopo cleaning e drying, lo spray selettivo di un conformal coating trasparente protegge contro humidity, salt fog e mold, estendendo significativamente la lifetime in harsh environments.

## Testing matrix: assicurare che ogni node sia corretto

DFT va applicato end-to-end. Se un prodotto non è testabile adeguatamente, la qualità non è garantibile. Usiamo una testing matrix a stadi per assicurare coverage.

| Test Stage | Test Method | Primary Goal | Coverage / defect types |
| :--- | :--- | :--- | :--- |
| **After bare-board fab** | Flying Probe Test (FPT) / Bed of Nails | Validare opens/shorts | 100% net connectivity; etch/drill defects |
| **After SMT** | 3D AOI | Ispezionare l’aspetto delle saldature | Wrong/missing parts, polarity, cold joints, bridging, tombstoning |
| **SMT critical parts** | 3D X-Ray | Ispezionare hidden joints (BGA, QFN) | BGA shorts, voids, Head-in-Pillow (HoP) |
| **PCBA circuit level** | ICT | Controllare parametri componenti e nets | Wrong values, opens/shorts, digital logic functions |
| **PCBA functional level** | FCT | Simulare end use e validare functions | Firmware programming, I/O, interfaces, power |
| **System level** | SLT / Burn-in | Validare stabilità e performance in condizioni reali | Compatibility issues, intermittent faults, early failures |
| **Reliability validation** | HALT/HASS, temp-humidity cycling, vibration | Valutare long-term reliability e margin | Weak points, potential failure modes |

Questa **testing matrix** è la spina dorsale della nostra quality assurance: dai solder joints microscopici alla system-level functionality.

## Quality e traceability: la forza dei dati

Nel manufacturing moderno, la quality non è “inspected in”: è “built in” e “managed in”.

- **SPC (Statistical Process Control)**: distribuiamo SPC monitoring points su step chiave come etching, plating e reflow per tracciare process parameters (es. chemistry concentration, oven temperature) in real time. Se i trend deragliano, il sistema allerta subito, così gli engineers intervengono prima che i difetti diventino sistemici.
- **MES (Manufacturing Execution System)**: le linee HILPCB sono gestite da MES. Ogni PCB/PCBA ha un QR code unico come “ID card”. Dai materiali in ingresso (gestiti dal nostro smart warehousing system) allo shipment finale, tutti i process data, equipment parameters, personnel information e test results sono legati a quel QR code. Questo abilita una vera end-to-end traceability: quando emergono issues, l’impatto si localizza in minuti—sia un component lot specifico o un equipment-parameter anomaly in una time window.

<div class="cta-box">
    <p>Un design Stackup perfetto ha bisogno di un partner manufacturing e test altrettanto forte per diventare reale. Il MES di HILPCB e la test capability completa assicurano che il tuo design intent venga eseguito con precisione e forniscono traceability data completamente trasparenti. Vuoi vedere come il tuo prossimo progetto può beneficiarne?</p>
    Carica ora i tuoi Gerber files per ottenere una valutazione DFM/DFT
</div>

## HILPCB’s integrated manufacturing + test capability

Trasformare una `stackup documentation guide` in un electronic product ad alta reliability richiede equipment avanzato, processi rigorosi e competenze specialistiche. HILPCB fornisce più della fabbricazione: offriamo una one-stop solution da design optimization a test validation.

<div class="div-style-6">

#### HILPCB core manufacturing and test capabilities

- **Advanced PCB fabrication**:
    - **Materials**: supporta materiali high-frequency/high-speed come Rogers, Taconic e Isola.
    - **Processes**: 20+ layers, 0.15 mm mechanical microvias, laser blind/buried vias, step copper/step slots, backdrilling, gold fingers e altri build complessi.
    - **Precision control**: LDI exposure, plasma cleaning, X-Ray registration per assicurare yield su build [HDI](/blog/what-is-hdi-pcb/).

- **Smart PCBA assembly**:
    - **Automated lines**: paste printers automatizzati, high-speed placement e 12-zone reflow ovens; supporto al posizionamento 01005.
    - **Closed-loop inspection**: 3D SPI + 3D AOI + 3D X-Ray chiudono il data loop e ottimizzano printing/placement parameters in real time.
    - **Smart storage**: storage intelligente a temperatura/umidità controllate per proteggere componenti, soprattutto MSD parts.

- **Comprehensive test lab**:
    - **In-house test capability**: sviluppo ICT/FCT + flying probe testers, X-Ray ad alta risoluzione, environmental chambers (temperature/humidity), vibration tables, salt-spray chambers, ecc.
    - **Reliability services**: validazione completa della **reliability checklist**, inclusi thermal shock, mechanical shock, vibration tests e HALT/HASS accelerated life testing.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

`stackup documentation guide` è il ponte tra design e manufacturing. Capire come influenza ogni step downstream—da etch compensation e reflow profiles al test-point planning—è una skill necessaria per ogni great engineer. In HILPCB non siamo solo l’esecutore del tuo documento, ma anche il tuo partner DFM/DFT. Con sistemi manufacturing e test process-driven, data-driven e intelligenti, assicuriamo che il tuo design intent venga implementato in modo preciso e affidabile—trasformandosi in prodotti con forte competitività di mercato.

> Need fabrication and assembly support? Contatta HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) o [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) per raccomandazioni DFM/DFT.


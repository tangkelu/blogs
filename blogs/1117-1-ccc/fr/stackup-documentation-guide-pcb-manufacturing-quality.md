---
title: "stackup documentation guide : un playbook process-driven pour le PCB manufacturing et le testing"
description: "En utilisant une stackup documentation guide comme backbone, ce walkthrough end-to-end couvre les détails de manufacturing, les checkpoints de quality control et des conseils DFM/DFT : des matériaux et de l’imaging à la soldermask, au SMT et à la test validation."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["stackup documentation guide", "soldermask exposure tutorial", "smt stencil design tutorial", "pcb fabrication process steps", "yield improvement roadmap", "surface finish selection tips"]
---
Bonjour, je suis instructeur à la HILPCB Manufacturing Academy. Au quotidien, je constate que beaucoup de design engineers considèrent une `stackup documentation guide` comme “juste” un document qui définit la structure de lamination et l’impedance control. Du point de vue manufacturing-and-test, c’est pourtant le “genesis blueprint” et la “execution constitution” de tout le production flow. Elle ne détermine pas seulement la performance électrique : elle influence profondément le yield, la reliability et le cost à chaque étape, des incoming materials jusqu’au functional testing final.

Aujourd’hui, nous allons utiliser ce document core comme fil conducteur pour parcourir l’ensemble du flux de PCB manufacturing et de test. Ce n’est pas seulement un **pcb manufacturing tutorial**, mais aussi une **yield improvement roadmap** qui relie le design intent à la manufacturing reality. Nous décomposerons des processus complexes en étapes type SOP et en checklists afin que votre équipe internalise réellement DFM (Design for Manufacturability) et DFT (Design for Testability).

## Manufacturing flow overview : du document de stackup au produit physique

Une `stackup documentation guide` détaillée est le point de départ de la fabrication. Elle définit les materials, thickness, copper weight et tolerances : des paramètres qui fixent la process window sur la ligne de production. Le tableau ci-dessous montre comment les principales étapes de manufacturing se mappent directement sur les informations du document de stackup.

| Process Step | Core Objective | Key Control Parameters | Related Stackup Info |
| :--- | :--- | :--- | :--- |
| **Laminate preparation** | S’assurer que les materials répondent aux exigences de design | Material type, board thickness, copper thickness, dimensional accuracy | Core et prepreg (PP) types, Dk/Df, Tg, CAF resistance |
| **Inner-layer imaging** | Reproduire précisément les patterns des inner layers | Exposure energy, develop time, registration (±25 µm) | Inner-layer copper thickness (ex. 0.5 oz, 1 oz), minimum line/space |
| **Lamination** | Presser la structure multilayer en un seul panneau | Temperature/pressure/time profile, resin-flow control | Stack order, PP type/quantity, overall thickness tolerance (±10%) |
| **Drilling** | Créer les through holes et les mounting holes | Spindle speed, feed rate, hole-position accuracy (±50 µm) | Hole size, hole type (PTH/NPTH/blind/buried), hole density, minimum annular ring |
| **Plating** | Construire la connexion électrique interlayer | Rectifier current density, bath chemistry, copper thickness (>20 µm) | Aspect ratio, copper thickness requirements |
| **Outer-layer imaging** | Reproduire précisément les patterns des outer layers | Registration, etch-factor control | Outer-layer copper thickness, impedance-trace width, BGA/QFN pad sizes |
| **Soldermask** | Protéger les traces et définir les zones soudables | Ink type/thickness, exposure accuracy, curing conditions | Soldermask color, minimum Solder Mask Dam width |
| **Surface finish** | Assurer solderability et protection | Plating thickness (ex. ENIG: Au 0.03–0.08 µm), flatness | [Surface Finish](/blog/pcb-surface-finish/) (HASL, ENIG, OSP, etc.) |
| **SMT assembly** | Placer et souder les composants | Paste volume, placement accuracy, reflow profile | BOM, packages, pad design |
| **Test & validation** | Garantir fonction électrique et reliability | Coverage, fault-diagnosis accuracy | Test-point layout, net connectivity |

## Precision control : imaging, etching et soldermask

Trace width et spacing sont directement liés à la signal integrity et à l’impedance control, et sont strictement définis dans le document de stackup. Le défi de manufacturing est de reproduire ces chiffres avec précision sur des boards réelles.

### Etch process window : transformer les chiffres en réalité

L’etching est un processus soustractif : il retire le copper indésirable et laisse les traces. Mais l’etchant n’attaque pas seulement vers le bas ; il etche aussi latéralement, créant un undercut. Pour compenser, nous appliquons une “etch compensation” aux design data, en élargissant les traces sur le phototool à l’avance.

<div class="div-style-1">

#### Process window: trace etching

- **Target**: atteindre ±10% de tolérance sur la trace width de design.
- **Input**: copper thickness définie par le stackup (ex. 1 oz HTE Copper).
- **Key parameters**:
    - **Etch compensation**: 1 oz copper nécessite typiquement 25–35 µm de compensation.
    - **Etch rate**: 1.2–1.8 m/min, contrôlée par chemistry concentration et temperature.
    - **Undercut control**: des spray systems haute précision et des etchants dédiés maintiennent l’undercut dans 12 µm.
- **Inspection method**: 100% AOI, avec cross-section analysis sur les lignes critiques pour mesurer line/space.
- **DFM tip**: lors de [impedance control design](/blog/what-is-impedance-control-in-pcb/), alignez-vous avec votre fabricator sur la capability de tolérance d’etch et laissez une design margin suffisante.

</div>

### soldermask exposure tutorial : bien plus que de la “peinture verte”

La solder mask est la “outer layer” de la PCB, mais son rôle va bien au-delà de l’esthétique. Elle définit les zones soudables et empêche le solder bridging pendant l’assembly. HILPCB utilise LDI (Laser Direct Imaging), plus précis que la film exposure traditionnelle.

<div class="div-style-3">

#### Soldermask LDI process steps

1.  **Surface pretreatment** : nettoyage chimique + brossage mécanique pour augmenter la rugosité et assurer l’ink adhesion.
2.  **Ink coating** : en cleanroom, appliquer uniformément la liquid photoimageable soldermask via screen printing automatisé ou spray. Contrôler la thickness à 8–15 µm sur les pads et 20–30 µm sur les traces.
3.  **Pre-curing** : bake court à 75–85°C pour tack-dry l’encre avant LDI exposure.
4.  **LDI exposure** : le laser scanne la soldermask directement (sans film) ; la registration peut atteindre ±15 µm. Critique pour former des soldermask dams entre des parts fine-pitch (ex. 0.4 mm BGA).
5.  **Developing** : lavage dans le developer ; les zones non exposées sont retirées pour révéler les pads.
6.  **Final curing** : bake long en tunnel oven à ~150°C pour curer complètement la soldermask et obtenir de solides performances physiques/chimiques.

C’est un **soldermask exposure tutorial** classique : le cœur est de contrôler energy et accuracy afin que les soldermask dams ne craquent pas et ne se déplacent pas.

## Drilling, plating et PTH quality control

Les vias sont les “vertical highways” des multilayer boards et leur reliability est critique. Le document de stackup définit les via types (through, blind, buried) et les sizes, qui influencent directement les choix de drilling et de plating.

### Drilling : accuracy et qualité de la hole wall

Les high aspect-ratio holes (board thickness / hole diameter) sont difficiles à la fois pour drilling et plating. Exemple : percer un hole de 0.2 mm dans une board de 2.0 mm donne un aspect ratio de 10:1.

- **Drilling control** : HILPCB utilise des high-speed pneumatic spindles (>150k RPM) et une X-Ray-assisted registration pour assurer un inner-layer pad alignment précis. Pour les microvias (<0.15 mm), on utilise le laser drilling.
- **Plasma de-smear** : la chaleur du drilling peut faire fondre la résine et créer du smear qui couvre l’inner-layer copper, dégradant la connexion électrique. Le Plasma De-smear retire les résidus de résine des hole walls et assure une copper adhesion fiable pour le plating.

### PTH copper : la base de la reliability

La copper thickness et l’uniformity dans les holes déterminent largement si une PCB survit au thermal shock (ex. soudure) et au long-term operation. Des standards comme IPC-6012 exigent typiquement une PTH copper thickness moyenne ≥ 20 µm.

- **Control method** : nous construisons une base conductive avec Electroless Copper, puis épaississons PTH et surface copper via Pattern Plating. Les lignes de plating HILPCB utilisent un dynamic current control avancé et une filtration à forte circulation pour des dépôts denses et uniformes, même dans des high-aspect-ratio holes.
- **Inspection** : des cross-section analysis régulières avec metallography microscopes mesurent la PTH copper thickness et vérifient la hole-wall quality pour garantir l’absence de voids, cracks ou défauts associés.

## SMT soldering et assembly essentials

Après la fabrication de la bare board, le processus passe à la PCBA (Printed Circuit Board Assembly). Pad design, soldermask definition et component placement—tous définis dans le stackup document—impactent directement le succès SMT.

### Stencil design : origine de la qualité du solder paste printing

Le solder paste printing est la première étape SMT et représente plus de 60% des soldering defects. Un bon **smt stencil design tutorial** souligne que le stencil design est décisif.

- **Aperture design** : la size/shape des apertures détermine le paste volume. Nous suivons des règles d’area ratio (>0.66) et d’aspect ratio (>1.5) pour éviter un paste release incomplet. Pour des parts fines comme 0201 et 0.4 mm BGA, des stencils électropolishés ou nano-coated améliorent le release.
- **Thickness selection** : la stencil thickness (typiquement 100–150 µm) se choisit selon les composants au pitch le plus fin—un exemple classique de coupler design intent et process constraints.

### Reflow soldering : l’art du temperature profiling

Le reflow soldering lie définitivement les composants à la PCB. Le cœur est un contrôle précis du profil pour activer le flux, fondre la solder et former un IMC fiable.

<div class="div-style-1">

#### Process window: lead-free reflow temperature profile

- **Target**: solder joints brillants et complets sans cold joints, opens, tombstoning, etc.
- **Input**: solder paste datasheet (ex. SAC305), PCB laminate/thickness, maximum component thermal mass.
- **Key parameters**:
    - **Preheat**: 150–180°C, 60–90 s, rampe douce pour éviter le thermal shock.
    - **Soak**: 180–210°C, 60–120 s, activer le flux et homogénéiser la température de la board.
    - **Reflow**: peak 240–250°C ; time above liquidus (217°C) 45–75 s.
    - **Cooldown**: cooling rate < 4°C/s pour une structure à grain fin et une joint strength élevée.
- **Inspection method**: HILPCB utilise 3D SPI, 3D AOI et X-Ray inspection pour un monitoring 100% de la qualité de soldering.

</div>

## Cleaning, conformal coating et reliability protection

Pour des applications high-reliability (medical, automotive, aerospace), la propreté post-solder et la protection sont critiques.

- **Cleaning** : même avec un flux “no-clean”, des résidus peuvent provoquer l’electrochemical migration (ECM) en environnement humide ou high-voltage et conduire à des shorts. HILPCB propose l’aqueous cleaning et utilise l’ion chromatography (IC) pour vérifier la propreté, en garantissant un ionic residue sous les limites (ex. IPC J-STD-001 exige <1.56 µg/cm² NaCl équivalent).
- **Conformal coating** : après cleaning et drying, une pulvérisation sélective d’un conformal coating transparent protège contre humidity, salt fog et mold, et prolonge fortement la lifetime en harsh environments.

## Testing matrix : s’assurer que chaque node est correct

DFT doit être appliqué end-to-end. Si un produit n’est pas testable correctement, la qualité ne peut pas être garantie. Nous utilisons une testing matrix par étapes pour assurer la coverage.

| Test Stage | Test Method | Primary Goal | Coverage / defect types |
| :--- | :--- | :--- | :--- |
| **After bare-board fab** | Flying Probe Test (FPT) / Bed of Nails | Valider opens/shorts | 100% net connectivity; etch/drill defects |
| **After SMT** | 3D AOI | Inspecter l’apparence des soudures | Wrong/missing parts, polarity, cold joints, bridging, tombstoning |
| **SMT critical parts** | 3D X-Ray | Inspecter les hidden joints (BGA, QFN) | BGA shorts, voids, Head-in-Pillow (HoP) |
| **PCBA circuit level** | ICT | Vérifier les paramètres composants et les nets | Wrong values, opens/shorts, digital logic functions |
| **PCBA functional level** | FCT | Simuler l’end use et valider les functions | Firmware programming, I/O, interfaces, power |
| **System level** | SLT / Burn-in | Valider stabilité et performance en conditions réelles | Compatibility issues, intermittent faults, early failures |
| **Reliability validation** | HALT/HASS, temp-humidity cycling, vibration | Évaluer long-term reliability et margin | Weak points, potential failure modes |

Cette **testing matrix** est le backbone de notre quality assurance : des solder joints microscopiques à la system-level functionality.

## Quality et traceability : la puissance des data

Dans le manufacturing moderne, la quality n’est pas “inspected in” ; elle est “built in” et “managed in”.

- **SPC (Statistical Process Control)** : nous déployons des SPC monitoring points sur des étapes clés comme etching, plating et reflow pour suivre les process parameters (ex. chemistry concentration, oven temperature) en temps réel. Si une dérive apparaît, le système alerte immédiatement, afin que les engineers interviennent avant que les défauts deviennent systémiques.
- **MES (Manufacturing Execution System)** : les lignes HILPCB sont gérées par MES. Chaque PCB/PCBA a un QR code unique comme “ID card”. Des incoming materials (gérés par notre smart warehousing system) jusqu’au shipment final, tous les process data, equipment parameters, personnel information et test results sont liés à ce QR code. Cela permet une end-to-end traceability réelle : si des issues sont détectées, l’impact est localisé en minutes—qu’il s’agisse d’un component lot précis ou d’une anomalie d’équipement sur une time window.

<div class="cta-box">
    <p>Un Stackup design parfait a besoin d’un partenaire manufacturing et test tout aussi solide pour devenir réel. Le MES de HILPCB et notre test capability complète assurent l’exécution précise de votre design intent et fournissent des traceability data totalement transparents. Envie de voir comment votre prochain projet peut en bénéficier ?</p>
    Upload vos Gerber files maintenant pour obtenir une évaluation DFM/DFT
</div>

## HILPCB’s integrated manufacturing + test capability

Transformer une `stackup documentation guide` en un electronic product high-reliability exige des équipements avancés, des processus stricts et une expertise spécialisée. HILPCB fournit plus que la fabrication : nous délivrons une one-stop solution de design optimization à test validation.

<div class="div-style-6">

#### HILPCB core manufacturing and test capabilities

- **Advanced PCB fabrication**:
    - **Materials**: supporte des matériaux high-frequency/high-speed comme Rogers, Taconic et Isola.
    - **Processes**: 20+ layers, 0.15 mm mechanical microvias, laser blind/buried vias, step copper/step slots, backdrilling, gold fingers et autres builds complexes.
    - **Precision control**: LDI exposure, plasma cleaning, X-Ray registration pour assurer le yield des builds [HDI](/blog/what-is-hdi-pcb/).

- **Smart PCBA assembly**:
    - **Automated lines**: paste printers automatisés, high-speed placement et 12-zone reflow ovens ; support du placement 01005.
    - **Closed-loop inspection**: 3D SPI + 3D AOI + 3D X-Ray ferment la boucle data et optimisent les printing/placement parameters en temps réel.
    - **Smart storage**: storage intelligent contrôlé en température/humidity pour protéger les composants, notamment les MSD parts.

- **Comprehensive test lab**:
    - **In-house test capability**: développement ICT/FCT + flying probe testers, X-Ray haute résolution, environmental chambers (temperature/humidity), vibration tables, salt-spray chambers, etc.
    - **Reliability services**: validation complète de la **reliability checklist**, incluant thermal shock, mechanical shock, vibration tests et HALT/HASS accelerated life testing.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

`stackup documentation guide` est le pont entre design et manufacturing. Comprendre comment elle influence chaque étape downstream—de l’etch compensation et des reflow profiles au test-point planning—est une compétence requise pour tout great engineer. Chez HILPCB, nous ne sommes pas seulement l’exécutant de votre document : nous sommes aussi votre partenaire DFM/DFT. Avec des systèmes manufacturing et test process-driven, data-driven et intelligents, nous garantissons une exécution précise et fiable de votre design intent—pour finalement devenir des produits à forte compétitivité marché.

> Need fabrication and assembly support? Contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.


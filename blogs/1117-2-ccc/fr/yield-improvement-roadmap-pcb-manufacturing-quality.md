---
title: "yield improvement roadmap : un guide opérationnel structuré pour la fabrication PCB et le test"
description: "Un yield improvement roadmap pratique, des matériaux et de l’imaging/etching jusqu’au solder mask, SMT et test/validation – avec détails process, points de contrôle qualité et conseils DFM/DFT de bout en bout."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["yield improvement roadmap", "surface finish selection tips", "pcb fabrication process steps", "smt stencil design tutorial", "soldermask exposure tutorial", "x ray inspection checklist"]
---
Bonjour à tous, je suis formateur à la HILPCB Manufacturing Academy. Dans les échanges quotidiens avec les équipes design et process, un pain point revient : comment augmenter le Yield de façon systématique ? Beaucoup d’équipes traitent les symptômes sans vision globale. Aujourd’hui, nous introduisons un concept central – **Yield Improvement Roadmap** – et l’utilisons pour découper le flux complet, de la fabrication bare board jusqu’aux tests PCBA, en SOP et checklists. L’objectif est un système qualité prédictible et contrôlable, du design à l’EOL.

Un `yield improvement roadmap` efficace ne se limite pas à corriger un défaut d’une seule étape : il intègre DFM/DFT, matériaux, process, équipements, tests et data analysis dans une boucle d’amélioration continue. Commençons par une vue d’ensemble.

## Vue d’ensemble du flux : construire votre yield improvement roadmap

Pour améliorer le yield, il faut comprendre l’objectif, les paramètres clés et l’impact de chaque étape. Nous séparons le flux en PCB Fabrication (bare board) et PCBA Assembly. Le tableau ci‑dessous est le cadre de base de votre `yield improvement roadmap`.

| Process Stage | Core Objective | Key Control Parameters | Direct Impact on Yield |
| :--- | :--- | :--- | :--- |
| **PCB Fabrication** | | | |
| Inner Layer Imaging | Répliquer le motif avec précision ; assurer l’impédance | Énergie d’exposition, précision d’alignement, temps/température de développement | Opens/shorts, mismatch d’impédance |
| Lamination | Assembler cores et prepregs en un stack | Ramp rate, pression, niveau de vide, temps de cure | Delamination, warpage, épaisseur diélectrique non uniforme |
| Drilling | Créer vias et trous composants | Vitesse/avance, durée de vie forets, précision position | Parois rugueuses, nail heads, décalage, no copper |
| PTH & Plating | Métallisation fiable des parois | Efficacité desmear, activité electroless copper, densité de courant | PTH voids, cuivre via insuffisant, mauvaise adhérence |
| Outer Layer & Etching | Former les pistes externes ; contrôler width/spacing | Etch rate, concentration, température, undercut | Opens/shorts, largeur hors tolérance, impédance en échec |
| Solder Mask | Protéger ; éviter le bridging | Viscosité ink, énergie d’exposition, alignement, cure | Mask dams/bridges, pelage, copper exposé |
| Surface Finish | Protéger le cuivre ; assurer solderability | Épaisseur (ex. ENIG Au), planéité, temps process | Mauvaise soudabilité, black pad, faible joint strength |
| **PCBA Assembly** | | | |
| Solder Paste Printing | Déposer la pâte avec précision ; volume correct | Stencil épaisseur/ouvertures, pression/vitesse racle, alignement | Manque/excès, bridging, spikes → défauts soudure |
| Component Placement | Placement précis des composants | Coordonnées, pression nozzle, précision vision | Missing, offset, polarité, tombstoning |
| Reflow Soldering | Former des joints fiables | Thermal profile, peak temp | Cold joints, opens, solder balls, BGA voids |
| Cleaning | Retirer résidus flux ; fiabilité électrique | Nettoyant, température, pression, temps | Résidus ioniques, ECM, problèmes de coating |
| Testing | Vérifier fonction et fiabilité | Coverage, contact probes, programme test | False Pass, False Fail |

---

## Imaging, etching et solder mask : la bataille au micron

Les pistes et le solder mask sont le « squelette » et la « peau » d’un PCB. Leur précision conditionne performances électriques et qualité de soudure.

### Fenêtre process : imaging transfer et etching

Imaging (exposure/develop) et etching fixent la précision des pistes. Le but est de copier les Gerber sur le cuivre sans perte, à grande échelle.

<div class="div-style-1">

#### Fenêtre process : trace etching

- **Objectif** : linewidth uniforme et undercut contrôlé pour une impédance cohérente.
- **Paramètres clés** :
    - **Concentration & température de l’etchant** : déterminent l’etch rate ; les variations dérivent la linewidth.
    - **Vitesse de convoyage** : fixe le temps d’exposition à la chimie.
    - **Pression de spray** : garantit une chimie fraîche et uniforme, critique sur fine lines.
- **Standard de contrôle** :
    - **Tolérance de largeur** : pour 50Ω, typiquement ±10%.
    - **Etch Factor** : mesure du side‑etch ; idéal > 3.
    - **Standard HILPCB** : ligne d’etching automatisée avec **tolérance stable à ±12µm**, via monitoring chimie et scan laser de linewidth pour la cohérence inter‑lots.

</div>

### Soldermask exposure tutorial (Soldermask Exposure Tutorial)

Le solder mask n’est pas une simple « peinture verte » : c’est un contrôleur de process. La précision des Solder Mask Dams est critique pour éviter le bridging sur QFP/BGA.

<div class="div-style-3">

#### Méthode solder mask en trois étapes

1.  **Coating** : sérigraphie automatique ou spray pour une épaisseur uniforme (8–15µm sur pad). Une épaisseur irrégulière crée du sous‑cure ou de la dérive d’exposition.
2.  **Pre-curing** : évaporer le solvant pour une surface « tack‑free ». Trop long/trop chaud complique le développement.
3.  **Exposure & Development** :
    *   **Alignement** : CCD auto alignment ; précision ±25µm.
    *   **Énergie d’exposition** : 250–400 mJ/cm² selon ink/épaisseur. Trop faible → adhérence faible ; trop forte → dams fins non développés.
    *   **Développement** : retirer l’ink non exposée et former le motif final.

**Conseil DFM** : agrandir l’ouverture solder mask de 2–3 mil par côté par rapport au pad. En zone BGA, NSMD améliore la fiabilité mais exige un alignement mask plus strict.

## Drilling et plating : bâtir des interconnexions verticales fiables

Les vias sont l’« autoroute verticale » des multilayers. La qualité de paroi et l’épaisseur cuivre via sont clés pour la fiabilité long terme.

### Contrôle qualité drilling

Le drilling mécanique est délicat, surtout en high aspect ratio (Aspect Ratio > 10:1).
- **Gestion des forets** : suivre la durée de vie ; un foret usé rugueux crée nail heads et dégrade le plating.
- **Desmear** : le resin smear peut isoler le cuivre interne ; l’éliminer par chimie ou plasma pour éviter les opens internes.

### Importance de l’épaisseur cuivre via

Le cuivre via est le chemin vertical. IPC‑6012 fixe des exigences (Class 2 average ≥ 20µm).
- **Défi** : courant plus faible au centre du trou → cuivre plus mince.
- **Approche HILPCB** : VCP + additifs high‑throw et pulse reverse current pour une épaisseur uniforme même sur deep holes.

### Surface finish selection tips (Surface Finish Selection Tips)

Le surface finish est la dernière étape de fabrication et impacte directement soudure et coût.
- **OSP** : low cost, flatness excellente ; shelf life courte, faible multi‑reflow.
- **HASL** : économique et soudable, mais flatness faible ; pas idéal fine pitch.
- **ENIG** : bonne flatness/solderability et stockage ; attention au black pad.
- **ImAg/ImSn** : entre OSP et ENIG ; bonne flatness mais risques oxydation/tin whisker.

**Conseil de choix** : considérer application, composants, budget et stockage. Pour high‑speed/high‑frequency ou BGA, recommander **ENIG**. Voir notre [internal link: surface finish selection guide].

## SMT : de la pâte à la soudure, la précision d’abord

En PCBA, le `yield improvement roadmap` se focalise sur la prévention des défauts de soudure. Plus de 60% des défauts proviennent du solder paste printing.

### SMT stencil design tutorial (SMT Stencil Design Tutorial)

Le stencil est le « moule » de la pâte : son design fixe volume et forme.
- **Épaisseur** : selon le composant le plus fin ; souvent 4–5 mil (0.10–0.12 mm).
- **Aperture design** :
    - **Aspect Ratio** : `aperture width / stencil thickness > 1.5`.
    - **Area Ratio** : `aperture area / aperture wall area > 0.66`.
    - **Anti‑solder‑ball** : pour chip, apertures en « U »/concaves réduisent les solder balls.
    - **BGA apertures** : souvent 10% plus petites que le pad.
- **Procédé stencil** : laser cutting + electropolishing pour des parois lisses et une meilleure release.

### Reflow et inspection X‑Ray

Le thermal profile du reflow dicte la qualité du joint (pré‑chauffe, soak, reflow, cooling).
- **Paramètres clés** : peak temp (lead‑free **245°C ±5°C**) et TAL (45–90 s).
- **Prévention** : profil inadéquat → cold joints, opens, tombstoning, BGA voids.
- **X-ray Inspection Checklist** : pour BGA/QFN, X‑ray est souvent l’unique NDT.
    1.  **Shorts** : ponts entre balls.
    2.  **Opens** : séparation ball‑pad.
    3.  **Voids** : bulles ; IPC‑A‑610 limite typiquement une void unique à ≤ 25% de la surface du ball.
    4.  **Alignement/taille** : offset et uniformité.
    5.  **PTH fill (for PiP)** : taux de remplissage Pin‑in‑Paste.

HILPCB dispose de 3D X‑Ray haute résolution, calcule automatiquement le void ratio et génère des rapports pour optimiser le process.

## Cleaning, conformal coating et fiabilité

Une PCBA fonctionnelle n’est pas forcément fiable. Résidus et environnement sont des facteurs majeurs.
- **Cleaning** : les résidus flux (ions actifs) favorisent l’ECM en humidité et des dendrites menant à des shorts. Standard : DI water cleaning et validation IC/OM, avec **ionic residue < 1.56µg/cm² (NaCl équivalent)**.
- **Conformal coating** : film isolant contre humidité/salt fog/moisissures. Selective coating automatisé pour éviter connecteurs et maîtriser l’épaisseur.

## Test matrix : des barrières multiples pour éviter les escapes

Le testing est la dernière ligne de défense d’un `yield improvement roadmap`, et la source de données pour le closed loop. Un seul test ne suffit pas : construire une matrice combinée.

| Test Type | Objective | Coverage | Applicable Stage | Pros & Cons |
| :--- | :--- | :--- | :--- | :--- |
| **AOI** | Défauts visibles | Missing/wrong, offset, polarité, solder balls, partiellement cold joints | Après reflow | **Pros**: Rapide, low cost, volume. <br>**Cons**: Ne voit pas BGA/defauts internes connecteurs. |
| **SPI** | Qualité impression pâte | Volume/area/height/offset/bridging | Après impression | **Pros**: Détecte avant formation du joint. <br>**Cons**: Ciblé printing. |
| **FPT** | Opens/shorts bare board | 100% net opens/shorts | Après fabrication | **Pros**: Sans fixture ; low volume/high mix. <br>**Cons**: Lent, coûteux. |
| **ICT** | Défauts composants | Opens/shorts, valeurs R/L/C, diode/transistor | Après assembly | **Pros**: Rapide, localisation précise. <br>**Cons**: Fixture cher ; dépend des test points (DFT). |
| **FCT** | Simuler usage réel | KPI, interfaces, power management | Après assembly ou système | **Pros**: Proche terrain ; couverture élevée. <br>**Cons**: Dév. long ; localisation composant limitée. |
| **X-Ray** | Joints invisibles | BGA/QFN shorts/voids/opens | Après reflow | **Pros**: Méthode clé BGA. <br**Cons**: Lent, coûteux ; sampling ou 100% sur composants critiques. |

**Conseil DFT** : réserver des test points suffisants et assurer pitch/position pour contact probes. Une bonne DFT peut augmenter la couverture ICT de ~70% à 95%+.

## Qualité et traçabilité : amélioration continue pilotée par la donnée

Sans boucle data, pas de `yield improvement roadmap`.
- **SPC** : déployer SPC sur SPI, AOI, ICT. Suivre CpK et déclencher des alertes en cas de dérive.
- **MES** : le cerveau de l’usine : chaque PCB/PCBA a un barcode unique reliant lots matériaux, machines, opérateurs, paramètres process et données test. En cas de plainte client : scoper l’impact, RCA, et boucle 8D.

<div class="div-style-6">

#### HILPCB : votre partenaire one‑stop fabrication & test

Construire et exécuter un `yield improvement roadmap` exige expertise process, équipements et systèmes data. HILPCB fournit :

- **Capacités avancées** : LDI automatisé, VCP plating, 3D SPI/AOI et 3D X‑Ray.
- **Traçabilité intégrée** : MES de bout en bout.
- **Support DFM/DFT** : rapports avant production pour éviter les pièges yield.
- **Laboratoire fiabilité** : thermal shock, cycling, vibration, salt spray.

Nous ne sommes pas seulement un fabricant, mais un partenaire stratégique pour la qualité et le yield.

**Prêt à lancer votre démarche yield improvement ? [Uploadez votre Gerber](/) pour une analyse DFM gratuite et construisons l’excellence ensemble.**

</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Cet article utilise un `yield improvement roadmap` pour structurer les détails de fabrication, checkpoints QC et conseils DFM/DFT des matériaux à l’imaging/solder mask, jusqu’au SMT et au test/validation. En appliquant les checklists et fenêtres process, et en impliquant tôt les équipes DFM/DFA HILPCB, vous accélérez prototype et volume tout en sécurisant qualité et conformité.

> Pour du support fabrication/assembly, contactez HILPCB via [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.


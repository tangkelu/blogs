---
title: "Explication des exigences CTI : Document stratégique sur les matériaux et l'empilage"
description: "Fourniture d'un arbre décisionnel complet de sélection des matériaux, de modèles d'empilage, de méthodes de modélisation de l'impédance/thermique et de processus de vérification de la fabrication avec listes de contrôle DFM/DFT/DFR."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 9
tags: ["cti requirement explanation", "thermal reliability stackup", "hdi stackup tutorial", "surface finish comparison", "hdmi pcb stackup guide"]
---

## 1. Résumé : scénarios, défis et bénéfices

**Scénario :** Dans la conception des produits électroniques modernes — des centres de données à très haut débit aux unités de gestion d’alimentation des véhicules à énergie nouvelle — le PCB n’est plus seulement un support de composants. Il devient la base physique des performances système et de la sécurité électrique sur tout le cycle de vie.

**Défi :** Le cœur du problème réside dans la stratégie de matériaux et d’empilage (Stackup). Un mauvais choix peut provoquer atténuation, désadaptation d’impédance, voire un claquage électrique catastrophique en environnement sévère (haute tension, forte humidité). Parmi les indicateurs de sécurité, **CTI (Comparative Tracking Index, indice comparatif de résistance au cheminement)** prend une importance croissante, mais est souvent négligé en phase amont. Une `cti requirement explanation` complète n’est pas seulement une question de conformité : elle impacte directement la fiabilité à long terme.

**Bénéfices :** Ce livre blanc fournit une solution systématique. En tant que guide officiel du laboratoire matériaux HILPCB, il propose une stratégie complète de la sélection des matériaux à la validation de fabrication. Grâce à des arbres décisionnels standardisés, une bibliothèque de templates de stackup, des méthodes de modélisation et des check‑lists DFM/DFR, il aide votre équipe à :

- **Réduire les risques de conception :** décisions matériaux data‑driven basées sur des exigences CTI explicites.
- **Accélérer le cycle de développement :** démarrer plus vite grâce à des templates d’empilage pré‑validés.
- **Augmenter la fiabilité :** garantir `thermal reliability stackup` et sécurité électrique via modélisation et validation.
- **Optimiser les coûts :** équilibrer performances et coût, éviter la sur‑conception et les retours coûteux.

---

## 2. Arbre décisionnel matériaux : une démarche systématique

Choisir le bon matériau PCB est la première étape et la plus critique du design d’empilage. CTI est le point de départ pour la sécurité, mais doit être co‑optimisé avec d’autres métriques (Dk, Tg, CTE, etc.).

<div class="div-type-1">

### CTI Requirement Explanation : l’indicateur central de sécurité

Le CTI mesure la capacité d’un matériau isolant à résister à la formation de traces conductrices de fuite sur la surface sous champ électrique et contamination électrolytique. La classe est définie par PLC (Performance Level Category) : plus le CTI est élevé, plus la résistance au cheminement est forte.

- **PLC 0 :** CTI ≥ 600V (niveau maximal ; industrie/énergie/automobile HV)
- **PLC 1 :** 400V ≤ CTI < 600V
- **PLC 2 :** 250V ≤ CTI < 400V
- **PLC 3 :** 175V ≤ CTI < 250V (les FR‑4 standards se situent généralement ici)

Pour un produit haute tension ou avec exigences de sécurité strictes, il faut figer la classe CTI attendue dès le début et sélectionner les matériaux correspondants.

</div>

### Arbre de décision de sélection matériaux

| Indicateur clé (Key Metric) | Matériaux/niveaux recommandés | Scénarios typiques | Contraintes/points d’attention |
| :--- | :--- | :--- | :--- |
| **CTI ≥ 600V (PLC 0)** | FR‑4 haut CTI (ex. S1170G), résines phénoliques, certains polyimides (PI) | Alimentations industrielles, onduleurs, EV BMS/OBC, médical | Coût plus élevé ; moins d’options — confirmer le stock HILPCB en amont. |
| **Faible Dk/Df (Low Dk/Df)** | Rogers (RO4350B, Dk≈3.48), Megtron 6 (Dk≈3.6), Isola FR408HR | RF 5G/6G, serveurs ≥25Gbps, `hdmi pcb stackup guide` | Exigences process élevées (ex. plasma après perçage) ; coût nettement supérieur au FR‑4 standard. |
| **Tg élevé (High Tg > 170°C)** | S1000-2M, IT-180A, TU-768 | Automobile, modules haute densité de puissance, multicouches cuivre épais | Matériau plus cassant ; paramètres de perçage à optimiser ; température de pressage plus élevée (≈190–210°C). |
| **Z‑CTE faible (Low Z‑CTE)** | FR‑4 faible CTE, Polyimide | HDI, BGA/LGA denses, cartes épaisses (>3.0mm) | Améliore fortement la fiabilité des PTH, réduit les fissures de vias en thermo‑cyclage. |
| **Haute conductivité thermique** | MCPCB (Al, 1–3 W/m·K), céramique (AlN, >150 W/m·K) | LED, modules MOSFET, drivers IGBT | Souvent 1–2 couches ; routage limité ; nécessite un design `thermal reliability stackup` dédié. |
| **Flexibilité / pliage** | Polyimide (PI) | Wearables, rigid‑flex, flex dynamique | Contrôle d’impédance plus complexe ; design des renforts (stiffener) important. |

---

## 3. Bibliothèque de templates stackup : point de départ de la standardisation

Sur la base de milliers de projets en production, le laboratoire HILPCB a consolidé des templates d’empilage standard. Ces modèles ont été validés par simulation et mesure et constituent une base fiable.

### Templates multicouches standard

| Nombre de couches | Structure (exemple) | Description | Applications clés |
| :--- | :--- | :--- | :--- |
| **4 couches** | SIG/GND/PWR/SIG | `Core(0.76mm) + PP + Core(0.76mm)` | Produits grand public, IoT. Coût efficace, mais EMI à soigner. |
| **6 couches** | SIG/GND/SIG/SIG/PWR/SIG | `Core + PP + Core + PP + Core` | Bon compromis coût/performance ; bonne isolation signal/alimentation. |
| **8 couches** | SIG/GND/SIG/PWR/GND/SIG/PWR/SIG | `Core + PP + PP + Core + PP + PP + Core` | Haute vitesse (PCIe, USB 3.0). Plusieurs plans de référence, contrôle 50Ω/100Ω facilité. |
| **10 couches** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | `Core + PP...` | Systèmes complexes, cartes serveurs. Blindage EMI maximal et PI robuste. |

### Templates de structures spéciales

<div class="div-type-3">

#### HDI (High‑Density Interconnect) 叠层教程

Exemple d’un empilage **1+N+1 (N=6) HDI**, structure typique `hdi stackup tutorial` :

- **L1 (SIG) :** Microvia (L1‑L2)
- **L2 (GND) :**
- **L3 (SIG) :** Buried Via (L3‑L6)
- **L4 (PWR) :**
- **L5 (GND) :**
- **L6 (SIG) :**
- **L7 (GND) :**
- **L8 (SIG) :** Microvia (L8‑L7)

**Procédé clé :** laminations séquentielles. On fabrique d’abord le noyau interne L2‑L7, on réalise les vias enterrés, puis on lamine L1 et L8, et enfin on perce les microvias au laser. Cette structure augmente fortement la densité de routage.

</div>

#### Rigid‑Flex et MCPCB

- **Rigid‑Flex :** structure `zone rigide (FR‑4) – zone flexible (PI) – zone rigide (FR‑4)`. La zone de transition est critique : il faut une transition d’efforts progressive pour éviter la rupture du cuivre.
- **MCPCB (substrat aluminium) :** structure `couche circuit (Cu) – couche isolante (haut k) – base métallique (Al)`. La conductivité thermique et la tenue diélectrique de l’isolant sont essentielles pour `thermal reliability stackup`.

---

## 4. Modélisation : impédance / thermique / mécanique

Une modélisation précise est la garantie que l’intention de design est réalisable en production. L’équipe HILPCB s’appuie sur des modèles de premier principe.

### Modélisation d’impédance (Impedance Modeling)

Pour les signaux haute vitesse (HDMI, DDR), le contrôle d’impédance est critique : la tolérance est généralement **±10%**, voire **±5%**.

- **Microstrip (couche externe) :**
$$ Z_0 \approx \frac{87}{\sqrt{\epsilon_r + 1.41}} \ln\left(\frac{5.98H}{0.8W + T}\right) $$
- **Stripline (couche interne) :**
$$ Z_0 \approx \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{4B}{0.67\pi(0.8W + T)}\right) $$

*Où :*

- $Z_0$ : impédance caractéristique (Ω)
- $\epsilon_r$ : constante diélectrique (Dk)
- $H$ : épaisseur diélectrique
- $W$ : largeur de piste
- $T$ : épaisseur cuivre
- $B$ : distance entre plans de référence

**Exemple :** Dans un `hdmi pcb stackup guide`, pour atteindre 100Ω différentiel avec FR‑4 Dk=4.2, diélectrique 0.1mm et cuivre 1oz (0.035mm), la simulation donne une largeur de piste d’environ 0.12mm.

### Modélisation thermique (Thermal Modeling)

Le cœur de l’analyse de fiabilité thermique est le calcul de la chaîne de résistances thermiques.

- **Résistance thermique stationnaire 1D (Rth) :**
$$ R_{th} = \frac{L}{k \cdot A} $$

*Où :*

- $R_{th}$ : résistance thermique (°C/W)
- $L$ : longueur du chemin thermique (m)
- $k$ : conductivité thermique (W/m·K)
- $A$ : section de transfert de chaleur (m²)

En cumulant les résistances du junction du composant vers la surface PCB puis vers le radiateur, on peut prédire la température de fonctionnement — base de `thermal reliability stackup`.

### Modélisation mécanique

L’attention se porte sur les contraintes liées au mismatch de Z‑CTE. En thermo‑cyclage (−40°C à 125°C), si le Z‑CTE est trop élevé (>50 ppm/°C), le cuivre des PTH subit de fortes contraintes de traction, pouvant générer micro‑fissures ou ruptures. Choisir un matériau avec Z‑CTE < 50 ppm/°C est un levier clé de fiabilité.

---

## 5. Hybrid stack / back‑drilling / structures avancées

Pour équilibrer coût et performance, HILPCB supporte des procédés avancés.

<div class="div-type-6">

### Empilage hybride (Hybrid Stack)

**Rogers + FR‑4 :** solution `hybrid stack` la plus courante.

- **Structure :** Rogers (ex. RO4350B) uniquement pour les couches RF externes ; couches internes numériques/alimentation en FR‑4 high‑Tg moins coûteux.
- **Défis :** paramètres de pressage (température/pression) et CTE différents ; programme de lamination dédié. Adhérence plus faible FR‑4↔Rogers ; un traitement plasma (Plasma Treatment) est souvent nécessaire après perçage.
- **Bénéfice :** économie de 30–50% de coût matière tout en conservant les performances RF.

</div>

### Back‑drilling

- **Objectif :** supprimer les stubs de vias pour réduire réflexions et pertes, particulièrement efficace au‑delà de 10Gbps.
- **Procédé :** après lamination et métallisation, perçage depuis l’autre face avec un foret de plus grand diamètre pour retirer la partie inutile ; exigence élevée de contrôle de profondeur.
- **Applications :** backplanes serveurs, commutateurs haute vitesse, modules optiques.

### Comparatif surface finish (Surface Finish Comparison)

Le traitement de surface influence directement la fiabilité de soudure et l’intégrité du signal.

| Traitement de surface | Avantages | Inconvénients | Applications recommandées |
| :--- | :--- | :--- | :--- |
| **HASL** | faible coût, bonne soudabilité | planéité médiocre, pas idéal pour pas fins | produits grand public, exigences de planéité faibles |
| **ENIG** | surface plane, résistance corrosion, adapté BGA | plus cher ; risque de « black pad » | cartes high‑speed, BGA/CSP, zones de contact |
| **OSP** | faible coût, très plane, écologique | stockage plus limité ; se dégrade après reflow multiples | grand public, rotation rapide, faible coût |
| **Immersion Silver** | bonne planéité, très bonnes propriétés électriques | oxydation ; stockage/handling stricts | RF, télécom |

---

## 6. Validation : des matériaux entrants à la fiabilité finale

Une `stackup strategy` robuste doit s’appuyer sur une validation en boucle fermée.

1. **Contrôle réception (IQC) :** vérifier CTI/Dk/Tg via datasheets et rapports ; tests par échantillonnage pour matériaux critiques.
2. **Suivi de lamination :** monitorer les profils température/pression selon la spécification ; FR‑4 standard ≈ **180°C**.
3. **Coupon test d’impédance :** coupons dédiés par lot ; mesure TDR de 50Ω/100Ω et autres ; confirmer une variation dans **±10%** (cœur de `coupon test`).
4. **Warpage :** mesures optiques (Shadow Moiré) avant/après reflow, cible < 0.75%.
5. **Essais fiabilité :**
    - **Thermal Shock :** par ex. 1000 cycles −40°C ↔ 125°C, puis micro‑sections pour PTH/microvias.
    - **IST :** chauffage rapide et charge de courant sur coupon pour accélérer les contraintes thermomécaniques et évaluer la fiabilité des vias.

---

## 7. Check‑list DFM/DFR/DFT

Cette check‑list (≥35 points) vise à aider les ingénieurs à éviter les problèmes courants de fabrication, fiabilité et testabilité dès la conception.

| Catégorie | Règle / point de contrôle | Paramètres recommandés / explications | Méthode de vérification |
| :--- | :--- | :--- | :--- |
| **Matériaux & stackup** | Le niveau CTI répond‑il aux exigences sécurité ? | choisir PLC 0–3 selon la tension | revue design |
|  | Dk/Df/Tg/CTE sont‑ils clairement spécifiés ? | indiquer le matériau dans le stackup | revue design |
|  | Stackup symétrique ? | symétrie cuivre/diélectrique pour limiter le warpage | analyse CAM |
|  | Combinaison Core/PP appropriée ? | éviter un PP unique très épais | analyse CAM |
| **Perçage** | diamètre mini perçage mécanique | ≥ 0.20mm | contrôle DFM |
|  | diamètre mini perçage laser (HDI) | ≥ 0.10mm | contrôle DFM |
|  | Aspect Ratio | < 10:1 (reco.), < 12:1 (limite) | contrôle DFM |
|  | Hole‑to‑Copper (piste/plan) | ≥ 0.20mm | DRC |
|  | NPTH‑to‑Copper | ≥ 0.25mm | DRC |
| **Routage** | largeur/espacement mini | 3.5/3.5mil (inner), 4/4mil (outer) | contrôle DFM |
|  | éviter angles vifs/droits | 45° ou arcs | DRC |
|  | fanout zone BGA | Dog‑bone ou Via‑in‑Pad en priorité | revue layout |
|  | appairage de longueur diff | erreur < 5mil (selon débit) | outil layout |
| **Plans cuivre** | via sous pads BGA/QFN ? | Via‑in‑Pad recommandé (bouchage résine) | contrôle DFM |
|  | thermal relief | largeur de liaison ≥ 50% du pad | contrôle DFM |
|  | distance grand plan ↔ pad | ≥ 0.25mm | DRC |
|  | suppression des copper islands | enlever les îlots non connectés | analyse CAM |
|  | densité stitching vias | bord carte et près des HS, pas < λ/20 | revue layout |
| **Solder mask** | largeur solder mask dam | ≥ 0.10mm (4mil) | contrôle DFM |
|  | ouverture mask | +0.05mm (2mil) par côté | contrôle DFM |
|  | tenting/plugging vias | selon besoin test ; par défaut tent | spec design |
| **Silkscreen** | largeur trait sérigraphie | ≥ 0.15mm (6mil) | contrôle DFM |
|  | écart sérigraphie ↔ pad | ≥ 0.15mm (6mil) | contrôle DFM |
|  | repères/polarité lisibles | assurer la lisibilité | revue layout |
| **DFR** | creepage/clearance HV | suivre IEC‑62368‑1, etc. | revue design |
|  | métal nu près du bord | distance au bord ≥ 0.4mm | contrôle DFM |
|  | chanfrein gold finger | 30° ou 45° | spec design |
|  | stamp holes / V‑cut | séparation facile sans dommage | contrôle DFM |
| **DFT** | taille/pas des points de test | Ø ≥ 0.8mm, pas ≥ 1.27mm | contrôle DFM |
|  | fiducials | ≥3 par carte, en diagonale | contrôle DFM |
|  | points ICT sous composants | éviter | revue layout |
|  | interface JTAG/SWD sortie | faciliter debug | revue design |
| **Autres** | tolérance d’épaisseur carte | ±10% | spec design |
|  | tolérance d’impédance | ±10% (standard), ±5% (strict) | spec design |
|  | cuivre final | répondre aux besoins de courant | simu densité courant |

---

## 8. Boucle de service HILPCB : partenaire de la théorie à la série

Ce livre blanc synthétise l’expérience accumulée par HILPCB sur de nombreux projets. Nos services forment une boucle fermée :

- **Stock matériaux & support laboratoire :** large portefeuille du FR‑4 standard à Rogers/Megtron, et validation rapide CTI/Dk.
- **Simulation & design stackup :** outils de référence pour impédance, thermique et SI afin d’optimiser tôt.
- **Capacités process avancées :** `hybrid stack`, back‑drilling haute précision, HDI, rigid‑flex avec expérience série.
- **Feedback production :** collecte continue des données de production et de `coupon test` pour améliorer règles DFM et templates.

<div class="div-type-1">

**Appel à l’action (CTA)**

Votre prochain projet mérite une base plus fiable et optimisée. Contactez le laboratoire matériaux HILPCB et **obtenez une revue gratuite de votre design d’empilage**. Nos experts fourniront des recommandations personnalisées sur les matériaux et le stackup selon votre `cti requirement explanation` et vos objectifs de performance.

**[Contacter un expert technique et lancer l’optimisation du projet](#contact)**

</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

En résumé, cet article autour de `cti requirement explanation` fournit un arbre décisionnel matériaux, une bibliothèque de templates stackup, des méthodes de modélisation impédance/thermique/mécanique et un processus de validation fabrication, complétés par une check‑list DFM/DFT/DFR. En appliquant les check‑lists et fenêtres process décrites, et en impliquant tôt l’équipe DFM/DFA de HILPCB, vous pouvez accélérer prototypage et montée en série tout en garantissant qualité et conformité.

> Pour le support de fabrication et d’assemblage, contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.

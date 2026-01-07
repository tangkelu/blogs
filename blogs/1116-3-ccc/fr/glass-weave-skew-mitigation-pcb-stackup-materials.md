---
title: "Glass weave skew mitigation : whitepaper matériaux et stackup strategy"
description: "Framework complet pour glass weave skew mitigation : decision tree matériaux, templates de stackup, modélisation impedance/thermal et validation fabrication—avec checklist DFM/DFT/DFR pour standardiser le stack design."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 9
tags: ["glass weave skew mitigation", "flex rigid material stackup", "surface finish comparison", "thermal reliability stackup", "hdmi pcb stackup guide", "cti requirement explanation"]
---
## 1. Résumé : contexte, défis et bénéfices

**Contexte :** avec PCIe 5.0/6.0, USB4, 400G Ethernet, HDMI 2.1 et autres interfaces high-speed, les débits sont entrés dans l’ère 25 Gbps et même 112 Gbps. À ces vitesses, le PCB n’est plus un interconnect passif : il devient un facteur actif qui impacte directement la performance du système.

**Défi :** la différence de Dk entre Glass Weave et Resin fait que les deux lignes d’une differential pair “voient” un Dk effectif différent, créant un écart de propagation : Glass Weave Skew (GWS). Un skew à l’échelle picoseconde suffit à fermer l’eye et à faire monter le BER, rendant le lien instable voire en failure. Les approches traditionnelles de stackup design ne suffisent plus.

**Bénéfices :** ce whitepaper fournit une stratégie complète de **glass weave skew mitigation** pour les équipes système et hardware. Avec decision tree matériaux, templates de stackup, méthodes de modélisation et flux de validation standardisés, l’équipe peut :
- **Shift-left du risque :** éviter le GWS tôt et réduire le cycle design–validate–iterate.
- **Augmenter la marge :** sécuriser la high-speed SI et obtenir des eyes plus ouverts et un BER plus bas.
- **Contrôler coût et reliability :** choisir des matériaux/process cost-effective tout en garantissant la long-term thermal reliability (**thermal reliability stackup**).
- **Standardiser le design :** construire des spécifications de stack réutilisables et améliorer l’efficacité de l’équipe.

---

## 2. Decision tree matériaux : des exigences au choix

Le bon matériau est la première étape (et la plus critique) pour réduire le GWS. L’idée centrale : des diélectriques avec un Dk spatialement plus uniforme. Sur la base de données de labo, HILPCB propose le decision tree suivant.

<div class="div-type-1">

### Principes clés de sélection matériaux
Trois stratégies principales (par efficacité et coût) :
1.  **Optimiser le style de glass weave :** choisir des tissus plus “plats” et à fenêtres plus petites (1067/1086) au lieu de 106/1080.
2.  **Utiliser Spread Glass :** spread mécanique des bundles pour réduire fortement les resin-rich regions.
3.  **Non-woven reinforcement :** élimine la structure tissée ; très coûteux, souvent réservé au RF/special.

</div>

Le tableau ci-dessous intègre data rate, loss budget, coût et manufacturability.

| **Performance metric** | **Key considerations** | **Material tier/series recommandé** | **Glass style** | **Applications typiques** | **Limites et notes** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **< 5 Gbps** | Cost first; faible risque GWS | Standard FR-4 (Tg ≥150°C) | 106, 1080, 7628 | USB 2.0, 1GbE, low-speed bus | Pas adapté aux high-speed differential pairs. Tolerance Dk plus grande (±0.2). |
| **5-15 Gbps** | GWS visible; balance coût/perf | Mid-Loss<br>*(ex. Shengyi S1000-2M)* | 1067, 1086, 3313 | PCIe 3.0/4.0, USB 3.1, SATA, 10GbE, **HDMI PCB Stackup Guide** | Nécessite du co-design routing (angle). Le matériau seul ne supprime pas le GWS. |
| **15-32 Gbps** | GWS devient bottleneck | Low-Loss<br>*(ex. Isola FR408HR, I-Speed)* | Spread Glass<br>ou mechanical spread | PCIe 5.0, 25/50G SerDes, DDR5 | Coût en hausse. Lamination (~200°C) et process window plus stricts. |
| **> 32 Gbps** | Loss + GWS exigent un contrôle extrême | Ultra-Low Loss<br>*(ex. Panasonic Megtron 6/7, Rogers RO4350B)* | mechanical spread ou non-woven | 100/400G Ethernet, OIF-CEI, PCIe 6.0 | Matériaux chers et difficiles. Souvent en **hybrid stack** pour contrôler le coût. |
| **High voltage / high reliability** | Safety et stabilité long terme | High-CTI (CTI ≥ 600V) | selon le débit | industrial control, power, automotive | **CTI requirement explanation**: CTI (Comparative Tracking Index) mesure la résistance au tracking; critique en high voltage. |
| **Flex-rigid** | Bending + signal transfer | Polyimide (PI) high-performance + Low-Loss FR-4 | none (PI) / Spread Glass (rigid) | **Flex rigid material stackup** for high-density interconnects | Impedance control et reliability au niveau du rigid–flex transition sont difficiles. |

---

## 3. Stackup template library

À partir du decision tree, nous proposons des stackup templates validés en production. Ils servent de point de départ et doivent être ajustés selon l’impedance et la board thickness.

### Exemple : 8 couches, comparaison GWS avant/après

**Template 1 : stack FR-4 standard (non optimisé)**
- **Use case :** < 5 Gbps
- **Risque :** GWS sévère au-delà de 5 Gbps.

| Layer | Type | Material | Thickness (mil) | Dk/Df (@10GHz) | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Signal | Copper | 1.4 | - | Top Layer |
| | Prepreg | 7628 | 7.0 | 4.7 / 0.020 | |
| 2 | Plane | Copper | 1.4 | - | GND |
| | Core | FR-4 (S1141) | 39.4 | 4.7 / 0.020 | |
| 3 | Plane | Copper | 1.4 | - | Power |
| | Prepreg | 7628 | 7.0 | 4.7 / 0.020 | |
| 4 | Signal | Copper | 1.4 | - | Inner Signal 1 |
| | Prepreg | 1080 x2 | 5.0 | 4.6 / 0.020 | |
| 5 | Signal | Copper | 1.4 | - | Inner Signal 2 |
| | Prepreg | 7628 | 7.0 | 4.7 / 0.020 | |
| 6 | Plane | Copper | 1.4 | - | Power |
| | Core | FR-4 (S1141) | 39.4 | 4.7 / 0.020 | |
| 7 | Plane | Copper | 1.4 | - | GND |
| | Prepreg | 7628 | 7.0 | 4.7 / 0.020 | |
| 8 | Signal | Copper | 1.4 | - | Bottom Layer |
| **Total** | | | **~62 mil** | | |

**Template 2 : stack optimisé GWS (Low-Loss + Spread Glass)**
- **Use case :** 15-32 Gbps
- **Optimisation :** dielectrics Low-Loss Spread Glass adjacents à L1/L4/L5/L8.

| Layer | Type | Material | Thickness (mil) | Dk/Df (@10GHz) | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Signal | Copper | 1.4 | - | Top Layer |
| | Prepreg | **I-Speed IS300 (Spread Glass)** | 5.0 | **3.6 / 0.005** | **GWS Mitigated** |
| 2 | Plane | Copper | 1.4 | - | GND |
| | Core | FR-4 (S1000-2M) | 40.0 | 4.2 / 0.012 | Cost-effective core |
| 3 | Plane | Copper | 1.4 | - | Power |
| | Prepreg | FR-4 (S1000-2M) | 5.0 | 4.2 / 0.012 | |
| 4 | Signal | Copper | 1.4 | - | Inner Signal 1 |
| | Prepreg | **I-Speed IS300 (Spread Glass)** | 4.0 | **3.6 / 0.005** | **GWS Mitigated** |
| 5 | Signal | Copper | 1.4 | - | Inner Signal 2 |
| | Prepreg | FR-4 (S1000-2M) | 5.0 | 4.2 / 0.012 | |
| 6 | Plane | Copper | 1.4 | - | Power |
| | Core | FR-4 (S1000-2M) | 40.0 | 4.2 / 0.012 | Cost-effective core |
| 7 | Plane | Copper | 1.4 | - | GND |
| | Prepreg | **I-Speed IS300 (Spread Glass)** | 5.0 | **3.6 / 0.005** | **GWS Mitigated** |
| 8 | Signal | Copper | 1.4 | - | Bottom Layer |
| **Total** | | | **~62 mil** | | |

<div class="div-type-3">

### Stackup considerations pour HDI / Flex / MCPCB
- **HDI (High-Density Interconnect):** en HDI, resin fill et uniformité du diélectrique dans les zones microvia ont plus d’impact. Recommander des low-loss matériaux laser-drillable.
- **Flex-Rigid:** PI (Dk ~3.4) côté flex diffère de FR-4 (Dk ~4.2) côté rigide ; le transition nécessite un impedance modeling fin. Les high-speed layers côté rigide doivent aussi appliquer la mitigation GWS.
- **MCPCB ([Metal Core PCB](https://hilpcb.com/en/products/metal-core-pcb)):** orienté dissipation, pas idéal pour high-speed. Si des diff pairs de contrôle existent, considérer l’uniformité Dk de la couche isolante au-dessus du metal core.

</div>

---

## 4. Modélisation : targets impedance, thermal et mécanique

Une modélisation précise est la base théorique du succès. HILPCB utilise Polar Si9000 et Ansys, mais les principes restent essentiels.

### Impedance Modeling

Objectif : ±7% ; pour >25Gbps viser ±5%.

**Microstrip approximation :**
Z₀ ≈ (87 / sqrt(ε_r + 1.41)) * ln(5.98 * H / (0.8 * W + T))
- `Z₀`: characteristic impedance (Ω)
- `ε_r`: Dk effectif
- `H`: dielectric thickness vers le reference plane
- `W`: trace width
- `T`: copper thickness

**Impact GWS :** le modèle classique suppose un seul `ε_r`. En GWS, `ε_r` varie (glass bundle vs resin). Spread Glass réduit la variation spatiale de `ε_r`, rapprochant l’impedance réelle de la prédiction.

### Thermal Modeling

La thermal reliability cible surtout le stress induit par le Z-axis CTE.

**Key metrics :**
- **Tg:** glass transition temperature. Choisir Tg > 170°C pour lead-free reflow (peak ~260°C).
- **Z-axis CTE:** le Z-CTE FR-4 augmente fortement après Tg (250–350 ppm/°C). Les high-speed materials ont souvent un Z-CTE plus bas (ex. Megtron 6 < 40 ppm/°C), réduisant le risque de via cracking.
- **Td:** decomposition temperature à 5% weight loss, indicateur de stabilité thermique long terme.

### Mechanical Modeling

- **Warpage:** stackup symétrique et équilibré. Éviter le stress post-lamination dû au CTE mismatch, surtout en hybrid stack. HILPCB recommande “symmetry” et “balance”.
- **Modulus:** rigidité. En **flex rigid material stackup**, PI low-modulus (flex) + FR-4 high-modulus (rigide) créent des stress concentration points à gérer mécaniquement.

---

## 5. Hybrid stack, backdrill et special structures

Pour un bon équilibre coût/performance, il faut souvent des structures/process plus avancés.

<div class="div-type-6">

### Rogers + FR-4 hybrid stack (Hybrid Stack)
Stratégie **hybrid stack** typique : Rogers ultra-low-loss (ex. RO4350B) seulement sur les outer layers critiques ; power planes et low-speed internes sur FR-4.
- **Challenges :**
    1.  **Compatibilité lamination:** Rogers (~280°C) vs FR-4 (~185°C) → programmes spéciaux + bonding film.
    2.  **CTE mismatch:** risque delamination/warpage.
    3.  **Drilling parameters:** optimiser speed/feed pour éviter smear et dommages de paroi.
- **Approche HILPCB :** base process mature, stackups Rogers+FR-4 validés, DFM checks.

</div>

### Back-drilling / controlled depth drilling

Les via stubs non utilisés forment des cavités résonantes et génèrent des reflections. Le backdrill enlève le stub depuis l’autre face du PCB.
- **Use case :** >10 Gbps, surtout backplanes épais.
- **Key parameters :** précision de profondeur (typ. ±2 mil), stub résiduel (target < 10 mil).
- **Support HILPCB :** depth control précis et validation TDR.

### Flex-Rigid

En **flex rigid material stackup**, le GWS existe en zone rigide. Traiter les high-speed layers rigides comme un PCB “indépendant” et appliquer la mitigation. Couvrir aussi l’impact Dk du coverlay et des adhésifs côté flex dans les modèles.

---

## 6. Validation flow : des matériaux au produit

Une stackup strategy fiable nécessite une validation en boucle fermée.

1.  **IQC (incoming):**
    - **Core:** vérifier Dk/Df des cores et PP vs datasheet.
    - **Méthode:** tests échantillonnés (cavity resonance, SPP).

2.  **Process control en lamination :**
    - **Core:** profils température/pression/temps selon les recommandations fournisseurs.
    - **Méthode:** thermocouples sur le rail panel, monitoring real-time.

3.  **Impedance coupon test :**
    - **Core:** vérifier l’impedance réelle dans la cible.
    - **Méthode:** coupons standard sur chaque panel + TDR 100% — étape clé du **coupon test**.

4.  **Confirmation structure stack :**
    - **Core:** vérifier thickness et registration réels.
    - **Méthode:** micro-section pour inspecter layer structure, hole copper thickness, stub résiduel backdrill.

5.  **Reliability tests :**
    - **Core:** stabilité long terme sous environnements extrêmes.
    - **Méthode:**
        - **Thermal Shock:** cycles rapides pour via reliability.
        - **PCT:** haute température/humidité pour moisture resistance et risque delamination.
        - **CAF:** risque de court-circuit par ion migration sous humidité élevée et bias.

---

## 7. Checklist DFM/DFR (≥35 items)

Checklist issue de l’expérience HILPCB (lab + manufacturing) pour éviter les pièges dès la conception.

| **Catégorie** | **Règle / check item** | **Paramètres / notes** | **Vérification** |
| :--- | :--- | :--- | :--- |
| **Signal Integrity** | **Glass Weave Skew Mitigation (Routing)** | Router les diff pairs avec 5–10° par rapport aux axes X/Y. | Layout Review |
| | **Glass Weave Skew Mitigation (Material)** | Utiliser Spread Glass sur les high-speed layers. | Stackup Review |
| | In-pair length matching | ΔL < 5 mil (selon le débit). | CAD Tool |
| | Inter-pair length matching | ΔL dans le bus < 20 mil. | CAD Tool |
| | Via stub length | >10Gbps : stub < 15 mil; backdrill recommandé. | Simulation, TDR |
| | Via impedance control | Optimiser l’anti-pad pour matcher l’impedance des traces. | Simulation, micro-section |
| | Reference plane continuity | Reference plane continu sous les routes high-speed. | Layout Review |
| | Plane-split crossing check | Interdire le passage de nets high-speed au-dessus de splits. | Layout Review |
| | **Surface Finish Comparison** | >10GHz : ENEPIG ou ISIG; éviter black pad ENIG et nickel loss. | Material Spec |
| | BGA fanout | Microvia ou staggered via pour éviter stub. | Layout Review |
| **Power Integrity** | Decaps proches | Decaps HF à < 100 mil. | Layout Review |
| | Power plane impedance | Chemin low-impedance; éviter planes étroits ou slots. | Simulation |
| | Via ampacity | Calculer temp rise/current capacity par IPC-2152. | Calculation |
| **Mechanical** | Stackup symmetry | Center-symmetric pour limiter warpage. | Stackup Design |
| | Copper balance | Copper distribution la plus uniforme possible. | Layout Review |
| | Thickness tolerance | Standard ±10%, jusqu’à ±5% en contrôle précis. | Stackup Spec |
| | Min annular ring | Grade A: ≥0.05mm; Grade B: ≥0.15mm. | DFM Check |
| | NFP removal | Retirer pads non connectés sur inner planes pour SI. | CAD Tool Setting |
| | V-cut / mouse-bite | V-cut résiduel 1/3 board thickness; pitch mouse-bite cohérent. | Panelization Spec |
| | Gold finger bevel | Bevel 30° ou 45°. | Fab Drawing |
| **Thermal** | Thermal vias | Arrays thermal vias sous heat sources vers plans dissipateurs. | Layout Review |
| | Large copper pours | Pours GND étendus favorisent heat spreading. | Layout Review |
| | Placement | Répartir les heat sources; éviter hot spots. | System Design |
| | **Thermal Reliability Stackup** | Z-CTE < 60 ppm/°C for high-reliability products. | Material Spec |
| **Manufacturing** | Min trace/space | 3/3 mil advanced, 4/4 mil mainstream. | DFM Check |
| | Min drill | Mécanique 0.15mm; laser 0.075mm. | DFM Check |
| | Solder mask dam | Min dam ≥ 3 mil entre pins BGA/QFP. | DFM Check |
| | Via-in-pad | Resin plug + plate over fill pour éviter solder loss. | Fab Note |
| | Test points | Accès aux nets clés; Ø ≥ 0.8mm. | DFT Review |
| | Panelization efficiency | Maximiser l’utilisation du laminate via panel design. | Panelization Spec |
| **Reliability** | **CTI Requirement Explanation** | Industrial/power: CTI ≥ 400V; automotive: CTI ≥ 600V. | Material Spec |
| | CAF resistance | Drill spacing > 0.35mm pour réduire CAF risk. | Layout Review |
| | Solder mask thickness | > 10µm en zones critiques pour isolation/protection. | Fab Spec |
| | PTH copper thickness | Class 2: avg 20µm; Class 3: avg 25µm. | IPC Standard |
| | Final surface finish | Choisir selon reflow count et storage environment. | **Surface Finish Comparison** |

---

## 8. HILPCB service loop et CTA

Une **stackup strategy** parfaite exige materials science, SI simulation et manufacturing. HILPCB fournit plus que le PCB : un service loop technique complet.

- **Matériaux en stock et alternatives :** de FR-4 à Megtron. En cas de lead time long ou cost overrun, nous proposons des alternatives validées avec analyse type **pcb material whitepaper**.
- **Stackup simulation/design gratuits :** avec vos targets impedance et layer planning, nos SI engineers produisent stackup design et **impedance modeling** pour traiter le GWS à la source.
- **Validation laboratoire :** tests Dk/Df, impedance **coupon test**, micro-sections reliability pour aligner design et produit.
- **Feedback production :** données DFM/DFY pour optimiser **hybrid stack** et process spéciaux (backdrill).

**Votre challenge est notre spécialité.** Ne laissez pas Glass Weave Skew devenir le bottleneck du prochain projet.

> **Passez à l’action :** [**contactez les experts matériaux et signal integrity HILPCB**](/contact) et chargez vos fichiers préliminaires ou concept de stackup pour obtenir un rapport gratuit “Stackup Manufacturability & GWS Risk Assessment”.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Cet article fournit un framework complet pour **glass weave skew mitigation** : decision tree matériaux, stackup templates, impedance/thermal/mechanical modeling et manufacturing validation, avec checklist DFM/DFT/DFR. En appliquant les check points et les process windows et en impliquant tôt l’équipe DFM/DFA de HILPCB, vous accélérez prototypes et mass production tout en maintenant qualité et compliance.


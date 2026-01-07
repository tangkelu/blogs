---
title: "low loss laminate tutorial : comprendre les paramètres matériaux et planifier un stackup — la première leçon"
description: "Un low loss laminate tutorial qui explique les paramètres matériaux clés, la planification de stackup, les compromis impédance/thermique/coût et les points de fabrication — avec tableaux de comparaison et exemples pour aider les équipes à bâtir une bibliothèque de stackups standard."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["low loss laminate tutorial", "hdI stackup tutorial", "hdmi pcb stackup guide", "surface finish comparison", "cti requirement explanation", "thermal reliability stackup"]
---
Bonjour, je suis formateur à la HILPCB Stackup & Materials Academy. Dans les échanges quotidiens avec des équipes d’ingénierie, je retrouve toujours le même point douloureux : face à un design high‑speed, comment choisir le bon low loss laminate parmi des centaines de matériaux PCB et définir un stackup qui atteint les objectifs de performance tout en gardant un bon équilibre coût / manufacturability ?

Beaucoup d’équipes sur‑spécifient (Megtron 6 pour 5Gbps) ou sous‑spécifient (FR‑4 standard poussé à 28Gbps) et se retrouvent avec des problèmes de Signal Integrity (SI). Ce **low loss laminate tutorial** est la première leçon pour vous et votre équipe : transformer des paramètres abstraits comme Dk/Df, CTI et fiber weave effect en étapes actionnables de stackup planning, soutenues par des pratiques de production HILPCB, afin de faire de meilleurs compromis.

## 1. Point de départ du stackup design : clarifier les entrées et les sorties attendues

Un stackup professionnel n’est pas un “guess” : c’est un processus systématique basé sur des exigences d’ingénierie claires. Avant de commencer, collectez les inputs suivants :

*   **Exigences signal :**
    *   Data rate maximal ? (ex. 5Gbps, 10Gbps, 28Gbps+)
    *   Cibles d’impédance ? (ex. 50Ω single‑ended, 90Ω/100Ω differential)
    *   Budget total d’insertion loss (dB) ?
*   **Exigences Power Integrity (PI) :**
    *   Courant requis par le core device ? (pilote l’épaisseur cuivre des power planes)
    *   PDN target impedance ? (impacte le coupling power/ground)
*   **Exigences thermiques :**
    *   Puissance et localisation des principales sources de chaleur ?
    *   Température ambiante et stratégie de refroidissement ? Cela détermine si vous avez besoin d’un **thermal reliability stackup**.
*   **Exigences safety et fiabilité :**
    *   Normes à respecter ? (ex. UL, CE)
    *   **CTI requirement explanation** : y a‑t‑il un requis Comparative Tracking Index ? Par exemple, les produits industriels / puissance exigent souvent CTI ≥ 175V (PLC=2), voire plus.
    *   Durée de vie cible et environnement d’usage ? (détermine si un high Tg est nécessaire)
*   **Contraintes mécaniques et coût :**
    *   Limite d’épaisseur PCB ?
    *   Cible de coût ?

**Votre output final doit être un fichier stackup professionnel contenant :**

1.  Définition de la fonction des couches (signal, ground, power).
2.  Références matériaux par couche (Core & Prepreg).
3.  Dielectric thickness et copper thickness par couche (inner/outer).
4.  Épaisseur finie totale et tolérance.
5.  Cibles d’impédance + recommandations de width/spacing par couche.
6.  Notes de process spéciales (backdrill, resin fill, etc.).

## 2. Material parameter cheat sheet : du FR‑4 au low loss laminate

Le bon matériau, c’est “la moitié du job”. Pour accélérer votre modèle mental, nous avons résumé des laminates courants de la bibliothèque HILPCB par classe de pertes. C’est une `dk df table` simplifiée ; les valeurs réelles varient avec la fréquence et le resin content.

<div class="div-type-1">
    <div class="div-type-1-title">Comparaison de performance des matériaux PCB</div>
    <div class="div-type-1-content">
        <p>Le tableau ci-dessous couvre des paramètres clés du FR‑4 standard aux matériaux extremely low-loss, afin de faire une première sélection selon les besoins (data rate, température d’usage, exigences safety).</p>
    </div>
</div>

| Classe matériau | Options HILPCB courantes | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Applications typiques |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard FR‑4** | S1141, KB-6160 | ~4.2 | ~0.020 | 140 | 315 | 175 | Digital/analog low‑frequency, consumer electronics |
| **Mid Tg FR‑4** | IT-158, S1155 | ~4.1 | ~0.018 | 150 | 330 | 175 | Multilayer, lead‑free assembly |
| **High Tg FR‑4** | IT-180A, S1000 | ~4.0 | ~0.015 | 180 | 345 | 175 | Servers, automotive, high‑reliability |
| **Medium loss** | TU-768, S7439 | ~3.8 | ~0.009 | 190 | 360 | 175 | < 10Gbps high‑speed, storage |
| **Low Loss (Low Loss)** | TU-872SLK, S1000-2M | ~3.6 | ~0.005 | 190 | 360 | 175 | 10-25Gbps, server backplanes, **hdmi pcb stackup guide** |
| **Very Low Loss (Very Low Loss)** | I-Speed, M4S | ~3.3 | ~0.003 | 200 | 380 | 175 | 25-56Gbps, RF communications, test equipment |
| **Ultra Low Loss (Ultra Low Loss)** | Megtron 6, Tachyon 100G | ~3.0 | ~0.002 | 210 | 400 | 175 | > 56Gbps, core networking, optical modules |
| **RF** | Rogers RO4350B | 3.48 | 0.0037 | 280 | 390 | 600 | RF/micro‑ondes, antennes |

**Interprétation des paramètres clés :**

*   **Dk (dielectric constant) :** un Dk plus bas signifie souvent une propagation plus rapide et facilite des traces plus larges à impédance égale. La constance du Dk est plus importante que la valeur absolue.
*   **Df (dissipation factor) :** paramètre clé de l’atténuation. Pour >5Gbps, Df < 0.01 est un seuil de base.
*   **Tg (glass transition temperature) :** transition “rigide” → “caoutchouteux”. High Tg (≥170°C) donne une meilleure stabilité en lead‑free et high‑reliability.
*   **Td (thermal decomposition temperature) :** température à 5% de perte de masse, indicateur de thermal reliability long terme.
*   **CTI (Comparative Tracking Index) :** résistance au tracking de surface. FR‑4 standard typiquement 175V (PLC=2) ; certaines applis demandent 600V (PLC=0).

## 3. Core stackup patterns : templates 4/6/8/10 couches

La théorie doit rencontrer la pratique. Voici des templates validés en production, bons points de départ à ajuster selon vos requirements.

| Layer count | Stackup (function) | Core | PP | Finished thickness (mm) | Typical use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4-layer** | SIG/GND/PWR/SIG | 1.0mm Core | 2x 1080 | 1.2 | IoT, MCU control, low‑cost consumer |
| **6-layer** | SIG/GND/SIG/PWR/GND/SIG | 0.5mm Core | 3x 2116 | 1.6 | Embedded systems, DDR3/4 motherboards |
| **8-layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | 0.2mm Core | 4x 2116/1080 | 1.6 | PCIe, USB3.x, HDMI, HPC |
| **10-layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | 0.15mm Core | 5x 1080/106 | 1.6 | Server motherboards, cas complexes **hdI stackup tutorial**, multi high‑speed buses |

**Design notes :**

*   **4-layer :** moins cher, mais EMI/SI plus faibles — rarement adapté au high‑speed.
*   **6-layer :** signaux internes + reference planes solides : excellent ratio coût/performance.
*   **8-layer :** deux reference planes en plus et structures Stripline excellentes — recommandation classique pour **hdmi pcb stackup guide**.
*   **10-layer+ :** pour haute densité et multi power-domain ; plus de ground planes améliore l’isolation et la PI.

## 4. Principes pour coordonner signal/power/ground/copper thickness

L’“âme” d’un bon stackup est la manière dont les couches collaborent.

<div class="div-type-3">
    <div class="div-type-3-title">Golden rules pour la planification de stackup</div>
    <ol>
        <li>
            <h6>Prioriser des reference planes continus</h6>
            <p>Les couches signal high‑speed doivent être adjacentes à un GND ou PWR plane solide. Évitez le routing au-dessus d’un split : cause majeure de crosstalk et d’EMI.</p>
        </li>
        <li>
            <h6>Router les signaux high‑speed sur couches internes</h6>
            <p>La Stripline interne (GND-SIG-GND) offre en général une meilleure immunité EMI et une impédance plus stable que la Microstrip externe (SIG-GND).</p>
        </li>
        <li>
            <h6>Coupler étroitement power et ground planes</h6>
            <p>Placez power et ground adjacents pour exploiter la capacitance de plans, améliorer la PI et fournir un return path HF à faible impédance.</p>
        </li>
        <li>
            <h6>Compromis sur l’épaisseur cuivre</h6>
            <p>Les couches signal utilisent souvent 0.5oz (18μm) ou 1oz (35μm). 0.5oz aide le fine line/space. Les power planes à fort courant peuvent nécessiter 2oz (70μm) ou plus — souvent avec un <strong>thermal reliability stackup</strong>.</p>
        </li>
        <li>
            <h6>Utiliser la symétrie pour éviter le warpage</h6>
            <p>Gardez le stackup aussi symétrique que possible (matériaux, épaisseur cuivre, distribution cuivre). L’asymétrie crée des contraintes en lamination et reflow et augmente le risque de warpage.</p>
        </li>
    </ol>
</div>

## 5. Hybrid lamination et matériaux spéciaux : quand le standard ne suffit plus

Parfois, un seul système matériau ne couvre pas tout — par exemple RF + contrôle digital. Dans ce cas, envisagez l’hybrid lamination.

| Option | Pros | Cons | HILPCB recommendation |
| :--- | :--- | :--- | :--- |
| **All Low Loss material** | Performance cohérente, process mature | Coût plus élevé | Idéal pour comms/servers avec exigences SI élevées. |
| **Rogers + FR‑4 hybrid** | Performance RF + coût digital réduit | Lamination complexe, risk reliability, CTE mismatch | Idéal pour designs d’intégration antenne ; HILPCB optimise les press cycles. |
| **MCPCB (metal core)** | Excellente dissipation | Souvent 1–2 couches ; routing difficile | LED high‑power, power modules, applis thermal‑critical. |
| **Rigid-Flex** | Interconnect 3D ; haute fiabilité | Design complexe ; coût très élevé | Wearables, aerospace, contraintes espace/fiabilité. |

## 6. Manufacturing impact : le “dernier kilomètre” du dessin au PCB physique

Un stackup parfait en théorie peut augmenter le coût ou réduire le yield si le DFM est ignoré.

<div class="div-type-6">
    <div class="div-type-6-title">Capacités HILPCB liées aux décisions de stackup</div>
    <div class="div-type-6-content">
        <ul>
            <li><strong>Resin Flow and Press Cycle:</strong> nous ajustons les profils température/pression selon le prepreg (PP). Par exemple, un 106 PP à forte résine exige un contrôle serré pour remplir les microvias laser HDI tout en évitant une perte de résine qui déstabilise l’épaisseur diélectrique.</li>
            <li><strong>Fiber Weave Effect:</strong> pour 25Gbps+, des styles “loose” (ex. 7628) créent des non-uniformités de Dk et dégradent l’impédance. HILPCB recommande des Flat Glass low loss laminates.</li>
            <li><strong>Back-drilling:</strong> les via stubs sont un “killer” high‑speed. Pour >10Gbps, nous proposons un backdrill depth-controlled pour réduire l’insertion loss de 1–2 dB.</li>
            <li><strong>Impedance coupons and TDR testing:</strong> chaque lot inclut des coupons ; mesure TDR pour rester dans la tolérance (+/- 10% ou plus serré).</li>
            <li><strong>Surface finish comparison:</strong> ENIG est flat et adapté high frequency mais risque “black pad” et coût plus élevé ; OSP est low cost mais shelf-life limitée. Nous recommandons l’option [internal link: PCB surface finish] selon l’application et le coût.</li>
        </ul>
    </div>
</div>

## 7. Comment HILPCB vous aide sur le stackup design ?

Après ce **low loss laminate tutorial**, la planification de stackup peut rester difficile. C’est précisément pourquoi la HILPCB Stackup & Materials Academy existe : nous ne sommes pas seulement un fabricant, mais un partenaire d’ingénierie.

Nous proposons un service **“Stackup quick claim”** pour vous éviter la sélection matériaux et les calculs répétitifs.

<div class="cta-container">
    <div class="cta-text">
        <h5>Vous ne savez pas par où commencer ? Laissez les ingénieurs HILPCB personnaliser votre stackup</h5>
        <p>Partagez vos requirements (data rate, layer count, impédance, etc.). Nos senior engineers livrent une proposition de stackup DFM-validée et optimisée stock sous 24h — plus un rapport détaillé de calcul d’impédance. Gratuit.</p>
    </div>
    Soumettre votre demande de stackup maintenant
</div>

**Pourquoi choisir HILPCB ?**

*   **200+ matériaux en stock :** du FR‑4 standard à Rogers et Megtron, évitant les délais liés aux MOQ et lead times.
*   **Engineering team expérimentée :** milliers de projets high‑speed/high‑frequency/high‑density — identification rapide des risques et optimisation coût/performance.
*   **Labo d’impédance avancé :** nous vérifions par TDR pour que chaque board respecte votre spec.

### Summary

Un excellent stackup est un équilibre entre performance, coût et manufacturability. Partez d’inputs clairs, utilisez le tableau paramètres pour une première sélection, réutilisez des patterns éprouvés et gardez une communication étroite avec votre PCB manufacturer (comme HILPCB). Anticiper les contraintes de fabrication aide à construire une bibliothèque de stackups standardisée et fiable et à accélérer le développement.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

En résumé, ce low loss laminate tutorial explique les paramètres matériaux, la planification de stackup, les compromis impédance/thermique/coût et les aspects de fabrication — avec tableaux et exemples — pour aider les équipes à bâtir une bibliothèque standard et à gérer le risque entre design, matériaux et test. En suivant les checklists et process windows ci‑dessus — et en impliquant tôt l’équipe DFM/DFA de HILPCB — vous pouvez accélérer prototype et volume tout en maintenant qualité et compliance.

> Pour la fabrication et l’assembly, contactez HILPCB via [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.

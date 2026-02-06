---
title: "Tutoriel sur le stackup HDI : Comprendre les paramètres des matériaux et la conception de l'empilage"
description: "Un guide complet sur le stackup HDI, expliquant les paramètres des matériaux, la planification de l'empilage, les compromis entre impédance, thermique et coût, ainsi que les points clés de fabrication."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["hdI stackup tutorial", "hdmi pcb stackup guide", "thermal reliability stackup"]
---

Bonjour à tous, je suis formateur à l'académie de l'empilage et des matériaux de HILPCB. Dans mon travail quotidien, je remarque que de nombreux ingénieurs se sentent démunis face à des paramètres techniques comme le Dk/Df, le CTI ou la Tg, ne sachant pas comment les transformer en un empilage (stackup) PCB fiable et productible. Une mauvaise conception de l'empilage peut, au mieux, entraîner des problèmes d'intégrité du signal, et au pire, provoquer une catastrophe de fiabilité lors de la production de masse.

Aujourd'hui, ce **hdI stackup tutorial** fera office de première leçon pour vous aider à construire systématiquement une réflexion de conception d'empilage. Nous allons ensemble transformer la science des matériaux abstraite en décisions d'ingénierie concrètes, vous permettant non seulement de concevoir un empilage performant, mais aussi d'anticiper et d'éviter les pièges de la fabrication. Que vous travailliez sur un `hdmi pcb stackup guide` haute vitesse ou sur un projet exigeant un `thermal reliability stackup` de haut niveau, ces connaissances constitueront votre base solide.

## Le point de départ du design d'empilage : Définir vos « contraintes »

Avant d'ouvrir votre outil de CAO (EDA) pour tracer la première piste, une conception d'empilage professionnelle commence par une analyse complète des besoins du projet. C'est comme un architecte qui doit comprendre l'usage du bâtiment, le budget et la nature du sol avant de dessiner les plans. Les conditions d'entrée pour la conception de l'empilage comprennent principalement :

*   **Besoins en intégrité du signal (SI)** :
    *   **Vitesse maximale** : Quelle est la vitesse de signal la plus élevée dans votre design ? S'agit-il de PCIe 3.0 à 10 Gbps ou de SerDes à 28 Gbps ? La vitesse détermine votre tolérance aux pertes de matériaux (Df).
    *   **Contrôle d'impédance** : Quelles impédances faut-il contrôler ? 50Ω asymétrique (single-ended) ou 90/100Ω différentiel ? Une impédance précise est le prérequis à une transmission stable.
*   **Besoins en intégrité de l'alimentation (PI)** :
    *   **Courant de cœur** : Quelle est l'intensité du courant transitoire pour les composants critiques (CPU, FPGA) ? Cela définit l'épaisseur de cuivre et la disposition des plans d'alimentation.
    *   **Capacité de plan** : Faut-il utiliser des plans d'alimentation et de masse adjacents pour créer une capacité de plan et fournir un découplage haute fréquence ?
*   **Gestion thermique et fiabilité** :
    *   **Consommation et environnement** : Quelle est la puissance totale de la carte, l'emplacement des composants qui chauffent et la température de fonctionnement finale ? Cela impacte directement le choix de la température de transition vitreuse (Tg) et de la température de décomposition thermique (Td).
    *   **Normes de sécurité** : Le produit comporte-t-il des parties haute tension ? Y a-t-il des exigences CTI (indice de résistance au cheminement) spécifiques (ex: >400V) ? Crucial pour l'industrie et l'énergie.
*   **Coût et chaîne d'approvisionnement** :
    *   **Coût cible** : Quel est le budget par carte ? Cela détermine si vous devez optimiser dans la gamme standard FR-4 ou si vous pouvez envisager des matériaux haute performance comme Rogers.
    *   **Volumes et délais** : Le volume annuel estimé et les délais de livraison influent sur la disponibilité des matériaux et les quantités minimales de commande (MOQ).

Ces conditions aboutiront à un plan d'empilage précis pour le fabricant de PCB, incluant le type de couche, le matériau, l'épaisseur, l'épaisseur de cuivre et les exigences d'impédance.

## Comprendre le « langage des matériaux » : Tableau récapitulatif des paramètres clés

Choisir le bon matériau est le cœur du design d'empilage. Face à des centaines de références, il faut savoir identifier les paramètres essentiels. Voici un tableau résumant les indicateurs clés de quelques matériaux représentatifs de la bibliothèque HILPCB.

<div style="background-color: #f0f7ff; border-left: 5px solid #007bff; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #0056b3; margin-top: 0;">Arbitrage des paramètres : Pas de matériau parfait, seulement des choix adaptés</h4>
    <p style="margin-bottom: 0;">Dans le choix des matériaux, performance et coût sont toujours en conflit. Par exemple, viser un Df (perte diélectrique) extrêmement bas implique généralement un coût plus élevé. De même, un matériau à haute Tg offre une meilleure stabilité thermique mais sa fenêtre de pressage est plus complexe. La valeur de l'ingénieur réside dans sa capacité à trouver le point d'équilibre optimal. Pour de l'électronique grand public sensible au coût, le S1141 ou l'IT-180A suffisent souvent ; pour une carte mère de station de base, le S1000-2M sera nécessaire.</p>
</div>

| Modèle | Fournisseur | Catégorie | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Application Cœur |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S1141** | Shengyi | FR-4 Standard | 4.2 | 0.020 | 140 | 315 | >175 | Grand public, contrôle basse fréquence |
| **IT-180A** | ITEQ | FR-4 Haute Tg | 3.9 | 0.012 | 175 | 345 | >400 | Serveurs, contrôle industriel, auto |
| **S1000-2M** | Shengyi | Mid-Loss | 3.6 | 0.009 | 190 | 360 | >400 | Calcul haute vitesse, centres de données |
| **EM-827** | EMC | Low-Loss | 3.4 | 0.006 | 200 | 370 | >600 | SerDes 25Gbps+, équipements réseau |
| **RO4350B** | Rogers | RF/Hyperfréquence | 3.48 | 0.0037 | 280 | 390 | >400 | Modules RF, antennes, 5G |

**Interprétation des paramètres :**
*   **Dk (Constante diélectrique)** : Influence la vitesse de propagation et l'impédance. Plus elle est basse et stable, mieux c'est pour les signaux rapides.
*   **Df (Facteur de perte)** : Quantité d'énergie transformée en chaleur dans le matériau. Crucial pour les longs trajets à haute fréquence.
*   **Tg (Température de transition vitreuse)** : Passage de l'état rigide à l'état souple. Une Tg élevée (>170°C) garantit la stabilité dimensionnelle lors des passages au four.
*   **Td (Température de décomposition)** : Température où le matériau perd 5% de son poids. Indique la résistance thermique à long terme.
*   **CTI** : Résistance aux fuites électriques de surface. Vital pour la haute tension.

## De 4 à 10+ couches : Modèles de structures d'empilage classiques

Voyons maintenant comment « assembler » ces matériaux. Un empilage ne se fait pas au hasard, il suit les principes de compatibilité électromagnétique (CEM) et d'intégrité du signal.

<div style="background-color: #fff4e5; border-left: 5px solid #ff9800; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #e65100; margin-top: 0;">Méthode de planification en trois étapes</h4>
    <ol>
        <li><strong>Déterminer le nombre de couches</strong> : Basé sur la densité de routage, les plans d'alimentation et le budget. Assigner une fonction (signal, masse, alim) à chaque couche.</li>
        <li><strong>Construire les plans de référence</strong> : Placer en priorité des plans GND (masse) continus. Ce sont les chemins de retour des signaux et des blindages naturels.</li>
        <li><strong>Optimiser et symétriser</strong> : Ajuster les épaisseurs pour l'impédance. Garder une structure symétrique (haut/bas) pour éviter le voilage (warping) lors de la fabrication.</li>
    </ol>
</div>

| Couches | Structure classique (Haut vers Bas) | Application type | Avantages | Inconvénients |
| :--- | :--- | :--- | :--- | :--- |
| **4 couches** | SIG/GND/PWR/SIG | Modules IoT, contrôleurs simples | Coût très bas, simple | CEM médiocre, impédance instable |
| **6 couches** | SIG/GND/SIG/SIG/PWR/SIG | Grand public, cartes industrielles | Plan de masse complet, CEM améliorée | Plans de référence moyens pour signaux internes |
| **6 couches (Rec)** | SIG/GND/PWR/GND/SIG/SIG | Applications HDMI/USB3.0 | Excellente CEM et SI, coût modéré | Perd une couche de routage |
| **8 couches** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | Serveurs, calcul haute performance | Blindage multicouche, impédance précise | Coût plus élevé, fabrication plus longue |
| **10 couches** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | Équipements réseau, cartes FPGA | Excellente isolation alim/masse | Coût élevé, précision de fabrication requise |

## La « Symphonie » des couches : Signal, Alimentation, Masse et épaisseur de cuivre

Un bon empilage est une orchestration harmonieuse de ses éléments.

### Couche de signal : Microstrip vs Stripline
*   **Microstrip** : Pistes en surface, un côté à l'air, l'autre sur le diélectrique. Avantages : simple à fabriquer et tester. Inconvénients : sensible aux parasites, plus de rayonnement.
*   **Stripline** : Pistes internes entre deux plans de référence. Avantages : excellente CEM, impédance stable. Inconvénients : routage plus complexe.
*   **Conseil HILPCB** : Pour les signaux >5Gbps, privilégiez le stripline.

### Plans de référence : La suprématie du GND
Un plan GND solide est la base du design haute vitesse. Il offre le chemin de retour le plus court et limite la diaphonie. Évitez de couper les plans de masse sous les signaux rapides.

### Épaisseur de cuivre : Arbitrage 1 oz vs 2 oz
*   **Capacité de courant** : Le cuivre 2 oz (70µm) supporte environ 1,5 à 1,8 fois plus de courant que le 1 oz (35µm). Nécessaire pour les couches d'alimentation.
*   **Impact impédance** : Un cuivre plus épais nécessite des pistes plus larges pour la même impédance, ce qui prend plus de place.
*   **Fabrication** : Le cuivre épais est plus dur à graver avec précision. Pour les cartes [HDI](/technology/what-is-hdi-pcb/), on utilise souvent 0.5 oz ou 1 oz en interne.

## Au-delà du FR-4 : Hybrides, bases métalliques et matériaux flexibles

### Empilage hybride (Hybrid Stackup)
Utiliser plusieurs matériaux différents, courant en RF. Par exemple, du Rogers pour la partie radio et de l'IT-180A pour la partie numérique. Cela permet de concentrer la performance là où c'est nécessaire tout en maîtrisant les coûts.

| Schéma Hybride | Avantages | Défis et Considérations |
| :--- | :--- | :--- |
| **Rogers + FR-4** | Haute performance dans les zones critiques, coût global maîtrisé | Déséquilibre du CTE (Coefficient d'Expansion Thermique), risque de délaminage ou fiabilité ; paramètres de pressage (Press Cycle) complexes, nécessite une usine expérimentée. |
| **Matériaux Haute Vitesse + Standard** | Répond aux exigences de faible perte pour les canaux rapides, réduit le coût total | Différence de flux de résine (Resin Flow) entre matériaux, peut affecter l'homogénéité de l'épaisseur diélectrique. |

### Bases métalliques (MCPCB) et Flex
*   **MCPCB** : Base alu ou cuivre pour une dissipation thermique maximale (LED haute puissance, alimentations).
*   **Flex / Rigid-Flex** : Pour les connexions 3D. Design complexe demandant une attention particulière aux contraintes de pliage.

## Du design à la production : Les impacts inévitables du procédé

Votre plan d'empilage n'est qu'un modèle théorique. La réalité physique dépend de l'usine.

<div style="background-color: #e8f5e9; border-left: 5px solid #2e7d32; padding: 20px; margin: 20px 0; border-radius: 5px;">
    <h4 style="color: #1b5e20; margin-top: 0;">Capacités de contrôle HILPCB</h4>
    <p style="margin-bottom: 0;">Chez HILPCB, nous analysons la faisabilité de votre empilage via nos modèles de pressage. En simulant le flux de résine, nous compensons les épaisseurs pour garantir une précision d'impédance de ±5%, bien meilleure que le standard industriel de ±10%.</p>
</div>

*   **Flux de résine (Resin Flow)** : Lors du pressage, la résine du préimprégné (PP) fond et remplit les vides du cuivre. L'épaisseur finale est donc moindre que l'épaisseur initiale du PP.
*   **Cycle de pressage** : Chaque matériau a sa courbe de température/pression. Un mauvais cycle cause des délaminations.
*   **Voilage (Warpage)** : Souvent dû à un manque de symétrie ou une répartition inégale du cuivre.
*   **Back-drilling** : Pour le >10Gbps, retirer les « stubs » de vias inutilisés pour éviter l'effet d'antenne.
*   **Coupon d'impédance** : Une barrette de test sur le panneau de production pour vérifier l'impédance réelle au TDR.

## HILPCB : Votre partenaire technique

HILPCB n'est pas qu'un fabricant, c'est votre partenaire. Nous simplifions vos designs :
*   **Bibliothèque de 200+ matériaux** : Des stocks permanents pour tous les besoins (FR-4, High-speed, RF, MCPCB).
*   **Laboratoire de test d'impédance** : Validation rigoureuse de chaque lot.

## Obtenez votre plan d'empilage personnalisé

Ne luttez plus seul avec les fiches techniques. HILPCB propose un service de conseil rapide pour vous fournir un empilage validé et prêt pour la production.

<div style="background-color: #f8f9fa; border: 1px solid #dee2e6; padding: 25px; margin: 30px 0; border-radius: 10px; text-align: center;">
    <h3 style="margin-top: 0;">Besoin d'aide pour votre empilage ?</h3>
    <p>Envoyez-nous vos besoins (couches, vitesse, impédance, matériaux spéciaux). Nos experts vous répondront sous 24h avec une proposition détaillée : choix des matériaux, calculs d'épaisseurs et simulations d'impédance.</p>
    <a href="#" style="display: inline-block; background-color: #007bff; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Obtenir mon plan d'empilage gratuit</a>
</div>

## Résumé : Un empilage réussi est un consensus entre design et fabrication

Un bon empilage n'est pas une simple superposition de couches. C'est la fusion de votre intention de design et des capacités de l'usine. Il commence par des besoins clairs et finit par le respect des contraintes de fabrication. Communiquez tôt avec des experts comme HILPCB pour faire de votre empilage le socle de votre succès.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

En suivant les conseils de ce **hdI stackup tutorial**, vous maîtrisez désormais les bases pour concevoir des empilages performants et fiables. N'oubliez pas d'impliquer l'équipe DFM de HILPCB dès le début pour sécuriser votre mise en production.

> Pour un support en fabrication et assemblage, contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des conseils DFM/DFT.

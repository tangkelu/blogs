---
title: "Via-in-Pad Plated Over (VIPPO) : Maîtriser les défis de collaboration opto-électronique et de consommation thermique dans les PCB de module optique de centre de données"
description: "Analyse approfondie des technologies essentielles pour Via-in-Pad Plated Over (VIPPO), couvrant l'intégrité des signaux haute vitesse, la gestion thermique et la conception de l'alimentation/interconnexion pour vous aider à construire des PCB de module optique de centre de données haute performance."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad Plated Over (VIPPO)", "Microvia/via empilée", "Cuivre lourd 3oz+", "Stackup hybride (Rogers+FR-4)", "Impédance contrôlée", "Pilier de cuivre"]
---

Avec le trafic du centre de données croissant exponentiellement, les demandes de solutions d'interconnexion de bande passante plus élevée et de consommation d'énergie inférieure deviennent urgentes. La technologie Co-Packaged Optics (CPO), intégrant les moteurs optiques et les ASIC de commutation sur le même substrat, est considérée comme la percée clé surpassant les goulots d'étranglement des modules optiques enfichables traditionnels. Cependant, cette intégration sans précédent apporte également des défis sévères de conception et de fabrication PCB.

En tant qu'ingénieur CPO, je comprends profondément que dans la collaboration opto-électronique et les compromis de consommation thermique, la technologie d'interconnexion PCB avancée est la base du succès. Parmi celles-ci, la technologie **via-in-pad plated over (VIPPO)** est le cœur pour maîtriser cette complexité. Ce n'est pas simplement la clé de réalisation du routage ultra-haute densité, mais le point d'appui de l'efficacité de l'intégrité du signal et de la gestion thermique.

## Routage au niveau du board CPO et collaboration d'interface opto-électronique : Valeur essentielle de VIPPO

Dans l'architecture CPO, les chemins de signal électrique haute vitesse (comme 224G PAM4) de l'ASIC au moteur optique sont drastiquement raccourcis, mais nécessitent des substrats PCB avec une densité de routage et une intégrité du signal sans précédent.

La technologie **via-in-pad plated over (VIPPO)** place les vias directement sous les coussinets de soudure, remplissant complètement avec du matériau conducteur (typiquement du cuivre), effectuant finalement un placage de planification, résolvant complètement ces problèmes.

**Les avantages essentiels se manifestent comme:**

1. **Densité de routage extrême:** VIPPO élimine les traces de fan-out externes aux coussinets et les coussinets de via, permettant aux broches de dispositif BGA haute densité un routage inter-direct.

2. **Chemins de signal les plus courts:** Les signaux directement des coussinets de dispositif via les structures VIPPO dans les traces de couche interne, chemins les plus courts, réduisent efficacement l'inductance parasite et la capacité.

3. **Intégrité de l'alimentation optimisée (PI):** Grâce à l'utilisation extensive de VIPPO sur les plans d'alimentation et de masse, réduisez significativement l'impédance du réseau de distribution d'alimentation (PDN).

Chez HILPCB, nous possédons des processus de fabrication VIPPO matures, réalisant un remplissage de micro-trou précis et une planification parfaite, assurant la fiabilité de l'assemblage SMT ultérieur, fournissant une base de fabrication PCB solide [Interconnexion haute densité (HDI)](https://hilpcb.com/en/products/hdi-pcb) pour vos projets CPO.

## Conception thermique : Distribution d'alimentation CPO et structure de refroidissement

CPO place des ASIC de puissance massive (atteignant des centaines de watts) et des moteurs optiques sensibles à la température (lasers, modulateurs) à proximité étroite, formant des défis sévères de "points chauds". La gestion thermique n'est plus simplement un problème au niveau du système, mais une collaboration multi-niveaux couvrant les puces, les substrats jusqu'aux radiateurs.

- **Chemins de conduction thermique verticale:** Les structures VIPPO remplies de cuivre sont essentiellement des colonnes thermiques efficaces, conduisant rapidement la chaleur des fonds de dispositif vers les plans thermiques internes PCB ou directement vers les radiateurs de face arrière.

- **Collaboration avec des couches de cuivre lourd:** Pour gérer les courants énormes et la chaleur, les substrats CPO utilisent généralement la technologie **cuivre lourd 3oz+**. VIPPO se connecte sans faille avec ces couches de cuivre épaisses, formant des réseaux de dissipation thermique tridimensionnels et efficaces.

- **Technologies de refroidissement supplémentaires:** Sous des demandes de refroidissement extrêmes, la technologie **pilier de cuivre** (copper pillar) est utilisée pour l'interconnexion et le refroidissement au niveau des puces.

## CTE faible et empilement de matériaux : Fiabilité et contrôle de la déformation

La fiabilité à long terme du module CPO dépend largement de la stabilité mécanique lors des cycles de température de fonctionnement.

**Par conséquent, la sélection des matériaux du substrat CPO et la conception du stackup sont critiques:**

- **Stackup hybride (Rogers+FR-4):** Stratégie équilibrée coût-performance courante. Près des couches de signal critiques des puces CPO, utilisez des matériaux spéciaux à faible CTE et faible perte (comme la série Rogers ou Tachyon).

- **Matériaux de base à faible CTE et prepregs:** La sélection de substrats avec un meilleur appariement CTE aux puces est une solution fondamentale.

- **Empilement symétrique et contrôle de la déformation:** La conception des structures **stackup hybride (Rogers+FR-4)** doit strictement respecter les principes de symétrie.

## Tests/étalonnage CPO et surveillance en ligne

La complexité du module CPO détermine que les processus de test et de vérification dépassent largement les PCB traditionnels.

1. **Tests de loopback (Loopback):** Pendant la phase de conception PCB, vous devez réserver des chemins de test de loopback électrique et optique.

2. **Surveillance en ligne et CMIS:** Les modules CPO doivent respecter les spécifications d'interface de gestion de module commun, rapportant en temps réel l'état de santé du module via les interfaces I2C.

3. **Interfaces de test haute fréquence:** Pour les tests de diagramme oculaire et BER précis, vous devez extraire les signaux atteignant 112GHz des substrats CPO.

4. **Compatibilité ATE (Automated Test Equipment):** La conception PCB doit considérer la compatibilité de la station de sonde ATE.

## Faisabilité de fabrication : Tolérances, accessoires et processus d'assemblage

Les conceptions excellentes sont inutiles si elles ne sont pas fabriquées économiquement et de manière fiable. La conception de faisabilité de fabrication du substrat CPO (DFM) et la conception d'assemblage (DFA) sont les clés du succès du projet.

- **Tolérances de fabrication:** Les substrats CPO imposent des exigences extrêmement strictes sur la largeur de trace/espacements, l'alignement entre les couches, la précision de forage.

- **Alignement du réseau de fibres:** Réaliser un alignement de précision sub-micromètre entre les réseaux de fibres et les circuits intégrés photoniques est l'étape d'assemblage CPO la plus difficile.

- **Accessoires d'assemblage et polymérisation:** Après l'achèvement de l'alignement, utilisez des adhésifs de polymérisation ultraviolette (UV) ou thermique pour fixer définitivement les réseaux de fibres.

- **Solutions clés en main:** La complexité CPO rend les coûts de communication entre les étapes de conception, fabrication et assemblage extrêmement élevés. La sélection de partenaires comme HILPCB fournissant la fabrication PCB via les services d'[assemblage PCBA clés en main](https://hilpcb.com/en/products/turnkey-assembly) simplifie considérablement les chaînes d'approvisionnement.

<div style="background: linear-gradient(135deg, #020617 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a5b4fc; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🚀 Emballage CPO : Directives de couche physique d'intégrité du signal (SI) de l'ère 224G</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Répondre aux défis extrêmes de budget de liaison dans l'emballage co-conçu de moteurs photoniques silicium et ASIC</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">01. Contrôle extrême de la tolérance d'impédance (Z-Accuracy)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logique essentielle :</strong>À des débits de 224Gbps, les chutes d'impédance ferment directement les diagrammes oculaires. Doit contrôler l'impédance différentielle dans <strong>±5%</strong>. Utilisez les modèles de compensation de gravure de second ordre précis de HILPCB, éliminant les effets de variation de largeur de trace de fabrication sur la réflexion du signal.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">02. Système de matériau ultra-basse perte (UL-Loss)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logique essentielle :</strong>Sélectionnez les matériaux diélectriques Megtron 8 ou Rogers <strong>Ultra-Low Loss</strong>, associés à la feuille de cuivre HVLP3 (hyper-low profile). Assurez-vous que la perte d'insertion de liaison au millimètre (IL) respecte les normes d'efficacité énergétique strictes de CPO.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">03. Structure VIPPO et suppression de la résonance</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logique essentielle :</strong>Utilisez la technologie <strong>VIPPO (Via-in-Pad Plated Over)</strong> combinée avec le back-drilling en profondeur complète, éliminant complètement les stubs de via (Stub). Réduisez la capacité parasite, décalez les points de résonance en dehors de la bande passante de travail.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #818cf8; display: flex; flex-direction: column;">
<strong style="color: #a5b4fc; font-size: 1.15em; margin-bottom: 12px;">04. Simulation de crosstalk 3D pleine onde (X-Talk)</strong>
<p style="color: rgba(255, 255, 255, 0.9); font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Logique essentielle :</strong>Dans les zones de routage haute densité, vous devez effectuer une simulation électromagnétique 3D pleine onde. Optimisez les réseaux de <strong>blindage GND</strong> via et les espacements de paires différentielles, supprimez FEXT et NEXT sous -40dB.</p>
</div>
</div>

<div style="margin-top: 35px; padding: 25px; background: rgba(165, 180, 252, 0.1); border-radius: 16px; border-right: 8px solid #818cf8; font-size: 0.95em; line-height: 1.7; color: #c7d2fe;">💡 <strong>Recommandation d'expert HILPCB :</strong>Dans la conception CPO, les vias thermiques sous les moteurs optiques entrent souvent en conflit avec les chemins de signal haute vitesse. Nous recommandons la technique de layout <strong>Grille non uniforme (Non-uniform Grid)</strong>, assurant la conductivité thermique tandis que la simulation 3D optimise les chemins de retour de signal, empêchant les dommages d'intégrité de référence du plan de masse.</div>
</div>

## Directives de couche physique d'intégrité du signal (SI) de l'ère CPO 224G

| Directive | Logique essentielle | Implémentation |
| :--- | :--- | :--- |
| **01. Contrôle extrême de la tolérance d'impédance (Z-Accuracy)** | À des débits de 224Gbps, les chutes d'impédance ferment directement les diagrammes oculaires. Doit contrôler l'impédance différentielle dans **±5%**. | Utilisez les modèles de compensation de gravure de second ordre précis de HILPCB, éliminant les effets de variation de largeur de trace de fabrication sur la réflexion du signal. |
| **02. Système de matériau ultra-basse perte (UL-Loss)** | Sélectionnez les matériaux diélectriques Megtron 8 ou Rogers de niveau **Ultra-Low Loss**, associés à la feuille de cuivre HVLP3 (hyper-low profile). | Assurez-vous que la perte d'insertion de liaison au millimètre (IL) respecte les normes d'efficacité énergétique strictes de CPO. |
| **03. Structure VIPPO et suppression de la résonance** | Utilisez la technologie **VIPPO (via-in-pad plated over)** combinée avec le back-drilling en profondeur complète, éliminant complètement les stubs de via (Stub). | Réduisez la capacité parasite, décalez les points de résonance en dehors de la bande passante de travail. |
| **04. Simulation de crosstalk 3D pleine onde (X-Talk)** | Dans les zones de routage haute densité, vous devez effectuer une simulation électromagnétique 3D pleine onde. | Optimisez les réseaux de **blindage GND** via et les espacements de paires différentielles, supprimez FEXT et NEXT sous -40dB. |

<div style="background-color: #1A237E; color: #ffffff; padding: 25px; border-radius: 10px; margin: 30px 0;">
    <h3 style="color: #ffffff; text-align: center; border-bottom: 2px solid #42A5F5; padding-bottom: 10px;">Capacités de fabrication de base de substrat CPO HILPCB</h3>
    <table style="width: 100%; margin-top: 15px; border-collapse: collapse; color: #000000;">
        <thead style="background-color: #42A5F5;">
            <tr>
                <th style="padding: 12px; text-align: left;">Paramètre technique</th>
                <th style="padding: 12px; text-align: left;">Capacité HILPCB</th>
                <th style="padding: 12px; text-align: left;">Valeur pour CPO</th>
            </tr>
        </thead>
        <tbody style="background-color: #ffffff;">
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Via-in-Pad Plated Over</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Remplissage cuivre/résine électrolytique, planéité &lt; 15µm</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Atteint la densité de routage maximale, optimise les chemins signal/thermique</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Microvia/Via empilée</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Prend en charge jusqu'à 4+N+4 étages vias empilées/entrelacées aveugles enterrées</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Construit des interconnexions 3D complexes, raccourcit les chemins de signal</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Cuivre lourd 3oz+</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Couches internes/externes supportent 3-10oz épaisseur de cuivre</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Porte des courants élevés, dissipation thermique efficace, améliore l'intégrité de l'alimentation</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Stackup Hybride</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Expert en stratification hybride Rogers/Megtron/Tachyon avec FR-4</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Équilibre les coûts, la performance et la fiabilité, contrôle la désadaptation CTE</td>
            </tr>
            <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Impédance contrôlée</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">Contrôle de tolérance ±5%, fournit des rapports de test TDR</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Garantit la qualité de transmission de signal haute vitesse, réduit le taux d'erreur de bit</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

La technologie **via-in-pad plated over (VIPPO)** n'est pas simplement un processus de fabrication de via unique ; c'est un point d'appui pour l'écosystème CPO entier. En fournissant une densité de routage incomparable, une intégrité du signal excellente, des canaux de conduction thermique efficaces, elle adresse parfaitement les défis essentiels de collaboration opto-électronique et de consommation thermique de CPO.

Sur le chemin vers 800G, 1.6T et une bande passante plus élevée, les exigences de technologie PCB ne font qu'augmenter. En tant que votre partenaire de confiance, HILPCB, tirant parti de l'accumulation profonde dans la fabrication de PCB à [cuivre lourd](https://hilpcb.com/en/products/heavy-copper-pcb) et de boards haute fréquence complexes, s'engage à fournir des solutions de substrat CPO de pointe aux clients mondiaux.

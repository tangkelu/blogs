---
title: "Copper coin : maîtriser les liens ultra-high-speed et les défis low-loss des high-speed SI PCB"
description: "Analyse approfondie de la technologie Copper coin : high-speed Signal Integrity, thermal management et power/interconnect design, pour concevoir des high-performance high-speed SI PCB."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["Copper coin", "Copper pillar", "Heavy copper 3oz+", "Hybrid stack-up (Rogers+FR-4)", "Via-in-Pad plated over (VIPPO)", "Controlled impedance"]
---
À l’ère data-driven, des data centers et AI accelerators aux infrastructures 5G/6G, la demande en bande passante et en débit augmente de manière exponentielle. Les liens SerDes à 112G, 224G et au-delà deviennent la norme, créant des défis inédits en design PCB. Les engineers doivent satisfaire des exigences strictes de Signal Integrity (SI) tout en gérant la chaleur massive générée par les puces high-performance. Dans ce contexte, **Copper coin** (embedded copper block) s’impose comme une solution clé pour équilibrer transmission ultra-high-speed et thermal management efficace. Ce n’est pas un simple composant de dissipation : c’est un élément fondamental de la stabilité et de la fiabilité du système.

En tant qu’engineer habitué aux mesures TDR/VNA et à l’analyse de S-parameters, je sais que chaque dB de loss et chaque ps de jitter peuvent faire échouer un lien. Les méthodes traditionnelles, comme les thermal via arrays, deviennent insuffisantes face à des FPGA, ASIC et GPU à 150W et plus. Cet article décortique **Copper coin** : principes, impacts SI/Power Integrity (PI), intégration avec des stack-up avancés, et points de contrôle en manufacturing, afin de traiter de façon structurée ces deux contraintes majeures du high-speed PCB.

### Qu’est-ce que Copper coin, et quels sont ses avantages clés ?

**Copper coin** est un procédé de fabrication avancé : un bloc de cuivre massif pré-usiné (souvent du cuivre C1100 haute pureté) est inséré dans une cavity préfabriquée ou une structure traversante du PCB. Le bloc est en contact direct avec le Thermal Pad du composant chauffant (par exemple une puce en package BGA) et traverse la carte jusqu’au backside, où il se couple à un grand heatsink ou à une chassis baseplate, créant un chemin thermique à très faible résistance.

Avantages principaux :

1.  **Conduction thermique exceptionnelle :** la conductivité du cuivre est d’environ 400 W/m·K, largement supérieure à FR-4 (~0,25 W/m·K) et à la conduction équivalente de plated vias. Un **Copper coin** massif évacue rapidement la chaleur des hotspots, souvent avec une efficacité de plusieurs ordres de grandeur au-dessus des thermal via arrays. Cela évite throttling et dommages liés aux Hot Spots.

2.  **Power Integrity (PI) améliorée :** le bloc est généralement connecté à GND. Sa masse métallique fournit un return path à très faible inductance et impédance pour les forts courants. Cela réduit l’impédance PDN, atténue Ground Bounce et SSN, et fournit un plan de référence stable et propre pour les signaux high-speed.

3.  **Rigidité mécanique renforcée :** le bloc augmente la rigidité locale sous la zone BGA, réduisant les contraintes dues au CTE mismatch lors de chocs, vibrations ou thermal cycling et améliorant la fiabilité long terme des joints de soudure BGA.

4.  **Flexibilité de design :** forme, taille et épaisseur du **Copper coin** sont personnalisables (T-shape, I-shape, formes spécifiques) pour optimiser le heat path et l’interface mécanique.

### Comment Copper coin répond aux défis de thermal management en high-speed ?

Dans les systèmes numériques high-speed, l’atténuation dépend fortement de la température. Lorsque la température de la puce augmente, les performances du silice se dégradent et le dielectrique du PCB chauffe, ce qui fait varier Dk et Df. Cela affecte la **Controlled impedance** des lignes et augmente la perte, dégradant la SI.

**Copper coin** crée une “thermal highway” :

-   **Contact direct et conduction efficace :** le Thermal Pad est couplé à la surface lisse du **Copper coin** via TIM ou soudure directe, permettant un transfert rapide du junction vers le bloc.
-   **Diffusion latérale et verticale :** au-delà de la conduction en Z, la masse du bloc offre un excellent spreading en X-Y, dissipant les hotspots et réduisant l’élévation locale de température.
-   **Couplage direct à la dissipation externe :** l’extrémité backside est généralement affleurante (ou légèrement saillante), assurant un contact direct avec heatsink, liquid cold plate ou châssis. Le métal-métal réduit fortement la résistance d’interface par rapport à FR-4 + vias.

Dans les applications à très fort courant (par exemple des power modules), on adopte aussi des procédés **Heavy copper 3oz+**. **Copper coin** s’intègre aux thick copper layers pour bâtir un système électro-thermique capable de transporter des centaines d’ampères et d’évacuer efficacement la chaleur Joule.

<div style="background-color: #F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align: center; color: #000000;">Comparaison des solutions de dissipation</h3>
<table style="width:100%; border-collapse: collapse; text-align: center;">
<thead style="background-color: #E0E0E0;">
<tr>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Caractéristique</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Copper Coin</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Thermal via array (Thermal Vias)</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Vapor chamber embedded (Vapor Chamber)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Conductivité thermique équivalente</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Très élevée (≈400 W/m·K)</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Faible à moyenne (50-150 W/m·K)</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Extrêmement élevée (1500-2000+ W/m·K)</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Résistance thermique</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Très faible</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Plus élevée</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Très faible</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Impact sur le routing</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Grande zone keep-out</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Routing entre vias possible mais limité</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Très grande zone keep-out</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Coût manufacturing</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Élevé</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Faible</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Très élevé</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Cas d’usage</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">High-power ASIC/FPGA, optical modules</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Medium/low-power, packages QFN</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Server CPU/GPU avec exigences thermiques extrêmes</td>
</tr>
</tbody>
</table>
</div>

### Impact “double tranchant” sur la SI : opportunités et risques

Du point de vue SI, **Copper coin** est une arme à double tranchant. Bien exploité, il améliore les performances ; négligé, il peut mener à une failure du lien.

**Opportunités (effets positifs) :**

-   **Plan de référence stable :** un bloc connecté à GND fournit un référentiel très stable. C’est essentiel pour les differential pairs : les deux traces voient un environnement cohérent, la **Controlled impedance** est mieux tenue et la conversion common-mode diminue.
-   **Réduction du crosstalk :** le bloc joue le rôle de grande structure de masse qui isole des zones : par exemple séparer le power noisy des SerDes sensibles et réduire EMI/crosstalk.
-   **Stabilité thermique :** en maîtrisant la température, **Copper coin** stabilise Dk/Df des matériaux (par ex. [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb)). Pour les liens long-reach et high-data-rate, de petites dérives Dk/Df suffisent à provoquer mismatch et sur-loss.

**Risques (effets négatifs) :**

-   **Discontinuité de référence :** si une net high-speed traverse le bord du bloc, le reference plane est interrompu. La return current doit contourner, l’aire de boucle augmente, avec des réflexions et EMI plus fortes.
-   **Discontinuité d’impédance :** même au-dessus, le champ change car la référence passe d’un foil fin à une masse de cuivre épaisse, provoquant souvent une baisse brutale d’impédance (discontinuité capacitive) et des réflexions.
-   **Blocage du routing :** le bloc crée une large keep-out area, rendant le fan-out BGA haute densité plus difficile.

Les solutions doivent être prévues tôt : ne pas router high-speed par-dessus le bord ; placer des ground Stitching Vias denses le long du périmètre ; utiliser une 3D EM simulation pour modéliser l’impact sur les transmission lines proches, et ajuster width/spacing pour compenser.

### Copper coin et stack-up avancé : une approche intégrée

La réussite de **Copper coin** dépend de son intégration avec le stack-up – surtout dans des systèmes combinant signaux high-speed et devices de forte puissance. Un matériau unique ne suffit généralement pas.

La stratégie **Hybrid stack-up (Rogers+FR-4)** est alors très pertinente : matériaux low-loss (Rogers, Megtron series) pour les couches critiques, FR-4 pour power/ground et couches low-speed.

Intégrer **Copper coin** dans un **Hybrid stack-up (Rogers+FR-4)** permet de concilier performance et coût :
1.  **Performance maximale :** router les differential pairs 56G/112G+ sur Rogers pour réduire insertion loss et dispersion, pendant que **Copper coin** extrait la chaleur des ASIC/FPGA sur le top.
2.  **Coût maîtrisé :** n’utiliser le low-loss coûteux que là où c’est nécessaire.
3.  **Intégration :** définir précisément thickness, embed depth et relation aux couches. La surface du bloc doit être coplanaire (Co-planarity) au cuivre externe pour assurer une soudure BGA fiable.

Dans les zones BGA denses autour du bloc, **Via-in-Pad plated over (VIPPO)** est également crucial. VIPPO place des vias directement dans les pads, les remplit de résine conductrice et replaque pour une surface plane. Cela réduit la longueur de routing et les parasites L/C, et aide le fan-out haute densité. L’ensemble **Copper coin** + **Hybrid stack-up (Rogers+FR-4)** + **Via-in-Pad plated over (VIPPO)** constitue la “triade” des [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb) modernes.

<div style="background: #ffffff; border: 1px solid #d1c4e9; border-top: 6px solid #673ab7; border-radius: 16px; padding: 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 10px 30px rgba(103,58,183,0.08);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 30px 0; font-size: 1.6em; font-weight: 800; border-bottom: 2px solid #b39ddb; padding-bottom: 15px; display: flex; align-items: center; justify-content: center;">🔥 Copper Coin : points clés design & thermal management</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">📍 Planification physique early</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Définir tôt la géométrie et l’embed depth du <strong>Copper Coin</strong>. Le traiter comme contrainte mécanique (Mechanical Constraint) et l’aligner précisément au Thermal Pad du power device.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🛤️ Signal et return path</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Éviter de router des signaux high-speed au-dessus des gaps entre le bloc et le reference plane. Placer des <strong>Stitch Vias</strong> en périphérie pour assurer la continuité du return path et éviter une émission <strong>EMI</strong> excessive.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🌡️ Optimisation TIM</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Utiliser un <strong>TIM</strong> à haute conductivité entre le package et le bloc. Contrôler strictement la <strong>Bondline Thickness (BLT)</strong> pour minimiser la résistance de contact et exploiter la conductivité du cuivre.</p>
</div>
<div style="background: #ede7f6; border: 1px solid #d1c4e9; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🏭 Alignement manufacturing (HILPCB)</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Échanger tôt avec <strong>Highleap PCB Factory</strong> : <strong>Coin Coplanarity</strong>, contrôle des débordements d’adhésif après press-fit, et risque de mismatch <strong>CTE</strong> entre matériaux.</p>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: #e8eaf6; border-radius: 8px; border-left: 5px solid #3f51b5; font-size: 0.88em; color: #283593; line-height: 1.6;">
<strong>Insight technique :</strong> comparé à un thermal via array classique, un Copper Coin embedded peut améliorer l’efficacité de transfert thermique de <strong>10×+</strong>. Pour des RF power amplifiers <strong>GaN</strong> à très forte power density, les solutions T-Coin ou I-Coin sont souvent la meilleure voie pour dissiper les transitoires à l’échelle milliseconde.
</div>
</div>

### Copper pillar vs Copper coin : différences et choix

En matière de structures thermiques métalliques internes, **Copper pillar** est aussi souvent cité. Malgré l’usage du cuivre dans les deux cas, la structure, les applications et les procédés diffèrent.

-   **Définition et structure :**
    -   **Copper coin :** bloc massif pré-usiné, embedded via press-fit/bonding ; généralement grand et couvre la footprint du package.
    -   **Copper pillar :** colonnes de cuivre obtenues par plating, plus petites et souvent en arrays denses ; colonnes solides ou vias remplis de cuivre.

-   **Applications principales :**
    -   **Copper coin :** point cooling d’un device de forte puissance (transfert thermique “macro”).
    -   **Copper pillar :** thermal management fin et interconnect vertical ; courant en HDI ou IC substrates comme chemins conductifs/thermiques, ou micro arrays sous la puce.

-   **Guide de sélection :**
    -   Pour un BGA avec TDP > 100W, **Copper coin** est le choix évident.
    -   Pour des devices low-power dispersés (ex. QFN power IC) ou des zones extrêmement denses nécessitant à la fois interconnect vertical et conduction thermique, **Copper pillar** est souvent plus adapté.
    -   Combinaison possible : **Copper coin** pour la dissipation principale, **Copper pillar** pour des hotspots locaux.

En résumé, **Copper coin** est l’“artillerie lourde” pour le cœur thermique ; **Copper pillar** est la solution “de précision” pour les besoins électro-thermiques distribués.

### Manufacturing et quality control d’un Copper coin PCB

Embedded un gros bloc métallique dans un [multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) de précision est complexe. Le succès dépend de la précision de procédé et du QC. Highleap PCB Factory (HILPCB) a une forte expérience sur **Copper coin**.

Étapes clés :

1.  **Cavity routing :** CNC haute précision pour usiner une cavity dans un stack partiellement laminé ; la profondeur conditionne la coplanarity finale.
2.  **Fabrication et surface treatment :** usinage au micron ; surface treatment (ex. ENIG) pour assurer bonding et soudabilité.
3.  **Press-fit & bonding :** insertion du bloc ; interference fit et/ou adhésif haute conductivité. Température et pression doivent être contrôlées pour préserver le matériau.
4.  **Planarization :** grinding/polishing pour atteindre la coplanarity requise (souvent ±1 mil) pour la soudure BGA.
5.  **Lamination et plating ultérieurs :** après embedding, on poursuit lamination, drilling et plating, en contrôlant chimie et température pour éviter toute dégradation de l’interface.

Le QC couvre tout le flux : inspection X-Ray pour la connectivité et l’absence de voids, cross-section pour la qualité d’interface, profilométrie pour la coplanarity. Pour **Heavy copper 3oz+**, HILPCB dispose de lignes dédiées d’etching et de plating pour garantir précision et uniformité du thick copper.

<div style="background-color: #1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align: center; color: #FFFFFF;">HILPCB : capacités de procédé avancées</h3>
<table style="width:100%; border-collapse: collapse; text-align: center;">
<thead style="background-color: #3F51B5;">
<tr>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Paramètre</th>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Capacité HILPCB</th>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Intérêt pour Copper Coin</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Max layers</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">64 layers</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Support de backplanes high-speed et cartes serveurs complexes</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Copper thickness range</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">0.5oz - 20oz</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Support complet pour Heavy copper 3oz+ et au-delà</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Précision impedance control</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">±5%</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Controlled impedance fiable pour les canaux high-speed</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Min mechanical drill</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">0.15mm</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Support HDI et Via-in-Pad fins</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Contrôle coplanarity</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">±0.025mm (1 mil)</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Fiabilité de soudure BGA et connecteurs HF</td>
</tr>
</tbody>
</table>
</div>

### Simulation : prédire précisément les performances du Copper coin

Vu l’impact de **Copper coin** et son coût, la multi-physics simulation avant fabrication est indispensable pour valider le design, détecter les risques tôt et éviter des respins coûteux.

Deux dimensions principales :

1.  **Thermal simulation :**
    -   **Objectif :** prédire la junction temperature, la distribution thermique sur le PCB et les heat flow paths.
    -   **Outils :** Ansys Icepak, Flotherm, SimScale, etc.
    -   **Inputs clés :** modèles 3D précis (stack-up, **Copper coin**, package, TIM, heatsink), propriétés thermiques, puissance dissipée et environnement.
    -   **Sorties :** valider la dissipation, optimiser la géométrie et dimensionner la solution de cooling externe.

2.  **Electromagnetic simulation :**
    -   **Objectif :** évaluer l’impact sur SI et PI.
    -   **Outils :** Ansys HFSS, CST Microwave Studio, Keysight ADS, etc.
    -   **SI :** extraire S-parameters de transmission lines incluant **Copper coin**, analyser insertion/return loss et crosstalk, et vérifier les nets proches du bord pour maintenir **Controlled impedance**.
    -   **PI :** analyser la courbe d’impédance PDN et valider la réduction de bruit via un ground path à faible impédance.

La simulation respecte “Garbage In, Garbage Out” : matériaux, géométrie et settings doivent refléter la fabrication réelle. HILPCB peut fournir un DFM review et intégrer tolérances/bases matériaux dans vos modèles pour maximiser la corrélation au produit final.

### Perspectives : Copper coin pour data centers et AI hardware

Avec la hausse continue de la power density, des puces à 300W voire 500W deviendront courantes. Dans ce contexte, **Copper coin** devient incontournable.

-   **Next-gen data centers :** en SerDes 224G+, les budgets loss/jitter sont extrêmement serrés. En stabilisant la température, **Copper coin** contribue à la stabilité des matériaux low-loss comme **Hybrid stack-up (Rogers+FR-4)**, et sécurise les backplanes long-reach (LR) et les interconnects d’optical modules.
-   **AI/HPC accelerators :** GPU et AI chips sont power-hungry. **Copper coin** est l’une des solutions PCB-level les plus efficaces pour soutenir des fréquences élevées en continu.
-   **CPO :** Co-Packaged Optics réduit la distance électrique mais augmente la heat flux density ; **Copper coin** et des techniques similaires sont au cœur des CPO substrates.
-   **Automotive electronics :** les besoins thermiques d’IGBT, LiDAR et domain controllers augmentent ; **Copper coin** a un fort potentiel en high-reliability.

Combiné à des procédés high-density comme **Via-in-Pad plated over (VIPPO)**, **Copper coin** supportera des packages avec plus de pins et un pitch plus fin, poussant la limite de performance.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**Copper coin** n’est pas seulement une méthode de refroidissement avancée : c’est une solution système qui influence fortement le design high-speed. Elle relie thermal management, SI et PI, et devient un outil incontournable pour la performance extrême. Du contrôle de **Controlled impedance**, au compromis coût/performance via **Hybrid stack-up (Rogers+FR-4)**, jusqu’à la haute densité grâce à **Via-in-Pad plated over (VIPPO)**, l’adoption réussie de **Copper coin** reflète la complexité du PCB moderne.

Cette puissance impose aussi des exigences élevées en manufacturing. Choisir un partenaire comme Highleap PCB Factory (HILPCB) est essentiel. Nous fabriquons des [Heavy copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb) conformes aux spécifications les plus strictes et proposons des services complets : design review, support de simulation et [turnkey PCBA assembly](https://hilpcb.com/en/products/turnkey-assembly), pour transformer votre innovation en produit fiable.

Si vous développez des produits high-performance de nouvelle génération et faites face à des défis thermiques et SI, contactez nos experts techniques. Explorons ensemble comment **Copper coin** peut donner à votre produit un “core” puissant et cool.


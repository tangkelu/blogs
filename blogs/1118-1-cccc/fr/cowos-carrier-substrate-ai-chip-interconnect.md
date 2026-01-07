---
title: "CoWoS carrier substrate : Packaging, PDN et high-speed interconnect pour systèmes AI chiplet"
description: "Approfondissement sur CoWoS carrier substrate : SI/PI, thermique, contraintes de routing/stack-up, DFM et fiabilité pour des solutions d’AI chip interconnect et de substrate PCB performantes."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["CoWoS carrier substrate", "CoWoS carrier substrate layout", "CoWoS carrier substrate routing", "data-center CoWoS carrier substrate", "CoWoS carrier substrate checklist", "CoWoS carrier substrate impedance control"]
---
Avec l’essor explosif de l’AI et du HPC, la demande de calcul croît de façon exponentielle. Pour dépasser les limites physiques de la Moore’s Law, l’industrie bascule vers l’intégration hétérogène basée sur des architectures Chiplet et le packaging avancé 2.5D/3D. Parmi ces solutions, CoWoS (Chip-on-Wafer-on-Substrate) de TSMC s’est imposé comme un standard de fait pour les accélérateurs AI haut de gamme (ex. NVIDIA H100/B200). Dans cette architecture complexe, le **CoWoS carrier substrate** joue le rôle de pont entre le silicium et l’extérieur : sa qualité de design et de fabrication conditionne performance, consommation et fiabilité.

Ce « substrate » n’est pas une simple carte. C’est un micro‑système qui doit assurer à la fois high-speed interconnect, PDN stable et chemins thermiques efficaces. Il supporte des AI SoC et stacks HBM de très grande valeur et doit garantir un transfert signal/puissance quasi parfait sur des dizaines de milliers d’interconnexions micrométriques. Le moindre défaut peut condamner un module coûteux. D’où l’importance de maîtriser les contraintes et la fabrication d’un **CoWoS carrier substrate**. Highleap PCB Factory (HILPCB), fort d’une expérience en advanced interconnect, fournit des solutions IC substrate pour aider les clients à relever ces défis.

## Quel est le rôle d’un CoWoS substrate et comment est-il structuré ?

Pour saisir son importance, il faut le replacer dans le système 2.5D. CoWoS s’appuie sur un Silicon Interposer pour intégrer latéralement plusieurs dies (SoC + HBM) à très haute densité. Mais cet interposer, grand et avec un CTE très différent de la PCB, ne peut pas être directement soudé sur une carte mère classique.

Le **CoWoS carrier substrate** devient alors un pont indispensable, avec trois fonctions clés :

1.  **Support mécanique et tampon de contraintes :** il fournit une plateforme rigide et agit comme couche intermédiaire pour réduire le mismatch entre Silicon Interposer (CTE ≈ 2.6 ppm/°C) et application PCB (CTE ≈ 17 ppm/°C), protégeant les micro‑joints lors des thermal cycles.

2.  **Fan‑out du signal (RDL) :** le pitch des Micro-bump sur l’interposer est très faible (40–50μm), tandis que le pitch des BGA balls sous le substrate est beaucoup plus grand (0.8–1.0mm). Les couches RDL internes réalisent le fan‑out du pas μm vers le pas mm.

3.  **Power delivery et dissipation :** l’AI chip demande des courants très élevés ; le substrate doit fournir un PDN à faible impédance de BGA à Micro-bumps et des chemins thermiques (Thermal Vias).

Structurellement, un CoWoS substrate typique est un Build-up haute densité sur matériaux avancés comme ABF (Ajinomoto Build-up Film). Les layer counts sont souvent 8–16 (ou plus), avec microvias denses, fine routing et grands plans d’alimentation/masse : le sommet de la fabrication [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb).

## Comment gérer les défis SI liés à HBM3/3e ?

HBM est devenu standard pour les accélérateurs AI. HBM3/3e dépasse 1.2TB/s par stack : des milliers de lignes fonctionnent en parallèle à haute fréquence. Les signaux passent de HBM à l’interposer puis via le **CoWoS carrier substrate** vers le SoC. La Signal Integrity (SI) est donc critique.

Principaux risques :

*   **Insertion Loss :** atténuation ; des matériaux à Dk/Df plus faibles réduisent la perte.
*   **Reflection :** les discontinuités d’impédance génèrent des réflexions.
*   **Crosstalk :** couplage entre lignes voisines.

Un bon **CoWoS carrier substrate layout** suit des règles strictes :

D’abord, **CoWoS carrier substrate impedance control** est la base. Les chemins doivent être en impédance contrôlée (50Ω ou selon le standard). Il faut calcul précis de width, épaisseur diélectrique et distance aux reference planes. Des outils comme l’online impedance calculator de HILPCB aident tôt.

Ensuite, length matching et minimisation de longueur. Le bus HBM exige un mismatch très faible entre DQ et DQS pour limiter le skew. Et le chemin BGA → interposer doit rester le plus court possible.

Enfin, contrôler le crosstalk : augmenter les espacements, insérer des ground shields et optimiser le stack‑up. Une Stripline entre deux ground planes fournit une excellente protection, indispensable pour **CoWoS carrier substrate routing**.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color:#000000; border-bottom: 3px solid #64B5F6; padding-bottom: 10px;">Évolution des exigences SI HBM : impact substrate</h3>
<table style="width:100%; border-collapse: collapse; text-align:center; color:#000000;">
<thead style="background-color:#F5F5F5; color:#000000;">
<tr>
<th style="padding:12px; border: 1px solid #ddd;">Indicateur</th>
<th style="padding:12px; border: 1px solid #ddd;">HBM2e</th>
<th style="padding:12px; border: 1px solid #ddd;">HBM3/3e</th>
<th style="padding:12px; border: 1px solid #ddd;">Impact sur CoWoS substrate</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Débit par pin</td>
<td style="padding:12px; border: 1px solid #ddd;">~3.6 Gbps</td>
<td style="padding:12px; border: 1px solid #ddd;">~9.0 Gbps+</td>
<td style="padding:12px; border: 1px solid #ddd; color:#1E3A8A;">Sensibilité accrue au loss du matériau et précision d’impédance</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Largeur du bus</td>
<td style="padding:12px; border: 1px solid #ddd;">1024-bit</td>
<td style="padding:12px; border: 1px solid #ddd;">1024-bit</td>
<td style="padding:12px; border: 1px solid #ddd;">Routing density très élevée ; crosstalk plus difficile</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Tolérance d’impédance</td>
<td style="padding:12px; border: 1px solid #ddd;">±10%</td>
<td style="padding:12px; border: 1px solid #ddd;">±7% ou plus strict</td>
<td style="padding:12px; border: 1px solid #ddd; color:#1E3A8A;">Nécessite des process plus avancés et un meilleur contrôle</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Budget insertion loss canal</td>
<td style="padding:12px; border: 1px solid #ddd;">Relativement souple</td>
<td style="padding:12px; border: 1px solid #ddd;">Extrêmement strict</td>
<td style="padding:12px; border: 1px solid #ddd;">Matériaux ultra low‑loss (ex. ABF) indispensables</td>
</tr>
</tbody>
</table>
</div>

## Pourquoi le PDN est-il critique pour les AI chips ?

Si la SI est l’« autoroute » des données, la Power Integrity (PI) est le « socle ». Les AI chips peuvent exiger des transient currents très élevés (haut di/dt). Un PDN faible entraîne IR Drop et Ground Bounce, dégradant performance ou provoquant des crashes.

Objectif PDN d’un **CoWoS carrier substrate** : maintenir une impédance très faible de BGA à Micro-bumps sur toute la bande, via co‑design :

*   **Plans basse impédance :** réserver des layers power/ground et les garder continus.
*   **Stratégie Decap :** gros condensateurs près du BGA pour basse fréquence, petits près du die pour haute fréquence ; optimisation via PI simulation.
*   **Réduction de loop inductance :** rapprocher les vias power/ground, critique pour `data-center CoWoS carrier substrate`.

Pour des `data-center CoWoS carrier substrate` >1000W, le PDN est aussi un sujet thermique : courants élevés → Joule heating ; PDN et thermique doivent être co‑designés.

## Quelles stratégies thermiques pour un CoWoS substrate ?

La thermique est l’un des défis majeurs du packaging AI. 1000W+ sur quelques centaines de mm² implique un heat flux extrême. Le **CoWoS carrier substrate** est un chemin important de conduction et impacte la température maximale et la fiabilité.

Stratégie efficace = multi‑chemins :

1.  **Chemin principal (haut) :** via die, TIM et heat spreader (lid) vers cooling externe.
2.  **Chemin secondaire (bas) :** via Micro-bumps/interposer vers le **CoWoS carrier substrate**, puis via BGA vers la system board ; utile pour réduire la température HBM.

Optimisations substrate :

*   **Thermal Vias :** matrices denses sous le die, vias remplis pour transférer la chaleur vers le bas.
*   **Matériaux conductifs :** diélectriques et copper foils à meilleure conductivité.
*   **Optimisation des plans cuivre :** conserver du cuivre dans les limites électriques.
*   **Co‑simulation :** thermal co‑simulation chip‑package‑substrate‑system pour dimensionner les vias et prévenir les hot spots.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🛠️ CoWoS substrate : checklist de sign‑off ingénierie</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Vérifications de contraintes physiques système pour packaging 2.5D à interconnexions denses</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. SI & domaine fréquentiel</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Points :</strong> tolérance impédance diff ≤ ±5% ? simulation **CoWoS carrier substrate impedance control** pour 112G/224G ? S‑parameters (IL/RL) avec margin au‑delà de 28GHz ?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. PI & réponse PDN</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Points :</strong> Target Impedance PDN compatible avec transient currents extrêmes ? inductance de montage Decap minimisée via **ESR/ESL modeling** ?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Heat flux & simulation thermique</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Points :</strong> couverture de la matrice Thermal Via suffisante pour 500W+ ? **CFD thermal-flow simulation** réalisée pour prévenir les hot spots et le throttling ?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. DFM & contraintes mécaniques</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Points :</strong> min L/S dans les limites fournisseur ? stack‑up en vraie <strong>symétrie miroir</strong> pour contrôler Warpage ?</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-right: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Insight HILPCB :</strong> le <strong>CTE matching</strong> est la ligne de vie de la fiabilité. Comme le substrate supporte un Silicon Interposer, choisir des matériaux package-grade à haut module et bas CTE (ABF ou BT avancé) réduit le stress sur les Micro-bumps lors des thermal cycles.
</div>
</div>

## Quelles contraintes de fabrication pour stack-up et routing ?

Un design théorique doit respecter des limites process réelles. La production de **CoWoS carrier substrate** est au sommet du [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) et de la technologie IC substrate ; les règles DFM sont strictes.

Contraintes principales :

*   **Fine line :** RDL nécessite L/S très fins (10μm/10μm ou moins).
*   **Microvia :** laser microvias, pad size et stacking (Stacked vs. Staggered) sont limités par le process ; stacked microvias économisent de la place mais exigent un alignement et un via‑fill très maîtrisés.
*   **Warpage :** grands substrates (100mm x 100mm+) sensibles au warpage ; stack-up doit être symétrique (cuivre et diélectriques).
*   **Handling matériaux :** ABF est sensible à température/humidité/cleanliness.

Une stratégie **CoWoS carrier substrate routing** réussie satisfait les contraintes électriques tout en contournant les goulots d’étranglement de fabrication, via une collaboration précoce avec un fabricant tel que HILPCB. Le team DFM peut identifier les risques et optimiser **CoWoS carrier substrate layout** pour équilibrer performance, coût et yield.

## Comment assurer la fiabilité long terme ?

Pour des AI servers 7x24, la fiabilité est vitale. La moindre défaillance du **CoWoS carrier substrate** est catastrophique. Les risques proviennent du mismatch matériaux et de la dégradation :

*   **Contraintes thermo‑mécaniques :** mismatch CTE entre silicium/substrate/PCB ; thermal cycling → fatigue et cracks.
*   **Microvia reliability :** interface cracks et opens intermittents.
*   **Electromigration :** migration d’ions sous forte current density, amincissant les conducteurs.

Une discipline IPC/JEDEC est indispensable : matériaux validés, éviter les stress concentrators, et tests comme TCT, HAST et drop. Une **CoWoS carrier substrate checklist** doit inclure ces validations.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color:#FFFFFF; border-bottom: 2px solid #90CAF9; padding-bottom: 10px;">Matrice de capacités HILPCB (IC substrate avancé)</h3>
<table style="width:100%; border-collapse: collapse; text-align:center; color:#FFFFFF;">
<thead style="background-color:rgba(255, 255, 255, 0.1); color:#FFFFFF;">
<tr>
<th style="padding:12px; border: 1px solid #424242;">Paramètre</th>
<th style="padding:12px; border: 1px solid #424242;">Capacité HILPCB</th>
<th style="padding:12px; border: 1px solid #424242;">Valeur pour CoWoS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Nombre de layers max</td>
<td style="padding:12px; border: 1px solid #424242;">Jusqu’à 56 layers</td>
<td style="padding:12px; border: 1px solid #424242;">PDN complexes et routing dense</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Min line/space</td>
<td style="padding:12px; border: 1px solid #424242;">8μm / 8μm</td>
<td style="padding:12px; border: 1px solid #424242;">RDL ultra dense, interface HBM</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Diamètre laser microvia</td>
<td style="padding:12px; border: 1px solid #424242;">Min 50μm</td>
<td style="padding:12px; border: 1px solid #424242;">Interconnexions inter-layer haute densité</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Précision impedance control</td>
<td style="padding:12px; border: 1px solid #424242;">±5%</td>
<td style="padding:12px; border: 1px solid #424242;">Supporte **CoWoS carrier substrate impedance control**</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Matériaux core</td>
<td style="padding:12px; border: 1px solid #424242;">ABF / BT / Low-Loss Materials</td>
<td style="padding:12px; border: 1px solid #424242;">Bonnes performances high-speed et thermiques</td>
</tr>
</tbody>
</table>
</div>

## Choix du fournisseur : quels critères ?

Vu la complexité du **CoWoS carrier substrate**, le choix du partenaire est déterminant :

1.  **Profondeur technique :** expérience IC substrate (ABF build-up) ? compréhension SI/PI type [High-speed PCB](https://hilpcb.com/en/products/high-speed-pcb) ? références `data-center CoWoS carrier substrate` ?
2.  **Capacité process :** LDI, vacuum etching, alignement, tolérances d’impédance et gestion yield.
3.  **Qualité :** ISO 9001, IATF 16949, AOI, X-Ray, cross‑section.
4.  **Supply chain :** ABF souvent contraint ; résilience nécessaire.
5.  **Service collaboratif :** DFM, simulations, et [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly).

Avec plus de dix ans d’expérience en PCB haut de gamme et IC substrate, HILPCB est un partenaire pertinent pour des programmes AI next‑gen.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**CoWoS carrier substrate** est bien plus qu’une « connection board » : c’est la fondation de précision de la compute AI moderne. Entre les signaux HBM3/3e multi‑TB/s, l’alimentation propre pour du silicium >1000W et la tenue au thermal cycling, chaque défi se situe au plus haut niveau d’ingénierie.

Un **CoWoS carrier substrate** performant et fiable exige des compétences transverses en SI, PI, thermique, matériaux et precision manufacturing, et une collaboration étroite avec un fabricant à la fois capable et rigoureux. L’importance stratégique du **CoWoS carrier substrate** ne fera qu’augmenter avec la demande d’advanced packaging.


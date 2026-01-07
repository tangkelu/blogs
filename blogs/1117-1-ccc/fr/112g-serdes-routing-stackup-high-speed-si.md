---
title: "112G SerDes routing stackup : relever la stabilité des liens ultra-high-speed et les défis low-loss des PCB high-speed SI"
description: "Un deep dive sur 112G SerDes routing stackup—Channel Budget, sélection de matériaux low-loss, impedance/crosstalk control, transitions via/connector, equalization/jitter et trade-offs DFM pour les PCB high-speed SI."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["112G SerDes routing stackup", "112G SerDes routing reliability", "112G SerDes routing low volume", "low-loss 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing quick turn"]
---
Avec la demande explosive de bande passante des data centers, de l’AI et des 5G communications, les débits sont entrés dans l’ère des 112Gbps/s. Dans ce contexte, la technologie 112G SerDes est devenue un core enabler de l’interconnexion high-speed de nouvelle génération. Mais à cette vitesse, le PCB design et le manufacturing font face à des défis sans précédent. Un **112G SerDes routing stackup** bien conçu n’est plus « juste une lamination » : c’est du systems engineering qui combine materials science, théorie électromagnétique et precision fabrication. Il détermine directement la signal integrity, la stabilité du lien et, au final, le succès du produit.

Cet article sert de **112G SerDes routing guide** détaillé du point de vue du design des connector et via-transitions. Nous couvrons tout, du Channel Budget à la sélection des matériaux, jusqu’à la manufacturability, pour vous aider à naviguer dans cet espace complexe. Pour les équipes qui construisent des [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb) de pointe, maîtriser un **112G SerDes routing stackup** optimisé est un prérequis. Highleap PCB Factory (HILPCB) s’appuie sur une forte expérience high-speed pour accompagner les clients du prototype au volume.

### Pourquoi le 112G SerDes Channel Budget est-il si strict ?

En design 112G SerDes, tout commence par le Channel Budget. Le Channel Budget définit la perte de signal maximale admissible et la noise margin sur le lien physique du transmitter (Tx) au receiver (Rx). Par rapport aux générations précédentes (28G/56G), le budget 112G est extrêmement serré—principalement parce qu’il utilise le PAM4 signaling.

Le PAM4 transporte 2 bits par symbol, ce qui divise la baud rate par deux et réduit une partie de la pression de bande passante, mais il réduit la SNR d’environ ~9.5dB et augmente fortement la sensibilité au noise et à l’atténuation. La fréquence de Nyquist du 112G PAM4 atteint 28 GHz. À cette fréquence, les PCB traces, vias et connectors introduisent une Insertion Loss (IL) importante.

Un channel 112G typique inclut plusieurs éléments, chacun consommant un loss budget précieux :
*   **ASIC package :** Substrate traces et vias dans le BGA package, premiers contributeurs de loss.
*   **PCB traces :** principale source de loss—due au dielectric loss, au conductor loss (skin effect et copper roughness) et à la longueur des traces.
*   **Vias :** through/blind/buried vias sont de fortes impedance discontinuities qui ajoutent reflection et perte supplémentaire, surtout sur les grandes [backplane PCB](https://hilpcb.com/en/products/backplane-pcb).
*   **Connectors :** les connectors high-speed tels que QSFP-DD et OSFP doivent être modélisés avec précision, y compris la PCB launch region.
*   **Cable assembly (optionnel) :** en rack-to-rack interconnect, le cable et ses connectors font aussi partie du channel.

La total channel insertion loss est généralement limitée à ~30–35dB (@28GHz). Une perte excessive sur un seul élément peut empêcher le link bring-up ou pousser le BER hors spécifications. Un channel modeling précis et une budget allocation rigoureuse sont donc la première—et la plus critique—étape du design **112G SerDes routing stackup**.

### Comment choisir les bons matériaux low-loss ?

La sélection des matériaux est la base du **low-loss 112G SerDes routing**. À 28GHz, la perte du FR-4 traditionnel est inacceptable, donc des laminates low-loss ou ultra-low-loss conçus pour les applications high-speed sont nécessaires. Les métriques principales sont Dk et Df.

*   **Dk :** impacte la propagation speed et la characteristic impedance. En high-speed design, on recherche un Dk stable sur la fréquence pour réduire la dispersion. Un Dk plus faible permet aussi des traces plus larges, ce qui réduit le conductor loss.
*   **Df :** quantifie directement le dielectric loss. Pour le 112G SerDes, le Df à 28GHz devrait être inférieur à 0.004—souvent plus proche de 0.002.

Au-delà de Dk/Df, deux autres facteurs comptent tout autant :

1.  **Fiber Weave Effect :** la structure périodique du fiberglass weave crée des non-uniformités locales de Dk. Quand la longueur de trace devient comparable au weave pitch, des variations d’impédance et du skew peuvent dégrader le differential signaling. Mitigations courantes :
    *   Utiliser des glass styles plus « plats » (ex. 1078, 1067).
    *   Utiliser du Mechanically Spread Glass.
    *   Router avec un léger angle (ex. 1–5°) par rapport au weave pour éviter un alignement parallèle.

2.  **Copper Roughness :** à haute fréquence, le skin effect force le courant à circuler à la surface du conducteur. Un copper rugueux augmente la longueur effective du chemin et le conductor loss. Utilisez un copper très lisse type VLP ou ULP ; le Rq typique doit être inférieur à 2 µm.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#000000;">Comparatif de performance des matériaux high-speed PCB</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Classe matériau</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Dk typique (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Df typique (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Target data rate</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Indice coût</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Standard FR-4</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">4.2 - 4.8</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.015 - 0.020</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">1x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Mid-loss materials</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.6 - 4.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.008 - 0.012</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">10 - 28 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">2x - 3x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Low-loss (e.g., Megtron 6)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.2 - 3.6</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.002 - 0.004</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">28 - 112 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">5x - 8x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Ultra-low-loss (e.g., Tachyon 100G)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 3.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">112 Gbps and above</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">> 10x</td>
</tr>
</tbody>
</table>
</div>

### Quelles stratégies clés pour l’impedance control et le crosstalk management ?

Dans **112G SerDes routing stackup**, une impedance control précise et une suppression stricte du crosstalk sont deux piliers supplémentaires de la qualité du signal.

**Impedance control :**
La differential impedance est typiquement 100Ω ou 90Ω, avec une tolérance aussi serrée que ±7% voire ±5%. Toute déviation géométrique de l’impédance cible crée des reflections, augmentant insertion loss et jitter. Facteurs clés :
*   **Trace width and thickness :** l’etch accuracy en manufacturing détermine la linewidth finale.
*   **Dielectric thickness :** le contrôle du PP (Prepreg) thickness post-lamination est critique.
*   **Material Dk :** la simulation doit utiliser le Dk fourni par le laminate supplier en tenant compte du resin content et des lamination conditions.

**Crosstalk management :**
Le crosstalk est du noise causé par l’EM coupling entre traces adjacentes. Dans les systèmes 112G PAM4 où la SNR est déjà faible, le crosstalk est souvent le #1 killer. Stratégies courantes :
*   **Augmenter le spacing :** le spacing differential-pair-to-pair est souvent recommandé à 3W ou plus ; sur les liens critiques, 5W ou plus peut être nécessaire.
*   **Reference-plane continuity :** garantir des reference GND/power planes continus sous le high-speed routing ; éviter de traverser des plane splits.
*   **Routage orthogonal entre signal layers adjacents :** les directions de routage doivent être perpendiculaires pour minimiser le broadside coupling.
*   **Ground-via shielding :** placer des Stitching Vias autour des differential pairs pour un effet Faraday-cage et isoler le noise.

Un crosstalk control efficace doit démarrer dès le stackup planning, avec des 3D full-wave EM simulators (ex. Ansys HFSS, CST) pour une prédiction et une optimisation précises.

### Quelle importance pour l’optimisation des transitions connector et vias ?

En tant que spécialiste du design des transitions connector/via, je peux l’affirmer : à 112G, la qualité des transitions fixe directement la limite supérieure de la channel performance. Un via ou un connector pad non optimisé peut facilement consommer plusieurs dB du budget via loss et reflection.

**Via optimization :**
Une via est une structure 3D complexe. Sa parasitic capacitance et son inductance créent des impedance discontinuities sévères à 28GHz. Tactiques clés :
*   **Back-drilling :** une des techniques les plus importantes. En perçant depuis l’arrière pour retirer l’unused via stub, on supprime des résonances à quarter-wavelength et on améliore nettement insertion loss et reflection. Le contrôle de profondeur de backdrill est un indicateur clé de la capability d’un fabricant.
*   **Anti-pad optimization :** agrandir l’ouverture anti-pad dans les reference planes réduit la parasitic capacitance de la via et rapproche l’impédance de la transmission line.
*   **Remove NFP :** supprimer les Non-Functional Pads sur les couches internes réduit la parasitic capacitance et améliore encore la performance.
*   **Utiliser la technologie [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) :** microvias et pads plus petits réduisent fortement la taille physique et les parasitics.
*   **Ground-via co-design :** placer 1–2 anneaux de ground vias autour de la signal via pour fournir un low-inductance return path et réduire le coupling.

**Connector optimization (Launch Tuning) :**
Les arrays de pins des connectors high-speed (ex. QSFP-DD) sont extrêmement denses, rendant le design de pad et de fan-out difficile. Une 3D simulation est nécessaire pour affiner pad shapes, trace widths et reference-plane openings afin de matcher l’impedance du connector et d’obtenir une transition smooth.

<div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(49, 27, 146, 0.1);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🧬 Via transitions : matrice d’optimisation pour les liens verticaux high-speed</h3>
<p style="text-align: center; color: #673ab7; font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Éliminer impedance jumps et parasitics pour protéger la signal integrity 112G+</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">01. Mandatory Backdrill et stub removal</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Retirer complètement les via stubs pour éliminer les points de résonance à haute fréquence. Au-delà de 28Gbps, garder la stub length strictement dans <strong>< 10 mil</strong> pour maintenir la linéarité de bande passante.</p>
</div>
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">02. Remove Non-functional Pads</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Supprimer les pads internes inutiles. Réduire la parasitic capacitance améliore le comportement TDR et diminue la reflection au niveau de la transition via.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">03. Design Anti-pad précis</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Utiliser un 3D full-wave solver pour optimiser les dimensions Anti-pad. Ajuster via-to-plane spacing pour compenser l’inductance locale et garantir une <strong>impedance continuity</strong> dans la transition verticale.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">04. Enclosure ground-via de type coaxial-like</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Placer des <strong>GND Stitching Vias</strong> symétriquement autour des signal vias pour former un return path coaxial-like, isoler le via crosstalk et réduire la return-loop inductance.</p>
</div>
</div>
<div style="margin-top: 30px; padding: 25px; background: #f1f5f9; border-radius: 16px; border-left: 8px solid #334155;">
<strong style="color: #1e293b; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 Connector Launch Tuning:</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;">Fine-tune de la fanout region pour un connector spécifique (ex. QSFP-DD ou PCIE 6.0). En ajustant pad edges et lamination gaps vers le reference plane, assurer une transition d’impédance smooth du routage horizontal vers le connector vertical et minimiser la <strong>Total Insertion Loss</strong>.</p>
</div>
<div style="margin-top: 20px; padding: 20px; background: linear-gradient(90deg, #311b92, #673ab7); border-radius: 12px; color: #ffffff; text-align: center; font-size: 0.92em;">
💡 <strong>HILPCB manufacturing note:</strong> La backdrill depth tolerance impacte directement le comportement du lien 112G. Nous utilisons un advanced laser depth-control system pour maintenir la <strong>Backdrill Tolerance à ±2 mil</strong>, réduisant fortement la reflection loss à haute fréquence.
</div>
</div>

### Comment equalization et jitter affectent-ils la performance du lien SerDes ?

Même avec un **112G SerDes routing stackup** optimisé, il reste du channel loss. Les SerDes modernes intègrent des circuits d’Equalization puissants pour compenser. Blocs courants :
*   **Tx FFE :** la pre-emphasis booste les composantes high-frequency pour contrer le comportement low-pass du channel.
*   **Rx CTLE :** un amplificateur programmable qui renforce sélectivement le high-frequency pour lisser la channel response.
*   **Rx DFE :** un equalizer non linéaire qui annule l’ISI des symbols précédents.

L’objectif côté PCB est de fournir un channel « smooth et prévisible ». Une réponse remplie de résonances et de discontinuités abruptes rend les equalizers difficiles à converger—ou peut conduire à l’échec.

Le jitter est une déviation temporelle et un autre ennemi majeur des liens high-speed. Sources de jitter côté PCB :
*   **Fiber weave effects dans le matériau.**
*   **Reflections issues d’impedance discontinuities.**
*   **Power Supply Noise :** le PDN noise se couple via les SerDes power pins dans le signal et crée du jitter—ce qui souligne l’importance du co-design SI/PI.

Un stackup robuste réduit jitter et ISI à la couche physique, diminue la dépendance à l’Equalization du SerDes et améliore la **112G SerDes routing reliability** globale.

### Comment le DFM équilibre-t-il performance et coût ?

Un **112G SerDes routing stackup** théoriquement parfait est inutile s’il ne peut pas être fabriqué de façon économique et fiable. Le DFM doit être pris en compte tôt. Les engineers HILPCB insistent sur une implication early pour éviter les pièges de manufacturability.

Points DFM clés :
*   **Line width/spacing control :** les designs 112G requièrent souvent 3/3mil (~75/75μm) ou plus fin, ce qui impose des exigences élevées sur imaging et etching.
*   **Drilling accuracy :** les PCBs à grand nombre de couches et à fort Aspect Ratio nécessitent une alignment accuracy très élevée en mechanical et laser drilling.
*   **Backdrill depth control :** la backdrill depth tolerance influence directement la stub length et exige des équipements avancés de contrôle Z-axis.
*   **Stackup symmetry :** pour réduire la lamination warpage, conserver un stackup aussi symétrique que possible.
*   **Surface finish :** à 28GHz, ENEPIG surpasse souvent ENIG grâce à une meilleure flatness, corrosion resistance et un meilleur comportement vis-à-vis du skin effect.

Dans les phases early—en particulier pour **112G SerDes routing quick turn**—une collaboration étroite avec un advanced manufacturer et une DFM review aident à éviter des redesigns tardifs coûteux et à accélérer le time to market.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#FFFFFF;">Aperçu des capabilities HILPCB en high-speed PCB manufacturing</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Process parameter</th>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max layer count</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Min line width/spacing</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">2.5 / 2.5 mil</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max Aspect Ratio</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Backdrill depth tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">+/- 2 mil (50μm)</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">±5%</td>
</tr>
</tbody>
</table>
</div>

### Comment assurer la long-term reliability du 112G SerDes routing ?

La **112G SerDes routing reliability** ne se limite pas aux objectifs électriques : elle vise une opération stable sur toute la product life. Points clés :

*   **Thermal management :** les 112G SerDes devices et optical modules dissipent une puissance importante ; le stackup doit fournir des heat paths efficaces. Ajouter des thermal reference planes, utiliser des matériaux à meilleure conductivité thermique et placer des thermal vias de façon stratégique aide à contrôler la température et éviter performance drop ou dommages permanents.
*   **Power Integrity (PI) :** un PDN stable et low-impedance est fondamental. Un bon decoupling placement, des power planes larges et un low-inductance via design suppriment le supply noise et fournissent un « clean power » pour le SerDes.
*   **CAF resistance :** sur des PCBs high-density avec de forts gradients de champ électrique, CAF est un failure mode potentiel. Sélectionner des matériaux high-CAF-resistance et utiliser des process drilling/plating optimisés est essentiel.
*   **Consistency testing :** en volume production, mettre en place des tests stricts—échantillonner la characteristic impedance via TDR et mesurer les S-parameters via VNA pour garantir la lot-to-lot consistency.

### Comment HILPCB supporte les prototypes low-volume et quick-turn ?

Nous savons que l’itération rapide et la prototype validation sont critiques pour le développement 112G SerDes. De nombreux projets démarrent avec des besoins **112G SerDes routing low volume**. HILPCB a construit un système de production flexible, de quelques prototypes jusqu’au full-scale volume.

Pour les projets **112G SerDes routing quick turn**, nous proposons :
*   **Expert DFM support :** stackup recommendations gratuites et DFM analysis avant commande pour équilibrer performance et manufacturability.
*   **Strong material inventory :** stock de laminates **low-loss 112G SerDes routing** mainstream (Isola, Rogers, Panasonic Megtron series, etc.) pour éviter de longs délais d’approvisionnement.
*   **Dedicated prototype line :** une ligne rapid-turn pour livrer des high-speed PCBs de haute qualité au plus vite.
*   **One-stop service :** au-delà de la PCB fabrication, nous supportons le component sourcing et la PCBA. Notre [turnkey assembly](https://hilpcb.com/en/products/turnkey-assembly) peut gérer la supply chain afin que vous vous concentriez sur la R&amp;D.

Que vous ayez besoin de cartes de validation **112G SerDes routing low volume** ou de commandes volume exigeantes, HILPCB dispose de la capability et de l’expérience pour être un partenaire fiable.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Construire un **112G SerDes routing stackup** robuste et fiable est un systems engineering complexe qui exige des trade-offs délicats entre SI, PI, thermal management et manufacturing. De l’analyse stricte du Channel Budget, au choix de matériaux low-loss, jusqu’à l’optimisation micron-level des vias et connector transitions—chaque détail compte.

À mesure que la technologie évolue vers 224G et au-delà, ces principes et défis ne feront que s’intensifier. Choisir un partenaire comme HILPCB—qui comprend à la fois la physique du design et le top-tier manufacturing—peut constituer un avantage décisif. Nous ne sommes pas seulement un fabricant, mais aussi un compagnon d’innovation technique, transformant les blueprints les plus exigeants en produits physiques high-performing. Si vous lancez votre prochain programme high-speed et avez besoin d’une solution **112G SerDes routing stackup** fiable, contactez nos experts techniques.


---
title: "Data-Center 112G SerDes Routing : Maîtriser les défis d'intégrité du signal ultra-haute vitesse et de faible perte pour PCB"
description: "Analyse approfondie de la technologie de base du data-center 112G SerDes routing, couvrant l'intégrité du signal haute vitesse, la gestion thermique et la conception d'alimentation/interconnexion, pour vous aider à créer des PCB haute performance à intégrité de signal élevée."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---

Avec la croissance explosive de l'intelligence artificielle (IA), de l'apprentissage automatique (ML) et du cloud computing, le trafic au sein des centres de données augmente à une vitesse sans précédent. Pour répondre à cette demande, l'industrie migre rapidement de la technologie 56G NRZ/PAM4 vers le 112G PAM4 SerDes. Ce saut double non seulement le débit par canal, mais apporte également des défis sans précédent en matière d'intégrité du signal (SI) pour la conception et la fabrication de PCB. Un **data-center 112G SerDes routing** réussi n'est plus une simple "connexion", mais une ingénierie système intégrant la science des matériaux, la théorie des champs électromagnétiques, la thermodynamique et la fabrication de précision. En tant qu'ingénieur en mesure et validation de conformité, je vais analyser en profondeur les difficultés fondamentales et les stratégies de réponse pour la conception de liaisons 112G SerDes du point de vue de la pratique.

Des traversées BGA du boîtier de la puce aux traces du PCB, en passant par les connecteurs et le fond de panier, pour atteindre enfin le récepteur, la performance de l'ensemble de ce canal physique détermine directement si le signal 112G peut être récupéré avec précision. Toute discontinuité d'impédance mineure, perte diélectrique excessive ou structure de via non optimisée peut entraîner une détérioration drastique du budget de liaison, causant finalement un taux d'erreur binaire (BER) catastrophique. Par conséquent, une stratégie complète de **high-speed 112G SerDes routing** doit intégrer dès le début de la conception des facteurs tels que la sélection des matériaux, la conception de l'empilement, le contrôle de l'impédance et les tolérances de fabrication, garantissant que le produit final répond non seulement aux performances électriques, mais possède également une haute fiabilité et une fabricabilité.

### Pourquoi le budget du canal 112G SerDes est-il si strict ?

Lorsque nous passons de 56G à 112G, nous ne sommes pas seulement confrontés au doublement de la fréquence d'horloge. La fréquence de Nyquist du signal 112G PAM4 (modulation d'amplitude d'impulsion à quatre niveaux) atteint 28 GHz, ce qui signifie que le signal est plus sensible à la perte de canal et au bruit pendant la transmission. Par rapport aux signaux NRZ (Non-Return-to-Zero) traditionnels, le diagramme de l'œil du signal PAM4 est compressé au tiers dans la direction verticale, réduisant considérablement la marge du rapport signal/bruit (SNR). Cela fait du budget de perte d'insertion totale (Insertion Loss, IL) du canal la contrainte la plus critique dans la conception du **data-center 112G SerDes routing**.

Un budget de perte totale typique pour une liaison 112G longue distance (LR) peut être limité à moins de 30-35dB @ 28GHz. Ce budget doit être réparti entre chaque composant du canal : boîtier de la puce, traces PCB, vias, connecteurs et boîtier du récepteur.

- **Perte d'insertion (IL)** : C'est le défi principal. À 28 GHz, les matériaux conventionnels comme le FR-4 ont des pertes énormes et ne peuvent pas répondre aux exigences. L'énergie du signal se dissipe sous forme de chaleur dans le diélectrique, entraînant une atténuation de l'amplitude du signal et la fermeture de l'œil.
- **Perte de retour (RL)** : Causée par des discontinuités d'impédance dans le canal, telles que les vias, les connecteurs, les plots BGA, etc. Le signal réfléchi se superpose au signal principal, formant une interférence inter-symboles (ISI), détériorant davantage la qualité du signal.
- **Diaphonie (Crosstalk)** : Le câblage haute densité rend le couplage électromagnétique entre les canaux adjacents extrêmement sévère. La diaphonie proche (NEXT) et la diaphonie lointaine (FEXT) réduisent directement le rapport signal/bruit au niveau du récepteur.
- **Marge de fonctionnement du canal (COM)** : En tant qu'indicateur d'évaluation de liaison plus avancé, le COM prend en compte de manière globale la perte d'insertion, la perte de retour, la diaphonie et la capacité de l'égaliseur (Equalizer), donnant finalement une valeur scalaire mesurant la qualité de la liaison. Dans la conception 112G, l'optimisation de la conception du canal par simulation COM est devenue la norme de l'industrie.

Pour respecter le budget de canal strict, les concepteurs doivent modéliser avec précision l'ensemble de la liaison dès la phase de simulation et travailler en étroite collaboration avec des fabricants expérimentés comme Highleap PCB Factory (HILPCB) pour s'assurer que le modèle de simulation correspond hautement aux résultats de fabrication réels.

### Sélection de matériaux à faible perte : La pierre angulaire de la liaison 112G

Les matériaux sont la base physique déterminant les performances des liaisons à haute vitesse. À une fréquence de 28 GHz, la constante diélectrique (Dk) et le facteur de perte (Df) des matériaux PCB jouent un rôle décisif dans l'atténuation du signal. Choisir le bon matériau à faible perte pour le **data-center 112G SerDes routing** est la première étape vers une conception réussie.

- **Constante diélectrique (Dk) et Facteur de perte (Df)** : Le Df est un indicateur clé mesurant la capacité du matériau à absorber l'énergie électromagnétique. Plus le Df est bas, plus la perte diélectrique du signal pendant la transmission est faible. Pour les liaisons 112G, il est généralement nécessaire de choisir des matériaux à perte ultra-faible (Ultra Low Loss) ou extrêmement faible (Extremely Low Loss) avec un Df inférieur à 0,004 @ 10 GHz, tels que Tachyon 100G, Megtron 6/7/8, série Rogers RO4000, etc. De plus, la stabilité et la cohérence du Dk sont cruciales pour le **112G SerDes routing impedance control**.
- **Effet de peau (Skin Effect)** : À une fréquence élevée comme 28 GHz, le courant a tendance à circuler à la surface du conducteur plutôt que de se répartir uniformément sur toute la section. Cela entraîne une augmentation de la résistance effective du conducteur, générant une perte de conducteur supplémentaire.
- **Rugosité de surface de la feuille de cuivre (Copper Roughness)** : Une surface de feuille de cuivre rugueuse augmentera la longueur du chemin de transmission du courant haute fréquence, exacerbant ainsi l'effet de peau et entraînant des pertes plus importantes. Par conséquent, dans la conception 112G, l'utilisation de feuilles de cuivre à profil ultra-bas (VLP) ou extrêmement bas (HVLP) est recommandée pour minimiser la perte de conducteur.
- **Effet de tissu de fibre de verre (Fiber Weave Effect)** : Le substrat PCB est un matériau composite constitué de tissu de fibre de verre et de résine. En raison des constantes diélectriques différentes du tissu de verre (Dk≈6) et de la résine (Dk≈3), lorsque la trace est parallèle aux faisceaux de fibres de verre, le Dk effectif ressenti changera localement, entraînant des fluctuations d'impédance et des écarts de timing (skew). Pour atténuer ce problème, on peut utiliser un tissu de verre aplati (Spread Glass) ou router les traces avec un angle minuscule (comme 1-5 degrés).

Le choix de la bonne combinaison de matériaux ne concerne pas seulement les performances, mais aussi le coût et la fabricabilité. Un excellent **112G SerDes routing guide** devrait conseiller aux concepteurs de communiquer avec les fabricants de PCB (comme HILPCB) dès le début du projet pour équilibrer les performances, les coûts et les risques liés à la chaîne d'approvisionnement.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Comparaison des performances des matériaux PCB haute vitesse</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Classe de matériau</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Matériau typique</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Facteur de perte (Df @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Constante diélectrique (Dk @ 10GHz)</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Débit applicable</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Perte standard</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Perte moyenne</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Faible perte</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Perte ultra-faible</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Contrôle précis de l'impédance et stratégie de routage

Le contrôle de l'impédance est au cœur de l'intégrité du signal haute vitesse. Dans le **high-speed 112G SerDes routing**, toute conception s'écartant de l'impédance cible (généralement 90 ou 100 ohms différentiels) entraînera une réflexion du signal, augmentant la gigue et l'interférence inter-symboles. Réaliser un **112G SerDes routing impedance control** précis nécessite d'agir à la fois sur la conception et la fabrication.

**Niveau conception :**
1.  **Conception précise de l'empilement** : Utiliser un solveur de champ 2D (comme Polar Si9000) ou intégré aux outils EDA pour calculer précisément l'impédance différentielle en fonction de la valeur Dk du matériau choisi, de l'épaisseur de couche, de la largeur de ligne, de l'espacement de ligne et de l'épaisseur de cuivre. Les tolérances de fabrication doivent être prises en compte et confirmées avec le fabricant pour sa plage de capacité de processus.
2.  **Géométrie des traces** :
    *   **Adaptation intra-paire différentielle** : La longueur des deux traces (P/N) de la paire différentielle doit être strictement adaptée pour éviter la conversion de bruit en mode commun et les écarts de timing. À un débit de 112G, la précision d'adaptation requise est généralement inférieure à 1-2 mil.
    *   **Éviter les virages à angle aigu** : Les virages de trace doivent utiliser des arcs ou des angles de 45 degrés, en évitant les angles droits de 90 degrés pour réduire la discontinuité d'impédance.
    *   **Continuité du plan de référence** : Les paires différentielles haute vitesse doivent avoir un plan de masse ou d'alimentation de référence continu. Le routage à travers des zones divisées causera des changements brusques d'impédance et de graves problèmes d'intégrité du signal.

**Niveau fabrication :**
La capacité de contrôle du processus par le fabricant détermine directement la précision finale de l'impédance. Des fabricants leaders comme Highleap PCB Factory (HILPCB) garantissent la cohérence de l'impédance grâce aux technologies suivantes :
- **Processus de gravure avancé** : Contrôle des tolérances de largeur et d'espacement de ligne dans une plage de ±5% ou même moins.
- **Contrôle précis du laminage** : Assurer une épaisseur uniforme et cohérente du noyau (Core) et du préimprégné (PP).
- **Test TDR** : Utiliser un réflectomètre dans le domaine temporel (TDR) pendant la production pour échantillonner ou inspecter entièrement les coupons de test (Test Coupon) afin de vérifier si l'impédance de la carte finie est dans les spécifications (par exemple ±7%).

### Vias et transition de connecteur : Points de discontinuité critiques dans la liaison

Dans les PCB multicouches, le via est une structure indispensable pour réaliser la connexion entre les couches, mais c'est aussi l'un des principaux points de discontinuité d'impédance dans le **data-center 112G SerDes routing**. Un via non optimisé dont la réflexion et la perte introduites suffisent à faire échouer toute la liaison 112G.

- **Moignon de via (Via Stub)** : Lorsque le signal est transmis de la couche superficielle à la couche intermédiaire, la partie inutilisée du via forme un "moignon". Ce moignon résonnera à haute fréquence, causant une grave atténuation du signal à des fréquences spécifiques, se manifestant par une "encoche" évidente sur la courbe S21 des paramètres S. Pour un signal de 28 GHz, même un moignon de quelques dizaines de mils est fatal. La solution est le **contre-perçage (Back-drilling)**, c'est-à-dire percer la colonne de cuivre excédentaire du via depuis l'arrière du PCB, en contrôlant la longueur du moignon à moins de 5-10 mil.
- **Optimisation de l'impédance des vias** : Le via lui-même est une structure 3D complexe, son impédance est influencée par la taille du plot (Pad), de l'anti-plot (Anti-pad) et du barillet du via (Barrel). Les outils de simulation de champ électromagnétique 3D (comme Ansys HFSS, CST) peuvent être utilisés pour optimiser la structure du via, en ajustant la taille de l'anti-plot pour correspondre à l'impédance de la trace et réduire la réflexion.
- **Optimisation de l'empreinte du connecteur (Footprint)** : Le connecteur intégré (comme QSFP-DD, OSFP) est une autre zone de transition critique. La disposition des plots BGA ou SMT du connecteur doit être optimisée en collaboration avec les traces PCB pour réaliser une transition d'impédance fluide. Cela implique souvent des plots non circulaires (Non-Circular Pad) et des techniques avancées de **112G SerDes routing layout** comme l'évidement local du plan de masse de référence.

Pour les fonds de panier et les cartes système complexes, la technologie [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) avec micro-vias et vias borgnes/enterrés peut fournir des chemins de connexion plus courts et des effets parasites plus faibles, et est un moyen efficace de réaliser un **high-speed 112G SerDes routing** à haute densité.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 Optimisation de la couche physique 112G SerDes : Directives pour vias et structures de transition</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Pour la continuité de l'impédance sous modulation PAM4 et l'optimisation de la réjection de mode commun</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Élimination des moignons (Stub) et précision du contre-perçage</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle de base :</strong> Le signal 112G est extrêmement sensible à la **résonance de Stub**. Un contre-perçage complet doit être mis en œuvre, contrôlant strictement la longueur du moignon à **&lt;8 mil** (mieux que les 10 mil courants dans l'industrie), pour repousser le premier point de résonance au-delà de la bande non active de 40GHz.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Compensation de champ électromagnétique de l'anti-plot (Antipad)</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle de base :</strong> Interdiction d'utiliser des valeurs empiriques. Il faut optimiser collaborativement le diamètre de l'anti-plot et la taille du plot de signal par **simulation EM 3D complète**, compenser la capacité parasite apportée par le via, et maintenir la fluctuation d'impédance différentielle au niveau du via dans une plage de **±5%** de la valeur cible.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Configuration des vias de blindage (Shadowing Vias)</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle de base :</strong> Disposer symétriquement **2-4 vias de retour de masse** autour de la paire de vias différentiels. En raccourcissant la zone de boucle de flux magnétique du chemin de retour, on réduit l'inductance d'interconnexion et on fournit une isolation de diaphonie inter-couche supérieure à **-40dB** pour les canaux sensibles.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. Fan-out de zone BGA et sélection de processus</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle de base :</strong> Pour les BGA à pas de 0,8 mm et moins, le processus **VIPPO (Via-in-Pad Plated Over)** est recommandé pour économiser de l'espace et réduire la réactance inductive. Si un fan-out en "os de chien" est utilisé, une conception de compensation de largeur spécifique doit être effectuée pour les segments de trace courts afin d'éviter la formation de points discontinus à haute fréquence locaux.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Conseil de fabrication HILPCB :</strong> Le succès de la conception 112G réside dans la <strong>tolérance résiduelle de contre-perçage (Back-drill Tolerance)</strong>. Nous recommandons de vérifier non seulement les paramètres Gerber lors de la phase de conception, mais aussi de confirmer avec l'usine sa capacité de retour sur le <strong>contre-perçage laser (Laser Back-drilling)</strong> ou le perçage à profondeur contrôlée (T-Control), afin de s'assurer que les écarts en production réelle n'entraînent pas de points d'encoche inattendus dans le domaine fréquentiel.
</div>
</div>

### Considérations centrales pour la disposition du routage 112G SerDes

Un **112G SerDes routing layout** réussi n'est pas seulement une question de connexion de fils, c'est un art de l'espace, de l'isolation et du timing. Dans les conceptions à haute densité, la diaphonie est le deuxième défi majeur après la perte d'insertion.

- **Espacement des canaux et contrôle de la diaphonie** : Plus l'espacement entre les paires différentielles est grand, plus la diaphonie est faible. Une règle de conception courante est la règle "3W" ou "5W" (W étant la largeur d'une seule trace), c'est-à-dire que la distance centre à centre des paires différentielles doit être maintenue à plus de 3 ou 5 fois la largeur d'une seule trace. Dans les zones à espace restreint, l'isolation peut être renforcée en insérant des traces de blindage de masse (Guard Trace) entre les paires différentielles.
- **Conception de l'empilement et stratégie de câblage** :
    *   **Stripline vs Microstrip** : La structure Stripline des couches internes, étant entourée par deux plans de référence haut et bas, offre un meilleur blindage EMI et une meilleure isolation du signal, et est le premier choix pour le routage 112G SerDes longue distance. Bien que la Microstrip de couche superficielle ait une perte légèrement inférieure (car une partie des lignes de champ est dans l'air), elle est plus sensible aux interférences externes.
    *   **Câblage orthogonal** : La direction de câblage des couches de signal adjacentes doit être orthogonale (par exemple, L3 est horizontale, L4 est verticale) pour réduire la diaphonie inter-couche.
- **Fan-out de zone BGA (Breakout)** : La zone BGA des puces ASIC ou FPGA à nombre élevé de broches est la zone à la densité de câblage la plus élevée. La stratégie de fan-out affecte directement l'intégrité du signal et la fabricabilité. Il est nécessaire de planifier soigneusement l'emplacement des vias, les chemins des traces et l'attribution des couches pour éviter que des réseaux de vias denses ne divisent gravement le plan de référence. La conception de cette partie nécessite généralement un **112G SerDes routing guide** détaillé pour guider les ingénieurs.
- **Intégrité de l'alimentation (PI)** : Un réseau de distribution d'alimentation (PDN) stable et à faible bruit est la base du fonctionnement normal des émetteurs-récepteurs SerDes. Le bruit PDN se traduira directement par une gigue d'horloge, détériorant la qualité du signal. Par conséquent, il est nécessaire de placer un nombre et une variété suffisants de condensateurs de découplage et d'effectuer une simulation d'impédance PDN pour assurer une faible impédance du réseau d'alimentation sur toute la gamme de fréquences.

### Égalisation et gigue : Co-conception de la puce au canal

Même avec les meilleurs matériaux et un routage optimal, un canal PCB de plusieurs dizaines de pouces produira toujours une interférence inter-symboles (ISI) sévère. Les émetteurs-récepteurs SerDes modernes intègrent de puissants circuits de traitement numérique du signal (DSP) et d'égalisation (Equalization) pour compenser les pertes de canal.

- **Égalisation côté émission (Tx EQ)** : Utilise généralement une égalisation par anticipation (FFE), améliorant les composantes haute fréquence du signal par pré-accentuation (Pre-emphasis) et désaccentuation (De-emphasis), compensant à l'avance les caractéristiques passe-bas du canal.
- **Égalisation côté réception (Rx EQ)** :
    *   **Égaliseur linéaire à temps continu (CTLE)** : Un filtre passe-haut analogique programmable utilisé pour amplifier les signaux haute fréquence et "ouvrir" initialement l'œil fermé.
    *   **Égaliseur à rétroaction de décision (DFE)** : Un égaliseur non linéaire qui élimine l'interférence du bit précédent sur le bit actuel (ISI arrière) en fonction des bits précédemment décidés. Le DFE est un outil puissant pour faire face aux fortes réflexions et ISI, mais il est sensible aux erreurs de décision, ce qui peut entraîner une propagation d'erreurs.

L'objectif de la conception de PCB est de créer un canal "bien comporté" qui permet à l'égaliseur SerDes de le compenser facilement, plutôt que de concevoir un canal à perte énorme et de dépendre excessivement de la capacité de l'égaliseur. Un schéma d'égalisation trop complexe augmentera la consommation d'énergie, la latence et la complexité de conception. Par conséquent, les ingénieurs SI doivent travailler en étroite collaboration avec les fournisseurs de puces pour obtenir le modèle IBIS-AMI de leur SerDes, et co-optimiser la conception du canal et les paramètres de l'égaliseur dans la simulation pour atteindre la meilleure marge COM.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 Rapport de validation de simulation de liaison 112G PAM4</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">Résumé de l'analyse Channel Operating Margin (COM)</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Perte d'insertion (IL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist : 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Limite cible : &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Marge de fonctionnement du canal (COM)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">État : PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Cible IEEE : &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Déviation de perte (ILD)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Contrôle d'ondulation : Excellent</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Limite cible : &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">Perte de retour effective (ERL)</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Suppression de réflexion : Conforme</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Limite cible : &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
189: 💡 <strong>Suggestion d'ingénierie :</strong> L'IL actuel est de -32dB, il ne reste que 3dB avant la limite budgétaire (-35dB). Compte tenu des tolérances Dk/Df dans la production en grande série, il est suggéré d'effectuer une simulation Monte Carlo spécifique pour la <strong>rugosité de la feuille de cuivre HVLP</strong> du matériau avant la production en série.
</div>
</div>

### Du prototype à la production de masse : Analyse de faisabilité de fabrication (DFM)

Même la conception de simulation la plus parfaite est sans valeur si elle ne peut pas être fabriquée de manière économique et fiable. La collaboration conception-fabrication est la clé du succès du **data-center 112G SerDes routing**, en particulier lors du traitement de prototypes **112G SerDes routing low volume** ou de production de masse à grande échelle.

- **Impact des tolérances de fabrication** : Les tolérances dans le processus de fabrication de PCB, telles que les variations de gravure de largeur/espacement de ligne, les variations d'épaisseur pendant le processus de laminage, entraîneront une déviation de l'impédance du produit final par rapport à la valeur de conception. Un fabricant fiable, tel que HILPCB, fournira son guide détaillé de capacité de processus (Process Capability Guide), et les concepteurs devraient intégrer ces tolérances dans le modèle de simulation dès le début de la conception et effectuer une analyse Monte Carlo pour évaluer les performances dans le pire des cas.
- **Traitement de surface** : Différents processus de traitement de surface ont des impacts différents sur les signaux haute fréquence. L'or par immersion chimique (ENIG) est le premier choix pour les applications haute vitesse en raison de sa surface plane et de sa bonne conductivité. Mais attention au problème du "Black Pad". L'ENEPIG offre une meilleure fiabilité. Le choix du processus nécessite d'équilibrer le coût, les performances et la fiabilité de la soudure.
- **Vérification DFM** : Avant d'envoyer les fichiers de conception (Gerber/ODB++) au fabricant, il est crucial d'effectuer une vérification DFM (Design for Manufacturability) complète. Cela permet de découvrir des problèmes de fabrication potentiels, tels que des trous de perçage trop petits, des anneaux de cuivre trop étroits, des pièges à acide (Acid Traps), etc., évitant ainsi des reprises coûteuses. De nombreux fournisseurs de PCB avancés offrent des services d'analyse DFM gratuits.

Que ce soit pour la validation de prototype en petit volume (**112G SerDes routing low volume**) ou la production à grande échelle, le choix d'un partenaire doté d'équipements avancés et d'un contrôle de processus strict est crucial. Cela garantit non seulement les performances du premier produit, mais aussi la cohérence entre les lots. Nous recommandons de choisir un fournisseur comme HILPCB qui offre un service complet de la fabrication de [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) à l'assemblage, pour simplifier la chaîne d'approvisionnement et assurer la qualité.

### Test et validation de conformité : Garantir que les performances de la liaison sont aux normes

En tant qu'ingénieur de mesure, je pense que "sans mesure, pas de parole". Le but ultime de la conception et de la simulation est la validation par des tests physiques. La validation de la liaison 112G SerDes est un processus complexe qui nécessite des équipements et des méthodes professionnels.

1.  **Mesure des paramètres S** : Utiliser un analyseur de réseau vectoriel (VNA) pour effectuer des mesures dans le domaine fréquentiel sur la carte de test PCB ou l'ensemble de la liaison, en extrayant ses paramètres S (y compris la perte d'insertion Sdd21, la perte de retour Sdd11, la diaphonie, etc.). Les paramètres S mesurés peuvent être comparés aux résultats de simulation pour vérifier la précision du modèle et utilisés pour le calcul du COM.
2.  **Mesure d'impédance TDR** : Utiliser un réflectomètre dans le domaine temporel (TDR) pour mesurer les courbes d'impédance des traces différentielles et des vias. Cela permet d'identifier intuitivement l'emplacement et la gravité des discontinuités d'impédance dans la liaison, et est un outil puissant pour la validation du **112G SerDes routing impedance control**.
3.  **Test de diagramme de l'œil et BER** : Connecter un générateur de motifs et un testeur de taux d'erreur binaire (BERT) aux deux extrémités de la liaison pour tester les performances de la liaison dans des conditions de travail réelles. En observant le degré d'ouverture (hauteur et largeur) du diagramme de l'œil (Eye Diagram) à l'extrémité de réception et en mesurant le taux d'erreur binaire, on peut finalement déterminer si la liaison répond aux spécifications de conception (comme BER < 1E-6).

Ces tests sont cruciaux non seulement en phase de R&D, mais aussi pour le contrôle qualité en phase de production. En effectuant des tests par échantillonnage sur les produits de la ligne de production, on peut garantir une cohérence de fabrication continue.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion : La collaboration globale est la clé du succès

En résumé, un **data-center 112G SerDes routing** réussi est une ingénierie système extrêmement difficile qui exige que l'équipe de conception possède des connaissances approfondies dans plusieurs domaines et collabore de manière transparente avec les partenaires de fabrication. De la sélection des bons matériaux à perte ultra-faible, à la conception précise de l'empilement et au contrôle de l'impédance, en passant par l'optimisation minutieuse des discontinuités telles que les vias et les connecteurs, chaque maillon est essentiel.

Nous devons dépasser la pensée traditionnelle de conception de PCB et considérer l'ensemble de la liaison comme un système unifié. Ce n'est qu'en effectuant une analyse précoce grâce à des outils de simulation de champ électromagnétique avancés, en combinant une compréhension profonde des capacités d'égalisation SerDes, et en plaçant toujours la faisabilité de fabrication (DFM) au premier plan, que nous pourrons trouver le meilleur équilibre entre performance, coût et fiabilité.

Pour les entreprises cherchant à réussir dans le domaine du 112G et des vitesses supérieures, choisir un partenaire comme Highleap PCB Factory (HILPCB), qui comprend à la fois la conception et excelle dans la fabrication, sera votre choix judicieux pour maîtriser les défis des liaisons ultra-haute vitesse et accélérer la mise sur le marché des produits. Nous fournissons une solution complète allant du conseil en sélection de matériaux, de l'analyse DFM à la fabrication de haute précision et à la validation des tests, garantissant que votre conception de **data-center 112G SerDes routing** passe du plan à un produit fiable de haute performance.

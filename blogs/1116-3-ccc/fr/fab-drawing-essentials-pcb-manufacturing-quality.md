---
title: "Fab drawing essentials : 20 questions fréquentes en fabrication et test"
description: "Synthèse de 20 problèmes typiques liés à fab drawing essentials en manufacturing/assembly/testing—symptômes, root causes et solutions—avec matrice défauts/contre-mesures et checklist d’audit qualité."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["fab drawing essentials", "smt stencil design tutorial", "soldermask exposure tutorial", "stackup documentation guide", "surface finish selection tips", "yield improvement roadmap"]
---
## Introduction : pourquoi le Fab Drawing est la base de la production PCB

Dans l’écosystème complexe de fabrication PCB, le **Fab Drawing** est le seul « document légal » et la single source of truth de la communication technique. Un Fab Drawing détaillé et précis est le point de départ d’un haut yield et d’une forte reliability—et le cœur d’une **yield improvement roadmap**. À l’inverse, toute omission, ambiguïté ou erreur peut déclencher une réaction en chaîne en fabrication, assembly et test, avec surcoûts, retards, voire failures terrain.

Cet article, centré sur **fab drawing essentials**, récapitule de façon structurée 20 problèmes courants sur l’ensemble du flux. Pour chaque point, nous couvrons symptômes, métriques, root causes, puis actions correctives et préventives—afin de construire un Fab Drawing « sans zones grises ».

---

## Partie 1 : Manufacturing FAQ

Les problèmes de fabrication sont souvent liés à des phénomènes physiques/chimiques, et leur origine remonte fréquemment aux définitions matériaux, stack-up et tolérances du Fab Drawing.

### 1. Problème : pourquoi observe-t-on un warpage important après reflow ?

-   **Symptômes** : la carte se courbe ou se vrille après chauffe ; le placement devient difficile ; BGA peut présenter open/short.
-   **Métriques** : Warpage > 0,75% (IPC-A-610 Class 2/3). Formule : (déformation max / diagonale PCB) × 100%.
-   **Root causes** :
    1.  **Stack-up asymétrique** : copper distribution déséquilibrée dans le stackup, entraînant un mismatch de CTE.
    2.  **Mauvais choix de matériau** : matériau High Tg non spécifié, ou mélange de matériaux à CTE différents.
    3.  **Grandes zones de cuivre** : copper pours étendus sans mesh/cross-hatching, augmentant les contraintes internes.
-   **Solution** : baking et pressage pour remise à plat, mais mesure de rework limitée.
-   **Prévention** :
    -   Dans le **stackup documentation guide**, exiger un stack-up symétrique et copper-balanced.
    -   Spécifier types/épaisseurs/fournisseurs de Core et PP.
    -   Imposer mesh/cross-hatching pour les zones cuivre > 500 mm² et documenter la règle.

### 2. Problème : PTH copper thickness insuffisant ou voids dans les trous ?

-   **Symptômes** : mauvaise continuité des vias, résistance élevée, opens après thermal shock ou vibrations.
-   **Métriques** : IPC-6012 Class 2 : hole copper thickness moyenne < 20 μm ; Class 3 requiert typiquement ≥ 25 μm. Nombre de voids > 1 ou longueur de void > 5% du diamètre du trou.
-   **Root causes** :
    1.  **Exigences ambiguës** : le Fab Drawing ne précise pas l’IPC Class (2/3) ni les cibles numériques.
    2.  **High Aspect Ratio** : Aspect Ratio > 10:1 rend le plating difficile sans exigence process dédiée.
    3.  **Perçage de mauvaise qualité** : paroi rugueuse ou smear/résidus qui dégradent la déposition cuivre.
-   **Solution** : micro-section du lot ; en cas de non-conformité, scrap fréquent.
-   **Prévention** :
    -   Dans la Drill Table et les notes : « Hole copper thickness conforme IPC-6012 Class 3 ; moyenne ≥ 25 μm ».
    -   Pour Aspect Ratio > 10:1, exiger des procédés renforcés (ex. pulse plating).

### 3. Problème : Solder mask bridge qui se décolle ou manque de précision ?

-   **Symptômes** : les solder mask dams entre pads fine pitch (ex. QFP, BGA) se décollent, créant du solder bridging et des shorts.
-   **Métriques** : Solder Mask Dam width < 75 μm (3 mil) ou décollement pendant SMT/reflow.
-   **Root causes** :
    1.  **Solder Mask Opening mal défini** : opening trop grand vs pad (souvent +2–3 mil par côté recommandé).
    2.  **Type/procédé non spécifié** : LDI haute précision non exigé ; l’exposition classique ne tient pas le fine pitch.
-   **Solution** : réparation manuelle (coûteuse/peu fiable) ou réduction de pâte via stencil.
-   **Prévention** :
    -   Définir clairement les règles d’opening ou fournir un Gerber solder mask précis.
    -   Selon **soldermask exposure tutorial**, indiquer : « Pitch ≤ 0,4 mm : procédé LDI obligatoire ».

### 4. Problème : propreté insuffisante et résidus ioniques ?

-   **Symptômes** : en haute température/humidité : fuites, electrochemical migration (ECM), dendrites, jusqu’au failure.
-   **Métriques** : Ion Chromatography > 0,65 μg/cm² (équivalent NaCl), non conforme IPC-J-STD-001.
-   **Root causes** : aucun niveau de propreté n’est exigé ; nettoyage standard sans renforcement local (ex. sous BGA).
-   **Solution** : plasma cleaning ou nettoyage ultrasons sur cartes finies.
-   **Prévention** : dans Fab Drawing : « cartes finies conformes IPC-J-STD-001 Class 3 + rapport de contamination ionique ».

### 5. Problème : surface finish avec épaisseur non uniforme ou oxydation ?

-   **Symptômes** : solderability faible, joint strength basse, gold fingers avec mauvais contact ; ENIG peut présenter “Black Pad”.
-   **Métriques** : ENIG Au < 1,27 μm (0,05 mil) ou Ni < 2,54 μm (0,1 mil). Le film OSP se dégrade après plusieurs reflow.
-   **Root causes** :
    1.  **Standard non spécifié** : le Fab Drawing indique « ENIG » sans standard/épaisseur (ex. IPC-4552).
    2.  **Mauvais choix de procédé** : selon **surface finish selection tips**, finish inadapté pour high-frequency/fine pitch (ex. HASL).
-   **Solution** : non récupérable ; scrap.
-   **Prévention** :
    -   Spécifier le finish et le standard : « ENIG per IPC-4552A, Au 0,05–0,1 μm, Ni 3–6 μm ».
    -   Pour zones critiques (gold fingers), définir un hard gold plus épais.

### 6. Problème : Back Drilling mal maîtrisé, stub trop long ?

-   **Symptômes** : SI dégradée en high-speed, avec réflexions et insertion loss importantes.
-   **Métriques** : stub après backdrill > 10 mil.
-   **Root causes** : définition backdrill peu claire dans Fab Drawing.
    1.  **Profondeur non définie** : top/bottom et layer d’arrêt non précisés.
    2.  **Tolérance de stub floue** : Max Stub non spécifié.
-   **Solution** : non réparables sur cartes déjà produites.
-   **Prévention** :
    -   Fournir un layer backdrill dédié et une table backdrill.
    -   Indiquer “start layer”, “stop layer” et “Max Stub” (ex. 8 mil) pour chaque trou.

<div class="custom-block-type-6">
    <h4>Présentation des capacités de fabrication HILPCB</h4>
    <p>HILPCB dispose de LDI avancés, de lignes de pulse plating et d’équipements de perçage à contrôle de profondeur pour exécuter précisément les exigences du Fab Drawing. Des trous High Aspect Ratio jusqu’à 20:1 au contrôle de profondeur backdrill à ±5 mil, notre flux de fabrication automatisé garantit que chaque PCB respecte l’intention de conception et sécurise la performance produit.</p>
</div>

---

## Partie 2 : Assembly FAQ

Les défauts d’assembly sont étroitement liés au pad design, au solder mask opening et au stencil design—à normaliser dès le Fab Drawing.

### 7. Problème : beaucoup de solder balls après SMT ?

-   **Symptômes** : petites billes de soudure autour des composants chip (R/C), avec risque de shorts.
-   **Métriques** : sur 6,5 cm², plus de 5 solder balls de Ø > 0,13 mm (IPC-A-610).
-   **Root causes** :
    1.  **Solder mask opening trop grand** : la pâte migre sur le mask pendant la chauffe et forme des balls.
    2.  **Apertures de stencil inadaptées** : en contradiction avec **smt stencil design tutorial**.
    3.  **Humidité du laminate** : packaging/storage non spécifiés.
-   **Solution** : retrait manuel + nettoyage.
-   **Prévention** :
    -   Définir règles NSMD ou SMD et tolérances d’opening précises.
    -   Exiger un vacuum packaging conforme aux exigences MSL.

### 8. Problème : tombstoning sur composants chip ?

-   **Symptômes** : un côté de 0402/0201 se lève, « debout » sur le pad.
-   **Métriques** : un côté est complètement décollé.
-   **Root causes** :
    1.  **Pads asymétriques** : tailles différentes ou copper area très différente, créant une tension de surface déséquilibrée.
    2.  **Solder mask sur le pad** : précision insuffisante et recouvrement partiel.
-   **Solution** : rework.
-   **Prévention** :
    -   Référencer une librairie interne ou IPC-7351 dans Fab Drawing.
    -   Exiger zéro résidu de mask sur les pads et définir la clearance minimale.

### 9. Problème : trop de voids après soudure BGA/QFN ?

-   **Symptômes** : X-Ray montre des voids dans les balls BGA ou sous le thermal pad QFN, dégradant thermique et fiabilité.
-   **Métriques** : void area > 25% par joint (IPC-7095B).
-   **Root causes** :
    1.  **Via-in-Pad mal géré** : VIP sans exigences fill/cap ; outgassing → voids.
    2.  **Stencil design** : grands thermal pads sans ouverture type window/grid pour dégazage.
-   **Solution** : rarement réparable ; remplacement composant coûteux.
-   **Prévention** :
    -   Fab Drawing : « tous Via-in-Pad remplis (résine conductrice/non) et plated capped ; flatness < 1 mil ».
    -   En assembly notes, selon **smt stencil design tutorial**, recommander des ouvertures windowpane ou dot-matrix pour thermal pads QFN.

### 10. Problème : Head-in-Pillow (HIP) sur BGA ?

-   **Symptômes** : les balls semblent en contact mais ne fusionnent pas complètement, joint fragile.
-   **Métriques** : 3D X-Ray ou micro-section : séparation à l’interface ball/pâte.
-   **Root causes** :
    1.  **PCB warpage** : voir Problème 1 ; gap au centre du BGA.
    2.  **Surface finish non uniforme** : corrosion Ni ENIG ou oxydation OSP, solderability en baisse.
-   **Solution** : reballing ou remplacement.
-   **Prévention** :
    -   Appliquer strictement les règles de stack-up symétrique et de sélection matériau.
    -   Spécifier un finish fiable et exiger des rapports de solderability en sortie.

<div class="custom-block-type-4">
    <h4>Alerte risque : un Fab Drawing ambigu est une « bombe à retardement »</h4>
    <p>Une petite omission—par exemple ne pas définir le process de remplissage Via-in-Pad—peut faire échouer un lot complet de soudure BGA et coûter des dizaines de milliers de dollars. Investir du temps sur <strong>fab drawing essentials</strong> en phase design est la meilleure façon d’éviter un risque massif en aval.</p>
</div>

### 11. Problème : teardrops ou pointes après Selective Soldering ?

-   **Symptômes** : après Selective Soldering sur THT, joints peu pleins, en forme de goutte ou avec pointes, non conforme IPC-A-610.
-   **Métriques** : angle de mouillage non > 270° ou présence de pointes.
-   **Root causes** :
    1.  **Thermal design insuffisant** : trous THT directement reliés à grands plans GND, dissipant trop vite.
    2.  **Solder mask opening trop petit** : gêne le flow et le mouillage.
-   **Solution** : retouche manuelle, mais faible homogénéité.
-   **Prévention** :
    -   Exiger des Thermal Relief Pads pour THT reliés à de grandes zones cuivre.
    -   Assurer des openings plus grands que les pads THT.

<div class="cta-container">
    <p>Votre Fab Drawing est-il suffisamment complet ? HILPCB propose une analyse DFM/DFA gratuite : nos ingénieurs examinent vos fichiers sous l’angle fabrication/assembly/test afin d’identifier et d’éliminer les risques avant lancement. <strong>Uploadez vos Gerber maintenant pour obtenir un rapport d’évaluation professionnel !</strong></p>
</div>

---

## Partie 3 : Testing FAQ

Les problèmes de test sont souvent la conséquence de défauts de fabrication/assembly, mais certains se préviennent directement via un meilleur Fab Drawing.

### 12. Problème : mauvais contact des probes ICT et taux élevé de faux rejets ?

-   **Symptômes** : ICT remonte de nombreux faux open ; le retest manuel est OK ; la productivité baisse.
-   **Métriques** : taux de faux rejets ICT > 5%.
-   **Root causes** :
    1.  **Test points non standardisés** : aucune définition min (taille/spacing/forme) ; pads trop petits, trop proches des composants ou du bord.
    2.  **Surface finish des test pads** : avec OSP, les contacts répétés peuvent dégrader le film protecteur.
-   **Solution** : nettoyer les probes, ajuster le fixture, réduire la vitesse.
-   **Prévention** :
    -   Créer un layer test point dédié et noter : « ICT test points : Ø min ≥ 0,8 mm, pitch ≥ 1,27 mm ; surface plane et sans solder mask ».
    -   Pour densité élevée, spécifier un plating or ou étain sur les test pads.

### 13. Problème : scripts FCT qui ne couvrent pas toutes les fonctions ?

-   **Symptômes** : produit OK en FCT mais défauts fonctionnels chez le client ; certains modules n’ont jamais été testés.
-   **Métriques** : couverture < 95%.
-   **Root causes** : manque d’informations d’aide au test (jumpers/interfaces pour activer des test modes).
-   **Solution** : mise à jour scripts/fixtures ; recall ou upgrade terrain.
-   **Prévention** :
    -   Dans l’Assembly Drawing, annoter clairement interfaces de debug/test, jumpers et switches.
    -   Joindre une “test instruction” expliquant l’entrée en différents modes.

### 14. Problème : critères flous pour les tests de fiabilité (ex. thermal shock) ?

-   **Symptômes** : après 500 cycles (-40°C to 125°C), désaccord sur pass/fail pour micro-fissures ou dérive de résistance.
-   **Métriques** : absence d’Accept/Reject Criteria.
-   **Root causes** : pas de référence à un standard fiabilité et pas de seuils pass/fail.
-   **Solution** : critères temporaires négociés (qualité/design/client).
-   **Prévention** :
    -   Définir conditions et critères : ex. « 1000 cycles -40°C à 125°C ; variation de résistance via < 10% ».
    -   Référencer des standards : « exigences fiabilité conformes IPC-TM-650 ».

### 15. Problème : Hipot avec faux déclenchements ou breakdown ?

-   **Symptômes** : lors du test diélectrique, alarme leakage, sans breakdown réel.
-   **Métriques** : leakage > 10 mA (typique) ou arc sous la tension spécifiée.
-   **Root causes** :
    1.  **Creepage/Clearance insuffisants** : HV/LV non mis en avant ; dépendance aux Gerber par défaut.
    2.  **Choix matériau** : grade CTI non adapté à la tension.
-   **Solution** : analyser pour distinguer breakdown réel vs arc de surface (humidité/contamination).
-   **Prévention** :
    -   Marquer les zones HV et définir les minima (ex. “>3 mm for 500V AC”).
    -   Spécifier CTI dans la BOM matériau (ex. CTI ≥ 400V).

---

## Partie 4 : Quality FAQ

Les problèmes qualité reflètent des lacunes systémiques. La complétude du Fab Drawing conditionne la robustesse du système qualité.

### 16. Problème : déclenchements SPC fréquents ?

-   **Symptômes** : sur drilling, line width, impedance, points hors UCL/LCL fréquents.
-   **Métriques** : Cpk < 1,33.
-   **Root causes** :
    1.  **Tolérances irréalistes** : trop strictes vs capability naturelle.
    2.  **CTQ non identifiés** : pas de focus de monitoring en usine.
-   **Solution** : analyser les points hors contrôle (special vs common causes).
-   **Prévention** :
    -   Aligner les tolérances avec le fournisseur et la **yield improvement roadmap**.
    -   Marquer les CTQ (ex. `[CTQ]`) : largeur de trace d’impédance, diamètre pad BGA, etc.

### 17. Problème : après complaint client, l’8D ne se clôt pas efficacement ?

-   **Symptômes** : la root cause n’est pas identifiée ; l’8D bloque au D4.
-   **Métriques** : cycle de clôture 8D > 30 jours.
-   **Root causes** : Fab Drawing incomplet et traçabilité insuffisante (ex. modèle matériau non spécifié).
-   **Solution** : DPA destructif (micro-section, SEM/EDX).
-   **Prévention** :
    -   Fab Drawing doit inclure material list complète, stack-up, standards de surface finish et exigences process spéciales.
    -   HILPCB mappe les paramètres Fab Drawing aux données de production (profil lamination, courant de plating). Notre système 8D corrèle exigences et paramètres réels pour localiser la root cause.

<div class="custom-block-type-5">
    <h4>Valeur HILPCB : quality assurance pilotée par la donnée</h4>
    <p>Nous sommes plus qu’un fabricant. HILPCB digitalise votre Fab Drawing et l’intègre profondément à notre MES. Du contrôle réception au shipment, chaque paramètre clé est enregistré et surveillé. Pour la traçabilité, nous fournissons un package 8D complet—from design specs aux données de production—rendant la root cause analysis beaucoup plus efficace.</p>
</div>

### 18. Problème : défaut qualité mais chaîne de traçabilité incomplète ?

-   **Symptômes** : lot défectueux détecté, mais impossible d’identifier toutes les cartes affectées ou de remonter aux shifts/lots matière.
-   **Métriques** : impossible de fournir un rapport bidirectionnel complet en 24 h.
-   **Root causes** : exigences de marquage de traçabilité absentes.
    1.  **Pas de serial unique** : pas d’exigence QR/serial par PCB.
    2.  **Format incohérent** : Date Code, UL mark, part number non définis.
-   **Solution** : élargir le recall, gaspillage important.
-   **Prévention** :
    -   Exiger sur silkscreen : part number, revision, UL mark, lead-free symbol, week code (WW/YY).
    -   Pour haute fiabilité : QR unique à un emplacement défini + règles d’encodage.

### 19. Problème : incohérences entre PCBs de fournisseurs différents ?

-   **Symptômes** : mêmes Gerber + Fab Drawing, mais différences couleur/impedance/mécanique.
-   **Métriques** : paramètres clés (ex. TDR impedance) > 10% d’écart.
-   **Root causes** : “espace d’interprétation” (FR-4 sans modèle, green solder mask sans code couleur).
-   **Solution** : tests et screening complémentaires.
-   **Prévention** :
    -   Matériaux : “manufacturer + model” ou AVL.
    -   Pantone Color Code pour solder mask et silkscreen.
    -   Exigences chiffrées et tolérancées (impedance, Dk/Df, etc.).

### 20. Problème : échec de certification finale (UL, CE, etc.) ?

-   **Symptômes** : rejet par le labo pour flame rating, creepage/clearance ou matériaux non conformes.
-   **Métriques** : échec → redesign + nouvel envoi.
-   **Root causes** : exigences compliance/sécurité incomplètes dans Fab Drawing.
-   **Solution** : modifier, refaire proto, retester—fort retard.
-   **Prévention** :
    -   En page 1 : “UL 94V-0”, “RoHS Compliant”.
    -   Vérifier la conformité UL yellow card des matériaux et encres.
    -   Confirmer la qualification du fournisseur et exiger UL mark + factory code.

---

## Contenu additionnel

### Matrice défauts / contre-mesures

Le tableau suivant résume défauts, process steps, métriques et actions : un outil pratique de troubleshooting rapide.

| Defect | Process step | Key metric | Corrective/Preventive action |
| :--- | :--- | :--- | :--- |
| **Warpage** | Stack-up, lamination | Warpage < 0,75% | **Prevention** : imposer stack-up symétrique et copper balance dans Fab Drawing. |
| **PTH Void** | Plating | Average hole copper thickness > 25 μm (Class 3) | **Prevention** : préciser IPC class + exigences process pour High Aspect Ratio holes. |
| **Solder mask dam peeling** | Solder mask, exposure | Min dam width > 75 μm | **Prevention** : exiger LDI et rules d’opening précises. |
| **BGA voids** | SMT, reflow | Void ratio < 25% | **Prevention** : Via-in-Pad resin fill + plated capping obligatoires. |
| **ICT contact issues** | Test | Test pad dia > 0,8 mm | **Prevention** : layer test point dédié + règles dans Fab Drawing. |
| **Traceability break** | Silkscreen, laser marking | Unique serial readability | **Prevention** : QR unique, emplacement et format définis. |
| **Impedance out of spec** | Etching, lamination | Impedance tolerance ±10% | **Prevention** : stack-up détaillé (Dk, Df, thickness) + modèle d’impédance. |
| **Black Pad** | ENIG | Ni phosphorus content 7–9% | **Prevention** : ENIG per IPC-4552A + rapport XRF. |

### Checklist d’audit qualité du Fab Drawing

Avant d’envoyer votre dossier au fabricant, utilisez la checklist ci-dessous pour vérifier que toutes les **fab drawing essentials** sont couvertes.

| # | Audit item | Status (Y/N) | Notes |
| :-- | :--- | :--- | :--- |
| 1 | Part number et revision clairement indiqués ? | | |
| 2 | Dimensions d’outline et tolérances définies ? | | |
| 3 | Stack-up détaillé fourni ? | | épaisseur par couche, modèle matériau, copper weight |
| 4 | Manufacturer + model des laminates spécifiés ? | | ou AVL |
| 5 | Épaisseur finale et tolérance définies ? | | |
| 6 | Drill Table complète fournie ? | | diamètres, tolérances, type (PTH/NPTH) |
| 7 | Exigence hole copper thickness (IPC class) définie ? | | |
| 8 | Trous spéciaux (blind/buried/backdrill) documentés ? | | |
| 9 | Min trace/space défini ? | | |
| 10 | Couleur/type/épaisseur solder mask spécifiés ? | | ex. LPI, green, matte |
| 11 | Règles de solder mask opening définies ? | | |
| 12 | Couleur silkscreen + hauteur mini texte définies ? | | |
| 13 | Surface finish + standard définis ? | | ex. ENIG per IPC-4552A |
| 14 | Exigences d’impedance control ? | | si oui : valeurs/tolérances/méthode test ? |
| 15 | CTQ dimensions/features marqués ? | | |
| 16 | Exigence warpage définie ? | | |
| 17 | Marquages sécurité/environnement inclus ? | | UL, RoHS, CE, etc. |
| 18 | Marquages de traçabilité (date code, serial) définis ? | | |
| 19 | Exigences Via-in-Pad fill/capping définies ? | | |
| 20 | Exigences supplémentaires zones spéciales (gold fingers) ? | | ex. beveling, gold plus épais |
| 21 | Exigences d’electrical test (flying probe/fixture) ? | | 100% E-Test |
| 22 | Règles de design des test points ICT fournies ? | | |
| 23 | Exigences propreté/ionic contamination spécifiées ? | | |
| 24 | Exigences packaging/shipping/storage spécifiées ? | | ex. MSL level |
| 25 | Notes claires, non ambiguës, à jour ? | | |

---

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Un Fab Drawing excellent est bien plus qu’un complément aux Gerber : c’est l’expression précise de l’intention de conception, la définition claire des contraintes de fabrication et une garantie forte de qualité. En traitant systématiquement ces 20 sujets et en intégrant les best practices de **fab drawing essentials** à votre workflow, vous améliorez significativement yield et fiabilité et construisez une relation supply chain efficace et transparente—le socle d’une **yield improvement roadmap** réussie.

<div class="cta-container">
    <p>Prêt à élever votre PCB design au niveau supérieur ? L’équipe d’experts HILPCB est prête à vous accompagner. Nous ne faisons pas que du manufacturing haut de gamme : nous voulons être votre partenaire dès la phase design, pour un Fab Drawing robuste dès le départ. <strong>Contactez-nous maintenant et démarrez votre parcours PCB haute fiabilité !</strong></p>
</div>

> Pour un support fabrication et assemblage, contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des conseils DFM/DFT.

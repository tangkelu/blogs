---
title: "Quand VIPPO vaut vraiment la peine sur un PCB de module optique : comment équilibrer échappement HDI, planéité des pads et chemin thermique"
description: "Une réponse directe sur le bon moment pour utiliser le VIPPO sur un PCB de module optique et sur son impact sur l’échappement HDI, la planéité des pads, la soudure SMT, le chemin thermique et la validation série, afin d’aider les équipes à décider si ce procédé vaut réellement la peine."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO", "Optical module PCB", "HDI PCB", "High-speed PCB", "Via in pad plated over", "PCB assembly"]
---

# Quand VIPPO vaut vraiment la peine sur un PCB de module optique : comment équilibrer échappement HDI, planéité des pads et chemin thermique

- **VIPPO est fait pour les zones denses où le via doit réellement être placé dans le pad. Ce n’est pas une option à étendre à toute la carte juste parce qu’elle paraît plus avancée.**
- **Sur un PCB de module optique, l’intérêt principal de VIPPO est d’ouvrir des canaux d’échappement, de raccourcir la transition verticale et d’amener plus vite la chaleur locale vers le cuivre interne.**
- **Le premier risque de VIPPO n’est pas le coût, mais la perte d’un pad qui se comporte comme un vrai pad soudable et répétable.**
- **Sur une carte de module optique, VIPPO doit être revu avec le stackup HDI, la stratégie microvia, les chemins d’impédance et la validation d’assemblage.**
- **Le bon critère n’est pas "peut-on le fabriquer une fois ?", mais "peut-on le fabriquer de la même façon en proto, présérie et volume ?".**

> **Quick Answer**  
> VIPPO signifie via-in-pad plated over. Sur un PCB de module optique, il ne vaut la peine d’être utilisé que lorsque le fanout HDI standard n’est plus efficace et que le design exige encore une soudure stable ainsi qu’un chemin thermique plat à travers la zone de pad. Les critères clés sont la valeur de routage, la planéité du pad, la fenêtre d’assemblage et la répétabilité en production.

## Table des matières

- [Que faut-il examiner en premier pour VIPPO sur un PCB de module optique ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi VIPPO n’est-il pas utilisé par défaut sur toute la carte du module optique ?](#scope)
- [Pourquoi la vraie question de fabrication n’est-elle pas "peut-on remplir le trou ?", mais "le pad se comporte-t-il encore comme un pad soudable normal" ?](#fabrication)
- [Pourquoi l’assemblage et la thermique doivent-ils être revus avec VIPPO ?](#assembly-thermal)
- [Comment valider un PCB de module optique en VIPPO avant la série ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner en premier pour VIPPO sur un PCB de module optique ?

Commencer par **le pitch des composants, la densité d’échappement, la planéité de pad requise, la structure HDI, le chemin thermique et la méthode de validation d’assemblage**.

Cela ne veut pas dire que "toutes les cartes haut de gamme doivent utiliser VIPPO", ni que toute carte de module optique a automatiquement besoin de via-in-pad. Le contexte public d’IPC-4761 rappelle que les méthodes de protection des vias servent à maintenir la fabricabilité avec un rendement et un coût acceptables, tout en permettant de comparer avantages et limites des différentes approches. Sur un PCB de module optique, il faut donc d’abord se demander :

1. **Les fanouts dog-bone, vias décalés ou microvias standards sont-ils déjà à bout ?**
2. **La zone exige-t-elle réellement un via dans le pad pour que le routage soit possible ?**
3. **Le pad doit-il rester particulièrement plat et régulièrement mouillable après SMT ?**
4. **VIPPO sert-il un objectif SI/thermique réel, ou seulement un dessin plus dense ?**
5. **Coupe micrographique, X-ray et cycle thermique sont-ils déjà prévus dans le plan prototype ?**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / paramètre | Bonne manière de l’évaluer | Pourquoi c’est important | Comment vérifier | Ce qui se passe si on l’ignore |
|---|---|---|---|---|
| Périmètre d’usage | Utiliser VIPPO seulement dans les zones d’échappement denses ou les pads thermiques critiques | VIPPO a de la valeur, mais son emploi large augmente coût et risque d’assemblage | Revue layout, revue densité composants | Coût et risque d’assemblage montent ensemble |
| Planéité du pad | Évaluer la surface soudable après filling, capping et planarization | Les boîtiers fine pitch sont très sensibles à la régularité de surface | Coupe, visuel, X-ray, première soudure | Solder wicking, joints affamés, coplanéité moins bonne |
| Structure de via | Toujours la revoir avec HDI, microvias et lamination séquentielle | VIPPO n’est pas une simple fonction de perçage isolée | Revue stackup, DFM fabrication | Le routage tient à peine, mais la fenêtre process est étroite |
| Chemin thermique | Utiliser VIPPO pour la chaleur seulement là où la dissipation doit vraiment descendre | Cela aide, mais ne remplace pas un design thermique complet | Simulation thermique, thermographie, comparaison carte | Un gain local est pris pour une vraie solution thermique |
| Interaction SMT | Revoir ouverture de pochoir, volume de pâte et profil de refusion ensemble | La structure du pad change directement la fenêtre d’assemblage | First article, X-ray, revue rework | Le proto se soude, la série fluctue |
| Validation série | Définir coupe, cycle thermique et comparaison multi-cartes dès le prototype | Les problèmes de fiabilité n’apparaissent pas uniquement dans le CAD | Coupon, cycle thermique, validation multi-cartes | L’instabilité n’apparaît qu’en présérie |

| Question de décision | Cas plutôt favorable à VIPPO | Cas plutôt sans VIPPO |
|---|---|---|
| Échappement BGA fine pitch | Les canaux voisins ont pratiquement disparu | Le fanout standard suffit encore |
| Dissipation via thermal pad | La chaleur locale doit être entraînée rapidement vers le cuivre interne | La chaleur est surtout gérée par cuivre de surface ou refroidissement externe |
| Assemblage double face | Un via-in-pad non traité provoquerait un fort solder wicking | Des pads non critiques peuvent accepter des vias décalés |
| Coût et fenêtre process | Le projet accepte un coût process plus élevé pour gagner en densité et stabilité | Le coût est serré et d’autres options HDI suffisent |

<div style="background: linear-gradient(135deg, #eef6f2 0%, #f7f1ea 100%); border: 1px solid #d7e1da; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #467566; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #35584d; font-weight: 700;">Density Is the Trigger</div>
      <div style="margin-top: 8px; color: #23342e;">Le bon déclencheur de VIPPO n’est pas l’image "haut de gamme", mais la disparition des canaux d’échappement classiques.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6b48; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5238; font-weight: 700;">Pad Quality Is the Real Risk</div>
      <div style="margin-top: 8px; color: #392f26;">Le vrai sujet n’est pas de remplir le via, mais d’obtenir ensuite un pad qui se soude encore comme un vrai land SMD.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4c7289; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395969; font-weight: 700;">HDI Context Matters</div>
      <div style="margin-top: 8px; color: #243640;">VIPPO doit être lu avec les microvias, la lamination séquentielle, les couches d’impédance et les transitions inter-couches. Une optimisation locale déplace vite le risque vers la fabrication.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #93595f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #74474b; font-weight: 700;">Validate Before Scale</div>
      <div style="margin-top: 8px; color: #3d262a;">La maturité série de VIPPO se prouve par coupes, X-ray, cycles thermiques et cohérence entre cartes, pas par un seul échantillon réussi.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Pourquoi VIPPO n’est-il pas utilisé par défaut sur toute la carte du module optique ?

Conclusion : **Parce que VIPPO est un outil pour résoudre des zones denses et des pads particuliers, pas un upgrade générique pour toute la carte.**

Altium explique publiquement que via-in-pad apparaît lorsque la densité devient telle que les canaux de fanout classiques disparaissent vite. Ce n’est que lorsque le routage est contraint de basculer fortement vers les couches internes que via-in-pad passe de "pratique" à "nécessaire". Cela correspond bien aux cartes de modules optiques, où DSP, retimers, drivers et BGAs de contrôle se concentrent dans un espace très réduit.

<a id="fabrication"></a>
## Pourquoi la vraie question de fabrication n’est-elle pas "peut-on remplir le trou ?", mais "le pad se comporte-t-il encore comme un pad soudable normal" ?

Conclusion : **Parce que la vraie difficulté du VIPPO n’est pas de boucher le trou, mais d’obtenir un pad plat, soudable et répétable après remplissage.**

Le sommaire public d’IPC-4761 rappelle que la protection des vias est liée aux questions de production, de fiabilité long terme et de choix matière. Multi Circuit Boards explique en outre qu’un IPC-4761 Type VII doit aboutir à une surface **flat and solderable** après remplissage, capping, planarization et métallisation.

Sur le plan fabrication, il faut donc regarder :

- **s’il reste des creux, bosses ou irrégularités locales après remplissage**
- **si le pad planarisé mouille encore de façon cohérente**
- **si la finition de surface est adaptée à cette structure**
- **si la cohérence pad-à-pad est suffisante dans la même zone**

<a id="assembly-thermal"></a>
## Pourquoi l’assemblage et la thermique doivent-ils être revus avec VIPPO ?

Conclusion : **Parce que VIPPO change à la fois le comportement de soudure et la façon dont la chaleur locale entre dans la carte.**

Altium indique publiquement que si un via dans le pad n’est pas correctement rempli, cappé et planarisé, la soudure peut être aspirée dans le barrel du via et créer un joint affaissé ou appauvri. Un pad VIPPO bien traité se rapproche beaucoup plus d’un land SMD normal. C’est encore plus critique sur les cartes de modules optiques, qui combinent souvent :

- BGA / LGA fine pitch
- grands pads thermiques inférieurs
- assemblage double face ou forte densité locale
- liaisons haut débit sensibles à la qualité du rework

<a id="validation"></a>
## Comment valider un PCB de module optique en VIPPO avant la série ?

Conclusion : **Une validation utile démontre que le pad VIPPO se comporte toujours comme prévu après fabrication, assemblage et cycle thermique.**

| Élément de validation | Question principale | Points d’observation recommandés |
|---|---|---|
| Coupe / coupon | Filling, capping et planarization sont-ils stables ? | Topographie du pad, remplissage, structure des couches |
| First article SMT + X-ray | Le pad provoque-t-il solder wicking, voiding élevé ou joints irréguliers ? | Joints BGA / LGA, cohérence, zones de grands pads thermiques |
| Thermographie / test thermique carte | VIPPO améliore-t-il vraiment la diffusion locale de chaleur ? | Delta-T composant, direction du flux thermique, régime stable |
| Comparaison multi-cartes | La fenêtre process est-elle assez large ? | Dispersion de soudure et de thermique dans une même zone |
| Recontrôle après cycle thermique | Pad et via restent-ils stables après cyclage ? | État des joints, évolution en coupe, cohérence du retest |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

Si vous développez aujourd’hui une carte de module optique, une carte de contrôle DSP ou une autre sous-carte dense et rapide, l’étape utile consiste à transformer "faut-il du VIPPO ?" en entrée fabricable :

- Si le sujet principal est l’échappement d’un BGA fine pitch, utiliser d’abord [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) pour définir précisément quelles zones de pads exigent réellement le VIPPO.
- Si la carte porte aussi des canaux différentiels rapides, revoir en parallèle le stackup et la structure de transition de [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- En prototype / EVT, intégrer directement coupes, X-ray, thermographie et limites de rework dans la revue [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Une fois zones VIPPO, finition, contrôles d’assemblage et exigences de validation clarifiés, les reporter dans [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) ou [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Quelle est la principale différence entre VIPPO et un via-in-pad ordinaire ?

VIPPO ne s’arrête pas au fait de placer un via dans le pad. Le via est rempli, cappé et planarisé pour que le pad se comporte comme une vraie land SMD.

### Tous les PCB de modules optiques ont-ils besoin de VIPPO ?

Non. VIPPO vaut généralement la peine seulement quand l’échappement fine pitch devient extrêmement serré ou qu’un pad thermique local a vraiment besoin d’un chemin thermique vertical.

### Le principal risque du VIPPO est-il simplement son coût plus élevé ?

Non. Le coût est une conséquence. Le vrai risque est la planéité du pad et la stabilité de l’assemblage.

### VIPPO peut-il résoudre à lui seul un problème thermique ?

Non. Il peut aider à envoyer la chaleur locale vers le cuivre interne, mais il ne remplace pas une architecture thermique complète.

### Pourquoi faut-il faire coupes et X-ray avant la série ?

Parce que beaucoup de problèmes VIPPO ne se voient pas dans le CAD et pas toujours non plus à l’extérieur. La coupe montre le remplissage et la topographie du pad, le X-ray révèle la qualité des joints cachés.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [IPC-4761 Table of Contents](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Appuie le contexte public des bénéfices, limites, sujets de production et matériaux autour des différentes méthodes de protection des vias.

2. [Increase Your Component and Trace High Density With Via-in-Pad Plated Over Technology | Altium](https://resources.altium.com/p/increase-your-component-and-trace-high-density-pad-technology)  
   Appuie l’explication publique de l’usage du via-in-pad dans les layouts denses et BGA fine pitch, y compris le risque de solder wicking des pads non traités.

3. [What via Types Are Described in IPC-4761? | Altium](https://resources.altium.com/p/what-types-are-described-ipc-4761-0)  
   Appuie le contexte public des catégories de protection de via IPC-4761 et le cadrage Type VII utilisé ici.

4. [Via Covering | Multi Circuit Boards](https://www.multi-circuit-boards.eu/en/pcb-design-aid/surface/via-covering.html)  
   Appuie l’explication publique selon laquelle le Type VII d’IPC-4761 vise une surface plate et soudable, souvent utilisée pour via-in-pad et structures séquentielles.

5. [Download IPC 4761 In PDF | IPC WebStore Mirror](https://www.ipcemarket.com/product/ipc-4761/)  
   Appuie le résumé public de la terminologie IPC-4761 sur tenting, plugging, filling, capping et fiabilité long terme.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB HDI et fabrication de modules optiques
- Relecture technique : équipe process PCB, HDI, SMT et thermique
- Dernière mise à jour : 2025-11-18

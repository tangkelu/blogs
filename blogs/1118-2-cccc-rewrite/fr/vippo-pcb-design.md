---
title: "Comment concevoir un PCB VIPPO : quand le via-in-pad vaut vraiment la peine et quand il n’ajoute que du risque d’assemblage"
description: "Une réponse directe sur les critères d’adoption, la définition de via protection, la planéité pad, la fenêtre d’assemblage et la validation à figer tôt dans un PCB VIPPO."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["VIPPO PCB", "Via-in-Pad Design", "Via in Pad", "HDI PCB", "SMT Assembly"]
---

# Comment concevoir un PCB VIPPO : quand le via-in-pad vaut vraiment la peine et quand il n’ajoute que du risque d’assemblage

- **La première question n’est pas de savoir si l’on peut mettre un via dans un pad, mais si le fanout classique, la via protection classique et le pitch actuel ne suffisent plus simultanément pour le routage et l’assemblage.**
- **VIPPO n’est pas une simple action CAD, mais une structure combinée de via protection, remplissage, cuivre de recouvrement, planéité du pad et comportement au reflow.**
- **Sur les BGA fine pitch, le principal risque apparaît souvent en assemblage plutôt qu’au test électrique du bare board.**
- **VIPPO est fortement couplé au HDI, aux microvias et à la distribution locale du cuivre.**
- **Ce qu’il faut figer est une structure de série, pas seulement une structure qui se soude une fois en prototype.**

> **Quick Answer**  
> Le cœur d’un PCB VIPPO n’est pas seulement de placer un via dans le pad, mais de prouver que breakout, soudabilité et chemin thermique y gagnent tout en gardant remplissage, cuivre cap, planéité et comportement reflow répétables.

## Table des matières

- [Que faut-il examiner d’abord sur un PCB VIPPO ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Quand VIPPO est-il vraiment le bon choix ?](#need)
- [Pourquoi la définition de via protection et de la structure filled via doit-elle être explicite ?](#structure)
- [Pourquoi la planéité du pad et la fenêtre d’assemblage décident-elles du résultat série ?](#assembly)
- [Pourquoi VIPPO doit-il être validé dans une boucle de fiabilité ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et informations de relecture](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord sur un PCB VIPPO ?

Commencer par **la raison d’adoption, la définition de via protection, la structure de remplissage et cuivre cap, la planéité du pad, la fenêtre d’assemblage et la méthode de validation**.

À clarifier tôt :

- **Le pitch actuel force-t-il vraiment le via-in-pad ?**
- **Faut-il réellement limiter le solder wicking ou raccourcir le breakout hors pad ?**
- **La zone est-elle aussi couplée à du HDI, des microvias ou un flux thermique élevé ?**
- **Planéité pad, solder mask et stratégie stencil convergent-ils ensemble ?**
- **Le package fabrication est-il assez explicite pour le PCB shop et l’assemblage ?**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / Paramètre | Méthode | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
| --- | --- | --- | --- | --- |
| Critère d’adoption | Prouver que le fanout classique ne suffit plus | VIPPO est coûteux et risqué | Revue fanout, revue package | Coût plus élevé sans gain réel |
| Définition via protection | Définir explicitement protection, remplissage, recouvrement et état de surface | Via-in-pad ne doit pas rester implicite | Fabrication notes, revue Gerber | PCB shop et assemblage lisent autre chose |
| Planéité pad | Juger la cohérence de l’array plutôt qu’un seul pad | Affecte impression, placement et reflow | Premier article, coplanarité, X-ray | Head-in-pillow, cold joint, dérive rendement |
| Couplage structurel | Évaluer VIPPO avec microvias, buried vias et cuivre local | Les structures empilées amplifient le stress | Coupe, revue DFM, contrôle post-reflow | Le proto passe, pas la série |
| Fenêtre d’assemblage | Figer ensemble stencil, pâte, pont solder mask et limite de retouche | Le risque VIPPO apparaît souvent d’abord en SMT | DOE SMT, premier article | Bare board OK, assemblage non |
| Boucle de validation | Voir coupon, coupe, X-ray et état post-reflow ensemble | Un premier succès n’est pas la répétabilité | Validation multi-cartes, trace lots | Les défauts latents apparaissent plus tard |

| Question précoce | Action d’ingénierie plus adaptée |
| --- | --- |
| Seulement un routage local serré | Comparer réellement dog-bone et VIPPO |
| Pitch BGA très serré et solder wicking inacceptable | Figer tôt structure pad+via et conditions d’assemblage |
| Projet avec HDI ou microvias | Revoir via-in-pad et microvias ensemble |
| Besoin de vérifier rapidement la clarté du dessin | Utiliser d’abord [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/) |

<div style="background: linear-gradient(135deg, #f3f5fb 0%, #eef6f2 100%); border: 1px solid #d8dfe7; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #536f94; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405a79; font-weight: 700;">Need Before Structure</div>
      <div style="margin-top: 8px; color: #243545;">Il faut démontrer la nécessité avant de discuter la géométrie. Sans nécessité claire, le risque est simplement déplacé au centre du pad.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #55715d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #45614d; font-weight: 700;">Structure Must Be Explicit</div>
      <div style="margin-top: 8px; color: #27352b;">Si remplissage, cuivre cap et état de surface ne sont pas écrits clairement, fabrication et assemblage suivront des logiques différentes.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6a4e; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f543d; font-weight: 700;">Assembly Fails First</div>
      <div style="margin-top: 8px; color: #372c24;">Beaucoup de problèmes VIPPO n’apparaissent pas au test bare board, mais à l’impression, au reflow et au X-ray.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a5e73; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #70485c; font-weight: 700;">Repeatability Matters</div>
      <div style="margin-top: 8px; color: #392833;">VIPPO devient série seulement quand plusieurs cartes, plusieurs reflows et états assemblés restent stables.</div>
    </div>
  </div>
</div>

<a id="need"></a>
## Quand VIPPO est-il vraiment le bon choix ?

Conclusion : **VIPPO ne vaut la peine que lorsque le fanout classique sacrifie déjà espace de routage, contrôle de la soudure ou chemin thermique, et qu’une structure plus simple ne suffit plus.**

À confirmer d’abord :

- **Le breakout de l’array package est-il réellement bloqué ?**
- **Le schéma via classique rend-il déjà le pad inacceptable ?**
- **Le chemin thermique local exige-t-il vraiment un via dans le pad ?**
- **Seuls quelques packages critiques ont-ils besoin de VIPPO ou toute la carte ?**

<a id="structure"></a>
## Pourquoi la définition de via protection et de la structure filled via doit-elle être explicite ?

Conclusion : **parce que le résultat de fabrication dépend fortement de ce qui est explicitement demandé, pas de l’habitude supposée de l’usine.**

À écrire explicitement :

- **Quels pads exigent un via-in-pad**
- **Si ces vias servent au breakout, à la thermique ou au contrôle d’assemblage**
- **Quelles sont les exigences de remplissage, recouvrement et planéité**
- **S’il existe aussi microvias, buried vias ou stackup spécial**
- **Quels endroits demandent coupons, coupes ou vérifications supplémentaires**

<a id="assembly"></a>
## Pourquoi la planéité du pad et la fenêtre d’assemblage décident-elles du résultat série ?

Conclusion : **parce que pour les BGA, LGA et fine pitch, VIPPO doit finir par se comporter comme un pad stable, pas comme un point spécial seulement “théoriquement soudable”.**

À figer ensemble :

- **La cohérence de tout l’array pad**
- **Le fait que le solder mask comprime ou non la vraie fenêtre de pâte**
- **L’adéquation du stencil à la surface réelle du pad après VIPPO**
- **Le besoin de X-ray ciblé sur les zones BGA critiques**

<a id="validation"></a>
## Pourquoi VIPPO doit-il être validé dans une boucle de fiabilité ?

Conclusion : **parce que le vrai risque n’est pas toujours “impossible à fabriquer”, mais plutôt “fabriqué et soudé une fois, puis dérive sous reflow, changement de lot ou contrainte”.**

Un chemin de release utile comprend souvent :

1. **Geler la raison d’adoption.**
2. **Geler la définition de fabrication.**
3. **Geler les entrées d’assemblage.**
4. **Geler la validation physique.**
5. **Geler la traçabilité des lots.**

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Pour breakout dense et changements de couche locaux, utiliser d’abord la voie [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Pour comparer approche standard et high-density, revoir [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) et VIPPO ensemble.
- Pour les risques liés au pad, au stencil et au reflow, intégrer [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Pour vérifier la clarté des dossiers de fabrication, utiliser [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/).
- Pour proto ou pilote, pousser les points critiques dans [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) et [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Faut-il utiliser VIPPO par défaut sur toutes les cartes BGA ?

A : Non. VIPPO ne vaut la peine que si le fanout classique n’est plus acceptable ou si le gain soudure / thermique est clairement démontré.

### Pourquoi les problèmes VIPPO apparaissent-ils souvent seulement en SMT ?

A : Parce qu’ils touchent le vrai comportement de soudure du pad, visible surtout à l’impression, au reflow et au X-ray.

### La mention “filled via” dans le dessin suffit-elle ?

A : Non. Il faut aussi définir via protection, type de recouvrement, planéité, validation et limites d’assemblage.

### Pourquoi faut-il revoir VIPPO et HDI ensemble ?

A : Parce que via-in-pad est souvent couplé à microvias, transitions denses, stackup et multiples reflows.

### Que faut-il figer en priorité avant fabrication ?

A : La raison d’adoption, la définition pad/via, les conditions de planéité et d’assemblage, la validation physique et la traçabilité lot.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [IPC-4761 Design Guide for Protection of Printed Board Via Structures](https://www.ipc.org/TOC/IPC-4761.pdf)  
   Étaye le fait que VIPPO doit être explicitement spécifié comme structure de via protection.

2. [IPC Board Design Standards](https://www.ipc.org/ipc-board-design-standards)  
   Étaye le contexte commun de standards de conception pour IPC-4761, IPC-2221, IPC-2226 et IPC-6012.

3. [IPC Releases IPC-6012F, Qualification and Performance Specification for Rigid Printed Boards](https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed)  
   Étaye l’idée de remonter tôt la validation des structures complexes et des coupons.

4. [IPC Issues Electronics Industry Warning on Printed Board Microvia Reliability for High Performance Products](https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high)  
   Étaye le risque de défaut latent sur structures couplées microvia / via-in-pad après reflow ou contrainte.

<a id="author"></a>
## Auteur et informations de relecture

- Auteur : équipe contenu HILPCB HDI et assemblage
- Relecture technique : équipe ingénierie procédé PCB, DFM et SMT
- Dernière mise à jour : 2025-11-18

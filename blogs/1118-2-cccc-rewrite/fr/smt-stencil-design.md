---
title: "Comment concevoir un stencil SMT : quoi figer d’abord sur les ouvertures, l’épaisseur et la fenêtre d’impression"
description: "Une réponse directe sur la logique d’ouverture, le choix d’épaisseur, le contrôle fine-pitch, le couplage avec les pads PCB et la boucle de retour de production à confirmer en premier."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["SMT Stencil Design", "Stencil Design", "Impression de pâte à braser", "SMT Assembly", "PCBA DFM"]
---

# Comment concevoir un stencil SMT : quoi figer d’abord sur les ouvertures, l’épaisseur et la fenêtre d’impression

- **Le premier point à figer n’est pas seulement l’épaisseur du stencil, mais quelles structures sont les plus difficiles à imprimer et les plus exposées au bridging ou au manque de pâte.**
- **Une ouverture de stencil n’est pas une copie mécanique du pad.**
- **Fine pitch, thermal pad central et BGA ne peuvent pas partager une seule logique simple.**
- **Beaucoup de défauts apparemment liés au placement ou au reflow viennent d’un manque de convergence entre pads PCB, solder mask et stencil.**
- **Un bon stencil de série s’améliore avec SPI, AOI et X-ray, pas seulement avec un proto qui passe une fois.**

> **Quick Answer**  
> Le cœur du stencil SMT n’est pas de choisir une épaisseur universelle, mais de définir forme d’ouverture, ratio de libération, épaisseur, conditions de pad et boucle de retour autour des structures les plus critiques.

## Table des matières

- [Que faut-il examiner d’abord dans la conception d’un stencil SMT ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi la stratégie d’ouverture contrôle-t-elle en réalité volume de pâte et release ?](#aperture)
- [Pourquoi l’épaisseur du stencil doit-elle être dictée par la structure la plus sensible ?](#thickness)
- [Pourquoi faut-il revoir le stencil avec les pads PCB, le solder mask et les paramètres d’assemblage ?](#pcb-dfm)
- [Pourquoi un stencil de production a-t-il besoin d’une boucle de retour de données ?](#feedback)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et informations de relecture](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord dans la conception d’un stencil SMT ?

Commencer par **le package le plus sensible, la géométrie d’ouverture, l’épaisseur, les conditions de pad PCB, les paramètres d’impression et les données de validation**.

Les questions clés sont en général :

- **Quelle famille de packages impose la plus petite ouverture**
- **Quels pads demandent un traitement spécifique**
- **Si l’épaisseur de base protège vraiment le composant le plus critique**
- **Si pad, solder mask et vias dégradent déjà la fenêtre d’impression**
- **Quelles données de proto reviendront dans la prochaine révision du stencil**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / Paramètre | Méthode | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
| --- | --- | --- | --- | --- |
| Identifier le composant le plus critique | Chercher plus petite ouverture, plus petit pitch et pad thermique complexe | Ces structures fixent la limite | Revue package, BOM | L’épaisseur est biaisée par les gros composants |
| Stratégie d’ouverture | Séparer par type de package, pas par défaut 1:1 | Contrôle volume et release | SPI, essai d’impression, comparaison défauts | Bridging, manque de pâte, slump |
| Choix d’épaisseur | Protéger d’abord la structure la plus sensible | L’épaisseur pilote la fenêtre de release | Premier article, étude de transfert | Les zones fine pitch décrochent d’abord |
| Couplage PCB | Revoir pad, solder mask et vias avec le stencil | Beaucoup de défauts naissent côté PCB | Revue DFM, comparaison Gerber | Le tuning stencil ne corrige pas la cause |
| Structures spéciales | QFN center pad, BGA, PoP et step stencil à juger séparément | Ce sont les zones les plus instables | X-ray, SPI, aspect post-reflow | Voids, head-in-pillow, dérive composant |
| Boucle de retour | Lier SPI/AOI/X-ray à la révision stencil | C’est ainsi que le rendement converge | Historique versions, Pareto | Les mêmes défauts reviennent |

| Règle publique d’usage | Signification technique |
| --- | --- |
| IPC-7525C : aucune règle fixe unique pour tous les stencils | Ouverture et épaisseur doivent être jugées par projet |
| Indium StencilCoach : ouverture rectangulaire souvent préfiltrée par `W/t > 1.5` | Utile pour un premier criblage |
| Indium StencilCoach : ouverture ronde/carrée souvent préfiltrée par `> 0.66` | Très utile pour BGA/CSP |

<div style="background: linear-gradient(135deg, #f7f4ef 0%, #f3f8f2 100%); border: 1px solid #e2ddd4; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6448; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f513b; font-weight: 700;">Aperture Controls Volume</div>
      <div style="margin-top: 8px; color: #382d24;">L’ouverture pilote à la fois volume de pâte, chemin de release et stabilité d’impression.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #59745f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #47604c; font-weight: 700;">Thickness Follows The Weakest Link</div>
      <div style="margin-top: 8px; color: #29352c;">L’épaisseur doit d’abord protéger la structure la plus difficile à imprimer.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #506d91; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405978; font-weight: 700;">PCB And Stencil Are Coupled</div>
      <div style="margin-top: 8px; color: #253544;">Sans convergence entre pad, solder mask et vias, même un bon stencil ne compense que localement.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6174; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #714b5e; font-weight: 700;">Data Must Update The Stencil</div>
      <div style="margin-top: 8px; color: #392833;">Sans retour SPI, AOI et X-ray, les défauts reviennent comme des problèmes prétendument aléatoires.</div>
    </div>
  </div>
</div>

<a id="aperture"></a>
## Pourquoi la stratégie d’ouverture contrôle-t-elle en réalité volume de pâte et release ?

Conclusion : **parce que l’ouverture définit la manière dont la pâte quitte le stencil et devient une soudure contrôlée.**

À figer en priorité :

- **Si les zones QFP/QFN exigent réduction ou contour spécial**
- **Si les zones BGA/CSP respectent une fenêtre d’area ratio réaliste**
- **Si le thermal pad central doit être segmenté**
- **Si plusieurs familles d’ouvertures doivent être créées**

<a id="thickness"></a>
## Pourquoi l’épaisseur du stencil doit-elle être dictée par la structure la plus sensible ?

Conclusion : **parce que la limite d’imprimabilité d’une carte est presque toujours imposée par la plus petite ouverture ou le point de release le plus difficile.**

Avant le freeze, il faut vérifier :

- **Où se trouvent les plus petites ouvertures**
- **Si une épaisseur unique protège encore les zones fine pitch**
- **S’il faut un step stencil**
- **Si les gros pads doivent être compensés par la forme d’ouverture plutôt que par une épaisseur plus forte**

<a id="pcb-dfm"></a>
## Pourquoi faut-il revoir le stencil avec les pads PCB, le solder mask et les paramètres d’assemblage ?

Conclusion : **parce que beaucoup de défauts d’impression ne sont pas des problèmes de stencil isolés, mais des problèmes de pad, solder mask, via et package jamais convergés ensemble.**

À revoir dans le même cycle :

- **Cohérence entre taille de pad et land pattern recommandé**
- **Réduction de la vraie fenêtre de pâte par le solder mask**
- **Effet de via-in-pad, bouchage ou finition de surface**
- **Besoin d’une stratégie void spécifique pour le thermal pad**

<a id="feedback"></a>
## Pourquoi un stencil de production a-t-il besoin d’une boucle de retour de données ?

Conclusion : **parce qu’un bon stencil de série n’est pas seulement celui qui imprime un prototype acceptable, mais celui qui produit des résultats proches lot après lot.**

Une boucle utile comprend en général :

1. **Classer les familles de composants critiques.**
2. **Lier les défauts aux familles d’ouvertures.**
3. **Lier l’épaisseur au mix composants.**
4. **Lire X-ray et SPI ensemble.**
5. **Réécrire les révisions dans des documents contrôlés.**

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Pour la stratégie d’ouverture et la classification package, impliquer d’abord [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Si achat composants, assemblage et fenêtre de reflow avancent ensemble, figer la stratégie stencil avec [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly).
- Pour une vérification précoce du dessin, utiliser [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/).
- Pour exposer plus tôt les risques, pousser les structures critiques en [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Ne pas repousser la discussion sur [PCB Surface Finish](https://hilpcb.com/en/services/pcb-surface-finish/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Une règle 1:1 ouverture/pad suffit-elle généralement ?

A : Non. Les différents packages demandent des équilibres différents entre volume, release et mouillage.

### Pourquoi ne peut-on pas choisir l’épaisseur seulement à partir du plus gros composant ?

A : Parce que la limite vient le plus souvent de la plus petite ouverture et du release le plus difficile.

### Pourquoi les BGA et thermal pads centraux exigent-ils presque toujours un traitement spécifique ?

A : Parce qu’ils amplifient plus facilement les voids, le head-in-pillow, le collapse inégal et la dérive composant.

### Pourquoi les problèmes de stencil remontent-ils souvent au design des pads PCB ?

A : Parce que pad, solder mask, vias et land pattern déterminent directement le comportement d’impression.

### Que faut-il figer en priorité avant fabrication ?

A : La classification composants, la stratégie d’ouverture, l’épaisseur de base ou le choix step stencil, les règles de couplage avec les pads PCB et la boucle SPI/AOI/X-ray.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [IPC-7525C TOC, Stencil Design Guidelines](https://www.ipc.org/TOC/IPC-7525C_TOC.pdf)  
   Étaye l’idée que le stencil design est une discipline dédiée et qu’aucune règle unique ne convient à tous les projets.

2. [StencilCoach Standard Apertures | Indium Corporation](https://software.indium.com/stencil-coach/standard-apertures.php)  
   Étaye les règles empiriques sur aspect ratio et area ratio.

3. [IPC Standards](https://www.ipc.org/ipc-standards)  
   Étaye la lecture conjointe des standards stencil, PCB et assemblage.

4. [Meet Your Standards | IPC-A-610](https://www.ipc.org/meet-your-standards)  
   Étaye le fait que le jugement final porte sur l’acceptabilité de la soudure finie.

<a id="author"></a>
## Auteur et informations de relecture

- Auteur : équipe contenu PCBA et assemblage HILPCB
- Relecture technique : équipe ingénierie procédé SMT, DFM et qualité
- Dernière mise à jour : 2025-11-18

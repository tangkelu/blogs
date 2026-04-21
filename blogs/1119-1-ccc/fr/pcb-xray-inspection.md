---
title: "Ce que l'inspection PCB X-Ray doit vraiment regarder : il ne s'agit pas seulement de sortir des images de voids"
description: "Guide pratique sur le périmètre, l'interprétation des défauts, la logique d'échantillonnage, le retour process et la chaîne de traçabilité à définir en priorité pour une inspection PCB X-Ray."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# Ce que l'inspection PCB X-Ray doit vraiment regarder : il ne s'agit pas seulement de sortir des images de voids

- **Le premier problème que l'inspection X-Ray doit résoudre n'est pas de savoir si une image d'anomalie cachée a été capturée, mais si la qualité des hidden joints peut vraiment être refermée sur le process d'assemblage, les règles d'échantillonnage et la chaîne de traçabilité.** Les titres publics d'IPC-7095E et IPC-7093 placent tous deux design et assembly process guidance au centre, ce qui montre déjà que le X-Ray ne doit pas être traité comme un simple jugement d'image a posteriori.
- **Le X-Ray ne doit pas être réduit au seul mot "void".** Sur les packages BGA, BTC, QFN, LGA et les grands bottom pads, wetting, bridging, offset, head-in-pillow, cohérence des joints et répartition des voids sont des dimensions de risque différentes.
- **Le résultat X-Ray le plus utile n'est pas d'identifier une seule mauvaise carte, mais de pouvoir relier l'image au stencil, à la solder paste, à la géométrie des pads, au profil de reflow et à l'exposition à l'humidité.** Si l'image ne revient pas dans le process, l'amélioration qualité reste lente.
- **La stratégie d'échantillonnage doit être liée au risque package, aux changements de lot et au coût de défaillance.** Nouveaux packages, nouveaux stencils, nouvelle solder paste ou nouvelle fenêtre de reflow ne devraient pas hériter automatiquement de l'ancienne densité d'échantillonnage.
- **Des images X-Ray sans numéro de lot, équipement, programme et enregistrement de jugement fournissent une base faible pour les futures root cause analysis et réclamations client.**

> **Quick Answer**  
> Le cœur de l'inspection PCB X-Ray n'est pas de produire une image nette. Il est de définir à l'avance quels packages doivent être contrôlés, quels risques de hidden joints comptent pour chaque famille de package, comment les résultats d'image reviennent au process et comment ils entrent dans la chaîne de traçabilité. Sur des PCBA BGA, BTC et à forte exigence de fiabilité, le X-Ray est un outil de contrôle de process, pas seulement une étape d'acceptation.

## Table des matières

- [Que faut-il revoir d'abord dans une inspection PCB X-Ray ?](#overview)
- [Règles clés et tableau de paramètres](#rules)
- [Quels produits et quels packages devraient intégrer le X-Ray au contrôle de routine ?](#scope)
- [Quels défauts et quels signaux le X-Ray doit-il réellement rechercher ?](#defects)
- [Pourquoi la plus grande valeur du X-Ray est-elle le retour process plutôt que la simple image ?](#process)
- [Pourquoi faut-il concevoir ensemble stratégie d'échantillonnage et chaîne de traçabilité ?](#sampling)
- [Prochaines étapes avec HILPCB](#next-steps)
- [FAQ](#faq)
- [Références publiques](#references)
- [Auteur et validation technique](#author)

<a id="overview"></a>
## Que faut-il revoir d'abord dans une inspection PCB X-Ray ?

Il faut commencer par **le type de package, le risque de hidden joint, la logique d'interprétation des défauts, la stratégie d'échantillonnage et la méthode de traçabilité**.

Ce n'est ni une simple question de savoir si la machine peut sortir une image, ni la seule question de savoir si le taux de void dépasse une ligne rouge. IPC-7095E pour BGA et IPC-7093 pour Bottom Termination Components placent tous deux design et assembly process guidance dans leur périmètre public. IPC a également indiqué dans la communication sur J-STD-001J que des illustrations supplémentaires liées aux bubbles visibles en X-Ray avaient été ajoutées. Pris ensemble, ces éléments publics montrent déjà que le X-Ray doit servir design, assemblage, inspection et fiabilité, pas seulement une décision image OK / NOK.

Les éléments à figer avant le pilote comprennent généralement :

- **quels packages et quels lots doivent entrer dans la routine X-Ray**
- **quels sont les risques de hidden joints les plus critiques pour chaque famille de package**
- **si l'interprétation regarde surtout le voiding, le wetting, le bridging, l'offset ou la cohérence**
- **comment la densité d'échantillonnage change avec nouveaux packages, nouvelles fenêtres process et niveau de risque**
- **comment images, jugements et données process alimentent la chaîne de traçabilité**

Pour les projets avec beaucoup de joints cachés, il est généralement utile de revoir en même temps les fenêtres process de [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) et [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), plutôt que de laisser stratégie d'inspection et stratégie d'assemblage dériver séparément.

<a id="rules"></a>
## Règles clés et tableau de paramètres

| Règle / Paramètre | Approche recommandée | Pourquoi c'est important | Comment vérifier | Que se passe-t-il si on l'ignore |
| --- | --- | --- | --- | --- |
| Périmètre d'inspection | Définir d'abord quels packages et quels cas à coût de défaillance imposent le X-Ray | Les joints à haut risque ne doivent pas attendre une panne terrain pour être vus | Revue NPI, liste packages, plan qualité | Un risque critique de hidden joint est raté |
| Focalisation de lecture | Les différents packages demandent un focus défaut différent, pas seulement le voiding | BGA, BTC et QFN ne défaillent pas de la même façon | Revue image first article, classification package | Des images sont prises, mais la conclusion reste faible |
| Retour process | Faire remonter chaque image au stencil, à la pâte, au pad et au reflow | La valeur de l'inspection est l'amélioration du process | Lier images et paramètres process | Les défauts sont trouvés mais pas améliorés |
| Stratégie d'échantillonnage | Ajuster l'échantillonnage selon risque, changement process et état du lot | Un sampling fixe peut masquer un nouveau risque | Plan d'échantillonnage first article et production | Les changements à haut risque passent inaperçus |
| Chaîne de traçabilité | Archiver ensemble image, ID carte, programme, équipe et jugement | Nécessaire pour failure analysis et traitement des réclamations | Revue MES / logs, lien au lot | La root cause devient spéculative |
| Coordination design | Revoir tôt pad design, via in pad et ouvertures de bottom pad | Beaucoup de constats X-Ray démarrent dès layout et package design | Revue DFM, contrôle package | La fenêtre d'assemblage se révèle trop étroite après pose |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">Définir d'abord quels packages et quelles situations de lot exigent un X-Ray routinier. Sans périmètre, l'inspection reste réactive.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">Des packages différents craignent des défauts cachés différents. Voiding, bridging, offset et head-in-pillow ne peuvent pas partager une seule grille de lecture.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">Si l'image ne remonte pas au stencil, à la solder paste, au pad design et au reflow, l'amélioration du yield reste lente.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">Sans ID carte, lot, programme et enregistrements de décision, les images X-Ray aident peu pour les réclamations client et la failure analysis.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Quels produits et quels packages devraient intégrer le X-Ray au contrôle de routine ?

En règle générale, **les packages à joints cachés, à fort coût de reprise, à dépendance thermique du bottom pad ou à fort coût de panne terrain sont les meilleurs candidats au X-Ray routinier**.

IPC-7095E est construit autour des BGA, et IPC-7093 autour des BTC / Bottom Termination Components. Cela indique déjà que ces packages ne sont pas de bons candidats à une libération basée uniquement sur AOI ou inspection visuelle. La question d'ingénierie la plus utile n'est donc pas "avons-nous une machine X-Ray ?", mais "si ce package est mal soudé, peut-on se permettre de le découvrir seulement au test fonctionnel ou sur le terrain ?"

Les packages typiquement à inclure en routine sont :

- **BGA, CSP et autres packages à billes cachées**
- **QFN, LGA et composants à grand bottom pad exposé**
- **composants de puissance où chemin thermique et cohérence du joint comptent**
- **PCBA multicouches, fine-pitch ou denses avec reprise coûteuse**
- **cartes automotive, médicales, industrielles ou télécom à forte exigence de fiabilité**

Si le projet s'oriente déjà vers l'assemblage en volume, il est généralement préférable d'intégrer ces packages dans la liste de pré-contrôle de [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) ou [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), plutôt que de décider après le first article "ce qu'il faudrait finalement radiographier".

<a id="defects"></a>
## Quels défauts et quels signaux le X-Ray doit-il réellement rechercher ?

Parce que **le vrai rôle du X-Ray n'est pas de demander "y a-t-il un void ?", mais d'identifier les modes de défaillance des hidden joints qui comptent pour ce package**.

BTC et BGA ne portent pas les mêmes risques, ce qui explique précisément pourquoi IPC les traite via des standards différents. Pour un BGA, les vérifications les plus utiles portent davantage sur wetting, collapse, offset, bridging et risques de type head-in-pillow. Pour BTC, QFN et les grands bottom pads, le focus va plus souvent vers la répartition des joints sous composant, la position des voids, la couverture des joints et leur cohérence.

Les observations les plus utiles sont généralement :

- **si le joint a formé une géométrie de wetting raisonnable et continue**
- **si les hidden joints présentent bridging ou regroupements locaux anormaux**
- **si les voids se concentrent dans des zones critiques thermiques ou mécaniques**
- **si le même composant dans le même lot montre une géométrie très dispersée**
- **si une anomalie locale renvoie à un problème de design, d'impression ou de reflow**

Si la carte contient aussi de grands thermal pads, des zones de puissance complexes ou une forte densité thermique, il est utile de revoir structure de pad et chemin thermique avec [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb), au lieu de traiter le X-Ray comme une action purement post-assemblage.

<a id="process"></a>
## Pourquoi la plus grande valeur du X-Ray est-elle le retour process plutôt que la simple image ?

Parce que **la vraie question n'est pas qu'une seule mauvaise carte existe, mais pourquoi la même anomalie se répète**.

IPC-7093 et IPC-7095 sont tous deux des documents de design and assembly process guidance et non de simples atlas d'images. Cela signifie que l'image doit être lue avec la stratégie d'ouverture de stencil, l'état de la solder paste, le pad design, le traitement via in pad, l'humidité des composants et le profil de reflow. Sans cette liaison, le X-Ray peut dire "il y a un problème ici", mais pas "pourquoi le même problème revient sans cesse".

Les facteurs process les plus utiles à remonter sont généralement :

- **si l'épaisseur de stencil et la stratégie d'ouverture conviennent au package**
- **si type, lot, stockage et usage de la solder paste sont stables**
- **si le pad design, la définition du solder mask et le via in pad sont appropriés**
- **si le profil de reflow correspond au composant et aux conditions carte**
- **si humidité du composant ou du PCB, warpage ou évolution de forme carte ont été négligés**

Si le projet est encore au stade prototype ou pilote, il est généralement préférable de planifier ces boucles de feedback avec [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) plutôt que de transformer le X-Ray en simple rapport de rebut.

<a id="sampling"></a>
## Pourquoi faut-il concevoir ensemble stratégie d'échantillonnage et chaîne de traçabilité ?

Parce que **la valeur de contrôle du X-Ray dépend du moment où l'on inspecte, du volume inspecté et de la capacité à remonter le résultat dans le process**.

Le contexte public autour de J-STD-001J montre déjà que l'interprétation des images X-Ray est de plus en plus formalisée dans les pratiques d'acceptation assembly. En termes d'ingénierie, cela signifie que la stratégie d'échantillonnage ne peut pas rester un template fixe. Elle doit évoluer avec le risque package, la maturité process, les changements process et le coût de défaillance.

Une approche plus robuste comprend généralement :

1. **Augmenter la densité d'inspection sur les premiers lots avec nouveaux packages, nouveaux stencils, nouvelle pâte ou nouveaux programmes de reflow.**
2. **Donner une priorité plus élevée aux BGA fine-pitch, aux grands bottom pads et aux composants thermiques critiques.**
3. **Lier les résultats d'échantillonnage à l'ID carte, à l'équipe, au programme, au lot de pâte et aux réglages équipement.**
4. **Définir des règles d'escalade vers un sampling renforcé ou un contrôle à 100 % si les anomalies se répètent.**
5. **Archiver les jugements d'image avec les actions correctives et non séparément.**

Sans chaîne de traçabilité, les images X-Ray n'aident que pour la décision immédiate. Avec une chaîne de traçabilité, elles soutiennent traitement des réclamations, failure analysis et amélioration continue du process. Pour les projets proches de la production, il est généralement préférable d'écrire ces attentes directement dans [Quote / RFQ](https://hilpcb.com/en/quote/) ou dans des instructions qualité en amont.

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

Si vous introduisez des BGA, QFN, grands bottom pads ou un autre projet avec beaucoup de joints cachés, l'étape suivante consiste généralement à transformer "inspection" en "entrée de contrôle process" :

- Quand le sujet principal est la qualité d'assemblage des hidden joints, intégrer d'abord packages critiques et points de contrôle dans la revue [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Quand fabrication PCB, approvisionnement, placement et test doivent être fermés en un seul flux, utiliser [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) pour aligner les frontières du workflow.
- Quand la carte comporte des composants à forte densité thermique ou de grands thermal pads exposés, revoir design des pads et chemin thermique avec [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb).
- Quand le choix package, le pad design et la fenêtre process doivent être prouvés tôt, pousser ces checkpoints d'abord dans [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quand périmètre, logique d'échantillonnage, méthode d'interprétation et exigences de traçabilité sont définis, transférer l'ensemble dans [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### L'inspection X-Ray concerne-t-elle surtout le pourcentage de voids ?

A : Non. Les voids ne sont qu'une catégorie de risque. Sur beaucoup de produits, wetting, bridging, offset, head-in-pillow, couverture des joints et cohérence lot à lot comptent autant ou davantage.

### Quels produits devraient mettre le X-Ray dans le process de routine ?

A : Les produits avec beaucoup de joints cachés, un coût de reprise élevé, une dépendance thermique au bottom pad ou une exigence de fiabilité forte sont les meilleurs candidats au X-Ray routinier.

### Pourquoi AOI ne suffit-il pas à lui seul ?

A : Parce que beaucoup de joints critiques sont sous le boîtier composant, là où l'AOI ne voit rien, alors que ces mêmes joints définissent souvent le chemin thermique et la fiabilité long terme.

### Pourquoi certaines équipes regardent-elles beaucoup d'images X-Ray sans améliorer rapidement le process ?

A : La raison la plus fréquente est que les images n'ont jamais été reliées au stencil, à la solder paste, au reflow, au pad design et aux données de lot. L'équipe détecte alors les anomalies sans refermer la root cause.

### Que faut-il figer en priorité avant production ?

A : Figer d'abord le périmètre d'inspection, la logique d'interprétation des défauts, la stratégie d'échantillonnage, les déclencheurs d'escalade et la chaîne de traçabilité. Ces choix façonnent davantage la qualité long terme qu'un résultat d'inspection isolé.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   Appui au point selon lequel IPC-7095E est cadré comme design and assembly process guidance pour BGA.

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   Appui au point selon lequel IPC-7093 est centré sur les Bottom Termination Components et inclut des sections liées à l'usage du X-Ray, à la reprise et à la fiabilité.

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   Appui au contexte public selon lequel J-STD-001J a ajouté des illustrations liées aux bubbles visibles en images X-Ray.

<a id="author"></a>
## Auteur et validation technique

- Auteur : équipe contenu HILPCB qualité PCBA
- Validation technique : équipe engineering process d'assemblage, inspection et fiabilité
- Dernière mise à jour : 2025-11-19

---
title: "Assemblage de substrat bridge pour chiplet : que figer d'abord entre zone bridge, warpage, underfill et tests par niveaux"
description: "Guide pratique sur les premiers points à figer dans l'assemblage d'un substrat bridge pour chiplet, notamment la géométrie de la zone bridge, le warpage, l'underfill, l'inspection et la stratégie de cyclage thermique pour les projets UCIe et EMIB."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["chiplet packaging", "Bridge substrate", "Advanced packaging assembly", "UCIe", "EMIB", "Underfill"]
---

# Assemblage de substrat bridge pour chiplet : que figer d'abord entre zone bridge, warpage, underfill et tests par niveaux

- **La première question sur un substrat bridge pour chiplet n'est pas la densité de routage, mais la répétabilité de la fenêtre d'assemblage dans la zone bridge.** Les spécifications UCIe définissent UCIe comme un standard ouvert d'interconnexion die-to-die au niveau package, couvrant couche physique, pile protocolaire, pile logicielle et conformité.
- **Une structure bridge n'est pas simplement un substrat BGA plus dense.** Intel présente EMIB comme un petit bridge en silicium intégré dans le substrat pour créer une interconnexion die-to-die à très haute densité sans interposeur silicium pleine taille.
- **Un prototype qui s'allume n'est pas encore un procédé de production.** Intel Foundry sépare wafer sort, die sort, burn-in, final test et system-level test, ce qui montre bien que les défauts doivent être filtrés par niveaux.
- **Zone bridge, underfill, cyclage thermique et traçabilité des défaillances doivent être revus ensemble.** Le risque le plus coûteux n'est généralement pas l'arrêt total, mais une dérive progressive sous contrainte thermo-mécanique avec une analyse racine devenue difficile.
- **Un substrat bridge stable n'est pas un seul échantillon qui fonctionne, mais une zone bridge, un jeu de matériaux, un flux d'assemblage et un plan de test qui restent répétables d'un lot à l'autre.**

> **Quick Answer**  
> Le cœur de l'assemblage d'un substrat bridge pour chiplet consiste à faire tenir dans une même fenêtre de fabrication la structure locale de la bridge, l'ordre de placement, l'underfill, le contrôle du warpage et les tests par niveaux. Sur les projets UCIe et EMIB, la vraie question n'est pas de savoir si un prototype démarre, mais si la zone bridge peut être assemblée, vérifiée, tracée et rester stable après cyclage thermique.

## Table des matières

- [Que faut-il regarder en premier sur un substrat bridge pour chiplet ?](#overview)
- [Règles clés et tableau de paramètres](#rules)
- [Pourquoi la conception du substrat doit-elle être pilotée par la fenêtre d'assemblage de la zone bridge ?](#bridge-window)
- [Pourquoi warpage, underfill et cyclage thermique forment-ils un seul sujet ?](#warpage-underfill)
- [Pourquoi faut-il anticiper known good die, tests par niveaux et traçabilité des défaillances ?](#kgd-test)
- [Comment valider l'assemblage d'un substrat bridge avant production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [FAQ](#faq)
- [Références publiques](#references)
- [Auteur et validation technique](#author)

<a id="overview"></a>
## Que faut-il regarder en premier sur un substrat bridge pour chiplet ?

Il faut commencer par **la zone bridge, la planéité locale, le warpage, l'underfill, les tests par niveaux et la validation en cyclage thermique**.

Il ne s'agit pas simplement de faire passer plus de signaux sur moins de surface. UCIe place dans un même cadre l'interconnexion package-level die-to-die, le modèle logiciel et les tests de conformité. Les documents publics d'Intel sur EMIB précisent que l'interconnexion s'appuie sur un petit bridge silicium intégré au substrat. Intel Foundry montre en plus une séparation claire entre die sort, burn-in, final test et system-level test.

Un ordre de revue initial plus robuste est généralement le suivant :

1. **Vérifier que la géométrie de la zone bridge, la séquence d'assemblage et la planéité locale restent dans une fenêtre répétable.**
2. **Évaluer ensemble le warpage, l'écoulement de l'underfill et les contraintes de polymérisation avec la zone bridge.**
3. **S'assurer que la stratégie de test permet de séparer les défauts du die des défauts d'assemblage dans la bridge.**
4. **Intégrer dès le départ le cyclage thermique et l'analyse de défaillance au plan pilote.**
5. **Définir en amont les portes d'inspection, les coupes métallographiques et la traçabilité lot par lot.**

Si le produit contient déjà une zone bridge très dense avec microvias et structures à pas fin, il est généralement préférable d'intégrer tôt les limites de fabrication de [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) et [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<a id="rules"></a>
## Règles clés et tableau de paramètres

| Règle / Paramètre | Approche recommandée | Pourquoi c'est important | Comment vérifier | Que se passe-t-il si on l'ignore |
|---|---|---|---|---|
| Fenêtre de la zone bridge | Revoir séparément la géométrie locale et la planéité autour de la bridge | Le risque principal est localisé dans la bridge, pas dans la moyenne carte | Revue structurelle, inspection locale, coplanarité | Les premiers échantillons passent, la répétabilité pilote est faible |
| Contrôle du warpage | Suivre la forme après lamination, placement, underfill et reflow | Les structures multi-matériaux réagissent fortement au warpage | Warpage tracking, comparaison de processus | Le yield chute d'abord sur la coplanarité et le placement bridge |
| Comportement de l'underfill | Vérifier remplissage, vides et contraintes de polymérisation | L'underfill peut protéger mais aussi créer de nouvelles contraintes | X-ray, coupe, comparaison avant/après cyclage | Les premiers échantillons passent, la tenue dans le temps dérive |
| Tests par niveaux | Séparer test du die, test d'assemblage et test système final | Permet d'isoler rapidement défaut die et défaut bridge | Die sort, burn-in, final test, SLT | Les causes racines se mélangent |
| Chaîne de traçabilité | Lier lots matière, historique reflow, underfill et échantillons | Beaucoup de défauts bridge sont cachés | Dossiers de lots, identifiants échantillons, flux FA | Les pannes sont difficiles à reconstituer |
| Validation en cyclage thermique | Considérer le cyclage comme un axe principal | Le risque de durée de vie vient souvent des contraintes thermo-mécaniques | Cyclage thermique, coupe, comparaison structurelle | Le bring-up est bon, la durée de vie ne tient pas |

| Scénario projet | Point d'attention d'assemblage le plus courant |
|---|---|
| Bridge UCIe au niveau package | Alignement bridge, planéité locale, stratégie de test par niveaux |
| Structure type EMIB | Cavité substrat, contraintes près de la bridge, underfill et inspection |
| Substrat multi-die / multi-chiplet | Séquence de placement, charge sur la bridge, cyclage thermique, traçabilité lot |

<div style="background: linear-gradient(135deg, #eef2fb 0%, #f7f0ea 100%); border: 1px solid #dcdfee; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #6d59a0; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #56457f; font-weight: 700;">Bridge Zone Is the Real Product</div>
      <div style="margin-top: 8px; color: #2f2941;">Sur un substrat bridge, la vraie cible process n'est pas la qualité moyenne de toute la carte, mais la capacité de la zone bridge à rester assemblable, inspectable et répétable.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6849; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b5239; font-weight: 700;">Warpage Comes Early</div>
      <div style="margin-top: 8px; color: #382e24;">Avec des cœurs de substrat fins, des matériaux mixtes et une densité locale élevée, le warpage devient souvent un tueur de rendement avant même les problèmes électriques.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4d7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a5f51; font-weight: 700;">Underfill Is a Reliability Process</div>
      <div style="margin-top: 8px; color: #23342d;">L'underfill n'est pas un geste cosmétique. C'est un processus de fiabilité, et un mauvais remplissage ou une mauvaise contrainte de polymérisation réduit directement la durée de vie.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7393; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38586f; font-weight: 700;">Testing Must Be Layered</div>
      <div style="margin-top: 8px; color: #243440;">Sans séparation entre tests du die, du package et du système, il devient très difficile de distinguer ensuite un défaut de bridge d'un défaut de die.</div>
    </div>
  </div>
</div>

<a id="bridge-window"></a>
## Pourquoi la conception du substrat doit-elle être pilotée par la fenêtre d'assemblage de la zone bridge ?

Parce que **la zone bridge est la région locale la plus sensible, la moins reproductible et souvent la première à dériver**.

Intel décrit publiquement EMIB comme un petit bridge silicium intégré dans le substrat pour assurer une interconnexion très dense entre dies. Cette architecture déplace l'attention du niveau moyen de la carte vers la fenêtre locale de la bridge.

Les questions à figer en amont sont notamment :

- **La distribution locale du cuivre autour de la bridge amplifie-t-elle les contraintes ?**
- **La séquence de placement ajoute-t-elle un historique thermique supplémentaire sur cette zone ?**
- **La planéité et la coplanarité près de la bridge suffisent-elles pour un assemblage répétable ?**
- **Les microvias, pads et bords de cavité restent-ils dans une fenêtre process réaliste ?**

Si la zone bridge n'est pas traitée comme un objet process à part entière, les essais pilotes échouent rarement de manière spectaculaire. Le plus fréquent est plutôt une fenêtre trop étroite et un besoin constant de réglages manuels. C'est pour cela qu'il vaut généralement mieux intégrer tôt les capacités [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) et [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<a id="warpage-underfill"></a>
## Pourquoi warpage, underfill et cyclage thermique forment-ils un seul sujet ?

Parce que **le risque de durée de vie sur un substrat bridge vient rarement d'un seul événement. Il résulte le plus souvent d'un cumul d'historiques thermiques et de contraintes matière.**

Un substrat bridge traverse généralement lamination, assemblage lié à la bridge, die attach, underfill, reflow et autres séquences thermiques de test. Chaque étape peut modifier l'état de contrainte local. L'underfill n'est pas toujours bénéfique. Il peut redistribuer les contraintes, mais un remplissage incomplet, trop de voids ou un mauvais matching de polymérisation peuvent aussi créer un nouveau mode de défaillance.

Les points les plus utiles à regrouper dans une même revue sont :

1. **L'évolution du warpage local avant et après underfill**
2. **L'intégrité de la zone bridge avant et après cyclage thermique**
3. **La concentration éventuelle de voids, contamination ou manque de flow dans les zones denses**
4. **L'apparition de fissures ou de signaux de délamination après cyclage**

Si l'on juge l'underfill uniquement à l'aspect visuel sans le relier à la tenue au cyclage thermique et à la structure bridge, la fiabilité est presque toujours surestimée. Pour des engineering samples, il est logique d'intégrer cela très tôt au plan [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="kgd-test"></a>
## Pourquoi faut-il anticiper known good die, tests par niveaux et traçabilité des défaillances ?

Parce que **dans l'advanced packaging, la panne la plus coûteuse n'est pas le défaut lui-même, mais l'incapacité à dire rapidement s'il vient du die, de la bridge ou du process**.

Intel Foundry présente publiquement dans son flux de test chiplet avancé le wafer sort, le die sort, le burn-in, le final test et le system-level test, avec l'objectif explicite de livrer des known good die avant assemblage final. Pour un substrat bridge, cela implique :

- **Un test doit être structuré par niveaux et non réduit au seul power-up final**
- **Le die sort et le known good die réduisent le bruit dans l'analyse des défauts bridge**
- **Le burn-in et le system-level test exposent mieux les défauts thermo-mécaniques marginaux**
- **La traçabilité lot et la liaison avec les échantillons doivent exister avant le pilote**

Sans ces bases, les anomalies apparaissent ensuite comme des pannes sporadiques, des dérives après cyclage thermique ou des différences lot à lot, sans visibilité nette pour distinguer die, bridge, underfill ou historique d'assemblage. Si le produit doit ensuite se raccorder à une carte serveur ou accélérateur, on peut aussi aligner cette logique package avec la logique système exposée dans [Why AI Server Motherboards Can Power Up but Still Fail in Production](/code/blogs/blogs/1119-1-ccc/fr/ai-server-motherboard-reliability.md).

<a id="validation"></a>
## Comment valider l'assemblage d'un substrat bridge avant production ?

Le vrai objectif est **de fermer la boucle entre zone bridge, underfill, cyclage thermique et cohérence inter-lots**.

Le chemin de validation le plus utile comprend généralement :

| Élément de validation | Question principale | Observations recommandées |
|---|---|---|
| Contrôle local de structure / coplanarité | La zone bridge est-elle dans la fenêtre d'assemblage ? | Planéité autour de la bridge, forme locale, état après placement |
| X-ray / coupe | L'underfill et les structures cachées sont-ils complets ? | Voids, qualité de remplissage, zones de concentration de défauts |
| Comparaison avant / après cyclage | La zone bridge reste-t-elle stable sous contrainte de durée de vie ? | Fissures, délamination, dérive visuelle et électrique |
| Tests par niveaux | Peut-on séparer défauts die, défauts d'assemblage et comportement système ? | Anomalies vues en die sort, burn-in, final test et SLT |
| Comparaison multi-lots | La fenêtre process est-elle assez large pour la série ? | Dispersion carte à carte, dérive des paramètres, signatures de lots |

Si le projet est déjà proche du pilote, ces points doivent être inscrits directement dans le plan fabrication et test. Une fois la fenêtre bridge, le comportement de l'underfill, les preuves de cyclage thermique et la stratégie de test stabilisés, il devient beaucoup plus simple de formaliser le tout dans une [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

Si vous travaillez sur un projet UCIe, EMIB ou autre substrat bridge pour chiplet, l'étape suivante consiste généralement à transformer "advanced packaging assembly" en données réellement fabricables :

- Quand le point principal est la zone bridge, les microvias et les détails locaux très fins, utiliser les filières [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) et [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) pour verrouiller les limites process locales.
- Quand l'objectif pilote est de valider la fenêtre bridge, le warpage et l'underfill, intégrer ces contrôles très tôt dans la revue [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Quand la cohérence inter-lots et la reconstruction des défaillances sont critiques, définir dès le départ coupes, X-ray, lots matière et traçabilité des paramètres.
- Quand la fenêtre bridge, les tests par niveaux et les exigences de cyclage thermique sont stabilisés, transférer l'ensemble vers [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) ou [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### La principale difficulté d'un substrat bridge pour chiplet est-elle la densité de routage ?

Pas seulement. Le sujet le plus difficile est souvent la fenêtre locale d'assemblage de la zone bridge, avec le warpage, l'underfill, le cyclage thermique et la logique de tests par niveaux.

### Pourquoi les structures de type EMIB rendent-elles l'assemblage plus sensible ?

Parce qu'EMIB utilise un petit bridge silicium intégré au substrat pour une interconnexion locale à très haute densité. La planéité locale, l'ordre de placement, les contraintes sur la bridge et l'underfill deviennent alors plus critiques.

### Ajouter de l'underfill améliore-t-il automatiquement la fiabilité ?

Non. Si le remplissage est incomplet, voidé ou mal équilibré en contraintes après polymérisation, l'underfill peut devenir lui-même une source de défaillance.

### Pourquoi planifier si tôt les tests par niveaux et la traçabilité ?

Parce qu'un grand nombre de défauts sur les substrats bridge sont des défauts cachés. Sans séparation die / package / système et sans traçabilité lot, l'analyse racine devient lente et ambiguë.

### Que faut-il figer en priorité avant fabrication ou pilote ?

Il faut d'abord figer la fenêtre d'assemblage de la zone bridge, le contrôle du warpage, la stratégie underfill, la structure de tests par niveaux, la validation au cyclage thermique et la chaîne de traçabilité des défaillances.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [Specifications | UCIe Consortium](https://www.uciexpress.org/specifications)  
   Référence utilisée pour les points relatifs à UCIe comme standard ouvert d'interconnexion die-to-die au niveau package couvrant couche physique, pile protocolaire, pile logicielle et conformité.

2. [Intel® Stratix® 10 FPGAs Overview - Intel EMIB Packaging Technology](https://www.intel.com/content/www/us/en/products/details/fpga/stratix/10/article.html)  
   Référence utilisée pour l'affirmation selon laquelle EMIB utilise un petit bridge silicium intégré au substrat sans grand interposeur silicium.

3. [Advanced Packaging Innovations | Intel Foundry Packaging](https://www.intel.com/content/www/us/en/foundry/packaging.html)  
   Référence pour la discussion sur les tests chiplet avancés par étapes avec wafer sort, die sort, burn-in, final test, system-level test et known good die avant assemblage final.

4. [EMIB Technology Brief | Intel](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf)  
   Utilisé pour compléter la discussion sur les bridges intégrés dans les cavités du substrat, les flux d'assemblage package standard et le microbump pitch plus serré localisé à la zone bridge.

<a id="author"></a>
## Auteur et validation technique

- Auteur : équipe contenu advanced packaging et assemblage haute densité de HILPCB
- Validation technique : équipe ingénierie process PCB, assemblage, thermo-mécanique et analyse de défaillance
- Dernière mise à jour : 2025-11-19

---
title: "Comment router une paire différentielle PCB : règles pratiques sur l’impédance, le plan de référence, le skew et les vias"
description: "Une réponse directe sur l’impédance cible, la continuité du plan de référence, la symétrie, la compensation de longueur, les via stubs et la validation de fabrication à examiner en premier."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# Comment router une paire différentielle PCB : règles pratiques sur l’impédance, le plan de référence, le skew et les vias

- **Le premier point à verrouiller n’est pas l’égalité absolue des longueurs, mais la cible définie par le standard ou le datasheet.** NXP demande **85 ohms différentiels** pour eUSB2 PTN3222, tandis que l’AN13335 pour l’Ethernet automobile route le MDI à **100 ohms**.
- **La symétrie compte plus qu’un simple faible écartement.** Intel AN528 rappelle que les deux lignes doivent être électriquement équivalentes, sinon la conversion différentiel-vers-commun apparaît.
- **La continuité du plan de référence et les changements de couche cassent souvent le lien avant le segment droit lui-même.**
- **Serpentins, anti-pads et via stubs ne doivent jamais être appliqués comme un modèle générique.**
- **Une paire différentielle n’est industrialisable que si stackup, tolérances, breakout et validation sont définis ensemble.**

> **Quick Answer**  
> Le cœur du routage d’une paire différentielle PCB est de maintenir un environnement de propagation symétrique dans le vrai stackup, avec la vraie épaisseur de cuivre et les vraies transitions. Il faut d’abord figer l’impédance cible et le budget de skew, puis contrôler le routage sur une même couche, la continuité du plan de référence, les vias symétriques et la compensation de longueur, avant de vérifier la carte fabriquée par coupon, TDR ou test système.

## Table des matières

- [Que faut-il examiner d’abord pour une paire différentielle PCB ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi faut-il définir la paire différentielle à partir du standard et du stackup ?](#standards-stackup)
- [Pourquoi symétrie, skew et serpentins sont-ils si souvent mal utilisés ?](#symmetry-skew)
- [Pourquoi le plan de référence, les changements de couche et les via stubs sont-ils des zones à risque ?](#planes-vias)
- [Comment valider le routage avant la production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord pour une paire différentielle PCB ?

Commencer par **la cible d’impédance de l’interface, le stackup, le plan de référence, la symétrie et la stratégie de changement de couche**.

Le sujet ne signifie ni "tirer deux pistes en parallèle", ni "router d’abord puis demander l’impédance plus tard". Les protocoles, PHY et connecteurs n’utilisent pas les mêmes règles. NXP AN13462 fixe eUSB2 à **85 ohms différentiels** et interdit les plane splits sur le trajet rapide. NXP AN13335 impose **100 ohms** pour le MDI Ethernet automobile et limite le déséquilibre interne à **1 mm** entre connecteur et choke. Intel 82566 ajoute **100 ohms différentiels (±20%)** avec moins de **50 mil** d’écart dans la paire.

Il faut donc d’abord confirmer :

1. **Si l’interface demande 85, 90, 95 ou 100 ohms différentiels**
2. **D’où vient le budget de skew autorisé dans la paire**
3. **Si la ligne est en microstrip ou stripline et si le plan de référence reste continu**
4. **Si les changements de couche sont permis et comment retour et stubs seront traités**
5. **Si le fabricant peut tenir cette géométrie sur le stackup visé**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / Paramètre | Méthode | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
|---|---|---|---|---|
| Impédance cible | La confirmer d’abord depuis le standard ou le datasheet | Toutes les paires différentielles ne sont pas à 100 ohms | Standard, datasheet, revue de stackup | Largeur et espacement partent faux |
| Symétrie | Garder le même environnement et les mêmes transitions | L’asymétrie crée de la mode conversion | Revue de layout, revue 3D des transitions | Plus de bruit en mode commun |
| Routage sur une même couche | Garder la paire sur une seule couche si possible | Les changements de couche ajoutent des discontinuités | Revue post-route, nombre de vias | Plus de skew et de réflexions |
| Plan de référence | Le garder continu, proche et cohérent | Un split casse le retour de courant | Revue des planes | Plus d’EMI et de conversion de mode |
| Compensation de longueur | Seulement selon le budget interface, près du point de mismatch | Un mauvais serpentin crée de l’ondulation d’impédance | Revue skew, TDR, simulation | Le correctif crée un nouveau problème |
| Via / stub | Réduire les vias; si changement de couche, prévoir signal via + GND vias symétriques | La via discontinuity reste un risque majeur | TDR, coupe micrographique, revue backdrill | Réflexion locale, ISI, détour de retour |

<a id="standards-stackup"></a>
## Pourquoi faut-il définir la paire différentielle à partir du standard et du stackup ?

Conclusion : **l’impédance cible et la géométrie ne sont pas un modèle universel ; elles résultent à la fois de l’interface et du stackup réel de fabrication.**

Les documents publics NXP et Intel le montrent clairement. eUSB2 est à **85 ohms**, l’Ethernet automobile MDI à **100 ohms**, et les interfaces true differential I/O d’Intel restent elles aussi dans un contexte **100 ohms**. L’ordre de travail correct est donc généralement :

1. **Figer la cible depuis le standard, le datasheet ou le design de référence**
2. **Choisir microstrip ou stripline selon perte, connecteur et EMI**
3. **Valider matériau, épaisseur diélectrique, cuivre et compensation avec le fabricant**
4. **Ensuite seulement, écrire largeur, espacement et tolérance dans les règles de layout**

<a id="symmetry-skew"></a>
## Pourquoi symétrie, skew et serpentins sont-ils si souvent mal utilisés ?

Conclusion : **parce que beaucoup d’équipes prennent l’égalité de longueur pour une preuve de bon routage, tout en oubliant la symétrie structurelle et l’évolution du couplage local.**

Intel AN528 rappelle qu’une paire idéale exige à la fois des lignes électriquement identiques et un skew aussi proche de zéro que possible. Cela signifie :

- **La symétrie inclut longueur, section, diélectrique, cuivre voisin et transitions**
- **Le skew dépend aussi de l’environnement de référence**
- **Un serpentin mal placé peut avoir une impédance pire que la ligne principale**

Intel AN875 ajoute que les trombones de compensation peuvent créer des zones faiblement couplées et une vitesse de propagation différente. NXP recommande donc de compenser près de la zone où le mismatch apparaît.

<a id="planes-vias"></a>
## Pourquoi le plan de référence, les changements de couche et les via stubs sont-ils des zones à risque ?

Conclusion : **dès qu’une paire change de couche, traverse un split ou laisse un stub, le premier risque se trouve souvent dans le chemin de retour et la discontinuité locale.**

NXP interdit les plane splits sur les paires rapides et recommande le moins de vias possible. Intel complète avec trois points pratiques :

- Le reste de fût de via agit comme un stub capacitif
- Un changement de couche a besoin de GND vias proches pour le retour
- Les deux lignes doivent garder une structure de via symétrique

Les zones les plus critiques sont souvent :

1. **La sortie de breakout BGA**
2. **Le launch du connecteur**
3. **Les zones autour des condensateurs AC coupling et composants common-mode**
4. **Les vias de changement de couche et les anti-pads**
5. **Les through-via stubs non traités dans les cartes plus épaisses**

<a id="validation"></a>
## Comment valider le routage avant la production ?

Conclusion : **une validation utile ne prouve pas seulement que le layout est "en paire" dans le CAD ; elle prouve que la géométrie fabriquée et le comportement système restent valides.**

| Élément de validation | Question principale | Point d’observation |
|---|---|---|
| Revue stackup / impédance | La géométrie cible est-elle fabricable ? | Largeur, espacement, cuivre, diélectrique, tolérance |
| Coupon / TDR | L’impédance réelle et les transitions restent-elles proches de la cible ? | Plateau d’impédance, discontinuités locales, effet via |
| Coupe micrographique | Le pressage et la gravure ont-ils déplacé la structure ? | Largeur réelle, cuivre, diélectrique, anti-pad |
| Test système | La paire reste-t-elle saine avec vrais composants et connecteurs ? | Eye diagram, training, BER, EMI |
| Comparaison multi-cartes | Le risque vient-il du design ou de la variation de build ? | Dispersion inter-cartes, cohérence de lot |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Fermer d’abord stackup, couches et stratégie de référence via [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) et [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).
- Utiliser l’[Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) avant le routage.
- Si le breakout est dense, revoir aussi la fenêtre de fanout et de vias de [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Envoyer stackup, table d’impédance, paires clés et méthode de validation directement dans [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) ou [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Les paires différentielles sont-elles toujours à 100 ohms par défaut ?

Non. eUSB2, par exemple, vise 85 ohms, alors que beaucoup d’interfaces Ethernet ou I/O rapides sont à 100 ohms.

### L’égalité de longueur suffit-elle ?

Non. Sans symétrie électrique du plan de référence, du cuivre voisin, des vias et des anti-pads, la mode conversion reste possible.

### Une paire différentielle ne doit-elle jamais changer de couche ?

Pas forcément, mais il faut limiter ces changements et les traiter comme une structure complète avec vias signal, vias GND, anti-pads et retour.

### Faut-il concentrer tous les serpentins en un seul endroit ?

Généralement non. La compensation doit rester proche du point de désaccord et ne pas devenir elle-même une nouvelle discontinuité.

### Pourquoi un plane split gêne-t-il aussi une paire différentielle ?

Parce qu’une paire différentielle ne travaille pas sans plan de référence. Un split modifie le chemin de retour et augmente le bruit en mode commun.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   Étaye les points sur la symétrie électrique, le faible skew et l’effet du fiber weave.

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   Étaye le risque d’ondulation d’impédance et de mode conversion avec les trombones.

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   Étaye la discussion sur via stubs, vias symétriques et GND vias pour le retour.

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   Étaye les contrôles de production sur 100 ohms, mismatch, distance GND via et stubs.

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   Étaye les exigences eUSB2 de 85 ohms, symétrie, matching et évitement des splits.

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   Étaye le contexte 100 ohms MDI, symétrie de masse et risque de common mode.

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   Étaye le contexte 100 ohms et l’usage éventuel du backdrill.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB pour interconnexions haut débit et SI
- Relecture technique : équipes process PCB, intégrité du signal et connecteurs
- Dernière mise à jour : 2025-11-18

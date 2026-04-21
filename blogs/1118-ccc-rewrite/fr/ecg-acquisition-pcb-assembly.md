---
title: "Ce qu’il faut contrôler dans l’assemblage PCB d’acquisition ECG : montage faible bruit, propreté et fiabilité wearable"
description: "Une réponse directe sur le chemin de réjection du mode commun, les fuites d’entrée, la propreté, les contraintes mécaniques et la validation fonctionnelle à examiner en premier dans l’assemblage PCB d’acquisition ECG."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Medical PCB assembly", "ECG acquisition PCB", "Wearable device PCB", "Low-noise PCB design", "ECG patch", "Clinical wearable"]
---

# Ce qu’il faut contrôler dans l’assemblage PCB d’acquisition ECG : montage faible bruit, propreté et fiabilité wearable

- **L’objectif d’une carte d’acquisition ECG n’est pas seulement "elle démarre", mais "la chaîne faible bruit reste valide en production".**
- **La réjection du mode commun et la boucle RLD ne peuvent pas rester seulement sur le schéma.**
- **Les zones d’entrée à haute impédance sont très sensibles aux résidus, à l’humidité et aux manipulations.**
- **Les structures flex et rigid-flex peuvent réinjecter directement des contraintes mécaniques dans la chaîne analogique.**
- **La validation doit inclure une vraie vérification de chaîne de signal et des enregistrements traçables.**

> **Quick Answer**  
> Le cœur de l’assemblage PCB d’acquisition ECG consiste à préserver un front-end analogique haute impédance et faible bruit après pose, nettoyage, retouche, contraintes mécaniques et intégration système. Les vrais points à contrôler ne sont pas seulement les soudures, mais la réjection du mode commun, les fuites d’entrée, la propreté, les contraintes structurelles et la validation fonctionnelle traçable.

## Table des matières

- [Que faut-il examiner d’abord dans l’assemblage PCB d’acquisition ECG ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi le risque d’assemblage ECG dépasse-t-il les simples défauts de soudure ?](#assembly-risk)
- [Pourquoi propreté, résidus et entrées haute impédance doivent-ils être gérés ensemble ?](#cleanliness)
- [Comment flex, radio et alimentation réinjectent-ils du bruit dans les canaux ECG ?](#mechanics-noise)
- [Comment valider l’assemblage ECG avant la production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord dans l’assemblage PCB d’acquisition ECG ?

Commencer par **le type d’électrode, le chemin de réjection du mode commun, la protection des nœuds haute impédance, les contraintes mécaniques et la méthode de validation**.

Le sujet ne se résume pas à "mieux poser les composants". Les notes TI montrent que le bruit 50/60Hz en ECG se couple via la peau, les câbles d’électrode, les réseaux de protection et les déséquilibres RC sur la carte. RLD, blindage Faraday, isolation et traitement aval aident, mais ne remplacent pas le contrôle d’assemblage.

Une séquence d’examen robuste est généralement :

1. **D’abord confirmer s’il s’agit d’électrodes humides, sèches ou patch**
2. **Ensuite identifier les points sensibles d’assemblage autour de l’AFE, du RLD, du lead-off et de la protection d’entrée**
3. **Puis choisir un process no-clean ou nettoyable et fixer les limites de retouche**
4. **Puis vérifier si flex, Bluetooth, batterie et charge réinjectent du bruit dans l’analogique**
5. **Enfin définir ensemble les tests fonctionnels et la traçabilité**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / paramètre | Comment juger | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
|---|---|---|---|---|
| Type d’électrode | Distinguer humide, sèche, patch ou multi-voie | L’impédance et la sensibilité d’assemblage changent fortement | Revue besoin, choix AFE, revue mécanique | Budget bruit et propreté mal posé |
| Chemin mode commun | Examiner ensemble RLD, résistances de protection, déséquilibre RC et blindage | Le bruit secteur dépend de toute la chaîne | Revue schéma + test bruit après assemblage | Hausse du 50/60Hz |
| Protection des nœuds haute impédance | Éviter résidus, humidité et retouches répétées en entrée | La haute impédance amplifie vite les fuites | Contrôle propreté, limites retouche, comparaison bruit | Dérive de baseline et bruit intermittent |
| Zone flex et connecteurs | Revoir composants, renforts, zone de pliage et soudures ensemble | La mécanique affecte la stabilité basse fréquence | Test flexion, visuel, revalidation | Dérive, rupture ou faux contact |
| Modules radio et puissance | Considérer Bluetooth, charge et PMIC comme sources de bruit | Le bruit numérique et de découpage peut revenir dans l’AFE | Tests en états de fonctionnement | Correct au labo, bruité en usage réel |
| Test fonctionnel et traçabilité | Lier les résultats au board ID et au lot | L’analyse de panne sinon devient lente | MES / logs / lot records | Root cause difficile à isoler |

<div style="background: linear-gradient(135deg, #f3f7f6 0%, #eef2f8 100%); border: 1px solid #d6dce8; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #5a8ca8; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #41697f; font-weight: 700;">CMR Is Assembly-Sensitive</div>
      <div style="margin-top: 8px; color: #243640;">La réjection du mode commun ECG n’est pas fixée par la puce seule. Quand s’additionnent impédance d’électrode, câblage, réseau de protection et déséquilibre carte, la variation d’assemblage devient du bruit secteur visible.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4f7d6b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #375a4d; font-weight: 700;">Cleanliness Protects Input Leakage</div>
      <div style="margin-top: 8px; color: #23352f;">Dans les zones d’entrée ECG à haute impédance, il faut piloter ensemble résidus, humidité et nombre de retouches. Avec des électrodes sèches, ces écarts deviennent rapidement de la dérive visible.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #7d6d56; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #635543; font-weight: 700;">Wearables Add Mechanics</div>
      <div style="margin-top: 8px; color: #3a3127;">Un dispositif porté sur la peau n’est pas qu’un sujet PCB. Si flex, renforts, connecteurs et charge ne sont pas figés tôt, les contraintes mécaniques reviendront dans la chaîne de signal.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #8c5f7c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6d4961; font-weight: 700;">Test What Ships</div>
      <div style="margin-top: 8px; color: #3d2535;">AOI et test de mise sous tension ne suffisent pas. Il faut vérifier bruit, baseline et lead-off dans les conditions réelles d’alimentation, de radio et de contact électrode.</div>
    </div>
  </div>
</div>

<a id="assembly-risk"></a>
## Pourquoi le risque d’assemblage ECG dépasse-t-il les simples défauts de soudure ?

Conclusion : **la vraie difficulté n’est pas de souder les composants, mais de garder fermée toute la chaîne faible bruit après assemblage.**

Le document TI `Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier` montre que la conversion mode commun vers différentiel dépend conjointement de l’impédance d’électrode, de l’impédance câble et du réseau d’entrée. Même avec des composants à 1 %, la CMR système peut chuter sensiblement.

Implications directes pour l’assemblage :

- **Chaque retouche près de l’AFE peut dégrader la symétrie**
- **Protection d’entrée, chemin RLD et réseau lead-off doivent être contrôlés sur la carte assemblée**
- **Un blindage ou une masse câble assemblés de façon variable feront dériver le bruit secteur d’un lot à l’autre**

<a id="cleanliness"></a>
## Pourquoi propreté, résidus et entrées haute impédance doivent-ils être gérés ensemble ?

Conclusion : **parce que l’entrée ECG est souvent une chaîne haute impédance, basse fréquence et faible amplitude, où une petite fuite devient vite visible.**

Analog Devices rappelle qu’une électrode humide peut être autour de **10kOhm**, tandis qu’une électrode sèche peut être **100 à 1000 fois** plus haute, par exemple **10MOhm**. À ce niveau, courant de biais, résidus et humidité prennent beaucoup plus d’importance.

En pratique, côté assemblage, cela concerne directement :

- la présence de flux ou de résidus ioniques dans la zone d’entrée
- l’efficacité réelle du nettoyage sous les boîtiers denses
- le séchage et le stockage vis-à-vis du retour d’humidité
- l’effet des retouches sur l’état de surface autour des nœuds haute impédance

| Scénario | Logique process plus adaptée | Points de confirmation |
|---|---|---|
| Électrodes humides, peu de voies, proto | Nettoyage plus simple possible, mais avec retest bruit | Nombre de retouches, baseline après nettoyage |
| Électrodes sèches, wearable | Définir le process depuis la logique haute impédance | Fuite d’entrée, bruit après humidité, répétabilité |
| Version flex ou rigid-flex | Examiner nettoyage et séchage avec la mécanique | Bords de renfort, zone connecteur, retest après pliage |

<a id="mechanics-noise"></a>
## Comment flex, radio et alimentation réinjectent-ils du bruit dans les canaux ECG ?

Conclusion : **dans un wearable ECG, la source de bruit réelle ne se limite souvent pas à l’entrée AFE. Batterie, Bluetooth, charge, blindage et flex peuvent ramener le problème via l’assemblage.**

Les sous-ensembles typiques sont :

- Bluetooth RF et antenne
- gestion de charge ou charge sans fil
- PMIC / DCDC / LDO
- connecteurs flex ou FPC
- boîtier, blindage et mousses conductrices

Pour l’équipe d’assemblage, les points à figer explicitement sont :

1. **Peut-on encore déplacer ou substituer le front-end analogique, le RLD ou le chemin de blindage ?**
2. **Les zones flex, connecteurs et renforts sont-ils éloignés des nœuds sensibles ?**
3. **Des retests bruit ont-ils été faits avec radio, charge et affichage actifs ?**
4. **Le blindage, les ressorts de masse et les contacts conducteurs sont-ils répétables en série ?**

<a id="validation"></a>
## Comment valider l’assemblage ECG avant la production ?

Conclusion : **le plus important n’est pas de multiplier les essais, mais de tester dans des conditions proches du produit livré.**

Le contexte public de l’IEC 60601-2-47 couvre safety et essential performance pour les systèmes ECG ambulatoires. Pour l’assemblage, cela signifie qu’il ne faut pas s’arrêter à l’AOI, au rayon X ou à l’ICT.

Un chemin de validation plus utile comprend en général :

| Point de validation | Ce qu’il vérifie | Points d’observation |
|---|---|---|
| Mise sous tension et fonction de base | L’assemblage fondamental est-il complet ? | Communication AFE, lead-off, tension de référence, courant statique |
| Bruit analogique et baseline | L’assemblage a-t-il dégradé la chaîne faible bruit ? | Bruit entrée ouverte, bruit secteur, stabilité de baseline |
| Essai en états de fonctionnement | Les autres modules polluent-ils l’ECG ? | Bluetooth, charge, écran, vibration |
| Retest fiabilité mécanique | Le port, la flexion ou les connexions créent-ils de nouveaux défauts ? | Zones flex, connecteurs, renforts, boîtier |
| Traçabilité | Pourra-t-on analyser plus tard les écarts de lot ? | Board ID, lots composants, paramètres process, résultats de test |

Avant un lot de validation, il faut généralement préparer au moins :

1. Structure de lead ECG, AFE utilisé et schéma RLD / lead-off  
2. Type d’électrode et forme d’usage  
3. Présence ou non de Bluetooth, charge, flex ou rigid-flex  
4. Critères de bruit, baseline et fonctionnement  
5. Exigences de traçabilité pour board ID, lot, nettoyage / retouche et test final

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Pour figer d’abord l’AFE et la fenêtre d’assemblage, commencer par [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Si le projet comporte des zones flex, une structure au contact peau ou du rigid-flex, examiner aussi [Rigid-Flex PCB](https://hilpcb.com/en/products/rigid-flex-pcb).
- Avant prototype et lot de validation, intégrer zones haute impédance, stratégie de propreté et retest bruit dans la phase [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Si vous voulez fermer en une boucle assemblage, matière entrante, test fonctionnel et traçabilité, l’écrire directement dans [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Pourquoi AOI et mise sous tension ne suffisent-ils pas pour une carte ECG ?

Parce que beaucoup de problèmes ECG ne sont pas de simples courts-circuits ou circuits ouverts, mais du bruit secteur, de la dérive de baseline, des fuites d’entrée ou des effets mécaniques.

### Pourquoi l’ECG à électrodes sèches est-il plus sensible à l’assemblage ?

Parce que l’impédance peut être 100 à 1000 fois plus élevée que celle d’électrodes humides classiques. Les effets de résidus, humidité et courants de biais sont donc plus amplifiés.

### Faut-il toujours nettoyer une carte ECG ?

Pas forcément, mais le no-clean ne doit pas être considéré comme un choix sûr par défaut. La décision dépend du type d’électrode, du layout haute impédance, de l’environnement wearable et de la stratégie de retouche.

### Une bonne boucle RLD suffit-elle à éliminer l’effet de l’assemblage sur le bruit secteur ?

Non. Le RLD améliore la réjection du mode commun, mais la contamination, un mauvais contact de blindage ou des écarts d’assemblage peuvent encore augmenter le 50/60Hz.

### Pourquoi la traçabilité d’un ECG médical ou wearable doit-elle aller jusqu’à la carte ?

Parce que les dérives de bruit et de stabilité viennent souvent de petits écarts entre lots, retouches ou structure mécanique, difficiles à isoler sans données carte par carte.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [TI AFE4960 Datasheet](https://www.ti.com/lit/ds/symlink/afe4960.pdf)  
   Étaye le contexte sur ECG, respiration, pace detection et l’usage dans des systèmes liés à IEC 60601-2-47 / 60601-2-27.

2. [TI Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier](https://www.ti.com/lit/pdf/sbaa188)  
   Étaye les conclusions sur les sources de bruit 50/60Hz, le rôle du RLD, du blindage Faraday, de l’isolation et du déséquilibre.

3. [TI Understanding Lead-Off Detection in ECG](https://www.ti.com/lit/pdf/sbaa196)  
   Étaye la place du lead-off dans la chaîne de validation ECG.

4. [Analog Devices: How to Add Wilson’s Central Terminal/Right Leg Drive Functions to the MAX30001/MAX30003 ECG AFEs in a Medical Wearable](https://www.analog.com/en/resources/design-notes/how-to-add-wilsons-central-terminalright-leg-drive-functions.html)  
   Étaye le contexte sur WCT / RLD, la suppression 50Hz / 60Hz et la stabilité du shield drive.

5. [Analog Devices: High-Impedance and Low-Noise Op Amps Enable Dry Electrodes in Medical Systems](https://www.analog.com/en/resources/design-notes/highimpedance-and-lownoise-op-amps-enable-dry-electrodes-in-medical-systems.html)  
   Étaye le contexte sur la forte impédance des électrodes sèches et l’importance d’une entrée haute impédance et faible bruit.

6. [IEC 60601-2-47 Standard Listing](https://standards.iteh.ai/catalog/standards/iec/e9f39061-7265-48e4-9bda-3b71d1af3eba/iec-60601-2-47-2001)  
   Étaye le contexte public sur safety, essential performance, EMC et exactitude des systèmes ECG ambulatoires.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB électronique médicale et wearable
- Relecture technique : équipe process assemblage PCB et hardware faible bruit
- Dernière mise à jour : 2025-11-18

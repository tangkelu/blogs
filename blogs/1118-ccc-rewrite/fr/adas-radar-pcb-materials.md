---
title: "Comment choisir les matériaux d’un PCB radar ADAS : performance 77/79GHz, stackup hybride et fiabilité automobile"
description: "Une réponse directe sur le comportement low-loss, la rugosité du cuivre, la compatibilité de lamination hybride, la finition de surface et la validation à examiner en premier pour un PCB radar ADAS."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["ADAS radar PCB", "Automotive PCB", "High-frequency PCB", "PCB materials", "77GHz radar PCB", "mmWave PCB"]
---

# Comment choisir les matériaux d’un PCB radar ADAS : performance 77/79GHz, stackup hybride et fiabilité automobile

- **Il faut d’abord regarder la stabilité du matériau, pas seulement un chiffre de perte typique très bas.**
- **La rugosité du cuivre amplifie directement la perte d’insertion et la dérive de phase en millimeter-wave.**
- **La voie correcte pour beaucoup de cartes radar ADAS n’est pas "tout en PTFE", mais un hybride RF + FR-4.**
- **Matériau, cuivre et finition doivent être revus ensemble.**
- **Un prototype réussi ne suffit pas à prouver la maturité industrielle.**

> **Quick Answer**  
> Le cœur du choix des matériaux pour un PCB radar ADAS n’est pas seulement de chercher le stratifié "le plus faible perte". Il faut confirmer ensemble la stabilité Dk/Df à 76-81GHz, la rugosité du cuivre, la compatibilité du stackup hybride, l’effet de la finition et la validation automobile. Une carte radar n’est solide que lorsque performance électrique, fenêtre de fabrication et fiabilité restent cohérentes en même temps.

## Table des matières

- [Que faut-il examiner d’abord pour les matériaux d’un PCB radar ADAS ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi la faible perte n’est-elle pas le seul critère ?](#low-loss)
- [Pourquoi rugosité du cuivre, finition et diélectriques minces amplifient-ils la perte ensemble ?](#copper-finish)
- [Comment juger si un stackup hybride est prêt pour la série ?](#hybrid-stackup)
- [Comment valider la stratégie matériau avant la production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord pour les matériaux d’un PCB radar ADAS ?

Commencer par **la bande de fonctionnement, la stabilité Dk/Df, la rugosité du cuivre, la compatibilité hybride et la méthode de validation**.

La question ne signifie ni "quel matériau HF est le meilleur", ni "77GHz impose toujours du PTFE". Les documents publics de Rogers montrent que le radar automobile travaille déjà à 77GHz, 79GHz et plus largement à 76-81GHz. À ce niveau, l’enjeu n’est pas seulement une faible perte, mais aussi la cohérence de phase, l’uniformité du matériau et la répétabilité de fabrication.

Il faut généralement distinguer :

1. **Quelles couches sont réellement RF ou antenne, et quelles couches sont numérique, contrôle ou puissance**
2. **Si la priorité est la perte minimale, la dérive de phase minimale ou un compromis coût-process plus équilibré**
3. **Si le design a besoin d’un stackup hybride RF + FR-4**
4. **Si la rugosité du cuivre, la finition et le process microvia annulent le gain attendu en mmWave**
5. **Si le fournisseur peut fournir traçabilité de lot, revue hybride et données de validation représentatives**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / Paramètre | Méthode | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
|---|---|---|---|---|
| Bande de fonctionnement | Confirmer 24GHz, 77GHz, 79GHz ou 76-81GHz | Plus la fréquence monte, plus perte, phase et variation process deviennent sensibles | Spécification, budget RF, modèle antenne | Mauvaise famille matériau dès le départ |
| Stabilité Dk | Examiner tolérance et dérive, pas seulement la valeur typique | Elle pilote impédance, phase et cohérence d’array | Datasheet, TCDk, revue de lot | Dispersion canal à canal plus élevée |
| Df / perte d’insertion | L’évaluer avec l’épaisseur, le cuivre et la géométrie | Le même Df ne se comporte pas pareil selon la structure | S-paramètres, coupons | Faible perte nominale mais carte trop dissipative |
| Rugosité cuivre | Priorité à rolled copper ou VLP / LoPro pour les couches RF | Les pertes conducteurs et erreurs de phase s’amplifient en mmWave | Specs matériau et cuivre | Plus de perte et plus de dérive de lot |
| Compatibilité hybride | Vérifier cap layer RF + FR-4 multilayer | La plupart des cartes radar n’utilisent pas un seul matériau partout | Revue de stackup, lamination, perçage | Warp, registration ou fiabilité inter-couches |
| Finition de surface | Ne pas traiter la finition RF comme un choix CAM tardif | Le nickel et son épaisseur influencent perte et phase | Revue finish, comparaison coupon | Perte supplémentaire et moins bonne cohérence |
| Fiabilité automobile | Évaluer humidité, cycles thermiques et compatibilité lead-free | Environnement véhicule et stress d’assemblage sont plus sévères | Méthodes IPC, humidité, cyclage | Le labo fonctionne, pas la validation série |

<a id="low-loss"></a>
## Pourquoi la faible perte n’est-elle pas le seul critère ?

Conclusion : **sur une carte radar ADAS, la priorité correcte est souvent la stabilité et la prévisibilité avant la perte nominale la plus basse.**

Les documents publics Rogers montrent que le radar automobile 77GHz et 79GHz doit tenir non seulement les exigences RF, mais aussi température et environnement. RO3003 est présenté avec une stabilité Dk, un faible Df, un bon TCDk et une faible absorption d’humidité. L’idée n’est donc pas seulement "faible perte", mais aussi "comportement stable dans le temps et l’environnement".

Isola Astra MT77 illustre une autre voie publique, plus équilibrée entre coût, performance HF et compatibilité process. Le bon choix dépend donc de la longueur d’antenne, du budget de perte des feeds, du nombre de couches, de la complexité numérique et de la route de fabrication.

<a id="copper-finish"></a>
## Pourquoi rugosité du cuivre, finition et diélectriques minces amplifient-ils la perte ensemble ?

Conclusion : **en millimeter-wave, cuivre et finition ne sont pas des détails de post-process, mais une partie intégrale de la stratégie matériau.**

Rogers explique publiquement qu’un cuivre plus rugueux augmente la perte conducteur et fait se comporter l’onde comme si le Dk effectif était plus élevé. L’effet devient encore plus visible avec des diélectriques fins. Les comparaisons publiques entre ED copper, rolled copper et VLP ED copper vont dans le même sens.

La finition ne doit pas non plus être décidée en fin de CAM. Un ENIG avec nickel peut ajouter perte d’insertion et variation de phase en mmWave. Il faut donc juger ensemble :

- largeur de piste RF et distribution du courant
- structure microstrip ou GCPW
- sensibilité de l’array à la cohérence de phase
- contraintes d’assemblage et de fiabilité

<a id="hybrid-stackup"></a>
## Comment juger si un stackup hybride est prêt pour la série ?

Conclusion : **la vraie question n’est généralement pas de savoir si un échantillon peut être fabriqué, mais si couches RF et couches FR-4 peuvent être laminées ensemble de façon stable dans le temps.**

RO4830 et RO4830 Plus sont publiquement positionnés comme matériaux cap layer pour des multilayers FR-4 dans le radar automobile 76-81GHz. Cela permet :

- **aux couches RF** d’utiliser un système plus faible perte et plus lisse
- **aux couches numérique, contrôle et puissance** de rester sur des matériaux FR-4 plus maîtrisés
- **à la fabrication globale** de rester proche d’un process multilayer de type FR-4

Mais l’hybride n’est pas sans risque. Il faut donc demander au fournisseur :

- si le matériau RF a déjà été validé avec le core et le prepreg FR-4 visés
- s’il existe une vraie expérience de perçage, desmear, microvia et finition sur hybride multilayer
- si la série exigera une fenêtre de lamination ou de perçage plus serrée qu’un job FR-4 classique
- si les lots matière peuvent être tracés et maintenus cohérents entre proto, NPI et série

<a id="validation"></a>
## Comment valider la stratégie matériau avant la production ?

Conclusion : **la validation ne doit pas seulement montrer qu’un matériau paraît bon en théorie, mais qu’il garde performance mmWave et stabilité structurelle après fabrication réelle.**

IPC TM-650 fournit le cadre général pour Dk, Df, TDR, perte de signal et cyclage thermique. Pour le radar ADAS, la validation utile ressemble surtout à une validation groupée :

| Élément de validation | Ce qu’il valide le mieux | Point d’observation |
|---|---|---|
| Coupons Dk/Df et perte | Le matériau remplit-il réellement le budget RF ? | Même géométrie, même finish, même cuivre |
| Coupon RF ou ligne test | Perte réelle des feeds et stabilité de phase | Diélectrique fin, rugosité différente, finish différent |
| Revue structure hybride | Lamination et perçage restent-ils sains ? | Warp, registration, qualité de trou, microvia |
| Validation environnement / assemblage | Compatibilité véhicule et lead-free | Cyclage, humidité, comportement après reflow |
| Reprise de cohérence par lot | Le design est-il adapté à NPI et SOP ? | Variation lot à lot de perte, phase et yield |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Pour les couches RF et les feeds antenne, commencer par [High-Frequency PCB](https://hilpcb.com/en/products/high-frequency-pcb).
- Si Rogers ou une famille équivalente est déjà choisie, revoir lamination hybride, perçage et finish via [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb).
- Lors du passage du proto au lot de validation, intégrer stackup, matériau, cuivre et finish dans [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Une fois matériau, structure et validation convergés, les pousser directement dans [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Un PCB radar ADAS doit-il être entièrement en PTFE ?

Non. Beaucoup de cartes 76-81GHz réservent le matériau faible perte aux couches RF critiques et gardent les autres couches en FR-4.

### Pourquoi Df seul ne suffit-il pas à choisir le matériau ?

Parce que le comportement mmWave dépend aussi de la tolérance Dk, du TCDk, de la rugosité du cuivre, de la finition, de l’épaisseur et de la variation process.

### La rugosité du cuivre est-elle vraiment critique sur un radar automobile ?

Oui. Les notes publiques mmWave montrent qu’un cuivre rugueux augmente la perte et déplace le comportement de phase.

### ENIG convient-il à un PCB radar ADAS ?

Avec prudence seulement. Le nickel peut ajouter perte et variation de phase dans les zones RF.

### Comment savoir qu’une carte radar hybride est prête pour la série ?

Il faut au minimum voir des coupons RF représentatifs, une bonne qualité de structure hybride et un comportement stable après essais thermiques, humidité ou assemblage lead-free.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [Rogers Automotive Radar Design Considerations for Autonomous and Safety Systems](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/technical-articles/automotive-radar-design-considerations-for-autonomous-and-safety-systems.pdf)  
   Étaye le contexte radar 77/79GHz et l’importance de la stabilité Dk, du TCDk et de l’humidité.

2. [Rogers RO3003 Laminates](https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates)  
   Étaye les données publiques sur RO3003.

3. [Rogers RO3003G2 Data Sheet](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3003g2--data-sheet.pdf)  
   Étaye le chemin matériau optimisé radar auto et le cuivre VLP ED.

4. [Rogers RO4830 Plus Laminates Data Sheet](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4830-plus-laminates-data-sheet.pdf)  
   Étaye l’usage cap layer 76-81GHz, l’hybride FR-4 et la compatibilité process.

5. [Rogers PCB Design and Fabrication Concerns for Millimeter-Wave Circuits](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/pcb-design-and-fabrication-concerns-for-millimeter-wave-circuits.pdf)  
   Étaye les conclusions sur rugosité du cuivre, finish et cohérence mmWave.

6. [Rogers Steering Circuit Materials for 77 GHz Automotive Radar](https://rogerscorp.com/en/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/steering-circuit-materials-for-77-ghz-automotive-radar.pdf)  
   Étaye la comparaison entre ED copper, rolled copper et VLP ED copper à 77GHz.

7. [Isola Astra MT77 Laminate and Prepreg Data Sheet](https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg.pdf)  
   Étaye l’exemple d’une autre voie matériau publique pour radar.

8. [IPC TM-650 Test Methods Manual](https://www.electronics.org/test-methods)  
   Étaye le cadre général des méthodes Dk, Df, TDR, perte de signal et cyclage thermique.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB haute fréquence et électronique automobile
- Relecture technique : équipes process PCB et ingénierie RF stackup
- Dernière mise à jour : 2025-11-18

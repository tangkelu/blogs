---
title: "Que faut-il vérifier dans l’assemblage PCB d’un étage de puissance GaN : inductance de boucle, thermal pads et cohérence de production"
description: "Une réponse directe sur la boucle de puissance, le Kelvin source, les voids de thermal pad, le cuivre épais et les méthodes de validation à examiner en premier dans l’assemblage PCB d’un étage de puissance GaN."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["GaN power PCB", "Power electronics PCB", "Thermal management", "PCB assembly", "GaN half bridge", "Kelvin source"]
---

# Que faut-il vérifier dans l’assemblage PCB d’un étage de puissance GaN : inductance de boucle, thermal pads et cohérence de production

- **Sur une carte GaN, ce qui se dégrade d’abord n’est souvent pas le composant lui-même, mais l’inductance parasite et le chemin thermique sur la carte.**
- **Un layout "correct" doit rester valide dans un stackup fabricable, pas seulement dans le CAD.**
- **Thermal pads et vias ne sont pas des détails secondaires, mais des variables process majeures.**
- **Le cuivre épais et les grandes zones cuivre apportent à la fois bénéfices et coûts process.**
- **La validation GaN ne peut pas se limiter à une belle capture de waveform.**

> **Quick Answer**  
> Le cœur de l’assemblage PCB d’un étage de puissance GaN n’est pas seulement de souder les composants. Il faut réaliser en même temps une boucle de faible inductance, un retour de gate stable, une structure de thermal pad à faible résistance thermique et une fenêtre d’assemblage répétable. Une carte GaN n’est vraiment industrialisable que si waveform, thermique, qualité de soudure et cohérence inter-lots restent ensemble sous contrôle.

## Table des matières

- [Que faut-il examiner d’abord dans l’assemblage PCB d’un étage de puissance GaN ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi les cartes GaN sont-elles si sensibles à l’inductance parasite et au retour mal contrôlé ?](#loop-control)
- [Pourquoi thermal pads, VIPPO et cuivre épais doivent-ils être revus ensemble ?](#thermal-pads)
- [Pourquoi faut-il lier gate-drive layout et cohérence d’assemblage ?](#gate-drive)
- [Comment valider l’assemblage GaN avant la production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord dans l’assemblage PCB d’un étage de puissance GaN ?

Commencer par **la boucle de puissance principale, la gate loop, le chemin Kelvin source, la structure du thermal pad et la méthode de validation**.

Il ne s’agit pas juste de dire que "la fréquence de commutation est un peu plus élevée". EPC montre clairement qu’à vitesse de commutation plus élevée et densité de puissance plus forte, l’inductance parasite de la boucle de puissance et de la boucle de gate doit être minimisée.

Une séquence robuste est généralement :

1. **Vérifier d’abord la relation physique réelle entre demi-pont et bus capacitor**
2. **Confirmer ensuite que le return plane se ferme directement sous les composants**
3. **Vérifier ensuite que Kelvin source et gate return restent indépendants et stables**
4. **Puis évaluer ensemble thermal pad, vias et épaisseur cuivre pour soudure et thermique**
5. **Enfin définir waveform checks, rayon X et validation thermique comme gates avant série**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / paramètre | Comment juger | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
|---|---|---|---|---|
| Boucle de puissance principale | Coupler étroitement le chemin top au premier return plane interne | Détermine overshoot, ringing et EMI | Revue layout, double-pulse test | Overshoot plus élevé, commutation dégradée |
| Gate loop | Garder résistances ON/OFF, return driver et gate/source compacts | Le GaN est très sensible aux parasites de gate | Waveform gate, contrôle false turn-on | False turn-on, extinction incomplète |
| Kelvin source | Le garder proche du source pad et découplé de la boucle puissance | Réduit common source inductance | Contrôle géométrie, comparaison waveform | Référence driver polluée |
| Thermal pad et vias | Vérifier d’abord la soudure pad, puis position et quantité de vias | Joue sur thermique et fenêtre de soudure | Rayon X, test thermique, microsection | Résistance thermique plus haute, soudure instable |
| Épaisseur et distribution cuivre | Utiliser le cuivre épais en tenant compte du return path et du warpage | Baisse la résistance mais modifie la fenêtre process | Revue stackup, cohérence reflow, planéité | Warpage et variabilité de soudure |
| Stratégie de validation | Vérifier ensemble waveform, thermique, soudure et cohérence inter-cartes | Les problèmes GaN sont souvent combinés | DPT, imagerie thermique, rayon X, comparaison lots | Une démo passe, pas la production |

<div style="background: linear-gradient(135deg, #eef3f8 0%, #f7f2ea 100%); border: 1px solid #d8dde5; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4f79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3b5d7d; font-weight: 700;">Loop First</div>
      <div style="margin-top: 8px; color: #243746;">En GaN, le premier sujet est le vrai chemin de fermeture de la boucle de puissance et de la gate loop. Sans boucle à faible parasite, les bonnes caractéristiques du composant sont vite mangées par overshoot et ringing.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #7b6346; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #624e38; font-weight: 700;">Kelvin Matters</div>
      <div style="margin-top: 8px; color: #352c23;">Le Kelvin source n’est pas décoratif. Dès que la référence du driver est contaminée par la boucle de puissance, le comportement de gate devient difficile à répéter.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4c7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395e51; font-weight: 700;">Thermal Pad Is Process Logic</div>
      <div style="margin-top: 8px; color: #23352e;">Thermal pad, VIPPO, ouverture de stencil et cuivre épais doivent être définis ensemble. Si le chemin thermique ne tient qu’en simulation, la montée en température et la qualité de soudure ne seront pas stables en série.</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #8d5a5a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #704646; font-weight: 700;">Production Beats Demo</div>
      <div style="margin-top: 8px; color: #3d2626;">Le succès en GaN n’est pas une seule démo propre, mais la capacité à garder overshoot, thermique et qualité de soudure dans la même bande de contrôle sur plusieurs cartes et plusieurs lots.</div>
    </div>
  </div>
</div>

<a id="loop-control"></a>
## Pourquoi les cartes GaN sont-elles si sensibles à l’inductance parasite et au retour mal contrôlé ?

Conclusion : **parce que la vitesse du GaN transforme même une petite inductance parasite en pics de tension visibles et en instabilité de gate-drive.**

EPC recommande clairement d’utiliser la première couche interne comme chemin de retour de puissance et de placer le bus capacitor de façon à ce que la boucle principale se referme directement sous les composants. Avec cette approche, l’overshoot peut baisser d’environ **40%** par rapport à un layout MOSFET silicium de référence.

Il ne s’agit pas seulement d’une piste plus large. Il faut en même temps :

- une boucle courte entre bus capacitor et demi-pont
- un return plane directement sous le chemin de puissance
- une gate loop séparée de la boucle de puissance
- une référence Kelvin source proche du vrai retour source

<a id="thermal-pads"></a>
## Pourquoi thermal pads, VIPPO et cuivre épais doivent-ils être revus ensemble ?

Conclusion : **parce que dans les designs GaN, les problèmes thermiques et les problèmes de soudure naissent souvent du même pad et de la même structure cuivre / vias.**

EPC AN031 donne des ordres de grandeur concrets :

- Sans vias, Rtheta,JMA est d’environ **45 K/W**
- Avec vias latéraux, environ **35 K/W**
- Avec **VIPPO** sous le composant, environ **30 K/W**

Le même document indique aussi qu’en combinant plusieurs optimisations, la résistance thermique peut baisser d’environ **30%**, l’une des actions les plus efficaces étant l’ajout de vias sous le composant, ainsi que le passage à **2 oz** de cuivre. Cela rappelle que :

- **La position des thermal vias** influence thermique et comportement de pâte
- **Le cuivre épais** aide la diffusion thermique mais modifie reflow et planéité
- **L’écartement des composants et la position du bus capacitor** jouent aussi sur le co-heating

<a id="gate-drive"></a>
## Pourquoi faut-il lier gate-drive layout et cohérence d’assemblage ?

Conclusion : **parce que la gate loop GaN ne doit pas seulement fonctionner, elle doit garder une géométrie et un retour extrêmement stables sur le hardware réel.**

EPC recommande de garder boucle de puissance et boucle de gate aussi orthogonales que possible et de former le retour Kelvin près du source pad. Pour des composants en parallèle, chaque FET GaN doit garder sa propre résistance de gate.

Exigences directes pour l’assemblage :

- la position relative des résistances de gate et du driver ne doit pas dériver en retouche
- Kelvin source et masse de référence driver ne doivent pas être absorbés dans un gros pad de courant
- les petites résistances, éléments de mesure et composants de protection autour du driver doivent rester compacts et symétriques
- un bon rayon X ou un bon visuel ne garantit pas à lui seul que la géométrie gate loop est correcte

<a id="validation"></a>
## Comment valider l’assemblage GaN avant la production ?

Conclusion : **la validation production GaN doit couvrir en même temps waveform, thermique et qualité de soudure.**

Un chemin de validation utile répond en général à :

| Point de validation | Ce qu’il vérifie | Points d’observation |
|---|---|---|
| Double-pulse test ou waveform de commutation | La boucle principale et la gate loop sont-elles saines ? | Overshoot, ringing, extinction, signe de false turn-on |
| Test thermique | Thermal pad et structure cuivre sont-ils vraiment efficaces ? | Montée en température stabilisée, delta-T, co-heating |
| Rayon X / inspection soudure | Le bottom pad et les joints cachés sont-ils répétables ? | Mouillage, répartition des voids, libération de pâte |
| Comparaison multi-cartes | La fenêtre process est-elle assez large ? | Dispersion carte à carte de waveform et température |
| Retest planéité / structure | Le cuivre épais ajoute-t-il des effets secondaires d’assemblage ? | Warpage, chauffe locale inégale, cohérence des soudures voisines |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Si la priorité est de figer thermal pad, cuivre et chemin thermique, commencer avec [High Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb).
- Si la carte comporte de fortes zones de courant et de forte densité thermique, examiner aussi [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb).
- Avant prototype ou lot de validation, intégrer design du thermal pad, critères rayon X, double-pulse checks et limites de retouche dans la phase [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Une fois stackup, bus capacitor, thermal pads et points de validation figés, les écrire directement dans [Quote / RFQ](https://hilpcb.com/en/quote/) ou le dossier [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Pourquoi les étages de puissance GaN sont-ils plus sensibles au layout et aux variations d’assemblage que les cartes MOSFET ?

Parce que le GaN commute plus vite et que de petites variations d’inductance parasite ou de chemin de retour deviennent immédiatement de l’overshoot, du ringing et un comportement gate instable.

### Faut-il toujours du cuivre épais sur une carte GaN ?

Pas forcément. Le cuivre épais aide sur la résistance et la thermique, mais il modifie aussi gravure, warpage et fenêtre de reflow.

### Plus de vias sous le thermal pad signifie-t-il toujours mieux ?

Non. Position des vias, choix VIPPO, ouverture de stencil et structure du pad doivent être conçus ensemble.

### Le rayon X est-il obligatoire en GaN ?

Pour les boîtiers avec bottom thermal pad, joints cachés ou interfaces thermiques critiques, il est souvent très précieux, car beaucoup de défauts ne se voient pas en extérieur.

### Pourquoi un prototype peut-il sembler bon alors que la production échoue ?

Parce qu’un prototype montre seulement qu’un design a fonctionné une fois dans une condition process donnée. Il ne prouve pas la stabilité inter-cartes et inter-lots.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [EPC GaN First Time Right: Schematic and Recommended Layout](https://epc-co.com/epc/design-support/gan-first-time-right/schematic-and-layout)  
   Étaye les conclusions sur la boucle principale, la gate loop, le retour sur première couche interne et la Kelvin connection.

2. [EPC AN031: PCB Design Guidelines to Maximize Cooling of eGaN FETs](https://epc-co.com/epc/Portals/0/epc/documents/product-training/AN031_PCB_Design_Guidelines_to_Maximize_Cooling_of_eGaN_FETs.pdf)  
   Étaye les données sur VIPPO, cuivre épais et amélioration thermique.

3. [EPC2092 Datasheet](https://epc-co.com/epc/documents/datasheets/EPC2092_datasheet.pdf)  
   Étaye les recommandations de layout vertical interne, boucles orthogonales et Kelvin source.

4. [TI LMG3410R050 Datasheet](https://www.ti.com/lit/ds/symlink/lmg3410r050.pdf)  
   Étaye le contexte sur le bottom thermal pad et la structure thermique recommandée.

5. [TI E2E: LMG3410R050 Layout Modeling Problem of LMG3410](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/919688/lmg3410r050-layout-modeling-problem-of-lmg3410)  
   Étaye le lien entre thermal pad, thermal vias et footprint recommandé.

6. [How to Design an eGaN FET-Based Power Stage with an Optimal Layout](https://epc-co.com/epc/home/post/15048/how-to-design-an-egan-fet-based-power-stage-with-an-optimal-layout)  
   Étaye le contexte public sur la réduction d’overshoot avec un layout optimisé.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB power electronics et assemblage haute densité
- Relecture technique : équipes process PCB, thermique et composants de puissance
- Dernière mise à jour : 2025-11-18

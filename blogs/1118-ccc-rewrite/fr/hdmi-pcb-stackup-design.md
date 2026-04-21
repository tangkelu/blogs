---
title: "Comment définir un stackup PCB HDMI : 100 ohms différentiel, loss budget et transitions de connecteur"
description: "Une réponse directe sur la version cible, l’impédance différentielle 100 ohms, les plans de référence, les pertes matériau et les transitions de connecteur à examiner en premier pour un stackup PCB HDMI."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# Comment définir un stackup PCB HDMI : 100 ohms différentiel, loss budget et transitions de connecteur

- **Le sujet central d’un stackup HDMI n’est pas le nombre de couches, mais la marge de fabrication restante au débit visé.**
- **La cible de base reste 100 ohms différentiel, mais la vraie difficulté est de la tenir en production.**
- **La continuité du plan de référence et les zones de launch consomment souvent la marge avant les segments droits.**
- **Toutes les cartes HDMI n’exigent pas un matériau low-loss premium, mais tous les projets ne sont pas non plus sûrs sur FR-4 standard.**
- **La validation doit s’appuyer sur des données de fabrication réelles.**

> **Quick Answer**  
> Le but d’un stackup PCB HDMI est de faire tenir ensemble paires différentielles 100 ohms, plans de référence continus, géométrie à faibles pertes et transitions de connecteur à la version et au débit visés. Un stackup n’est réellement bon que s’il garde encore de la marge après lamination, gravure et assemblage.

## Table des matières

- [Que faut-il examiner d’abord dans un stackup PCB HDMI ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi faut-il commencer le stackup HDMI par un loss budget basé sur le débit et la longueur ?](#loss-budget)
- [Pourquoi l’impédance différentielle 100 ohms doit-elle être liée à la fabrication réelle ?](#impedance)
- [Pourquoi connecteurs, changements de couche et stubs sont-ils plus dangereux que les segments droits ?](#transitions)
- [Comment valider un stackup HDMI avant production ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner d’abord dans un stackup PCB HDMI ?

Commencer par **la version HDMI visée, le lane rate, la longueur de piste sur la carte, les plans de référence et les transitions de connecteur**.

Il ne suffit pas d’appliquer des règles génériques high-speed à une paire différentielle. HDMI 2.1b monte à **48Gbps** de capacité totale, et TI indique pour FRL des lane rates de **3/6/8/10/12Gbps**. Les premières questions sont donc :

1. **Le lien est-il réellement en HDMI 2.0 TMDS ou déjà en HDMI 2.1 FRL ?**
2. **La longueur et la position des connecteurs imposent-elles des changements de couche ou des stubs longs ?**
3. **Le FR-4 ordinaire laisse-t-il encore assez de marge ?**
4. **Le plan de référence reste-t-il continu sur tout le chemin ?**
5. **L’usine sait-elle tenir de façon répétable la géométrie 100 ohms différentielle ?**

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / paramètre | Comment juger | Pourquoi c’est important | Comment vérifier | Si on l’ignore |
|---|---|---|---|---|
| Version HDMI et débit | Distinguer TMDS jusqu’à 6Gbps et FRL jusqu’à 12Gbps/lane | Le débit définit loss budget et fenêtre matériau | Spécification, datasheet, réglage protocole | Mauvais stackup, marge eye et EMI réduite |
| Impédance différentielle | Viser environ 100 ohms différentiel pour les paires HDMI | Exigence de base de la structure de transmission | Calcul d’impédance, coupon, TDR | Plus de réflexion et eye plus étroit |
| Plan de référence | Garder la paire près d’un plan de référence continu | La continuité du retour influence SI et EMI | Revue layout, contrôle des changements de couche | Plus de mode conversion et de rayonnement |
| Matériau et cuivre | Choisir selon longueur, débit et rugosité cuivre | Pertes et dispersion process montent avec le débit | Revue stackup, microsection, test d’insertion loss | Prototype OK, marge série plus faible |
| Transition connecteur / via | Launch, anti-pad, stub et changements de couche à revoir séparément | Les transitions échouent souvent avant les segments droits | Modélisation 3D, TDR, waveform mesurée | Écran noir, artefacts, instabilité |
| Cohérence de fabrication | La valeur de design doit se traduire en vraie géométrie usine | Lamination et gravure déplacent les dimensions | Microsection, coupon, comparaison lots | Dérive de marge entre lots |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 et HDMI 2.1 ne devraient pas partager une logique de stackup floue. On fixe d’abord le lane rate, puis matériau, couches et budget de longueur.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100 Ohm Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100 ohms n’est pas qu’une valeur de saisie logicielle. Il faut que cette valeur survive à la lamination, à la gravure et à l’état réel du cuivre.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">Sur les cartes HDMI, la marge se perd souvent d’abord dans les launches de connecteur, les changements de couche et les stubs, plutôt que dans les longues pistes droites.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">Un stackup HDMI mature se prouve par coupons, microsections et données TDR / insertion loss montrant que la géométrie fabriquée reste proche du modèle.</div>
    </div>
  </div>
</div>

<a id="loss-budget"></a>
## Pourquoi faut-il commencer le stackup HDMI par un loss budget basé sur le débit et la longueur ?

Conclusion : **parce que la bonne famille matériau et le bon stackup dépendent du lane rate réel, de la longueur et du nombre de transitions, pas de l’habitude prise sur ce type d’interface.**

HDMI 2.1b monte à **48Gbps** de capacité totale. TI donne jusqu’à **12Gbps** par lane en FRL et jusqu’à **6Gbps** en TMDS pour HDMI 2.0b. Les vraies questions deviennent :

- **Quelle est la longueur du trajet sur la carte ?**
- **Combien de connecteurs, ESD, redrivers et changements de couche existent ?**
- **Le FR-4 ordinaire laisse-t-il encore assez de marge ?**
- **Le design est-il déjà dans une zone qui exige moins de pertes et un meilleur contrôle diélectrique ?**

<a id="impedance"></a>
## Pourquoi l’impédance différentielle 100 ohms doit-elle être liée à la fabrication réelle ?

Conclusion : **parce que les 100 ohms HDMI ne sont pas une cible abstraite, mais le résultat physique de la lamination, de la compensation de gravure et de la géométrie réelle du cuivre.**

TI exprime explicitement l’exigence 100 ohms dans plusieurs documents HDMI. En série, cette valeur se déplace avec :

- l’épaisseur diélectrique réelle après lamination
- la largeur gravée par rapport à la largeur dessinée
- la rugosité cuivre
- le masque, la forme du plan de référence et le cuivre voisin

<a id="transitions"></a>
## Pourquoi connecteurs, changements de couche et stubs sont-ils plus dangereux que les segments droits ?

Conclusion : **parce que les segments droits HDMI sont souvent maîtrisables alors que launches, vias et changements de couche introduisent beaucoup plus facilement sauts d’impédance, mode conversion et pertes supplémentaires.**

Les points à examiner séparément sont surtout :

- la continuité du plan de référence sous le launch du connecteur
- la géométrie pad / anti-pad des vias
- la fermeture du retour par vias de masse aux changements de couche
- le besoin éventuel de raccourcir ou backdriller les stubs
- la symétrie conservée après breakout

<a id="validation"></a>
## Comment valider un stackup HDMI avant production ?

Conclusion : **une validation HDMI utile ne prouve pas seulement qu’une paire 100 ohms existe sur le dessin, mais que la carte fabriquée respecte encore la cible.**

Un chemin pratique inclut généralement :

| Point de validation | Ce qu’il vérifie | Points d’observation |
|---|---|---|
| Coupon d’impédance | L’usine tient-elle la géométrie cible de manière répétable ? | Cible 100 ohms et dispersion lot à lot |
| Microsection | Lamination et gravure ont-elles déplacé la structure ? | Épaisseur diélectrique, largeur de piste, profil cuivre |
| TDR ou insertion loss | Transitions et chemin complet sont-ils sains ? | Discontinuités locales, segment droit vs transition |
| Comparaison multi-cartes | La fenêtre process est-elle assez large ? | Cohérence eye / impédance / pertes |
| Test système | Le stackup tient-il avec vrais connecteurs et composants ? | Résolution, artefacts, seuil écran noir, EMI |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

- Faire converger matériau, cuivre et direction stackup via [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- Utiliser tôt l’[Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) pour estimer la géométrie 100 ohms.
- Si breakout connecteur, changements de couche et fan-out plus dense existent, vérifier aussi [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) ou [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Une fois stackup, coupons et launch review stabilisés, les intégrer directement dans [Quote / RFQ](https://hilpcb.com/en/quote/) ou [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### Chaque carte HDMI 2.1 exige-t-elle un matériau low-loss premium ?

Pas forcément. Tout dépend du lane rate réel, de la longueur et du nombre de transitions.

### Suffit-il de dessiner la paire à 100 ohms ?

Non. Le résultat réel dépend aussi de la lamination, de la compensation de gravure, de la rugosité et du plan de référence.

### Les paires différentielles HDMI ont-elles encore besoin d’un plan de référence continu ?

Oui. Le routage différentiel ne supprime pas le besoin d’un retour stable.

### Les problèmes HDMI apparaissent-ils plutôt dans la piste ou dans la transition connecteur ?

Très souvent dans le launch de connecteur, le via de changement de couche ou le stub.

### Pourquoi les coupons ou le TDR sont-ils importants ?

Parce qu’ils montrent si la géométrie fabriquée reste fidèle au modèle.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   Étaye le contexte officiel de 48Gbps et des résolutions / fréquences plus élevées.

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   Étaye les données FRL à 3/6/8/10/12Gbps.

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   Étaye le contexte HDMI 2.0b / 6Gbps TMDS.

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   Étaye les règles 100 ohms HDMI et le contrôle des transitions.

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   Étaye l’évaluation conjointe du stack, des plans de référence, des vias et du routing.

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   Étaye la formulation officielle des 100 ohms ±10%.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB interfaces high-speed et stackup
- Relecture technique : équipes process PCB, SI et connecteurs high-speed
- Dernière mise à jour : 2025-11-18

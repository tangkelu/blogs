---
title: "Que regarder d’abord dans le routage SFP et QSFP-DD : breakout 112G, backdrill et maîtrise de la transition sur la host board"
description: "Une réponse directe sur le format d’interface, le breakout, les plans de référence, le backdrill, les matériaux et les contraintes d’assemblage/thermique à examiner en priorité pour le routage SFP et QSFP-DD à 112G, afin de préserver la marge de canal autour du connecteur sur les host boards et backplanes haut débit."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["QSFP-DD routing", "SFP routing", "High-speed connector PCB", "Signal integrity", "Low-loss PCB", "112G PAM4"]
---

# Que regarder d’abord dans le routage SFP et QSFP-DD : breakout 112G, backdrill et maîtrise de la transition sur la host board

- **À 112G PAM4, le "dernier pouce" près du connecteur décide souvent du lien avant même la grande ligne principale.**
- **Les points d’attention ne sont pas exactement les mêmes entre QSFP-DD et SFP112, mais dans les deux cas tout se joue sur le launch, le breakout et la stabilité du retour de courant.**
- **QSFP-DD est difficile non seulement à cause du débit, mais parce que son interface 8 lanes cumule densité, thermique et pression SI sur la même host board.**
- **Un matériau plus performant peut réduire la perte totale, mais ne sauvera pas un breakout mal conçu.**
- **Le routage du connecteur doit être examiné en même temps que le cage, le heatsink et la méthode d’assemblage.**

> **Quick Answer**  
> Le vrai sujet du routage SFP et QSFP-DD n’est pas seulement d’amener les paires différentielles jusqu’au bord de carte. À 112G, la géométrie du breakout, la transition de pad, la stratégie via/backdrill, les plans de référence et l’assemblage du connecteur doivent tous fonctionner ensemble sur la host board. La vraie marge ne vient pas du plus beau routage tronc, mais d’un "dernier pouce" encore fabricable, assemblable et répétable.

## Table des matières

- [Que faut-il examiner en premier dans le routage SFP et QSFP-DD ?](#overview)
- [Tableau récapitulatif des règles et paramètres clés](#rules)
- [Pourquoi la zone de breakout fixe-t-elle souvent la limite basse d’un canal 112G ?](#breakout)
- [Pourquoi vias, backdrill et plans de référence doivent-ils converger ensemble dans la zone de launch ?](#launch-via)
- [Pourquoi matériaux, cages et thermique ne peuvent-ils pas être revus séparément du routage ?](#thermal-materials)
- [Comment valider le routage du connecteur sur une host board avant la série ?](#validation)
- [Prochaines étapes avec HILPCB](#next-steps)
- [Questions fréquentes (FAQ)](#faq)
- [Références publiques](#references)
- [Auteur et relecture technique](#author)

<a id="overview"></a>
## Que faut-il examiner en premier dans le routage SFP et QSFP-DD ?

Commencer par **le format d’interface, le nombre de lanes et le débit, la structure du breakout, la stratégie via/backdrill et l’enveloppe thermique/mécanique**.

La question ne se résume pas à "router la paire différentielle jusqu’au connecteur". Et QSFP-DD n’est pas simplement "plus de paires qu’un SFP". Les documents publics de TE montrent SFP jusqu’à **112G** et QSFP-DD dans la plage **56-112G** avec une **architecture PAM4 à 8 lanes**. Les premières questions sur la host board sont donc :

1. **Est-on face à un launch SFP112 à une ou quelques lanes, ou à un launch QSFP-DD à 8 lanes ?**
2. **La zone de breakout dispose-t-elle d’assez de couches, d’espace de fanout et de continuité de plan ?**
3. **Faut-il du backdrill, des vias blind/buried ou une structure plus agressive ?**
4. **Le cage, le heatsink ou les ports empilés changent-ils l’espace disponible et le retour de courant côté carte ?**
5. **Assemblage et gestion thermique sont-ils déjà revus dans la même boucle de validation ?**

Pour une carte de switch, NIC, serveur ou backplane, il est généralement préférable de figer tôt stackup et perçage avec [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb), [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) et [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).

<a id="rules"></a>
## Tableau récapitulatif des règles et paramètres clés

| Règle / paramètre | Bonne manière de l’évaluer | Pourquoi c’est important | Comment vérifier | Ce qui se passe si on l’ignore |
|---|---|---|---|---|
| Format d’interface | Distinguer d’abord le contexte SFP112 et le contexte QSFP-DD 8 lanes | Densité et limites thermiques changent fortement | Datasheet connecteur, revue architecture | Stackup et stratégie breakout mal alignés |
| Chemin de breakout | Sortir vite du pad field avec peu de neck-down et peu de distorsion | Le dernier pouce consomme la marge le plus vite | Simulation 3D/2.5D, revue layout | Un bon trunk routing ne compense pas la perte du launch |
| Via / backdrill | Minimiser les stubs de through-via sur les lanes rapides; backdrill si nécessaire | La résonance des stubs devient critique à 112G | TDR, coupe micrographique, revue perçage | Return loss dégradé, training instable, BER en hausse |
| Plans de référence | Garder sous launch et breakout des retours de courant continus et prévisibles | L’interaction connector-PCB n’est plus négligeable | Revue des planes, solveur 3D | Mode conversion et bruit common-mode augmentent |
| Matériau / cuivre | Juger selon la longueur totale du canal et le budget d’insertion loss | Le low-loss material ne résout qu’une partie du problème | Revue stackup, simulation IL, coupon | Upgrade matière, mais lien toujours instable |
| Cage / heatsink / assemblage | Revoir ensemble cage, heatsink, coplanéité et contrainte d’assemblage | La zone connecteur est aussi une zone critique d’assemblage | Revue assemblage, revue thermique, X-ray / visuel | Le proto marche, la présérie varie |

| Exemple d’interface | Point public clé | Indication de design |
|---|---|---|
| SFP | Guide TE : 1-112G lane rate | Moins de lanes, mais launch toujours sensible |
| QSFP-DD | Page TE : eight-lane electrical interface, 28G/56G/112G, jusqu’à 800 Gbps | Densité, thermique et risque breakout s’additionnent |
| Connexion host 112G | Cadence : connector et final inch ne doivent plus être séparés | Il faut modéliser board et connector ensemble |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef6f1 100%); border: 1px solid #d5e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365c7c; font-weight: 700;">Final Inch First</div>
      <div style="margin-top: 8px; color: #233546;">Sur une host board 112G, le risque principal se trouve souvent dans les premiers millimètres de breakout et de transition pad, pas dans la longue route principale.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7b72; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a6159; font-weight: 700;">Backdrill Is a Routing Decision</div>
      <div style="margin-top: 8px; color: #223630;">Dans un breakout 112G, le backdrill n’est pas une correction tardive, mais une règle de routage qui commence dès le choix des vias et des transitions de couches.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #886847; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Material Cannot Fix Launch Errors</div>
      <div style="margin-top: 8px; color: #3a2f25;">Un matériau low-loss réduit la perte totale du canal, mais ne récupère pas les réflexions ou la mode conversion créées par des stubs, anti-pads ou retours de courant cassés.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5f7d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c4960; font-weight: 700;">Cage and Thermal Change the Board</div>
      <div style="margin-top: 8px; color: #392733;">Les cages QSFP-DD, heatsinks et configurations empilées modifient espace, airflow et assemblage sur la host board. Impossible de les séparer de la SI.</div>
    </div>
  </div>
</div>

<a id="breakout"></a>
## Pourquoi la zone de breakout fixe-t-elle souvent la limite basse d’un canal 112G ?

Conclusion : **Parce qu’à 112G, la partie la plus fragile du canal est souvent l’ensemble formé par pads de connecteur, vias, anti-pads et premiers millimètres de routage host.**

Cadence l’écrit clairement : aux débits plus faibles, on pouvait souvent analyser séparément le connecteur et la carte de référence puis combiner les résultats. À **112G PAM4**, ce n’est plus vrai, car l’interaction entre breakout et connecteur devient trop forte pour être négligée. Sur une host board SFP ou QSFP-DD, cela veut dire :

- **les pertes et réflexions du launch ne sont plus des effets secondaires**
- **le crosstalk local et la mode conversion apparaissent avant les pertes de la grande route**
- **si la géométrie du breakout est instable, l’equalization ne réparera pas totalement**

<a id="launch-via"></a>
## Pourquoi vias, backdrill et plans de référence doivent-ils converger ensemble dans la zone de launch ?

Conclusion : **Parce que dans un breakout 112G, la structure des vias et le retour de courant font eux-mêmes partie de la performance du connecteur.**

L’erreur classique consiste à traiter les vias comme un détail secondaire et à repousser le sujet du backdrill. En réalité, through-via, stub résiduel, forme d’anti-pad, pas des GND vias et keep-out des planes déterminent ensemble :

- si le return loss reste acceptable
- si l’insertion loss démarre déjà trop haut
- si la cohérence lane-to-lane est suffisante
- si bruit common-mode et crosstalk sont amplifiés

À 112G, cela signifie en pratique : **structure de via, backdrill et ouvertures de plane doivent être modélisés et revus dans le même cycle.**

<a id="thermal-materials"></a>
## Pourquoi matériaux, cages et thermique ne peuvent-ils pas être revus séparément du routage ?

Conclusion : **Parce qu’un canal 112G sur host board n’est pas juste une piste, mais un système composé de matériau, connecteur, cage, thermique et assemblage.**

TE positionne QSFP-DD comme une **architecture PAM4 8 lanes** destinée au HPC, à l’AI/ML et au networking dense. La page QSFP-DD indique aussi que des solutions 2x1 empilées peuvent donner plus de hauteur pour un airflow plus uniforme et un dissipateur ASIC plus grand. Amphenol regroupe dans un même système produit les connecteurs SMT 1x1 / 2x1, cages empilées 2x1 et multiples heatsinks.

On ne peut donc pas séparer :

- **la capacité du matériau à tenir le budget de perte**
- **l’effet cage / heatsink sur la frontière mécanique et thermique**
- **la stabilité de la coplanéité, de la contrainte d’assemblage et de l’appui du connecteur**
- **la cohérence de l’airflow et de la structure de masse avec plusieurs ports voisins**

<a id="validation"></a>
## Comment valider le routage du connecteur sur une host board avant la série ?

Conclusion : **Une validation utile prouve que la zone de launch et le canal principal restent valides après fabrication et assemblage réels.**

| Élément de validation | Question principale | Points d’observation recommandés |
|---|---|---|
| Co-simulation 3D / 2.5D | Connecteur et breakout fonctionnent-ils comme un seul ensemble ? | Launch, anti-pad, GND vias, interaction cage |
| Coupon / TDR | Les stubs et discontinuités locales sont-ils maîtrisés ? | Plateau d’impédance, stub résiduel, points de réflexion |
| Coupe et contrôle perçage | Le backdrill après métallisation reste-t-il conforme à la cible ? | Longueur de stub, géométrie des trous, cuivre, cohérence |
| Test de lien système | Le module réel et la host board gardent-ils assez de marge ? | Training, BER, cohérence entre lanes |
| Contrôle multi-cartes / assemblage | Soudure du connecteur et montage de cage sont-ils répétables ? | Coplanéité, voiding, contrainte thermique, dispersion inter-cartes |

<a id="next-steps"></a>
## Prochaines étapes avec HILPCB

Si vous développez actuellement une host board SFP112 ou QSFP-DD 112G, l’étape suivante la plus utile consiste à transformer le "routage haut débit" en exigences fabricables autour de la zone connecteur :

- Utiliser d’abord [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) et [Backplane PCB](https://hilpcb.com/en/products/backplane-pcb) pour figer stackup, matériaux et direction du canal 112G.
- Pour des breakouts plus denses et des transitions de couches plus serrées, vérifier en parallèle la fenêtre vias / backdrill de [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) ou [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).
- Pendant la phase prototype, intégrer directement connecteur, cage, thermique et contrôles d’assemblage dans la revue [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Une fois launch, backdrill, matériau et méthode d’assemblage alignés, reporter ces conditions directement dans [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) ou [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Questions fréquentes (FAQ)

<!-- faq:start -->

### La perte matière est-elle le principal problème du routage QSFP-DD 112G ?

Non. Elle compte, mais les premiers problèmes apparaissent généralement dans la géométrie du breakout, la qualité du launch, les stubs de vias, l’anti-pad et la continuité du retour de courant.

### SFP112 est-il beaucoup plus simple que QSFP-DD parce qu’il a moins de lanes ?

La pression de densité est plus faible, mais les règles de base sont les mêmes. SFP112 doit lui aussi maîtriser transition 112G, stubs, matériau et cohérence d’assemblage.

### Peut-on décider du backdrill seulement après un mauvais premier proto ?

En général non. Dans une zone connecteur 112G, le backdrill fait plutôt partie des conditions d’entrée du design.

### Pourquoi cage et heatsink influencent-ils la revue de routage ?

Parce que cage, heatsink, ports empilés, espace, airflow et stratégie de masse sur la host board sont couplés.

### Pourquoi une simulation 2D seule ne suffit-elle pas pour une zone connecteur 112G ?

Parce que Cadence indique explicitement que l’interaction électromagnétique entre breakout et connecteur ne peut plus être négligée à 112G.

<!-- faq:end -->

<a id="references"></a>
## Références publiques

1. [TE High-Speed Input/Output Interconnect Selection Guide](https://www.te.com/content/dam/te-com/documents/datacomm/global/ddn-hsio-guide-en-2026.pdf)  
   Appuie le contexte public selon lequel SFP monte jusqu’à 1-112G et QSFP-DD couvre 56-112G en architecture PAM4 8 lanes.

2. [TE QSFP-DD Interconnects](https://www.te.com/en/products/connectors/high-speed-pluggable-io-connectors-and-cages/qsfp-dd.html)  
   Appuie l’explication sur l’interface électrique 8 lanes, les modes 28G NRZ / 56G PAM4 / 112G PAM4, jusqu’à 800 Gbps, ainsi que le couplage cage/heatsink avec la host board.

3. [Cadence White Paper: Overcoming Signal Integrity Challenges of 112G Connections](https://www.cadence.com/ko_KR/home/resources/white-papers/overcoming-signal-integrity-challenges-of-112g-connections-wp.html)  
   Appuie la conclusion d’ingénierie selon laquelle à 112G, connector et breakout final inch doivent être modélisés ensemble.

4. [Amphenol ExtremePort™ QSFP DD 112G Connectors Datasheet](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/datasheet/inputoutput/hsio_cn_extremeport_qsfp_dd_112g.pdf)  
   Appuie l’explication publique des connecteurs 112G QSFP-DD, cages empilées et options de heatsink comme un seul système d’interconnexion host.

5. [QSFP-DD MSA Specification Page](https://www.qsfp-dd.com/specification/)  
   Appuie le contexte normatif public autour des 8 interfaces électriques haut débit du QSFP-DD.

<a id="author"></a>
## Auteur et relecture technique

- Auteur : équipe contenu HILPCB High-Speed Interconnect et Connectors
- Relecture technique : équipe process PCB, SI et assemblage haut débit
- Dernière mise à jour : 2025-11-18

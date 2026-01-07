---
title: "Via-in-Pad plated over (VIPPO) : relever les défis packaging et high-speed interconnect pour AI chip interconnect et substrate PCBs"
description: "Deep dive sur Via-in-Pad plated over (VIPPO) : Signal Integrity, Power Integrity, chemins thermiques, contrôles process et stratégies de design coût‑efficaces pour AI interconnect et IC substrate PCBs haute performance."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad plated over (VIPPO)", "Copper pillar", "Hybrid stack-up (Rogers+FR-4)", "Backdrill quality control", "Heavy copper 3oz+", "Controlled impedance"]
---
Avec la croissance explosive de l’AI, du HPC et des workloads data center, les exigences sur le hardware atteignent un niveau inédit. La puissance et le débit des AI accelerators, GPU et ASIC augmentent, ce qui rend la conception et la fabrication d’IC substrates et de PCB beaucoup plus exigeantes. Dans ce contexte, **Via-in-Pad plated over (VIPPO)** est passée d’option à procédé indispensable : elle impacte directement SI, stabilité PDN et efficacité thermique. Vu sous l’angle d’un thermal interface design engineer, cet article décortique **Via-in-Pad plated over (VIPPO)** et explique comment elle répond aux défis packaging et high‑speed interconnect des AI chip interconnect et substrates.

En HDI, notamment avec des BGA à 0.4 mm (ou moins) de pitch, le fanout Dog‑bone classique ne suffit plus en densité. **Via-in-Pad plated over (VIPPO)** place le via sous le pad, le remplit (conductif ou non) puis replaque la surface pour obtenir un pad plan, directement soudable. Cela libère de la place de routage et améliore les performances électriques et thermiques. Comprendre comment HILPCB peut optimiser vos designs AI interconnect/substrate est un avantage réel.

### Qu’est-ce que Via-in-Pad plated over (VIPPO) ?

**Via-in-Pad plated over (VIPPO)** est un procédé avancé de fabrication PCB destiné à résoudre la congestion de routage liée à la forte densité de composants. Le flux standard comprend :

1.  **Drilling :** percer un via au centre du pad (BGA, LGA, autres SMD).
2.  **Via-wall plating :** plaquer du cuivre sur la paroi pour assurer la connexion interlayer.
3.  **Filling :** remplir complètement le via avec une epoxy conductrice ou non. Étape critique : les voids peuvent se dilater en reflow et provoquer des failures de soudure.
4.  **Planarization :** grinding ou CMP pour rendre la surface parfaitement affleurante au cuivre.
5.  **Plated-over cap :** replaque cuivre sur via et pad pour une surface continue et fiable.
6.  **Surface finish :** ENIG, ImAg, OSP, etc.

Comparé au Dog‑bone, **Via-in-Pad plated over (VIPPO)** supprime la fanout trace, raccourcit le chemin du signal et permet de placer des decoupling capacitors plus près des pins d’alimentation. Pour les substrates AI modernes, cette optimisation densité + performance est fondamentale.

### Comment VIPPO améliore la Signal Integrity des AI substrates ?

Les systèmes AI fonctionnent à des dizaines/centaines de Gbps (PCIe 6.0, HBM3e). À ces fréquences, de petites imperfections géométriques créent de gros problèmes SI. **Via-in-Pad plated over (VIPPO)** agit comme « gardien » SI.

D’abord, en supprimant la fan‑out trace du Dog‑bone, VIPPO réduit fortement la longueur du chemin entre ball BGA et routage interne, diminuant l’inductance/capacité parasites et les discontinuités d’impédance. Pour des paires différentielles en **Controlled impedance**, la transition est plus lisse et prévisible, réduisant réflexions et jitter.

Ensuite, VIPPO réduit l’impact des via stubs. Dans un multilayer classique, un through‑via traverse toutes les couches ; les portions inutilisées deviennent des stubs qui résonnent. **Backdrill quality control** supprime les stubs mais ajoute coût et étapes. VIPPO combinée à des blind/buried vias peut éviter les stubs dès la conception, offrant des canaux plus propres pour SerDes et memory buses.

<div style="background-color:#F5F7FA;padding:20px;border-radius:8px;margin:20px 0;">
<h3 style="color:#000000;text-align:center;border-bottom:3px solid #64B5F6;padding-bottom:10px;">Comparatif de performance des technologies de via</h3>
<table style="width:100%;border-collapse:collapse;text-align:center;color:#000000;">
<thead style="background-color:#F5F5F5;color:#000000;">
<tr>
<th style="padding:12px;border:1px solid #ddd;">Attribut</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #4CAF50;">Via-in-Pad plated over (VIPPO)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #FFC107;">Dog-bone via (Dog-Bone Via)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #F44336;">Open via-in-pad (Via-in-Pad Open)</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Densité de routage</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Très élevée</b></td>
<td style="padding:12px;border:1px solid #ddd;">Faible</td>
<td style="padding:12px;border:1px solid #ddd;">Élevée</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Longueur chemin signal</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>La plus courte</b></td>
<td style="padding:12px;border:1px solid #ddd;">Longue</td>
<td style="padding:12px;border:1px solid #ddd;">Courte</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Inductance parasite</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>La plus faible</b></td>
<td style="padding:12px;border:1px solid #ddd;">Élevée</td>
<td style="padding:12px;border:1px solid #ddd;">Faible</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Performance thermique</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Excellente</b></td>
<td style="padding:12px;border:1px solid #ddd;">Faible</td>
<td style="padding:12px;border:1px solid #ddd;">Moyenne</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Complexité fabrication</td>
<td style="padding:12px;border:1px solid #ddd;">Élevée</td>
<td style="padding:12px;border:1px solid #ddd;">Faible</td>
<td style="padding:12px;border:1px solid #ddd;">Moyenne</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Fiabilité soudure</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Élevée (void‑free)</b></td>
<td style="padding:12px;border:1px solid #ddd;">Élevée</td>
<td style="padding:12px;border:1px solid #ddd;">Faible (risque solder wicking)</td>
</tr>
</tbody>
</table>
</div>

### Quel est le rôle de VIPPO en thermal management ?

Les AI chips peuvent dépasser plusieurs centaines de watts de TDP, voire 1000 W+. Sans extraction thermique efficace, le chip throttle ou se dégrade. **Via-in-Pad plated over (VIPPO)** joue le rôle de micro‑canal thermique.

Avec un filling thermiquement conducteur (ou même une epoxy non conductrice où le plated copper domine), VIPPO fournit un chemin de faible résistance thermique du pad vers de grands plans internes GND/power. Ces plans diffusent la chaleur (heat spreading). Pour les hot spots, on place souvent un array VIPPO sous le composant pour former une matrice de « thermal pillars ».

Cette voie board‑level se combine à des solutions package‑level (vapor chamber) et system‑level (fans, liquid cooling). Des plans **Heavy copper 3oz+** améliorent encore la diffusion grâce à leur faible résistance thermique latérale. En tant que fabricant [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb), Highleap PCB Factory (HILPCB) maîtrise l’etch et la lamination thick‑copper pour une intégration VIPPO fiable.

### Comment VIPPO améliore la Power Integrity (PI) ?

Les AI chips imposent un PDN très basse impédance pour absorber de grands transitoires (di/dt). **Via-in-Pad plated over (VIPPO)** aide PI de plusieurs façons.

D’abord, VIPPO fournit des connexions power/ground plus courtes et directes, réduisant l’inductance entre plans et pins. Avec V = L * (di/dt), moins d’inductance signifie moins de bruit rail.

Ensuite, VIPPO permet de placer les decoupling capacitors au dos du BGA, presque « back‑to‑back » avec les pins power/ground, réduisant l’inductance de boucle et améliorant le découplage HF.

Enfin, VIPPO est synergique avec **Copper pillar** en advanced packaging : **Copper pillar** offre une meilleure conduction électrique/thermique que les bumps et est courante en Flip‑Chip. VIPPO fournit des pads haute densité et basse impédance côté substrate, maintenant un chemin courant faible impédance jusqu’au die.

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: -0.5px;">🚀 HILPCB : indicateurs clés de fabrication pour substrates AI next‑gen</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Puissance des large models : densité extrême et architecture power haut courant</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Capacité lamination ultra‑élevée</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">56 <span style="font-size: 16px; font-weight: 600; color: #64748b;">Layers</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Maîtrise **Any-layer HDI** et mixed lamination pour des core substrates stables sur 800G switch et compute cards.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">VIPPO &amp; microvia process</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">0.15 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mm</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Support **Via-in-Pad** filling + plated‑over. Optimise le fanout BGA et l’escape routing pour des AI chips à très fort pin count.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Contrôle d’impédance extrême &amp; SI</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">±5 <span style="font-size: 20px; font-weight: 600; color: #64748b;">%</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Alignement strict **PCIe 6.0/7.0** via etch compensation haute précision.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Gestion haut courant &amp; haute puissance</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">12 <span style="font-size: 20px; font-weight: 600; color: #64748b;">oz</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Solutions thick‑copper power layers pour AI core jusqu’à 1000W+ afin de réduire le drop PDN et l’échauffement.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Intégration matériaux avancés</strong>
<p style="font-size: 1.1em; font-weight: 800; margin: 15px 0; color: #1e3a8a; line-height: 1.4;">ABF / Megtron 8 / Rogers</p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Support complet **Ajinomoto Build-up Film (ABF)** et matériaux RF Ultra‑Low Loss.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Fine‑line &amp; technologie substrate</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">2/2 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mil</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Avec **mSAP**, routage ultra‑fin pour l’interconnect haute densité en architectures Chiplet.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #3b82f6; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Note HILPCB :</strong> pour des substrates AI de 56 layers et plus, le matching <strong>Z-axis CTE</strong> est critique. Intégrer une simulation **Warpage** dès la phase stackup pour assurer la coplanarité au reflow BGA.
</div>
</div>

### Impact de VIPPO sur les stackups complexes

**Via-in-Pad plated over (VIPPO)** est un pilier pour les designs HDI ultra denses et [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb). Elle permet le fanout BGA fine‑pitch sans augmenter le nombre de couches.

Sur les systèmes mixed‑signal RF + high‑speed digital, **Hybrid stack-up (Rogers+FR-4)** est courant : [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) pour la RF et FR‑4/ABF‑like pour le digital. VIPPO s’intègre bien en assurant densité et transitions inter‑matériaux maîtrisées pour SI/PI.

VIPPO se combine aussi aux microvias (stacked/staggered) pour créer un réseau 3D : amener les signaux de la surface puis les distribuer sur les couches via microvias, minimisant les connexions Z‑axis.

### Points de qualité critiques en fabrication VIPPO

VIPPO est plus complexe ; le contrôle process est clé :

1.  **Qualité du filling :** vacuum‑assisted filling pour éviter les voids ; sinon risque de pad lifting et Head‑in‑Pillow en reflow.
2.  **Planarity :** contrôler grinding/polishing (souvent ±0.5 mil). Une mauvaise planéité dégrade l’impression de pâte et la soudure.
3.  **Adhérence copper cap :** peel strength suffisante pour éviter delamination sous choc thermique.
4.  **Précision dimensionnelle :** diamètre, position, taille pad.

Comparé à **Backdrill quality control** (profondeur + stub removal), VIPPO exige un QC multi‑étapes et un Cpk plus élevé. HILPCB utilise AOI, X‑ray et micro‑section pour viser IPC‑6012 Class 3 (ou plus).

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.75em; font-weight: 800; letter-spacing: -0.5px;">🎯 Process VIPPO : points de sign‑off design &amp; fabrication haute densité</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Guide fabrication pour optimiser densité fanout BGA et Signal Integrity</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">01. Void-free filling</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> filling dense. Les bulles résiduelles se dilatent en reflow et provoquent pad lifting ou cracks de soudure.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">02. Surface planarity</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> la planéité pilote le yield. Contrôler etch‑back et grinding pour éviter recess/protrusion et réduire opens/HoP.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">03. Aspect ratio et plating challenges</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> un aspect ratio élevé complique la pénétration chimique et le filling. Pour thick boards, valider tôt les paramètres vacuum afin d’éviter l’underfill.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">04. Cost effectiveness et usage sélectif</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> VIPPO coûte plus cher ; l’utiliser uniquement là où nécessaire : BGA core &lt; 0.8 mm pitch ou zones critiques pour thermiques/return path/SI.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #2563eb; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Tip HILPCB :</strong> pour les pads VIPPO, nous recommandons une ligne de cap plating dédiée <strong>POFV</strong> afin d’augmenter la peel strength et réduire la delamination en thermal cycling sévère.
</div>
</div>

### VIPPO et advanced packaging (ex. Copper Pillar)

Les technologies 2.5D/3D (CoWoS, Foveros) sont clés : les chips se connectent via interposer/direct bonding en SiP. **Via-in-Pad plated over (VIPPO)** sert de pont entre package complexe et main PCB.

Avec **Copper pillar**, l’intérêt est encore plus net : moins de résistance, meilleure capacité de courant et meilleure thermique que les bumps, souvent utilisé en Flip‑Chip. Le pitch serré impose des pads très denses et précis ; VIPPO fournit des pads plans adaptés, ce qui améliore l’uniformité, en particulier pour HBM. Cela soutient des objectifs [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Équilibrer gains VIPPO et coûts de fabrication

VIPPO est un procédé value‑added plus coûteux que des vias standard, du fait du resin fill et des étapes additionnelles (filling, planarization, second plating). La stratégie est l’usage sélectif : appliquer VIPPO là où elle apporte le plus de valeur (fine‑pitch BGA breakout, interfaces high‑speed, zones thermiques critiques) et utiliser des alternatives ailleurs.

Avec un fabricant expérimenté comme HILPCB, un DFM précoce aide à décider où VIPPO maximise le ROI performance et où des microvias réduisent les coûts, y compris en **Hybrid stack-up (Rogers+FR-4)**. Notre capacité [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) couvre l’ensemble des solutions.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion : VIPPO, passage obligé vers l’AI hardware du futur

**Via-in-Pad plated over (VIPPO)** est devenue une technologie enabling pour l’AI/HPC next‑gen. Densité de routage, SI supérieure, chemins thermiques efficaces et PDN stable : VIPPO répond directement aux défis des AI chips. Sans VIPPO, beaucoup de designs de substrates modernes seraient difficiles à réaliser.

Pour en tirer pleinement parti, il faut une collaboration étroite design/fabricant, en maîtrisant règles de design, contraintes process et checkpoints QC. Avec HILPCB, vous bénéficiez d’un contrôle **Controlled impedance** précis, d’une expérience **Heavy copper 3oz+** et d’une compréhension des interfaces **Copper pillar** pour passer du design à une production fiable.

Contactez HILPCB pour un devis rapide et lancer votre projet AI substrate – construisons la prochaine vague technologique ensemble.


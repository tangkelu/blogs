---
title: "Rigid-flex PCB : liens ultra-high-speed et défis low-loss pour la high-speed signal integrity"
description: "Analyse de Rigid-flex PCB : high-speed SI, thermal management et conception power/interconnect pour construire des PCB hautes performances."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["Rigid-flex PCB", "Copper coin", "ENIG/ENEPIG/OSP", "Backdrill quality control", "Hybrid stack-up (Rogers+FR-4)", "Microvia/stacked via"]
---
En tant qu’ingénieur de mesure/validation (TDR/VNA, extraction S-parameters), je sais que dans les designs ultra-high-speed et haute densité, le choix de la technologie d’interconnect peut décider du succès. **Rigid-flex PCB** apporte routage 3D et fiabilité, et devient une solution clé pour les défis de high-speed SI, en assurant la cohérence du channel du chip au connector.

Cet article explique, côté validation SI, comment matériaux, stackup et procédés de fabrication adressent atténuation, crosstalk et discontinuités d’impédance à 28G/56G/112G+. Focus sur Hybrid stack-up, Microvia/stacked via, surface finish, backdrill et Copper coin.

### Pourquoi Rigid-flex PCB est clé en high-speed

Les interconnexions par câbles/connecteurs introduisent de fortes discontinuités et du loss à Gbps. Chaque transition consomme eye opening et jitter budget. Rigid-flex intègre rigid et flex, supprime ces interfaces, améliore IL/RL, la densité 3D, la reliability (moins de pannes mécaniques) et réduit le TCO global.

### Hybrid stack-up : optimiser SI et coût

**Hybrid stack-up (Rogers+FR-4)** combine Rogers/Megtron pour les layers high-speed et FR-4 (High-Tg) pour power/low-speed. Points clés : stackup symétrique (warpage), compatibilité de lamination et Dk/Df corrects dans les modèles d’impédance.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#000000; text-align:center;">Hybrid stackup : comparaison performance/cost</h3>
<table style="width:100%; border-collapse: collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Stackup</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Use case</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">SI</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Coût relatif</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Complexité</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All FR-4</td>
<td style="padding:12px; border:1px solid #ccc;">&lt; 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">Correct</td>
<td style="padding:12px; border:1px solid #ccc;">★</td>
<td style="padding:12px; border:1px solid #ccc;">Faible</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Hybrid stack-up (Rogers+FR-4)</td>
<td style="padding:12px; border:1px solid #ccc;">5 - 56 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">Excellent</td>
<td style="padding:12px; border:1px solid #ccc;">★★★</td>
<td style="padding:12px; border:1px solid #ccc;">Élevée</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All Rogers/Megtron</td>
<td style="padding:12px; border:1px solid #ccc;">&gt; 56 Gbps / RF</td>
<td style="padding:12px; border:1px solid #ccc;">Max</td>
<td style="padding:12px; border:1px solid #ccc;">★★★★★</td>
<td style="padding:12px; border:1px solid #ccc;">Moyenne</td>
</tr>
</tbody>
</table>
</div>

### Microvia/stacked via

Avec des pitch BGA de 0.5mm et moins, les vias mécaniques limitent la densité. **Microvia/stacked via** devient standard : microvia laser (<150µm) et stacked via pour interconnect vertical compact. Il faut un procédé plated-filled fiable et microsection. HILPCB sait sécuriser [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

### Défis SI en flex zone

1) contrôle d’impédance plus difficile (Polyimide/Coverlay), 2) bending impacte géométrie/delay (Neutral Axis, symétrie diff pair), 3) hatched ground dégrade return path (crosstalk/EMI trade-off).

<div style="background: #ffffff; border: 1px solid #d1c4e9; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(103,58,183,0.08);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 40px 0; font-size: 1.8em; font-weight: 800; border-bottom: 4px solid #9575cd; padding-bottom: 15px; display: inline-block; width: 100%;">🌀 Flex zone : matrice design high-speed SI & reliability</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">01. Circular Traces & impedance</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Imposer <strong>Circular Traces</strong> et éviter 90°/45° dans les zones de bending.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">02. Teardrop</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Ajouter <strong>Teardrop</strong> pour renforcer pad-trace junction.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">03. Stiffener</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>FR-4/PI stiffener</strong> près des connecteurs/SMT pour isoler le stress.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">04. No-via en zone dynamique</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Éviter les vias dans la zone de <strong>Bending Radius</strong>.</p>
</div>
</div>
<div style="margin-top: 30px; background: #311b92; color: #ffffff; padding: 25px; border-radius: 16px; border-left: 8px solid #9575cd;">
<strong style="color: #b39ddb; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 HILPCB : balanced copper design</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Staggered Traces</strong> limite le twist (I-Beam Effect) et stabilise l’impédance après des millions de bends.</p>
</div>
</div>

### Surface finish et pertes HF

OSP est très lisse (faible loss) mais moins robuste aux multiples reflow. ENIG/ENEPIG ajoutent une nickel layer qui augmente le loss à haute fréquence (>10GHz). Pour 28Gbps+, privilégier OSP ou Immersion Gold sans nickel si possible, en équilibrant fiabilité/cost.

### Backdrill quality control

Les via stubs résonnent (¼ λ) et creusent S21. Backdrill enlève le stub mais exige Z-depth control précis et vérification via TDR/microsection. Sans **Backdrill quality control**, risque d’overdrill et de failure.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#FFFFFF; text-align:center;">HILPCB capacité de fabrication haute précision</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; text-align: center;">
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Max layers</h4>
<p style="margin: 0; font-size: 1.2em;">64L (Rigid), 20L (Rigid-flex)</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Min trace/space</h4>
<p style="margin: 0; font-size: 1.2em;">2.5 / 2.5 mil</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Impedance tolerance</h4>
<p style="margin: 0; font-size: 1.2em;">±5%</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Backdrill depth tol.</h4>
<p style="margin: 0; font-size: 1.2em;">±0.05mm</p>
</div>
</div>
</div>

### Copper coin pour la thermique locale

**Copper coin** intègre un bloc cuivre dans le laminé et, via Thermal Vias, crée un chemin thermique vertical très efficace. Exige un contrôle précis et un process de lamination/CNC avancé.

### Cohérence manufacturing & test chez HILPCB

DFM + support simulation, contrôle **Microvia/stacked via** et **Backdrill quality control**, production stable **ENIG/ENEPIG/OSP**, validation VNA/TDR (S-parameters, coupons d’impédance) et service one-stop incluant [SMT assembly](https://hilpcb.com/en/products/smt-assembly).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**Rigid-flex PCB** est devenu mainstream pour miniaturisation, intégration et high-speed. En appliquant **Hybrid stack-up (Rogers+FR-4)**, **Microvia/stacked via**, **ENIG/ENEPIG/OSP**, **Backdrill quality control** et **Copper coin**, on dépasse les limites des PCB traditionnels. Avec un partenaire expérimenté comme HILPCB, les designs rigid-flex complexes se transforment en produits hautes performances.


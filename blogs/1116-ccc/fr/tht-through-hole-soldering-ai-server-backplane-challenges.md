---
title: "THT/through-hole soldering : maîtriser les défis d’interconnexion high-speed des backplane PCBs pour AI servers"
description: "Analyse approfondie de THT/through-hole soldering : SI, thermal management et power/interconnect design pour vous aider à construire des backplane PCBs AI server haute performance."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["THT/through-hole soldering", "AI server motherboard PCB mass production", "AI server motherboard PCB reliability", "AI server motherboard PCB stackup", "AI server motherboard PCB routing", "AI server motherboard PCB quick turn"]
---
Avec la croissance exponentielle des besoins de calcul AI/ML, la conception hardware des AI servers fait face à des défis inédits. En tant que hub reliant compute, storage et réseau, le design et la fabrication des backplane PCBs déterminent directement performance et stabilité du système. Bien que l’SMT soit dominante, pour les connectors devant supporter high current, de nombreux cycles d’insertion et des contraintes mécaniques sévères, **THT/through-hole soldering** reste indispensable grâce à sa reliability supérieure.

Cependant, à PCIe 5.0/6.0 et au-delà, le THT traditionnel devient un SI bottleneck. Savoir gérer les défis de THT/through-hole soldering et équilibrer mechanical strength, PI et high-speed SI est un sujet incontournable. Cela exige une optimisation end-to-end, des matériaux et du stackup jusqu’aux procédés de soldering. HILPCB fournit des services avancés de fabrication et assembly pour répondre aux besoins des AI servers de nouvelle génération.

### Pourquoi THT/through-hole soldering reste indispensable dans les backplanes AI server

L’SMT est avantageuse en densité et automatisation, mais dans les backplanes AI server, le THT apporte des avantages physiques difficiles à égaler, et reste la solution privilégiée pour les connectors critiques.

1.  **Mechanical strength et durabilité inégalées :** les connectors de backplane (ex. Orthogonal Midplane Connectors, OCP NIC 3.0) sont grands, riches en pins, et subissent de nombreux cycles. Les pins THT traversent le PCB et sont entièrement mouillés par la soudure, créant une liaison bien plus robuste que l’adhérence d’un pad SMT. C’est clé pour la **AI server motherboard PCB reliability** face à vibration et choc.

2.  **Excellente capacité high current :** les accelerator cards (GPU, TPU) dépassent souvent 1000W et nécessitent des centaines d’ampères via la backplane. Les pins THT et barrels PTH offrent une section bien plus grande que les pads SMT, avec moins de résistance et moins d’échauffement. Cela stabilise la PDN, réduit IR Drop et alimente proprement les puces.

3.  **Thermal paths simplifiés :** les pins THT conduisent aussi la chaleur vers les layers PWR/GND internes, dont les grandes surfaces cuivre jouent le rôle de heat spreader.

Dans un design AI server orienté performance, THT/through-hole soldering n’est donc pas un choix “legacy”, mais une stratégie pour une interconnexion high power et high reliability.

### High-speed SI : défis SI des THT vias et optimisation

À l’ère 56/112 Gbps PAM4, le via du connector THT devient une source majeure de défis SI. Sans optimisation, les vias peuvent fortement dégrader le signal.

*   **Via stub effect :** sur un multilayer PCB, la portion non utilisée forme un stub qui résonne, provoquant réflexion et Insertion Loss, pouvant fermer l’œil.
*   **Impedance discontinuity :** la géométrie du via crée un saut d’impédance, augmente Return Loss et introduit du Jitter.
*   **Via-to-via crosstalk :** dans les zones denses, les THT vias adjacents se couplent, causant du crosstalk, particulièrement critique en différentiel.

Pour résoudre, il faut un **AI server motherboard PCB routing** précis et une stratégie de fabrication. La technique la plus importante est **Back-drilling/Controlled Depth Drilling**, qui retire le stub depuis l’autre face. Un bon process contrôle le stub résiduel à 10mil (~254μm), nécessitant une excellente précision de profondeur. Anti-pad optimization, tuning des reference planes et ground-via shielding aident aussi au matching et à la réduction du crosstalk.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Comparaison SI avant/après optimisation THT via (simulation @ 28 GHz)</h3>
<table style="width:100%; border-collapse:collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Metric</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Standard THT via (unoptimized)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Optimized THT via (with back-drill)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Improvement</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Insertion Loss</td>
<td style="padding:12px; border:1px solid #ccc;">-4.5 dB (severe attenuation)</td>
<td style="padding:12px; border:1px solid #ccc;">-1.2 dB (significantly improved)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Improved 73%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Return Loss</td>
<td style="padding:12px; border:1px solid #ccc;">< -10 dB (strong reflection)</td>
<td style="padding:12px; border:1px solid #ccc;">< -18 dB (good match)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Reflection reduced > 8 dB</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Stub resonance point</td>
<td style="padding:12px; border:1px solid #ccc;">~15 GHz (limits bandwidth)</td>
<td style="padding:12px; border:1px solid #ccc;">> 40 GHz (moved out of band)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Resonance shifted > 160%</td>
</tr>
</tbody>
</table>
</div>

### Influence du stackup backplane sur la performance THT

Un **AI server motherboard PCB stackup** bien conçu est la base d’un THT performant. Le stackup définit les propriétés électriques et influence manufacturability et cost.

La sélection matériaux est critique : les backplanes utilisent souvent des Ultra-Low Loss materials comme Megtron 6/7 et Tachyon 100G (Dk/Df très bas). Des copper foils plats (HVLP) et du Spread Glass réduisent le Fiber Weave Effect et améliorent l’uniformité d’impédance en différentiel.

Le nombre de couches et l’épaisseur sont également clés : souvent 20–40 couches et >6mm. Cela complique le THT, notamment via l’Aspect Ratio. Des trous à aspect ratio élevé (18:1+) exigent un plating cuivre très uniforme ; des zones trop fines entraînent opens ou problèmes de reliability.

Enfin, la continuité des reference planes est essentielle pour un return path propre. Dans la zone connector, chaque via signal doit avoir un plan GND/PWR proche et continu. Splits/voids cassent le retour et augmentent EMI/crosstalk. HILPCB peut aider via son expérience [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Power integrity (PI) : défis high current des connectors THT

La backplane doit fournir une alimentation stable à un grand nombre de cores. Les connectors THT sont critiques ; la PI impacte directement la stabilité système.

Le défi principal est le high current et l’IR Drop. Un connector GPU peut transporter >500A à 12V ou 48V. Même avec une faible résistance des pins, la chute sur traces/vias/pins devient significative. Un drop trop élevé entraîne undervoltage, throttling ou crash.

Solutions :
*   **Heavy copper / ultra-heavy copper :** utiliser 3oz+ sur PWR/GND pour réduire la résistance. HILPCB fournit [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb).
*   **Optimiser le power path :** traces courtes et larges, plus de pins/vias THT en parallèle pour réduire la résistance.
*   **Découplage précis :** placer suffisamment de decoupling près des connectors power pour transients et suppression du bruit.

Un PDN robuste est la base de la yield et de la stabilité long terme de **AI server motherboard PCB mass production**.

<div style="background:linear-gradient(135deg, #E1BEE7, #CE93D8); color:#311B92; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#311B92;">Key points for THT power integrity design</h3>
<ul style="list-style-type: none; padding-left: 0;">
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Minimize loop inductance:</strong> rapprocher PWR/GND pins et raccourcir le return path.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Control IR Drop:</strong> calcul via PI simulation et optimisation via heavy copper ou plus de planes.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Strategic decoupling:</strong> réseau multi-niveaux entre connector et load (ex. VRM).</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Electro-thermal co-design:</strong> évaluer Joule heating et protéger **AI server motherboard PCB reliability**.</li>
</ul>
</div>

### Thermal management et reliability pour THT soldering

Le soldering est l’étape finale et la plus critique. Pour des backplanes épaisses à forte thermal mass, le Wave Soldering est difficile : le PCB absorbe beaucoup de chaleur, la zone de soudure manque de température, créant cold joints et défauts.

Les procédés modernes utilisent davantage :
*   **Selective Soldering :** un mini nozzle soude localement les zones THT, contrôle l’apport thermique et évite le thermal shock des SMT ; idéal pour SMT+THT.
*   **Pin-in-Paste / Intrusive Reflow :** imprimer la pâte dans les trous, insérer les pins puis reflow. La pâte remplit le barrel et forme un joint fiable. Compatible SMT, simplifie le flow et convient à **AI server motherboard PCB quick turn**.

La reliability long terme impose les exigences IPC-A-610 sur le Barrel Fill (souvent 75%+). L’X-Ray NDT est nécessaire pour vérifier voids/cracks.

### DFM : manufacturability et yield des backplanes THT

Un [backplane PCB](https://hilpcb.com/en/products/backplane-pcb) parfait en théorie peut échouer en production si le DFM est négligé. Pour les backplanes THT complexes, le DFM est crucial.

*   **Aspect Ratio :** épaisseur / diamètre de perçage minimum. Trop élevé → plating insuffisant au centre. Il faut respecter la capability du fabricant.
*   **Annular Ring :** anneau cuivre autour du trou ; largeur suffisante pour tolérances de perçage, selon classes IPC.
*   **Spacing et tolérances :** hole-to-copper, hole-to-hole, back-drill depth tolerance, impactant performance et yield.

HILPCB propose une analyse DFM gratuite : revue des fichiers avant production, identification des risques et recommandations, pour sécuriser **AI server motherboard PCB mass production**.

<div style="background-color:#1A237E; color:white; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:white;">HILPCB high-complexity backplane manufacturing capability</h3>
<table style="width:100%; border-collapse:collapse; color:white;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">Process parameter</th>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">HILPCB capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max layer count</td>
<td style="padding:12px; border:1px solid #7986CB;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max PCB thickness</td>
<td style="padding:12px; border:1px solid #7986CB;">10.0 mm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max drill aspect ratio</td>
<td style="padding:12px; border:1px solid #7986CB;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Back-drill depth control</td>
<td style="padding:12px; border:1px solid #7986CB;">± 50 µm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #7986CB;">± 5%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Supported materials</td>
<td style="padding:12px; border:1px solid #7986CB;">Megtron 6/7, Rogers, Tachyon 100G, etc.</td>
</tr>
</tbody>
</table>
</div>

### Comment HILPCB assure un THT/through-hole soldering haute fiabilité

HILPCB intègre advanced equipment, contrôle process strict et expertise engineering pour que chaque opération de THT/through-hole soldering atteigne le plus haut standard.

1.  **Advanced fabrication & assembly equipment :** drilling mécanique/laser de haute précision, plating lines avancées, automation pour selective soldering et intrusive reflow, assurant cohérence et précision.
2.  **Contrôle qualité strict :** AOI sur inner-layers, X-Ray sur registration et barrel fill THT. Tests électriques et reliability tests (ex. thermal shock) garantissent des [backplane PCB](https://hilpcb.com/en/products/backplane-pcb) robustes.
3.  **One-stop solution :** optimisation **AI server motherboard PCB stackup**/**AI server motherboard PCB routing**, quick turn, volume production et [through-hole assembly](https://hilpcb.com/en/products/through-hole-assembly) : un flux end-to-end qui sécurise la qualité et réduit le time-to-market pour **AI server motherboard PCB quick turn**.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**THT/through-hole soldering** reste essentiel dans les backplanes AI server modernes. Ce n’est plus une simple “insertion soldering”, mais un engineering complexe combinant high-speed SI, PI, thermal management et precision manufacturing. La réussite exige une collaboration étroite entre designers et fabricants expérimentés comme HILPCB.

Avec un back-drilling avancé, un stackup maîtrisé, un PDN robuste et des procédés de soldering contrôlables, nous pouvons combiner les avantages reliability du THT avec les exigences high-speed. Si vous développez des AI servers, switches ou systèmes HPC nouvelle génération et recherchez un partenaire capable de résoudre les défis THT/through-hole soldering, HILPCB est un excellent choix.


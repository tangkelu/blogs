---
title: "gerber data preparation : livre blanc fabrication PCB & management qualité"
description: "Explique process capability (CPK), yield improvement, quality tools, test coverage et traceability pour gerber data preparation—avec une checklist DFM/DFT/DFR pour structurer une collaboration robuste entre design et manufacturing."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 9
tags: ["gerber data preparation", "soldermask exposure tutorial", "yield improvement roadmap", "aoI spi best practices", "fab drawing essentials", "smt stencil design tutorial"]
---
## 1. Executive summary : objectifs qualité et métriques business

Chez HILPCB, nous pensons que les meilleurs produits électroniques commencent par un blueprint digital irréprochable. La “source” de la fabrication PCB—`gerber data preparation`—n’est pas une simple conversion de fichiers : c’est un déterminant majeur du yield, de la fiabilité et du coût final. La moindre déviation, ambiguïté ou omission dans les Gerber peut être amplifiée de façon exponentielle tout au long de la fabrication, de l’assembly et des tests, entraînant des dépassements de coûts, des retards, voire des field failures.

Ce livre blanc explique de manière systématique comment HILPCB construit un système de management qualité end-to-end autour des données Gerber. Notre objectif est d’établir avec les clients une relation de manufacturing transparente et collaborative, en convertissant le Design Intent en Physical Reality sans perte.

**Engagements clés et métriques opérationnelles :**
*   **First Pass Yield (FPY):** > 99.5%
*   **Critical process capability (CPK):** > 1.67
*   **On-Time Delivery (OTD):** > 98%
*   **DFM feedback cycle:** < 4 hours

Grâce à un DFM/DFT front-loaded, un process control strict (SPC), une test coverage complète et une traceability digitale de bout en bout, nous garantissons que dès l’upload des Gerber, chaque décision de fabrication est data-driven et chaque risque qualité est activement maîtrisé. Ce n’est pas seulement un flux de production : c’est une `yield improvement roadmap` complète.

<div class="div-type-1">
    <h3>Des données à l’excellence : Gerber est le socle de la qualité</h3>
    <p>Nous exécutons des contrôles DFM automatisés sur 500+ règles Gerber afin d’identifier et d’optimiser les risques de manufacturability, testability et reliability avant la fabrication physique. Cela maintient notre FPY moyenne au-dessus de 99.5% et fait gagner aux clients du temps et des coûts d’itération.</p>
</div>

---

## 2. Manufacturing capability data : traduire les specs Gerber en précision physique

Chaque ligne, pad et perçage dans les Gerber correspond à une étape de process physique. HILPCB vise à reproduire ces instructions digitales avec précision et à garantir la cohérence via un process control quantifié. Le tableau ci-dessous met en regard les paramètres Gerber clés, nos capability, nos métriques de contrôle et des cas typiques de mass production.

| Process | Key Gerber parameter | HILPCB capability & tolerance | Process control metric | Mass production case |
| :--- | :--- | :--- | :--- | :--- |
| **Imaging** | Min. trace/space | 2.5/2.5 mil (0.0635mm) | LDI alignment accuracy: ±0.5 mil | 5G module, HDI |
| **Drilling** | Min. mechanical drill | 0.15mm (6 mil) | Hole position accuracy: ±1 mil | Automotive ECU |
| **Drilling** | Min. laser drill | 0.075mm (3 mil) | Laser blind-via depth control: ±10% | Smartphone mainboard, Anylayer |
| **Plating** | PTH copper thickness | Avg. > 25µm | Copper thickness uniformity CV < 8% (SPC) | Industrial server power board |
| **Soldermask** | Solder mask dam | ≥ 3 mil (0.076mm) | Soldermask registration: ±1.5 mil | High-precision medical sensor |
| **Surface finish** | BGA pad size/flatness | ENIG Au: 2–4 µin | XRF sampling for Au/Ni thickness (CPK > 1.67) | AI compute substrate |
| **Routing** | Profile tolerance | ±0.1mm (4 mil) | CNC path accuracy: ±0.05mm | Consumer enclosure board |

<div class="div-type-6">
    <h3>Investir dans la précision : notre force de manufacturing</h3>
    <p>HILPCB utilise des équipements de pointe tels que Schmoll drilling (Germany), Mitsubishi laser drilling (Japan) et Orbotech LDI (Israel). Ces investissements permettent des <code>fab drawing essentials</code> plus exigeants et garantissent que chaque feature définie en Gerber est produite avec une haute précision stable, en maintenant CPK au-dessus de 1.67.</p>
</div>

---

## 3. Quality tools : optimisation de process data-driven

Nous pensons que la qualité se conçoit et se fabrique—elle ne se “rajoute” pas par l’inspection. HILPCB déploie un toolkit qualité digital complet, qui étend les standards de `gerber data preparation` à chaque étape de production.

*   **SPC (Statistical Process Control):** checkpoints SPC en temps réel sur plating, etching, lamination, etc. Par exemple, les cartes de contrôle de largeur de ligne en etching suivent la dérive ; lorsque les tendances approchent les limites, des alertes déclenchent des ajustements engineering avant l’apparition de défauts.

*   **CPK (Process Capability Index):** CPK > 1.67 est notre minimum pour les étapes critiques—signe d’une distribution serrée et d’une marge solide face à la variation normale.

*   **MSA (Measurement System Analysis):** Gage R&R régulier pour AOI, X-Ray, flying probe, etc., afin que la variation de mesure soit bien inférieure à la variation de process.

*   **8D problem solving:** en cas d’anomalie, nous appliquons l’8D du containment à la root cause jusqu’aux corrective actions systémiques. Par exemple, un défaut de soudure BGA peut être relié à la conception de soldermask dans les Gerber et conduire à des mises à jour des règles DFM.

*   **Digital quality dashboard:** visibilité en temps réel sur FPY, CPK, equipment OEE et statut qualité du WIP pour décider vite et allouer les ressources efficacement.

---

## 4. SMT/assembly capability et defect control

La qualité de la bare-board est un prérequis au succès PCBA. Dans les Gerber, les layers paste et silkscreen influencent fortement les résultats SMT.

**Des Gerber à des joints de soudure parfaits :**
Nous commençons par une analyse approfondie du Gerber paste layer—plus qu’un stencil 1:1 ; c’est l’application pratique de `smt stencil design tutorial`.

1.  **Stencil optimization:** selon les component types (01005, 0.4mm-pitch BGA), le pad design et le process de reflow, nous optimisons les paste apertures :
    *   **Aperture reduction/enlargement:** réduire bridging ou opens.
    *   **Rounded corners / anti-solder-ball:** améliorer le release et réduire les défauts.
    *   **Step stencil:** permettre des volumes de pâte différenciés pour des assemblages mixtes (gros composants + fine pitch).

2.  **SPI (Solder Paste Inspection):** inspection SPI 3D à 100%. SPI mesure volume, area, height et offset pour maintenir la pâte dans les process windows. C’est le cœur de `aoI spi best practices` et cela peut prévenir >60% des défauts SMT.

3.  **AOI (Automated Optical Inspection):** l’AOI avant et après reflow détecte wrong/missing parts, polarité, opens, bridges, etc. Notre AOI program library est liée aux component libraries et peut auto-générer les programmes d’inspection à partir des Gerber et de la BOM, améliorant accuracy et efficiency.

<div class="div-type-3">
    <h3>Notre trajectoire : une zero-defect SMT roadmap</h3>
    <p>En intégrant SPI/AOI à notre MES, nous construisons un closed-loop feedback system. Si SPI détecte des offsets pâte répétés, le système alerte les opérateurs pour calibrer l’imprimante. Si l’AOI montre une hausse du defect rate sur un composant, les ingénieurs reviewent les profils de reflow et le design du stencil. Cette amélioration continue data-driven est une pierre angulaire du parcours HILPCB vers le zero-defect manufacturing.</p>
</div>

---

## 5. Test coverage : vérification complète du design intent

Le testing est la dernière—et la plus critique—barrière pour valider la fonction PCB/PCBA. Notre stratégie est multi-couches et complète afin de détecter efficacement différentes classes de défauts. La planification des test points doit commencer dans `gerber data preparation` via des règles DFT.

| Test type | Objective | Typical coverage | Defect spectrum |
| :--- | :--- | :--- | :--- |
| **Flying probe** | Bare-board electrical connectivity | 100% nets | Opens, shorts, high resistance |
| **ICT** | Component-level PCBA defects | >95% components | Wrong/missing, opens/shorts, value errors |
| **FCT** | Validate product function in simulated use | 100% critical functions | Logic errors, performance failures, firmware issues |
| **Hipot** | Verify insulation strength and safety | 100% (as required) | Breakdown, insufficient spacing |
| **Burn-in** | Screen early-life failures | 100% (high-reliability) | Early component failure, latent solder defects |
| **Reliability test** | Long-term stability (temp cycle, vibration) | Sampling/as needed | Material fatigue, thermal mismatch, long-term reliability |

---

## 6. Traceability : digital thread des Gerber au produit fini

Dans la fabrication d’électronique complexe, localiser rapidement et précisément la root cause est essentiel. Le système de traceability full-chain de HILPCB donne à chaque PCB une “digital identity” unique et enregistre les données de cycle de vie complet, de la naissance à la livraison.

*   **Unique ID:** chaque PCB (ou panel) reçoit un QR code unique au découpage matière. Cet ID relie la Gerber version du client, la BOM version et toutes les instructions de production.
*   **Process data capture:** à chaque station clé (imaging, plating, SPI, AOI, ICT, FCT), l’équipement scanne le QR et uploade en temps réel vers le MES les paramètres de process (temperature/pressure/time), les lots matière, machine IDs, operator IDs et résultats d’inspection.
*   **Data lake + visualization:** toutes les données sont centralisées. En saisissant un numéro de série PCB, nous pouvons obtenir un rapport d’historique complet en 5 secondes :
    *   Quel jour, quelle machine, quelle ligne l’a produite ?
    *   Quels laminate lots et component lots ont été utilisés ?
    *   Quelles images SPI/AOI sont associées ?
    *   Quels logs et valeurs ICT/FCT ont été enregistrés ?

Cette traceability ne sert pas uniquement à l’after-sales ; c’est le moteur de données de la `yield improvement roadmap`. L’analyse de corrélation peut révéler des liens subtils entre lots matière et yield, ou l’impact d’une dérive équipement sur la performance—permettant des améliorations qualité proactives.

---

## 7. DFM/DFT/DFR checklist : relier design et manufacturing collaboration

Les programmes réussis reposent sur une collaboration étroite entre design et manufacturing. La checklist ci-dessous résume 35+ checkpoints clés de `gerber data preparation`, couvrant DFM, DFT et DFR. Nous recommandons de l’utiliser pendant le design pour minimiser les EQ et les changements tardifs.

| Category | Check item | Recommendation / standard | Impact |
| :--- | :--- | :--- | :--- |
| **Gerber data integrity** | 1. File format | RS-274X (Extended Gerber) | Avoid layer alignment errors |
| | 2. Layer order | Provide clear stackup order diagram/notes | Ensure correct lamination |
| | 3. Drill files | Excellon + tool table | Avoid wrong hole sizes |
| | 4. `fab drawing essentials` | Include thickness/tolerance/material/soldermask color etc. | Reduce ambiguity and EQ |
| | 5. Coordinate origin | Use a unified origin across all layers | Ensure accurate registration |
| **DFM - fabrication** | 6. Min trace/space | Follow capability with 20% margin | Improve etch yield |
| | 7. Copper-to-edge | Outer ≥ 0.2mm, inner ≥ 0.3mm | Prevent exposure/short |
| | 8. Pad-to-trace | Smooth transitions, no sharp corners | Reduce Acid Trap |
| | 9. BGA pad design | Prefer NSMD; mask opening 3–4 mil larger | Improve solder reliability |
| | 10. Solder mask dam | ≥ 3 mil (fine pitch) | Prevent bridging |
| | 11. `soldermask exposure tutorial` | Uniform solder mask expansion, typically 1–2 mil | Ensure pad exposure |
| | 12. Via tenting/plugging | Clearly define plugging or tenting | Avoid solder wicking/short |
| | 13. Silkscreen | No silkscreen on pads; line ≥ 5 mil; text ≥ 30 mil | Readability; no solder impact |
| | 14. Gold finger design | Chamfer edge connectors | Improve insertion; protect plating |
| | 15. Panelization | V-cut or mouse-bites; consider rails | Improve SMT efficiency & depanel |
| **DFM - assembly** | 16. Component spacing | Same ≥ 10 mil, mixed ≥ 20 mil | Placement/rework/AOI |
| | 17. Orientation | Keep polarity parts consistent | Reduce placement errors |
| | 18. `smt stencil design tutorial` | Paste aperture area ratio > 0.66 | Ensure good paste release |
| | 19. Fiducials | ≥3 per board, diagonal, away from edge | SMT alignment |
| | 20. Tall parts | Avoid near fine-pitch parts | Reflow/rework access |
| | 21. Via-in-Pad | Resin plug + copper fill & planarization (POFV) | Prevent voids/opens under BGA |
| **DFT - test** | 22. Test points | 100% test points on critical nets | Improve ICT/flying probe |
| | 23. TP size/spacing | Dia ≥ 0.8mm, pitch ≥ 1.27mm | Stable probe contact |
| | 24. TP distribution | Evenly on both sides | Balance fixture stress |
| | 25. JTAG/SWD | Reserve debug/programming | Firmware + boundary scan |
| | 26. Power net test | Provide TP per power net | Validate PI |
| **DFR - reliability** | 27. Orphan pads | Avoid unconnected inner pads | Reduce reliability risk |
| | 28. Teardrops | Add at pad-trace junctions | Strength; drill tolerance |
| | 29. Copper fill | Use hatch; avoid solid large copper | Reduce warp |
| | 30. Thermal pads | Use on PWR/GND via pads | Improve solderability |
| | 31. Impedance control | Provide impedance + stackup | Ensure HS SI |
| | 32. Dead copper | Remove unconnected inner copper | Avoid antenna effects |
| | 33. HV spacing | Follow IPC-2221B (clearance/creepage) | Product safety |
| | 34. Material selection | Choose FR-4/Rogers by freq/temp/env | Long-term stability |
| | 35. Annular ring | Min annular ring ≥ 3 mil | Reliable layer connectivity |

---

## 8. HILPCB collaboration case et perspectives

**Case:** un client majeur du secteur médical développant un instrument de diagnostic portable faisait face à des resets intermittents sous certaines conditions de vibration. La FPY de son premier prototype n’était que de 85% et le défaut était difficile à reproduire.

**Notre flow de collaboration :**
1.  **Deep DFM/DFR analysis:** après l’upload des Gerber et des fichiers de design, nous avons exécuté le DFM standard ainsi qu’un DFR ciblé. Nous avons trouvé plusieurs vias sous un BGA critique sans teardrops, et aux extrêmes de tolérance de perçage l’annular ring devenait très faible.
2.  **Traceability analysis:** nous avons extrait les données de production complètes des échantillons en échec. Elles montraient que tous provenaient d’un même batch avec une drill Z-axis compensation proche de la limite supérieure de contrôle.
3.  **Root-cause hypothesis:** nous avons conclu que le stress mécanique (vibration) combiné à de faibles variations de manufacturing provoquait des micro-cracks au niveau de la connexion BGA solder joint / inner-layer, entraînant des défauts électriques intermittents.
4.  **Co-optimization and validation:** nous avons fourni un rapport détaillé et recommandé deux modifications Gerber : ajouter des teardrops sur les vias/pads critiques et élargir le routing pour augmenter les annular rings des vias clés. Le client a adopté les changements et nous avons produit un nouveau lot de prototypes.

**Result:** la FPY est passée à **99.8%** et les tests vibration/choc n’ont plus reproduit de resets. Avec une collaboration étroite sur `gerber data preparation`, nous n’avons pas seulement résolu le problème de yield ; nous avons amélioré la fiabilité long terme de façon fondamentale.

**Travailler avec HILPCB, c’est obtenir non seulement des PCB de haute qualité, mais aussi un engineering partner.** Nous intervenons tôt pour transformer l’expérience manufacturing et les quality tools en avantage de design—afin de construire des produits stables, fiables et compétitifs.

**Prêt à démarrer votre journey vers l’excellence manufacturing ?**

Uploadez vos Gerber maintenant pour recevoir un DFM report gratuit.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Cet article explique gerber data preparation depuis la capability (CPK) et le yield improvement jusqu’aux quality tools, test coverage et traceability—avec une checklist DFM/DFT/DFR pour structurer les mécanismes de collaboration. En suivant la checklist/les process windows et en impliquant tôt l’équipe DFM/DFA de HILPCB, vous pouvez accélérer prototype et mass production tout en conservant qualité et compliance.

> Besoin de support fabrication ou assembly ? Contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.

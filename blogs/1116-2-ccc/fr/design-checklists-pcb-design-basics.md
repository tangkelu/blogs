---
title: "pcb design checklists : livre blanc pour construire un workflow PCB manufacturable"
description: "Pour les responsables design : framework piloté par pcb design checklists avec stackup/routing strategy, checklists DFM/DFT et templates de design handoff pour aligner design et manufacturing."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 9
tags: ["pcb design checklists", "drc rule template pcb", "mixed signal pcb layout", "pcb loop area reduction", "pcb stackup tutorial", "split plane design guide"]
---
## 1. Executive summary : du chaos au contrôle — la révolution “Checklist-driven”

Dans le développement électronique high-speed/high-density, le PCB design est devenu un goulot d’étranglement critique. Des données de l’industrie montrent que plus de 70% des retards projets sont directement liés aux respins PCB : chaque itération entraîne des semaines de retard et des coûts de dizaines à centaines de milliers de dollars. Les douleurs typiques : absence de processus standard, qualité trop dépendante des seniors, rupture design/manufacturing (les problèmes DFM apparaissent trop tard), faible capitalisation et réutilisation des connaissances, onboarding long.

Ce livre blanc du HILPCB Design Enablement Center propose un processus standardisé piloté par **pcb design checklists**. Nous présentons un maturity model, des méthodes pratiques de stackup planning, des stratégies modulaires de placement/routing, une checklist DFM/DFT et des templates de design handoff. Objectif : un système prédictible et réplicable visant >95% de first-pass success, compatible avec la plateforme digitale de manufacturing HILPCB.

## 2. PCB design process maturity model : où en est votre équipe ?

| Niveau | Caractéristiques | Défis clés | Outils & méthodes |
| :--- | :--- | :--- | :--- |
| **L1: Experience-driven (Ad-hoc)** | - Process non documenté, dépend des habitudes individuelles.<br>- Checks limités aux defaults EDA.<br>- Reviews formelles sans checklist structurée.<br>- Interaction fabricant limitée au DFM pre-release. | - Qualité instable, rework élevé.<br>- Knowledge transfer difficile.<br>- Risque projet mal contrôlé. | - Notes perso<br>- EDA default DRC |
| **L2: Template-based (Standardized)** | - Templates de base (schematic spec, naming Gerber).<br>- Premières **pcb design checklists** incomplètes.<br>- Reviews avec agenda mais peu de métriques. | - Exécution incohérente.<br>- Checklist en retard vs process capability.<br>- Faible efficacité cross-team. | - Wiki/docs<br>- `drc rule template pcb` |
| **L3: Managed** | - Checklist end-to-end (requirements → layout → routing → handoff).<br>- DFM/DFT obligatoires pour le sign-off.<br>- Règles synchronisées avec manufacturing capability.<br>- Versioning via PLM/PDM. | - Enforcement ?<br>- Mesure qualité/efficacité ?<br>- Feedback data vers design ? | - PLM/PDM<br>- Collaboration platform<br>- DFM tools |
| **L4: Optimized** | - KPI quantitatifs (first-pass, impedance hit rate).<br>- Données AOI/e-test yield optimisent les règles.<br>- Automatisation des checks.<br>- Libraries modulaires réutilisables (IP). | - Complexité data/analysis.<br>- Compétences cross-domaine.<br>- Forte intégration toolchain. | - Automated review<br>- BI/data platform<br>- Traceability HILPCB |

## 3. Stackup, matériaux et impédance : les fondations

Le stackup définit les limites SI/PI et EMC. Un mauvais stackup est difficile à rattraper au routing. Recommandation : co-design du stackup avec HILPCB dès la phase schematic.

<div class="div-style-1">
    <h4>Trois piliers du stackup planning</h4>
    <ul>
        <li><strong>Signal Integrity (SI) first :</strong>reference planes continus pour les signaux critiques (impedance control, crosstalk).</li>
        <li><strong>Power Integrity (PI) :</strong>plans PWR/GND couplés pour un PDN low-impedance.</li>
        <li><strong>Cost & lead time :</strong>privilégier matériaux/stackups standards HILPCB, éviter l’asymétrie et les matériaux “exotiques” sans besoin.</li>
    </ul>
</div>

| Scénario | Stackup recommandé (exemple) | Matériaux | Notes clés |
| :--- | :--- | :--- | :--- |
| **High-speed digital (server, AI accelerator)** | 12L: SIG-GND-SIG-PWR-GND-SIG-SIG-GND-PWR-SIG-GND-SIG | Mid/low-loss (IT-158, S7439) | - 50Ω/90Ω/100Ω ±5%.<br>- Reference plane adjacent et continu.<br>- PWR/GND coupling pour PDN. |
| **Mixed-signal (DAQ, medical)** | 8L: ANA_SIG-ANA_GND-DIG_SIG-DIG_GND-PWR-DIG_SIG-DIG_GND-ANA_SIG | FR-4 Tg150/170 | - Partition analog/digital.<br>- [split plane design guide](/blog/split-plane-design-guide).<br>- Analog loin du digital HS. |
| **RF/microwave (5G)** | 10L hybrid | RF: Rogers/Taconic<br>Digital: FR-4 | - Dk/Df stables.<br>- ±2–3%.<br>- Simulation alignée aux données HILPCB. |

**Action :** utiliser [pcb stackup tutorial](/blog/pcb-stackup-tutorial) et demander un modeling basé sur des paramètres de production réels.

## 4. Library de stratégies modulaires (placement/routing)

Documenter et templatiser des règles pour modules récurrents (power, CPU core, DDR) améliore vitesse et qualité.

<div class="div-style-3">
    <h4>Chemin d’implémentation</h4>
    <ol>
        <li><strong>Identifier les modules :</strong>SMPS, DDR4/5, PCIe, Ethernet PHY, etc.</li>
        <li><strong>Documenter best practices :</strong>ex. SMPS: placement des caps, feedback routing, [pcb loop area reduction](/blog/pcb-loop-area-reduction) pour réduire EMI.</li>
        <li><strong>Créer des templates DRC :</strong>mettre en forme en `drc rule template pcb` (DDR4: diff pair spacing, length-match, max via count).</li>
        <li><strong>Review & itération :</strong>reviews périodiques et implication des manufacturing engineers HILPCB.</li>
    </ol>
</div>

**Exemples de contenu :**
*   **High-speed diff pairs:** same-layer, tight coupling, length-match, reference plane continuity.
*   **PDN:** placement des decoupling (small-to-large) et via stitching.
*   **Mixed-signal:** règles de [mixed signal pcb layout](/blog/mixed-signal-pcb-layout), star ground vs single-point ground.
*   **Clock:** H-tree/star topology, termination, shielding via GND.

## 5. Checklist DFM/DFT/DFA : >35 “golden rules” à vérifier

| Category | Rule / check item | Recommended spec | Risk if violated | How to verify |
| :--- | :--- | :--- | :--- | :--- |
| **DFM** | **Min trace/space** | ≥ 3/3 mil (0.076mm) | Shorts/opens, yield drop | EDA DRC, CAM |
| | **Min annular ring** | ≥ 3 mil (outer), ≥ 2.5 mil (inner) | Drill offset → open/breakout | EDA DRC, Gerber |
| | **BGA pad to via (Via-in-Pad)** | Prefer VIPPO, or ensure via plugging/copper fill & planarization | Solder wicking → opens | Spec, DFM tool |
| | **Copper to board edge** | ≥ 12 mil (inner), ≥ 8 mil (outer) | Exposed copper / shorts at routing | EDA DRC, FAB drawing |
| | **Aspect ratio** | ≤ 10:1 (thickness/drill) | Uneven plating, weak PTH reliability | Stackup design, DFM |
| | **Copper island** | Remove floating copper | Can peel in etch and short | EDA rule check |
| | **Solder mask bridge** | ≥ 3 mil (0.076mm) | Solder bridging on fine pitch | EDA DRC, Gerber |
| | **Silkscreen on pad** | Prohibited | Poor solderability, solder defects | Gerber review |
| | **Unused pads** | Remove if possible | Fewer drills, lower cost | EDA cleanup |
| | **Lamination void prevention** | Hatch/grid large copper | Delamination / blowout risk | Design spec |
| | **Min slot width** | ≥ 0.6mm | Tool breakage, hard machining | FAB drawing |
| **DFA** | **Component spacing** | Same type: ≥ 12 mil; mixed: ≥ 20 mil | Hard to solder/rework | 3D check, DFA tool |
| | **Component-to-edge** | ≥ 120 mil (with rails) | Cannot pass reflow conveyor | Placement check, DFA tool |
| | **Fiducials** | 3, L-shape, ≥120 mil from edge | Pick-and-place misalignment | Placement check |
| | **Polarity marking** | Clear (diodes, caps) | Reverse placement, functional failure | Schematic vs PCB |
| | **Tall parts** | Avoid clustering | Impacts wave/selective soldering | 3D check |
| | **0201/01005** | Follow IPC-7351B footprint | Tombstoning risk | Library check |
| | **Vias under BGA** | Avoid unless filled/plugged | Solder wicking → BGA open | Placement check |
| | **Thermal pad** | Cross / X-style spokes | Hard soldering, opens | Library check |
| | **Panelization** | V-cut or mouse-bites; rails ≥ 5mm | Not SMT-producible | Panel drawing review |
| **DFT** | **Test-point coverage** | Critical nets > 90% | Faults hard to localize | Test plan review |
| | **Test-point size/spacing** | Dia ≥ 0.8mm, pitch ≥ 1.27mm | Poor probe contact | DFT rules |
| | **Test-point distribution** | Evenly spread | Fixture stress, board bending | DFT analysis |
| | **ICT test points** | At end of nets, away from tall parts | ICT not feasible | Placement review |
| | **JTAG chain** | TCK/TMS/TDI/TDO complete | Boundary-scan not possible | Schematic/layout |
| **Electrical** | **Impedance tolerance** | Target ±10%, critical ±5% | Reflections/distortion | Stackup, sim |
| | **Return-path continuity** | No splits under high-speed | Z discontinuity, EMI | Split-cross check |
| | **Decoupling placement** | Close to pins, shortest path | Weak HF noise suppression | Layout review |
| | **Crosstalk** | Meet 3W or stricter | Coupling/interference | SI sim, EDA DRC |
| | **Via count on high-speed** | Minimize; keep diff pairs consistent | Z discontinuity, loss | Layout review |
| | **Power plane integrity** | Avoid over-splitting by signals | More noise and IR drop | Plane check |
| | **Ground bounce** | Sufficient ground vias | Logic threshold errors | PI sim |
| | **ESD protection** | Place near connectors | ESD damage risk | Schematic/layout |
| | **Clock shielding** | Guard with ground traces | Clock susceptible to noise | Layout review |
| | **Analog/digital ground isolation** | Single-point or ferrite bead | Digital noise contaminates analog | Layout review |

## 6. Design → manufacturing handoff : transfert d’information sans perte

Un package `design handoff` clair et complet est essentiel. Toute ambiguïté crée du retard ou des erreurs.

**Checklist des livrables standard :**
1.  **Gerber files (RS-274X ou ODB++):**
    *   [ ] All copper layers (Top, Bottom, Inner layers)
    *   [ ] Solder mask (Top/Bottom Solder Mask)
    *   [ ] Silkscreen (Top/Bottom Silkscreen)
    *   [ ] Solder paste (Top/Bottom Solder Paste)
    *   [ ] Drill drawing layers (Drill Drawing)
    *   [ ] Board outline layer (Board Outline)
2.  **NC drill file:**
    *   [ ] Excellon (tailles et positions).
3.  **Stackup report:**
    *   [ ] Stackup détaillé (dielectric/copper thickness, matériaux, ex. FR-4 S1000-2M).
    *   [ ] Targets d’impédance et correspondances layer/largeur.
4.  **FAB drawing:**
    *   [ ] Laminate, Tg, finish (ENIG, lead-free HASL).
    *   [ ] Tolerances thickness et profil.
    *   [ ] Couleurs solder mask et silkscreen.
    *   [ ] Exigences spéciales (impedance control, gold fingers, blind/buried vias).
5.  **BOM:**
    *   [ ] RefDes, Qty, MPN, package, description.
    *   [ ] DNI (Do Not Install).
6.  **Pick and place / centroid:**
    *   [ ] Centroids, rotations, side.
7.  **Test plan:**
    *   [ ] Exigences ICT/FCT et test points.

<div class="cta-div">
    <div class="cta-content">
        <h3>Prêt à démarrer votre journey de design standardisé ?</h3>
        <p>Téléchargez les templates de handoff et checklists complètes HILPCB pour un passage fluide du design au manufacturing. Nos experts peuvent fournir un DFM pre-review gratuit.</p>
    </div>
    Obtenir templates & review gratuit
</div>

## 7. KPI : mesurer et améliorer

*   **FPY:** target **>95%**.
*   **ECOs per project:** changements entre design freeze et mass production.
*   **Impedance hit rate:** via TDR coupon; target **≥98%** dans **±5%**.
*   **Prototype cycle time:** réduit via handoff standard et partenaires agiles comme HILPCB.

## 8. Services HILPCB : closed loop entre règles et données de production

<div class="div-style-6">
    <h4>HILPCB digital manufacturing capabilities</h4>
    <p>De AOI à X-Ray et TDR, les données sont collectées et analysées pour fournir un feedback “real-world” et améliorer les règles de design.</p>
</div>

**Services core :**
*   **Process coaching & checklist customization:** **pcb design checklists** et `drc rule template pcb`.
*   **Early co-design:** stackup/material selection + DFM pre-review.
*   **Digital traceability & data feedback:** archivage reports (impédance, yield).

<div class="cta-div">
    <div class="cta-content">
        <h3>Prêt à démarrer votre journey de design standardisé ?</h3>
        <p>Téléchargez les templates de handoff et checklists complètes HILPCB pour un passage fluide du design au manufacturing. Nos experts peuvent fournir un DFM pre-review gratuit.</p>
    </div>
    Obtenir templates & review gratuit
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Ce document fournit un framework guidé par pcb design checklists (stackup/routing strategy, checklists DFM/DFT, templates handoff) pour gérer les risques et augmenter le first-pass success. En appliquant la checklist et en impliquant tôt l’équipe DFM/DFA HILPCB, vous accélérez proto et production en maintenant qualité et compliance.

> Besoin de fabrication ou d’assemblage ? Contactez HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) ou [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) pour des recommandations DFM/DFT.


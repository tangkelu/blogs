---
title: "Low-loss RDL fan-out substrate : défis de packaging et high-speed interconnect pour AI chip interconnect et substrate PCB"
description: "Analyse de low-loss RDL fan-out substrate : high-speed SI, thermal management et conception power/interconnect pour AI chip interconnect et substrate PCB hautes performances."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["low-loss RDL fan-out substrate", "RDL fan-out substrate cost optimization", "RDL fan-out substrate design", "RDL fan-out substrate stackup", "RDL fan-out substrate impedance control", "RDL fan-out substrate quick turn"]
---
En tant que PI engineer spécialisé en high-density power integrity, je fais face chaque jour aux défis extrêmes des AI chips : centaines à milliers d’ampères de transient current, load steps à l’échelle nanoseconde, et alimentation stable/“clean” pour des dizaines de milliers d’I/O dans un volume toujours plus contraint. Dans ce contexte, l’advanced packaging est décisif—et **low-loss RDL fan-out substrate** est au cœur de la révolution. Ce n’est pas seulement un pont entre le die et l’extérieur : c’est la fondation pour délivrer la compute performance de façon complète et efficace. Sans un substrate low-loss bien conçu, un AI chip puissant reste “puissant sur le papier”.

L’essor rapide de l’AI et du high-performance computing (HPC) pousse les limites du packaging. Avec des architectures Chiplet, intégrer plusieurs dies (CPU, GPU, HBM) dans un seul package exige une interconnect density, des data rates et une efficacité de power delivery inédites. Wire bonding et flip-chip traditionnels ne suffisent plus. Grâce à ses performances électriques, sa capacité thermique et son routing haute densité, **low-loss RDL fan-out substrate** devient un composant indispensable des solutions 2.5D/3D.

### What Defines a Low-Loss RDL Fan-Out Substrate in AI Applications?

RDL (Redistribution Layer) est un empilement de metal routing et de layers diélectriques fabriqués sur wafer/panel, qui redistribue les petits pads denses du die vers des BGA à pitch plus large. Fan-Out signifie que l’aire RDL peut dépasser l’empreinte du die, accueillant plus d’I/O et intégrant plusieurs Chiplets.

“Low-loss” est l’exigence électrique ultime. En AI, les data rates atteignent le Tbps (ex. HBM3e) et les fréquences montent à plusieurs dizaines de GHz. À ces fréquences, l’insertion loss devient extrêmement sensible. Un **low-loss RDL fan-out substrate** se caractérise par :

1.  **Dielectric loss ultra-faible :** matériaux à faible Dk/Df (ABF, résines modifiées) pour limiter l’énergie absorbée et transformée en chaleur.
2.  **Conductor loss optimisé :** avec le skin effect, le courant se concentre en surface ; copper plus lisse et géométries contrôlées réduisent les pertes.
3.  **Signal integrity excellente :** impedance continue, crosstalk minimisé, reflections maîtrisées pour conserver un eye opening suffisant et un BER conforme.

Pour un AI accelerator, un **low-loss RDL fan-out substrate** hautes performances est une lifeline entre HBM et compute core : de petites imperfections peuvent devenir un bottleneck système.

### Why is RDL Fan-Out Substrate Stackup Critical for Signal Integrity?

Dans la pratique PI, le stackup design est une décision critique dès le démarrage. Un mauvais **RDL fan-out substrate stackup** dégrade SI/PI à la racine et se corrige très difficilement plus tard :

-   **Controlled impedance :** dépend de la largeur, de la distance au reference plane (PWR/GND) et du Dk. Un stack stable est la base de **RDL fan-out substrate impedance control** ; variations de thickness/Dk créent mismatch et reflections.
-   **Return paths propres :** chaque trace high-speed doit disposer d’un reference plane continu (souvent GND) à proximité ; sinon la return current fait des détours, augmentant EMI et inductance.
-   **Crosstalk minimisé :** un bon **RDL fan-out substrate stackup** place des shields GND et contrôle le spacing.
-   **PDN low-impedance :** coupler étroitement PWR/GND crée de la plane capacitance et un chemin low-impedance pour le decoupling HF.

En résumé, **RDL fan-out substrate stackup** est la “constitution” du package : il définit le cadre de toutes les performances électriques.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
    <h3 style="text-align:center; color:#000000; border-bottom: 3px solid #64B5F6; padding-bottom: 10px;">Comparatif des matériaux diélectriques pour RDL substrates avancés</h3>
    <table style="width:100%; border-collapse: collapse; text-align:center; color:#000000;">
        <thead style="background-color:#F5F5F5; color:#000000;">
            <tr>
                <th style="padding:12px; border: 1px solid #ddd;">Matériau</th>
                <th style="padding:12px; border: 1px solid #ddd; border-bottom: 3px solid #FF7043;">Dk (@10GHz)</th>
                <th style="padding:12px; border: 1px solid #ddd; border-bottom: 3px solid #4CAF50;">Df (@10GHz)</th>
                <th style="padding:12px; border: 1px solid #ddd; border-bottom: 3px solid #AB47BC;">Thermal conductivity (W/m·K)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding:12px; border: 1px solid #ddd;">Époxy standard (FR-4)</td>
                <td style="padding:12px; border: 1px solid #ddd;">~4.2</td>
                <td style="padding:12px; border: 1px solid #ddd;">~0.020</td>
                <td style="padding:12px; border: 1px solid #ddd;">~0.3</td>
            </tr>
            <tr>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">Polyimide (Polyimide)</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~3.2</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.005</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.2</td>
            </tr>
            <tr>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">ABF (Ajinomoto Build-up Film)</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~2.8</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.002</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.5</td>
            </tr>
            <tr>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">mPPE (Modified Polyphenylene Ether)</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~2.6</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.0015</td>
                <td style="padding:12px; border: 1px solid #ddd; background-color: #E3F2FD;">~0.4</td>
            </tr>
        </tbody>
    </table>
    <p style="text-align:center; font-size:14px; color:#666; margin-top:15px;">Note : valeurs typiques ; la performance réelle dépend du grade et du process. Choisir le bon matériau low-loss est le premier pas vers un <strong>low-loss RDL fan-out substrate</strong> hautes performances.</p>
</div>

### How Does Material Selection Impact Loss and Performance?

Les matériaux sont la “génétique” du substrate. Pour **low-loss RDL fan-out substrate**, le choix du diélectrique et du copper est déterminant.

**Diélectrique :**
ABF et similaires offrent un avantage majeur sur Dk/Df vs FR-4.
-   **Low Dk :** propagation plus rapide et moins de delay. À impedance égale, permet des traces plus larges ou un diélectrique plus épais, réduisant les pertes et la sensibilité aux tolérances.
-   **Low Df :** détermine la part d’énergie convertie en chaleur. Pour des liens longs/high-frequency (Chiplet XSR/USR SerDes), low Df est clé. C’est aussi critique en [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

**Copper :**
Avec le skin effect, la roughness du copper devient un driver de loss.
-   **STD copper :** rugueux → plus de loss.
-   **VLP/HVLP :** très lisse → standard sur **low-loss RDL fan-out substrate**.

Les propriétés thermiques (k, CTE) impactent aussi thermal path et reliability. Un CTE plus proche du silicium réduit stress, warpage et risque de delamination.

### What are the Key Challenges in RDL Fan-Out Substrate Design?

**RDL fan-out substrate design** est un système complexe (électrique, thermique, mécanique, manufacturing).

1.  **Routing ultra-dense :** des dizaines/centaines de milliers d’I/O ; RDL à 2µm/2µm voire 1µm/1µm. Il faut une précision extrême et une planification des canaux pour éviter la congestion et respecter equal-length/diff constraints.
2.  **PI design :** construire un PDN low-impedance du BGA au pad ; optimiser decap placement, plans PWR/GND, et réduire la package inductance (last inch).
3.  **Thermal & stress mécanique :** TDP parfois >1000W. La chaleur doit traverser RDL, microvias et TIM. Le CTE mismatch (silicium/mold/substrate) génère warpage et peut dégrader BGA yield et long-term reliability—problèmes similaires à [HDI PCB](https://hilpcb.com/en/products/hdi-pcb), mais plus sévères.
4.  **DFM :** un optimum théorique n’est pas forcément manufacturable. Collaboration précoce avec la fab sur microvia min, registration, uniformité de plating, etc.

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin: 30px 0;">
    <h3 style="text-align:left; color:#FFFFFF; display: flex; align-items: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="28" height="28" style="margin-right: 10px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"></path></svg>Priorités clés en RDL Fan-Out Substrate design</h3>
    <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.8;">
        <li><strong>Warpage control = lifeline :</strong> CTE mismatch est l’ennemi #1. Stack symétrique, choix core et material matching sont indispensables.</li>
        <li><strong>Microvia reliability :</strong> aspect ratio, fill et plating déterminent la long-term reliability, surtout en thermal cycling.</li>
        <li><strong>PDN impedance targets :</strong> définir tôt une courbe cible et utiliser la simulation pour la stratégie decap et les plans.</li>
        <li><strong>Collaboration précoce avec la fab :</strong> DFM review en concept stage pour éviter des redesigns coûteux en fin de projet.</li>
    </ul>
</div>

### Achieving Precise RDL Fan-Out Substrate Impedance Control at Scale?

Pour PCIe 6.0 et HBM3e, les tolérances d’impedance atteignent ±7% voire ±5%. Obtenir un **RDL fan-out substrate impedance control** strict à l’échelle nécessite un contrôle coordonné :

-   **Etching précis :** uniformité de width sur des millions de traces.
-   **Épaisseur diélectrique uniforme :** contrôle strict en sequential build-up (SBU).
-   **Dk stable :** faible variation lot-à-lot.
-   **Inspection avancée :** TDR sur coupons pour piloter la consistence.

HILPCB utilise vacuum etching/lamination et SPC pour maintenir chaque **low-loss RDL fan-out substrate** dans la spec. Nos engineers aident aussi via simulation et tools d’impedance pour réduire le cycle de dev.

### Can RDL Fan-Out Substrate Cost Optimization Coexist with High Performance?

Oui, avec une stratégie claire. **Low-loss RDL fan-out substrate** est cher : matériaux avancés, process complexes (souvent 20+ steps), capex et exigences de yield. La **RDL fan-out substrate cost optimization** est possible en équilibrant :

1.  **Optimisation stackup :** réduire le nombre de couches RDL tout en tenant SI/PI (ex. 12 → 10 via routing plus efficace).
2.  **Matériaux gradués :** ultra low-loss seulement sur les nets critiques ; hybrid-material stackup ailleurs.
3.  **Panelization efficiency :** maximiser l’utilisation du panel en intégrant les contraintes dès le design.
4.  **Amélioration du yield :** levier #1 sur le coût : DFM robuste, contrôle process et test augmentent le yield.

Un partenaire expérimenté identifie ces leviers tôt et évite l’over-design.

<div style="background-color:#1A237E; color: white; padding: 20px; border-radius: 8px; margin: 30px 0;">
    <h3 style="text-align:center; color:#FFFFFF; border-bottom: 2px solid #00BCD4; padding-bottom: 10px;">Capacités de fabrication HILPCB (IC Substrate)</h3>
    <table style="width:100%; border-collapse: collapse; text-align:center; color:#FFFFFF;">
        <thead style="background-color:rgba(255,255,255,0.1); color:#FFFFFF;">
            <tr>
                <th style="padding:12px;">Paramètre</th>
                <th style="padding:12px;">Capacité</th>
                <th style="padding:12px;">Paramètre</th>
                <th style="padding:12px;">Capacité</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding:10px; border: 1px solid #4A55A2;">Max layers</td>
                <td style="padding:10px; border: 1px solid #4A55A2;">20+ Layers</td>
                <td style="padding:10px; border: 1px solid #4A55A2;">Min trace/space</td>
                <td style="padding:10px; border: 1px solid #4A55A2;">10µm / 10µm</td>
            </tr>
            <tr>
                <td style="padding:10px; border:  1px solid #4A55A2;">Min microvia</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">50µm (Laser Drill)</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">Max aspect ratio</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">12:1</td>
            </tr>
            <tr>
                <td style="padding:10px; border:  1px solid #4A55A2;">Impedance tolerance</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">±5%</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">Matériaux supportés</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">ABF, BT, mPPE, PI</td>
            </tr>
            <tr>
                <td style="padding:10px; border:  1px solid #4A55A2;">Surface finish</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">ENEPIG, Immersion Sn/Ag</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">Certifications</td>
                <td style="padding:10px; border:  1px solid #4A55A2;">ISO9001, IATF16949</td>
            </tr>
        </tbody>
    </table>
</div>

### How Does Manufacturing Affect Reliability and Turnaround?

Un **low-loss RDL fan-out substrate** n’a de valeur que s’il est manufacturable de façon fiable. Chaque détail du process impacte performance et long-term reliability :

-   **Microvia formation & fill :** précision laser, propreté des parois et qualité de plating/fill déterminent la reliability Z-axis. Voids/delamination peuvent échouer en thermal cycling.
-   **Registration en lamination :** avec 10+ couches, l’alignement doit être au niveau micron.
-   **Warpage control :** contrôle température/pression/temps + stack symétrique et low-stress materials.
-   **Test/inspection :** au-delà de AOI/flying probe, on exige souvent thermal shock, HAST et board-level drop tests.

Pour de nombreux projets AI, le time-to-market est critique. La capacité **RDL fan-out substrate quick turn** devient un indicateur clé : DFM review rapide, préparation outillage et réglages process. HILPCB, via MES digital et une équipe quick-turn, vise un **RDL fan-out substrate quick turn** leader pour accélérer validation et ramp.

### Partnering for Success in Your Next AI Substrate Project

Concevoir et fabriquer un **low-loss RDL fan-out substrate** est difficile et impose une collaboration fluide design/fab. Un partenaire fort en design et manufacturing réduit le risque et raccourcit le cycle.

Highleap PCB Factory (HILPCB) est plus qu’un fabricant : un technical solution provider. Avec plus de 10 ans sur [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb), nous comprenons les exigences AI/HPC. Nos atouts :

-   **Support end-to-end :** engagement amont sur **RDL fan-out substrate stackup**, matériaux et impedance planning.
-   **Manufacturing avancé :** production stable en fine trace/space et strict impedance control.
-   **Système qualité :** ISO9001 et IATF16949, tests et inspections complets.
-   **Service flexible :** quick-turn prototypes et volume production.

En résumé, **low-loss RDL fan-out substrate** est un enabler clé de l’AI next-gen. Les défis vont de la materials science au precision manufacturing. Si vous cherchez un partenaire fiable, contactez HILPCB : transformons vos innovations en produits réels.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Cet article analyse low-loss RDL fan-out substrate sous l’angle high-speed SI, thermal management et power/interconnect. En suivant la checklist et les process windows, et en impliquant tôt l’équipe DFM/DFA HILPCB, vous réduisez le risque et accélérez prototypes et production sans sacrifier qualité et compliance.


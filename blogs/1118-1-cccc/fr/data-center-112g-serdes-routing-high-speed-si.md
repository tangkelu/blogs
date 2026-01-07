---
title: "data-center 112G SerDes routing : Contraintes SI pour liens ultra‑rapides et low‑loss"
description: "Analyse de data-center 112G SerDes routing : budget de canal, matériaux, stack-up, Impedance Control, transitions via/connecteur, DFM et validation pour PCBs high-speed SI."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---
Avec la croissance explosive de l’AI, du ML et du cloud computing, le trafic des data centers augmente à un rythme inédit. Pour suivre, l’industrie migre rapidement de 56G NRZ/PAM4 vers 112G PAM4 SerDes. Ce saut n’est pas qu’un doublement de débit : il rend la SI beaucoup plus difficile. Une **data-center 112G SerDes routing** réussie devient du system engineering mêlant matériaux, électromagnétisme, thermique et precision manufacturing. Vu du côté measurement/compliance, cet article résume les difficultés clés et les réponses pratiques pour les canaux 112G.

Du BGA pad du package, aux traces et vias PCB, en passant par connecteurs/backplanes jusqu’au Rx, la performance du canal physique dicte la récupérabilité du 112G. Une petite discontinuité d’impédance, un dielectric loss trop élevé ou des vias non optimisées peuvent dégrader le budget et provoquer un BER catastrophique. Une stratégie **high-speed 112G SerDes routing** doit intégrer tôt matériaux, stack-up, Impedance Control et tolérances process.

### Pourquoi le budget canal 112G est-il si strict ?

Passer de 56G à 112G, ce n’est pas seulement doubler la fréquence. Pour 112G PAM4, Nyquist atteint 28 GHz : loss et noise deviennent critiques. Par rapport au NRZ, l’œil PAM4 est comprimé (1/3 en vertical) et la SNR margin chute. Le budget Insertion Loss (IL) devient donc une contrainte majeure de **data-center 112G SerDes routing**.

Un lien 112G long-reach (LR) typique peut être limité à ~30–35 dB @ 28GHz, réparti entre package, PCB, vias, connecteurs et Rx.

- **Insertion Loss (IL):** challenge principal ; FR-4 est trop loss à 28 GHz.
- **Return Loss (RL):** dû aux discontinuités (vias, connecteurs, BGA). Les réflexions créent de l’ISI.
- **Crosstalk:** la densité augmente NEXT/FEXT et réduit le SNR.
- **COM:** Channel Operating Margin agrège IL/RL/crosstalk et capacité Equalizer ; COM est devenu standard.

Il faut un modèle end‑to‑end précis en simulation et une collaboration étroite avec un fabricant expérimenté (ex. HILPCB).

### Choix des matériaux low‑loss : la base du 112G

Les matériaux posent la limite physique. À 28 GHz, Dk/Df gouvernent l’atténuation. Choisir des matériaux adaptés est la première étape pour **data-center 112G SerDes routing**.

- **Dk/Df:** pour 112G, on vise souvent Ultra Low Loss (Df < 0.004 @ 10GHz) : Tachyon 100G, Megtron 6/7/8, Rogers RO4000. La stabilité Dk est critique pour **112G SerDes routing impedance control**.
- **Skin Effect:** courant en surface → loss conducteurs.
- **Copper Roughness:** cuivre rugueux augmente loss ; préférer VLP/HVLP.
- **Fiber Weave Effect:** verre vs résine → variations Dk effectif, ripple d’impédance et skew ; Spread Glass et routage à 1–5°.

Le choix matériaux est aussi un trade‑off coût/DFM/supply ; un **112G SerDes routing guide** recommande un alignement early avec le fabricant.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Comparaison matériaux high-speed PCB</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Classe</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Matériaux typiques</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Df @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dk @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Débit</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standard loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Medium loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Impedance Control précis et discipline de routage

Impedance Control est le cœur de la SI. En **high-speed 112G SerDes routing**, toute dérive de l’impédance cible (souvent 90Ω/100Ω diff) augmente réflexions, jitter et ISI. Il faut du travail côté design et manufacturing.

**Design :** stack-up calculé (Polar Si9000), géométrie (match 1–2 mil, pas de 90°, reference planes continus).
**Manufacturing :** etching précis, lamination contrôlée, tests TDR sur coupons (ex. ±7%).

### Vias et transitions connecteur

Vias = discontinuités majeures :

- **Via Stub:** résonances et notches S21 ; **Back-drilling** pour stub 5–10 mil.
- **Optimisation via:** 3D EM (HFSS, CST) pour pad/antipad/barrel.
- **Footprint connecteur:** QSFP-DD/OSFP co‑optimisés ; Non-Circular Pad et clearances locales : techniques **112G SerDes routing layout**.

Microvias et blind/buried vias en [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) réduisent parasitiques et favorisent le high-density routing.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes PHY : règles vias et transitions</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Continuité d’impédance et suppression common-mode en PAM4</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Stub & Back-drill</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> full‑depth back-drill, stub **&lt;8 mil** pour pousser la première résonance au‑delà de 40GHz.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Antipad via 3D EM</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> co‑optimiser antipad et pads via <strong>3D full-wave EM</strong> pour tenir la variation diff dans **±5%**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Shadowing Vias</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> placer **2–4** vias de retour GND autour de chaque paire diff ; viser une isolation &lt; **-40dB**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. Breakout BGA & process</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Règle :</strong> pitch 0.8mm et moins : **VIPPO** recommandé ; dog-bone avec compensation de largeur sur segment court.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Note HILPCB :</strong> 112G dépend fortement de la <strong>Back-drill Tolerance</strong>. Confirmer Laser Back-drilling / T-Control pour éviter des notches inattendus.
</div>
</div>

### Points clés de layout pour 112G SerDes

- **Spacing/crosstalk:** règle 3W/5W, Guard Trace si nécessaire.
- **Stack-up:** Stripline interne privilégiée ; Microstrip plus sensible ; routage orthogonal entre layers adjacents.
- **Breakout BGA:** planifier vias/layers sans fragmenter les reference planes ; un **112G SerDes routing guide** est important.
- **PI:** PDN noise → jitter ; decoupling et simulation d’impédance PDN.

### Equalization & jitter: co‑design chip‑channel

- **Tx EQ:** FFE, Pre-emphasis/De-emphasis.
- **Rx EQ:** CTLE et DFE (puissant mais sensible aux erreurs).

Objectif : un channel “bien comporté” pour éviter de sur‑dépendre de l’equalization. Utiliser IBIS-AMI pour co‑optimiser channel et equalizer et maximiser COM margin.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4 : rapport de sign-off simulation</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">Résumé COM</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">IL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">COM</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ILD</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Ripple: good</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ERL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Compliant</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
💡 <strong>Note :</strong> IL = -32dB, marge restante 3dB avant -35dB. Faire un Monte Carlo sur la <strong>HVLP copper roughness</strong> avant la production.
</div>
</div>

### Du prototype à la production : DFM

- **Tolérances:** intégrer variations et faire du Monte Carlo.
- **Surface finish:** ENIG vs ENEPIG, vigilance “black pad”.
- **DFM check:** Gerber/ODB++ avant release.

### Tests & validation

VNA (Sdd21/Sdd11), TDR, Eye Diagram et BER (BER < 1E-6).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

La **data-center 112G SerDes routing** exige une approche end‑to‑end : matériaux ultra low‑loss, stack-up et Impedance Control, optimisation vias/connecteurs, et DFM en priorité. Traiter le channel comme un système unique, simuler tôt (EM + IBIS-AMI) et valider par measurement/compliance est la voie pour équilibrer performance/coût/fiabilité. Un partenaire comme HILPCB aide à industrialiser rapidement et de manière fiable les designs 112G et au‑delà.


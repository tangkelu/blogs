# P4-210A 2026-05-06 EMC Source Lane: Capacitor Role / Parasitic / Resonance Boundary

Date: 2026-05-06

Status: `completed_at_claim_family_level`

## Purpose

Extract the narrowest reusable claim inventory from the EMC handbook for capacitor role naming, capacitor parasitics, self-resonance, and parallel-resonance boundary language.

This lane remains `source-first` and `conservative`:

- the handbook is treated as claim inventory, not authority
- no handbook numeric, value recipe, compliance implication, or universal effectiveness statement is promoted
- the output is a demand map for later official-source recovery, not a fact-layer upgrade

## Inputs Used

Primary controller context:

- `llm_wiki/logs/p4-209-2026-5-6-emc-handbook-controller-note.md`
- `llm_wiki/logs/p4-209a-2026-5-6-emc-handbook-lane-layout-filter-ground.md`

Primary handbook extraction root:

- `tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/`

## Exact Input Slice

Tightest text slice for this lane:

- `pages/page-0023.txt`
  - capacitor role taxonomy
  - equivalent-circuit framing
  - self-resonance setup
- `pages/page-0024.txt`
  - single-capacitor frequency-response figure reference
  - parallel-capacitor antiresonance setup
- `pages/page-0025.txt`
  - antiresonance narrative
  - ESR influence narrative
- `pages/page-0026.txt`
  - ESL influence narrative
  - selection framing setup
- `pages/page-0027.txt`
  - insertion-loss comparison claim inventory
  - decoupling / bypass design suggestions
- `pages/page-0028.txt`
  - multi-capacitor range / pairing suggestions
  - storage-capacitor split from decoupling
- `pages/page-0029.txt`
  - storage-capacitor distribution figure only

Relevant figure/table-bearing pages identified in the extraction manifest:

- page `23`
  - `images/ee651ce708f34162.png`
  - `images/616ec0450c1dddd9.png`
- page `24`
  - `images/f03ebfe2a83bd871.png`
  - `images/540ccff5a80d231f.png`
- page `25`
  - `images/046ab5539d3ae95e.png`
- page `26`
  - `images/b904ebfcc1fcf680.png`
  - `images/606f1b70c24f6bb3.png`
- page `27`
  - `images/f4251a4931d0dd24.png`
- page `28`
  - `images/465f6624b2e3d8b5.png`
- page `29`
  - `images/7b9993ccc8aaa42b.jpeg`

## Smallest Neutral Claim Families

### 1. Capacitor role vocabulary

Smallest safe reusable family from the handbook text:

- capacitor roles are being separated by function, not by a single interchangeable label
- the text distinguishes:
  - `decoupling`
  - `bypass`
  - `bulk` / `storage`
- storage-capacitor discussion is a separate subfamily from decoupling / bypass discussion

What stays blocked at this stage:

- any claim that these role definitions are canonical across vendors or standards
- any value ladder, quantity rule, or guaranteed outcome attached to those role labels

### 2. Non-ideal capacitor model vocabulary

Smallest safe reusable family:

- EMC filter-capacitor discussion must treat real capacitors as non-ideal
- the handbook frames the practical part with capacitance plus series parasitic terms
- `ESR` and `ESL` are explicit boundary vocabulary for later source recovery

What stays blocked:

- handbook-derived parasitic magnitudes
- any package-specific parasitic default
- any statement that one package or dielectric is universally better without owner data

### 3. Self-resonance boundary

Smallest safe reusable family:

- a practical filter capacitor has a self-resonant region
- the useful impedance behavior of a capacitor changes around that self-resonant region
- capacitor selection for filtering / bypass work must account for frequency-dependent behavior rather than ideal-capacitor assumptions

What stays blocked:

- handbook self-resonance formulas
- handbook frequency cutoffs
- any claim that a capacitor behaves as a universal low-pass element over all relevant frequencies

### 4. Parallel-capacitor antiresonance boundary

Smallest safe reusable family:

- combining capacitors can create an antiresonant impedance peak rather than uniformly lowering impedance everywhere
- antiresonance risk belongs in the same boundary family as capacitor-combination planning
- multi-capacitor selection needs frequency-range reasoning, not only more capacitance

What stays blocked:

- the handbook's plotted peak locations
- the handbook's specific capacitor-pair recipes
- any direct reuse of its pair-ratio guidance as a universal rule

### 5. ESR / ESL effect vocabulary

Smallest safe reusable family:

- `ESR` affects the shape and height of the combined impedance response
- `ESL` affects resonance / antiresonance location and high-frequency usefulness
- package / structure differences are part of the ESL discussion family

What stays blocked:

- table values in `表3-1`
- direct reuse of any package ranking without current datasheet support
- any blanket statement that lower `ESR` or lower `ESL` is always globally optimal

### 6. Placement and local-use posture

Smallest safe reusable family:

- decoupling guidance is being tied to local placement near IC power pins
- bypass guidance is being tied to short local return paths and parasitic control
- storage capacitors are being framed as a different placement / distribution problem from per-pin decoupling

What stays blocked:

- minimum counts per IC
- handbook plane-split usage suggestions as reusable defaults
- value-ratio or quantity rules for broad reuse

## Blocked Claims And Numerics

The following remain explicitly blocked from promotion out of this handbook lane:

- `~5 nH` mounted multilayer-capacitor parasitic inductance
- `~30 mOhm` lead resistance
- all handbook self-resonance and antiresonance frequencies
- the `15 MHz to 175 MHz` impedance-peak narrative
- the `150 MHz` peak reference
- `ESR / n` style derived statements as reusable fact-layer guidance
- `22 nF` example and its cited usable frequency range
- any `0.01 uF` versus `0.1 uF` frequency superiority rule copied from the handbook
- the `>50 MHz` board-frequency recommendation
- the `2:1` capacitor-pairing rule as a general design rule
- all explicit capacitance values for storage-capacitor placement such as `1 uF`, `10 uF`, `22 uF`, `33 uF`
- all board-level quantity rules such as `1-4` capacitors around a device
- dielectric-family acceptability claims such as `X7R`, `Y5V`, `Z5U` being broadly suitable
- any implication that the handbook figures or examples prove EMC compliance, adequate decoupling, or production readiness

## Recovery Priorities: Next Authoritative Source Classes

Recover authority by source class, not by copying handbook figures.

### 1. Semiconductor vendor decoupling / PDN guidance

Needed to recover:

- decoupling versus bypass role boundaries
- near-pin placement posture
- frequency-range planning language for local power integrity

Likely source classes:

- IC vendor hardware design guides
- FPGA / MCU / CPU power-distribution application notes
- mixed-signal layout guidance from major semiconductor vendors

### 2. Capacitor manufacturer technical notes and datasheets

Needed to recover:

- self-resonance vocabulary
- ESR / ESL vocabulary
- package- and value-dependent behavior boundaries

Likely source classes:

- Murata / TDK / KEMET / AVX / KYOCERA AVX application notes
- current MLCC / tantalum datasheets with impedance-frequency plots

### 3. PDN / SI educational authority from major EDA or component vendors

Needed to recover:

- antiresonance explanation
- multi-capacitor combination boundaries
- caution against simplistic value-stacking rules

Likely source classes:

- Cadence, Keysight, Siemens EDA, or Altium technical guidance
- owner-authored SI / PDN notes from recognized vendor ecosystems

### 4. Standards-adjacent authority only if actually necessary

Potentially relevant later, but not first:

- IEC / IEEE / IPC references if a future lane needs controlled terminology or measurement framing

Do not use this class first for cookbook decoupling recipes; vendor-owner guidance is the better recovery path.

## Selective Vision Candidates

Selective vision is only justified where the extracted text clearly points to figure-dependent impedance behavior:

- page `23`
  - `图3-9` equivalent-circuit framing
  - `图3-10` single-capacitor frequency-response framing
- page `24`
  - `图3-11` parallel-capacitor equivalent model
- page `25`
  - `图3-12` antiresonance response figure
- page `26`
  - `表3-1` package / ESL table, if later source comparison requires image verification only
- page `27`
  - `图3-13` insertion-loss comparison
  - `图3-14` placement example
- page `28`
  - `图3-15` multi-capacitor pairing example
- page `29`
  - `图14` storage-capacitor distribution example

Vision is not needed to promote facts now. It is only a later support tool for figure interpretation after authoritative recovery begins.

## Lane Outcome

This lane successfully isolates a conservative capacitor-role / parasitic / resonance claim inventory from the handbook, but it does not produce new reusable facts on its own.

Final status: `completed_at_claim_family_level`; next valid move is narrow authoritative recovery from semiconductor-vendor decoupling guidance and capacitor-manufacturer parasitic / resonance documentation.

Date: 2026-05-01
Lane: `P4-87b satellite standards / outgassing / Class 3A authority recovery scout`
Input: `/code/blogs/tmps/2026.4.29/en/satellite-pcb.md`
Workspace checked: `/code/blogs/llm_wiki`
Output: `/code/blogs/llm_wiki/logs/p4-87b-satellite-space-material-outgassing-authority-scout.md`
Scope status: `completed_at_claim_family_level`
Evidence status: `source_backed_fact_layer_partial`

# Purpose

This scout log treats `satellite-pcb.md` as claim inventory only, checks which exact-noun authority anchors already exist inside `llm_wiki`, and records what can be safely reused versus what remains blocked pending new official sources.

This lane does not add facts, wiki pages, source records, or tracker updates. It preserves a deletion-safe map for the next integration pass.

# Draft Focus Observed

The draft repeatedly depends on these authority-sensitive noun families:

- `ASTM E595`
- NASA outgassing screening context
- `IPC-6012 Class 3/A`
- `IPC-6012FS` versus legacy `IPC-6012ES`
- `GSFC-STD-7000`
- `ECSS-E-ST-10-03`
- `Parylene C`
- `Parylene HT`
- `IPC-CC-830 Type AR`
- `QML`
- `LEO`, `CubeSat`, `GEO`, `NewSpace`, constellation, and `space-grade` readiness language

# Existing `llm_wiki` Support Checked

## Directly reusable authority set

- `facts/standards/high-reliability-program-and-outgassing-metadata.md`
  Use: guarded hi-rel program vocabulary, `ASTM E595` method identity, NASA outgassing database context, and `QML/QPL` separation.

- `facts/standards/22-layer-outgassing-and-screening-acceptance-boundary.md`
  Use: keeps `TML`, `CVCM`, and outgassing wording in method or screening context rather than universal acceptance proof.

- `facts/standards/ipc-6012-addendum-program-metadata.md`
  Use: current `IPC-6012FS` identity, procurement-triggered addendum framing, and `IPC-6012FS` superseding `IPC-6012ES`.

- `facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`
  Use: keeps `Class 3`, `Class 3A`, and addendum vocabulary at hierarchy/context level rather than free threshold tables.

- `facts/standards/22-layer-qualification-listing-and-release-authority-boundary.md`
  Use: blocks `QML`, listing, certification, and release-authority inflation.

- `facts/standards/fai-and-aerospace-quality-workflow-metadata.md`
  Use: guarded aerospace documentation, FAI, audit, and quality-workflow vocabulary without supplier-execution proof.

- `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`
  Use: keeps aerospace/program readiness language separate from PCB readiness proof.

- `sources/registry/standards/astm-e595-15r21-page.md`
  Use: strongest current local anchor for `ASTM E595` identity.

- `sources/registry/methods/nasa-vacuum-outgassing-database-page.md`
  Use: NASA database existence and `ASTM E595` linkage.

- `sources/registry/methods/nasa-outgassing-user-guide-page.md`
  Use: historical screening-threshold context for `TML 1.0%` and `CVCM 0.10%`.

- `sources/registry/standards/ipc-6012fs-space-military-addendum-page.md`
  Use: current `IPC-6012FS` identity and high-level space/military scope.

- `sources/registry/standards/ipc-6012fs-toc.md`
  Use: clause-family visibility only.

- `sources/registry/standards/ipc-cc-830c-toc.md`
  Use: generic `IPC-CC-830C` identity only.

## Adjacent but not exact replacement support

- `sources/registry/standards/ecss-q-st-70-12c-rev1-pcb-design-standard.md`
  Use: ECSS space PCB design-rule and definition context.
  Limit: this is not `ECSS-E-ST-10-03`, so it cannot stand in for ESA verification/test-environment claims from the draft.

# Safe Reuse Classes

## 1. `ASTM E595` and NASA outgassing

Safe reuse:

- `ASTM E595` as an outgassing test-method identity
- NASA outgassing database existence and screening context
- guarded wording that `TML` / `CVCM` values belong to screening/database presentation context
- guarded wording that materials, coatings, masks, adhesives, and inks may be evaluated within program-specific outgassing workflows

Not unlocked:

- draft numeric claims about specific material pass/fail results
- supplier `qualified materials list` claims
- schedule reduction, testing duration savings, or qualification-package claims
- whole-board or mission approval conclusions from `ASTM E595` alone

## 2. `IPC-6012FS` and `Class 3/A` normalization

Safe reuse:

- `IPC-6012FS` is the current public space/military avionics addendum anchor in this corpus
- `IPC-6012FS` is the right normalization path when the draft says `Class 3/A` in a space/military rigid-board context
- guarded wording that the addendum is procurement-triggered and modifies or adds exceptions relative to the base rigid-board specification
- guarded wording that `IPC-6012ES` is legacy relative to the current `IPC-6012FS` branch

Not unlocked:

- via-plating minima, cleanliness limits, microsection frequencies, thermal-shock counts, or any other `Class 3/A` numeric thresholds
- claims that a supplier fabricates to `Class 3/A` or is approved under `IPC-6012FS`
- translating public TOC or product-page metadata into clause-level acceptance requirements

## 3. Aerospace quality and qualification governance

Safe reuse:

- `QML`, `QPL`, qualification, listing, certification, and release authority are separate governance layers
- aerospace documentation and FAI vocabulary can be used as workflow context only
- guarded wording that program-specific procurement or customer flowdown governs applicability

Not unlocked:

- `NASA-qualified PCB`
- supplier `QML` status for laminates, coatings, or finished boards
- flight qualification, heritage, approval, or release-authority claims

# Blocked Claim Families From The Draft

These draft classes remain blocked even after local reuse:

- radiation, thermal-cycle, vibration, and shock numerics
- `LEO`, `CubeSat`, `GEO`, `NewSpace`, or constellation readiness claims presented as supplier capability proof
- lead-time, price, quantity, yield, scale, or commercial-economics claims
- `64 layers`, copper-coin thermal-resistance, and other capability numerics without dated capability evidence
- exact `Class 3/A` thresholds or acceptance tables
- `QML` material-list ownership or qualification status
- `space-grade`, `flight-qualified`, `NASA-qualified`, `radiation-tolerant laminate`, or heritage claims
- coating-performance numerics and comparative claims for `Parylene C`, `Parylene HT`, or acrylic systems

# Source Gaps Still Open

## Highest-value exact-noun gaps

- `GSFC-STD-7000`
  Missing: official local source record for NASA general environmental verification/test framing.
  Impact: draft launch vibration/shock references remain unsupported.

- `ECSS-E-ST-10-03`
  Missing: official local source record for ESA system-engineering verification/test framing.
  Impact: ESA-side vibration/test references remain unsupported.

- `Parylene C`
  Missing: owner or primary technical source record strong enough for conservative identity-only reuse.
  Impact: draft claims about deposition behavior, anti-whisker effect, corona behavior, and outgassing numbers remain blocked.

- `Parylene HT`
  Missing: owner or primary technical source record strong enough for conservative identity-only reuse.
  Impact: draft high-temperature and UV-stability language remains blocked.

- `IPC-CC-830 Type AR`
  Missing: exact public anchor for `Type AR` subtype identity.
  Impact: local `IPC-CC-830C` TOC is too generic to recover subtype-specific claims.

## Secondary normalization gap

- dedicated local fact card for `space material / outgassing / Class 3A` aggregation
  Current state: reusable pieces exist, but they are split across hi-rel and `22-layer` boundary cards.
  Impact: retrieval for `satellite-pcb.md` remains fragmented even though much of the safe authority is already present.

# Recommended Minimal Next Integration Scope

If this lane is picked for mainline integration, the safest smallest follow-on is:

- candidate fact path:
  `llm_wiki/facts/standards/space-material-outgassing-and-class-3a-metadata-boundary.md`

- minimal safe scope:
  aggregate `ASTM E595`, NASA outgassing database/user-guide context, `IPC-6012FS` normalization, and `Class 3/A` hierarchy boundaries

- explicit exclusions:
  `GSFC-STD-7000` and `ECSS-E-ST-10-03` numerics, `Parylene C/HT` performance claims, `Type AR` subtype claims, supplier capability proof, and all program-readiness/commercial claims until exact official sources are added

# Lane Status

- Lane result: `scouted`
- Best current reuse class: `space-material / outgassing / class-3a metadata boundary`
- Integration readiness: `partial`
- Why partial:
  the outgassing and `IPC-6012FS` side is already strong enough for a narrow identity/boundary card, but launch-environment standards and coating exact nouns still have direct source gaps

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-87b-satellite-space-material-outgassing-authority-scout.md`

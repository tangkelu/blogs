# P4-60B 2025-11-10 Ohm's Law Institutional Authority Scout

Date: 2026-04-30
Scope lane: `institutional electrical fundamentals formula recovery` for `/code/blogs/tmps/2025.11.10/en/ohms-law.md`
Edit boundary honored: only this file was created

## Purpose

- Treat `/code/blogs/tmps/2025.11.10/en/ohms-law.md` as claim inventory only, not authority.
- Recover the narrowest institution-grade source pack that can safely unlock `Ohm's law` at `source_backed_fact_layer_partial`.
- Keep scope narrow to SI / unit identity and the minimal formula identity / variable relationship only.
- Keep historical framing, derivations, worked examples, I-V teaching, ohmic / non-ohmic taxonomy, power-law expansions, AC impedance, and PCB consequence claims blocked.

## Exact Files Reviewed

### Draft claim inventory

- `/code/blogs/tmps/2025.11.10/en/ohms-law.md`

### Relevant existing `llm_wiki` context

- `/code/blogs/llm_wiki/logs/p4-58b-2025-11-10-formula-pedagogy-authority-scout.md`
- `/code/blogs/llm_wiki/logs/p4-59a-2025-11-10-formula-split-and-local-coverage-prep.md`
- `/code/blogs/llm_wiki/logs/backlog.md`

## Exact Sources Checked

### Selected for the conservative source pack

1. NIST, `SI Units – Electric Current`
   - URL: https://www.nist.gov/pml/owm/si-units-electric-current
   - Explicit support:
     - the SI unit of electric potential difference is the volt (`V`)
     - `1 V = 1 W/A`
     - the SI unit of electric resistance is the ohm (`Ω`)
     - `1 Ω = 1 V/A`
   - Safe use:
     - SI unit names, symbols, and unit-expression identity only
   - Not safe by itself:
     - using the unit expressions alone to claim `I = V/R` or `V = IR` as an explicit law statement; that would be inference if this were the only source

2. OpenStax, `College Physics 2e, 20.2 Ohm's Law: Resistance and Simple Circuits`
   - URL: https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits
   - Explicit support:
     - current through most substances is directly proportional to applied voltage
     - current is inversely proportional to resistance
     - combining those relationships gives `I = V/R`
     - resistance unit identity `1 Ω = 1 V/A`
     - `Ω` is the symbol for ohm
   - Safe use:
     - minimal Ohm's-law relationship and variable roles only
   - Not safe by itself:
     - expanding into broader simple-circuit pedagogy, worked examples, temperature behavior, or ohmic-material teaching as reusable fact-layer coverage

### Checked but not adopted for the narrowest pack

3. NIST, `Ampere: The Present`
   - URL: https://www.nist.gov/si-redefinition/ampere-present
   - Why checked:
     - it explicitly states `I = V/R`
   - Why not adopted:
     - it is a broader metrology / history page and is not the narrowest fit for this lane

4. OpenStax, `Physics, 19.1 Ohm's law`
   - URL: https://openstax.org/books/physics/pages/19-1-ohms-law
   - Why checked:
     - it explicitly states the law and unit relationship
   - Why not adopted:
     - it expands further into current fundamentals, worked examples, and ohmic / non-ohmic teaching than needed for this minimal recovery lane

## Conservative Unlock Boundary

With the two-source pack above, the lane can safely unlock only the following:

- `volt`, `ampere`, and `ohm` as unit identities with symbols `V`, `A`, and `Ω`
- explicit unit identity for resistance:
  - `1 Ω = 1 V/A`
- minimal Ohm's-law variable relationship:
  - current is directly proportional to applied voltage
  - current is inversely proportional to resistance
  - explicit source form from OpenStax: `I = V/R`

## Explicit vs Inferred Formula Status

- Explicit in source:
  - `I = V/R` is explicit in the adopted OpenStax source
  - `1 Ω = 1 V/A` is explicit in both the adopted NIST and OpenStax sources
- Inference / algebraic rearrangement, not separately explicit in the adopted pack:
  - `V = IR`
  - `R = V/I`
- Practical consequence:
  - if a later fact card or wiki line uses `V = IR`, it should be labeled as an algebraic rearrangement of the explicit sourced relationship unless a later source pack intentionally adds a page that prints `V = IR` directly

## Blocked Claims That Remain Blocked

- Georg Simon Ohm historical-origin framing, publication year, and biography claims
- water-flow or pressure analogies presented as authoritative teaching
- derivation-heavy teaching and stepwise calculator-style instruction
- worked examples, tables, and problem-solving walkthroughs
- ohmic vs non-ohmic taxonomy, device examples, and temperature-behavior teaching
- I-V curve interpretation, slope teaching, and graph-based explanations
- power-law expansions such as `P = VI`, `P = I^2R`, and `P = V^2/R`
- AC extensions such as reactance, impedance, or `V = IZ`
- any PCB consequence claims involving trace width, copper weight, current capacity, connector rating, heating, voltage drop budgets, or manufacturability

## Residual Gaps

- no adopted source in this pass that explicitly prints the classroom form `V = IR`; current support stops at the explicit `I = V/R` form plus unit identities
- no official / institutional source pack yet for power formulas or watts-to-amps conversion teaching
- no separate standards or institutional lane yet for PCB current-carrying, thermal, or layout consequences
- no source adopted here for historical context, derivations, analogies, or worked-example pedagogy

## Promotion Judgment

Judgment: `promotable_to_source_backed_fact_layer_partial_with_strict_boundary`

That promotion is safe only if the downstream fact layer stays inside this narrow envelope:

- SI unit identity for `V`, `A`, and `Ω`
- explicit resistance unit expression `1 Ω = 1 V/A`
- minimal Ohm's-law relationship in the explicit sourced form `I = V/R`, or clearly labeled algebraic rearrangements of that relationship

Everything else in the current draft remains blocked pending a separate source-recovery lane.

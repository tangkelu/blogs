---
fact_id: "methods-rf-transmission-line-structure-vocabulary-boundary"
title: "Public IPC metadata plus existing RF source layers support microstrip and stripline as high-frequency printed-board structure vocabulary, but not broad CPW performance claims"
topic: "RF transmission-line structure vocabulary boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "ipc-6018d-toc"
  - "ipc-4103b-toc"
  - "smiths-interconnect-microstrip-isolator-circulator-anatomy"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
tags: ["rf", "high-frequency", "microstrip", "stripline", "cpw", "transmission-line", "structure-boundary", "stackup"]
---

# Canonical Summary

> The current source layer is strong enough to support a conservative RF structure-vocabulary boundary: `microstrip` and `stripline` are legitimate transmission-line and construction-family terms inside high-frequency printed-board scope, while exact geometry rules, impedance formulas, isolation outcomes, and broad `CPW` superiority claims remain unsupported or source-sensitive.

## Stable Facts

- Public `IPC-6018D` TOC metadata supports high-frequency printed-board scope and construction-family vocabulary that includes `microstrip` and `stripline`.
- Public `IPC-4103B` TOC metadata supports high-speed / high-frequency base-material scope that explicitly includes printed boards used in `microstrip`, `stripline`, and high-speed digital circuits.
- The current internal APT high-frequency and microwave pages consistently place `microstrip` and `stripline` inside stackup, impedance, and RF-execution context rather than as free-floating marketing terms.
- The current source layer is therefore strong enough to support a guarded structure-vocabulary split:
  `microstrip` commonly belongs to exposed outer-layer RF / high-frequency transmission-line context, while `stripline` belongs to buried internal-layer transmission-line context inside multilayer planning.
- Existing RF validation and transition-control layers reinforce that transmission-line naming, via / launch control, and measurement / verification are related but not interchangeable evidence classes.
- The Smiths Interconnect article is only narrow support for high-level `microstrip` vocabulary in RF component context; it is not a neutral design-rule source for board-wide geometry or performance claims.

## Conditions And Methods

- Use this card when drafts need a conservative explanation of `microstrip` and `stripline` as RF / high-frequency printed-board structure vocabulary.
- Keep `structure naming`, `stackup position`, `transition control`, and `measurement / validation` as separate layers.
- Safe `microstrip` posture:
  describe it as an outer-layer transmission-line structure family used in RF / high-frequency board context.
- Safe `stripline` posture:
  describe it as an internal-layer transmission-line structure family inside multilayer high-frequency board context.
- Pair this card with `standards-high-frequency-printed-board-and-material-boundary`, `methods-pcb-impedance-and-rf-measurement-method-boundary`, and `processes-rf-drilling-and-transition-control` when the prompt also needs standards scope, verification vocabulary, or via-transition context.

## Limits And Non-Claims

- This card does not authorize impedance formulas, field-solver equations, quarter-wave derivations, or geometry tables.
- It does not authorize exact width, thickness, spacing, or tolerance examples for `50 ohm`, `75 ohm`, `90 ohm`, or `100 ohm` structures.
- It does not authorize generic isolation, radiation-loss, insertion-loss, or mmWave-superiority claims for `microstrip`, `stripline`, or `CPW`.
- It does not authorize broad `CPW` claims because the current reusable source layer for `CPW` is materially weaker and still draft-heavy.
- It does not prove supplier capability, manufacturing precision, TDR coverage, VNA scope, or finished-board RF performance.

## Open Questions

- Add a dedicated official or public source lane for `CPW` before promoting any reusable `coplanar waveguide` fact card.
- Add stronger external structure references if a future pass needs guarded topology comparison beyond layer-position vocabulary.

## Source Links

- https://www.ipc.org/TOC/IPC-6018D_TOC.pdf
- https://www.ipc.org/TOC/IPC-4103B.pdf
- https://www.smithsinterconnect.com/smiths-interconnect-blog/the-anatomy-of-a-microstrip-isolator-and-circulator/
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json

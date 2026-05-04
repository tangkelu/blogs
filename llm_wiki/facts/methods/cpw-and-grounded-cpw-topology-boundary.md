---
fact_id: "methods-cpw-and-grounded-cpw-topology-boundary"
title: "CPW and grounded CPW now have guarded structure identity, not performance authority"
topic: "CPW and grounded CPW topology boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "ansys-coplanar-waveguide-driven-terminal"
  - "ansys-coplanar-waveguide-with-ground-driven-terminal"
  - "cadence-rf-pcb-design-guidelines"
  - "frontendapt-pcb-impedance-control-page-en"
tags: ["rf", "cpw", "grounded-cpw", "coplanar-waveguide", "transmission-line", "structure-boundary"]
---

# Canonical Summary

> Current official/public sources are strong enough to support a conservative `CPW` boundary: `CPW` is a real RF transmission-line structure with a center signal conductor and coplanar side grounds, and `grounded CPW` exists as a distinct variant with an added ground-plane context. These sources do not support generic `CPW` superiority, probing-readiness, `MMIC`-fit, via-fence, or supplier-capability claims.

## Stable Facts

- Ansys' current HFSS help defines `CPW` as a structure with a signal trace between two coplanar ground conductors.
- The same Ansys help page states that signal width and gap to the side grounds affect characteristic impedance.
- Ansys' current grounded-CPW help page shows that `coplanar waveguide with ground plane` exists as a distinct transmission-line variant.
- Cadence's current RF PCB article groups `coplanar waveguides`, `striplines`, and `microstrips` as common RF trace families.
- The current internal APT impedance-control page already names `coplanar` among impedance-structure families, which is useful as adjacent local context but not enough by itself for reusable publication.

## Conditions And Methods

- Use this card only for guarded structure-identity wording such as:
  `CPW is a coplanar transmission-line family`, `the center conductor is flanked by side grounds`, and `grounded CPW is a distinct variant`.
- Keep `structure identity`, `impedance calculation`, `via / fence execution`, `probing`, and `finished-board RF performance` as separate evidence classes.
- Pair this card with RF validation, transition-control, and standards-scope layers when a prompt needs broader execution context.

## Limits And Non-Claims

- This card does not authorize exact geometry examples, impedance formulas, or target-ohm recipes.
- It does not authorize `CPW is best for mmWave`, `best for probing`, `best for MMIC`, or similar ranking language.
- It does not authorize generic via-fence, parasitic-mode suppression, launch optimization, or fabrication-tolerance claims.
- It does not prove supplier capability, TDR coverage, VNA scope, or finished-board RF behavior.

## Open Questions

- Add a stronger primary source if future drafts need guarded via-fence or grounded-return wording beyond basic grounded-CPW existence.
- Add a separate source lane if any publication truly needs probing, package-transition, or `MMIC` integration language.

## Source Links

- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v251/en/Subsystems/HFSS/Content/GettingStarted/CoPlanarWaveguideDrivenTerminal.htm
- https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v242/en/Subsystems/HFSS/Content/GettingStarted/CoplanarWaveguidewithGroundDrivenTerminal.htm
- https://resources.pcb.cadence.com/home/2023-rf-pcb-design-guidelines
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json

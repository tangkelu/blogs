---
fact_id: "standards-schematic-symbol-standards-identity-boundary"
title: "IEC 60617 and IEEE/ANSI 315 support schematic-symbol standards identity, not universal pedagogy or CAD-tool recommendations"
topic: "Schematic symbol standards identity boundary"
category: "standards"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "iec-60617-database-page"
  - "ieee-ansi-315-1975-standard-page"
tags: ["schematic-symbols", "iec-60617", "ieee-315", "ansi-y32-2", "graphical-symbols", "reference-designators", "standards-boundary"]
---

# Canonical Summary

> Official IEC and IEEE SA metadata are strong enough to support a conservative standards-identity layer for schematic-symbol writing: `IEC 60617` is the IEC-owned graphical-symbol database for electrotechnical diagrams, and `IEEE/ANSI 315-1975` is a historical U.S. graphic-symbol and reference-designation standard page with inactive-reserved status. These sources do not justify universal reading conventions, exact symbol-shape instruction, or recommendations for one CAD workflow over another.

## Stable Facts

- IEC describes `IEC 60617` as a database of graphical symbols for use in electrotechnical diagrams and states that the database is the official source of `IEC 60617`.
- The IEC page states that the database incorporates parts 2 to 13 and covers broad symbol domains such as conductors, passive components, semiconductors, energy conversion, controlgear, measuring instruments, telecommunications equipment, and diagram-planning views.
- IEEE SA describes `IEEE/ANSI 315-1975` as an IEEE standard for graphic symbols for electrical and electronics diagrams, including reference designation letters.
- The IEEE SA page provides lifecycle metadata showing that `IEEE/ANSI 315-1975` is `Inactive-Reserved`, with ANSI approval in 1975, publication in 1975, reaffirmation in 1993, and inactivation in 2019.
- The IEEE SA page states that the standard was designed around graphic symbols and class designation letters for use on electrical and electronics diagrams and sought compatibility with IEC recommendations.
- Together, these sources support a safe standards-family identity layer:
  `IEC 60617` as the IEC-owned symbol database and `IEEE/ANSI 315-1975` as a historical U.S.-side diagram-symbol standard reference.

## Conditions And Methods

- Use this card for `schematic-symbols.md` only when the article needs standards identity and document-family framing.
- Safe `IEC 60617` posture:
  describe it as the IEC-owned database for graphical symbols used in electrotechnical diagrams.
- Safe `IEEE/ANSI 315-1975` posture:
  describe it as a historical IEEE/ANSI standard page for graphic symbols and reference designation letters, and note its inactive-reserved status when relevant.
- Keep standards identity separate from tutorial claims about how every engineer should read or draw schematics.
- Pair this card with narrower tool-owner or educational sources only if a future pass needs CAD workflow, library-management, or beginner-instruction claims.

## Limits And Non-Claims

- This card does not authorize exact symbol meanings, shapes, stroke rules, or category-by-category symbol definitions.
- It does not authorize claims that `IEC 60617` and `IEEE 315` are fully interchangeable in every symbol set.
- It does not authorize universal reading conventions such as one mandatory left-to-right, top-to-bottom, or power-at-top rule.
- It does not authorize CAD-tool recommendations, library-completeness claims, ERC/DRC advice, or schematic-layout best practices.
- It does not authorize `current U.S. active standard` wording for `IEEE/ANSI 315-1975`.

## Open Questions

- Add a narrower official or institutional source only if future drafts need public instruction on reference designators, symbol-library governance, or pedagogy.
- Add tool-owner sources only if future drafts need bounded feature identity for schematic-capture software.

## Source Links

- https://webstore.iec.ch/en/publication/2723
- https://standards.ieee.org/ieee/315/515/

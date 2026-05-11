---
fact_id: "methods-zero-ohm-jumper-resistor-identity-boundary"
title: "Zero-ohm chip resistors are reusable only as jumper-class identity plus low-but-nonzero practical resistance boundary"
topic: "zero-ohm jumper resistor identity boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-09"
exact_data_class: "boundary_convention"
scope_type: "manufacturer_scoped_zero_ohm_chip_resistor_identity_marking_and_practical_resistance_boundary"
canonical_unit_policy: "Preserve source wording such as `0 ohm`, `jumper`, `000`, `0`, and `less than 50 mOhm`. Do not normalize manufacturer-scoped identity statements into universal design rules."
source_ids:
  - "rohm-jumper-chip-resistor-faq"
  - "panasonic-chip-resistor-zero-ohm-marking-guide"
tags: ["zero-ohm", "0-ohm", "jumper-resistor", "chip-resistor", "000-marking", "0-marking", "milliohm", "identity-boundary"]
---

# Canonical Summary

> The local corpus may now reuse one narrow official-source-backed boundary for zero-ohm chip resistors: official ROHM and Panasonic sources support treating them as `jumper`-class chip resistors, Panasonic publicly states that markings such as `000` and `0` can denote that class, and ROHM publicly states that real jumper chip resistors still have practical resistance rather than mathematically perfect zero resistance. This card does not authorize universal role taxonomy, fuse substitution, or current/power selection rules.

## Stable Facts

- Panasonic Industry states that some chip resistors use special zero-ohm markings such as:
  `000`, `0`, etc.
- Panasonic Industry states that those zero-ohm markings mean resistance value `approx. 0 ohm` and describes the part as `used as a jumper`.
- Panasonic Industry gives one example table row:
  `000 -> 0 ohm -> Zero ohm resistor`
- ROHM's official resistor FAQ frames the component class as `jumper chip resistors`.
- ROHM states that ideally jumper resistors have no resistance, but every conductive element possesses a certain level of resistance.
- ROHM states that its jumper resistors normally have resistance less than `50 mOhm`.

## Exact Data Scope

- exact for:
  - official `jumper` identity wording from ROHM and Panasonic
  - official Panasonic marking examples:
    `000`, `0`
  - the practical-resistance boundary that ROHM's jumper resistors are not physically perfect zero resistance and are normally `< 50 mOhm`
- not exact for:
  - every zero-ohm resistor made by every vendor
  - all package-dependent markings
  - current rating, power rating, or derating rules
  - all claimed use cases from secondary articles

## Conditions And Methods

- Use this card when the E6 article needs a safe owner-backed explanation that a `0 ohm resistor` can be a chip `jumper resistor` class rather than a separate magical component category.
- Use this card when a prompt needs to explain why `0 ohm` naming is nominal shorthand and should not be read as mathematically perfect zero resistance in the physical part.
- Use Panasonic's marking examples only as publicly stated manufacturer examples, not as a universal cross-vendor marking law.
- Pair this card with later owner datasheets only if a future lane needs named-part current, power, size, or environmental limits.

## Safe Blog Usage

- Safe to say that official owner sources describe zero-ohm chip resistors as jumper-style parts.
- Safe to say that markings such as `000` or `0` are publicly used by Panasonic for zero-ohm resistor identification.
- Safe to say that `0 ohm` naming is nominal and that actual jumper chip resistors can still have small real resistance.

## Limits And Non-Claims

- This card does not authorize the article's full `5 roles` taxonomy as universally proven.
- It does not authorize blanket debug, isolation, configuration, grounding, or option-selection claims unless a later source pass lands each role separately.
- It does not authorize fuse-substitute or sacrificial-protection claims.
- It does not authorize current-carrying, power-dissipation, temperature-rise, or package-selection rules.
- It does not authorize procurement, stock, cost, or assembly-yield claims.
- It does not authorize turning Panasonic's marking examples into an all-manufacturer marking standard.

## Relationship To E6 Article Route

- This card upgrades `0Ohm电阻` handling in `0Ω电阻在PCB板中的5大常见作用.pdf` from claim-family-only to one source-backed identity boundary.
- The landed scope is intentionally narrow:
  `jumper-class identity`
  `public marking examples`
  `low-but-nonzero practical resistance boundary`
- The route remains open for later role-by-role recovery if additional official sources are found.

## Source Links

- https://fscdn.rohm.com/en/products/databook/operation/passive/resistor/common/faq.pdf
- https://industrial.panasonic.com/ww/ds/ss/technical/b28

---
source_id: "rohm-jumper-chip-resistor-faq"
title: "Resistors - FAQ"
organization: "ROHM Co., Ltd."
owner: "ROHM"
source_type: "manufacturer_faq_pdf"
url: "https://fscdn.rohm.com/en/products/databook/operation/passive/resistor/common/faq.pdf"
jurisdiction: "global"
published_at: "2012-09"
checked_at: "2026-05-09"
retrieved_at: "2026-05-09"
trust_tier: "t1"
stability: "stable"
must_refresh: false
original_source_language: "en"
authority_class: "manufacturer_faq"
exact_data_class: "vendor_scoped_exact_data"
scope_type: "vendor_scoped_jumper_chip_resistor_identity_and_practical_resistance_boundary"
source_origin_path: "official ROHM FAQ PDF"
source_page_range: "page 2, question 7"
confidence: "high"
topic_tags: ["rohm", "jumper-resistor", "zero-ohm", "chip-resistor", "milliohm", "identity-boundary"]
status: "active"
notes: "Official ROHM FAQ PDF. Safe for the narrow owner-backed boundary that jumper chip resistors are treated as nominal zero-ohm class parts but still have practical low resistance in real conductive elements. Do not expand this into fuse behavior, current sizing, or universal application-role claims."
---

# Source Summary

## What It Covers

- ROHM resistor FAQ coverage for `jumper` chip resistors
- the distinction between ideal zero resistance and real conductive-element resistance
- ROHM's practical resistance statement for its own jumper resistors

## Why It Matters

- gives the E6 article route one official manufacturer source for `jumper resistor` identity instead of leaving `0 ohm` wording at secondary-blog level
- adds a safe non-mathematical boundary:
  nominal `0 ohm` naming does not mean physically zero resistance in the real part

## Extraction Notes

- Safe for the FAQ statement that ideally jumper resistors have no resistance.
- Safe for the FAQ statement that every conductive element possesses a certain level of resistance.
- Safe for the FAQ statement that ROHM's jumper resistors normally have a resistance less than `50 mOhm`.
- Safe for `jumper chip resistor` identity wording because the FAQ question itself is:
  `What is the resistance value of 'jumper' chip resistors?`
- Do not rewrite this FAQ into universal power, current, fusing, derating, or PCB role-selection rules.

## Refresh Notes

- Stable PDF with revision footer `2012.09 - Rev.A`; refresh only if a later prompt needs a newer ROHM jumper-resistor FAQ revision
- Preserve the `ROHM owner-scoped jumper resistor` framing whenever reusing the `< 50 mOhm` boundary

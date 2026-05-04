---
lane: "P4-87a 2026.4.29 hearing-aid wireless and telecoil authority scout"
title: "Authority-recovery scout for hearing-aid wireless, Auracast, and telecoil exact nouns in 2026.4.29"
status: "completed_at_claim_family_level"
reviewed_at: "2026-05-01"
owner_scope: "/code/blogs/llm_wiki/logs/p4-87a-hearing-aid-wireless-and-telecoil-authority-scout.md"
model: "gpt-5"
input_root: "/code/blogs/tmps/2026.4.29/en/hearing-aid-pcb.md"
---

# Scope

- Assigned lane: `hearing-aid authority recovery scout for 2026.4.29`
- Input inspected as claim inventory only:
  `/code/blogs/tmps/2026.4.29/en/hearing-aid-pcb.md`
- Output-only boundary honored: only this log file was edited
- No edits made to trackers, facts, wiki pages, source registry, or unrelated files
- Focus held to exact-noun authority recovery candidates around `BLE Audio`, `Auracast`, `telecoil`, and tightly adjacent official-source routes

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-87a-hearing-aid-wireless-and-telecoil-authority-scout.md`

# Files And Sources Inspected

## Draft inspected

- `tmps/2026.4.29/en/hearing-aid-pcb.md`

## Existing local reuse layer inspected

- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md`
- `facts/methods/conformal-coating-medical-regulated-boundary.md`
- `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md`
- `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
- `facts/standards/medical-and-automotive-led-pcb-standards-boundary.md`
- `sources/registry/standards/bluetooth-core-specification-page.md`
- `sources/registry/standards/iso-13485-2016-page.md`
- `sources/registry/standards/iec-60601-1-medical-electrical-equipment-page.md`
- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`

## External official-source routes checked on 2026-05-01

- Bluetooth SIG `LE Audio`
  - `https://www.bluetooth.com/learn-about-bluetooth/bluetooth-technology/le-audio/`
- Bluetooth SIG `Support for hearing assistance`
  - `https://www.bluetooth.com/learn-about-bluetooth/bluetooth-technology/le-audio/hearing/`
- Bluetooth SIG `Bluetooth LE Audio FAQs`
  - `https://www.bluetooth.com/media/le-audio/le-audio-faqs/`
- Bluetooth SIG `Auracast`
  - `https://www.bluetooth.com/auracast/`
- Bluetooth SIG `Auracast - How it works`
  - `https://www.bluetooth.com/auracast/how-it-works/`
- IEC `IEC 60118-4:2014+AMD1:2017 CSV`
  - `https://webstore.iec.ch/en/publication/61949`
- IEC `IEC 60118-13:2019`
  - `https://webstore.iec.ch/en/publication/59638`

# Lane Status

- Overall lane status: `completed_at_claim_family_level`
- Existing support depth: `source_backed_fact_layer_partial`
- Exact-noun blocker shape: `blocked_pending_official_source`
- Recommended next deliverable after source recovery:
  `facts/interfaces/hearing-aid-wireless-and-telecoil-identity-boundary.md`

# Existing Support IDs And Paths Worth Reusing

## Medical manufacturing-control and documentation boundary

- `wiki/processes/medical-imaging-wearable-empty-image-rewrite-gate.md`
  - topic id: `processes-medical-imaging-wearable-empty-image-rewrite-gate`
- `facts/methods/pcba-medical-traceability-dhr-dmr-boundary.md`
  - fact id: `methods-pcba-medical-traceability-dhr-dmr-boundary`
- `facts/standards/fda-medical-device-documentation-and-traceability-metadata.md`
  - fact id: `standards-fda-medical-device-documentation-and-traceability-metadata`
- `facts/methods/conformal-coating-medical-regulated-boundary.md`
  - fact id: `methods-conformal-coating-medical-regulated-boundary`

## Regulated-market standards boundary already present

- `sources/registry/standards/iso-13485-2016-page.md`
  - source id: `iso-13485-2016-page`
- `sources/registry/standards/iec-60601-1-medical-electrical-equipment-page.md`
  - source id: `iec-60601-1-medical-electrical-equipment-page`
- `facts/standards/medical-and-automotive-led-pcb-standards-boundary.md`
  - fact id: `standards-medical-and-automotive-led-pcb-boundary`

## Wireless identity boundary already present

- `sources/registry/standards/bluetooth-core-specification-page.md`
  - source id: `bluetooth-core-specification-page`
- `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`
  - fact id: `standards-interface-wireless-positioning-product-level-boundary`

# Safe Reuse Classes

- `hearing aid` may be used as application context that increases miniaturization, moisture, traceability, and documentation pressure.
- `ISO 13485`, `IEC 60601-1`, `FDA`, `DMR`, `DHR`, and `UDI` may be used only at standards, documentation, or manufacturing-role boundary level.
- Generic `Bluetooth` may be used only at standards-owner and product-level boundary level through the existing Bluetooth SIG core-spec source and wireless boundary card.
- Coating, traceability, inspection, and compact medical-adjacent assembly workflow language may be reused, but only as manufacturing-control posture.

# Exact-Noun Authority Recovery Candidates

## 1. `BLE Audio` and `LE Audio`

- Current local status:
  blocked as an exact noun for hearing-aid writing; current corpus has only generic `Bluetooth Core Specification` identity.
- Strongest official-source route:
  - Bluetooth SIG `LE Audio`
  - Bluetooth SIG `Support for hearing assistance`
  - Bluetooth SIG `Bluetooth LE Audio FAQs`
- Safe recovery shape if added:
  - `LE Audio` as the Bluetooth SIG's next-generation Bluetooth audio family
  - hearing-aid support as Bluetooth SIG hearing-assistance context
  - guarded linkage between `LE Audio` and `Auracast`
  - guarded note that LE Audio depends on newer Bluetooth core features, if taken from the SIG FAQ layer
- Still blocked even after a minimal identity pass:
  - `LC3 codec at 32 kHz sample rate`
  - latency, power draw, battery-life, interoperability, pairing simplicity, smartphone coverage, and product-readiness claims
  - any claim that a bare PCB, board layout, or supplier is `Bluetooth LE Audio` qualified

## 2. `Auracast`

- Current local status:
  blocked as an exact noun; not present in local facts or source registry.
- Strongest official-source route:
  - Bluetooth SIG `Auracast`
  - Bluetooth SIG `Auracast - How it works`
  - Bluetooth SIG `LE Audio` page for parent-family context
- Safe recovery shape if added:
  - `Auracast` as Bluetooth SIG broadcast-audio capability or brand-family vocabulary
  - public-broadcast and assistive-listening context at standards-owner level
  - transmitter / receiver / assistant vocabulary only if taken from the Bluetooth SIG how-it-works page
- Still blocked even after a minimal identity pass:
  - venue availability, user adoption, privacy, reliability, audio quality, range, or hearing-aid compatibility claims
  - any statement that a supplier can ship `Auracast-ready` hardware without product evidence
  - draft claims that public systems already support the exact target use case

## 3. `telecoil`

- Current local status:
  blocked as an exact noun family; no local `IEC 60118` source record exists.
- Strongest official-source route:
  - IEC `IEC 60118-4:2014+AMD1:2017 CSV`
  - optional adjacent route: IEC `IEC 60118-13:2019` if the future rewrite must discuss hearing-aid immunity around nearby mobile wireless devices
- Safe recovery shape if added:
  - `telecoil` only as induction pick-up coil context for hearing aids
  - `induction-loop systems for hearing aid purposes` as the exact official noun family
  - loop-system / hearing-aid interface context without converting it into PCB geometry or performance proof
- Still blocked even after a minimal identity pass:
  - `3.15 kHz +/-10%` draft numerics
  - coil orientation rules, field-strength thresholds, intelligibility outcome claims, interference claims, or PCB spiral equivalence claims
  - any claim that the draft's telecoil implementation details are standardized, sufficient, or production-proven

# Tightly Adjacent But Not Yet Safe

- `IEC 60601-1`:
  already present locally, but only as medical electrical equipment standards identity; it does not prove `all PCB materials meet IEC 60601-1 requirements`.
- `ISO 13485`:
  already present locally, but only as QMS identity; it does not prove HILPCB certification or hearing-aid program qualification.
- `ISO 10993-5`:
  cited in the draft, but there is no current local source record for this exact standard in `llm_wiki`.
- `IEEE 1528`:
  cited in the draft as SAM head context, but there is no current local source record for this exact noun in `llm_wiki`.
- `Qi`:
  cited in the draft as charging-family context, but there is no current local source record for Wireless Power Consortium Qi identity in `llm_wiki`.

# Blocked Claims That Must Stay Blocked In This Lane

- All battery-life, power, current, leakage, field-strength, antenna-gain, keepout, charging-coil, sample-rate, and delay numerics from the draft
- `FDA Class II`, `510(k)`, `EU MDR`, or supplier `ISO 13485` language used as board-readiness or supplier-proof claims
- `Cochlear Implant PCB`, implantable, patient-contact, or medical-release language
- `IEC 60601-1`, `ISO 10993-5`, or any biocompatibility wording used as proof that board materials or finishes are medically suitable
- HILPCB capability claims around `01005`, bare-die bonding, hearing-implant boards, layer counts, volume, yield, traceability depth, or medical qualification
- RF coexistence, telecoil immunity, `BLE Audio` interoperability, `Auracast` assistive-listening readiness, and phone or public-venue compatibility claims

# Source Gaps

- No local source record yet for `LE Audio`
- No local source record yet for `Auracast`
- No local source record yet for `IEC 60118-4`
- No local source record yet for `IEC 60118-13`
- No local source record yet for `ISO 10993-5`
- No local source record yet for `IEEE 1528`
- No local source record yet for `Qi`

# Recommended Narrow Next Step

- Recover only the identity layer first:
  `LE Audio`, `Auracast`, `telecoil`, and `IEC 60118-4`, with optional `IEC 60118-13` if wireless-immunity adjacency is required.
- Keep recovery output at exact-noun vocabulary and owner-standard context only.
- Do not combine this lane with:
  `ISO 10993-5`, `IEEE 1528`, `Qi`, `FDA Class II`, `510(k)`, `MDR`, implant, or HILPCB certification proof.

# Scout Conclusion

- The hearing-aid draft already has reusable medical manufacturing-control and generic Bluetooth boundary support.
- The narrow missing authority layer is not broad `medical` support; it is the exact-noun family around `LE Audio`, `Auracast`, and `telecoil`.
- This lane is suitable for a small next integration once Bluetooth SIG and IEC `60118` owner pages are registered.

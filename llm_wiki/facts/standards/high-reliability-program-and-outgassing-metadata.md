---
fact_id: "standards-high-reliability-program-and-outgassing-metadata"
title: "Public aerospace, medical, military, and outgassing references support program-metadata framing for hi-rel PCB writing, not proof of qualification"
topic: "high reliability program and outgassing metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "as9102c-first-article-inspection-page"
  - "iso-13485-2016-page"
  - "fda-qmsr-page"
  - "fda-udi-basics-page"
  - "ipc-validation-services-qml-ipc-1791-page"
  - "ipc-validation-services-qml-j-std-001s-space-military-addendum-page"
  - "ipc-6012em-medical-addendum-release"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fa-toc"
  - "mil-prf-55110-general-spec-page"
  - "mil-prf-31032-general-spec-page"
  - "mil-prf-31032-1e-rigid-multilayer-thermosetting-spec-sheet-page"
  - "mil-prf-31032-qml-page"
  - "dla-qml-qpl-qbl-listing-page"
  - "dla-sourcing-qualifications-division-page"
  - "astm-e595-15r21-page"
  - "nasa-vacuum-outgassing-database-page"
  - "nasa-outgassing-user-guide-page"
tags: ["as9102", "iso-13485", "fda", "qmsr", "udi", "ipc-6012em", "mil-prf-31032", "astm-e595", "nasa", "outgassing", "high-reliability", "metadata"]
---

# Canonical Summary

> Public SAE, ISO, FDA, IPC, DLA, ASTM, and NASA pages are strong enough to anchor high-reliability program vocabulary in `llm_wiki`: `AS9102C` for first-article-inspection identity, `ISO 13485:2016` plus FDA `QMSR` and `UDI` pages for medical-device quality-system and traceability vocabulary, current `IPC-6012` addendum pages for procurement-triggered medical and automotive branches beyond generic `Class 3` framing, `MIL-PRF-55110` / `MIL-PRF-31032` for the legacy/current military rigid-board qualification ecosystem, and `ASTM E595` plus NASA outgassing pages for method and screening context. None of these public pages prove that a given PCB supplier, lot, or stackup is qualified, certified, or approved.

## Stable Facts

- `AS9102C` is the current SAE first-article-inspection requirements reference and publicly frames `FAI` as a documented inspection discipline complementary to customer and regulatory requirements.
- `ISO 13485:2016` is the current published ISO medical-device quality-management-system reference in this corpus and is publicly positioned as a regulatory-purpose `QMS` framework.
- FDA's public `QMSR` page now gives this corpus a current U.S. regulatory anchor for medical-device quality-system framing linked to `21 CFR Part 820` and `ISO 13485:2016`.
- FDA's public `UDI Basics` page gives this corpus guarded vocabulary for device identification and traceability concepts such as `DI`, `PI`, and `GUDID`.
- IPC's public `QML IPC-1791` page adds a guarded organization-level `trusted source` layer for electronic designers, fabricators, and assemblers in integrity-assurance markets without qualifying any specific finished board.
- IPC's public `QML J-STD-001S Space/Military Addendum` page adds a separate guarded assembly-process listing layer for `EMS/OEM` providers, which is narrower than bare-board qualification and should stay separate from rigid-board acceptance framing.
- IPC's public `IPC-6012EM` release page confirms that IPC created a medical applications addendum to the rigid-board performance-specification family and publicly states that it was intended for medical-device use cases needing more-stringent fabrication requirements than generic `Class 3` framing.
- IPC's public `IPC-6012FA` product page and TOC confirm that automotive rigid-board requirements now also sit inside the same procurement-triggered `IPC-6012` addendum-family structure, with automotive-specific qualification/reliability clause families remaining controlled content rather than reusable public thresholds.
- `MIL-PRF-55110` is a legacy rigid-board general specification whose public detail page is useful for identity and scope framing, but it remains a guarded linkage anchor rather than current qualification proof.
- `MIL-PRF-31032` is publicly framed by DLA as the general printed-board performance-specification family tied to a military qualification ecosystem and `QML` handling.
- DLA's public `MIL-PRF-31032/1E` detail page gives the rigid multilayer thermosetting-resin branch a cleaner sheet-level identity anchor inside the broader `MIL-PRF-31032` ecosystem, but it still does not prove current qualification, listing, or supplier approval.
- DLA's public `QML/QPL/QBL` listing page adds a stronger government-side boundary that qualification listing is generally performed in advance against governing specifications and should stay separate from acquisition-time acceptance.
- DLA's public Sourcing and Qualifications Division page confirms that qualification listings, technical evaluations, audits, and printed-wiring-board qualification management belong to an active DLA organizational ecosystem.
- `ASTM E595-15(2021)` is publicly framed as a vacuum-outgassing screening test method measuring `TML`, `CVCM`, and `WVR`, not as a universal mission-acceptance rule by itself.
- NASA Goddard publicly states that its vacuum outgassing database supports spaceflight-material screening and that testing is performed in accordance with `ASTM E595`.
- NASA's outgassing user guide also publicly shows that the familiar `TML 1.0%` and `CVCM 0.10%` values belong to the database's low-outgassing screening presentation and should not be flattened into universal bare-board acceptance criteria without program authority.

## Conditions And Methods

- Use this card when a `22-layer` or other hi-rel draft needs to mention aerospace `FAI`, medical-device `QMS`, medical addendum context, military-board qualification programs, or outgassing-screening context.
- Use this card when a `22-layer` or other hi-rel draft needs guarded `trusted source` or organization-level integrity-assurance vocabulary without implying customer approval or release authority.
- Use this card when a `22-layer` or other hi-rel draft needs guarded wording that some IPC `QML` listings can sit at the `assembly-process` layer for `EMS/OEM` providers rather than at the bare-board or finished-board qualification layer.
- Use this card when a `22-layer` or other hi-rel draft needs guarded wording that military qualification-listing infrastructure can be a pre-acquisition government listing layer rather than a direct product-acceptance decision.
- Pair this card with actual supplier certifications, customer flowdowns, program documents, and licensed standards before making any claim about approval, compliance, or release authority.
- Use the outgassing part of this card for method naming and screening context, not for flattening spacecraft-material acceptance into one generic threshold table.

## Limits And Non-Claims

- This card does not prove that any PCB fabricator is certified to `ISO 13485`, compliant with `AS9102`, or qualified under `MIL-PRF-31032`.
- It does not prove that any supplier complies with `IPC-6012FA` or that automotive addendum wording transfers into reusable acceptance thresholds for a `22-layer` board.
- It does not prove that an organization listed under `IPC-1791 QML` is approved, accepted, or release-authorized for any specific `22-layer` program or finished board.
- It does not prove that a company listed under `J-STD-001S` `QML` can fabricate, qualify, or release a specific `22-layer` bare board.
- It does not prove that `MIL-PRF-55110` is a current qualification basis, current listing status, or supplier approval for any specific board.
- It does not prove that appearance inside any DLA `QML/QPL/QBL` listing ecosystem automatically makes a supplier or board accepted for a specific `22-layer` program or acquisition.
- It does not provide clause-level `FAI` content, medical-device traceability requirements, military acceptance thresholds, or cleanroom-class requirements.
- It does not turn `IPC-6012EM`, `ASTM E595`, or NASA outgassing data into automatic approval for a finished multilayer board, adhesive system, or assembly.

## Open Questions

- Add a separate guarded source layer for explicit supplier certification evidence only if future evidence packs need manufacturer-specific certification claims.
- Decide whether additional `MIL-PRF-31032` specification-sheet families beyond the rigid-multilayer thermosetting-resin branch need their own metadata cards.

## Source Links

- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
- https://www.iso.org/standard/59752.html
- https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
- https://www.electronics.org/validation-services-qualified-manufacturing-companies-qml-j-std-001s-spacemilitary-addendum
- https://www.electronics.org/news-release/ipc-releases-ipc-6012em-medical-applications-addendum-ipc-6012e-qualification-and
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english-0
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=29227
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=119627
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=119628
- https://landandmaritimeapps.dla.mil/programs/qmlqpl/QPLdetail.aspx?QPL=31032
- https://www.dla.mil/Working-With-DLA/Applications/Details/Article/2937421/qmlqpl-listing-qualified-manufacturers-listqualified-product-list/
- https://www.dla.mil/Land-and-Maritime/Offers/Technical-Support/Sourcing-Division/
- https://store.astm.org/e0595-15r21.html
- https://etd.gsfc.nasa.gov/capabilities/capabilities-listing/vacuum-outgassing-database/
- https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide

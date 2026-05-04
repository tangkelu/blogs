---
fact_id: "standards-ipc-flex-rigid-flex-standards-hierarchy-boundary"
title: "IPC flex and rigid-flex standards hierarchy separates design guidance (IPC-2223E) from performance qualification (IPC-6013E), both distinct from rigid-board specs (IPC-6012F)"
topic: "IPC flex and rigid-flex standards hierarchy"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "ipc-2223e-flex-rigid-flex-design-standard-page"  # refreshed 2026-05-03
  - "ipc-6013e-toc"  # refreshed 2026-05-03
  - "ipc-6012f-toc"  # refreshed 2026-05-03
  - "ipc-6012-addendum-taxonomy-page"
tags: ["ipc", "ipc-2223", "ipc-6013", "ipc-6012", "flex", "rigid-flex", "design-standard", "performance-specification", "hierarchy", "boundary"]
---

# Canonical Summary

> IPC maintains separate but related standards for flex/rigid-flex printed boards: `IPC-2223E` as the sectional design standard, `IPC-6013E` as the qualification and performance specification. These are distinct from the rigid-board ecosystem (`IPC-6012F` base + addendums). Understanding this hierarchy prevents conflating design guidance with acceptance criteria, and rigid-board rules with flexible-board requirements.

## Standards Hierarchy

### Design vs Performance Separation

| Standard | Type | Scope | Board Family |
|----------|------|-------|--------------|
| IPC-2223E | Sectional Design Standard | Design rules, geometry, material selection | Flexible / Rigid-Flexible |
| IPC-6013E | Performance Specification | Qualification, testing, acceptance criteria | Flexible / Rigid-Flexible |
| IPC-6012F | Performance Specification | Qualification, testing, acceptance criteria | Rigid (multilayer, microvia, metal-core) |

### Key Distinctions

**IPC-2223E (Design)**
- Provides design guidance for flexible and rigid-flexible board constructions
- Covers material selection, conductor geometry, bend radius considerations, adhesive systems
- Does not specify acceptance thresholds or qualification criteria

**IPC-6013E (Performance)**
- Qualification and performance specification for flexible printed boards
- Defines acceptance criteria, test methods, and qualification requirements
- Pairs with IPC-2223E design inputs for complete flex/rigid-flex coverage

**IPC-6012F (Rigid Performance)**
- Qualification and performance specification for rigid printed boards
- Base document for medical (IPC-6012EM), automotive (IPC-6012FA), and space/military (IPC-6012FS) addendums
- Does not cover flexible or rigid-flexible constructions

## Cross-References and Relationships

- `IPC-2223E` design output feeds into `IPC-6013E` qualification requirements
- `IPC-6013E` and `IPC-6012F` are parallel performance specifications for different board families
- `IPC-6012F` addendums (EM/FA/FS) extend rigid-board requirements for specific industries
- No addendum structure currently exists for `IPC-6013E` in public IPC metadata

## Conditions And Methods

- Use this hierarchy card when articles conflate design standards with performance specifications
- Apply when distinguishing rigid-board requirements from flex/rigid-flex requirements
- Reference when explaining why acceptance criteria cannot be derived from design standards alone
- Pair with material-specific fact cards (Kapton, Upilex, LCP) for complete flex board guidance

## Limits And Non-Claims

- This card does not provide specific bend radius values, cycle counts, or geometric thresholds
- It does not reproduce acceptance criteria from IPC-6013E or IPC-6012F
- It does not prove supplier capability or certification under any IPC standard
- It does not establish that IPC-2223E and IPC-6013E are interchangeable or equivalent

## Open Questions

- Monitor IPC for potential flex/rigid-flex addendum structure similar to IPC-6012F addendums
- Assess whether future high-reliability flex applications will require dedicated addendum coverage

## Source Links

- https://shop.electronics.org/ipc-2223/ipc-2223-standard-only/Revision-e/english
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://shop.electronics.org/taxonomy/term/792

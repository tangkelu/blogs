---
fact_id: "methods-selective-wave-solder-and-mixed-technology-sequencing"
title: "Selective and wave solder should be framed as board-population choices inside SMT-first mixed-technology assembly"
topic: "Selective and wave solder mixed-technology sequencing"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "ipc-document-revision-table"
  - "ipc-j-std-001j-toc"
  - "ipc-a-610h-toc"
tags: ["selective-solder", "wave-solder", "smt", "tht", "mixed-technology", "sequencing"]
---

# Canonical Summary

> For mixed-technology assemblies, the stable rewrite is that SMT reflow, through-hole insertion, and either selective or wave solder are sequenced together; the choice between selective and wave depends on board population and nearby component constraints, not on a universal superiority claim.

## Stable Facts

- The internal SMT/THT page frames stencil and paste engineering, SMT placement, selective and wave solder, and inspection/test as parts of one assembly flow.
- The internal selective-solder page frames targeted soldering for through-hole content on mixed-technology boards while protecting nearby SMDs.
- The HIL through-hole assembly page also describes SMT-first sequencing followed by THT insertion and wave or selective solder for mixed-technology builds.
- The HIL through-hole assembly page describes wave solder as a throughput-oriented method for THT-dense boards and selective solder as a localized-heating method for mixed-technology layouts.
- Internal inspection pages tie post-solder inspection and electrical validation back into the same process chain.
- IPC assembly standards metadata can anchor soldered-assembly and acceptability standard families at a high level, but not detailed workmanship thresholds.

## Conditions And Methods

- Use this card for `selective-wave-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-medical-imaging-wearable`, and related SMT/THT mixed-assembly rewrites.
- Safe rewrite pattern: dense SMT or heat-sensitive neighbors can push a board toward selective solder, while THT-heavy populations can make wave solder relevant when the layout permits it.
- Treat manual soldering, selective solder, and wave solder as production-route options influenced by component population, thermal sensitivity, board geometry, and inspection strategy.
- For medical imaging, wearable, or compact mixed-signal assemblies, keep the claim at the process-planning level rather than stating a mandatory soldering route.
- For articles comparing methods, say selective solder can help localize heat around through-hole joints on mixed-tech boards; do not state it is always lower risk or always higher reliability than wave solder.

## Limits And Non-Claims

- This card does not provide solder-pot settings, nozzle sizes, preheat windows, nitrogen requirements, or hole-fill acceptance thresholds.
- It does not prove that every medical or wearable assembly uses selective solder rather than wave or hand solder.
- It does not authorize IPC class-specific acceptability claims or yield claims.
- It does not claim selective solder is categorically required for all high-density or mixed-technology boards.

## Open Questions

- Add public source support for selective-solder design-for-access guidance if future slugs need stronger DFM language.
- Add a separate card for hand-solder and rework boundaries if prototype-heavy medical wearable rewrites need that distinction.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf

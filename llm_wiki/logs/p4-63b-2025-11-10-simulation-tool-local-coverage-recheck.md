# P4-63B Simulation Tool Local Coverage Recheck

Date: 2026-04-30
Scope: local coverage recheck for `/code/blogs/llm_wiki` against `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Recheck Result

The current `llm_wiki` corpus does cover parts of the named simulation-tool lane, but only at adjacent boundary level. It already supports:

- formula identity for `W`, `V`, `A`, and the narrow `A = W / V` restatement
- current-driven PCB consequence wording at conductor-sizing / high-current-layout level
- pre-fabrication validation as a workflow boundary
- PCB design-tool feature identity for KiCad and Autodesk EAGLE / Fusion
- CAM / fabrication-data exchange boundaries for Gerber and IPC-DPMX / IPC-2581
- validation-method separation for ICT vs FCT and flying probe vs ICT

It does not yet have a dedicated `llm_wiki` source record or fact card for the named HILPCB circuit simulator itself.

## Source-Backed Coverage Already Present

- `facts/methods/electrical-formula-identity-boundary.md` supports the minimal formula lane only; it explicitly blocks simulation, manufacturability, and PCB consequence claims beyond that.
- `facts/methods/current-carrying-trace-width-and-copper-boundary.md` supports current-driven conductor sizing and high-current layout, and explicitly blocks simulation accuracy, DFM, DFT, and manufacturability claims.
- `facts/methods/pre-fabrication-validation-workflow-boundary.md` supports review / prototype / FAI / staged handoff language, and explicitly says it does not authorize claims about a vendor-specific online circuit simulator.
- `facts/methods/pcb-design-tool-official-feature-identity-boundary.md` supports feature identity for KiCad and Autodesk tools, including integrated SPICE simulation and 3D viewer vocabulary for KiCad, but only as tool identity.
- `facts/methods/cam-data-exchange-format-boundary.md` and `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` support Gerber, IPC-DPMX / IPC-2581, and viewer-status vocabulary as format / tool-boundary context.
- `facts/methods/pcba-ict-vs-fct-boundary.md`, `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md`, and `facts/methods/advanced-validation-scope-segmentation.md` support validation-stage separation, but not simulation proof.

## Adjacent Context Only

- `facts/methods/internal-resource-layer-prompt-support-corpus.md` and `sources/registry/internal/frontendapt-resources-index-page-en.md` show that the internal resource hub includes an `online tools` bucket, but they do not register the simulator page as a dedicated `llm_wiki` source.
- The local HILEAP corpus contains a real HILPCB circuit-simulator page and related blog references, including `/code/hileap/frontendHIL/pages/tools/circuit-simulator.vue` and the `/tools/circuit-simulator` route, but that material is outside the `llm_wiki` source registry used for this recheck.
- The article at `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md` explicitly uses `HILPCB’s online circuit simulator` as validation language, so the named-tool lane exists in the draft, but not yet in `llm_wiki` as an owned fact layer.

## Boundary Assessment

The narrowest promotable boundary is:

- a named, vendor-branded online circuit simulator can be mentioned as a tool identity
- it must remain separate from claims that the tool proves current draw, simulation accuracy, thermal behavior, manufacturability, or production readiness
- it must not be used to imply that the board is complete, validated, or design-closed

However, because `llm_wiki` currently lacks a dedicated source record or fact card for that simulator identity, the boundary is only adjacent today. It is not yet fully source-backed inside `llm_wiki` the way KiCad feature identity, Gerber identity, or validation workflow boundaries are.

## Conclusion

No tracker updates, fact edits, or wiki edits were needed for this recheck. The corpus already supports a strict separation between formula identity, board-consequence review, and validation workflow. The named simulation-tool lane remains too thin to promote as an owned `llm_wiki` fact layer without a dedicated source registration pass.

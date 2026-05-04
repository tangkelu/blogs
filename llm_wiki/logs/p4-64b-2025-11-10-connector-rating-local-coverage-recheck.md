# P4-64B Local Coverage Recheck

Date: 2026-04-30  
Scope: `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`

## Conclusion

The local llm_wiki layer is strong enough to support the draft only at the formula-to-board-consequence boundary: calculate current, then move into generic conductor-sizing and high-current-layout review. It is not strong enough to promote connector-rating or component-current-rating claims without owner datasheets or a dedicated current-rating source lane.

## Already Source-Backed

- The watts-to-amps draft can safely keep the basic `A = W / V` teaching lane separate from board-design consequences. The local formula boundary card explicitly allows that narrow algebraic restatement and blocks trace-width, copper-weight, connector-rating, and thermal conclusions inferred directly from the formula layer.
- The current-carrying boundary card supports a conservative PCB consequence lane after current is known: conductor width, copper weight, planes, vias, current-path geometry, and thermal-stress review.
- The power-interface route-selection card supports the architectural split between board-level soldered hardware, press-fit connector zones, and off-board cable or harness integration.
- The THT / press-fit / harness fact card supports the distinction between soldered board retention, press-fit insertion, and harness or box-build handoff, while explicitly refusing current ratings and related connector numerics.
- The THT-heavy assemblies card supports keeping connectors, relays, transformers, inductors, and other mechanically stressed or larger power hardware inside the same mixed-technology assembly workflow, but not rating claims.

## Adjacent Context Only

- The power-energy and medical industry pages are useful for scenario framing only. They support inverter, charger, imaging, wearable, and interface-module context, but they do not authorize current numbers, connector ratings, compliance proof, or product capability claims.
- The press-fit finish and backplane cards support hole control, finish choice, and connector-zone planning. That is adjacent to connector selection, but it is not a current-rating source.
- The harness and box-build pages support wiring, routing, electromechanical integration, firmware load, functional test, and serialization. That is adjacent to off-board connection strategy, not a connector ampacity authority.
- The internal source registry entries for through-hole, SMT/THT, surface finish, drilling, power-energy, and medical pages all point to process and context, not vendor-rated connector current.

## Not Yet Promotable

- `connector ratings` in the draft are not promotable from the current local corpus. The closest support only says connector ratings should be treated as a separate evidence lane, and the current boundary cards explicitly block connector-rating conclusions.
- `component ratings` are also not promotable from the current local corpus when they are tied to the calculated current. The draft’s line about selecting components that safely handle the current is reasonable engineering advice, but the local llm_wiki layer does not back it with a reusable rating fact.
- There is no narrow connector-current boundary in the local corpus that is safe to promote without a connector-owner datasheet, a vendor application note, or a dedicated connector-rating fact card.

## Practical Rewrite Boundary

- Keep the article at: power calculation -> current calculation -> generic board-consequence review.
- If the draft needs to mention a connector or component, phrase it as a design-review dependency, not as an asserted rating.
- If the draft needs a true connector-current claim, add a separate evidence lane first; do not infer it from PCB current math, THT context, press-fit context, or harness context.

## Evidence Notes

- Draft lines `16`, `18`, `27`, `31`, `75`, `78`, `81`, `84`, `93`, `94`, `102`, `104`, `111`, `119`, and `123` are the main claim pressure points.
- Most of those lines are supportable only up to generic board-design review language, not up to connector ampacity or component-rating promotion.
- The only clearly promotable narrow boundary today is the board-consequence boundary after current is known, not a connector-rating boundary.

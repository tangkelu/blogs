---
lane: "P4-64C connector-rating official-source scout"
title: "Official-source scout for the narrowest promotable connector-rating and component-current-rating lane"
status: "completed_at_claim_family_level"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-64c-2025-11-10-connector-rating-official-source-scout.md"
input_root: "/code/blogs/tmps/2025.11.10/en"
model: "gpt-5.4"
---

# Purpose

- Assigned lane: `P4-64C connector-rating official-source scout`
- Goal: determine the narrowest promotable official-source lane for the draft's `connector ratings` and `component current ratings` claim family.
- Draft input was treated as claim inventory only, not as authority.
- Output-only boundary honored: no tracker edits, no fact/wiki/source-registry edits, and no edits outside this log.

# Exact Files Reviewed

## Draft and local files

- `/code/blogs/tmps/2025.11.10/en/watts‑to‐amps.md`
- `/code/blogs/llm_wiki/logs/p4-61a-2025-11-10-watts-to-amps-pcb-consequence-split.md`
- `/code/blogs/llm_wiki/wiki/processes/power-interface-connector-assembly-route-selection.md`

## Official public sources checked

### Used for the conservative unlock boundary

- TE Connectivity, `Power Systems Connectors in Power Systems`
  - https://www.te.com/en/products/connectors/power-connectors/intersection/communications-power-connectors.html
- TE Connectivity, `Economy Power 2.5 Connectors`
  - https://www.te.com/en/products/connectors/power-connectors/intersection/economy-power-2-5-connectors.html
- TE Connectivity, `Wire to Board Economy Power Connectors`
  - https://www.te.com/en/products/connectors/power-connectors/intersection/economy-power-connectors.html
- Molex, `EXTreme LPHPower`
  - https://www.molex.com/en-us/products/connectors/board-to-board-connectors/extreme-power-products/extreme-lphpower
- Phoenix Contact, `HV M5/1 NFF - High-current connector - 1056835`
  - https://www.phoenixcontact.com/en-us/products/bolt-connection-terminal-block-hv-m51-nff-1056835
- Phoenix Contact, `SF-7EP1N8A90A2 - Coupler connector - 1605570`
  - https://www.phoenixcontact.com/en-us/products/circular-connector-cable-side-sf-7ep1n8a90a2-1605570
- TE Connectivity, `AC Contactors: TPST, 2PST`
  - https://www.te.com/en/product-CAT-D-PST-AC-CONT.html

### Checked but not used to widen the unlock

- WAGO, `Mini Terminal Block – A Real Space Genius`
  - https://www.wago.com/us/electrical-interconnections/discover-rail-mount-terminal-blocks/mini-rail-mount-terminal-blocks
- WAGO, `Plug-in current transformer (855-305/250-509)`
  - https://www.wago.com/us/signal-conditioners/plug-in-current-transformer/p/855-305_250-509

# Draft Claim Inventory Rechecked

- `watts‑to‐amps.md` line 16 ties current conversion to `component ratings`.
- `watts‑to‐amps.md` line 27 says current values let readers `select components`.
- `watts‑to‐amps.md` line 78 says if current shows `10 A drawn from a regulator or connector`, readers `must select components that safely handle that current plus a safety margin`.
- `watts‑to‐amps.md` line 111 says current `dictates ... component ratings`.

# Existing Local Coverage Reconfirmed

- `p4-61a` already split `connector ratings and component current ratings` into a separate evidence lane and kept it blocked without a source pack.
- `power-interface-connector-assembly-route-selection.md` explicitly says connector-family-specific current claims must be refreshed before publishing.
- No existing local fact card or wiki page provides a source-backed generic `connector current-rating selection` rule.

# Official Source Findings

## What the manufacturer-owned sources clearly show

- TE's power-connector selection page explicitly asks `How much current is required in the application?` and says power-connector performance is typically measured in amperes.
- TE connector family pages publish explicit current fields such as `Maximum Current Rating (A) 4.2` for Economy Power 2.5 and `rated for 7.5A` / `support up to 11A` for Economy Power / Economy Power II.
- Molex connector pages publish `Current (MAX per contact)` fields, such as `30.0A` on EXTreme LPHPower.
- Phoenix Contact connector pages publish `nominal current` fields, such as `76 A` on HV M5/1 NFF and `9 A` on SF-7EP1N8A90A2.
- TE component-owner pages also publish explicit `Contact Current Rating (A)` fields for electromechanical parts, such as `50 | 60 | 120 | 245` on the cited AC contactor page.

## Conservative inference allowed from those sources

- Once current is known, it is supportable to use that current as a screening input when choosing a connector.
- It is supportable to tell readers to compare candidate parts against the manufacturer-published current field on the official product page or datasheet, using terms like `maximum current rating`, `current (max per contact)`, `nominal current`, or `contact current rating`.
- A similarly narrow statement can be made for current-rated electromechanical components that expose an official `contact current rating`.
- This is still a conservative inference from TE's selector question plus cross-manufacturer rating fields. It is not a universal connector law and not a general rule for every component class.

# Conservative Unlock Boundary

## Promotable now

- `After calculating current, check the candidate connector's manufacturer-published current rating or nominal current on the official product page or datasheet.`
- `Connector families publish different official current ratings, so current can be used as one screening input after the required current is known.`
- `For current-rated electromechanical parts that publish a contact current rating, the official component page or datasheet can be used as the rating reference.`

## Exact boundary condition

- Keep the statement at `manufacturer-published current field exists and should be checked after current is known`.
- If the draft wants to say `component`, narrow it to a named current-rated class or to `current-rated electromechanical components`.
- Do not widen from `check the published rating` into `how much margin`, `why the rating is what it is`, or `what else current automatically determines`.

# Blocked Claims That Remain Blocked

- any `plus a safety margin` instruction or formula
- any universal rule that current alone determines the correct connector or component
- any thermal-rise, overheating, ambient-temperature, derating, or voltage-drop explanation
- any current-sharing or `per pin` aggregation claim
- any reliability, life, qualification, field-failure, or manufacturability claim
- any statement that all `components` generically have one comparable current-rating field
- any regulator-specific current-rating claim
- any trace-width, copper-weight, power-plane, via, DFM, DFT, simulation, or production consequence claim
- any named connector-family numeric claim unless the exact family page or datasheet is the cited authority

# Residual Gaps

- No official regulator-owner source was recovered here, so the draft's `regulator or connector` wording is still too broad.
- No single official cross-vendor source was found that states the final prose exactly as `calculate current, then choose any part with adequate rating`; that selector sentence is still a conservative synthesis from TE's selection prompt plus official rating fields.
- No official-source basis was recovered for safety margins, derating practice, thermal behavior, current sharing, or broad manufacturability/reliability framing.
- If future copy wants named connector families, exact amp values, or application-specific conditions, each family will need its own product-page or datasheet citation.

# Promotion Judgment

- `connector current-rating selection` is promotable only in a very narrow form: once current is known, check the connector manufacturer's published current rating or nominal current on the official product page or datasheet.
- `component current ratings` is only partially promotable if rewritten narrowly to a named current-rated component class or to `current-rated electromechanical components` with a component-owner source like the cited TE contactor page.
- The draft's broader sentence about `components that safely handle that current plus a safety margin` remains blocked.
- Overall readout: `partial promotion only`, with the safest unlocked lane being `check official manufacturer current-rating fields after current is known`.

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-64c-2025-11-10-connector-rating-official-source-scout.md`

# H1 Material Numeric Coverage Closeout Summary

Date: 2026-04-25

## Result

`H1` is complete.

This means the planned exact-product material recovery program for the current high-numeric-density target rows is now closed.

It does **not** mean every material branch is numerically open for reuse.

## What H1 Finished

- exact-product mainstream / high-Tg `FR-4` anchors across `Isola`, `ITEQ`, `Shengyi`, and `Panasonic`
- exact-product digital low-loss / very-low-loss / ultra-low-loss anchors across the currently targeted `Isola`, `ITEQ`, and `Panasonic` rows
- exact-product RF / hybrid anchors across the targeted `Rogers`, `Ventec`, and `AGC` rows already prioritized in `H1`
- branch normalization for `Panasonic`, `ITEQ`, and `Arlon`
- a reusable cross-vendor digital-material normalization layer for guarded high-speed digital writing

## What H1 Deliberately Did Not Unlock

- generic `FR-4` rows remain `gap_control`
- `Taconic` remains `gap_control`
- generic `RCC / FRCC / bondply / low-flow / no-flow / build-up` branches remain `gap_control`
- generic rigid-flex material branches such as `polyimide / Kapton / UPILEX / adhesiveless flex` remain `gap_control`
- narrow exact-product exceptions such as `RO4450F`, `RO4460G2`, `R-FR10`, `R-F705S`, and `VT-4B7` do not upgrade their whole branch
- `IMS` remains only partially open at exact-product material-constant level; board-level thermal-outcome claims remain held

## Closeout Rule

Use this rule going forward:

`H1 completion closes the planned exact-product recovery program for the current target rows; it does not release Taconic, generic RCC/FRCC/build-up materials, generic rigid-flex material branches, generic FR-4 averages, or boundary-only exceptions from explicit gap_control.`

## Handoff

- `H2` should now take over fabrication capability numerics, not material-source recovery
- future material work after `H1` should be limited to:
  - factual corrections
  - newly discovered official exact-product sources worth separate admission
  - selector / normalization hygiene that does not reopen held branches

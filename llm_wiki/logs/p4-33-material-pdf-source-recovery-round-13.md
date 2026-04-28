# P4-33 Material PDF Source Recovery Round 13

Date: 2026-04-28
Status: `source_backed_fact_layer_partial`

## Purpose

Start the TUC material PDF lane by upgrading three high-confidence TUC local PDF rows after official TUC product-page checks, scout download-endpoint binding, and direct PDF text extraction.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/tu-901_datasheet.pdf`
- `/code/blogs/tmps/materias_pdf/tu-787 lk_datasheet.pdf`
- `/code/blogs/tmps/materias_pdf/tu-872 lk_datasheet.pdf`
- `https://www.tuc.com.tw/zh-tw/products-detail/id/40`
- `https://www.tuc.com.tw/zh-tw/products-detail/id/10`
- `https://www.tuc.com.tw/en-us/products-detail/id/1`
- scout-observed dynamic download endpoints:
  - `https://www.tuc.com.tw/_run.php?id=192&work=down_member`
  - `https://www.tuc.com.tw/_run.php?id=51&work=down_member`
  - `https://www.tuc.com.tw/_run.php?id=3&work=down_member`

## Added Source Records

- `tuc-tu-901-datasheet-page`
- `tuc-tu-787-lk-datasheet-page`
- `tuc-tu-872-lk-datasheet-page`

## Added Fact Cards

- `materials-tuc-tu-901`
- `materials-tuc-tu-787-lk`
- `materials-tuc-tu-872-lk`

## Source-Backed Data Unlocked

- TUC `TU-901`: source-scoped Tg 260 C halogen-free laminate / prepreg values, including Tg, Td, CTE, thermal stress, T260 / T288 / T300, `RC70%` Dk / Df at `10 GHz`, impedance-simulation Dk as a separate non-measured context row, and guarded availability / QPL wording.
- TUC `TU-787 LK`: source-scoped halogen-free low-Dk / low-Df laminate / prepreg values, including Tg, Td, CTE, thermal stress, T-288, `RC75` Dk / Df at `1 GHz` and `10 GHz`, and guarded mobile / telecom application context.
- TUC `TU-872 LK`: source-scoped modified-epoxy FR-4 low-Dk / low-Df laminate / prepreg values, including Tg by DMA / DSC / TMA, Td, CTE, thermal stress, T260 / T288 / T300, `RC50%` Dk / Df at `1 GHz`, `5 GHz`, and `10 GHz`, and guarded QPL / high-speed application context.

## Still Blocked

- Finished-board insertion loss, impedance, SI, RF, backplane, server, telecom, base-station, substrate, HDI, ELIC, aerospace, military, harsh-environment, mobile-device, or office-router performance claims.
- Stackup default, trace-length, channel budget, CAF lifetime, lead-free assembly success, high-layer reliability, qualification, or released-lot acceptance for a specific stackup.
- Supplier process windows, build capability, certification, stock, price, MOQ, lead time, yield, or production approval.
- TUC `TU-865S` remains pending explicit preliminary-revision matching before numeric extraction.
- `SCGA-500 GF220` remains blocked pending an exact live official TUC page or official download URL.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `three TUC material rows only`
- cumulative P4-33 material PDF source-backed upgrade: `20` AGC exact-product rows plus `5` Rogers exact-product rows plus `13` Ventec exact-product rows plus `4` Shengyi exact-product rows plus `3` TUC exact-product rows
- next lane: TUC `TU-865S` only after preliminary-revision binding, more TUC verified rows, Ventec product-form-specific rows, AGC TSM / TLX / TLY / TLE / TLC / TLF / RF tails, or selector wiki aggregation for recovered rows.

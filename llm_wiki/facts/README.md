# Fact Cards

本目录存放原子事实卡片。

原则：

- 一张卡片一个主题
- 卡片只表达经来源支持的事实
- 推断和判断要单独标注
- 动态数据必须标记刷新要求

建议子目录：

- `materials/`
- `methods/`
- `standards/`
- `compliance/`
- `market/`

## Current Coverage Snapshot

As of 2026-04-24, the fact layer includes:

- Official-source material facts for Rogers, Isola, Panasonic Megtron, Ventec, and AGC RF/high-speed families.
- Site-mentioned material baseline coverage for APT/HIL public non-blog pages, including Arlon N-series product identity anchors, Isola, Panasonic MEGTRON, Rogers bondply, Taconic gap-control, FR-4, PTFE/Teflon, IMS, ceramic/alumina/AlN, ABF, BT, flex-material, and LCP class-level anchors.
- Conservative standards and compliance facts for IPC metadata, IPC assembly / HDI / electrical-test / coating metadata, 3GPP indexing, RoHS, REACH, and SVHC handling.
- Internal-support and official-support method facts from `frontendAPT`, `frontendHIL`, IPC, material vendors, solder vendors, coating vendors, and RF semiconductor vendors covering RF stackups, PTFE processing, finish zoning, validation, drilling/backdrill, backplane integration, PCBA process/test gates, MCPCB/IMS, reflow profiling, conformal coating, and phased-array context.
- Internal-support material facts covering APT material-family pages for Arlon, Isola, Megtron, Taconic, Teflon/PTFE, spread-glass FR-4, and controlled-impedance stackups.

Internal fact cards are not official manufacturer or standards claims. Use them as capability and process-context support, then attach official sources or live-refresh checks before publishing numeric customer-facing claims.

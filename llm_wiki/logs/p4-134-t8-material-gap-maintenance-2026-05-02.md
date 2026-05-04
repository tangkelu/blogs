# P4-134 T8 Material Gap Maintenance

**Date**: 2026-05-02
**Scope**: T8 材料基础后续的深度缺口跟踪
**Source**: P4-125 roadmap continuation from T8 materials baseline

---

## Executive Summary

从 **T8 完成的材料基础** 出发，执行 **T18-1/T18-2 材料深度补全** 的状态检查。当前 Taconic 和 Arlon RF/PTFE 家族仍然无法从官方渠道恢复，保持 `source_gap` 状态。Flex、铜箔、陶瓷平台已有较好的 exact-product 覆盖。

---

## Material Gap Status (T8 → T18)

### 1. Taconic RF Laminate ⏸️ HOLD

| Family | Status | Reason |
|--------|--------|--------|
| RF | `source_gap` | 4taconic.com 仅展示工业PTFE织物/胶带 |
| TLY | `source_gap` | 无RF层压板产品页面 |
| TLX | `source_gap` | 无数据表锚点 |
| TLC | `source_gap` | 无法从官方渠道恢复 |
| TLE | `source_gap` | 无法从官方渠道恢复 |

**Fact Card**: `materials-taconic-official-source-coverage-gap`
**Action**: 保持 `must_refresh: true`，等待 Taconic 官方产品页面重新上线

---

### 2. Arlon RF/PTFE ⏸️ HOLD

| Family | Status | Reason |
|--------|--------|--------|
| CLTE-XT | `source_gap` | 不在当前官方产品sitemap中 |
| TC350 | `source_gap` | 无法恢复 |
| AD250 | `source_gap` | 无法恢复 |
| AD255 | `source_gap` | 无法恢复 |
| AD300 | `source_gap` | 无法恢复 |
| CuClad | `source_gap` | 无法恢复 |
| DiClad | `source_gap` | 无法恢复 |

**已覆盖**: N-series (33N, 35N, 37N, 45N, 45NK), 55NT, 84N, 85N, 85NT, 86HP
**Fact Card**: `materials-arlon-rf-ptfe-current-site-gap`
**Action**: 保持 `must_refresh: true`，等待 Arlon 官方重新发布

---

### 3. Flex Materials ✅ COVERED

| Product | Owner | Status |
|---------|-------|--------|
| UPILEX-S | UBE | ✅ exact-product |
| Kapton HN | DuPont | ✅ exact-product |
| 85N | Arlon | ✅ exact-product |
| 85NT | Arlon | ✅ exact-product |
| N7000-3F | AGC | ✅ exact-product |
| R-F705S | Panasonic | ✅ exact-product (LCP) |

**Fact Card**: `materials-flex-exact-product-anchor-map`
**Gap**: 通用 polyimide/LCP/adhesiveless flex 的数值支持仍不均衡

---

### 4. Copper Foil ✅ COVERED

| Product | Owner | Type | Status |
|---------|-------|------|--------|
| JTCS-P1 | JX | ED rigid | ✅ exact-product |
| JDLC | JX | ED rigid | ✅ exact-product |
| HLP-II | JX | ED rigid | ✅ exact-product |
| JXEFL-V2 | JX | ED FPC | ✅ exact-product |
| JXEFL-BHM | JX | ED FPC | ✅ exact-product |
| FZ-WS | Furukawa | ED/VLP | ✅ exact-product |
| GTS-STD | Furukawa | ED | ✅ exact-product |
| GTS-MP | Furukawa | ED | ✅ exact-product |

**Fact Card**: `materials-copper-foil-exact-product-profile-anchor-map`
**Gap**: 供应商中性的粗糙度表、RF损耗排名仍被阻止

---

### 5. Ceramic Platform ✅ COVERED

| Platform | Source | Status |
|----------|--------|--------|
| LTCC | KYOCERA | ✅ official anchor |
| Thin-film ceramic | KYOCERA | ✅ official anchor |
| Ceramic substrates | CeramTec | ✅ official anchor |
| AlN | MARUWA | ✅ official anchor |
| IMS | Ventec | ✅ official anchor |
| DBC/AMB/DPC | MARUWA | ✅ family names only |

**Fact Card**: `materials-ceramic-platform-anchor-map`
**Gap**: DBC/AMB/DPC 的热/电/厚度数值仍稀疏

---

## Recommended Next Actions

### Short-term (保持观察)

1. **Taconic**: 每月检查 4taconic.com 是否恢复RF层压板产品页面
2. **Arlon**: 每季度检查 arlonemd.com 是否重新发布 CLTE-XT/TC350/AD系列/CuClad/DiClad

### Medium-term (可探索)

3. **DBC/AMB/DPC**: 寻找 KYOCERA/MARUWA 的产品级数据表补充热/电参数
4. **Flex数值**: 评估是否需要从 85N/85NT/N7000-3F 数据表提取更多弯曲/可靠性参数

### Hold Boundary (保持阻止)

- ❌ 不从第三方镜像恢复 Taconic/Arlon 数据表
- ❌ 不创建供应商中性的铜箔粗糙度排名
- ❌ 不将 DBC/AMB 泛化为通用陶瓷平台能力

---

## Related Documents

| Document | Purpose |
|----------|---------|
| `facts/materials/taconic-official-source-coverage-gap.md` | Taconic 缺口跟踪 |
| `facts/materials/arlon-rf-ptfe-current-site-gap.md` | Arlon 缺口跟踪 |
| `facts/materials/flex-exact-product-anchor-map.md` | Flex 已覆盖锚点 |
| `facts/materials/copper-foil-exact-product-profile-anchor-map.md` | 铜箔已覆盖锚点 |
| `facts/materials/ceramic-platform-anchor-map.md` | 陶瓷平台已覆盖锚点 |

---

*This log follows the P4-125 roadmap and T8 material foundation. Updates require new official source discovery.*

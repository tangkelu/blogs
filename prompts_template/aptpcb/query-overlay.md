# APTPCB Query Overlay

把本文件叠加到 `../shared/query.md` 上使用。

## 站点承接优先级

1. `pcb/`
2. `pcba/`
3. `capabilities/`
4. `materials/`
5. `industries/`
6. `resources/`
7. `tools/`
8. `quote/`

## 内链策略

- 单篇建议 `4-6` 个内链
- 至少 `2-3` 个指向 `pcb/`、`pcba/`、`capabilities/` 或 `materials/`
- 对专题强的文章，允许增加 `industries/` 与 `resources/dfm-guidelines`

## APTPCB 特有承接逻辑

- 材料类主题优先指向 `materials/`
- 行业应用类主题优先指向 `industries/`
- 工艺与制造能力类主题优先指向 `capabilities/` 或 `pcb/`
- 装配与测试类主题优先指向 `pcba/`
- 工程支持类主题可接 `resources/` 与工具页

## APTPCB CTA 规则

- 当前可公开复用的联系邮箱是 `sales@aptpcb.com`
- 当前可公开复用的承接页是 `https://aptpcb.com/en/quote/`
- 当前可公开复用的工程响应表述是“DFM feedback within 24 hours”，但只能用于 `commercial` 模式或已明确进入报价 / quick-turn / DFM 商业动作的页面
- CTA 必须由 `page_intent_mode` 决定，不能把所有 Query 文章默认写成“工程问题场景 + 提交资料 + 24 小时 DFM 反馈”

| `page_intent_mode` | CTA mode | 必须写什么 | 禁止写法 |
| --- | --- | --- | --- |
| `knowledge` | `reference CTA` | 给出 `2-4` 个下一步阅读路径，优先指向定义、材料、capability、industry 或 DFM guideline 页面；只说明读者下一步应补哪类背景知识 | 不写 `/en/quote/` 主 CTA，不写 `24 hours`，不写“send your files”式收口 |
| `review` | `review CTA` | 说明读者应准备哪套 review package，例如 `Gerber`、`ODB++`、`stackup`、目标阻抗、材料限制、测试要求、应用约束；说明 APTPCB 可做 DFM / stackup / assembly / test-access review | 不默认承诺 SLA，不把 review CTA 改写成直接报价，不要求所有资料都必须走 quote page |
| `handoff` | `handoff CTA` | 说明 release / handoff package 的输入边界，例如 `Gerber`、`ODB++`、`BOM`、坐标文件、装配图、测试要求、polarity / Pin 1 / rotation note、结构 / enclosure 条件；强调交接完整性和误做风险 | 不写成泛泛“联系我们”，不把资料交接问题强行改成价格问题 |
| `commercial` | `quote CTA` | 可以使用 `https://aptpcb.com/en/quote/`、`sales@aptpcb.com` 和 “DFM feedback within 24 hours”；说明报价或 quick-turn 判断需要哪些输入 | 不能缺少资料包定义，不能只写品牌口号或单独裸链 |

- 如果输入没有显式提供 `page_intent_mode`，先按搜索意图推断：定义 / 原理 / 选型背景为 `knowledge`；DFM / NPI / release readiness 为 `review`；Gerber / ODB++ / BOM / test handoff 为 `handoff`；quote / cost / lead time / quick-turn / supplier selection 为 `commercial`
- 同一批 APTPCB Query 文章不得连续复用同一种 CTA 句式；至少改变 opening pain、资料包顺序、承接动词和收尾链接结构
- 允许在主 CTA 后补 `2-4` 个相关链接，但这些链接只能服务当前 CTA mode，不应把 `knowledge` 文章硬拉到报价页

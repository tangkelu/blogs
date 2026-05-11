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

- APTPCB 的 Query 文章结尾 CTA，优先写成“工程问题场景 + 提交资料 + 24 小时 DFM 反馈”
- 当前可公开复用的联系邮箱是 `sales@aptpcb.com`
- 当前可公开复用的承接页是 `https://aptpcb.com/en/quote/`
- 当前可公开复用的工程响应表述是“DFM feedback within 24 hours”
- 可以自然写入的资料类型包括：`Gerber`、`ODB++`、`stackup`、`BOM`、目标阻抗、测试要求、材料限制、应用场景、结构 / enclosure 条件
- 不要每篇都复制同一句 CTA；必须根据文章主题改写问题场景
- 允许在主 CTA 后补 `2-4` 个相关链接，但这些链接只能作为辅助，不应盖过主 CTA

# Legacy Prompt Directory Cleanup Plan

本文件用于给 `/code/blogs/prompts` 与 `/code/blogs/prompts_aptpcb` 做最终收口。

目标不是“看到旧文件就全删”，而是：

- 确认当前唯一生产入口是 `prompts_template`
- 确认哪些旧资产已经被吸收
- 明确哪些目录可直接删除
- 明确哪些目录更适合先归档再删除

## 一、当前状态

当前目录体量：

- `/code/blogs/prompts_template`：约 204K
- `/code/blogs/prompts`：约 4.2M
- `/code/blogs/prompts_aptpcb`：约 12M

当前生产脚本实际读取的是：

- `prompts_template/shared/query.md`
- `prompts_template/shared/pillar.md`
- `prompts_template/hilpcb/*`
- `prompts_template/aptpcb/*`

因此，`prompts` 与 `prompts_aptpcb` 已不在现行生产链路中。

## 二、已经完成吸收的旧资产

以下内容已经吸收到 `prompts_template`，不需要继续依赖旧目录：

- 参数事实库标准：
  - `shared/fact-seed-repository-standard.md`
  - `shared/fact-seed-repository-template.csv`
- APT 历史关键词映射参考：
  - `aptpcb/legacy-keyword-content-map.md`
- APT 站内图片资源索引：
  - `aptpcb/assets-image-catalog.md`
- Query / Pillar 主模板收敛规则
- `story / playbook / comparison / application / capability` 的降级与模块化规则

## 三、处理原则

### 1. 可直接删除

满足以下条件的旧目录或文件，可直接删除：

- 不被当前脚本读取
- 内容已被 `prompts_template` 吸收
- 只剩历史模板变体，没有额外资产价值

### 2. 先归档再删除

满足以下条件的目录，建议先归档：

- 仍有历史追溯价值
- 还承载旧关键词映射、旧实验模板、旧生成思路
- 团队短期内可能还会回看

### 3. 必须保留在新体系中

必须保留的不是旧目录本身，而是已经迁入 `prompts_template` 的“精华资产”：

- Shared 方法论
- Query / Pillar 生产提示词
- 站点 overlay
- 内链策略与链接池
- 事实参数库标准
- 关键词集群与数据组织标准

## 四、建议动作清单

### A. `/code/blogs/prompts`

建议结论：

- 可直接删除

理由：

- 当前生产链路完全不读取本目录
- 其中真正还有价值的内容，已经提炼进入 `prompts_template`
- 剩余内容以 v1/v2/v3/v4 行业模板、v5 参数库旧形态为主
- 继续保留只会制造“旧模板也能继续用”的误判

删除前最后确认项：

- `fact-seed-repository` 的字段与规则已迁入 `prompts_template/shared/`
- 不再需要回看旧 HIL 系列行业模板写法

### B. `/code/blogs/prompts_aptpcb`

建议结论：

- 先归档，再删除

理由：

- 目录更大，历史阶段更多
- 含 v5 / v6 / `_legacy` / `plan_templates` / `temp_test`
- 虽然已退出生产链路，但仍保留较多历史关键词编排、模板实验和迁移痕迹
- 已经在关键 README 和 `story/playbook` 模板头部加了 archive 标记，误用风险已显著下降

建议归档范围：

- `blogs_prompt_v5/`
- `blogs_prompt_v6/`
- `_legacy/`
- `plan_templates/`
- `temp_test/`

建议归档方式：

- 移到单独 archive 目录
- 或打包成只读备份
- 然后从主工作目录移除

## 五、`story / playbook` 的最终定位

旧目录里的 `story` 与 `playbook` 不应继续作为一级模板保留。

现在的最终定位是：

- `playbook`：只保留采购 / RFQ / 验收 / 供应商评估模块能力
- `story`：只保留少量品牌叙事、案例复盘、复杂 trade-off 解释写法

换句话说：

- 保留“能力”
- 不保留“旧模板体系”

## 六、推荐执行顺序

1. 继续把所有新生产都锁定在 `prompts_template`
2. 备份 `prompts_aptpcb`
3. 从主工作区移除 `prompts_aptpcb`
4. 直接删除 `prompts`
5. 清理仓库里残留的旧目录说明与脚本注释

## 七、最终建议

如果你现在要收口：

- `/code/blogs/prompts`：可以删
- `/code/blogs/prompts_aptpcb`：建议先归档，确认无追溯需求后再删

后续所有博客生产、模板演进、规则沉淀，都只应进入：

- `/code/blogs/prompts_template`

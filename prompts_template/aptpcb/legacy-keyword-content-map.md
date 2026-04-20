# APTPCB Legacy Keyword Content Map

本文件吸收自旧目录：

- `prompts_aptpcb/v6_content_map.md`

它不是生产提示词，也不是主模板。  
它的作用只有两个：

- 记录 APTPCB 历史关键词资产与文件名映射
- 给后续 topic cluster 补齐、去重、迁移提供参考

## 使用原则

1. 只把它当作历史资产清单，不把它当作当前执行模板。
2. 只有当某个关键词：
   - 符合当前 `Query / Pillar` 体系
   - 与站点现有承接页匹配
   - 能拿到 evidence pack
   才值得继续生产。
3. 看到旧 map 中的关键词，不代表都值得保留。

## 典型可借鉴方向

旧 v6 map 真正有价值的，不是模板结构，而是这些内容组织方式：

- 制造 / 成本 / lead time
- PCBA / 测试 / 质量
- Flex / rigid-flex
- High-speed / impedance
- Materials / thermal
- Reliability / compliance
- 行业专题簇：
  - Data center / AI
  - 5G / RF / mmWave
  - Automotive
  - Power / Energy
  - Medical
  - Industrial / Robotics

## 当前建议

如果后续需要继续整理 APTPCB 的关键词资产，优先把旧 map 中的信息转成以下几类文档，而不是继续维护旧版大表：

- `shared/topic-cluster-roadmap.md`
- `shared/keyword-cluster-design-standard.md`
- `aptpcb/site-content-map.md`

## 原始文件位置

完整历史文件仍可参考：

- `/code/blogs/prompts_aptpcb/v6_content_map.md`

后续如果要彻底删除旧目录，应先确认需要保留的关键词簇已迁入 `prompts_template` 的 cluster 文档。

# Fact Seed Repository Standard

本文件把旧 `prompts/blogs_prompt_v5/fact-seed-repository/` 中仍然有执行价值的规则，收敛为 `prompts_template` 的正式共享标准。

目标只有一个：

- 建立博客生产时的参数与事实“单一真理来源”

它服务于：

- `shared/evidence-pack-template.md`
- `shared/query.md`
- `shared/pillar.md`

它不替代 evidence pack；它是 evidence pack 背后的参数底座。

## 一、为什么需要 Fact Seed Repository

技术博客最大的风险不是句子写得不顺，而是：

- 参数漂移
- 跨文口径冲突
- 站点能力与行业事实混写
- 大模型在缺数时自行猜值

因此，所有会进入正文的关键数字、能力上限、材料参数、标准参数口径，都应尽量先进入 Fact Seed Repository。

## 二、使用范围

适用于以下类型的数据：

- 材料参数
- 已公开的站点 capability 参数
- 官方 datasheet / 标准中的数值
- 已验证的工艺窗口
- 需要跨多篇文章保持一致的参数口径

不适用于：

- 没有来源的经验值
- 尚未确认的内部估算
- 项目定制结果
- 不能对外发布的内部工艺细节

## 三、生产规则

1. 生产提示词只能引用 `status=verified` 的参数行。
2. 每一个数值型参数都必须带：
   - `source_type`
   - `source_ref`
   - `version`
3. 如果没有可用的 `verified` 参数：
   - 不允许模型猜值
   - 必须改写为条件判断、趋势判断，或在内部流程里标记 `DATA_GAP`
4. HILPCB、APTPCB 与 Shared 的参数域必须分开维护。
5. 参数变更必须升版本，并记录变更时间与复核责任。

## 四、推荐字段

最小字段集合如下：

| 字段 | 作用 |
| --- | --- |
| `record_id` | 唯一编号 |
| `site_scope` | `HILPCB` / `APTPCB` / `Shared` |
| `category` | 大类，如 Material / Factory Capability / Standard |
| `sub_category` | 子类，如 Rogers / HDI / FR4 |
| `param_key` | 参数名 |
| `param_value` | 参数值 |
| `unit` | 单位 |
| `condition_or_freq` | 条件、频段、温度、测试前提 |
| `test_method` | 测试方法或引用方法 |
| `source_type` | 来源类型 |
| `source_ref` | 来源引用 |
| `effective_date` | 生效日期 |
| `version` | 版本号 |
| `status` | `draft` / `verified` / `deprecated` |
| `owner` | 责任人 |
| `last_verified_at` | 最近复核时间 |
| `notes` | 补充说明 |

## 五、状态语义

### `draft`

- 已录入
- 可能有来源
- 还不能进入生产正文

### `verified`

- 已完成复核
- 来源和口径已确认
- 可进入生产提示词和博客正文

### `deprecated`

- 历史参数
- 不再推荐使用
- 仅保留追溯价值

## 六、与 prompts_template 的关系

后续执行顺序建议为：

1. 先准备 topic / keyword
2. 再准备 evidence pack
3. 再从 Fact Seed Repository 拉取可用的 `verified` 参数
4. 如果没有参数：
   - 不写数字
   - 或触发 `DATA_GAP`
5. 再执行 `query` 或 `pillar`

## 七、现阶段最低落地要求

在完整参数库尚未成形前，至少先做到：

- 共享一个统一字段结构
- 只允许 `verified` 进入正文
- 站点 capability 参数分域管理
- 缺失时不猜值

## 八、兼容说明

本文件吸收自旧目录：

- `prompts/blogs_prompt_v5/fact-seed-repository/README.md`
- `prompts/blogs_prompt_v5/fact-seed-repository/fact_seed_repository_template.csv`
- `prompts/blogs_prompt_v5/design.md` 中关于参数库、版本与 `DATA_GAP` 的规则

旧目录后续只保留归档价值，不再作为执行入口。

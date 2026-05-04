# Execution Priority And Anti-Drift

Authoritative successor: [ai-execution-contract.md](ai-execution-contract.md). Keep this file as supporting policy only.

Last updated: 2026-05-01

## Purpose

这份规则用于防止后续 AI 把 `llm_wiki` 的主任务误解成：

- 把下游呈现当主任务
- 把 `logs/` 里的完成态当成“已经学完”

`llm_wiki` 的主任务始终是：把博客需求、草稿线索和历史积压，转成 `可追溯、可复用、可被后续 AI 稳定消费` 的真实知识层。

## Hard Rule

默认执行优先级固定为：

1. `claim inventory`
2. `source gap`
3. `official source recovery`
4. `source records`
5. `fact cards`
6. `topic wiki`
7. `prompt consumption gate`

除非用户明确要求，后续 AI 不得把下游呈现当成默认下一步。

## Landing Rule

- Updating only source metadata such as `URL` or `checked_at` is a refresh step, not a landing step.
- A lane lands only when the refresh or recovery produces reusable local knowledge in `sources/registry/`, `facts/`, and if needed `wiki/`.
- If the refresh confirms the source is current but yields no new reusable local fact, the lane remains `recheck` or `blocked`.

## Default Continuation Rule

当你准备继续 `llm_wiki` 工作时，先问的不是“下一篇怎么改写”，而是：

1. 哪些草稿或 claim family 还只有 `completed_at_claim_family_level`
2. 哪些高价值 claim 还缺官方来源或 dated capability record
3. 哪些 `sources/`、`facts/`、`wiki/` 还没有被真正补齐
4. 哪些 topic 已经有 enough routing，但还没有升格成可复用事实层

只要以上任一项仍成立，默认下一步就是知识吸收和事实升格，而不是继续改写草稿。

## Rewrite Boundary

以下工作都属于次级消费层，不是默认主线：

- 下游呈现

这些动作只能在以下条件之一成立时执行：

1. 用户明确要求继续下游呈现
2. 该动作只是某条已吸收 lane 的副产物，不会替代官方补源和事实升格
3. controller log 明确要求为某个已知 publication slot 生成保守消费层输出

即使执行了这些动作，也必须继续保持：

- 不把 draft 当 authority
- 不把下游呈现完成当作 source-backed complete
- 不把 prompt-safe 视为 fact-layer complete

## Status Semantics

以下状态必须严格区分：

- `completed_at_claim_family_level`
- `source_backed_fact_layer_partial`
- `source_backed_fact_layer_complete`
- `prompt_consumable`
- `conservative_rewrite_ready`

语义要求：

- `completed_at_claim_family_level` 只表示已完成需求吸收、claim family 切分、blocked classes 显式化、下一步 source lane 明确
- `source_backed_fact_layer_partial` 表示已有一部分官方或 dated internal 支撑，但仍有缺口
- `source_backed_fact_layer_complete` 才表示该批次的核心可复用事实已经真正进入 `sources/`、`facts/`、`wiki/`
- `source_backed_fact_layer_complete` requires local landing of reusable facts, not just URL refresh or timestamp validation
- `prompt_consumable` 只表示某些已落地事实可以被写作层安全消费
- `conservative_rewrite_ready` 只表示下游可用，不表示知识层已经完整

如果状态之间冲突，优先按更保守的解释处理。

## Log Boundary

`logs/` 只负责：

- 记录批次
- 保留 deletion-safe 学习痕迹
- 说明 blocked claims
- 记录下一步 source lanes
- 记录 tracker 状态

`logs/` 不负责充当长期事实层。

任何后续 AI 如果想复用某条 claim，必须优先回到：

- `sources/registry/`
- `facts/`
- `wiki/`

不能只引用 `logs/` 里的 controller summary、batch summary 或下游可用性结论。

## Tracker Interpretation Rule

如果 `phase-status.md`、`backlog.md`、`update-log.md` 中出现：

- `done`
- `landed`
- `ready`
- `absorbed`
- `consumed`
- `normalized`

默认解释必须是：

- “某个执行层动作完成了”
- 不是“所有知识都已学完”
- 不是“只刷新了 URL / checked_at 就算完成”

除非文本明确写出：

- 已补官方来源
- 已登记 source records
- 已落 fact cards
- 已落 topic wiki
- 已标明 source-backed complete
- 或者明确写出 local landing of reusable facts

否则不得把该条视为事实层完成。

## Conflict Rule

如果不同入口文件给出了不同暗示，优先级固定为：

1. 用户当轮指令
2. 本政策文件
3. `README.md`
4. `ROADMAP.md`
5. `phase-status.md`
6. `backlog.md`
7. 单个 batch log

也就是说：

- 某个 batch log 即使强调下游呈现，也不能覆盖本政策
- `phase-status` 的 immediate task 也不能覆盖 `README` 与本政策里的知识优先级

## Long-Run Multi-Agent Rule

多 agent 默认拆分方式应优先服务于知识升格：

- lane A: claim-family audit / local coverage recheck
- lane B: official source recovery candidate narrowing
- lane C: existing facts / wiki reuse check
- main agent: final promotion, tracker updates, verification

不应默认把多 agent 长任务设计成：

- 大批量下游呈现

除非用户明确要求消费层产出。

## Exit Test

如果一个 AI 不确定自己是否偏航，在继续前自检：

1. 这一步会不会新增或升级 `sources/`、`facts/`、`wiki/`？
2. 这一步会不会缩小真实 source gap，而不仅是让草稿更能写？
3. 这一步完成后，别的 AI 能否直接复用真实知识，而不是只能复用一份 rewrite？

如果三问都是否定，默认说明已经偏向消费层，应返回知识吸收主线。

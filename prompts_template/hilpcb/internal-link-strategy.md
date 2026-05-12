# HILPCB Internal Link Strategy

HILPCB 的技术博客内链默认遵循“产品页 / 服务页优先，博客页次之”的原则。

## 原则

- 产品页优先
- 服务页和工具页其次
- 博客页只做辅助
- 内链分散分布，不要堆在结尾

## 推荐比例

- 40% 产品页
- 30% 服务页 / 工具页
- 20% 相关博客
- 10% `quote/`

## 推荐位置

- 开头：1 个
- 中段：2-3 个
- FAQ / 结尾：1-2 个

## 分布要求

- 不要把 3 个以上链接集中在同一段
- 同一目标类型不要连续堆叠
- 开头和中段优先产品 / 服务 / 工具页
- FAQ / 结尾可补 1 个博客页，但不能替代主承接

## 主题优先承接

### 标准 1-2 层 / 低密度 / 成本敏感 PCB

- `products/single-double-layer-pcb`
- `products/fr4-pcb`
- `services/pcb-prototype`
- `quote/`

使用场景：

- 关键词包含 `single layer PCB`、`double layer PCB`、`2 layer PCB`、`single sided PCB`、`double sided PCB`
- 内容讨论简单控制板、LED driver、sensor board、power supply、low-density routing、cost-sensitive prototype
- 文章需要解释“什么时候 1-2 层够用，什么时候升级到 multilayer/HDI”

规则：

- 这类主题开头或第一个相关技术段优先链接到 `products/single-double-layer-pcb`
- 不要把这类意图默认承接到 `products/fr4-pcb`、`products/multilayer-pcb` 或博客页
- 如涉及能力参数，优先查 `llm_wiki/facts/processes/hil-single-double-layer-capability-specs.md`
- 当前稳定口径：1-2 layers, 24-48h quick-turn, 150/150 μm standard trace/space, 75/75 μm advanced trace/space, FR-4 Tg 130-170°C

### 高速 / 阻抗 / SI

- `products/high-speed-pcb`
- `products/high-frequency-pcb`
- `products/backplane-pcb`
- `tools/impedance-calculator`

### HDI / Microvia / Fine Pitch

- `products/hdi-pcb`
- `products/multilayer-pcb`
- `services/pcb-prototype`

规则：

- 关键词包含 `HDI PCB`、`microvia`、`blind via`、`buried via`、`VIPPO`、`via-in-pad`、`fine-pitch BGA` 时，优先承接到 `products/hdi-pcb`
- 如果文章只是普通多层板、plane/routing layer 增加，不要默认落到 HDI；优先 `products/multilayer-pcb`
- 如果主问题是高速损耗、协议、阻抗，而不是微孔/封装逃逸，优先 `products/high-speed-pcb`

### Rigid-Flex / Flex

- `products/rigid-flex-pcb`
- `products/flex-pcb`
- `products/box-build-assembly`

### PCBA / BOM / 缺陷 / 测试

- `products/turnkey-assembly`
- `products/smt-assembly`
- `products/through-hole-assembly`
- `products/small-batch-assembly`
- `products/large-volume-assembly`

规则：

- BOM sourcing、AVL、EOL、alternates、procurement ownership、component traceability 优先承接到 `products/turnkey-assembly`
- connector、terminal、relay、transformer、press-fit、wave solder、selective solder、mixed-technology THT 优先承接到 `products/through-hole-assembly`
- NPI、first article、prototype PCBA、pilot build 优先承接到 `products/small-batch-assembly`
- repeat production、mass production、SPC、MES traceability、pilot-to-volume ramp、forecast-driven PCBA 优先承接到 `products/large-volume-assembly`
- enclosure、harness、firmware loading、system test、pack-out 优先承接到 `products/box-build-assembly`

### 材料 / 表面处理 / 热管理

- `products/rogers-pcb`
- `products/high-tg-pcb`
- `products/teflon-pcb`
- `services/pcb-surface-finish`

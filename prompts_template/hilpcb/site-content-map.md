# HILPCB Site Content Map

基于当前站点结构整理的博客承接地图。

## 产品页

- `products/single-double-layer-pcb`
- `products/fr4-pcb`
- `products/multilayer-pcb`
- `products/heavy-copper-pcb`
- `products/flex-pcb`
- `products/high-tg-pcb`
- `products/hdi-pcb`
- `products/rigid-flex-pcb`
- `products/high-speed-pcb`
- `products/ic-substrate-pcb`
- `products/high-frequency-pcb`
- `products/backplane-pcb`
- `products/metal-core-pcb`
- `products/rogers-pcb`
- `products/ceramic-pcb`
- `products/teflon-pcb`
- `products/high-thermal-pcb`
- `products/halogen-free-pcb`
- `products/turnkey-assembly`
- `products/smt-assembly`
- `products/through-hole-assembly`
- `products/box-build-assembly`
- `products/large-volume-assembly`
- `products/small-batch-assembly`

## 服务页

- `services/pcb-prototype`
- `services/quick-turn-pcb`
- `services/pcb-surface-finish`

## 工具页

- `tools/impedance-calculator`
- `tools/gerber-viewer`
- `tools/pcb-viewer`
- `tools/bom-viewer`
- `tools/3d-viewer`
- `tools/circuit-simulator`

## 博客承接原则

- 高速 / 阻抗优先接产品 + 工具
- 1-2 层 / 单双面 / 简单 FR-4 / low-density prototype 优先接 `products/single-double-layer-pcb`
- HDI / microvia / VIPPO / fine-pitch BGA 优先接 `products/hdi-pcb`
- 组装 / DFT / BOM 风险优先接组装产品页
- BOM sourcing / AVL / EOL / alternates / turnkey PCBA 优先接 `products/turnkey-assembly`
- connector / terminal / transformer / press-fit / wave-selective solder 优先接 `products/through-hole-assembly`
- repeat production / SPC / MES / volume ramp 优先接 `products/large-volume-assembly`
- 材料 / 表面处理优先接材料产品页 + 表面处理服务页
- 当文章在解释“什么时候 1-2 层够用，什么时候该升级”，先落到 `products/single-double-layer-pcb`，再根据密度升级到 `products/multilayer-pcb` 或 `products/hdi-pcb`

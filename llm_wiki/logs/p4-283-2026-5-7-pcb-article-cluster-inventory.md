# P4-283 PCB Article Cluster Inventory

Date: 2026-05-07
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Derived extraction root: `/code/blogs/tmps/pcb_pdf_extracted_full`
Execution mode: `article_cluster_inventory_only`

## Purpose

Bring the `59` short article PDFs under `PCB文章` into formal controller-owned learning scope at the `clustered claim-family inventory` level.

This file does not promote new `sources/`, `facts/`, or `wiki/`.

## Scope Summary

- article PDF count: `59`
- extracted article pages: `334`
- repeated posture across the set:
  - strong technical demand signals
  - repeated `华秋DFM` branding shell
  - repeated CTA / QR / footer surfaces
  - frequent secondary-rule tables and vendor-workflow framing

Default status for all article PDFs in this pass:

- `claim_family_level_only`

## Cluster Inventory

### Cluster `E1`: DFM and design-review governance

Representative PDFs:

- `引领工业新思想--DFM的含义将如何演变.pdf`
- `全局DFM意识对于PCB设计的重要性.pdf`
- `PCB layout有DRC检查为什么还要用DFM.pdf`
- `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf`
- `华秋DFM在硬件制造中的作用.pdf`
- `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf`

Controller posture:

- mostly `claim_inventory_only`

Reason:

- heavy vendor framing
- workflow persuasion
- generalized improvement claims

### Cluster `E2`: layout, routing, stackup, layers, and impedance

Representative PDFs:

- `PCB布局布线的可制造性设计.pdf`
- `印制电路板设计重点.pdf`
- `一文带你读懂PCB电路板设计中各种层的定义.pdf`
- `PCB叠层顺序规划配置方案.pdf`
- `PCB为什么常用50Ω阻抗？6大原因.pdf`
- `PCB阻抗误差控制在5%，究竟有多难？.pdf`
- `PCB内层的可制造性设计.pdf`
- `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`

Controller posture:

- `future_bounded_learning_candidate`

Reason:

- strong taxonomy and design-context value
- exact tolerances and numerics still blocked

### Cluster `E3`: fabrication features, pads, holes, slots, vias, solder mask, and traces

Representative PDFs:

- `PCB可制造性设计及案例分析之孔槽篇.pdf`
- `器件引脚的方槽、方孔如何避坑？.pdf`
- `器件引脚小尺寸的孔和槽如何避坑？.pdf`
- `PCB板漏孔、漏槽在设计端如何避坑.pdf`
- `一招搞定PCB阻焊过孔问题.pdf`
- `这样做，轻松拿捏阻焊桥！.pdf`
- `PCB设计如何防止阻焊漏开窗.pdf`
- `PCB焊盘设计之问题详解.pdf`
- `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf`
- `千万不能小瞧的PCB半孔板.pdf`
- `PCB“金手指”从设计到生产全流程.pdf`
- `如何避免“断头线”带来的DFM（可制造性）问题？.pdf`
- `PCB设计孔间距的DFM可靠性.pdf`

Controller posture:

- `strongest_future_bounded_learning_candidate`

Reason:

- high-value failure-mode vocabulary
- strong figure-recovery potential
- dimensions and process windows still blocked

### Cluster `E4`: panelization, outline, edge-clearance, and marking

Representative PDFs:

- `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf`
- `PCB拼板，不得不注意的10个问题！.pdf`
- `PCB板各种形状的拼版实例分享.pdf`
- `啥？PCB拼版对SMT组装有影响！.pdf`
- `PCB板的Mark点设计对SMT重要性.pdf`
- `元器件到PCB板边缘间距不足的严重性.pdf`
- `PCBA板边器件布局重要性.pdf`

Controller posture:

- `future_bounded_learning_candidate`

Reason:

- neutral process vocabulary is recoverable
- exact edge distances and factory-specific panel rules remain blocked

### Cluster `E5`: assembly, DFA, soldering, stencil, and test

Representative PDFs:

- `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`
- `关于PCBA元器件布局的重要性.pdf`
- `组装电子元器件间距不足的严重性.pdf`
- `如何避免踩坑钢网.pdf`
- `你想知道的BGA焊接问题都在这里.pdf`
- `那些关于DIP器件不得不说的坑.pdf`
- `元器件虚焊原因之一盘中孔的可制造设计规范.pdf`
- `PCBA丝印位号与极性符号的组装性设计.pdf`
- `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`

Controller posture:

- `future_bounded_learning_candidate`

Reason:

- assembly-defect and test-method identity value is real
- acceptance thresholds and capability claims remain blocked

### Cluster `E6`: packages, BOM, and component-selection alignment

Representative PDFs:

- `电子元器件封装(Package).pdf`
- `如何解决bom物料与焊盘不匹配问题.pdf`
- `BOM查错助力元器件采购.pdf`
- `如何避免采购电子元器件入坑.pdf`
- `0Ω电阻在PCB板中的5大常见作用.pdf`
- `单层双面多层FPC有何区别？.pdf`

Controller posture:

- `mixed_candidate`

Reason:

- package and package-to-footprint alignment can feed later bounded learning
- procurement and sourcing guidance should mostly stay claim inventory only

### Cluster `E7`: manufacturing data exchange, file prep, and vendor-tool workflow

Representative PDFs:

- `PCB制造文件传输数据的主要格式.pdf`
- `华秋DFM组装分析前需准备的数据文件.pdf`
- `简单好用！再也不用担心PCB图形对齐问题.pdf`
- `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf`
- `华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf`
- `华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf`

Controller posture:

- mostly `claim_inventory_only`

Reason:

- branded workflow and tool-promo surfaces dominate
- a small neutral subset around file-format identity may be recoverable later

## Cluster Ranking For Future Formal Learning

Highest-value future bounded candidates:

1. `E3 fabrication features`
2. `E5 assembly / stencil / test`
3. `E2 layout / routing / stackup / impedance`
4. `E4 panelization / outline / marking`
5. `E6 packages / BOM` partial subset only

Lower-priority claim-inventory clusters:

6. `E1 DFM governance and persuasion`
7. `E7 vendor-tool workflow`

## Governance Consequences

- all article-PDF numerics remain `secondary_pdf_claim_inventory_only`
- full branded pages remain blocked as reusable figures
- cluster outputs may feed later bounded lane planning, but not direct fact promotion
- Chinese titles remain provenance only; future reusable knowledge must use English canonical naming

## Recommended Next Log Filenames

If later AI turns these clusters into narrower controller files, prefer:

- `logs/p4-283a-2026-5-7-pcb-article-dfm-governance-and-vendor-tool-hold-map.md`
- `logs/p4-283b-2026-5-7-pcb-article-layout-stackup-and-impedance-boundary-map.md`
- `logs/p4-283c-2026-5-7-pcb-article-fabrication-features-and-panelization-boundary-map.md`
- `logs/p4-283d-2026-5-7-pcb-article-assembly-test-package-and-bom-boundary-map.md`

## Current Status

- extraction availability:
  - `completed`
- per-article formal learning:
  - `not_started`
- clustered claim-family inventory:
  - `now_defined`
- direct fact promotion from article PDFs:
  - `not_allowed_by_default`

## One-Sentence Resume Direction

Continue the `PCB文章` corpus by treating `E2-E6` as future bounded-learning candidates and `E1/E7` as mostly neutralized claim-inventory and asset-metadata lanes, without promoting branded rule tables, workflow claims, or secondary-PDF numerics directly into reusable facts.

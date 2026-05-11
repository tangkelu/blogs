# APTPCB Assets Image Catalog

本文件吸收自旧目录：

- `prompts_aptpcb/assets-img-filenames.md`

用途：

- 写博客时快速判断 APTPCB 站内是否已有可复用图片资源
- 避免临时去旧目录翻找图片路径
- 作为“站内素材索引”，不是强制模板的一部分

## 使用规则

1. 仅在图片确实能增强技术说明时使用。
2. 不要为了凑图而插图。
3. 如果文章命中 `must_add_figure` 或 `should_add_figure`，优先从站内素材里找可复用图，再考虑 AI 信息图。
4. 优先选择：
   - 工厂实拍
   - 检测设备图
   - 与文章主题强相关的产品 / 工艺图
5. 如果图片只体现品牌形象，不体现技术信息，优先不使用。
6. 如果使用 AI 生成的信息图，必须让它承担“流程翻译 / 决策可视化 / 结构解释”职责，而不是做成视觉广告。
7. AI 图表落正文时，默认同时补：
   - 引导句
   - 高信息密度 alt
   - 专业图注
8. 同一篇文章里，正文技术图通常控制在 `1` 张优先；除非第二张图确实解释了不同的工程问题。
9. 如果图片不合适，或会重复首图 / 降低信息密度，可以改用轻量 HTML 卡片承担同样的解释任务。

## 常用博客类资源示例

- `/assets/img/blogs/2025/03/advanced-pcb-manufacturing.webp`
- `/assets/img/blogs/2025/03/advanced-pcb-manufacturing-1.webp`
- `/assets/img/blogs/2025/03/high-frequency-pcb-fabrication.webp`
- `/assets/img/blogs/2025/03/high-frequency-pcb-fabrication-1.webp`
- `/assets/img/blogs/2025/05/pcb-stackup-design.webp`
- `/assets/img/blogs/2025/05/pcb-stackup-design-1.webp`
- `/assets/img/blogs/2025/05/pcb-stackup-design-2.webp`
- `/assets/img/blogs/2025/05/rigid-flex-pcb-design.webp`
- `/assets/img/blogs/2025/05/rigid-flex-pcb-design-1.webp`
- `/assets/img/blogs/2025/05/rogers-pcb-manufacturing.webp`
- `/assets/img/blogs/2025/05/rogers-pcb-manufacturing-1.webp`
- `/assets/img/blogs/2025/06/medical-pcb-assembly.webp`

## 常用工业 / 能力类资源示例

- `/assets/img/industries/server-pcb.webp`
- `/assets/img/industries/robotics-pcb.webp`
- `/assets/img/industries/medical-pcb.webp`
- `/assets/img/industries/power-pcb.webp`
- `/assets/img/industries/rf-pcb-assembly.webp`
- `/assets/img/about/about-pcb-factory-ldi.webp`
- `/assets/img/about/about-pcba-X-Ray-inspecting.webp`
- `/assets/img/about/about-pcba-SPI-Solder-Paste-Inspection.webp`
- `/assets/img/home/smt-assembly-line.webp`
- `/assets/img/home/pcb-factory.webp`

## 说明

旧文件列出了更完整的 600+ 资源路径。  
如果需要做全量迁移或自动索引，仍可参考原文件：

- `/code/blogs/prompts_aptpcb/assets-img-filenames.md`

当前 `prompts_template` 只保留“常用索引”职责，不再维护完整大清单。

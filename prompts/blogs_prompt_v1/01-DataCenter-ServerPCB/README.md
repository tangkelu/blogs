# 关键词管理系统使用说明

## 概述

这个JSON文件现在支持跟踪关键词的使用状态和关联的模板文件。

## 新的JSON结构

### 顶层字段

- `section_number`: 章节编号
- `section_title`: 章节标题
- `available_templates`: 可用的模板文件列表
- `subsections`: 子章节数组

### 关键词对象结构

每个关键词现在是一个对象，包含以下字段：

```json
{
  "keyword": "Server Motherboard PCB",
  "used": false,
  "template": null,
  "usage_date": null,
  "notes": ""
}
```

#### 字段说明

- `keyword`: 关键词文本
- `used`: 布尔值，表示是否已使用
- `template`: 使用的模板文件名（从available_templates中选择）
- `usage_date`: 使用日期（ISO格式：YYYY-MM-DD）
- `notes`: 备注信息

## 使用示例

### 标记关键词为已使用

```json
{
  "keyword": "Server Motherboard PCB",
  "used": true,
  "template": "datacenter-server-pcb-v1.md",
  "usage_date": "2025-01-27",
  "notes": "用于技术博客文章"
}
```

### 查询未使用的关键词

可以通过编程方式筛选 `used: false` 的关键词。

### 统计使用情况

- 总关键词数量
- 已使用关键词数量
- 各模板的使用频率
- 按日期统计使用情况

## 可用模板

当前可用的模板文件：

1. `datacenter-server-pcb-v1.md`
2. `datacenter-server-pcb-v2.md`
3. `datacenter-server-pcb-v3.md`

## 维护建议

1. 使用关键词时，及时更新 `used` 状态
2. 记录使用的模板文件名
3. 添加使用日期便于追踪
4. 在notes字段中记录相关信息
5. 定期检查未使用的关键词，优化内容策略
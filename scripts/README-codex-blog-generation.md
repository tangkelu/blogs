# Codex Blog Generation CLI

本工具使用以下优先级读取模型配置：

1. `/root/.codex/config.toml` + `/root/.codex/auth.json`
2. `/code/chatbot/.env.local`
3. `/code/chatbot/.env`

默认工作流为两阶段：

1. 联网生成 evidence pack
2. 基于 evidence pack 生成最终博客 Markdown

## 单篇生成

```bash
node /code/blogs/scripts/run_codex_blog_generation_test.mjs \
  --site hilpcb \
  --template auto \
  "pcb impedance control"
```

## 指定模板

```bash
node /code/blogs/scripts/run_codex_blog_generation_test.mjs \
  --site aptpcb \
  --template pillar \
  "high speed pcb"
```

## 批量生成

关键词文件一行一个关键词：

```txt
pcb impedance control
high speed pcb
rogers pcb material
```

运行：

```bash
node /code/blogs/scripts/run_codex_blog_generation_test.mjs \
  --site hilpcb \
  --template auto \
  --keywords-file /abs/path/keywords.txt
```

## 输出目录

默认输出到：

`/code/blogs/output/<site>/<template>/`

每个关键词生成：

- `*.evidence.md`
- `*.md`
- `*.meta.json`

失败或截断的文章不会进入正式目录，而会归档到：

`/code/blogs/output/_failed/<site>/<template>/`

其中失败文章文件名会带 `.incomplete.md` 后缀。

说明：

- 正式可检查的博客，以 `/code/blogs/output/<site>/<template>/` 下的 `*.md` 为准。
- 根目录 `/code/blogs/output/` 下历史遗留的孤立文件不是当前规范输出，可能包含早期截断测试稿。

## 参数

- `--site hilpcb|aptpcb`
- `--template auto|query|pillar`
- `--keyword "<keyword>"`
- `--keywords-file /abs/path/file.txt`
- `--output-dir /abs/path/output`
- `--locale zh-CN`
- `--max-attempts 3`

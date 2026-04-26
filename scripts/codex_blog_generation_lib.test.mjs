import test from 'node:test'
import assert from 'node:assert/strict'

import {
  assembleLlmWikiEvidenceContext,
  buildArtifactPaths,
  buildPromptBundle,
  buildEvidencePrompt,
  buildArticleFromEvidencePrompt,
  buildLlmWikiLookup,
  extractOutputTextFromResponsePayload,
  extractCodexProviderConfig,
  loadKeywords,
  loadLlmWikiIndex,
  loadOpenAiConfigFromFiles,
  looksLikeCompleteBlog,
  parseCliArgs,
  parseDotEnv,
  resolveLlmWikiEvidenceStrategy,
  scoreLlmWikiLookup,
  shouldUseWebSearchForLlmWikiLookup,
  resolveTemplateType,
  sanitizeModelText,
  SITE_CONFIGS,
  validateCompleteBlog,
  shouldRetryGenerationError
} from './codex_blog_generation_lib.mjs'

test('parseDotEnv reads basic key value pairs', () => {
  const parsed = parseDotEnv(`
OPENAI_API_KEY=sk-test
OPENAI_BASE_URL=https://example.com/v1
# comment
OPENAI_MODEL=gpt-5.2-codex
`)

  assert.equal(parsed.OPENAI_API_KEY, 'sk-test')
  assert.equal(parsed.OPENAI_BASE_URL, 'https://example.com/v1')
  assert.equal(parsed.OPENAI_MODEL, 'gpt-5.2-codex')
})

test('loadOpenAiConfigFromFiles prefers a codex model when available', () => {
  const config = loadOpenAiConfigFromFiles([
    {
      path: '/tmp/.env.local',
      content: `
OPENAI_API_KEY=sk-local
OPENAI_BASE_URL=https://gmn.example.com/v1
OPENAI_MODEL=gpt-5.2
`
    },
    {
      path: '/tmp/.env',
      content: `
OPENAI_MODEL=gpt-5.2-codex
`
    }
  ])

  assert.equal(config.apiKey, 'sk-local')
  assert.equal(config.baseUrl, 'https://gmn.example.com/v1')
  assert.equal(config.model, 'gpt-5.2-codex')
})

test('buildPromptBundle includes shared prompt, site overlay, and internal links', () => {
  const prompt = buildPromptBundle({
    keyword: 'pcb impedance control',
    sharedPrompt: 'SHARED QUERY PROMPT',
    siteOverlay: 'SITE OVERLAY',
    internalLinkPool: 'https://hilpcb.com/en/products/high-speed-pcb',
    siteKey: 'hilpcb',
    locale: 'zh-CN'
  })

  assert.match(prompt, /SHARED QUERY PROMPT/)
  assert.match(prompt, /SITE OVERLAY/)
  assert.match(prompt, /https:\/\/hilpcb\.com\/en\/products\/high-speed-pcb/)
  assert.match(prompt, /pcb impedance control/)
  assert.match(prompt, /只输出最终 Markdown/)
})

test('shouldRetryGenerationError only retries transient failures', () => {
  assert.equal(shouldRetryGenerationError('503 Service temporarily unavailable'), true)
  assert.equal(shouldRetryGenerationError('429 rate limit exceeded'), true)
  assert.equal(shouldRetryGenerationError('request timeout'), true)
  assert.equal(shouldRetryGenerationError('empty output from model'), true)
  assert.equal(shouldRetryGenerationError('401 unauthorized'), false)
})

test('sanitizeModelText removes fenced wrappers', () => {
  const cleaned = sanitizeModelText('```markdown\\n# title\\n```')
  assert.equal(cleaned, '# title')
})

test('staged prompts include keyword and evidence constraints', () => {
  const evidencePrompt = buildEvidencePrompt({
    keyword: 'pcb impedance control',
    siteKey: 'hilpcb',
    locale: 'zh-CN',
    localEvidenceContext: 'LLM WIKI LOCAL CONTEXT',
    allowWebSearch: false
  })
  const articlePrompt = buildArticleFromEvidencePrompt({
    keyword: 'pcb impedance control',
    sharedPrompt: 'SHARED QUERY PROMPT',
    siteOverlay: 'SITE OVERLAY',
    internalLinkPool: 'POOL',
    evidenceText: 'EVIDENCE TEXT',
    siteKey: 'hilpcb',
    locale: 'zh-CN'
  })

  assert.match(evidencePrompt, /pcb impedance control/)
  assert.match(evidencePrompt, /LLM WIKI LOCAL CONTEXT/)
  assert.match(evidencePrompt, /本地 llm_wiki/i)
  assert.doesNotMatch(evidencePrompt, /必须联网搜索公开可验证来源/)
  assert.match(articlePrompt, /EVIDENCE TEXT/)
  assert.match(articlePrompt, /SHARED QUERY PROMPT/)
  assert.match(articlePrompt, /frontmatter 之后必须输出一个且仅一个正文 H1|不要缺失 H1/)
  assert.match(articlePrompt, /顶部答案块|不要机械输出“## 直接回答”|4-6 条短结论/)
  assert.match(articlePrompt, /公开参考资料|Public Sources|Sources/i)
  assert.match(articlePrompt, /HTML 卡片|HTML card/i)
  assert.match(articlePrompt, /参数密集型|工程控制型|4-card HTML 卡片/)
  assert.match(articlePrompt, /成本优化|优先级排序|比较矩阵|补充表格/)
  assert.match(articlePrompt, /不是装饰块|工程结论|风险信号|验证动作|冻结项/)
  assert.match(articlePrompt, /配色要跟主题走|不要随机换色|机械复用同一套主色/)
  assert.match(articlePrompt, /目录/)
  assert.match(articlePrompt, /内联来源归因|根据 .*?规范|According to/i)
  assert.match(articlePrompt, /作者与审核信息|reviewedBy|作者实体|专家/i)
})

test('extractCodexProviderConfig reads active codex provider and auth token', () => {
  const config = extractCodexProviderConfig({
    configToml: `
model_provider = "codex120"
model = "gpt-5.4"

[model_providers.codex]
base_url = "https://gmn.example.com"

[model_providers.codex120]
base_url = "https://api.jucode.cn/v1"
`,
    authJson: JSON.stringify({
      OPENAI_API_KEY: 'sk-test-token'
    })
  })

  assert.equal(config.provider, 'codex120')
  assert.equal(config.baseUrl, 'https://api.jucode.cn/v1')
  assert.equal(config.model, 'gpt-5.4')
  assert.equal(config.apiKey, 'sk-test-token')
})

test('resolveTemplateType supports explicit and auto selection', () => {
  assert.equal(resolveTemplateType('pcb impedance control', 'auto'), 'query')
  assert.equal(resolveTemplateType('high speed pcb', 'auto'), 'pillar')
  assert.equal(resolveTemplateType('anything', 'query'), 'query')
  assert.equal(resolveTemplateType('anything', 'pillar'), 'pillar')
})

test('parseCliArgs supports site, template, file and positional keyword', () => {
  const args = parseCliArgs([
    '--site',
    'aptpcb',
    '--template=query',
    '--keywords-file',
    '/tmp/keywords.txt',
    'pcb impedance control'
  ])

  assert.equal(args.site, 'aptpcb')
  assert.equal(args.template, 'query')
  assert.equal(args.keywordsFile, '/tmp/keywords.txt')
  assert.equal(args.keyword, 'pcb impedance control')
})

test('loadKeywords merges direct keyword and keyword file content', async () => {
  const fs = await import('node:fs/promises')
  const filePath = '/tmp/codex-blog-keywords.txt'
  await fs.writeFile(filePath, '# comment\npcb stackup\n\npcb impedance control\n', 'utf8')

  const keywords = loadKeywords({
    keyword: 'pcb impedance control',
    keywordsFile: filePath
  })

  assert.deepEqual(keywords, ['pcb impedance control', 'pcb stackup'])
})

test('site configs expose both target sites', () => {
  assert.ok(SITE_CONFIGS.hilpcb)
  assert.ok(SITE_CONFIGS.aptpcb)
})

test('extractOutputTextFromResponsePayload reads non-stream response text', () => {
  const text = extractOutputTextFromResponsePayload({
    output: [
      { type: 'reasoning' },
      {
        type: 'message',
        content: [
          { type: 'output_text', text: '---\n# A' },
          { type: 'output_text', text: '\n- point one' }
        ]
      }
    ]
  })

  assert.equal(text, '---\n# A\n\n- point one')
})

test('looksLikeCompleteBlog distinguishes truncated text', () => {
  assert.equal(
    looksLikeCompleteBlog(
      '---\ntitle: "A"\n---\n# A\n- one\n- two\n- three\n<!-- faq:start -->\n<!-- faq:end -->\n作者：团队\n完整收尾。'
    ),
    true
  )
  assert.equal(looksLikeCompleteBlog('---\n- one\n半句截断，'), false)
  assert.equal(
    looksLikeCompleteBlog(
      '---\ntitle: "A"\n---\n# A\n- one\n- two\n<!-- faq:start -->\n<!-- faq:end -->\n作者：团队\n完整收尾。'
    ),
    false
  )
})

test('shared query prompt requires toc, public sources, and optional html cards', async () => {
  const fs = await import('node:fs/promises')
  const prompt = await fs.readFile('/code/blogs/prompts_template/shared/query.md', 'utf8')

  assert.match(prompt, /长文默认启用目录|默认添加目录/)
  assert.match(prompt, /唯一 H1 大标题|frontmatter 之后必须紧跟一个且仅一个正文 H1/)
  assert.match(prompt, /顶部答案块|不强制增加 `## 直接回答`|短结论列表/)
  assert.match(prompt, /公开参考资料|Public Sources|Sources/)
  assert.match(prompt, /至少列出\s*`?3`?\s*条|至少三条/)
  assert.match(prompt, /HTML 卡片|HTML card/i)
  assert.match(prompt, /早期 Markdown table \+ 4-card HTML 卡片|参数密集型|工程控制型/)
  assert.match(prompt, /成本优化|优先级排序|trade-off 决策矩阵|补充 Markdown table/)
  assert.match(prompt, /卡片不是随机装饰|工程结论|冻结项|风险信号|验证动作/)
  assert.match(prompt, /配色必须服从主题逻辑|不要机械复用同一套主色|高对比度|工程感/)
  assert.match(prompt, /定义型摘要|40-60\s*词|40–60\s*词|Definition/i)
  assert.match(prompt, /内联来源归因|根据 .*?规范|According to/i)
  assert.match(prompt, /作者实体|真实作者|reviewedBy|审核人实体/)
  assert.match(prompt, /FAQ.*query phrasing|检索式问法|自然语言搜索问句/i)
})

test('shared pillar prompt requires ai-seo authority and citation signals', async () => {
  const fs = await import('node:fs/promises')
  const prompt = await fs.readFile('/code/blogs/prompts_template/shared/pillar.md', 'utf8')

  assert.match(prompt, /目录/)
  assert.match(prompt, /唯一 H1 大标题|frontmatter 之后必须紧跟一个且仅一个正文 H1/)
  assert.match(prompt, /公开参考资料|Sources/)
  assert.match(prompt, /总览表 \+ 4-card HTML 卡片|多张 Markdown table|参数密集型/)
  assert.match(prompt, /工程结论|风险信号|验证动作|冻结项|选型逻辑/)
  assert.match(prompt, /配色按主题走|不要机械复用同一套配色|高对比度|工程文档气质/)
  assert.match(prompt, /定义型摘要|40-60\s*词|40–60\s*词|Definition/i)
  assert.match(prompt, /内联来源归因|根据 .*?规范|According to/i)
  assert.match(prompt, /作者实体|真实作者|reviewedBy|审核人实体/)
  assert.match(prompt, /FAQ.*query phrasing|检索式问法|自然语言搜索问句/i)
})

test('shared evidence pack template requires ai-seo evidence primitives', async () => {
  const fs = await import('node:fs/promises')
  const prompt = await fs.readFile('/code/blogs/prompts_template/shared/evidence-pack-template.md', 'utf8')

  assert.match(prompt, /定义型摘要|Quick Answer|Quick Definition/i)
  assert.match(prompt, /内联来源归因|in-body citation|citation handle/i)
  assert.match(prompt, /作者|审核|authority|reviewedBy/i)
  assert.match(prompt, /FAQ.*query phrasing|自然语言搜索问句|检索式问法/i)
})

test('validateCompleteBlog rejects truncated article output', () => {
  assert.throws(
    () => validateCompleteBlog('---\n# A\n- one\n半句截断，'),
    /incomplete or truncated/i
  )
})

test('buildArtifactPaths separates successful and failed outputs', () => {
  const successPaths = buildArtifactPaths({
    outputDir: '/code/blogs/output',
    site: 'hilpcb',
    templateType: 'query',
    stem: '2026-demo',
    status: 'success'
  })
  const failedPaths = buildArtifactPaths({
    outputDir: '/code/blogs/output',
    site: 'hilpcb',
    templateType: 'query',
    stem: '2026-demo',
    status: 'failed'
  })

  assert.equal(successPaths.outputDir, '/code/blogs/output/hilpcb/query')
  assert.equal(successPaths.markdownPath, '/code/blogs/output/hilpcb/query/2026-demo.md')
  assert.equal(failedPaths.outputDir, '/code/blogs/output/_failed/hilpcb/query')
  assert.equal(
    failedPaths.markdownPath,
    '/code/blogs/output/_failed/hilpcb/query/2026-demo.incomplete.md'
  )
})

test('loadLlmWikiIndex reads wiki, fact, and source records from a custom root', async () => {
  const fs = await import('node:fs/promises')
  const root = '/tmp/llm-wiki-index-fixture'

  await fs.rm(root, { recursive: true, force: true })
  await fs.mkdir(`${root}/wiki/processes`, { recursive: true })
  await fs.mkdir(`${root}/facts/materials`, { recursive: true })
  await fs.mkdir(`${root}/sources/registry/materials`, { recursive: true })

  await fs.writeFile(
    `${root}/wiki/processes/controlled-impedance-planning.md`,
    `---
topic_id: "processes-controlled-impedance-planning"
title: "Controlled Impedance Planning"
tags: ["impedance", "stackup", "pcb"]
fact_ids:
  - "methods-controlled-impedance-tdr-verification-posture"
source_ids:
  - "frontendapt-pcb-pcb-impedance-control-page-en"
---

# Definition

> Controlled impedance planning aligns stackup, geometry, and verification.
`,
    'utf8'
  )

  await fs.writeFile(
    `${root}/facts/materials/isola-370hr.md`,
    `---
fact_id: "materials-isola-370hr"
title: "Isola 370HR baseline material card"
tags: ["isola", "370hr", "high-tg"]
must_refresh: false
source_ids:
  - "isola-370hr-datasheet"
---

# Canonical Summary

> 370HR is a high-Tg laminate baseline.

## Source Links

- https://www.isola-group.com/370hr.pdf
`,
    'utf8'
  )

  await fs.writeFile(
    `${root}/sources/registry/materials/isola-370hr-datasheet.md`,
    `---
source_id: "isola-370hr-datasheet"
title: "Isola 370HR Datasheet"
organization: "Isola"
url: "https://www.isola-group.com/370hr.pdf"
topic_tags: ["isola", "370hr", "datasheet"]
must_refresh: false
---

# Source Summary

- Official datasheet.
`,
    'utf8'
  )

  const index = loadLlmWikiIndex(root)

  assert.equal(index.length, 3)
  assert.equal(index.filter((entry) => entry.kind === 'wiki').length, 1)
  assert.equal(index.filter((entry) => entry.kind === 'fact').length, 1)
  assert.equal(index.filter((entry) => entry.kind === 'source').length, 1)
})

test('buildLlmWikiLookup finds relevant local documents for a keyword', () => {
  const index = [
    {
      kind: 'wiki',
      id: 'processes-controlled-impedance-planning',
      title: 'Controlled Impedance Planning',
      tags: ['impedance', 'stackup', 'pcb'],
      headings: ['Definition'],
      summary: 'Aligns stackup and verification.',
      links: [],
      sourceIds: ['frontendapt-pcb-pcb-impedance-control-page-en'],
      factIds: ['methods-controlled-impedance-tdr-verification-posture'],
      mustRefresh: false,
      path: '/tmp/wiki.md'
    },
    {
      kind: 'fact',
      id: 'methods-controlled-impedance-tdr-verification-posture',
      title: 'Controlled impedance TDR verification posture',
      tags: ['impedance', 'tdr'],
      headings: ['Canonical Summary'],
      summary: 'TDR is a validation posture.',
      links: ['https://example.com/tdr'],
      sourceIds: ['ipc-2141'],
      factIds: [],
      mustRefresh: false,
      path: '/tmp/fact.md'
    },
    {
      kind: 'source',
      id: 'random-copper-page',
      title: 'Heavy copper page',
      tags: ['copper'],
      headings: ['Source Summary'],
      summary: 'Not relevant.',
      links: ['https://example.com/copper'],
      sourceIds: [],
      factIds: [],
      mustRefresh: false,
      path: '/tmp/source.md'
    }
  ]

  const lookup = buildLlmWikiLookup('pcb impedance control', index)

  assert.equal(lookup.hasMatches, true)
  assert.equal(lookup.matches[0].id, 'processes-controlled-impedance-planning')
  assert.equal(lookup.matches.some((entry) => entry.id === 'methods-controlled-impedance-tdr-verification-posture'), true)
})

test('assembleLlmWikiEvidenceContext summarizes local hits for prompt consumption', () => {
  const lookup = {
    keyword: 'pcb impedance control',
    hasMatches: true,
    matches: [
      {
        kind: 'wiki',
        id: 'processes-controlled-impedance-planning',
        title: 'Controlled Impedance Planning',
        tags: ['impedance', 'stackup'],
        headings: ['Definition'],
        summary: 'Aligns stackup and verification.',
        links: [],
        sourceIds: ['frontendapt-pcb-pcb-impedance-control-page-en'],
        factIds: ['methods-controlled-impedance-tdr-verification-posture'],
        mustRefresh: false,
        path: '/tmp/wiki.md',
        score: 12
      },
      {
        kind: 'fact',
        id: 'methods-controlled-impedance-tdr-verification-posture',
        title: 'Controlled impedance TDR verification posture',
        tags: ['impedance', 'tdr'],
        headings: ['Canonical Summary'],
        summary: 'TDR is a validation posture.',
        links: ['https://example.com/tdr'],
        sourceIds: ['ipc-2141'],
        factIds: [],
        mustRefresh: false,
        path: '/tmp/fact.md',
        score: 9
      }
    ]
  }

  const context = assembleLlmWikiEvidenceContext(lookup)

  assert.match(context, /Local LLM Wiki Matches/)
  assert.match(context, /Controlled Impedance Planning/)
  assert.match(context, /TDR is a validation posture/)
  assert.match(context, /https:\/\/example\.com\/tdr/)
  assert.match(context, /coverage_score/i)
})

test('scoreLlmWikiLookup rewards diversified local evidence', () => {
  const score = scoreLlmWikiLookup({
    hasMatches: true,
    matches: [
      {
        kind: 'wiki',
        links: [],
        sourceIds: ['source-a'],
        factIds: ['fact-a'],
        mustRefresh: false
      },
      {
        kind: 'fact',
        links: ['https://example.com/a'],
        sourceIds: ['source-b'],
        factIds: [],
        mustRefresh: false
      },
      {
        kind: 'source',
        links: ['https://example.com/b'],
        sourceIds: [],
        factIds: [],
        mustRefresh: false
      }
    ]
  })

  assert.equal(score >= 10, true)
})

test('resolveLlmWikiEvidenceStrategy returns local_only for strong local coverage', () => {
  const strategy = resolveLlmWikiEvidenceStrategy({
    hasMatches: true,
    matches: [
      {
        kind: 'wiki',
        title: 'Controlled Impedance Planning',
        summary: 'Planning summary',
        links: [],
        sourceIds: ['source-a'],
        factIds: ['fact-a'],
        mustRefresh: false
      },
      {
        kind: 'fact',
        title: 'Controlled impedance TDR verification posture',
        summary: 'Validation summary',
        links: ['https://example.com/tdr'],
        sourceIds: ['source-b'],
        factIds: [],
        mustRefresh: false
      },
      {
        kind: 'source',
        title: 'IPC note',
        summary: 'Public source note',
        links: ['https://example.com/ipc'],
        sourceIds: [],
        factIds: [],
        mustRefresh: false
      }
    ]
  })

  assert.equal(strategy.mode, 'local_only')
  assert.equal(strategy.useWebSearch, false)
})

test('resolveLlmWikiEvidenceStrategy returns hybrid for weak but non-empty local coverage', () => {
  const strategy = resolveLlmWikiEvidenceStrategy({
    hasMatches: true,
    matches: [
      {
        kind: 'wiki',
        title: 'PCB page',
        summary: 'Generic summary',
        links: [],
        sourceIds: [],
        factIds: [],
        mustRefresh: true
      }
    ]
  })

  assert.equal(strategy.mode, 'hybrid')
  assert.equal(strategy.useWebSearch, true)
})

test('resolveLlmWikiEvidenceStrategy keeps internal-only evidence in hybrid mode', () => {
  const strategy = resolveLlmWikiEvidenceStrategy({
    hasMatches: true,
    matches: [
      {
        kind: 'wiki',
        title: 'APT PCB Capability Page',
        summary: 'Internal capability framing.',
        links: [],
        sourceIds: ['frontendapt-pcb-page'],
        factIds: ['methods-controlled-impedance'],
        mustRefresh: false,
        jurisdiction: 'internal'
      },
      {
        kind: 'fact',
        title: 'Controlled impedance posture',
        summary: 'Useful but still internal-only support.',
        links: [],
        sourceIds: ['frontendapt-pcb-page'],
        factIds: [],
        mustRefresh: false,
        jurisdiction: 'internal'
      },
      {
        kind: 'source',
        title: 'APT capability page',
        summary: 'Internal source note.',
        links: [],
        sourceIds: [],
        factIds: [],
        mustRefresh: false,
        jurisdiction: 'internal',
        trustTier: 't2'
      }
    ]
  })

  assert.equal(strategy.mode, 'hybrid')
  assert.equal(strategy.useWebSearch, true)
})

test('shouldUseWebSearchForLlmWikiLookup enables fallback for hybrid and web_only modes', () => {
  assert.equal(shouldUseWebSearchForLlmWikiLookup({ hasMatches: true, matches: [{}] }), true)
  assert.equal(shouldUseWebSearchForLlmWikiLookup({ hasMatches: false, matches: [] }), true)
  assert.equal(
    shouldUseWebSearchForLlmWikiLookup({
      hasMatches: true,
      matches: [
        {
          kind: 'wiki',
          links: [],
          sourceIds: ['source-a'],
          factIds: ['fact-a'],
          mustRefresh: false
        },
        {
          kind: 'fact',
          links: ['https://example.com'],
          sourceIds: ['source-b'],
          factIds: [],
          mustRefresh: false
        },
        {
          kind: 'source',
          links: ['https://example.com/2'],
          sourceIds: [],
          factIds: [],
          mustRefresh: false
        }
      ]
    }),
    false
  )
})

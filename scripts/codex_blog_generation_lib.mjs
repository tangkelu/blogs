import fs from 'node:fs'
import path from 'node:path'

const BLOGS_ROOT = '/code/blogs'
const LLM_WIKI_ROOT = path.join(BLOGS_ROOT, 'llm_wiki')

export const SITE_CONFIGS = {
  hilpcb: {
    siteKey: 'hilpcb',
    locale: 'zh-CN',
    queryOverlayPath: path.join(BLOGS_ROOT, 'prompts_template/hilpcb/query-overlay.md'),
    pillarOverlayPath: path.join(BLOGS_ROOT, 'prompts_template/hilpcb/pillar-overlay.md'),
    internalLinkPoolPath: path.join(BLOGS_ROOT, 'prompts_template/hilpcb/internal-link-pool.md')
  },
  aptpcb: {
    siteKey: 'aptpcb',
    locale: 'zh-CN',
    queryOverlayPath: path.join(BLOGS_ROOT, 'prompts_template/aptpcb/query-overlay.md'),
    pillarOverlayPath: path.join(BLOGS_ROOT, 'prompts_template/aptpcb/pillar-overlay.md'),
    internalLinkPoolPath: path.join(BLOGS_ROOT, 'prompts_template/aptpcb/internal-link-pool.md')
  }
}

export const SHARED_PROMPT_PATHS = {
  query: path.join(BLOGS_ROOT, 'prompts_template/shared/query.md'),
  pillar: path.join(BLOGS_ROOT, 'prompts_template/shared/pillar.md')
}

export function parseDotEnv(content) {
  const result = {}

  for (const line of content.split(/\r?\n/)) {
    const trimmed = line.trim()
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) {
      continue
    }

    const index = trimmed.indexOf('=')
    const key = trimmed.slice(0, index).trim()
    let value = trimmed.slice(index + 1).trim()

    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1)
    }

    result[key] = value
  }

  return result
}

export function loadOpenAiConfigFromFiles(files) {
  const merged = {}
  const modelCandidates = []

  for (const file of files) {
    if (!file?.content) {
      continue
    }

    const parsed = parseDotEnv(file.content)
    Object.assign(merged, parsed)

    if (parsed.OPENAI_MODEL) {
      modelCandidates.push(parsed.OPENAI_MODEL)
    }
  }

  const codexModel = modelCandidates.find((model) => model.toLowerCase().includes('codex'))
  const fallbackModel = modelCandidates.find(Boolean) || 'gpt-5.2-codex'

  return {
    apiKey: merged.OPENAI_API_KEY || '',
    baseUrl: merged.OPENAI_BASE_URL || 'https://api.openai.com/v1',
    model: codexModel || fallbackModel
  }
}

export function loadOpenAiConfigFromPaths(paths) {
  const files = paths.map((filePath) => ({
    path: filePath,
    content: fs.existsSync(filePath) ? fs.readFileSync(filePath, 'utf8') : ''
  }))

  return loadOpenAiConfigFromFiles(files)
}

export function loadRuntimeConfig() {
  const codexConfigPath = '/root/.codex/config.toml'
  const codexAuthPath = '/root/.codex/auth.json'

  if (fs.existsSync(codexConfigPath) && fs.existsSync(codexAuthPath)) {
    const codexConfig = extractCodexProviderConfig({
      configToml: fs.readFileSync(codexConfigPath, 'utf8'),
      authJson: fs.readFileSync(codexAuthPath, 'utf8')
    })

    if (codexConfig.apiKey) {
      return codexConfig
    }
  }

  return loadOpenAiConfigFromPaths(['/code/chatbot/.env.local', '/code/chatbot/.env'])
}

export function extractCodexProviderConfig(input) {
  const configToml = input.configToml || ''
  const authJson = input.authJson || '{}'
  const activeProvider =
    configToml.match(/^model_provider\s*=\s*"([^"]+)"/m)?.[1] || 'codex'
  const model = configToml.match(/^model\s*=\s*"([^"]+)"/m)?.[1] || 'gpt-5.4'
  const escapedProvider = activeProvider.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  const activeSectionRegex = new RegExp(
    String.raw`\[model_providers\.${escapedProvider}\][\s\S]*?base_url\s*=\s*"([^"]+)"`,
    'm'
  )
  const baseUrl =
    configToml.match(activeSectionRegex)?.[1] ||
    configToml.match(/\[model_providers\.codex\][\s\S]*?base_url\s*=\s*"([^"]+)"/m)?.[1] ||
    'https://api.openai.com/v1'

  const auth = JSON.parse(authJson)
  const apiKey =
    auth.OPENAI_API_KEY || auth.api_key || auth.token || auth.access_token || ''

  return {
    provider: activeProvider,
    model,
    baseUrl,
    apiKey
  }
}

export function buildPromptBundle(input) {
  return [
    `你现在要为 ${input.siteKey.toUpperCase()} 生成一篇真实可发布的技术博客测试稿。`,
    `目标语言：${input.locale}`,
    `主关键词：${input.keyword}`,
    '',
    '执行要求：',
    '- 必须默认联网搜索，优先使用公开可验证来源。',
    '- 只在能核实的前提下写数字、标准、术语、工艺判断。',
    '- 如果公开来源不足，不要编造数据，改写成条件判断或验证建议。',
    '- 内链优先链接产品页、服务页、工具页，次级才是博客页。',
    '- 文章必须适合 HILPCB 商业承接，但不能把站点能力写成行业通用事实。',
    '- 只输出最终 Markdown。',
    '',
    '共享主提示词：',
    input.sharedPrompt.trim(),
    '',
    '站点 overlay：',
    input.siteOverlay.trim(),
    '',
    '可用内链池：',
    input.internalLinkPool.trim(),
    '',
    '补充执行要求：',
    '- 文章使用 Query 结构。',
    '- 必须包含 frontmatter、H1 下方顶部答案块、早期表格、主体 H2、FAQ 包裹、作者与审核信息。',
    '- FAQ 必须保留 <!-- faq:start --> 和 <!-- faq:end -->。',
    '- 在不影响可读性的前提下，尽量把关键来源结论融入正文。',
    '- 不要输出提示词说明、证据包清单或分析备注。'
  ].join('\n')
}

export function shouldRetryGenerationError(message) {
  return /(503|429|timeout|temporarily unavailable|empty output)/i.test(message || '')
}

export function sanitizeModelText(text) {
  return (text || '')
    .replace(/\\n/g, '\n')
    .trim()
    .replace(/^```[a-zA-Z0-9_-]*\n/, '')
    .replace(/\n```$/, '')
    .trim()
}

export function extractOutputTextFromResponsePayload(payload) {
  if (!payload || typeof payload !== 'object') {
    return ''
  }

  const outputs = Array.isArray(payload.output) ? payload.output : []
  const chunks = []

  for (const item of outputs) {
    if (item?.type !== 'message' || !Array.isArray(item.content)) {
      continue
    }

    for (const content of item.content) {
      if (content?.type === 'output_text' && typeof content.text === 'string') {
        chunks.push(content.text)
      }
    }
  }

  return sanitizeModelText(chunks.join('\n').trim())
}

export function looksLikeCompleteBlog(text) {
  const normalized = sanitizeModelText(text)
  if (!normalized) {
    return false
  }

  const withoutFrontmatter = normalized.replace(/^---[\s\S]*?---\s*/, '')
  const h1Matches = withoutFrontmatter.match(/^#\s+.+$/gm) || []
  const bodyAfterH1 = withoutFrontmatter.replace(/^#\s+.+\n+/, '')
  const firstH2Index = bodyAfterH1.search(/^##\s+/m)
  const introSegment = firstH2Index === -1 ? bodyAfterH1 : bodyAfterH1.slice(0, firstH2Index)
  const introBulletMatches = introSegment.match(/^\s*-\s+/gm) || []

  return (
    normalized.startsWith('---') &&
    h1Matches.length === 1 &&
    introBulletMatches.length >= 3 &&
    normalized.includes('<!-- faq:start -->') &&
    normalized.includes('<!-- faq:end -->') &&
    normalized.includes('作者') &&
    !/[，、：:；;或]\s*$/.test(normalized)
  )
}

export function validateCompleteBlog(text) {
  const normalized = sanitizeModelText(text)
  if (!looksLikeCompleteBlog(normalized)) {
    throw new Error('Generated article is incomplete or truncated')
  }
  return normalized
}

export function buildArtifactPaths(input) {
  const status = input.status === 'failed' ? 'failed' : 'success'
  const outputDir =
    status === 'failed'
      ? path.join(input.outputDir, '_failed', input.site, input.templateType)
      : path.join(input.outputDir, input.site, input.templateType)
  const markdownSuffix = status === 'failed' ? '.incomplete.md' : '.md'

  return {
    outputDir,
    markdownPath: path.join(outputDir, `${input.stem}${markdownSuffix}`),
    evidencePath: path.join(outputDir, `${input.stem}.evidence.md`),
    metaPath: path.join(outputDir, `${input.stem}.meta.json`)
  }
}

export function buildEvidencePrompt(input) {
  const strategyMode = input.strategyMode || (input.allowWebSearch ? 'web_only' : 'local_only')
  const prompt = [
    `请围绕关键词“${input.keyword}”为 ${input.siteKey.toUpperCase()} 准备技术博客证据包。`,
    `目标语言：${input.locale}`,
    `页面类型：${input.templateType}`,
    '',
    '要求：',
    strategyMode === 'hybrid'
      ? '- 先使用本地 llm_wiki 已命中的资料，再联网补充本地未覆盖或证据不足的公开来源。'
      : input.allowWebSearch
        ? '- 当前本地 llm_wiki 未形成足够命中，允许联网搜索公开可验证来源补齐。'
        : '- 优先只使用本地 llm_wiki 已命中的资料，不要额外联网搜索。',
    '- 只收集与 PCB/PCBA 技术判断直接相关的事实、标准、白皮书、datasheet 语境、验证方法。',
    '- 不要编造数字。',
    '- 不要输出整篇博客。',
    '- 输出中文简明证据包，至少分成以下八段：',
    '  1. Public Facts',
    '  2. Project Judgments',
    '  3. Candidate Internal Links',
    '  4. Source Notes',
    '  5. Quick Answer Material',
    '  6. Inline Citation Handles',
    '  7. Authority / Reviewer Inputs',
    '  8. FAQ Query Seeds',
    '- Source Notes 至少列出 3 个公开来源，并写明它们各自支持什么结论。',
    '- Quick Answer Material 需要提供可压缩成 40-60 词定义型摘要的原料。',
    '- Inline Citation Handles 至少提供 3 组，可直接写进正文，如“根据某规范”“某 datasheet 给出”。',
    '- Authority / Reviewer Inputs 需要准备作者、审核人、团队边界或实体资料，优先真实可识别实体。',
    '- FAQ Query Seeds 至少提供 4 个贴近自然语言搜索问句的高频问法。',
    '- Candidate Internal Links 只写适合导向 HILPCB 产品页、服务页、工具页的落点建议。'
  ]

  if (input.localEvidenceContext) {
    prompt.push('', '本地 llm_wiki 命中资料：', input.localEvidenceContext.trim())
  }

  return prompt.join('\n')
}

export function readTextFile(filePath) {
  return fs.readFileSync(filePath, 'utf8')
}

export function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true })
}

export function slugify(value) {
  return value
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}

export function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, '-')
}

function splitFrontmatter(rawText) {
  const match = rawText.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/)
  if (!match) {
    return { frontmatter: '', body: rawText }
  }

  return {
    frontmatter: match[1],
    body: match[2]
  }
}

function parseFrontmatterValue(rawValue) {
  const trimmed = rawValue.trim()
  if (!trimmed) {
    return ''
  }

  if (
    (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
    (trimmed.startsWith("'") && trimmed.endsWith("'"))
  ) {
    return trimmed.slice(1, -1)
  }

  if (trimmed === 'true') {
    return true
  }

  if (trimmed === 'false') {
    return false
  }

  if (trimmed.startsWith('[') && trimmed.endsWith(']')) {
    return trimmed
      .slice(1, -1)
      .split(',')
      .map((item) => item.trim())
      .filter(Boolean)
      .map((item) => {
        if (
          (item.startsWith('"') && item.endsWith('"')) ||
          (item.startsWith("'") && item.endsWith("'"))
        ) {
          return item.slice(1, -1)
        }
        return item
      })
  }

  return trimmed
}

function parseSimpleFrontmatter(rawText) {
  const result = {}
  let currentKey = ''

  for (const line of rawText.split(/\r?\n/)) {
    if (!line.trim()) {
      continue
    }

    const keyMatch = line.match(/^([A-Za-z0-9_]+):\s*(.*)$/)
    if (keyMatch) {
      currentKey = keyMatch[1]
      const rawValue = keyMatch[2]
      result[currentKey] = parseFrontmatterValue(rawValue)
      continue
    }

    const listMatch = line.match(/^\s*-\s+(.*)$/)
    if (listMatch && currentKey) {
      const existing = Array.isArray(result[currentKey]) ? result[currentKey] : []
      existing.push(parseFrontmatterValue(listMatch[1]))
      result[currentKey] = existing
    }
  }

  return result
}

function extractHeadings(body) {
  return body
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => /^#+\s+/.test(line))
    .map((line) => line.replace(/^#+\s+/, ''))
}

function extractSummary(body) {
  const quoteMatch = body.match(/>\s*([^\n]+)/)
  if (quoteMatch) {
    return quoteMatch[1].trim()
  }

  const paragraphMatch = body.match(/\n\n([^\n#>-][^\n]*)/)
  return paragraphMatch ? paragraphMatch[1].trim() : ''
}

function extractLinks(body) {
  const links = new Set()

  for (const match of body.matchAll(/https?:\/\/[^\s)]+/g)) {
    links.add(match[0])
  }

  return [...links]
}

function normalizeStringArray(value) {
  if (Array.isArray(value)) {
    return value.map((item) => String(item).trim()).filter(Boolean)
  }

  if (typeof value === 'string' && value.trim()) {
    return [value.trim()]
  }

  return []
}

function tokenizeForLookup(value) {
  return (value || '')
    .toLowerCase()
    .split(/[^a-z0-9]+/i)
    .map((token) => token.trim())
    .filter((token) => token.length >= 2)
}

function scoreLlmWikiEntry(tokens, entry) {
  let score = 0
  const haystacks = [
    entry.id,
    entry.title,
    entry.summary,
    ...entry.tags,
    ...entry.headings
  ]
    .join(' \n ')
    .toLowerCase()

  for (const token of tokens) {
    if (entry.id.toLowerCase().includes(token)) {
      score += 5
    }
    if (entry.title.toLowerCase().includes(token)) {
      score += 4
    }
    if (entry.tags.some((tag) => tag.toLowerCase().includes(token))) {
      score += 3
    }
    if (haystacks.includes(token)) {
      score += 1
    }
  }

  if (entry.kind === 'wiki') {
    score += 2
  }

  if (entry.mustRefresh) {
    score -= 1
  }

  return score
}

function walkMarkdownFiles(rootDir) {
  if (!fs.existsSync(rootDir)) {
    return []
  }

  const results = []
  const stack = [rootDir]

  while (stack.length > 0) {
    const current = stack.pop()
    const stat = fs.statSync(current)

    if (stat.isDirectory()) {
      for (const child of fs.readdirSync(current)) {
        stack.push(path.join(current, child))
      }
      continue
    }

    if (current.endsWith('.md')) {
      results.push(current)
    }
  }

  return results
}

function readLlmWikiDocument(kind, filePath) {
  const rawText = readTextFile(filePath)
  const { frontmatter, body } = splitFrontmatter(rawText)
  const meta = parseSimpleFrontmatter(frontmatter)

  const idKey =
    kind === 'wiki' ? 'topic_id' : kind === 'fact' ? 'fact_id' : 'source_id'

  return {
    kind,
    id: String(meta[idKey] || path.basename(filePath, '.md')).trim(),
    title: String(meta.title || '').trim(),
    tags: normalizeStringArray(meta.tags || meta.topic_tags),
    headings: extractHeadings(body),
    summary: extractSummary(body),
    links: extractLinks(body),
    sourceIds: normalizeStringArray(meta.source_ids),
    factIds: normalizeStringArray(meta.fact_ids),
    mustRefresh: Boolean(meta.must_refresh),
    jurisdiction: String(meta.jurisdiction || '').trim(),
    trustTier: String(meta.trust_tier || '').trim(),
    sourceType: String(meta.source_type || '').trim(),
    path: filePath
  }
}

export function loadLlmWikiIndex(rootDir = LLM_WIKI_ROOT) {
  const groups = [
    { kind: 'wiki', dir: path.join(rootDir, 'wiki') },
    { kind: 'fact', dir: path.join(rootDir, 'facts') },
    { kind: 'source', dir: path.join(rootDir, 'sources/registry') }
  ]

  const entries = []

  for (const group of groups) {
    for (const filePath of walkMarkdownFiles(group.dir)) {
      entries.push(readLlmWikiDocument(group.kind, filePath))
    }
  }

  return entries
}

export function buildLlmWikiLookup(keyword, index, options = {}) {
  const maxMatches = options.maxMatches || 6
  const tokens = [...new Set(tokenizeForLookup(keyword))]

  const matches = index
    .map((entry) => ({
      ...entry,
      score: scoreLlmWikiEntry(tokens, entry)
    }))
    .filter((entry) => entry.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, maxMatches)

  return {
    keyword,
    hasMatches: matches.length > 0,
    matches
  }
}

export function assembleLlmWikiEvidenceContext(lookup) {
  if (!lookup?.hasMatches || !Array.isArray(lookup.matches) || lookup.matches.length === 0) {
    return ''
  }

  const coverageScore = scoreLlmWikiLookup(lookup)
  const strategy = resolveLlmWikiEvidenceStrategy(lookup)

  const lines = [
    `Local LLM Wiki Matches For: ${lookup.keyword}`,
    '',
    'Use these local materials first. Keep numeric claims bounded by their stated source conditions.',
    `coverage_score: ${coverageScore}`,
    `coverage_mode: ${strategy.mode}`
  ]

  lookup.matches.forEach((entry, index) => {
    lines.push('')
    lines.push(`${index + 1}. [${entry.kind}] ${entry.title || entry.id}`)
    lines.push(`   id: ${entry.id}`)
    if (entry.tags.length > 0) {
      lines.push(`   tags: ${entry.tags.join(', ')}`)
    }
    if (entry.summary) {
      lines.push(`   summary: ${entry.summary}`)
    }
    if (entry.factIds.length > 0) {
      lines.push(`   fact_ids: ${entry.factIds.join(', ')}`)
    }
    if (entry.sourceIds.length > 0) {
      lines.push(`   source_ids: ${entry.sourceIds.join(', ')}`)
    }
    if (entry.links.length > 0) {
      lines.push(`   links: ${entry.links.slice(0, 3).join(', ')}`)
    }
    if (entry.mustRefresh) {
      lines.push('   must_refresh: true')
    }
    lines.push(`   file: ${entry.path}`)
  })

  return lines.join('\n')
}

export function shouldUseWebSearchForLlmWikiLookup(lookup) {
  return resolveLlmWikiEvidenceStrategy(lookup).useWebSearch
}

export function scoreLlmWikiLookup(lookup) {
  if (!lookup?.hasMatches || !Array.isArray(lookup.matches) || lookup.matches.length === 0) {
    return 0
  }

  let score = 0
  const kindSet = new Set()
  const sourceIdSet = new Set()
  const factIdSet = new Set()
  let publicLinkCount = 0
  let refreshPenalty = 0
  let internalOnlyPenalty = 0

  for (const match of lookup.matches) {
    if (match.kind) {
      kindSet.add(match.kind)
    }

    for (const sourceId of normalizeStringArray(match.sourceIds)) {
      sourceIdSet.add(sourceId)
    }

    for (const factId of normalizeStringArray(match.factIds)) {
      factIdSet.add(factId)
    }

    publicLinkCount += normalizeStringArray(match.links).length

    if (match.summary) {
      score += 1
    }

    if (match.mustRefresh) {
      refreshPenalty += 1
    }

    if ((match.jurisdiction || '').toLowerCase() === 'internal') {
      internalOnlyPenalty += 1
    }
  }

  score += kindSet.size * 2
  score += Math.min(sourceIdSet.size, 3) * 2
  score += Math.min(factIdSet.size, 3) * 2
  score += Math.min(publicLinkCount, 3)
  score -= refreshPenalty
  score -= internalOnlyPenalty

  return Math.max(score, 0)
}

export function resolveLlmWikiEvidenceStrategy(lookup) {
  if (!lookup?.hasMatches || !Array.isArray(lookup.matches) || lookup.matches.length === 0) {
    return {
      mode: 'web_only',
      coverageScore: 0,
      useWebSearch: true
    }
  }

  const coverageScore = scoreLlmWikiLookup(lookup)
  const hasWiki = lookup.matches.some((match) => match.kind === 'wiki')
  const hasFact = lookup.matches.some((match) => match.kind === 'fact')
  const hasSource = lookup.matches.some((match) => match.kind === 'source')
  const hasPublicLinks = lookup.matches.some(
    (match) => Array.isArray(match.links) && match.links.length > 0
  )
  const hasExternalAnchor = lookup.matches.some((match) => {
    const jurisdiction = (match.jurisdiction || '').toLowerCase()
    return jurisdiction !== 'internal' && Array.isArray(match.links) && match.links.length > 0
  })
  const hasStructuredRefs = lookup.matches.some(
    (match) =>
      normalizeStringArray(match.sourceIds).length > 0 ||
      normalizeStringArray(match.factIds).length > 0
  )

  if (
    coverageScore >= 10 &&
    hasWiki &&
    hasFact &&
    (hasSource || hasPublicLinks) &&
    hasStructuredRefs &&
    hasExternalAnchor
  ) {
    return {
      mode: 'local_only',
      coverageScore,
      useWebSearch: false
    }
  }

  return {
    mode: 'hybrid',
    coverageScore,
    useWebSearch: true
  }
}

export function resolveTemplateType(keyword, requestedTemplate = 'auto') {
  if (requestedTemplate === 'query' || requestedTemplate === 'pillar') {
    return requestedTemplate
  }

  const normalized = (keyword || '').trim().toLowerCase()
  const pillarSignals = [
    'guide',
    'complete guide',
    'overview',
    'introduction',
    'stackup',
    'surface finish',
    'surface finishes',
    'testing',
    'inspection',
    'materials',
    'high speed pcb',
    'rigid flex pcb',
    'rigid-flex pcb',
    'what is pcb stackup',
    'pcb testing and inspection'
  ]
  const querySignals = [
    'what is',
    'how to',
    'vs',
    'difference between',
    'cost',
    'lead time',
    'troubleshooting',
    'impedance control',
    'microvia reliability',
    'enig vs osp',
    'warpage'
  ]

  if (querySignals.some((token) => normalized.includes(token))) {
    return 'query'
  }

  if (pillarSignals.some((token) => normalized.includes(token))) {
    return 'pillar'
  }

  return normalized.split(/\s+/).length <= 4 ? 'pillar' : 'query'
}

export function buildArticleFromEvidencePrompt(input) {
  return [
    `你现在要基于已准备好的证据包，为 ${input.siteKey.toUpperCase()} 生成一篇真实可发布的中文技术博客。`,
    `目标语言：${input.locale}`,
    `主关键词：${input.keyword}`,
    `页面类型：${input.templateType}`,
    '',
    '你必须严格依据下面的证据包写作；证据包没有提供的硬数字，不要补造。',
    '',
    '证据包：',
    sanitizeModelText(input.evidenceText),
    '',
    '共享主提示词：',
    input.sharedPrompt.trim(),
    '',
    '站点 overlay：',
    input.siteOverlay.trim(),
    '',
    '可用内链池：',
    input.internalLinkPool.trim(),
    '',
    '补充执行要求：',
    '- 本轮不要再联网搜索，直接基于证据包与模板生成。',
    '- 只输出最终 Markdown。',
    '- frontmatter 之后必须输出一个且仅一个正文 H1，大标题默认与 frontmatter.title 保持一致或高度一致；不要缺失 H1。',
    '- H1 下方先给 4-6 条短结论构成的顶部答案块，默认不要机械输出“## 直接回答”这类小标题。',
    '- 在顶部答案块之后增加一个可被 AI 单独摘录的定义型摘要块，控制在 40-60 词左右。',
    '- 长文默认添加目录，放在顶部答案块与定义型摘要块之后。',
    '- 保留 FAQ 包裹注释。',
    '- 正文出现具体数值、标准目标、材料参数、测试方法或公开结论时，必须加入自然的内联来源归因，例如“根据某规范”“某 datasheet 给出”“某 layout guide 指出”。',
    '- 文章结尾必须增加“公开参考资料”或“Sources”区块，至少 3 条可点击公开来源，并说明各自支撑的正文结论。',
    '- FAQ 问题优先使用自然语言搜索问句和 query phrasing，不要只写目录式标题。',
    '- 作者与审核信息优先使用真实可识别实体；如没有真实姓名，也要写清团队边界和审核责任。',
    '- 如果主题适合在前 30% 内容里并列呈现 trade-off、风险、推荐动作或验证路径，可以加入 1 组轻量 HTML 卡片；不适合则不要强加。',
    '- 参数密集型或工程控制型主题优先考虑“早期表格 + 4-card HTML 卡片”；成本优化、优先级排序、比较矩阵类主题优先考虑“早期表格 + 补充表格”。',
    '- HTML 卡片不是装饰块。卡片内容必须表达工程结论、风险信号、验证动作、冻结项或选型提醒，不能写空泛营销文案。',
    '- 如果使用 HTML 卡片，配色要跟主题走，不要随机换色，也不要在相邻文章里机械复用同一套主色、渐变和视觉气质。',
    '- 配色方向要保持工程感与高对比度，例如：材料/表面处理偏工艺与材料色，功率/热管理偏工业能量色，医疗/低噪声偏洁净克制色，高频高速/阻抗偏冷静技术色。',
    '- 内链优先产品页、服务页、工具页，分布要均衡。',
    '- 不要泄露证据包、模板、提示词等内部术语。'
  ].join('\n')
}


export function resolveSiteAssets(siteKey, templateType) {
  const site = SITE_CONFIGS[siteKey]
  if (!site) {
    throw new Error(`Unsupported site: ${siteKey}`)
  }

  const sharedPromptPath = SHARED_PROMPT_PATHS[templateType]
  if (!sharedPromptPath) {
    throw new Error(`Unsupported template type: ${templateType}`)
  }

  const overlayPath =
    templateType === 'pillar' ? site.pillarOverlayPath : site.queryOverlayPath

  return {
    locale: site.locale,
    sharedPromptPath,
    overlayPath,
    internalLinkPoolPath: site.internalLinkPoolPath
  }
}

export function loadSitePromptBundle(siteKey, templateType) {
  const assets = resolveSiteAssets(siteKey, templateType)
  return {
    locale: assets.locale,
    sharedPrompt: readTextFile(assets.sharedPromptPath),
    siteOverlay: readTextFile(assets.overlayPath),
    internalLinkPool: readTextFile(assets.internalLinkPoolPath)
  }
}

export function parseCliArgs(argv) {
  const args = {
    site: 'hilpcb',
    template: 'auto',
    locale: 'zh-CN',
    outputDir: path.join(BLOGS_ROOT, 'output'),
    keyword: '',
    keywordsFile: '',
    maxAttempts: 3
  }

  const positionals = []
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index]
    if (!token.startsWith('--')) {
      positionals.push(token)
      continue
    }

    const [rawKey, inlineValue] = token.split('=', 2)
    const key = rawKey.replace(/^--/, '')
    const value = inlineValue ?? argv[index + 1]
    const consumesNext = inlineValue == null

    if (key === 'site' && value) {
      args.site = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'template' && value) {
      args.template = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'locale' && value) {
      args.locale = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'output-dir' && value) {
      args.outputDir = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'keyword' && value) {
      args.keyword = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'keywords-file' && value) {
      args.keywordsFile = value
      if (consumesNext) index += 1
      continue
    }

    if (key === 'max-attempts' && value) {
      args.maxAttempts = Number(value) || 3
      if (consumesNext) index += 1
      continue
    }
  }

  if (!args.keyword && positionals.length > 0) {
    args.keyword = positionals.join(' ')
  }

  return args
}

export function loadKeywords(input) {
  const keywords = []

  if (input.keyword) {
    keywords.push(input.keyword.trim())
  }

  if (input.keywordsFile) {
    const content = readTextFile(input.keywordsFile)
    for (const line of content.split(/\r?\n/)) {
      const trimmed = line.trim()
      if (!trimmed || trimmed.startsWith('#')) {
        continue
      }
      keywords.push(trimmed)
    }
  }

  return [...new Set(keywords.filter(Boolean))]
}

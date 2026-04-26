import fs from 'node:fs'
import path from 'node:path'
import OpenAI from '/code/chatbot/node_modules/openai/index.mjs'

import {
  assembleLlmWikiEvidenceContext,
  buildArtifactPaths,
  buildArticleFromEvidencePrompt,
  buildEvidencePrompt,
  buildLlmWikiLookup,
  ensureDir,
  extractOutputTextFromResponsePayload,
  loadLlmWikiIndex,
  loadKeywords,
  loadRuntimeConfig,
  loadSitePromptBundle,
  looksLikeCompleteBlog,
  parseCliArgs,
  resolveLlmWikiEvidenceStrategy,
  sanitizeModelText,
  shouldUseWebSearchForLlmWikiLookup,
  shouldRetryGenerationError,
  slugify,
  timestamp,
  validateCompleteBlog,
  resolveTemplateType
} from './codex_blog_generation_lib.mjs'

const CONFIG = loadRuntimeConfig()
const LLM_WIKI_INDEX = loadLlmWikiIndex()

async function runStreamingRequest(client, input, options = {}) {
  const maxAttempts = options.maxAttempts || 3
  let attempts = 0
  let lastError = null

  while (attempts < maxAttempts) {
    attempts += 1
    let text = ''
    let searchStarted = false
    const searchQueries = []
    const citations = []

    try {
      const stream = await client.responses.create({
        model: CONFIG.model,
        stream: true,
        store: false,
        reasoning: { effort: 'medium' },
        ...(options.useWebSearch ? { tools: [{ type: 'web_search' }] } : {}),
        input: [
          {
            role: 'user',
            content: input
          }
        ]
      })

      for await (const event of stream) {
        if (
          event.type === 'response.web_search_call.searching' ||
          (event.type === 'response.output_item.added' && event.item?.type === 'web_search_call')
        ) {
          searchStarted = true
        }

        if (event.type === 'response.web_search_call.in_progress') {
          const query = event.query || event.item?.query
          if (query) {
            searchQueries.push(query)
          }
        }

        if (event.type === 'response.output_text.delta' && event.delta) {
          text += event.delta
        }

        if (
          event.type === 'response.content_part.done' &&
          Array.isArray(event.part?.annotations)
        ) {
          for (const annotation of event.part.annotations) {
            if (annotation?.type === 'url_citation') {
              citations.push({
                title: annotation.title || '',
                url: annotation.url || ''
              })
            }
          }
        }
      }

      text = sanitizeModelText(text)
      if (!text) {
        throw new Error('empty output from model')
      }

      return {
        attempts,
        text,
        searchStarted,
        searchQueries,
        citations
      }
    } catch (error) {
      lastError = error
      const message = error instanceof Error ? error.message : String(error)
      if (attempts >= maxAttempts || !shouldRetryGenerationError(message)) {
        throw error
      }
      await new Promise((resolve) => setTimeout(resolve, attempts * 2000))
    }
  }

  throw lastError || new Error('request failed without explicit error')
}

async function runNonStreamingRequest(client, input, options = {}) {
  const maxAttempts = options.maxAttempts || 3
  let attempts = 0
  let lastError = null

  while (attempts < maxAttempts) {
    attempts += 1

    try {
      const response = await client.responses.create({
        model: CONFIG.model,
        stream: false,
        store: false,
        reasoning: { effort: 'medium' },
        ...(options.useWebSearch ? { tools: [{ type: 'web_search' }] } : {}),
        input: [
          {
            role: 'user',
            content: input
          }
        ]
      })

      const text = extractOutputTextFromResponsePayload(response)
      if (!text) {
        throw new Error('empty output from model')
      }

      return {
        attempts,
        text,
        searchStarted: Boolean(options.useWebSearch),
        searchQueries: [],
        citations: []
      }
    } catch (error) {
      lastError = error
      const message = error instanceof Error ? error.message : String(error)
      if (attempts >= maxAttempts || !shouldRetryGenerationError(message)) {
        throw error
      }
      await new Promise((resolve) => setTimeout(resolve, attempts * 2000))
    }
  }

  throw lastError || new Error('request failed without explicit error')
}

async function generateOne(client, input) {
  const templateType = resolveTemplateType(input.keyword, input.template)
  const promptBundle = loadSitePromptBundle(input.site, templateType)
  const locale = input.locale || promptBundle.locale
  const llmWikiLookup = buildLlmWikiLookup(input.keyword, LLM_WIKI_INDEX)
  const localEvidenceContext = assembleLlmWikiEvidenceContext(llmWikiLookup)
  const evidenceStrategy = resolveLlmWikiEvidenceStrategy(llmWikiLookup)
  const useWebSearch = shouldUseWebSearchForLlmWikiLookup(llmWikiLookup)

  const evidencePrompt = buildEvidencePrompt({
    keyword: input.keyword,
    siteKey: input.site,
    locale,
    templateType,
    localEvidenceContext,
    allowWebSearch: useWebSearch,
    strategyMode: evidenceStrategy.mode
  })

  const evidenceResult = await runStreamingRequest(client, evidencePrompt, {
    useWebSearch,
    maxAttempts: input.maxAttempts
  })

  const articlePrompt = buildArticleFromEvidencePrompt({
    keyword: input.keyword,
    sharedPrompt: promptBundle.sharedPrompt,
    siteOverlay: promptBundle.siteOverlay,
    internalLinkPool: promptBundle.internalLinkPool,
    evidenceText: evidenceResult.text,
    siteKey: input.site,
    locale,
    templateType
  })

  let articleResult = await runNonStreamingRequest(client, articlePrompt, {
    useWebSearch: false,
    maxAttempts: input.maxAttempts
  })

  if (!looksLikeCompleteBlog(articleResult.text)) {
    articleResult = await runStreamingRequest(client, articlePrompt, {
      useWebSearch: false,
      maxAttempts: input.maxAttempts
    })
  }

  const stem = `${timestamp()}-${slugify(input.keyword)}`
  const completeArticle = looksLikeCompleteBlog(articleResult.text)
    ? validateCompleteBlog(articleResult.text)
    : null
  const artifactPaths = buildArtifactPaths({
    outputDir: input.outputDir,
    site: input.site,
    templateType,
    stem,
    status: completeArticle ? 'success' : 'failed'
  })

  ensureDir(artifactPaths.outputDir)
  fs.writeFileSync(artifactPaths.evidencePath, evidenceResult.text.trim() + '\n', 'utf8')

  if (!completeArticle) {
    fs.writeFileSync(artifactPaths.markdownPath, articleResult.text.trim() + '\n', 'utf8')
    fs.writeFileSync(
      artifactPaths.metaPath,
      JSON.stringify(
        {
          ok: false,
          site: input.site,
          templateType,
          keyword: input.keyword,
          model: CONFIG.model,
          baseUrl: CONFIG.baseUrl,
          error: 'Generated article is incomplete or truncated',
          evidence: {
            attempts: evidenceResult.attempts,
            searchStarted: evidenceResult.searchStarted,
            searchQueries: evidenceResult.searchQueries,
            citations: evidenceResult.citations,
            sourceMode: evidenceStrategy.mode,
            coverageScore: evidenceStrategy.coverageScore,
            localLlmWikiHits: llmWikiLookup.matches.map((entry) => ({
              id: entry.id,
              kind: entry.kind,
              title: entry.title,
              score: entry.score,
              path: entry.path
            })),
            evidencePath: artifactPaths.evidencePath
          },
          article: {
            attempts: articleResult.attempts,
            citations: articleResult.citations,
            markdownPath: artifactPaths.markdownPath
          }
        },
        null,
        2
      ) + '\n',
      'utf8'
    )
    throw new Error(
      `Generated article is incomplete or truncated. Archived under ${artifactPaths.outputDir}`
    )
  }

  fs.writeFileSync(artifactPaths.markdownPath, completeArticle.trim() + '\n', 'utf8')
  fs.writeFileSync(
    artifactPaths.metaPath,
    JSON.stringify(
      {
        ok: true,
        site: input.site,
        templateType,
        keyword: input.keyword,
        model: CONFIG.model,
        baseUrl: CONFIG.baseUrl,
        evidence: {
          attempts: evidenceResult.attempts,
          searchStarted: evidenceResult.searchStarted,
          searchQueries: evidenceResult.searchQueries,
          citations: evidenceResult.citations,
          sourceMode: evidenceStrategy.mode,
          coverageScore: evidenceStrategy.coverageScore,
          localLlmWikiHits: llmWikiLookup.matches.map((entry) => ({
            id: entry.id,
            kind: entry.kind,
            title: entry.title,
            score: entry.score,
            path: entry.path
          })),
          evidencePath: artifactPaths.evidencePath
        },
        article: {
          attempts: articleResult.attempts,
          citations: articleResult.citations,
          markdownPath: artifactPaths.markdownPath
        }
      },
      null,
      2
    ) + '\n',
    'utf8'
  )

  return {
    site: input.site,
    templateType,
    keyword: input.keyword,
    evidenceAttempts: evidenceResult.attempts,
    articleAttempts: articleResult.attempts,
    evidenceSourceMode: evidenceStrategy.mode,
    evidenceCoverageScore: evidenceStrategy.coverageScore,
    localLlmWikiHits: llmWikiLookup.matches.length,
    evidenceSearchStarted: evidenceResult.searchStarted,
    evidenceSearchQueriesCount: evidenceResult.searchQueries.length,
    evidencePath: artifactPaths.evidencePath,
    markdownPath: artifactPaths.markdownPath,
    metaPath: artifactPaths.metaPath
  }
}

async function main() {
  if (!CONFIG.apiKey) {
    throw new Error('No usable API key found in /root/.codex/auth.json or fallback env files')
  }

  const args = parseCliArgs(process.argv.slice(2))
  const keywords = loadKeywords(args)

  if (keywords.length === 0) {
    throw new Error('Provide a keyword or --keywords-file')
  }

  const client = new OpenAI({
    apiKey: CONFIG.apiKey,
    baseURL: CONFIG.baseUrl,
    defaultHeaders: {
      'User-Agent': 'codex-blog-generation-cli/1.0'
    }
  })

  const results = []
  for (const keyword of keywords) {
    const result = await generateOne(client, {
      site: args.site,
      template: args.template,
      locale: args.locale,
      outputDir: args.outputDir,
      maxAttempts: args.maxAttempts,
      keyword
    })
    results.push(result)
  }

  console.log(
    JSON.stringify(
      {
        ok: true,
        site: args.site,
        requestedTemplate: args.template,
        model: CONFIG.model,
        baseUrl: CONFIG.baseUrl,
        count: results.length,
        results
      },
      null,
      2
    )
  )
}

main().catch((error) => {
  console.error(
    JSON.stringify(
      {
        ok: false,
        error: error instanceof Error ? error.message : String(error)
      },
      null,
      2
    )
  )
  process.exit(1)
})

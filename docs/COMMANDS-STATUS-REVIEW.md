# SEO Max - Commands Status Review

**Date:** 25 February 2026  
**Reviewed by:** GitHub Copilot  
**Project:** SEO Max v2.0  

---

## Summary

✅ **4 out of 4 commands** described in the README are working in the old `claude-seo-main` project.

❌ **0 out of 4 commands** are implemented in the new `seo-max` v2.0 project yet.

---

## Detailed Status

### 1. ✅ `/seo page <url>` — Single Page Analysis

**Status in claude-seo-main:** ✅ **WORKING**

**Location:**
- Skill: `skills/seo-page/SKILL.md`
- Referenced in: `seo/SKILL.md`, `docs/COMMANDS.md`, `README.md`

**What it does:**
```bash
/seo page https://example.com/about
```

**Analyzes:**
- ✅ On-page SEO (title, meta description, H1, headings hierarchy)
- ✅ Content quality (word count, E-E-A-T signals, readability)
- ✅ Technical elements (canonical, robots meta, Open Graph, Twitter Card)
- ✅ Schema markup (detection, validation)
- ✅ Images (alt text, file size, format optimization)
- ✅ Core Web Vitals (LCP issues, render-blocking resources)

**Output:**
- Detailed single-page analysis report
- Issue severity levels (Critical → High → Medium → Low)
- Specific recommendations per category

---

### 2. ✅ `/seo schema <url>` — Schema Markup Analysis & Generation

**Status in claude-seo-main:** ✅ **WORKING**

**Location:**
- Skill: `skills/seo-schema/SKILL.md`
- Agent: `agents/seo-schema.md` (for parallel processing in audits)
- Templates: `schema/templates.json` (50+ ready-to-use JSON-LD snippets)
- References: `references/schema-types.md`

**What it does:**
```bash
/seo schema https://example.com
```

**Capabilities:**
- ✅ **Detect** all schema markup formats:
  - JSON-LD (preferred)
  - Microdata (itemscope, itemprop)
  - RDFa (typeof, property)

- ✅ **Validate** against Google's specifications:
  - Required properties per type
  - Data type correctness
  - Deprecated types awareness
  - Placeholder text detection
  - URL format validation

- ✅ **Generate** new schema markup:
  - 50+ schema types with templates
  - Organization, Product, Article, Event, VideoObject, etc.
  - JSON-LD format (Google's preference)
  - Ready-to-copy snippets

**Supported Schema Types (Active):**
- Organization, LocalBusiness, SoftwareApplication
- Product, ProductGroup, Offer, AggregateRating, Review
- Article, BlogPosting, NewsArticle, Person
- VideoObject, ImageObject, Event, JobPosting, Course
- BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode
- BreadcrumbList, WebSite, WebPage, ContactPage, ProfilePage
- Service, DiscussionForumPosting

**Deprecated (Never Recommend):**
- ❌ HowTo (removed Sept 2023)
- ❌ FAQ (restricted to gov/health since Aug 2023)
- ❌ SpecialAnnouncement (deprecated July 2025)

---

### 3. ✅ `/seo sitemap generate` — Sitemap Generation

**Status in claude-seo-main:** ✅ **WORKING**

**Location:**
- Skill: `skills/seo-sitemap/SKILL.md`
- Agent: `agents/seo-sitemap.md` (parallel analysis in audits)
- Industry Templates: `skills/seo-plan/assets/` (saas.md, ecommerce.md, etc.)
- Documentation: `docs/COMMANDS.md`

**What it does:**
```bash
/seo sitemap generate
```

**Full-Featured Sitemap Generation:**
- ✅ **Auto-detect** business type (SaaS, e-commerce, local, publisher, agency)
- ✅ **Interactive** structure planning with user
- ✅ **Industry templates** for 5+ business types
- ✅ **Quality gates enforcement:**
  - ⚠️ WARNING at 30+ location pages (enforce 60%+ unique content)
  - 🛑 HARD STOP at 50+ location pages (require justification)
- ✅ **Programmatic page safeguards:**
  - Validates content uniqueness
  - Detects thin content
  - Prevents doorway page penalties
- ✅ **XML generation:**
  - Valid XML format
  - Automatic sitemap index for >50k URLs
  - Split by content type (pages, posts, images, videos)
  - lastmod date generation

**Also Available:**
- ✅ `/seo sitemap <url>` — Analyze existing sitemap
  - XML validation
  - URL status code checking
  - Coverage analysis
  - Deprecated tag detection

---

### 4. ✅ `/seo insights <url>` — AI Search Optimization

**Status in claude-seo-main:** ✅ **WORKING**

**Location:**
- Skill: `skills/seo-geo/SKILL.md`
- Agent: `agents/seo-schema.md` (delegated in audits)
- New for: February 2026

**What it does:**
```bash
/seo insights https://example.com
```

**Generative Engine Optimization (GEO) Analysis:**
- ✅ **AI Visibility Analysis** for:
  - Google AI Overviews (1.5B users/month)
  - ChatGPT web search (900M weekly active)
  - Perplexity (500M+ monthly queries)
  - Other AI-powered search engines

**Key Metrics:**
- ✅ **Citability Score** (25% weight):
  - Optimal passage length: 134-167 words
  - Self-contained answer blocks
  - Quotable sentences with facts/statistics

- ✅ **Brand Mention Analysis** (critical signal):
  - YouTube mentions (~0.737 correlation)
  - Reddit mentions (high correlation)
  - Wikipedia presence
  - LinkedIn presence
  - Domain authority (weak correlation: ~0.266)

  **Key Finding:** Brand mentions correlate 3× more strongly with AI citations than backlinks!

- ✅ **AI Crawler Accessibility:**
  - GPTBot, ClaudeBot, PerplexityBot detection
  - robots.txt compliance
  - Content visibility to AI crawlers

- ✅ **Platform-Specific Optimization:**
  - Only 11% of domains cited by both ChatGPT and Google AI Overviews
  - Each platform (Google AI, ChatGPT, Perplexity) has different ranking signals
  - Tailored optimization per platform

- ✅ **llms.txt Compliance:**
  - Training data attribution
  - Citation preferences
  - Content restrictions

---

## Implementation Status: SEO Max v2.0

### Current State (25 Feb 2026)

| Command | claude-seo-main | seo-max v2.0 | Status |
|---------|-----------------|-------------|--------|
| `/seo page` | ✅ Skill exists | ❌ Not migrated | 🔴 TODO |
| `/seo schema` | ✅ Skill exists | ❌ Not migrated | 🔴 TODO |
| `/seo sitemap` | ✅ Skill exists | ❌ Not migrated | 🔴 TODO |
| `/seo insights` | ✅ Skill exists | ❌ Not migrated | 🚠 TODO |

### What Needs to be Done

**All 4 commands need to be migrated to SEO Max v2.0:**

#### Phase 1: Create Data CSVs
1. **seo-page-checks.csv** - On-page analysis rules
2. **schema-types.csv** - ✅ **ALREADY CREATED**
3. **sitemap-rules.csv** - Sitemap validation
4. **insights-signals.csv** - AI search optimization factors

#### Phase 2: Build Python Scripts
1. **page_analyzer.py** - On-page SEO analysis
2. **schema_validator.py** - Schema detection and validation
3. **sitemap.py** - Sitemap generation and validation
4. **insights_optimizer.py** - AI search optimization analysis

#### Phase 3: Integrate with CLI
1. Add commands to `src/seo/scripts/search.py`
2. BM25 ranking for each domain
3. Master + Overrides persistence for strategies

#### Phase 4: Platform Templates
1. Create SKILL.md templates for all 15 platforms
2. Update README with complete command reference
3. Add examples and usage guides

---

## Recommendation: Priority Order

### 🟢 **Already Done (✅)**
1. Schema types CSV - ✅ `src/seo/data/schema-types.csv` exists

### 🟡 **High Priority** (3 days)
2. `/seo page` - Create on-page analysis
3. `/seo schema` - Integrate with existing CSV
3. **Then `/seo insights`** — Add AI search signals

### 🟠 **High Priority** (2-3 days)
5. `/seo sitemap` - Create sitemap rules and generator

---

## Files Referenced

### Old Project (claude-seo-main)
- Skills: `skills/seo-page/`, `skills/seo-schema/`, `skills/seo-geo/`, `skills/seo-sitemap/`
- Agents: `agents/seo-schema.md`, `agents/seo-sitemap.md`
- Data: `schema/templates.json` (50+ templates)
- References: `references/schema-types.md`
- Templates: `skills/seo-plan/assets/`
- Docs: `docs/COMMANDS.md`, `README.md`

### New Project (seo-max)
- CSV: `src/seo/data/schema-types.csv` ✅
- Scripts: `src/seo/scripts/core.py` (BM25 engine) ✅
- Pending: All other Python scripts and platform templates

---

## Testing

### Test in Old Project (claude-seo-main)
To verify functionality works, you can test in Claude Code:
```bash
# Single page analysis
/seo page https://example.com/about

# Schema validation
/seo schema https://example.com

# Generate sitemap
/seo sitemap generate

# AI search optimization
/seo geo https://example.com
```

### Test in New Project (seo-max)
Currently not functional - requires migration.

---

## Conclusion

✅ **All 4 commands are fully functional in claude-seo-main**

❌ **None are implemented yet in seo-max v2.0**

**Total Migration Effort:** 5-7 days
- Phase 1: CSVs (2-3 days)
- Phase 2: Python scripts (2-3 days)
- Phase 3: CLI integration (1 day)
- Phase 4: Templates & docs (1-2 days)

**Next Steps:**
1. Prioritize which command to migrate first
2. Create CSV data structure
3. Build Python analysis/generation scripts
4. Integrate with BM25 search engine
5. Add to all 15 platform templates

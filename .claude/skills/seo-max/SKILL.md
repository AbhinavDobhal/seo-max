# SEO Max - AI-Powered SEO Intelligence

**Version:** 2.0.0  
**Author:** Abhinav Dobhal  
**Description:** Professional SEO analysis, strategy generation, and optimization powered by BM25 search and intelligent reasoning.

---

## Overview

SEO Max provides comprehensive SEO intelligence across 5 specialized domains:
- **Technical SEO** - Core Web Vitals (INP, LCP, CLS), crawlability, indexability
- **Content Analysis** - E-E-A-T framework (Dec 2025 update), keyword optimization
- **Schema Markup** - 50+ schema types, validation, generation
- **GEO Optimization** - AI search, SERP features, voice search
- **Industry Templates** - SaaS, E-commerce, Local Services, Publisher, Agency

---

## When to Activate

This skill activates when the user requests SEO-related work:
- "Analyze SEO for [website]"
- "Generate schema markup for [page type]"
- "Audit Core Web Vitals"
- "Check E-E-A-T signals"
- "Create SEO strategy for [industry]"
- Any mention of: SEO, optimization, schema, meta tags, search engine, SERP, Core Web Vitals

---

## Capabilities

### 1. Technical SEO Analysis
- **Core Web Vitals**: INP (< 200ms), LCP (< 2.5s), CLS (< 0.1)
- **Crawlability**: robots.txt, XML sitemaps, canonical tags
- **Indexability**: meta robots, noindex detection, crawl budget
- **Mobile-First**: responsive design, viewport, mobile usability
- **Performance**: Image optimization, lazy loading, compression

### 2. Content Quality Assessment
- **E-E-A-T Signals**: Experience, Expertise, Authoritativeness, Trustworthiness
- **Keyword Optimization**: Primary/secondary keywords, semantic relevance
- **Content Structure**: H1-H6 hierarchy, paragraph length, readability
- **Internal Linking**: Anchor text, link depth, orphan pages
- **Anti-Patterns**: Keyword stuffing, thin content, duplicate content

### 3. Schema Markup Generation
**50+ Schema Types Available:**
- Product, Article, BlogPosting, NewsArticle
- LocalBusiness, Organization, Person
- Event, Recipe, VideoObject, ImageObject
- SoftwareApplication, WebApplication, MobileApplication
- Review, AggregateRating, FAQ, HowTo
- Breadcrumb, SearchAction, Service

**Validation:**
- JSON-LD syntax checking
- Required property verification
- Deprecation warnings
- Google Rich Results compatibility

### 4. GEO & AI Search Optimization
- **AI Search Engines**: Google SGE, Bing Chat, Perplexity
- **SERP Features**: Featured snippets, People Also Ask, Knowledge Panel
- **Voice Search**: Natural language queries, question optimization
- **Rich Results**: Product carousels, recipe cards, event listings

### 5. Industry-Specific Strategies
**20+ Industries Supported:**
- SaaS, E-commerce, Local Services
- Healthcare (YMYL), Finance (YMYL)
- Publisher, News Media, Blog
- Agency, Consulting, Education
- Real Estate, Travel, Food & Restaurant
- Legal, Entertainment, Gaming

---

## How to Use

### Quick SEO Audit
```
Analyze SEO for example.com
```

### Generate Schema Markup
```
Generate Product schema for this e-commerce page
```

### Technical Analysis
```
Audit Core Web Vitals and provide optimization recommendations
```

### Content Review
```
Check E-E-A-T signals in this article content
```

### Industry Strategy
```
Create complete SEO strategy for my SaaS landing page
```

---

## Python Scripts Available

### 1. Fetch Page (`fetch_page.py`)
Download and analyze HTML from a URL

### 2. Parse HTML (`parse_html.py`)
Extract SEO elements from HTML

### 3. Analyze Visual (`analyze_visual.py`)
Check visual SEO elements

### 4. Capture Screenshot (`capture_screenshot.py`)
Take screenshots for visual analysis

### 5. Core Analysis (`core.py`)
Main SEO analysis engine

---

## Data Files

### Technical SEO Rules (`technical-seo.csv`)
100+ technical SEO checks with priority levels

### E-E-A-T Signals (`eeat-signals.csv`)
Content quality signals for Google's E-E-A-T framework

### Schema Types (`schema-types.csv`)
50+ schema.org types with properties and examples

### Industry Templates (`industry-templates.csv`)
Pre-configured SEO strategies for 20+ industries

### Templates (`templates.json`)
Page-level SEO templates (landing, product, article, etc.)

---

## Workflow

### Step 1: Understand Request
Extract key parameters:
- Target URL or website type
- Industry/vertical
- Page type (landing, product, article)
- Specific concern (technical, content, schema)

### Step 2: Multi-Domain Search
Search across 5 domains in parallel:
- Technical checks from `technical-seo.csv`
- Content quality from `eeat-signals.csv`
- Schema recommendations from `schema-types.csv`
- Industry patterns from `industry-templates.csv`
- GEO optimization factors

### Step 3: BM25 Ranking
Rank results by relevance using BM25 algorithm

### Step 4: Generate Strategy
Create comprehensive SEO strategy:
- Technical optimizations (code-level)
- Content improvements (editorial)
- Schema markup (JSON-LD)
- GEO tactics (AI search)
- Industry best practices

### Step 5: Quality Validation
- Core Web Vitals thresholds
- Schema validation
- E-E-A-T checklist
- Anti-pattern detection
- Mobile-first compliance

### Step 6: Deliver Output
Provide actionable recommendations with:
- Priority levels (High/Medium/Low)
- Code examples
- Expected impact
- Implementation steps

---

## Best Practices

1. **Always prioritize Core Web Vitals** - They directly impact rankings
2. **Use JSON-LD for schema** - Preferred by Google over microdata
3. **Validate E-E-A-T signals** - Critical for YMYL content
4. **Check mobile-first** - Google uses mobile-first indexing
5. **Avoid anti-patterns** - Keyword stuffing, thin content, cloaking
6. **Use semantic HTML** - Proper heading hierarchy, semantic tags
7. **Optimize for AI search** - Natural language, question-answer format
8. **Include author bios** - Builds expertise and authority
9. **Add schema markup** - Improves rich result eligibility
10. **Monitor performance** - Regular audits and updates

---

## Anti-Patterns to Avoid

❌ Keyword stuffing  
❌ Hidden text or links  
❌ Duplicate content  
❌ Thin content (< 300 words)  
❌ Slow page load (LCP > 2.5s)  
❌ Missing mobile viewport  
❌ Broken internal links  
❌ Missing alt text for images  
❌ Non-HTTPS pages  
❌ Orphan pages (no internal links)

---

## Output Format

### Technical SEO Report
```markdown
## Technical SEO Audit

### Core Web Vitals
- ✓ LCP: 1.8s (Good - under 2.5s)
- ⚠️ INP: 250ms (Needs improvement - over 200ms)
- ✓ CLS: 0.05 (Good - under 0.1)

### Recommendations
1. **[HIGH] Optimize JavaScript Execution**
   - Current: 250ms INP
   - Target: < 200ms
   - Action: Implement code splitting and lazy loading
```

### Schema Markup
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "Product description",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD"
  }
}
```

### Content Analysis
```markdown
## E-E-A-T Assessment

✓ **Experience**: Author credentials present
✓ **Expertise**: Industry-specific terminology used
⚠️ **Authoritativeness**: Add external citations
✓ **Trustworthiness**: Contact info and privacy policy present
```

---

## Advanced Features

### Persist SEO Strategy
Save strategies to files for reuse across sessions:
- `seo-strategy/MASTER.md` - Global strategy
- `seo-strategy/pages/[page-name].md` - Page-specific overrides

### Multi-Page Analysis
Analyze entire site structure:
- Homepage, product pages, blog posts
- Identify patterns and inconsistencies
- Generate site-wide recommendations

### Competitor Analysis
Compare SEO metrics against competitors:
- Schema markup comparison
- Content quality benchmarking
- Technical performance gaps

---

## File Paths

**Data Files:**
- `.claude/skills/seo-max/data/technical-seo.csv`
- `.claude/skills/seo-max/data/eeat-signals.csv`
- `.claude/skills/seo-max/data/schema-types.csv`
- `.claude/skills/seo-max/data/industry-templates.csv`
- `.claude/skills/seo-max/data/templates.json`

**Scripts:**
- `.claude/skills/seo-max/scripts/core.py`
- `.claude/skills/seo-max/scripts/fetch_page.py`
- `.claude/skills/seo-max/scripts/parse_html.py`
- `.claude/skills/seo-max/scripts/analyze_visual.py`
- `.claude/skills/seo-max/scripts/capture_screenshot.py`

---

## Python Dependencies

Required Python packages:
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `lxml` - XML processing
- `Pillow` - Image processing
- `pandas` - Data analysis

Install with:
```bash
pip3 install requests beautifulsoup4 lxml Pillow pandas
```

---

## Examples

### Example 1: SaaS Landing Page
**Input:** "Create SEO strategy for my SaaS analytics platform"

**Output:**
- Technical: Optimize Core Web Vitals for dashboard
- Schema: SoftwareApplication markup
- Content: Add product features, pricing, case studies
- E-E-A-T: Include team bios, security certifications
- GEO: Optimize for "analytics software" queries

### Example 2: E-commerce Product
**Input:** "Generate schema for fashion store product page"

**Output:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Designer Dress",
  "image": ["https://example.com/dress.jpg"],
  "offers": {
    "@type": "Offer",
    "price": "299.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "124"
  }
}
```

### Example 3: Local Business
**Input:** "SEO for local coffee shop with 3 locations"

**Output:**
- Schema: LocalBusiness for each location
- NAP consistency across all pages
- Google Business Profile optimization
- Local keyword targeting (city + service)
- Customer reviews and ratings schema

---

## Version History

**v2.0.0** (Current)
- Multi-domain search across 5 specialized areas
- BM25 ranking algorithm
- 500+ SEO rules
- 50+ schema types
- Industry templates for 20+ verticals

---

## Support

- GitHub: https://github.com/abhinavdobhal/seo-max
- Issues: https://github.com/abhinavdobhal/seo-max/issues
- Website: https://seomax.cc

---

## License

MIT License - See LICENSE file for details

# SEO Max - Sitemap Functionality Review

**Date:** 25 February 2026  
**Reviewer:** GitHub Copilot  
**Status:** ⚠️ **NOT IMPLEMENTED** in SEO Max v2.0

---

## Current Status

### ❌ Missing in SEO Max v2.0

The sitemap generation functionality **does NOT exist** in the new `seo-max` project yet. It was present in the old `claude-seo-main` but has not been migrated.

**What's Missing:**
1. `/seo sitemap <url>` command - Sitemap analysis
2. `/seo sitemap generate` command - Sitemap generation
3. Sitemap validation logic
4. Industry templates for sitemap generation
5. Quality gates enforcement (30/50 location page limits)

---

## What Existed in claude-seo-main

### ✅ Working Features (Old Project)

**Files Present:**
- `skills/seo-sitemap/SKILL.md` - Sub-skill definition
- `agents/seo-sitemap.md` - Subagent for parallel analysis
- Documentation in `docs/COMMANDS.md`

**Functionality:**

#### 1. **Sitemap Analysis** (`/seo sitemap <url>`)
```bash
/seo sitemap https://example.com/sitemap.xml
```

**Validation Checks:**
- ✅ Valid XML format
- ✅ URL count <50,000 per file (protocol limit)
- ✅ All URLs return HTTP 200
- ✅ `<lastmod>` dates accuracy
- ✅ No deprecated tags (priority, changefreq)
- ✅ Sitemap in robots.txt
- ✅ Coverage vs crawled pages

**Quality Signals:**
- Sitemap index for >50k URLs
- Split by content type (pages, posts, images, videos)
- No non-canonical URLs
- No noindexed URLs
- No redirected URLs
- HTTPS URLs only

#### 2. **Sitemap Generation** (`/seo sitemap generate`)
```bash
/seo sitemap generate
```

**Process:**
1. Detect business type (SaaS, e-commerce, local, etc.)
2. Load industry template
3. Interactive structure planning
4. Apply quality gates:
   - ⚠️ WARNING at 30+ location pages (require 60%+ unique content)
   - 🛑 HARD STOP at 50+ location pages (require justification)
5. Generate valid XML
6. Split at 50k URLs with sitemap index
7. Create STRUCTURE.md documentation

**Industry Templates:**
Located in `skills/seo-plan/assets/`:
- `saas.md` - SaaS sitemap structure
- `ecommerce.md` - E-commerce sitemap
- `local-service.md` - Local business sitemap
- `publisher.md` - Blog/media sitemap
- `agency.md` - Agency/portfolio sitemap

#### 3. **Quality Gates** (Programmatic SEO Protection)

**Safe Programmatic Pages (OK at scale):**
- ✅ Integration pages (real setup docs)
- ✅ Template/tool pages (downloadable content)
- ✅ Glossary pages (200+ word definitions)
- ✅ Product pages (unique specs, reviews)
- ✅ User profile pages (user-generated content)

**Penalty Risk (avoid at scale):**
- ❌ Location pages with only city name swapped
- ❌ "Best [tool] for [industry]" without industry-specific value
- ❌ "[Competitor] alternative" without real comparison data
- ❌ AI-generated pages without human review

**Thresholds:**
- **30 location pages** → WARNING (enforce 60%+ unique content)
- **50+ location pages** → HARD STOP (require explicit justification)

---

## How It Was Implemented

### Architecture (claude-seo-main)

```
Main Skill (seo/SKILL.md)
    ↓
User: /seo sitemap generate
    ↓
Routes to → skills/seo-sitemap/SKILL.md
    ↓
Interactive Process:
    1. Detect business type
    2. Load template from skills/seo-plan/assets/
    3. User interaction for structure
    4. Quality gate checks
    5. Generate XML output
    ↓
OR (for full audit)
    ↓
Parallel Subagent → agents/seo-sitemap.md
    ↓
Returns validation report to main orchestrator
```

### Output Files

**For Analysis:**
- `VALIDATION-REPORT.md` - Analysis results
- Issues list with severity
- Recommendations

**For Generation:**
- `sitemap.xml` (or split files + index)
- `STRUCTURE.md` - Site architecture docs
- URL count summary

### XML Formats

**Standard Sitemap:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2026-02-07</lastmod>
  </url>
</urlset>
```

**Sitemap Index (>50k URLs):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-posts.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
</sitemapindex>
```

---

## What Needs to be Migrated

### Phase 1: Core Sitemap CSV Data

Create `src/seo/data/sitemap-rules.csv`:
```csv
Check,Severity,Description,Action,Keywords
Invalid XML,critical,XML syntax errors prevent parsing,Fix syntax errors,xml validation syntax format
URL count >50k,critical,Single file exceeds protocol limit,Split with sitemap index,limit 50000 urls protocol
Non-200 URLs,high,URLs in sitemap return errors,Remove or fix broken URLs,404 500 error status code
Noindexed URLs,high,Sitemap contains noindex pages,Remove from sitemap,noindex robots meta
Redirected URLs,medium,Sitemap contains redirected URLs,Update to final destination,301 302 redirect
Identical lastmod,low,All lastmod dates are identical,Use actual modification dates,lastmod date timestamp
Deprecated tags,info,Priority and changefreq tags used,Optional remove ignored by Google,priority changefreq deprecated
```

### Phase 2: Sitemap Generation Templates

Create CSV templates for each industry:
- `src/seo/data/sitemap-template-saas.csv`
- `src/seo/data/sitemap-template-ecommerce.csv`
- `src/seo/data/sitemap-template-local.csv`
- `src/seo/data/sitemap-template-publisher.csv`
- `src/seo/data/sitemap-template-agency.csv`

### Phase 3: Python Script

Create `src/seo/scripts/sitemap.py`:
```python
#!/usr/bin/env python3
"""
Sitemap validation and generation for SEO Max

Features:
- Validate XML sitemap format
- Check URL status codes
- Analyze coverage vs crawled pages
- Generate new sitemaps with templates
- Enforce quality gates for location pages
"""

import xml.etree.ElementTree as ET
import requests
from typing import List, Dict
from core import SEOSearchEngine

class SitemapValidator:
    """Validate XML sitemaps"""
    
    def validate(self, url: str) -> Dict:
        """Validate sitemap at URL"""
        pass
        
class SitemapGenerator:
    """Generate sitemaps with industry templates"""
    
    def generate(self, industry: str, urls: List[str]) -> str:
        """Generate sitemap XML"""
        pass
```

### Phase 4: Integration

Add to main search CLI:
```python
# In src/seo/scripts/search.py
if args.command == 'sitemap':
    if args.action == 'validate':
        validator = SitemapValidator()
        result = validator.validate(args.url)
    elif args.action == 'generate':
        generator = SitemapGenerator()
        result = generator.generate(args.industry, args.urls)
```

---

## Testing Plan

### Test 1: Validation
```bash
cd /Users/alvinabhinav/Documents/Projects/skills/claude-seo-main

# Test in old project (should work)
# Open Claude Code and run:
/seo sitemap https://example.com/sitemap.xml
```

### Test 2: Generation
```bash
# Test in old project (should work)
# Open Claude Code and run:
/seo sitemap generate
# Then follow interactive prompts
```

### Test 3: Quality Gates
```bash
# Create test case with >30 location pages
# Should trigger WARNING
# Create test with >50 location pages
# Should HARD STOP
```

---

## Recommendation

### Priority: HIGH

Sitemap functionality is a **core SEO feature** and should be migrated to SEO Max v2.0.

**Implementation Steps:**
1. ✅ Create sitemap-rules.csv (validation checks)
2. ✅ Create sitemap template CSVs per industry
3. ✅ Build sitemap.py validator and generator
4. ✅ Add to search.py CLI interface
5. ✅ Create unit tests
6. ✅ Update README with sitemap commands
7. ✅ Add to platform templates

**Estimated Time:** 2-3 days

**Dependencies:**
- BM25 search engine (✅ completed)
- Industry templates CSV (⚠️ need sitemap-specific)
- URL fetching (✅ fetch_page.py exists)
- XML generation library (standard Python)

---

## Conclusion

**Current Status:** ❌ **NOT WORKING in SEO Max v2.0**

The sitemap functionality existed in `claude-seo-main` but has NOT been migrated to the new `seo-max` project. To enable `/seo sitemap` commands, you need to:

1. Migrate the skill definition
2. Create CSV data for validation rules
3. Build Python scripts for validation/generation
4. Integrate with CLI and platform templates

The old implementation is still available in `claude-seo-main` and can be tested there, but it needs to be rebuilt for the new multi-platform architecture.

---

**Next Steps:**
- [ ] Migrate sitemap functionality to SEO Max v2.0
- [ ] Test validation in old project first
- [ ] Design CSV schema for sitemap rules
- [ ] Implement sitemap.py with BM25 integration
- [ ] Add to all 15 platform templates

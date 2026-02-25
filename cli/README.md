# SEO Max CLI

Command-line interface for SEO Max v2.0.0

## Quick Start

```bash
# Show help
seo-max --help

# Show version
seo-max --version

# Analyze a page
seo-max page https://example.com

# Check schema
seo-max schema https://example.com

# Run full audit
seo-max explore https://example.com
```

## Commands

- `page <url>` — Analyze single page
- `schema <url>` — Validate schema markup
- `insights <url>` — AI search optimization
- `sitemap <url>` — Analyze sitemap
- `explore <url>` — Full site audit

## Usage in Code

```javascript
const seoMax = require('seo-max');

console.log(seoMax.version);      // v2.0.0
console.log(seoMax.name);         // seo-max
console.log(seoMax.config);       // Configuration object
```

## Integration

Works with:
- Claude (claude.ai)
- Cursor (cursor.sh)
- Copilot (GitHub Copilot)
- Windsurf
- Continue (continue.dev)

## License

MIT — See LICENSE in root directory

# SEO Max

<p align="center">
  <img src="https://img.shields.io/npm/v/seo-max?style=for-the-badge&logo=npm&label=CLI" alt="npm">
  <img src="https://img.shields.io/badge/platforms-15+-green?style=for-the-badge" alt="15+ Platforms">
  <img src="https://img.shields.io/badge/python-3.8+-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+">
  <img src="https://img.shields.io/github/license/abhinavdobhal/seo-max?style=for-the-badge&color=blue" alt="License">
</p>

<p align="center">
  <b>🚀 AI-powered SEO intelligence across 15+ coding assistants</b><br>
  <i>Professional SEO analysis, strategy generation, and optimization powered by BM25 search and intelligent reasoning</i>
</p>

<p align="center">
  <a href="https://abhinavdobhal.github.io/seo-max">Website</a> •
  <a href="#installation">Installation</a> •
  <a href="#features">Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Docs</a>
</p>

---

## What's New in v2.0

### Intelligent SEO Strategy Generation

**SEO Max v2.0** introduces an AI-powered reasoning engine that analyzes your website and generates a complete, tailored SEO strategy in seconds.

**Multi-Domain Analysis** - Parallel search across:
- ✅ Technical SEO (Core Web Vitals, crawlability, indexability)
- ✅ Content Quality (E-E-A-T signals, keyword optimization)
- ✅ Schema Markup (validation, generation, recommendations)
- ✅ AI Search Insights (search visibility, platform signals)
- ✅ Industry Templates (SaaS, E-commerce, Local, etc.)

### How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  1. USER REQUEST                                                │
│     "Analyze SEO for my SaaS product website"                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. MULTI-DOMAIN SEARCH (5 parallel searches)                   │
│     • Technical checks (100+ rules)                             │
│     • Content analysis (E-E-A-T framework)                      │
│     • Schema recommendations (50+ types)                        │
│     • Industry matching (20+ verticals)                         │
│     • GEO factors (AI search optimization)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. REASONING ENGINE (BM25 Ranking)                             │
│     • Match industry → SEO strategy rules                       │
│     • Apply priority ranking                                    │
│     • Filter anti-patterns                                      │
│     • Process decision rules                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. COMPLETE SEO STRATEGY OUTPUT                                │
│     Technical + Content + Schema + GEO + Industry Best Practices│
└─────────────────────────────────────────────────────────────────┘
```

---

## Features

- **🔍 Technical SEO** - Core Web Vitals (INP, LCP, CLS), crawlability, indexability, mobile-first
- **📝 Content Analysis** - E-E-A-T framework (Dec 2025 update), keyword optimization, content quality
- **🏷️ Schema Markup** - 50+ schema types, validation, generation, deprecation awareness
- **🤖 GEO Optimization** - AI search optimization, SERP features, voice search
- **🏭 Industry Templates** - SaaS, E-commerce, Local Services, Publisher, Agency
- **📊 BM25 Search Engine** - Algorithmic ranking across 500+ SEO rules
- **🎯 Smart Recommendations** - Industry-specific strategies with anti-patterns
- **💾 Persistence** - Master + Overrides pattern for hierarchical SEO strategies
- **🌐 15+ Platforms** - Claude Code, Cursor, Windsurf, Copilot, Continue, and more

---

## Installation

### Using CLI (Recommended)

```bash
# Install CLI globally
npm install -g seo-max

# Go to your project
cd /path/to/your/project

# Install for your AI assistant
seomax init --ai claude      # Claude Code
seomax init --ai cursor      # Cursor
seomax init --ai windsurf    # Windsurf
seomax init --ai copilot     # GitHub Copilot
seomax init --ai continue    # Continue
seomax init --ai antigravity # Antigravity
seomax init --ai kiro        # Kiro
seomax init --ai codex       # Codex CLI
seomax init --ai roocode     # Roo Code
seomax init --ai gemini      # Gemini CLI
seomax init --ai trae        # Trae
seomax init --ai qoder       # Qoder
seomax init --ai codebuddy   # CodeBuddy
seomax init --ai droid       # Droid (Factory)
seomax init --ai all         # All assistants
```

### Other CLI Commands

```bash
seomax versions              # List available versions
seomax update                # Update to latest version
seomax init --offline        # Skip GitHub download, use bundled assets
```

---

## Prerequisites

Python 3.8+ is required for analysis scripts.

```bash
# Check if Python is installed
python3 --version

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```

---

## Usage

### Skill Mode (Auto-activate)

**Supported:** Claude Code, Cursor, Windsurf, Antigravity, Codex CLI, Continue, Gemini CLI, OpenCode, Qoder, CodeBuddy, Droid (Factory)

The skill activates automatically when you request SEO work. Just chat naturally:

```
Analyze SEO for example.com
```

### Workflow Mode (Slash Command)

**Supported:** Kiro, GitHub Copilot, Roo Code

Use the slash command to invoke the skill:

```
/seo audit example.com
```

### Example Prompts

```
Audit this website for SEO issues

Generate schema markup for a product page

Analyze Core Web Vitals performance

Check E-E-A-T signals in this content

Create SEO strategy for SaaS landing page
```

---

## Advanced: SEO Strategy Generator

Generate complete SEO strategies directly:

```bash
# Generate SEO strategy with ASCII output
python3 .claude/skills/seo-max/scripts/search.py "saas product" --seo-strategy -p "MyApp"

# Generate with Markdown output
python3 .claude/skills/seo-max/scripts/search.py "ecommerce" --seo-strategy -f markdown

# Domain-specific search
python3 .claude/skills/seo-max/scripts/search.py "core web vitals" --domain technical
python3 .claude/skills/seo-max/scripts/search.py "product schema" --domain schema
python3 .claude/skills/seo-max/scripts/search.py "eeat signals" --domain content

# Industry-specific search
python3 .claude/skills/seo-max/scripts/search.py "saas seo" --industry saas
```

### Persist SEO Strategy (Master + Overrides Pattern)

Save your SEO strategy to files for hierarchical retrieval across sessions:

```bash
# Generate and persist to seo-strategy/MASTER.md
python3 .claude/skills/seo-max/scripts/search.py "example.com" --seo-strategy --persist -p "MyProject"

# Also create a page-specific override file
python3 .claude/skills/seo-max/scripts/search.py "blog post" --persist -p "MyProject" --page "blog"
```

This creates a `seo-strategy/` folder structure:

```
seo-strategy/
├── MASTER.md           # Global SEO Strategy (technical, content, schema)
└── pages/
    └── blog.md         # Page-specific overrides (only deviations from Master)
```

---

## Supported Platforms

| Platform | Mode | Installation Path |
|----------|------|-------------------|
| **Claude Code** | Skill Mode | `~/.claude/skills/seo-max/` |
| **Cursor** | Skill Mode | `.cursor/seo-max/` + `.cursorrules` |
| **Windsurf** | Skill Mode | `.windsurf/seo-max/` |
| **Continue** | Skill Mode | `.continue/skills/seo-max/` |
| **Antigravity** | Skill Mode | `.antigravity/seo-max/` |
| **Codex CLI** | Skill Mode | `.codex/skills/seo-max/` |
| **Gemini CLI** | Skill Mode | `.gemini/skills/seo-max/` |
| **OpenCode** | Skill Mode | `.opencode/skills/seo-max/` |
| **Qoder** | Skill Mode | `.qoder/skills/seo-max/` |
| **CodeBuddy** | Skill Mode | `.codebuddy/skills/seo-max/` |
| **Droid (Factory)** | Skill Mode | `.factory/skills/seo-max/` |
| **GitHub Copilot** | Workflow Mode | Uses workspace `/seo-max` command |
| **Kiro** | Workflow Mode | Uses `/seo-max` command |
| **Roo Code** | Workflow Mode | Uses `/seo-max` command |
| **Trae** | Skill Mode (SOLO) | `.trae/skills/seo-max/` |

---

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Platform Comparison](docs/PLATFORMS.md)
- [Search Engine Usage](docs/SEARCH-ENGINE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contributing](docs/CONTRIBUTING.md)

---

## Star History

If you find this useful, please ⭐ star the repository!

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## About

**SEO Max** - Professional SEO intelligence for AI coding assistants

Created by **Abhinav Dobhal**

Other projects: [Portfolio](https://github.com/AbhinavDobhal)

---

<p align="center">
  <b>If you find this useful, consider supporting the project:</b><br><br>
  ⭐ <a href="https://github.com/abhinavdobhal/seo-max">Star on GitHub</a>
</p>

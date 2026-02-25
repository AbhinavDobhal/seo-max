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

# Initialize for your AI assistant (automatically sets up Python environment)
seo-max init --ai claude      # Claude Code
seo-max init --ai cursor      # Cursor
seo-max init --ai windsurf    # Windsurf
seo-max init --ai copilot     # GitHub Copilot
seo-max init --ai continue    # Continue
seo-max init --ai antigravity # Antigravity
seo-max init --ai kiro        # Kiro
seo-max init --ai codex       # Codex CLI
seo-max init --ai roocode     # Roo Code
seo-max init --ai gemini      # Gemini CLI
seo-max init --ai trae        # Trae
seo-max init --ai qoder       # Qoder
seo-max init --ai codebuddy   # CodeBuddy
seo-max init --ai droid       # Droid (Factory)
seo-max init --ai all         # All assistants
```

**What `seo-max init` does:**
1. ✅ Copies all skill files to the AI assistant's folder
2. ✅ Creates Python virtual environment (`.venv`)
3. ✅ Installs all dependencies from `requirements.txt`
4. ✅ Makes everything ready to use immediately

### Other CLI Commands

```bash
seo-max --version             # Show version number
seo-max --help                # Show help information
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

### Setting Up Python Environment

**The `seo-max init` command automatically handles Python setup!**

If you installed using `seo-max init --ai <platform>`, Python environment is already configured. Skip to [Running SEO Analyzers](#running-seo-analyzers).

#### Manual Setup (if needed)

If you prefer manual setup or need to reconfigure:

```bash
# Navigate to skills folder
cd ~/.claude/skills/seo-max  # macOS/Linux
cd %USERPROFILE%\.claude\skills\seo-max  # Windows

# Run the automated setup script
./setup.sh  # macOS/Linux
setup.bat   # Windows
```

**Or completely manual:**

```bash
# Navigate to skills folder
cd ~/.claude/skills/seo-max  # macOS/Linux
cd %USERPROFILE%\.claude\skills\seo-max  # Windows

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running SEO Analyzers

After running the setup, you can execute the five core analyzers:

```bash
# Navigate to skills folder
cd ~/.claude/skills/seo-max

# Activate virtual environment (if not already active)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows

# Run analyzers
python3 scripts/page_analyzer.py https://example.com
python3 scripts/schema_validator.py https://example.com
python3 scripts/insights_optimizer.py https://example.com
python3 scripts/sitemap.py https://example.com/sitemap.xml
python3 scripts/site_crawler.py https://example.com
```

**Example Output:**
```
All five analyzers have been initialized for example.com:

✅ page_analyzer.py - Page-level SEO analysis complete
✅ schema_validator.py - Schema markup validation complete
✅ insights_optimizer.py - AI optimization insights complete
✅ sitemap.py - Sitemap analysis complete
✅ site_crawler.py - Site crawl complete
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

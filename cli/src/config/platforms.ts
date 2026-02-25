import type { AIType, PlatformConfig } from '../types';

export const platformConfigs: Record<Exclude<AIType, 'all'>, PlatformConfig> = {
  claude: {
    platform: 'claude',
    displayName: 'Claude Code',
    installType: 'full',
    folderStructure: {
      root: '.claude',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.claude/skills/seo-max/scripts',
    frontmatter: {
      name: 'seo-max',
      description: 'AI-powered SEO intelligence - technical analysis, E-E-A-T validation, schema generation, and strategic recommendations powered by BM25 search'
    },
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  cursor: {
    platform: 'cursor',
    displayName: 'Cursor',
    installType: 'full',
    folderStructure: {
      root: '.cursor',
      skillPath: 'seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.cursor/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  windsurf: {
    platform: 'windsurf',
    displayName: 'Windsurf',
    installType: 'full',
    folderStructure: {
      root: '.windsurf',
      skillPath: 'seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.windsurf/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  antigravity: {
    platform: 'antigravity',
    displayName: 'Antigravity',
    installType: 'full',
    folderStructure: {
      root: '.agent',
      skillPath: 'seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.agent/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  copilot: {
    platform: 'copilot',
    displayName: 'GitHub Copilot',
    installType: 'reference',
    folderStructure: {
      root: '.github',
      skillPath: 'copilot-instructions.md',
      filename: 'copilot-instructions.md'
    },
    scriptPath: '.shared/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: false
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'workflow'
  },
  kiro: {
    platform: 'kiro',
    displayName: 'Kiro',
    installType: 'reference',
    folderStructure: {
      root: '.kiro',
      skillPath: 'workflows/seo-max.md',
      filename: 'seo-max.md'
    },
    scriptPath: '.shared/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: false
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'workflow'
  },
  roocode: {
    platform: 'roocode',
    displayName: 'Roo Code',
    installType: 'reference',
    folderStructure: {
      root: '.roo',
      skillPath: 'workflows/seo-max.md',
      filename: 'seo-max.md'
    },
    scriptPath: '.shared/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: false
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'workflow'
  },
  codex: {
    platform: 'codex',
    displayName: 'Codex CLI',
    installType: 'full',
    folderStructure: {
      root: '.codex',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.codex/skills/seo-max/scripts',
    frontmatter: {
      name: 'seo-max',
      description: 'AI-powered SEO intelligence - technical analysis, E-E-A-T validation, schema generation, and strategic recommendations powered by BM25 search'
    },
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  qoder: {
    platform: 'qoder',
    displayName: 'Qoder',
    installType: 'full',
    folderStructure: {
      root: '.qoder',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.qoder/skills/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  gemini: {
    platform: 'gemini',
    displayName: 'Gemini CLI',
    installType: 'full',
    folderStructure: {
      root: '.gemini',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.gemini/skills/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  trae: {
    platform: 'trae',
    displayName: 'Trae',
    installType: 'full',
    folderStructure: {
      root: '.trae',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.trae/skills/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence (SOLO Mode)',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  opencode: {
    platform: 'opencode',
    displayName: 'OpenCode',
    installType: 'full',
    folderStructure: {
      root: '.opencode',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.opencode/skills/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  continue: {
    platform: 'continue',
    displayName: 'Continue',
    installType: 'full',
    folderStructure: {
      root: '.continue',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.continue/skills/seo-max/scripts',
    frontmatter: {
      name: 'seo-max',
      description: 'AI-powered SEO intelligence - technical analysis, E-E-A-T validation, schema generation, and strategic recommendations powered by BM25 search'
    },
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  codebuddy: {
    platform: 'codebuddy',
    displayName: 'CodeBuddy',
    installType: 'full',
    folderStructure: {
      root: '.codebuddy',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.codebuddy/skills/seo-max/scripts',
    frontmatter: null,
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  },
  droid: {
    platform: 'droid',
    displayName: 'Droid (Factory)',
    installType: 'full',
    folderStructure: {
      root: '.factory',
      skillPath: 'skills/seo-max',
      filename: 'SKILL.md'
    },
    scriptPath: '.factory/skills/seo-max/scripts',
    frontmatter: {
      name: 'seo-max',
      description: 'AI-powered SEO intelligence - technical analysis, E-E-A-T validation, schema generation, and strategic recommendations powered by BM25 search'
    },
    sections: {
      quickReference: true
    },
    title: 'SEO Max - Professional SEO Intelligence',
    description: 'AI-powered SEO analysis and optimization for technical, content, schema, and strategic insights',
    skillOrWorkflow: 'skill'
  }
};

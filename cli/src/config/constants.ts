export const DISPLAY_NAMES: Record<string, string> = {
  claude: 'Claude Code',
  cursor: 'Cursor',
  windsurf: 'Windsurf',
  antigravity: 'Antigravity',
  copilot: 'GitHub Copilot',
  kiro: 'Kiro',
  roocode: 'Roo Code',
  codex: 'Codex CLI',
  qoder: 'Qoder',
  gemini: 'Gemini CLI',
  trae: 'Trae',
  opencode: 'OpenCode',
  continue: 'Continue',
  codebuddy: 'CodeBuddy',
  droid: 'Droid (Factory)',
};

export const SKILL_MODE_PLATFORMS = [
  'claude',
  'cursor',
  'windsurf',
  'antigravity',
  'codex',
  'continue',
  'gemini',
  'opencode',
  'qoder',
  'codebuddy',
  'droid',
  'trae'
];

export const WORKFLOW_MODE_PLATFORMS = [
  'kiro',
  'copilot',
  'roocode'
];

export const INSTALLATION_PATHS: Record<string, string> = {
  claude: '~/.claude/skills/seo-max/',
  cursor: '.cursor/seo-max/ + .cursorrules',
  windsurf: '.windsurf/seo-max/',
  continue: '.continue/skills/seo-max/',
  antigravity: '.agent/seo-max/ + .shared/',
  codex: '.codex/skills/seo-max/',
  gemini: '.gemini/skills/seo-max/',
  opencode: '.opencode/skills/seo-max/',
  qoder: '.qoder/skills/seo-max/',
  codebuddy: '.codebuddy/skills/seo-max/',
  droid: '.factory/skills/seo-max/',
  copilot: 'Uses workspace /seo command',
  kiro: 'Uses /seo-max command',
  roocode: 'Uses /seo-max command',
  trae: '.trae/skills/seo-max/',
};

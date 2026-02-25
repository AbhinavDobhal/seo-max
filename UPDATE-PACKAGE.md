# 📦 How to Update npm Package

## Version Update Flow

### Option 1: Automatic Version Bumping (Recommended)

Use npm's built-in versioning commands:

```bash
# Patch update (2.0.0 → 2.0.1)
npm version patch

# Minor update (2.0.0 → 2.1.0)
npm version minor

# Major update (2.0.0 → 3.0.0)
npm version major
```

These commands will:
- ✅ Update package.json version
- ✅ Create a git commit
- ✅ Create a git tag

---

### Option 2: Manual Version Update

Edit `package.json` directly:

```json
{
  "name": "seo-max",
  "version": "2.0.1",  // Change this
  ...
}
```

Then manually commit:
```bash
git add package.json
git commit -m "bump: v2.0.1"
git tag v2.0.1
```

---

## Update Code & Publish

### Step 1: Make Code Changes

Update your Python scripts, documentation, or features:

```bash
# Example: Update a Python script
vim src/seo/scripts/page_analyzer.py

# Or update documentation
vim README.md
vim CHANGELOG.md
```

### Step 2: Commit Changes

```bash
git add .
git commit -m "feat: add new feature" 
# or
git commit -m "fix: bug fix for issue #123"
# or
git commit -m "docs: update documentation"
```

### Step 3: Update Version

```bash
npm version patch  # for bug fixes
npm version minor  # for new features
npm version major  # for breaking changes
```

This automatically:
- Updates package.json
- Creates commit "v2.0.1"
- Creates git tag v2.0.1

### Step 4: Update Changelog

Add entry to top of `CHANGELOG.md`:

```markdown
## [2.0.1] - 2026-02-25

### Added
- New feature X

### Fixed
- Bug fix for Y

### Changed
- Documentation updates

## [2.0.0] - 2026-02-20
...
```

Commit:
```bash
git add CHANGELOG.md
git commit --amend --no-edit  # Add to last commit
```

Or create separate commit:
```bash
git commit -m "docs: update CHANGELOG for v2.0.1"
```

### Step 5: Rebuild Distribution

If you changed Python code or added files:

```bash
npm run build
```

### Step 6: Verify Package Contents

```bash
npm pack --dry-run
```

Should show your updated version (2.0.1):
```
npm notice Tarball Contents ===
npm notice name:          seo-max
npm notice version:       2.0.1
...
```

### Step 7: Publish to npm

```bash
npm publish
```

Or with OTP if you have 2FA:
```bash
npm publish --otp 123456
```

Expected output:
```
npm notice Publishing to https://registry.npmjs.org/
npm notice 📦 seo-max@2.0.1
...
+ seo-max@2.0.1
```

### Step 8: Push to GitHub

```bash
git push origin main
git push origin v2.0.1
```

---

## Quick Update Checklist

Use this checklist for each update:

- [ ] Make code changes
- [ ] Update CHANGELOG.md
- [ ] Test locally with: `npm run build`
- [ ] Run: `npm version patch/minor/major`
- [ ] Verify with: `npm pack --dry-run`
- [ ] Publish with: `npm publish`
- [ ] Verify on npmjs.com
- [ ] Push to GitHub: `git push origin main --tags`

---

## Common Update Scenarios

### Scenario 1: Bug Fix in Python Script

```bash
# 1. Fix the bug
vim src/seo/scripts/page_analyzer.py

# 2. Commit the fix
git add src/seo/scripts/page_analyzer.py
git commit -m "fix: correct page scoring algorithm"

# 3. Bump patch version (2.0.0 → 2.0.1)
npm version patch

# 4. Publish
npm publish

# 5. Verify
npm info seo-max

# 6. Push
git push origin main --tags
```

### Scenario 2: New Feature

```bash
# 1. Add new analyzer or feature
vim src/seo/scripts/new_feature.py

# 2. Update CLI
vim cli/dist/cli.js

# 3. Commit
git add .
git commit -m "feat: add new SEO analyzer"

# 4. Update CHANGELOG
vim CHANGELOG.md
git add CHANGELOG.md
git commit --amend --no-edit

# 5. Bump minor version (2.0.0 → 2.1.0)
npm version minor

# 6. Publish
npm publish

# 7. Push
git push origin main --tags
```

### Scenario 3: Major Breaking Change

```bash
# 1. Update package.json exports or CLI interface
vim package.json cli/dist/cli.js

# 2. Update README with migration guide
vim README.md

# 3. Update CHANGELOG
vim CHANGELOG.md

# 4. Commit all changes
git add .
git commit -m "feat!: breaking change - new API structure"

# 5. Bump major version (2.0.0 → 3.0.0)
npm version major

# 6. Publish
npm publish

# 7. Push
git push origin main --tags
```

---

## Update Files Explained

### package.json
```json
{
  "name": "seo-max",
  "version": "2.0.1",  // ← Update this
  "description": "AI-powered SEO intelligence",
  ...
}
```

### CHANGELOG.md
```markdown
# Changelog

## [2.0.1] - 2026-02-25

### Fixed
- Bug fix description

### Added
- New feature

## [2.0.0] - Previous Release
...
```

### Semantic Versioning (semver)

Follow this pattern: `MAJOR.MINOR.PATCH`

| Scenario | Update | Example |
|----------|--------|---------|
| Bug fix | PATCH | 2.0.0 → 2.0.1 |
| New feature (backward compatible) | MINOR | 2.0.0 → 2.1.0 |
| Breaking change | MAJOR | 2.0.0 → 3.0.0 |

---

## Verify Update Succeeded

After publishing:

```bash
# Check npm registry
npm info seo-max

# Should show latest version:
# seo-max@2.0.1

# Or visit:
# https://www.npmjs.com/package/seo-max
```

Install updated version:
```bash
# Update global installation
npm install -g seo-max@latest

# Or in a project
npm update seo-max
```

---

## Troubleshooting Update Issues

### Issue: "Version already published"
```bash
# Version 2.0.1 already exists
# Solution: Use next version
npm version minor
npm publish
```

### Issue: "You do not have permission to publish"
```bash
# Need to be logged in
npm login

# Then publish
npm publish
```

### Issue: OTP required
```bash
# You have 2FA enabled (good!)
npm publish --otp 123456
```

### Issue: Package changes not in dist

```bash
# Rebuild distribution
npm run build

# Then commit and publish
git add cli/dist/
git commit -m "build: rebuild distribution"
npm version patch
npm publish
```

### Issue: Need to undo a version

Only do this if you just published and realize there's a critical issue:

```bash
# Un-publish a version (careful!)
npm unpublish seo-max@2.0.1

# Or deprecate it
npm deprecate seo-max@2.0.1 "Critical bug, use 2.0.2"

# Then publish a fix
npm version patch
npm publish
```

---

## Automated Publishing (Optional)

For frequent updates, use `np`:

```bash
# Install np globally
npm install -g np

# Then for each release:
np

# Answers prompts for:
# - Version bump (patch/minor/major)
# - Publish confirmation
# - Automatically handles: git, npm, tags
```

Or use GitHub Actions for automated releases.

---

## Example: Complete Update Workflow

```bash
# 1. Make changes
vim src/seo/scripts/page_analyzer.py
vim README.md

# 2. Test
npm run build

# 3. Commit changes
git add .
git commit -m "feat: improve page analysis scoring"

# 4. Update version (patch → 2.0.1)
npm version patch

# 5. Verify
npm pack --dry-run

# 6. Publish
npm publish

# 7. Verify on npm
npm info seo-max

# 8. Push to GitHub
git push origin main --tags

# Done! ✅
```

---

## Summary

**To update and publish:**

```bash
# 1. Make code changes
vim src/...

# 2. Update version
npm version patch

# 3. Publish
npm publish

# 4. Push
git push origin main --tags
```

**That's it!** Your package is updated on npm in ~2 minutes.

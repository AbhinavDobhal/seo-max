# NPM Publishing Guide for SEO Max v2.0

**Target:** Publish `seo-max` v2.0.0 to npmjs.org  
**Date:** 25 February 2026

---

## Step-by-Step Publishing Process

### Step 1: Verify npm Account & Login

First, ensure you have an npm account and are logged in:

```bash
# Check if you're logged in
npm whoami

# If not logged in, login
npm login
# Enter username, password, and OTP if enabled
```

If you don't have an npm account yet:
- Visit https://www.npmjs.com/signup
- Create an account
- Verify your email
- Enable 2FA for security (recommended)

---

### Step 2: Build CLI Distribution

The `cli/dist/` directory needs to be generated before publishing:

```bash
npm run build
```

This will:
- Compile TypeScript files (if present)
- Generate `cli/dist/index.js`
- Generate `cli/dist/index.d.ts` (TypeScript definitions)
- Generate `cli/dist/cli.js` (CLI executable)

**If you haven't set up the build script yet**, the CLI package needs a `package.json`:

```bash
# Create cli/package.json if it doesn't exist
cat > cli/package.json << 'EOF'
{
  "name": "seo-max-cli",
  "version": "2.0.0",
  "description": "CLI for SEO Max",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "seo-max": "dist/cli.js"
  },
  "scripts": {
    "build": "echo 'Build CLI distribution'"
  },
  "license": "MIT"
}
EOF
```

---

### Step 3: Create Build Output Structure

Create the necessary dist files:

```bash
# Create dist directory
mkdir -p cli/dist

# Create a basic index.js
cat > cli/dist/index.js << 'EOF'
#!/usr/bin/env node

/**
 * SEO Max v2.0
 * AI-powered SEO intelligence for 15+ coding assistants
 */

const path = require('path');
const { PageAnalyzer } = require('../../src/seo/scripts/page_analyzer');

// Export main module
module.exports = {
  PageAnalyzer,
  version: '2.0.0',
  name: 'seo-max'
};

if (require.main === module) {
  console.log('SEO Max CLI v2.0.0');
  console.log('Use as: seo-max <command> [options]');
}
EOF

# Create TypeScript definitions
cat > cli/dist/index.d.ts << 'EOF'
export interface PageAnalysisResult {
  url: string;
  overall_score: number;
  category_scores: Record<string, number>;
  rule_results: Array<any>;
}

export class PageAnalyzer {
  analyze(url: string, htmlContent: string, metadata?: Record<string, any>): PageAnalysisResult;
}

export const version: string;
export const name: string;
EOF

# Create CLI executable
cat > cli/dist/cli.js << 'EOF'
#!/usr/bin/env node

const pkg = require('../package.json');

function main() {
  const args = process.argv.slice(2);
  
  if (!args[0]) {
    console.log(`\n🚀 SEO Max v${pkg.version}`);
    console.log('AI-powered SEO intelligence\n');
    console.log('Usage: seo-max <command> [options]\n');
    console.log('Commands:');
    console.log('  page <url>      Analyze single page');
    console.log('  schema <url>    Validate schema markup');
    console.log('  insights <url>  AI search optimization');
    console.log('  sitemap <url>   Sitemap analysis');
    console.log('  explore <url>   Full site audit\n');
    return 0;
  }
  
  const command = args[0];
  console.log(`Executing: ${command} ${args.slice(1).join(' ')}`);
  return 0;
}

if (require.main === module) {
  process.exit(main());
}

module.exports = main;
EOF

# Make CLI executable
chmod +x cli/dist/cli.js
```

**Or if you're using TypeScript**, compile it:

```bash
# If using TypeScript
npx tsc --outDir cli/dist --declaration

# Or with a build tool
npm run build  # (from cli directory)
```

---

### Step 4: Verify Package Contents

Check what will be published:

```bash
# See what npm will publish
npm pack --dry-run

# Or more detailed:
npm pack --dry-run 2>&1 | head -50
```

Expected output should include:
```
seo-max-2.0.0.tgz
├── cli/dist/
├── src/seo/data/
├── src/seo/scripts/
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

### Step 5: Test Package locally

```bash
# Create a test directory
mkdir -p test-npm-package
cd test-npm-package

# Install from local tarball
npm install ../seo-max-2.0.0.tgz

# Test CLI
./node_modules/.bin/seo-max
# or
npx seo-max

cd ..
rm -rf test-npm-package
```

---

### Step 6: Run Dry-Run Publish

Test the publishing process without actually publishing:

```bash
npm publish --dry-run --verbose
```

This will:
- ✅ Verify your credentials
- ✅ Check package.json validity
- ✅ Confirm file contents
- ✅ Validate package name isn't taken
- ⚠️ NOT actually publish (safe to test)

Expected output:
```
npm notice Packfile contents:
npm notice === Tarball Contents ===
npm notice 115.8kB  cli/dist/index.js
npm notice 2.3kB    cli/dist/index.d.ts
npm notice 1.2kB    cli/dist/cli.js
npm notice 44.9kB   src/seo/data/
...
npm notice === Tarball Details ===
npm notice name:          seo-max
npm notice version:       2.0.0
npm notice filename:      seo-max-2.0.0.tgz
npm notice filesize:      ...kb
npm notice integrity:     sha512-...
npm notice shasum:        ...
npm notice tarball:       https://registry.npmjs.org/seo-max/-/seo-max-2.0.0.tgz
npm notice total files:   21
```

If there are any errors, fix them before proceeding.

---

### Step 7: Create Git Tag (Optional but Recommended)

Tag the release in git:

```bash
# Create and push tag
git tag -a v2.0.0 -m "Release v2.0.0: Phase 2 Python scripts complete"
git push origin v2.0.0

# Verify tag
git tag -l v2.0.0
git show v2.0.0
```

---

### Step 8: Publish to npm

Now publish for real:

```bash
npm publish
```

This will:
- ✅ Upload package to npm registry
- ✅ Make it available globally
- ✅ Create npmjs.org package page
- ✅ Publish docs and tags

Expected output:
```
npm notice Publishing to https://registry.npmjs.org/
npm notice 📦 seo-max@2.0.0
npm notice === Tarball Contents ===
...
npm notice Tarball published to: https://registry.npmjs.org/seo-max/-/seo-max-2.0.0.tgz
+ seo-max@2.0.0
```

---

### Step 9: Verify Publication

Check that your package is live on npm:

```bash
# Check npm registry
npm info seo-max

# Or visit:
# https://www.npmjs.com/package/seo-max
# https://www.npmjs.com/package/seo-max/v/2.0.0
```

Expected output:
```
seo-max@2.0.0 | MIT | deps: none

AI-powered SEO intelligence for 15+ coding assistants

Repository: https://github.com/abhinavdobhal/seo-max.git
Homepage: https://abhinavdobhal.github.io/seo-max/
Bugs: https://github.com/abhinavdobhal/seo-max/issues

dist
.tarball: https://registry.npmjs.org/seo-max/-/seo-max-2.0.0.tgz
.shasum: ...
.integrity: sha512-...
.uncompressed size: ... B

engines:
node 18.0.0 - ...
npm 9.0.0 - ...

maintainers:
- @abhinavdobhal

dist-tags:
latest: 2.0.0
```

---

### Step 10: Installation Test

Users can now install your package:

```bash
# Global installation (for CLI)
npm install -g seo-max

# Or local
npm install seo-max

# Use CLI
seo-max
# or
npx seo-max
```

---

## Common Issues & Solutions

### Issue: "Package name already taken"
**Solution:** Choose a different name or check if you have publishing rights

### Issue: "You do not have permission to publish"
**Solution:** 
- Ensure you're logged in: `npm whoami`
- Check package isn't marked `private: true` in package.json

### Issue: "Invalid semver version"
**Solution:** Use format X.Y.Z (e.g., 2.0.0)

### Issue: "No dist files found"
**Solution:** Run `npm run build` first

### Issue: "OTP required"
**Solution:** If you have 2FA enabled:
```bash
npm publish --otp <6-digit-code>
```

### Issue: "Package already exists at this version"
**Solution:** Increment version number:
```bash
npm version patch  # 2.0.0 → 2.0.1
npm version minor  # 2.0.0 → 2.1.0
npm version major  # 2.0.0 → 3.0.0
```

---

## Publish Checklist

- [ ] npm account created and verified
- [ ] `npm login` successful
- [ ] All code committed to git
- [ ] `npm run build` completes successfully
- [ ] `cli/dist/` directory created with files
- [ ] `.npmignore` configured properly
- [ ] `package.json` is valid JSON
- [ ] Version number correct (2.0.0)
- [ ] `name` is unique on npm
- [ ] `private: false` in package.json
- [ ] `npm publish --dry-run` passes
- [ ] Git tag created: `v2.0.0`
- [ ] Git pushed: `git push origin v2.0.0`
- [ ] `npm publish` executed successfully
- [ ] Package appears on npmjs.com
- [ ] `npm install -g seo-max` works

---

## Post-Publishing

### Update Documentation
After publishing, update your README:

```markdown
## Installation

### Global (CLI)
```bash
npm install -g seo-max
seo-max page <url>
```

### Local (Node module)
```bash
npm install seo-max
const { PageAnalyzer } = require('seo-max');
```

### Update GitHub
- Add "Published on npm" badge to README
- Link to npm package page
- Update installation instructions

---

## What's Next

After v2.0.0 is published:

1. **Create Release Notes** on GitHub
2. **Announce on Social Media**
3. **Monitor Downloads** at npmjs.com
4. **Gather Feedback** from users
5. **Plan v2.1.0** features
6. **Setup Automated Publishing** (optional)

---

## Automated Publishing (Optional)

For future releases, automate with `np`:

```bash
npm install -g np

# Guided release process
np

# Or with options
np --yolo --skip-cleanup
```

---

**Ready to publish? Run these commands in order:**

```bash
npm run build
npm publish --dry-run
npm publish
```

Good luck! 🚀

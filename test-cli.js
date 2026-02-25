#!/usr/bin/env node

// Test the CLI setup
const path = require('path');
const fs = require('fs');

console.log('🔍 SEO Max CLI Diagnostic Test\n');

// Check if files exist
const files = {
  'index.js': './cli/dist/index.js',
  'cli.js': './cli/dist/cli.js',
  'index.d.ts': './cli/dist/index.d.ts',
  'package.json': './package.json'
};

console.log('📁 Checking files:');
let allExist = true;
for (const [name, filepath] of Object.entries(files)) {
  const fullPath = path.join(__dirname, filepath);
  const exists = fs.existsSync(fullPath);
  console.log(`   ${exists ? '✓' : '✗'} ${name} (${filepath})`);
  if (!exists) allExist = false;
}

console.log('');

// Try to load the module
console.log('🔧 Loading module:');
try {
  const pkg = require('./cli/dist/index.js');
  console.log(`   ✓ Module loaded successfully`);
  console.log(`   ✓ Version: ${pkg.version}`);
  console.log(`   ✓ Name: ${pkg.name}`);
  if (pkg.config) {
    console.log(`   ✓ Config found (${pkg.config.supportedAnalyzers?.length || 0} analyzers)`);
  }
} catch (error) {
  console.log(`   ✗ Failed to load module: ${error.message}`);
  allExist = false;
}

console.log('');

// Check package.json
console.log('📦 Package configuration:');
try {
  const pkg = require('./package.json');
  console.log(`   ✓ name: ${pkg.name}`);
  console.log(`   ✓ version: ${pkg.version}`);
  console.log(`   ✓ private: ${pkg.private}`);
  console.log(`   ✓ main: ${pkg.main}`);
  console.log(`   ✓ bin.seo-max: ${pkg.bin?.['seo-max'] || 'NOT SET'}`);
  console.log(`   ✓ types: ${pkg.types}`);
} catch (error) {
  console.log(`   ✗ Failed to read package.json: ${error.message}`);
}

console.log('');
console.log('');

if (allExist) {
  console.log('✅ All checks passed! Ready to publish.');
  console.log('');
  console.log('Next steps:');
  console.log('  npm publish');
  process.exit(0);
} else {
  console.log('❌ Some checks failed. Please review above.');
  process.exit(1);
}

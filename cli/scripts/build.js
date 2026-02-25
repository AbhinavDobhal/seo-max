#!/usr/bin/env node

/**
 * Build script for SEO Max CLI
 * Generates distribution files in cli/dist/
 */

const fs = require('fs');
const path = require('path');

const distDir = path.join(__dirname, '../dist');

// Ensure dist directory exists
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
  console.log('✓ Created dist directory');
}

// Check that all required files exist
const requiredFiles = [
  'index.js',
  'cli.js',
  'index.d.ts'
];

let allFilesExist = true;
requiredFiles.forEach(file => {
  const filePath = path.join(distDir, file);
  if (fs.existsSync(filePath)) {
    console.log('✓ ' + file);
  } else {
    console.log('✗ Missing: ' + file);
    allFilesExist = false;
  }
});

// Make cli.js executable
const cliPath = path.join(distDir, 'cli.js');
if (fs.existsSync(cliPath)) {
  fs.chmodSync(cliPath, 0o755);
  console.log('✓ Made cli.js executable');
}

// Build summary
console.log('');
if (allFilesExist) {
  console.log('✓ Build complete! Distribution is ready.');
  console.log('');
  console.log('Files generated:');
  console.log('  • cli/dist/index.js (main entry point)');
  console.log('  • cli/dist/cli.js (CLI executable)');
  console.log('  • cli/dist/index.d.ts (TypeScript definitions)');
  console.log('');
  console.log('Ready to publish with: npm publish');
} else {
  console.log('✗ Build failed: missing files');
  process.exit(1);
}

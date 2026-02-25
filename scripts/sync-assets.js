#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log('✓ Syncing SEO Max assets...');

// Create necessary directories
const dirs = [
  '.claude/skills/seo',
  '.claude/skills/seo/data',
  '.claude/skills/seo/scripts',
  '.claude/skills/seo/references',
  '.claude/skills/seo/templates'
];

dirs.forEach(dir => {
  const fullPath = path.join(__dirname, '..', dir);
  if (!fs.existsSync(fullPath)) {
    fs.mkdirSync(fullPath, { recursive: true });
    console.log(`  Created: ${dir}`);
  }
});

// Copy data files
const srcData = path.join(__dirname, '../src/seo/data');
const destData = path.join(__dirname, '../.claude/skills/seo/data');

if (fs.existsSync(srcData)) {
  const files = fs.readdirSync(srcData);
  files.forEach(file => {
    fs.copyFileSync(
      path.join(srcData, file),
      path.join(destData, file)
    );
  });
  console.log(`  Copied ${files.length} data files`);
}

// Copy scripts (skip __pycache__ and .pyc files)
const srcScripts = path.join(__dirname, '../src/seo/scripts');
const destScripts = path.join(__dirname, '../.claude/skills/seo/scripts');

if (fs.existsSync(srcScripts)) {
  const files = fs.readdirSync(srcScripts).filter(file => 
    !file.startsWith('.') && file !== '__pycache__' && !file.endsWith('.pyc')
  );
  files.forEach(file => {
    const srcFile = path.join(srcScripts, file);
    const destFile = path.join(destScripts, file);
    const stat = fs.statSync(srcFile);
    if (!stat.isDirectory()) {
      fs.copyFileSync(srcFile, destFile);
    }
  });
  console.log(`  Copied ${files.length} script files`);
}

// Copy references
const srcRef = path.join(__dirname, '../src/seo/references');
const destRef = path.join(__dirname, '../.claude/skills/seo/references');

if (fs.existsSync(srcRef)) {
  const files = fs.readdirSync(srcRef);
  files.forEach(file => {
    fs.copyFileSync(
      path.join(srcRef, file),
      path.join(destRef, file)
    );
  });
  console.log(`  Copied ${files.length} reference files`);
}

// Copy templates
const srcTemplates = path.join(__dirname, '../src/seo/templates');
const destTemplates = path.join(__dirname, '../.claude/skills/seo/templates');

if (fs.existsSync(srcTemplates)) {
  const files = fs.readdirSync(srcTemplates);
  files.forEach(file => {
    const srcFile = path.join(srcTemplates, file);
    const destFile = path.join(destTemplates, file);
    
    // Handle directories
    if (fs.statSync(srcFile).isDirectory()) {
      if (!fs.existsSync(destFile)) {
        fs.mkdirSync(destFile, { recursive: true });
      }
      // Copy files inside the directory
      const subFiles = fs.readdirSync(srcFile);
      subFiles.forEach(subFile => {
        fs.copyFileSync(
          path.join(srcFile, subFile),
          path.join(destFile, subFile)
        );
      });
    } else {
      fs.copyFileSync(srcFile, destFile);
    }
  });
  console.log(`  Copied templates`);
}

console.log('✓ Asset sync complete!');

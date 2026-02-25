#!/usr/bin/env node

/**
 * Prepare assets for npm package distribution
 * Copies skill files from .claude/skills/seo-max to cli/assets
 */

const fs = require('fs');
const path = require('path');

const sourceDir = path.join(__dirname, '../../.claude/skills/seo-max');
const targetDir = path.join(__dirname, '../assets/seo-max');

console.log('📦 Preparing assets for distribution...\n');

// Function to copy directory recursively
function copyDir(src, dest) {
  // Create destination directory
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  // Read source directory
  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      // Recursively copy subdirectory
      copyDir(srcPath, destPath);
    } else {
      // Copy file
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// Check if source exists
if (!fs.existsSync(sourceDir)) {
  console.error('❌ Error: Source directory not found:', sourceDir);
  console.error('   Make sure .claude/skills/seo-max exists');
  process.exit(1);
}

// Copy all files
try {
  copyDir(sourceDir, targetDir);
  
  // Count files
  const countFiles = (dir) => {
    let count = 0;
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isDirectory()) {
        count += countFiles(path.join(dir, entry.name));
      } else {
        count++;
      }
    }
    return count;
  };
  
  const fileCount = countFiles(targetDir);
  
  console.log('✅ Assets prepared successfully!');
  console.log(`   Copied ${fileCount} files to cli/assets/seo-max/`);
  console.log('');
  console.log('📁 Files included:');
  console.log('   • SKILL.md');
  console.log('   • requirements.txt');
  console.log('   • setup.sh / setup.bat');
  console.log('   • scripts/ (Python analyzers)');
  console.log('   • data/ (CSV files)');
  console.log('   • templates/ (Schema templates)');
  console.log('');
  
} catch (error) {
  console.error('❌ Error copying files:', error.message);
  process.exit(1);
}

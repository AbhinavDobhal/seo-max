#!/bin/bash
# SEO Max - Python Environment Setup Script
# Automatically creates virtual environment and installs dependencies

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

echo "🚀 SEO Max - Python Setup"
echo ""

# Check if Python 3.8+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo ""
    echo "Install Python 3.8+ first:"
    echo "  • macOS: brew install python3"
    echo "  • Ubuntu/Debian: sudo apt install python3"
    echo "  • Windows: winget install Python.Python.3.12"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "📥 Upgrading pip..."
pip install --quiet --upgrade pip

# Install dependencies
echo "📥 Installing dependencies from requirements.txt..."
pip install --quiet -r "$SCRIPT_DIR/requirements.txt"

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment manually:"
echo "  source $VENV_DIR/bin/activate"
echo ""
echo "To run analyzers:"
echo "  python3 scripts/page_analyzer.py https://example.com"
echo "  python3 scripts/schema_validator.py https://example.com"
echo "  python3 scripts/insights_optimizer.py https://example.com"
echo "  python3 scripts/sitemap.py https://example.com/sitemap.xml"
echo "  python3 scripts/site_crawler.py https://example.com"
echo ""

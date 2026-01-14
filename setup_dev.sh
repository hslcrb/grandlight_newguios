#!/bin/bash

# GrandLight Development Setup Script
# This script sets up the development environment for the GrandLight project

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║           GrandLight Development Setup                     ║"
echo "║           Glassmorphism GUI Library for Python             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python3 --version

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -e ".[dev]"

# Run tests
echo ""
echo "🧪 Running tests..."
pytest tests/ -v

# Check code quality
echo ""
echo "🎨 Checking code quality..."
black --check grandlight/
flake8 grandlight/ --max-line-length=88 --extend-ignore=E203

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                    Setup Complete! ✨                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests:"
echo "  pytest tests/ -v"
echo ""
echo "To format code:"
echo "  black grandlight/"
echo ""
echo "Happy coding! 🚀"
echo ""

# GrandLight Project Structure

This document provides an overview of the GrandLight package structure and development workflow.

## 📁 Project Structure

```
grandlight_newguios/
├── grandlight/              # Main package directory
│   ├── __init__.py         # Package initialization and metadata
│   └── effects.py          # Glassmorphism effects and themes
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_effects.py     # Tests for effects module
├── examples/               # Example usage
│   └── basic_usage.py      # Basic usage demonstration
├── pyproject.toml          # Modern Python packaging configuration
├── LICENSE                 # MIT License
├── README.md               # Project documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── MANIFEST.in             # Package manifest
├── .gitignore              # Git ignore rules
└── venv/                   # Virtual environment (not committed)
```

## 🚀 Quick Start

### Installation for Development

1. **Clone the repository**
   ```bash
   cd /path/to/grandlight_newguios
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=grandlight tests/

# Run specific test
pytest tests/test_effects.py::TestGlassEffect::test_default_initialization -v
```

### Code Quality Checks

```bash
# Format code with Black
black grandlight/

# Check formatting
black --check grandlight/

# Lint with flake8
flake8 grandlight/ --max-line-length=88 --extend-ignore=E203

# Type checking with mypy
mypy grandlight/
```

## 📦 Building and Publishing

### Build the Package

```bash
# Install build tools
pip install build twine

# Build distributions
python -m build

# This creates:
# - dist/grandlight-0.1.0.tar.gz (source distribution)
# - dist/grandlight-0.1.0-py3-none-any.whl (wheel)
```

### Publish to PyPI

```bash
# Test on TestPyPI first
twine upload --repository testpypi dist/*

# Then publish to PyPI
twine upload dist/*
```

## 🔧 Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

3. **Test your changes**
   ```bash
   pytest tests/
   black grandlight/
   flake8 grandlight/
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add new glassmorphic component"
   git push origin feature/your-feature-name
   ```

5. **Create a pull request**

## 🎨 Current Features

### GlassEffect Class
- Configurable blur intensity (0-100)
- Adjustable opacity (0.0-1.0)
- Custom background colors with RGBA support
- Optional border styling
- Shadow effects for depth

### Pre-defined Themes
- **Light Theme**: Bright, clean glassmorphism
- **Dark Theme**: Deep, modern glassmorphism
- **Colorful Theme**: Custom color tints
- **Frosted Theme**: Heavy blur for intense effect

## 🛣️ Roadmap

Future components to be implemented:

### Core Components
- [ ] Window - Main application window
- [ ] GlassPanel - Container with glass effect
- [ ] GlassButton - Interactive glassmorphic button
- [ ] GlassLabel - Text display with glass background
- [ ] GlassInput - Text input field with glass styling

### Advanced Components
- [ ] GlassNavBar - Navigation bar
- [ ] GlassDialog - Modal dialogs
- [ ] GlassMenu - Dropdown menus
- [ ] GlassCard - Card component
- [ ] GlassTooltip - Hover tooltips

### Features
- [ ] Animation support
- [ ] Event handling
- [ ] Layout managers
- [ ] Custom themes
- [ ] GPU acceleration for blur effects

## 📊 Test Coverage

Current test coverage:
- ✅ GlassEffect initialization
- ✅ Parameter validation
- ✅ Theme presets
- ✅ Error handling

Run coverage report:
```bash
pytest --cov=grandlight --cov-report=html tests/
# Open htmlcov/index.html to view detailed coverage
```

## 📝 Version History

- **v0.1.1** (2026-01-15)
  - Updated GitHub links and profile handle
- **v0.1.0** (2026-01-15)
  - Initial release
  - GlassEffect dataclass
  - Pre-defined theme presets
  - Basic testing framework

## 👥 Contributors

- Rheehose (Rhee Creative) - Creator and maintainer

## 📄 License

MIT License - Copyright (c) 2008-2026 Rheehose (Rhee Creative)

---

For more information, see [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md)

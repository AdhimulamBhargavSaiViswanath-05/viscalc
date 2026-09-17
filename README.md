# VISCalc

A modular and beginner-friendly Python calculator package.

## Overview

VISCalc is a personal learning project designed to explore modern Python packaging practices. This package aims to provide a clean, well-structured calculator implementation organized into separate modules for different types of calculations.

**Status**: 🚧 Currently under active development

## Planned Features

- **Basic Calculator**: Addition, subtraction, multiplication, division, and modulo operations
- **Scientific Calculator**: Power, square root, logarithms, and exponential functions
- **Trigonometric Calculator**: Sine, cosine, tangent, and their inverse functions

## Project Structure

```
viscalc/
├── src/
│   └── viscalc/
│       ├── __init__.py         # Package initialization
│       ├── basic.py            # Basic arithmetic operations
│       ├── scientific.py       # Scientific calculations
│       └── trigonometry.py     # Trigonometric functions
├── tests/                      # Test suite (coming soon)
├── .gitignore                  # Git ignore patterns
├── LICENSE                     # MIT License
├── README.md                   # This file
└── pyproject.toml              # Package configuration
```

## Installation

### For Development

1. Clone the repository:
   ```bash
   git clone git@github-personal:AdhimulamBhargavSaiViswanath-05/viscalc.git
   cd viscalc
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

### From PyPI

> **Note**: This package is not yet published to PyPI. PyPI publishing will be available after the initial development and testing phase is complete.

## Usage

> **Note**: Implementation is in progress. Usage examples will be added once the core functionality is complete.

```python
# Example usage (coming soon)
from viscalc import basic

# result = basic.add(5, 3)
# print(result)  # Output: 8
```

## Development

This project follows the "src layout" structure, which is a modern Python packaging best practice. The src layout ensures that:

- You're testing the installed package, not the raw source code
- Import behavior matches what end users will experience
- The package is properly installable before development begins

### Requirements

- Python 3.10 or higher
- No external runtime dependencies (currently)

### Project Goals

This project serves as a learning experience to understand:

- Modern Python packaging with `pyproject.toml`
- The src-based project layout
- Package distribution and version management
- Writing maintainable, modular Python code
- Testing and continuous integration practices

## Testing

> **Note**: Test suite is under development.

Tests will be located in the `tests/` directory and will use `pytest` as the testing framework.

```bash
# Run tests (coming soon)
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Author**: Bhargav Sai Viswanath Adhimulam  
**Repository**: https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc

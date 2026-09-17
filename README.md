# VISCalc

A modular and beginner-friendly Python calculator package containing basic, scientific, and trigonometric mathematical operations.

## Features

VISCalc provides 26 calculator functions organized into three modules:

### Basic Calculator

Fundamental arithmetic operations:

- **`add(a, b)`** - Addition
- **`subtract(a, b)`** - Subtraction
- **`multiply(a, b)`** - Multiplication
- **`divide(a, b)`** - Division (raises `ZeroDivisionError` if b=0)
- **`modulo(a, b)`** - Modulo operation (raises `ZeroDivisionError` if b=0)
- **`percentage(value, percent)`** - Calculate percentage of a value

### Scientific Calculator

Advanced mathematical functions:

- **`power(base, exponent)`** - Exponentiation
- **`square_root(value)`** - Square root (raises `ValueError` if value < 0)
- **`logarithm(value, base=10)`** - Logarithm with specified base (raises `ValueError` for invalid domains)
- **`natural_log(value)`** - Natural logarithm (raises `ValueError` if value ≤ 0)
- **`exponential(value)`** - e^value
- **`factorial(value)`** - Factorial (raises `ValueError` for negative or non-integer values)

### Trigonometry Calculator

Complete trigonometric operations with both radian and degree support:

**Core trigonometric functions (radians):**
- **`sin(angle)`** - Sine (angle in radians)
- **`cos(angle)`** - Cosine (angle in radians)
- **`tan(angle)`** - Tangent (angle in radians)

**Degree-based trigonometric functions:**
- **`sin_deg(angle)`** - Sine (angle in degrees)
- **`cos_deg(angle)`** - Cosine (angle in degrees)
- **`tan_deg(angle)`** - Tangent (angle in degrees)

**Inverse trigonometric functions (return radians):**
- **`asin(value)`** - Arcsine, returns radians (raises `ValueError` if value outside [-1, 1])
- **`acos(value)`** - Arccosine, returns radians (raises `ValueError` if value outside [-1, 1])
- **`atan(value)`** - Arctangent, returns radians

**Inverse trigonometric functions (return degrees):**
- **`asin_deg(value)`** - Arcsine, returns degrees (raises `ValueError` if value outside [-1, 1])
- **`acos_deg(value)`** - Arccosine, returns degrees (raises `ValueError` if value outside [-1, 1])
- **`atan_deg(value)`** - Arctangent, returns degrees

**Angle conversion:**
- **`radians(degrees)`** - Convert degrees to radians
- **`degrees(radians)`** - Convert radians to degrees

## Installation

> **Note**: This package is not yet published to PyPI. The installation instructions below will work once the package is published.

### From PyPI (coming soon)

```bash
pip install viscalc
```

### Development Installation

For local development, clone the repository and install in editable mode:

```bash
git clone https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc.git
cd viscalc
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

### Basic Calculator Examples

```python
from viscalc import basic

# Addition
print(basic.add(5, 3))  # Output: 8

# Subtraction
print(basic.subtract(10, 4))  # Output: 6

# Multiplication
print(basic.multiply(7, 6))  # Output: 42

# Division
print(basic.divide(15, 3))  # Output: 5.0

# Modulo
print(basic.modulo(17, 5))  # Output: 2

# Percentage
print(basic.percentage(200, 15))  # Output: 30.0
```

### Scientific Calculator Examples

```python
from viscalc import scientific

# Power
print(scientific.power(2, 10))  # Output: 1024

# Square root
print(scientific.square_root(16))  # Output: 4.0

# Logarithm
print(scientific.logarithm(100))  # Output: 2.0 (base 10)
print(scientific.logarithm(8, 2))  # Output: 3.0 (base 2)

# Natural logarithm
import math
print(scientific.natural_log(math.e))  # Output: 1.0

# Exponential
print(scientific.exponential(2))  # Output: 7.389...

# Factorial
print(scientific.factorial(5))  # Output: 120
```

### Trigonometry Calculator Examples

```python
from viscalc import trigonometry
import math

# Radian-based trigonometric functions
print(trigonometry.sin(0))  # Output: 0.0
print(trigonometry.cos(0))  # Output: 1.0
print(trigonometry.tan(math.pi / 4))  # Output: 1.0

# Degree-based trigonometric functions
print(trigonometry.sin_deg(30))  # Output: 0.5
print(trigonometry.cos_deg(60))  # Output: 0.5
print(trigonometry.tan_deg(45))  # Output: 1.0

# Inverse trigonometric functions (return radians)
print(trigonometry.asin(0.5))  # Output: 0.523... (π/6 radians)
print(trigonometry.acos(0.5))  # Output: 1.047... (π/3 radians)
print(trigonometry.atan(1))  # Output: 0.785... (π/4 radians)

# Inverse trigonometric functions (return degrees)
print(trigonometry.asin_deg(0.5))  # Output: 30.0
print(trigonometry.acos_deg(0.5))  # Output: 60.0
print(trigonometry.atan_deg(1))  # Output: 45.0

# Angle conversion
print(trigonometry.radians(180))  # Output: 3.141... (π)
print(trigonometry.degrees(math.pi))  # Output: 180.0
```

## Error Handling

VISCalc provides clear error handling for invalid operations:

- **Division and modulo by zero**: Raises `ZeroDivisionError`
  ```python
  basic.divide(10, 0)  # ZeroDivisionError: Cannot divide by zero
  ```

- **Square root of negative numbers**: Raises `ValueError`
  ```python
  scientific.square_root(-4)  # ValueError: Cannot calculate square root of a negative number
  ```

- **Invalid logarithm inputs**: Raises `ValueError`
  ```python
  scientific.logarithm(0)  # ValueError: Logarithm value must be greater than 0
  scientific.logarithm(10, 1)  # ValueError: Logarithm base cannot be 1
  ```

- **Invalid factorial inputs**: Raises `ValueError`
  ```python
  scientific.factorial(-5)  # ValueError: Factorial is not defined for negative numbers
  scientific.factorial(3.5)  # ValueError: Factorial requires an integer value
  ```

- **Inverse trigonometry domain errors**: Raises `ValueError`
  ```python
  trigonometry.asin(2)  # ValueError: Arcsine domain is [-1, 1]
  trigonometry.acos(-1.5)  # ValueError: Arccosine domain is [-1, 1]
  ```

## Testing

VISCalc includes a comprehensive test suite with **109 tests** covering all functions, edge cases, and error conditions.

Latest test results:
```
109 passed in 0.06s
```

Run tests with pytest:
```bash
python -m pytest -q
```

## Project Structure

```
viscalc/
├── src/
│   └── viscalc/
│       ├── __init__.py
│       ├── basic.py            # Basic arithmetic operations
│       ├── scientific.py       # Scientific calculations
│       └── trigonometry.py     # Trigonometric functions
├── tests/
│   ├── test_basic.py
│   ├── test_scientific.py
│   └── test_trigonometry.py
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

## Development

### Requirements

- Python 3.10 or higher
- No external runtime dependencies

### Development Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

4. Run tests:

```bash
python -m pytest -q
```

### Development Dependencies

- `pytest>=9.0` - Testing framework
- `build>=1.0` - Build tool for creating distributions
- `twine>=5.0` - Tool for uploading packages to PyPI

## Python Compatibility

VISCalc supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Author**: Bhargav Sai Viswanath Adhimulam
**Repository**: https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc
**Version**: 0.1.0

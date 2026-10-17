# VISCalc

[![PyPI version](https://img.shields.io/pypi/v/viscalc.svg)](https://pypi.org/project/viscalc/)
[![Python versions](https://img.shields.io/pypi/pyversions/viscalc.svg)](https://pypi.org/project/viscalc/)
[![License: MIT](https://img.shields.io/pypi/l/viscalc.svg)](LICENSE)

A small, beginner-friendly Python calculator library with **basic**, **scientific**, and **trigonometry** functions. It has no dependencies, uses type hints, and ships with a full test suite.

VISCalc is also a learning project. It was built to practise modern Python packaging, testing, Git branching, and publishing to PyPI with GitHub Actions.

## Installation

```bash
pip install viscalc
```

Requires Python 3.10 or newer. No other packages are needed.

## Quick Start

```python
from viscalc import basic, scientific, trigonometry

basic.add(5, 3)                 # 8
scientific.power(2, 10)         # 1024
scientific.factorial(5)         # 120
trigonometry.sin_deg(30)        # 0.49999999999999994 (about 0.5)
```

> Floating-point results can differ slightly from the "exact" answer (for example `sin_deg(30)` is not exactly `0.5`). Use `math.isclose()` when comparing floats.

## Functions

VISCalc has 26 functions in three modules.

### `viscalc.basic`

| Function | Description | Raises |
|----------|-------------|--------|
| `add(a, b)` | Sum of `a` and `b` | - |
| `subtract(a, b)` | `a` minus `b` | - |
| `multiply(a, b)` | Product of `a` and `b` | - |
| `divide(a, b)` | `a` divided by `b` | `ZeroDivisionError` if `b == 0` |
| `modulo(a, b)` | Remainder of `a / b` | `ZeroDivisionError` if `b == 0` |
| `percentage(value, percent)` | `percent`% of `value` | - |

### `viscalc.scientific`

| Function | Description | Raises |
|----------|-------------|--------|
| `power(base, exponent)` | `base` raised to `exponent` | - |
| `square_root(value)` | Square root | `ValueError` if `value < 0` |
| `logarithm(value, base=10)` | Logarithm of `value` in `base` | `ValueError` if `value <= 0`, `base <= 0`, or `base == 1` |
| `natural_log(value)` | Natural logarithm (base e) | `ValueError` if `value <= 0` |
| `exponential(value)` | e raised to `value` | - |
| `factorial(value)` | `value!` | `ValueError` if `value` is negative or not an integer |

### `viscalc.trigonometry`

| Function | Description | Raises |
|----------|-------------|--------|
| `sin(angle)`, `cos(angle)`, `tan(angle)` | Trig functions, angle in **radians** | - |
| `sin_deg(angle)`, `cos_deg(angle)`, `tan_deg(angle)` | Trig functions, angle in **degrees** | - |
| `asin(value)`, `acos(value)` | Inverse sine / cosine, returns **radians** | `ValueError` if `value` is outside `[-1, 1]` |
| `atan(value)` | Inverse tangent, returns **radians** | - |
| `asin_deg(value)`, `acos_deg(value)` | Inverse sine / cosine, returns **degrees** | `ValueError` if `value` is outside `[-1, 1]` |
| `atan_deg(value)` | Inverse tangent, returns **degrees** | - |
| `radians(degrees)` | Convert degrees to radians | - |
| `degrees(radians)` | Convert radians to degrees | - |

## Examples

```python
import math
from viscalc import basic, scientific, trigonometry

# Basic
basic.divide(15, 3)             # 5.0
basic.modulo(17, 5)             # 2
basic.percentage(200, 15)       # 30.0

# Scientific
scientific.square_root(16)      # 4.0
scientific.logarithm(100)       # 2.0  (base 10)
scientific.logarithm(8, 2)      # 3.0  (base 2)
scientific.natural_log(math.e)  # 1.0

# Trigonometry
trigonometry.cos(0)             # 1.0
trigonometry.tan_deg(45)        # about 1.0
trigonometry.asin_deg(0.5)      # about 30.0
trigonometry.radians(180)       # 3.141592653589793
trigonometry.degrees(math.pi)   # 180.0
```

## Error Handling

Invalid input raises a clear, standard Python exception, so you can catch it normally:

```python
from viscalc import basic, scientific

try:
    basic.divide(10, 0)
except ZeroDivisionError as error:
    print(error)  # Cannot divide by zero

try:
    scientific.square_root(-4)
except ValueError as error:
    print(error)  # Cannot calculate square root of a negative number
```

Error messages used by the library:

| Situation | Exception | Message |
|-----------|-----------|---------|
| `divide(a, 0)` | `ZeroDivisionError` | `Cannot divide by zero` |
| `modulo(a, 0)` | `ZeroDivisionError` | `Cannot perform modulo with zero divisor` |
| `square_root(-x)` | `ValueError` | `Cannot calculate square root of a negative number` |
| `logarithm(0)` | `ValueError` | `Logarithm value must be greater than 0` |
| `logarithm(10, 0)` | `ValueError` | `Logarithm base must be greater than 0` |
| `logarithm(10, 1)` | `ValueError` | `Logarithm base cannot be 1` |
| `natural_log(0)` | `ValueError` | `Natural logarithm value must be greater than 0` |
| `factorial(3.5)` | `ValueError` | `Factorial requires an integer value` |
| `factorial(-5)` | `ValueError` | `Factorial is not defined for negative numbers` |
| `asin(2)`, `asin_deg(2)` | `ValueError` | `Arcsine domain is [-1, 1]` |
| `acos(2)`, `acos_deg(2)` | `ValueError` | `Arccosine domain is [-1, 1]` |

## Development

```bash
git clone https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc.git
cd viscalc
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python -m pytest
```

The `dev` extra installs `pytest`, `build`, and `twine`.

### Project layout

```
viscalc/
├── src/viscalc/
│   ├── __init__.py
│   ├── basic.py
│   ├── scientific.py
│   └── trigonometry.py
├── tests/
│   ├── test_basic.py
│   ├── test_scientific.py
│   └── test_trigonometry.py
├── .github/workflows/          # TestPyPI and PyPI publishing (Trusted Publishing)
├── pyproject.toml
├── LICENSE
└── README.md
```

### Branching and releases

- `main` holds stable, released code.
- `dev` is the integration branch.
- Work happens on `feature/*` branches and is merged through pull requests: `feature/*` -> `dev` -> `main`.
- Releases are published to PyPI from GitHub Actions using PyPI Trusted Publishing (no API tokens).

## Contributing

Bug reports and suggestions are welcome. Please [open an issue](https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc/issues). For code changes, branch from `dev`, add or update tests, make sure `python -m pytest` passes, and open a pull request into `dev`.

## Links

- PyPI: https://pypi.org/project/viscalc/
- Source: https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc
- Issues: https://github.com/AdhimulamBhargavSaiViswanath-05/viscalc/issues

## License

MIT License. See [LICENSE](LICENSE).

## Author

**Adhimulam Bhargav Sai Viswanath**
GitHub: [AdhimulamBhargavSaiViswanath-05](https://github.com/AdhimulamBhargavSaiViswanath-05)

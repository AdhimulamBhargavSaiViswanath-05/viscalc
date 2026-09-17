"""
Tests for the scientific calculator operations module.
"""

import math
import pytest
from viscalc.scientific import (
    power,
    square_root,
    logarithm,
    natural_log,
    exponential,
    factorial,
)


class TestPower:
    """Test cases for the power function."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 3) == 1000

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(2, 0) == 1
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
        assert power(4, -1) == 0.25

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        assert power(4, 0.5) == 2.0
        assert power(27, 1/3) == pytest.approx(3.0)


class TestSquareRoot:
    """Test cases for the square_root function."""

    def test_square_root_positive_value(self):
        """Test square root of positive numbers."""
        assert square_root(9) == 3.0
        assert square_root(16) == 4.0
        assert square_root(25) == 5.0
        assert square_root(2) == pytest.approx(1.414213562373095)

    def test_square_root_zero(self):
        """Test square root of zero."""
        assert square_root(0) == 0.0

    def test_square_root_negative_value(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            square_root(-1)
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            square_root(-25)


class TestLogarithm:
    """Test cases for the logarithm function."""

    def test_logarithm_default_base(self):
        """Test logarithm with default base 10."""
        assert logarithm(100) == pytest.approx(2.0)
        assert logarithm(1000) == pytest.approx(3.0)
        assert logarithm(10) == pytest.approx(1.0)
        assert logarithm(1) == pytest.approx(0.0)

    def test_logarithm_custom_base(self):
        """Test logarithm with custom base."""
        assert logarithm(8, 2) == pytest.approx(3.0)
        assert logarithm(27, 3) == pytest.approx(3.0)
        assert logarithm(16, 4) == pytest.approx(2.0)
        assert logarithm(math.e, math.e) == pytest.approx(1.0)

    def test_logarithm_invalid_value_zero(self):
        """Test that logarithm of zero raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm value must be greater than 0"):
            logarithm(0)

    def test_logarithm_invalid_value_negative(self):
        """Test that logarithm of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm value must be greater than 0"):
            logarithm(-5)

    def test_logarithm_invalid_base_zero(self):
        """Test that base of zero raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm base must be greater than 0"):
            logarithm(10, 0)

    def test_logarithm_invalid_base_negative(self):
        """Test that negative base raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm base must be greater than 0"):
            logarithm(10, -2)

    def test_logarithm_base_equal_to_one(self):
        """Test that base equal to 1 raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
            logarithm(10, 1)


class TestNaturalLog:
    """Test cases for the natural_log function."""

    def test_natural_log_positive_value(self):
        """Test natural logarithm of positive numbers."""
        assert natural_log(math.e) == pytest.approx(1.0)
        assert natural_log(1) == pytest.approx(0.0)
        assert natural_log(math.e ** 2) == pytest.approx(2.0)
        assert natural_log(10) == pytest.approx(2.302585092994046)

    def test_natural_log_invalid_zero(self):
        """Test that natural log of zero raises ValueError."""
        with pytest.raises(ValueError, match="Natural logarithm value must be greater than 0"):
            natural_log(0)

    def test_natural_log_invalid_negative(self):
        """Test that natural log of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Natural logarithm value must be greater than 0"):
            natural_log(-1)
        with pytest.raises(ValueError, match="Natural logarithm value must be greater than 0"):
            natural_log(-10)


class TestExponential:
    """Test cases for the exponential function."""

    def test_exponential_positive_value(self):
        """Test exponential with positive values."""
        assert exponential(0) == 1.0
        assert exponential(1) == pytest.approx(math.e)
        assert exponential(2) == pytest.approx(math.e ** 2)

    def test_exponential_zero(self):
        """Test exponential of zero."""
        assert exponential(0) == 1.0

    def test_exponential_negative_value(self):
        """Test exponential with negative values."""
        assert exponential(-1) == pytest.approx(1 / math.e)
        assert exponential(-2) == pytest.approx(1 / (math.e ** 2))

    def test_exponential_large_value(self):
        """Test exponential with larger values."""
        assert exponential(5) == pytest.approx(math.e ** 5)


class TestFactorial:
    """Test cases for the factorial function."""

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1

    def test_factorial_positive_integer(self):
        """Test factorial of positive integers."""
        assert factorial(5) == 120
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(6) == 720
        assert factorial(10) == 3628800

    def test_factorial_negative_value(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-5)

    def test_factorial_non_integer_value(self):
        """Test that factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError, match="Factorial requires an integer value"):
            factorial(3.5)
        with pytest.raises(ValueError, match="Factorial requires an integer value"):
            factorial(2.0)

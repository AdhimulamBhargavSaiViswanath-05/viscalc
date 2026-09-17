"""
Tests for the basic arithmetic operations module.
"""

import pytest
from viscalc.basic import add, subtract, multiply, divide, modulo, percentage


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtract:
    """Test cases for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2
        assert subtract(0, 10) == -10

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(5, -3) == 8

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Test cases for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(4, 5) == 20
        assert multiply(3, 7) == 21

    def test_multiply_negative_numbers(self):
        """Test multiplying with negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20
        assert multiply(6, -2) == -12

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(0, 5) == 0
        assert multiply(10, 0) == 0
        assert multiply(0, 0) == 0

    def test_multiply_floats(self):
        """Test multiplying floating-point numbers."""
        assert multiply(2.5, 4) == 10.0
        assert multiply(1.5, 2.5) == pytest.approx(3.75)


class TestDivide:
    """Test cases for the divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0

    def test_divide_with_remainder(self):
        """Test division that results in a decimal."""
        assert divide(7, 2) == 3.5
        assert divide(5, 4) == 1.25

    def test_divide_negative_numbers(self):
        """Test dividing with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(0, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0


class TestModulo:
    """Test cases for the modulo function."""

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        assert modulo(10, 3) == 1
        assert modulo(15, 4) == 3
        assert modulo(20, 6) == 2

    def test_modulo_no_remainder(self):
        """Test modulo when there is no remainder."""
        assert modulo(10, 5) == 0
        assert modulo(12, 3) == 0

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        assert modulo(-10, 3) == 2  # Python's modulo behavior with negatives
        assert modulo(10, -3) == -2

    def test_modulo_by_zero(self):
        """Test that modulo by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot perform modulo with zero divisor"):
            modulo(10, 0)
        with pytest.raises(ZeroDivisionError, match="Cannot perform modulo with zero divisor"):
            modulo(0, 0)

    def test_modulo_zero_by_number(self):
        """Test modulo of zero by a number."""
        assert modulo(0, 5) == 0


class TestPercentage:
    """Test cases for the percentage function."""

    def test_percentage_basic(self):
        """Test basic percentage calculations."""
        assert percentage(200, 10) == 20.0
        assert percentage(50, 20) == 10.0
        assert percentage(100, 50) == 50.0

    def test_percentage_zero(self):
        """Test percentage with zero values."""
        assert percentage(0, 10) == 0.0
        assert percentage(100, 0) == 0.0

    def test_percentage_over_100(self):
        """Test percentage greater than 100%."""
        assert percentage(50, 200) == 100.0
        assert percentage(10, 150) == 15.0

    def test_percentage_decimal(self):
        """Test percentage with decimal values."""
        assert percentage(80, 12.5) == 10.0
        assert percentage(150.5, 10) == pytest.approx(15.05)

    def test_percentage_negative(self):
        """Test percentage with negative values."""
        assert percentage(-100, 10) == -10.0
        assert percentage(100, -10) == -10.0

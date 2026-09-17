"""
Scientific calculator operations for VISCalc.

This module provides scientific mathematical functions including power operations,
square roots, logarithms, exponentials, and factorials.
"""

import math


def power(base: float, exponent: float) -> float:
    """
    Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent to raise the base to.

    Returns:
        The result of base raised to exponent.

    Example:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(2, -1)
        0.5
    """
    return base ** exponent


def square_root(value: float) -> float:
    """
    Calculate the square root of a value.

    Args:
        value: The number to calculate the square root of.

    Returns:
        The square root of the value.

    Raises:
        ValueError: If value is negative.

    Example:
        >>> square_root(9)
        3.0
        >>> square_root(0)
        0.0
    """
    if value < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(value)


def logarithm(value: float, base: float = 10) -> float:
    """
    Calculate the logarithm of a value with a given base.

    Args:
        value: The number to calculate the logarithm of (must be > 0).
        base: The logarithm base (default: 10, must be > 0 and != 1).

    Returns:
        The logarithm of value with the specified base.

    Raises:
        ValueError: If value <= 0, base <= 0, or base == 1.

    Example:
        >>> logarithm(100)
        2.0
        >>> logarithm(8, 2)
        3.0
    """
    if value <= 0:
        raise ValueError("Logarithm value must be greater than 0")
    if base <= 0:
        raise ValueError("Logarithm base must be greater than 0")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(value, base)


def natural_log(value: float) -> float:
    """
    Calculate the natural logarithm (ln) of a value.

    Args:
        value: The number to calculate the natural logarithm of (must be > 0).

    Returns:
        The natural logarithm of the value.

    Raises:
        ValueError: If value <= 0.

    Example:
        >>> natural_log(math.e)
        1.0
        >>> natural_log(1)
        0.0
    """
    if value <= 0:
        raise ValueError("Natural logarithm value must be greater than 0")
    return math.log(value)


def exponential(value: float) -> float:
    """
    Calculate e raised to the power of value.

    Args:
        value: The exponent to raise e to.

    Returns:
        e raised to the power of value.

    Example:
        >>> exponential(0)
        1.0
        >>> exponential(1)
        2.718281828459045
    """
    return math.exp(value)


def factorial(value: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        value: The non-negative integer to calculate factorial of.

    Returns:
        The factorial of the value.

    Raises:
        ValueError: If value is negative or not an integer.

    Example:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    if not isinstance(value, int):
        raise ValueError("Factorial requires an integer value")
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(value)

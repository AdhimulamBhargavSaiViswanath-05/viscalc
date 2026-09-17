"""
Basic arithmetic operations for VISCalc.

This module provides fundamental calculator functions including addition,
subtraction, multiplication, division, modulo, and percentage calculations.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Example:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.

    Example:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.

    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(-2, 3)
        -6
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: The dividend (number to be divided).
        b: The divisor (number to divide by).

    Returns:
        The quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def modulo(a: float, b: float) -> float:
    """
    Calculate the remainder of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The remainder of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.

    Example:
        >>> modulo(10, 3)
        1
        >>> modulo(15, 4)
        3
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulo with zero divisor")
    return a % b


def percentage(value: float, percent: float) -> float:
    """
    Calculate a percentage of a value.

    Args:
        value: The base value.
        percent: The percentage to calculate.

    Returns:
        The calculated percentage of the value.

    Example:
        >>> percentage(200, 10)
        20.0
        >>> percentage(50, 20)
        10.0
    """
    return value * percent / 100

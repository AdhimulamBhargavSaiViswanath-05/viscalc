"""
Trigonometric calculator operations for VISCalc.

This module provides trigonometric functions including sine, cosine, tangent,
their inverse functions, and degree/radian conversion utilities.
"""

import math


def sin(angle: float) -> float:
    """
    Calculate the sine of an angle in radians.

    Args:
        angle: The angle in radians.

    Returns:
        The sine of the angle (value between -1 and 1).

    Example:
        >>> sin(0)
        0.0
        >>> sin(math.pi / 2)
        1.0
    """
    return math.sin(angle)


def cos(angle: float) -> float:
    """
    Calculate the cosine of an angle in radians.

    Args:
        angle: The angle in radians.

    Returns:
        The cosine of the angle (value between -1 and 1).

    Example:
        >>> cos(0)
        1.0
        >>> cos(math.pi)
        -1.0
    """
    return math.cos(angle)


def tan(angle: float) -> float:
    """
    Calculate the tangent of an angle in radians.

    Args:
        angle: The angle in radians.

    Returns:
        The tangent of the angle.

    Example:
        >>> tan(0)
        0.0
        >>> tan(math.pi / 4)
        1.0
    """
    return math.tan(angle)


def sin_deg(angle: float) -> float:
    """
    Calculate the sine of an angle in degrees.

    Args:
        angle: The angle in degrees.

    Returns:
        The sine of the angle (value between -1 and 1).

    Example:
        >>> sin_deg(0)
        0.0
        >>> sin_deg(90)
        1.0
        >>> sin_deg(30)
        0.5
    """
    return math.sin(math.radians(angle))


def cos_deg(angle: float) -> float:
    """
    Calculate the cosine of an angle in degrees.

    Args:
        angle: The angle in degrees.

    Returns:
        The cosine of the angle (value between -1 and 1).

    Example:
        >>> cos_deg(0)
        1.0
        >>> cos_deg(180)
        -1.0
        >>> cos_deg(60)
        0.5
    """
    return math.cos(math.radians(angle))


def tan_deg(angle: float) -> float:
    """
    Calculate the tangent of an angle in degrees.

    Args:
        angle: The angle in degrees.

    Returns:
        The tangent of the angle.

    Example:
        >>> tan_deg(0)
        0.0
        >>> tan_deg(45)
        1.0
    """
    return math.tan(math.radians(angle))


def asin(value: float) -> float:
    """
    Calculate the arcsine (inverse sine) of a value, returning radians.

    Args:
        value: The value to calculate arcsine of (must be in range [-1, 1]).

    Returns:
        The angle in radians (between -π/2 and π/2).

    Raises:
        ValueError: If value is outside the domain [-1, 1].

    Example:
        >>> asin(0)
        0.0
        >>> asin(1)
        1.5707963267948966
        >>> asin(0.5)
        0.5235987755982989
    """
    if value < -1 or value > 1:
        raise ValueError("Arcsine domain is [-1, 1]")
    return math.asin(value)


def acos(value: float) -> float:
    """
    Calculate the arccosine (inverse cosine) of a value, returning radians.

    Args:
        value: The value to calculate arccosine of (must be in range [-1, 1]).

    Returns:
        The angle in radians (between 0 and π).

    Raises:
        ValueError: If value is outside the domain [-1, 1].

    Example:
        >>> acos(1)
        0.0
        >>> acos(0)
        1.5707963267948966
        >>> acos(-1)
        3.141592653589793
    """
    if value < -1 or value > 1:
        raise ValueError("Arccosine domain is [-1, 1]")
    return math.acos(value)


def atan(value: float) -> float:
    """
    Calculate the arctangent (inverse tangent) of a value, returning radians.

    Args:
        value: The value to calculate arctangent of (any real number).

    Returns:
        The angle in radians (between -π/2 and π/2).

    Example:
        >>> atan(0)
        0.0
        >>> atan(1)
        0.7853981633974483
        >>> atan(-1)
        -0.7853981633974483
    """
    return math.atan(value)


def asin_deg(value: float) -> float:
    """
    Calculate the arcsine (inverse sine) of a value, returning degrees.

    Args:
        value: The value to calculate arcsine of (must be in range [-1, 1]).

    Returns:
        The angle in degrees (between -90 and 90).

    Raises:
        ValueError: If value is outside the domain [-1, 1].

    Example:
        >>> asin_deg(0)
        0.0
        >>> asin_deg(1)
        90.0
        >>> asin_deg(0.5)
        30.0
    """
    if value < -1 or value > 1:
        raise ValueError("Arcsine domain is [-1, 1]")
    return math.degrees(math.asin(value))


def acos_deg(value: float) -> float:
    """
    Calculate the arccosine (inverse cosine) of a value, returning degrees.

    Args:
        value: The value to calculate arccosine of (must be in range [-1, 1]).

    Returns:
        The angle in degrees (between 0 and 180).

    Raises:
        ValueError: If value is outside the domain [-1, 1].

    Example:
        >>> acos_deg(1)
        0.0
        >>> acos_deg(0)
        90.0
        >>> acos_deg(-1)
        180.0
    """
    if value < -1 or value > 1:
        raise ValueError("Arccosine domain is [-1, 1]")
    return math.degrees(math.acos(value))


def atan_deg(value: float) -> float:
    """
    Calculate the arctangent (inverse tangent) of a value, returning degrees.

    Args:
        value: The value to calculate arctangent of (any real number).

    Returns:
        The angle in degrees (between -90 and 90).

    Example:
        >>> atan_deg(0)
        0.0
        >>> atan_deg(1)
        45.0
        >>> atan_deg(-1)
        -45.0
    """
    return math.degrees(math.atan(value))


def radians(degrees: float) -> float:
    """
    Convert degrees to radians.

    Args:
        degrees: The angle in degrees.

    Returns:
        The angle in radians.

    Example:
        >>> radians(0)
        0.0
        >>> radians(180)
        3.141592653589793
        >>> radians(90)
        1.5707963267948966
    """
    return math.radians(degrees)


def degrees(radians: float) -> float:
    """
    Convert radians to degrees.

    Args:
        radians: The angle in radians.

    Returns:
        The angle in degrees.

    Example:
        >>> degrees(0)
        0.0
        >>> degrees(math.pi)
        180.0
        >>> degrees(math.pi / 2)
        90.0
    """
    return math.degrees(radians)

"""
Tests for the trigonometric calculator operations module.
"""

import math
import pytest
from viscalc.trigonometry import (
    sin,
    cos,
    tan,
    sin_deg,
    cos_deg,
    tan_deg,
    asin,
    acos,
    atan,
    asin_deg,
    acos_deg,
    atan_deg,
    radians,
    degrees,
)


class TestSin:
    """Test cases for the sin function."""

    def test_sin_zero(self):
        """Test sine of zero."""
        assert sin(0) == 0.0

    def test_sin_special_angles(self):
        """Test sine of special angles in radians."""
        assert sin(math.pi / 6) == pytest.approx(0.5)
        assert sin(math.pi / 4) == pytest.approx(math.sqrt(2) / 2)
        assert sin(math.pi / 3) == pytest.approx(math.sqrt(3) / 2)
        assert sin(math.pi / 2) == pytest.approx(1.0)

    def test_sin_negative_angles(self):
        """Test sine with negative angles."""
        assert sin(-math.pi / 6) == pytest.approx(-0.5)
        assert sin(-math.pi / 2) == pytest.approx(-1.0)

    def test_sin_large_angles(self):
        """Test sine with large angles."""
        assert sin(2 * math.pi) == pytest.approx(0.0)
        assert sin(3 * math.pi / 2) == pytest.approx(-1.0)

    def test_sin_full_circle(self):
        """Test sine at key points around the unit circle."""
        assert sin(0) == pytest.approx(0.0)
        assert sin(math.pi / 2) == pytest.approx(1.0)
        assert sin(math.pi) == pytest.approx(0.0)
        assert sin(3 * math.pi / 2) == pytest.approx(-1.0)
        assert sin(2 * math.pi) == pytest.approx(0.0)


class TestCos:
    """Test cases for the cos function."""

    def test_cos_zero(self):
        """Test cosine of zero."""
        assert cos(0) == 1.0

    def test_cos_special_angles(self):
        """Test cosine of special angles in radians."""
        assert cos(math.pi / 6) == pytest.approx(math.sqrt(3) / 2)
        assert cos(math.pi / 4) == pytest.approx(math.sqrt(2) / 2)
        assert cos(math.pi / 3) == pytest.approx(0.5)
        assert cos(math.pi / 2) == pytest.approx(0.0)

    def test_cos_negative_angles(self):
        """Test cosine with negative angles."""
        assert cos(-math.pi / 3) == pytest.approx(0.5)
        assert cos(-math.pi) == pytest.approx(-1.0)

    def test_cos_large_angles(self):
        """Test cosine with large angles."""
        assert cos(2 * math.pi) == pytest.approx(1.0)
        assert cos(3 * math.pi / 2) == pytest.approx(0.0)

    def test_cos_full_circle(self):
        """Test cosine at key points around the unit circle."""
        assert cos(0) == pytest.approx(1.0)
        assert cos(math.pi / 2) == pytest.approx(0.0)
        assert cos(math.pi) == pytest.approx(-1.0)
        assert cos(3 * math.pi / 2) == pytest.approx(0.0)
        assert cos(2 * math.pi) == pytest.approx(1.0)


class TestTan:
    """Test cases for the tan function."""

    def test_tan_zero(self):
        """Test tangent of zero."""
        assert tan(0) == 0.0

    def test_tan_special_angles(self):
        """Test tangent of special angles in radians."""
        assert tan(math.pi / 6) == pytest.approx(1 / math.sqrt(3))
        assert tan(math.pi / 4) == pytest.approx(1.0)
        assert tan(math.pi / 3) == pytest.approx(math.sqrt(3))

    def test_tan_negative_angles(self):
        """Test tangent with negative angles."""
        assert tan(-math.pi / 4) == pytest.approx(-1.0)
        assert tan(-math.pi / 6) == pytest.approx(-1 / math.sqrt(3))

    def test_tan_near_pi_over_2(self):
        """Test tangent near pi/2 (returns large finite value, not infinity)."""
        result = tan(math.pi / 2)
        assert abs(result) > 1e10  # Very large value


class TestSinDeg:
    """Test cases for the sin_deg function."""

    def test_sin_deg_zero(self):
        """Test sine of zero degrees."""
        assert sin_deg(0) == 0.0

    def test_sin_deg_special_angles(self):
        """Test sine of special angles in degrees."""
        assert sin_deg(30) == pytest.approx(0.5)
        assert sin_deg(45) == pytest.approx(math.sqrt(2) / 2)
        assert sin_deg(60) == pytest.approx(math.sqrt(3) / 2)
        assert sin_deg(90) == pytest.approx(1.0)

    def test_sin_deg_negative_angles(self):
        """Test sine with negative angles in degrees."""
        assert sin_deg(-30) == pytest.approx(-0.5)
        assert sin_deg(-90) == pytest.approx(-1.0)

    def test_sin_deg_full_circle(self):
        """Test sine at key points around the circle in degrees."""
        assert sin_deg(0) == pytest.approx(0.0)
        assert sin_deg(90) == pytest.approx(1.0)
        assert sin_deg(180) == pytest.approx(0.0)
        assert sin_deg(270) == pytest.approx(-1.0)
        assert sin_deg(360) == pytest.approx(0.0)


class TestCosDeg:
    """Test cases for the cos_deg function."""

    def test_cos_deg_zero(self):
        """Test cosine of zero degrees."""
        assert cos_deg(0) == 1.0

    def test_cos_deg_special_angles(self):
        """Test cosine of special angles in degrees."""
        assert cos_deg(30) == pytest.approx(math.sqrt(3) / 2)
        assert cos_deg(45) == pytest.approx(math.sqrt(2) / 2)
        assert cos_deg(60) == pytest.approx(0.5)
        assert cos_deg(90) == pytest.approx(0.0)

    def test_cos_deg_negative_angles(self):
        """Test cosine with negative angles in degrees."""
        assert cos_deg(-60) == pytest.approx(0.5)
        assert cos_deg(-180) == pytest.approx(-1.0)

    def test_cos_deg_full_circle(self):
        """Test cosine at key points around the circle in degrees."""
        assert cos_deg(0) == pytest.approx(1.0)
        assert cos_deg(90) == pytest.approx(0.0)
        assert cos_deg(180) == pytest.approx(-1.0)
        assert cos_deg(270) == pytest.approx(0.0)
        assert cos_deg(360) == pytest.approx(1.0)


class TestTanDeg:
    """Test cases for the tan_deg function."""

    def test_tan_deg_zero(self):
        """Test tangent of zero degrees."""
        assert tan_deg(0) == 0.0

    def test_tan_deg_special_angles(self):
        """Test tangent of special angles in degrees."""
        assert tan_deg(30) == pytest.approx(1 / math.sqrt(3))
        assert tan_deg(45) == pytest.approx(1.0)
        assert tan_deg(60) == pytest.approx(math.sqrt(3))

    def test_tan_deg_negative_angles(self):
        """Test tangent with negative angles in degrees."""
        assert tan_deg(-45) == pytest.approx(-1.0)
        assert tan_deg(-30) == pytest.approx(-1 / math.sqrt(3))

    def test_tan_deg_near_90(self):
        """Test tangent near 90 degrees (returns large finite value)."""
        result = tan_deg(90)
        assert abs(result) > 1e10  # Very large value


class TestAsin:
    """Test cases for the asin function."""

    def test_asin_valid_range(self):
        """Test arcsine with valid input values."""
        assert asin(0) == 0.0
        assert asin(0.5) == pytest.approx(math.pi / 6)
        assert asin(math.sqrt(2) / 2) == pytest.approx(math.pi / 4)
        assert asin(math.sqrt(3) / 2) == pytest.approx(math.pi / 3)

    def test_asin_boundary_values(self):
        """Test arcsine at domain boundaries."""
        assert asin(1) == pytest.approx(math.pi / 2)
        assert asin(-1) == pytest.approx(-math.pi / 2)

    def test_asin_invalid_greater_than_one(self):
        """Test that arcsine raises ValueError for values > 1."""
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin(1.1)
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin(2.0)

    def test_asin_invalid_less_than_minus_one(self):
        """Test that arcsine raises ValueError for values < -1."""
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin(-1.1)
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin(-2.0)


class TestAcos:
    """Test cases for the acos function."""

    def test_acos_valid_range(self):
        """Test arccosine with valid input values."""
        assert acos(1) == 0.0
        assert acos(0.5) == pytest.approx(math.pi / 3)
        assert acos(math.sqrt(2) / 2) == pytest.approx(math.pi / 4)
        assert acos(0) == pytest.approx(math.pi / 2)

    def test_acos_boundary_values(self):
        """Test arccosine at domain boundaries."""
        assert acos(1) == pytest.approx(0.0)
        assert acos(-1) == pytest.approx(math.pi)

    def test_acos_invalid_greater_than_one(self):
        """Test that arccosine raises ValueError for values > 1."""
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos(1.1)
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos(2.0)

    def test_acos_invalid_less_than_minus_one(self):
        """Test that arccosine raises ValueError for values < -1."""
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos(-1.1)
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos(-2.0)


class TestAtan:
    """Test cases for the atan function."""

    def test_atan_zero(self):
        """Test arctangent of zero."""
        assert atan(0) == 0.0

    def test_atan_positive_values(self):
        """Test arctangent with positive values."""
        assert atan(1) == pytest.approx(math.pi / 4)
        assert atan(math.sqrt(3)) == pytest.approx(math.pi / 3)
        assert atan(1 / math.sqrt(3)) == pytest.approx(math.pi / 6)

    def test_atan_negative_values(self):
        """Test arctangent with negative values."""
        assert atan(-1) == pytest.approx(-math.pi / 4)
        assert atan(-math.sqrt(3)) == pytest.approx(-math.pi / 3)

    def test_atan_large_values(self):
        """Test arctangent with large values approaches pi/2."""
        assert atan(1000) == pytest.approx(math.pi / 2, abs=0.01)
        assert atan(-1000) == pytest.approx(-math.pi / 2, abs=0.01)


class TestAsinDeg:
    """Test cases for the asin_deg function."""

    def test_asin_deg_valid_range(self):
        """Test arcsine in degrees with valid input values."""
        assert asin_deg(0) == 0.0
        assert asin_deg(0.5) == pytest.approx(30.0)
        assert asin_deg(math.sqrt(2) / 2) == pytest.approx(45.0)
        assert asin_deg(math.sqrt(3) / 2) == pytest.approx(60.0)

    def test_asin_deg_boundary_values(self):
        """Test arcsine in degrees at domain boundaries."""
        assert asin_deg(1) == pytest.approx(90.0)
        assert asin_deg(-1) == pytest.approx(-90.0)

    def test_asin_deg_invalid_greater_than_one(self):
        """Test that arcsine in degrees raises ValueError for values > 1."""
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin_deg(1.1)
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin_deg(2.0)

    def test_asin_deg_invalid_less_than_minus_one(self):
        """Test that arcsine in degrees raises ValueError for values < -1."""
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin_deg(-1.1)
        with pytest.raises(ValueError, match="Arcsine domain is \\[-1, 1\\]"):
            asin_deg(-2.0)


class TestAcosDeg:
    """Test cases for the acos_deg function."""

    def test_acos_deg_valid_range(self):
        """Test arccosine in degrees with valid input values."""
        assert acos_deg(1) == 0.0
        assert acos_deg(0.5) == pytest.approx(60.0)
        assert acos_deg(math.sqrt(2) / 2) == pytest.approx(45.0)
        assert acos_deg(0) == pytest.approx(90.0)

    def test_acos_deg_boundary_values(self):
        """Test arccosine in degrees at domain boundaries."""
        assert acos_deg(1) == pytest.approx(0.0)
        assert acos_deg(-1) == pytest.approx(180.0)

    def test_acos_deg_invalid_greater_than_one(self):
        """Test that arccosine in degrees raises ValueError for values > 1."""
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos_deg(1.1)
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos_deg(2.0)

    def test_acos_deg_invalid_less_than_minus_one(self):
        """Test that arccosine in degrees raises ValueError for values < -1."""
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos_deg(-1.1)
        with pytest.raises(ValueError, match="Arccosine domain is \\[-1, 1\\]"):
            acos_deg(-2.0)


class TestAtanDeg:
    """Test cases for the atan_deg function."""

    def test_atan_deg_zero(self):
        """Test arctangent in degrees of zero."""
        assert atan_deg(0) == 0.0

    def test_atan_deg_positive_values(self):
        """Test arctangent in degrees with positive values."""
        assert atan_deg(1) == pytest.approx(45.0)
        assert atan_deg(math.sqrt(3)) == pytest.approx(60.0)
        assert atan_deg(1 / math.sqrt(3)) == pytest.approx(30.0)

    def test_atan_deg_negative_values(self):
        """Test arctangent in degrees with negative values."""
        assert atan_deg(-1) == pytest.approx(-45.0)
        assert atan_deg(-math.sqrt(3)) == pytest.approx(-60.0)

    def test_atan_deg_large_values(self):
        """Test arctangent in degrees with large values approaches 90."""
        assert atan_deg(1000) == pytest.approx(90.0, abs=0.1)
        assert atan_deg(-1000) == pytest.approx(-90.0, abs=0.1)


class TestRadians:
    """Test cases for the radians function."""

    def test_radians_zero(self):
        """Test conversion of zero degrees to radians."""
        assert radians(0) == 0.0

    def test_radians_common_angles(self):
        """Test conversion of common angles from degrees to radians."""
        assert radians(90) == pytest.approx(math.pi / 2)
        assert radians(180) == pytest.approx(math.pi)
        assert radians(270) == pytest.approx(3 * math.pi / 2)
        assert radians(360) == pytest.approx(2 * math.pi)
        assert radians(30) == pytest.approx(math.pi / 6)
        assert radians(45) == pytest.approx(math.pi / 4)
        assert radians(60) == pytest.approx(math.pi / 3)

    def test_radians_negative_values(self):
        """Test conversion of negative angles from degrees to radians."""
        assert radians(-90) == pytest.approx(-math.pi / 2)
        assert radians(-180) == pytest.approx(-math.pi)


class TestDegrees:
    """Test cases for the degrees function."""

    def test_degrees_zero(self):
        """Test conversion of zero radians to degrees."""
        assert degrees(0) == 0.0

    def test_degrees_common_angles(self):
        """Test conversion of common angles from radians to degrees."""
        assert degrees(math.pi / 2) == pytest.approx(90.0)
        assert degrees(math.pi) == pytest.approx(180.0)
        assert degrees(3 * math.pi / 2) == pytest.approx(270.0)
        assert degrees(2 * math.pi) == pytest.approx(360.0)
        assert degrees(math.pi / 6) == pytest.approx(30.0)
        assert degrees(math.pi / 4) == pytest.approx(45.0)
        assert degrees(math.pi / 3) == pytest.approx(60.0)

    def test_degrees_negative_values(self):
        """Test conversion of negative angles from radians to degrees."""
        assert degrees(-math.pi / 2) == pytest.approx(-90.0)
        assert degrees(-math.pi) == pytest.approx(-180.0)

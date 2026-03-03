import math
import pytest
import student_code

def test_calculate_radius_basic():
    # Test with area = 314.159... (expected radius = 10)
    expected = 10.0
    actual = student_code.calculate_radius(math.pi * 100)
    assert actual == pytest.approx(expected, rel=1e-3), f"Expected {expected}, but got {actual}"

def test_calculate_radius_small():
    # Test with area = pi (expected radius = 1)
    assert student_code.calculate_radius(math.pi) == pytest.approx(1.0)

def test_calculate_radius_zero():
    # Test with area = 0
    assert student_code.calculate_radius(0) == 0.0

def test_calculate_radius_type():
    # QA Check: Ensure the return type is a float or int, not a string
    result = student_code.calculate_radius(10)
    assert isinstance(result, (int, float)), "Function must return a numerical value."

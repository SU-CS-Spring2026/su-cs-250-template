import student_code
import pytest

def test_area_positive():
    assert student_code.calculate_area(5) == 78.54 # Simple check
    
def test_area_zero():
    assert student_code.calculate_area(0) == 0

def test_invalid_input():
    with pytest.raises(ValueError):
        student_code.calculate_area(-1)

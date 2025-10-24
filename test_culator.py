import pytest
from MEHculator import multiply,divide,add,subtract,power_of

def test_add():
    """Tests the addition function"""
    assert add(7,10000000000000000000000000003) == 10000000000000000000000000010
    assert add(2,10) == 12
def test_subtract():
    """Tests the subtraction function"""
    assert subtract(16,3) == 13
    assert subtract(10203222001, 1) == 10203222000
def test_divide():
    """Tests the division function"""
    assert divide(4,2) == 2
    assert divide(3,0) == 0 #failure
def test_multiply():
    """Tests the multiplication function"""
    assert multiply(3,3) == 9
    assert multiply(12,4) == 48
def test_exponent():
    """Tests the exponentials function"""
    assert power_of(4,2) == 16
    assert power_of(102387218277189723, 1) == 102387218277189723
from src.DescendingOrder import descending_order
import pytest

def test_order():
    
    assert descending_order(0) == 0
    assert descending_order(15) == 51
    assert descending_order(123456789) == 987654321
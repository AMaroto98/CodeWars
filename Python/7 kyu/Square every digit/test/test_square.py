from src.SquareEveryDigit import square_digits
import pytest

def test_square():

    assert square_digits(9119) == 811181
    assert square_digits(0) == 0
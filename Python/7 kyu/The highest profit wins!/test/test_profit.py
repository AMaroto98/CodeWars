from src.TheHighestProfitWins import min_max
import pytest

def test_profit():

    assert (min_max([1,2,3,4,5]) == [1, 5])
    assert (min_max([2334454,5]) == [5, 2334454])
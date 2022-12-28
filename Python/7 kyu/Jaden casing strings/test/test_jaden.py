from src.jaden import to_jaden_case
import pytest
 
def test_jaden():
    quote = "How can mirrors be real if our eyes aren't real"
    assert to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real"
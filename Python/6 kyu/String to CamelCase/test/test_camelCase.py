from src.StringToCamelCase import to_camel_case
import pytest

def test_camel():
    assert to_camel_case("") == "", "An empty string was provided but not returned"
    assert to_camel_case("the_stealth_warrior"), "theStealthWarrior" == "to_camel_case('the_stealth_warrior') did not return correct value"
    assert to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior" == "to_camel_case('The-Stealth-Warrior') did not return correct value"
    assert to_camel_case("A-B-C"), "ABC" == "to_camel_case('A-B-C') did not return correct value"
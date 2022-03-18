"""Place to Test Functions in the EX06 Dictionary Function Assignment."""

__author__ = "730322370"

from dictionary import invert, favorite_color, count


def test1_invert() -> None: 
    """To Test Invert Function Once."""
    assert invert({'a': 'z', 'b': 'y'}) == {'z': 'a', 'y': 'b'}
 

def test2_invert() -> None: 
    """To Test Invert Function Twice."""
    assert invert({'1': '2', '5': '3'}) == {'2': '1', '3': '5'}


def test3_invert() -> None: 
    """To Test Invert Function Thrice."""
    assert invert({'4': '4', '4': '4'}) == {'4': '4', '4': '4'}


def test1_favorite_color() -> None: 
    """To Test Favorite Color Function Once."""
    assert favorite_color({"Marc": "yellow", "Summer": "yellow"}) == "yellow"


def test2_favorite_color() -> None: 
    """To Test Favorite Color Function Twice."""
    assert favorite_color({"Marc": "yellow", "Summer": "green"}) == "yellow"


def test3_favorite_color() -> None: 
    """To Test Favorite Color Function Thrice."""
    assert favorite_color({"Marc": "yellow", "Summer": "purple", "Dian": "yellow"}) == "yellow"


def test1_count() -> None: 
    """To Test Count Function Once."""
    assert count(["a", "b", "b", "a"]) == {"a": 2, "b": 2}
 

def test2_count() -> None: 
    """To Test Count Function Twice."""
    assert count(["Marc", "Summer", "Summer", "Dian"]) == {"Marc": 1, "Summer": 2, "Dian": 1}


def test3_count() -> None: 
    """To Test Count Function Thrice."""
    assert count(["1", "2", "2", "2", "1", "3"]) == {"1": 2, "2": 3, "3": 1}


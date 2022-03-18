"""Place to Test Functions for the Utils Functions."""


___author__ = "730322370"


from utils import only_evens, sub, concat 


def test1_only_evens() -> None: 
    """To Test Only Evens Function Once."""
    assert only_evens([1, 2, 3]) == [2]


def test2_only_evens() -> None: 
    """To Test Only Evens Function Twice."""
    assert only_evens([1, 5, 3]) == []


def test3_only_evens() -> None: 
    """To Test Only Evens Function Thrice."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test1_sub() -> None: 
    """To Test Sub Function Once."""
    some_list = [10, 20, 30, 40]
    assert sub(some_list, 1, 3) == [20, 30]


def test2_sub() -> None: 
    """To Test Sub Function Twice."""
    some_list = [10, 20, 30, 40]
    assert sub(some_list, -1, 3) == [10, 30]


def test3_sub() -> None: 
    """To Test Sub Function Thrice."""
    some_list = [10, 20, 30, 40]
    assert sub(some_list, 100, 3) == []


def test1_concat() -> None:
    """To Test Concat Function Once."""
    list_one = [1, 2, 3, 4]
    list_two = [5, 6, 7, 8]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8]


def test2_concat() -> None:
    """To Test Concat Function Twice."""
    list_one = [1, 2, 3, 4]
    list_two = [5, 6, 7, 8]
    assert concat(list_two, list_one) == [5, 6, 7, 8, 1, 2, 3, 4]


def test3_concat() -> None:
    """To Test Concat Function Thrice."""
    list_two = [5, 6, 7, 8]
    list_three = [9] 
    assert concat(list_two, list_three) == [5, 6, 7, 8, 9]
    
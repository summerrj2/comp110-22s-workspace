"""EX06 Dictionary Functions."""


__author__ = "730322370"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """To Invert a Dictionary."""
    index = 0 
    list_of_keys = list()
    list_of_values = list()
    new_dictionary = dict() 
    for key in dictionary: 
        temp_key: str = key 
        temp_value = dictionary[key]  
        list_of_keys.append(temp_key)
        list_of_values.append(temp_value)
    call_error(list_of_values)
    for key in list_of_values:
        new_dictionary[key] = list_of_keys[index]
        index += 1
    return new_dictionary


def call_error(a_list: list[str]) -> None: 
    """To Raise an Error for Dictionary Inversion.""" 
    index_a = 0 
    index_b = 0
    while index_a < len(a_list): 
        while index_b < len(a_list): 
            if index_b != index_a: 
                if a_list[index_a] == a_list[index_b]: 
                    raise KeyError("This list kinda trash")
            index_b += 1 
        index_a += 1 


def favorite_color(colors: dict[str, str]) -> str:
    """To Find the Favorite Color."""
    new_dictionary: dict[str, int] = dict()
    for key in colors: 
        value = colors[key]
        is_color_present: bool = value in new_dictionary
        if is_color_present is True: 
            new_dictionary[value] += 1
        else: 
            new_dictionary[value] = 1 
    highest_count: int = 0 
    highest_color: str = ""
    for key in new_dictionary:
        current_value = new_dictionary[key]
        if current_value > highest_count:
            highest_color = key
            highest_count = current_value
    return highest_color

def count(some_list: list[str]) -> dict[str, int]:
    """To Count The Numbers of Unique Values in a List."""
    new_dictionary: dict[str, int] = dict()
    for item in some_list: 
        is_color_present: bool = item in new_dictionary
        if is_color_present is True: 
            new_dictionary[item] += 1
        else: 
            new_dictionary[item] = 1 
    return new_dictionary

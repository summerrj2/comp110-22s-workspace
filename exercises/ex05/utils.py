"""Place to Implement Function Skeleton."""


__author__ = "730322370"


def only_evens(list_of_integers: list[int]) -> list[int]: 
    """To Return Only Even Elements in the Input Parameter."""
    index: int = 0 
    while index < len(list_of_integers): 
        if list_of_integers[index] % 2 != 0: 
            list_of_integers.pop(index)
        else: 
            index += 1 
    return list_of_integers


def sub(some_list: list[int], start_index: int, end_index: int) -> list[int]:
    """To Return a Subset of a Given List Between Two Indices."""
    if start_index < 0: 
        start_index = 0 
    if end_index > len(some_list): 
        end_index = len(some_list)
    sub_set_list: list[int] = list() 
    if len(some_list) == 0 or start_index >= len(some_list) or end_index <= 0: 
        return sub_set_list
    sub_set_list.append(some_list[start_index]) 
    sub_set_list.append(some_list[end_index - 1]) 
    return sub_set_list 


def concat(list_one: list[int], list_two: list[int]) -> list[int]: 
    """To Return a List that is the Product of Two Lists Squished Together."""
    final_list = list()
    list_one_length: int = len(list_one)
    list_two_length: int = len(list_two)
    index: int = 0 
    while index < list_one_length: 
        final_list.append(list_one[index])
        index += 1
    index -= index 
    while index < list_two_length: 
        final_list.append(list_two[index])
        index += 1
    return final_list
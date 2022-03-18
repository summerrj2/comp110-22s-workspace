import random
"""Wordle - EX02."""

__author__ = "730322370"


def contains_char(guessed_word: str, single_character: str) -> bool: 
    """Searching for Single Character in Guessed Word."""
    assert len(single_character) == 1
    index: int = 0 
    while index < len(guessed_word):
        if single_character == guessed_word[index]: 
            return True
        index = index + 1  
    return False


def emojified(guess_string: str, secret_string: str) -> str: 
    """To return a string of emojis."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji: str = ""
    assert len(guess_string) == len(secret_string)
    while index < len(secret_string): 
        if guess_string[index] == secret_string[index]: 
            emoji = emoji + GREEN_BOX
        else: 
            contains_character: bool = contains_char(secret_string, guess_string[index])
            if contains_character is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        index = index + 1
    return emoji


def input_guess(expected_length: int) -> str: 
    """To Prompt a User for a Guess."""
    guess_string: str = input(f"Enter a {expected_length} character word:")
    while len(guess_string) != expected_length:
        guess_string = input(f"That wasn't {expected_length} chars! Try again:")
    return guess_string


def main() -> None: 
    """The Entrypoint of the Program and the Main Game Loop."""
    turn_number: int = 1
    strings = ["adieu", "bitch", "exist", "moxie", "scone", "scorn", "vices", "vixen", "might", "trust", "skiff", "kaput", "caput", "dived", "zebra"]
    secret_string: str = random.choice(strings)
    has_won: bool = False 
    while turn_number < 7 and has_won is not True: 
        print(f"=== Turn {turn_number}/6 ===")
        guess_string = input_guess(len(secret_string))
        print(emojified(guess_string, secret_string))
        if guess_string == secret_string:
            print(f"You won in {turn_number}/6 turns!")
            has_won = True 
        turn_number += 1
    if turn_number == 7 and has_won is not True: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__": 
    main() 
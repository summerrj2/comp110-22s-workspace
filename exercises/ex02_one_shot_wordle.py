"""One Short Wordle Exercise 02."""

__author__ = "730322370"

SECRET: str = "python"
guess: str = input("What is your 6-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = ""
guessed_character: bool = False
alternative_indices: int = 0 

while len(guess) != len(SECRET):
    guess: str = input(f"That was not {len(SECRET)} letters! Try again:")

while index < len(SECRET): 
    if guess[index] == SECRET[index]: 
        emoji: str = (f"{emoji}{GREEN_BOX}") 
        index = index + 1 
    else: 
        while guessed_character is not True and alternative_indices < len(SECRET):
            if guess[index] == SECRET[alternative_indices]:
                alternative_indices = alternative_indices + 1
                guessed_character: bool = True 
        if guessed_character is True: 
            emoji: str = (f"{emoji}{YELLOW_BOX}")
            index = index + 1 
        else: 
            emoji: str = (f"{emoji}{WHITE_BOX}")
            index = index + 1

print(emoji) 
if guess != SECRET: 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")
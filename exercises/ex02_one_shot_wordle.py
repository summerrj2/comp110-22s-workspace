"""One Short Wordle Exercise 02."""

__author__ = "730322370"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
SECRET: str = "eight"
guess: str = input(f"What is your {len(SECRET)}-letter guess?")
index: int = 0
emoji: str = ""

while len(guess) != len(SECRET):
    guess = input(f"That was not {len(SECRET)} letters! Try again:")

while index < len(SECRET): 
    if guess[index] == SECRET[index]: 
        emoji = emoji + GREEN_BOX
        index = index + 1 
    else: 
        guessed_character: bool = False
        alternative_index: int = 0 
        while guessed_character is not True and alternative_index < len(SECRET):
            if guess[index] == SECRET[alternative_index]:
                guessed_character = True 
                alternative_index = alternative_index + 1
                emoji = emoji + YELLOW_BOX
            else: 
                alternative_index = alternative_index + 1
        if guessed_character is not True: 
            emoji = emoji + WHITE_BOX 
        index = index + 1

print(emoji) 
if guess != SECRET: 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")
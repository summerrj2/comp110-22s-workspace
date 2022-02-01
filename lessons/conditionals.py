"""An example of conditional (-f-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("what is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!")
    print("Have a wonderful day!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    prin("Try running the program again")

print("Game over.")
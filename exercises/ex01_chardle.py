"""EX01 Chardle -- A Word Game."""

__author__ = "730322370"

code_word: str = input("Enter a 5-character word:")

if len(code_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit() 

character: str = input("Enter a single character:")

if len(character) != 1:
    print("Error: Character must be a single character")
    exit()

instance: int = 0 

print("Searching for " + character + " in " + code_word) 

if character == code_word[0]: 
    print(character + " found at index 0")
    instance = instance + 1
if character == code_word[1]: 
    print(character + " found at index 1")
    instance = instance + 1
if character == code_word[2]: 
    print(character + " found at index 2")
    instance = instance + 1
if character == code_word[3]: 
    print(character + " found at index 3")
    instance = instance + 1
if character == code_word[4]: 
    print(character + " found at index 4") 
    instance = instance + 1

if instance == 0: 
    print("No instances of " + character + " found in " + code_word)
else:
    if instance == 1: 
        print(str(instance) + " instance of " + character + " found in " + code_word)
    else: 
        if instance >= 2: 
            print(str(instance) + " instances of " + character + " found in " + code_word) 

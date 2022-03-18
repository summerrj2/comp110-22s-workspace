"""Example of writing a function to search a list."""


def main() -> None: 
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["Pokemon", "Wordle"]
    if contains(guess, possible_answers): 
        print("We're letting the secret club..." )
    else: 
        print("Go back to Davis")


# Define a function names contains
# Parameters 
#   1. needle - str we're looing for 
#   2. haystack - list of strs we're looking through 
def contains(needle: str, haystack: list[str]) -> bool:
    """Test if Needle is Found in Haystack."""
# Algorithm: for each item in haystack: 
#   Test if equal to needle 
#       If so, return True 
    for item in haystack: 
        if item == needle: 
            return True 
#   After all iteams checked, return False if needle not found 
    return False
#   Returns True if needle found 


print(__name__)

if __name__ == "__main__": 
    main()
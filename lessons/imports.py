"""Examples of Importing Python."""


from lessons import helpers 

# Import names defined globally in a module 
from lessons.helpers import powerful 

# To Alias a module 
from lessons import helpers as hp 


def main() -> None: 
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))

if __name__ == "__main__":
    main()

main()
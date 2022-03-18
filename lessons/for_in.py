"""Example of for in syntax."""

names: list[str] = ["Summer", "Dian", "Monica", "Jacob"]

#Example of iterating through names in a while loop 
i: int = 0 
while i < len(names): 
    name: str = names[i]
    print(name) 
    i += 1 

# The following for...in loop is the same as the while loop
for name in names: 
    print(name)
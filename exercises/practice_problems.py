a: int = 8 
b: int = 2
c: int = 0 

i: int = 2

while a > b: 
    if a % 2 == 0: 
        b += 2
    elif a % 3 == 0: 
        b += 1
    elif a % 2 == 1: 
        if a % 7 == 0: 
            while i > 0: 
                b -= i 
                i -= 1
            i = 2
        b += 1
    a -= 1
    c += 1

print(a)
print(b)
print(c)

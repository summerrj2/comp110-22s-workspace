

a = "a" 
b = "a" + "c"
print(b + a)
b = b + "b"
a = a + b[len(a) + 1]
print(a[1])
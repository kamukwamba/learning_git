def divide(a,b):
    c = a/b
    d = a%b
    if d == 0:
        print(b, "is a factor of \"a\"")

    return c

def mult(a,b):
    c = a*b 
    return c

def add(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

print(divide(10, 4))
print(divide(10,2))


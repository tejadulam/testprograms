# Write a function named type_check that takes two parameters and it should return True if both parameters are of the same data type, and False otherwise.
# For example, calling type_check(1, 2) should return True, while calling type_check("a", 1) should return False.


def type_check(a,b):
    if type(a) == type(b):
        return ("True")
    else:
        return ("false")
    
print(type_check("teja",34))
print(type_check(12.23,34.3))


def type_check(a,b):
    return type(a) == type(b)
r1 = type_check(1,2)
r2 = type_check("a",1)
print(r1,r2)
# Write a function ‘round_to_two_places’ which takes one argument ‘num’ and returns 
# the given number rounded to two decimal places. For Example, round_to_two_places(3.14159) should return 3.14.

def round_two_places(x):
    return round(x,2)
print(round_two_places(12.345))
print(round_two_places(123.4567))
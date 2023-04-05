# Write a program "num_identifier.py" that will print whether the number is a single digit number or double digit number or big number.

n = int(input("enter n: "))
if n <= 9:
    print("given num is single digit number")
elif n<=99:
    print("given num is double digit number")
else:
    print("given number is big number")
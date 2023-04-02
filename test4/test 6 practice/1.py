# Write a program "count_digits.py" to print the number of digits in the given number.

n = (input("enter number: "))
count = 0
for i in n:
    if i.isdigit():
        count+=1
print(count)
print(f"The number of digit in given number is {count}")
# Write a program "list_reverse.py" to  reverse a list without using list slicing?

l = []
for x in range(5):
    n = int(input("enter num: "))
    l.append(n)
print(l)
l.reverse()
print(l)
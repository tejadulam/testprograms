# Write a program "dups.py" to print a list with all duplicates in the given list. For example, if lst=[1, 3, 2, 1, 2, 5, 6] it should return [1, 2].

l1 = []
n = int(input("enter no of times : "))
for i in range(n):
    v = int(input("enter n: "))
    l1.append(v)
print(l1)
l2 = []
for i in l1:
    if l1.count(i)!=1 and i not in l2:
        l2.append(i)
print(l2)


r = []
for i in range(5):
    n = int(input("enter n:"))
    r.append(n)
print(r)
r.sort()
print("the largest number in the list is", r[-1])
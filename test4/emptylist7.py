l = []
for i in range(5):
    n = int(input("enter n: "))
    if n not in l:
        print("list contain elements")
    else:
        print("empty list")
    l.append(n)
    print(l)
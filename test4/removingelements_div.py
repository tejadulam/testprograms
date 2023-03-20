l = []
for i in range(6):
    n = int(input("enter n: "))
    if n%3!=0:
        l.append(n)
print(l)

#first enter elements [3,1,21,44,22,27]
#remove those elements divisible by 3 [1,44,22]
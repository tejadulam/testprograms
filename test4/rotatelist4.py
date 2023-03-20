l = []
for i in range(5):
    n = int(input("enter n: "))
    l.append(n)
print(l)
print(l[-1:]+l[:-1])

#[3,2,1,4,5]
#[5,3,2,1,4]
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
c = 0
for i in tuple:
    if i%2==0:
        c+=1
print("Number of even numbers",c)
s = 0
for i in tuple:
    if i%2!=0:
        s+=1
print("Numbers of odd numbers",s)
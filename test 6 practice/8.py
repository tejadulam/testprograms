# Write a program "invert_dict.py" to interchange keys and values in a dictionary. For example, if the given dictionary is {'x':1,'y':2,'z':3}, it should return {1:'x',2:'y',3:'z'}.


d = {"x":1,"y":2,"z":3}
m = {}
for key in d:
    value = d[key]
    m[value] = key
print(m)
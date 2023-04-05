# Write a function to display the elements of list thrice if it is a number and display the element terminated with ‘#’ if it is not a number.

def elements(data):

    for x in data:
        if x.isdigit():
            return (x*3)
        elif x.isalpha():
            return (x,"#")
print(elements(["41","DHURVA","GURU","13"]))
    
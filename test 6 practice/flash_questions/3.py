# ----- question 3
# 3. Write a function that returns the second highest number in a list.
def second_highest(l):
    '''
    This function will return second highest number in a given list

    Parameters:
        l : list of numbers

    Returns: 
        This will return the second highest number from the given list

    '''
    try:
        n = sorted(l,reverse = True)#---here we are sorting the given list 
        r = n[1]  
        return r
    except Exception as err:
        return

l = [9, 5]
print(second_highest(l))


# ------ Normal Logic------
def second_highest_number(l):
    '''
        This function will return second highest number in a given list

    Parameters:
        l : list of numbers
    
    Returns: 
        This will return the second highest number from the given list

    '''
    n = sorted(l,reverse = True)
    return n[1]
l = [34,99,77,66]
print(second_highest_number(l))

# ----- Another Method -----
def second_largest_number(num):
    if len(num) >= 2:
        return sorted(num,reverse = True)
    return "Given list contains less than 2 elements"
num = [12,44,66]
print(second_largest_number(num))
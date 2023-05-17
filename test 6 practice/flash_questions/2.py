# ----- question 2
"""2. Given a list of n tuples, where each tuple contains 3 elements.
 Write a function that return the sorted list of tuples based on second element in each tuple."""

def sorted_list_tuples_second_element(elements):
    '''
    This function will return the sorted list of tuples based on second elements

    Parameters:
        elements : list of tuples(each tuple contains 3 elements)
    Returns:
        this will return the sorted list of tuples based on 2nd element in tuple
    '''
    return sorted(elements,key = lambda x:x[1])

elements = [("abc",99,39000.03),("xyz",23,33000.23),("pqr",88,35000.5)]
print(sorted_list_tuples_second_element(elements))

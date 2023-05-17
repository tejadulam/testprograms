# ------ question 1
# 1. Write a function that returns the common elements between two given lists.
def common_element(l1,l2):
    '''
    This function return the common elements between 
    two given lists

    Parameters:
        l1 : list of numbers
        l2 : list of numbers

    Returns:
        This will return the common elements in given lists
    '''
    return  list(set(l1).intersection(l2))

l1 = [2,3,5,6]
l2 = [3,8,5,7]
print(common_element(l1,l2))
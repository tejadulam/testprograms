# ----------- question 4
# 4. Write a function that returns the first non-repeating character in a string.

def first_non_repeating_char(string):
    '''
    This function will return the first non repeating character in string

    Parameters:
        input_string : string

    Returns:
        this will return the non repeating character

    '''
    for char in string:
        if string.count(char) == 1:
            return char
    return None

# Calling function
input_string = "abracadabra"
result = first_non_repeating_char(input_string)
print(result)
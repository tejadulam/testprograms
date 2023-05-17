# ------ question 5
# 5. Write a function that checks if two strings (for example, listen and silent) are anagrams of each other.
 
def check_two_strings(s1, s2):
    '''
    This function will check given 2 strings are anagrams of each other

    Parameters : 
        s1 : string
        s2 : string
    
    Returns:
        return the given strings are anagrams of each other or not
    '''
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 ="listen"
s2 ="silent"
check_two_strings(s1, s2)
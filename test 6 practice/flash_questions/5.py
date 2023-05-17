# ------ question 5
# 5. Write a function that checks if two strings (for example, listen and silent) are anagrams of each other.
 
def check_two_strings(s1, s2):
    '''
    This function will return the 
    '''
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 ="listen"
s2 ="silent"
check_two_strings(s1, s2)
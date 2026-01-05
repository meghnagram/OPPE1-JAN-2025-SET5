def has_no_vowels_in_even_indices(s: str) -> bool:
    """Checks if there are no vowels in even indices of a string.

    Args:
        s (str): The input string.

    Returns:
        bool: True if no vowels are in even indices, False otherwise.
    """
    
    return not (set(s[::2].lower()) & set("aeiou")) 

# def has_no_vowels_in_even_indices(s: str) -> bool:
#     c=0
#     for i in range(len(s)):
#         if i%2==0 and s[i] in ('a','e','i','o','u'):
#             c=1
      
      
#     if c==1:       
#         return False
#     else:
#         return True

# Check If a String has No Vowels in Even Indices
# Write a function has_no_vowels_in_even_indices that takes a string s as input and returns True if there are no vowels in the even indices of the string, otherwise returns False.

# Examples

# >>> has_no_vowels_in_even_indices("babebibobu") # The vowels are present in odd indices
# True
# >>> has_no_vowels_in_even_indices("abcde") # a is present in even index 0
# False
# >>> has_no_vowels_in_even_indices("test") # only vowel e is present in odd index 1
# True 
# >>> has_no_vowels_in_even_indices("why") # no vowels
# True 
        
        

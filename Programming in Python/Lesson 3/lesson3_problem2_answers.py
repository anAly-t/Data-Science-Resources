# Practice Exercise 2: Is the string a palindrome?

def is_palindrome(s):
    # Edge case: Empty string or single character string is always a palindrome
    if len(s) <= 1:
        return True
    
    # Convert the string to lowercase and remove spaces and punctuation
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))                        # Output: True
print(is_palindrome("hello"))                          # Output: False
print(is_palindrome(""))                               # Output: True (empty string is considered palindrome)
print(is_palindrome("a"))                              # Output: True (single character string is considered palindrome)

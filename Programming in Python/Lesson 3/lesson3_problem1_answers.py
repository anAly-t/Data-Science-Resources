# DASC1092 Practice Exercise Lesson 3 Problem 1

# Practice Assignment 1: Even, Odd, or Zero

def classify_number(num):
    # Check if the input is not an integer
    if not isinstance(num, int):
        return "Input is not an integer"

    # Check if the number is zero
    if num == 0:
        return "Zero"
    
    # Check if the number is positive
    elif num > 0:
        # Check if the number is even
        if num % 2 == 0:
            return "Positive Even"
        # If not even, it must be odd
        else:
            return "Positive Odd"
    
    # If the number is not positive (it's negative)
    else:
        # Check if the number is even
        if num % 2 == 0:
            return "Negative Even"
        # If not even, it must be odd
        else:
            return "Negative Odd"

# Test cases
print(classify_number(4))      # Output: Positive Even
print(classify_number(3))      # Output: Positive Odd
print(classify_number(-2))     # Output: Negative Even
print(classify_number(-7))     # Output: Negative Odd
print(classify_number(0))      # Output: Zero
print(classify_number(2.5))    # Output: Input is not an integer

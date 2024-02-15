### Easy Debugging Practice Exercises:

# Problem 1 - Syntax error:

def print_message():
       print("Hello, Debugging!")

# Problem 2 - Logical error:
def calculate_sum(a, b):
       result = a + b  # Fixed: Changed subtraction to addition
       return result


# Problem 3 - Runtime error:
def divide_numbers(x, y):
       result = x / y  # Fixed: Removed division by zero error
       return result


# Problem 4 - Indentation error:
for i in range(5):
    print(i)


# Problem 5 - Variable name error:
import math

def calculate_area(radius):
       area = math.pi * radius**2  # Fixed: Added 'math.' to reference 'pi'
       return area

# Problem 6 - Type error:
result = "3" + str(4)  # Fixed: Converted integer to string before concatenation


# Problem 7 - List comprehension error:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]  # Fixed: Added exponent value


# Problem 8 - Logical error in factorial calculation:
def factorial(n):
       result = 1
       for i in range(1, n + 1):  # Fixed: Adjusted the range and multiplication logic
           result = result * i
       return result


# Problem 9 - Loop to print even numbers:
for i in range(10):
       if i % 2 == 0:
           print(i)

### Hard Debugging Practice Exercises:

# Hard Problem 1 - Calculate average:
def calculate_average(numbers):
       total = sum(numbers)  # Fixed: Used the built-in 'sum' function
       average = total / len(numbers)
       return average

   # Test the function
grades = [90, 85, 92, 88, 95]
result = calculate_average(grades)
print(f"Average Grade: {result}")


# Hard Problem 2 - Palindrome check:
# No, there are no errors
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

   # Test the function
test_string = "level"
if is_palindrome(test_string):
       print(f"{test_string} is a palindrome.")
else:
       print(f"{test_string} is not a palindrome.")


# Hard Problem 3 - Filter even numbers:
# Possible runtime error
def divide_numbers(x, y):
        if y != 0:  # Fixed: Added a check to avoid division by zero
            result = x / y
            return result
        else:
            print("Error: Division by zero is not allowed.")
            return None  # or handle it according to your specific needs

# added a check to ensure that the denominator y is not zero before performing the division. If it is zero, an error message is printed, and the function returns None 
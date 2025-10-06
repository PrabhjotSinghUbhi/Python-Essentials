# 04_function_in_python.py

# Introduction to Functions in Python

# What is a function?
# A function is a block of code that performs a specific task.
# Functions help us organize code, avoid repetition, and make programs easier to read.

# 1. Defining a simple function
def greet():
    print("Hello, welcome to Python functions!")

# 2. Calling a function
greet()  # This will print the greeting message

# 3. Function with parameters (inputs)
def add_numbers(a, b):
    result = a + b
    print("The sum is:", result)

add_numbers(5, 3)  # Output: The sum is: 8

# 4. Function with a return value
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print("The product is:", product)  # Output: The product is: 24

# 5. Default parameter values
def say_hello(name="Guest"):
    print("Hello,", name)

say_hello("Alice")  # Output: Hello, Alice
say_hello()         # Output: Hello, Guest

# 6. Functions can return multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9, 4]
minimum, maximum = get_min_max(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)

# 7. Docstrings: Documenting your functions
def square(n):
    """Returns the square of a number n."""
    return n * n

print(square(5))  # Output: 25

# Summary:
# - Define functions using 'def'
# - Call functions by their name followed by parentheses
# - Use parameters to pass data to functions
# - Use 'return' to send back a result
# - Use docstrings to describe what your function does
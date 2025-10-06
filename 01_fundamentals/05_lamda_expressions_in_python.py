# 05_lambda_expressions_in_python.py

"""
Lambda Functions in Python
--------------------------

Lambda functions are small, anonymous functions defined with the `lambda` keyword.
They are useful for creating simple functions without giving them a name.

Syntax:
    lambda arguments: expression

The expression is evaluated and returned.
"""

# Example 1: A simple lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print("add_ten(5):", add_ten(5))  # Output: 15

# Example 2: Lambda function with two arguments
multiply = lambda a, b: a * b
print("multiply(3, 4):", multiply(3, 4))  # Output: 12

# Example 3: Using lambda with the `map` function
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)  # Output: [1, 4, 9, 16]

# Example 4: Using lambda with the `filter` function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4]

# Example 5: Lambda in sorting
pairs = [(1, 3), (2, 2), (4, 1)]
# Sort by the second element of each tuple
pairs_sorted = sorted(pairs, key=lambda x: x[1])
print(
    "Pairs sorted by second element:", pairs_sorted
)  # Output: [(4, 1), (2, 2), (1, 3)]

"""
When to use lambda functions:
- When you need a small function for a short period of time.
- When passing a simple function as an argument (e.g., to map, filter, or sort).

Limitations:
- Lambda functions can only contain a single expression.
- They are less readable for complex logic. Use `def` for larger functions.
"""


# Example 6: Equivalent function using def
def add_ten_def(x):
    return x + 10


print("add_ten_def(5):", add_ten_def(5))  # Output: 15

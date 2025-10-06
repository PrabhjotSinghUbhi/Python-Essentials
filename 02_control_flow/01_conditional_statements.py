# 01_conditional_statements.py
# Introduction to Conditional Statements in Python

# Conditional statements allow you to execute certain blocks of code based on conditions.

# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult.")

# Example 2: if-else statement
temperature = 15
if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Example 4: Nested if statements
number = 10
if number > 0:
    print("Number is positive.")
    if number % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not positive.")
# 02_input_output_in_python.py

# --- OUTPUT IN PYTHON ---

# The print() function is used to display output.
print("Hello, World!")  # Using double quotes
print('Hello, World!')  # Using single quotes

# You can use triple quotes for multi-line strings.
print("""This is a
multi-line string
using triple double quotes.""")

print('''This is also a
multi-line string
using triple single quotes.''')

# Backticks `` are NOT used for strings in Python (unlike some other languages).
# In Python, using backticks will cause a syntax error in Python 3.

# --- INPUT IN PYTHON ---

# The input() function is used to take input from the user.
name = input("Enter your name: ")
print("Hello,", name)

# By default, input() returns a string.
# To get an integer, use int() to convert the input.
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# --- FORMATTED OUTPUT ---

# You can use f-strings (formatted string literals) for formatting:
print(f"Hello, {name}. Next year you will be {age + 1} years old.")

# You can also use the format() method:
print("Hello, {}. You are {} years old.".format(name, age))

# Or use the % operator (older style):
print("Hello, %s. You are %d years old." % (name, age))

# --- ESCAPING QUOTES ---

# To include quotes inside strings, use the opposite quote or escape them:
print('He said, "Python is fun!"')
print("It's a beautiful day!")
print("He said, \"Python is fun!\"")
print('It\'s a beautiful day!')

# --- SUMMARY ---
# - Use print() for output.
# - Use input() for input (always returns a string).
# - Convert input to int/float if needed.
# - Use single, double, or triple quotes for strings.
# - Use f-strings or format() for formatted output.
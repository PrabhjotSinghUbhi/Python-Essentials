# 06_type_coversion_and_casting.py
# Type Conversion and Casting in Python

# Type Conversion (also called Type Casting) is the process of converting one data type to another.

# 1. Implicit Type Conversion
# Python automatically converts one data type to another when needed.

a = 5        # int
b = 2.0      # float

result = a + b  # int + float => float
print("Result:", result)
print("Type of result:", type(result))

# 2. Explicit Type Conversion (Casting)
# You can manually convert data types using functions like int(), float(), str(), etc.

# Convert float to int
num_float = 9.8
num_int = int(num_float)  # This will truncate the decimal part
print("num_int:", num_int)

# Convert int to float
num = 7
num_f = float(num)
print("num_f:", num_f)

# Convert int to string
age = 25
age_str = str(age)
print("age_str:", age_str)
print("Type of age_str:", type(age_str))

# Convert string to int
s = "123"
s_int = int(s)
print("s_int:", s_int)
print("Type of s_int:", type(s_int))

# Note: Not all conversions are possible!
# For example, converting a non-numeric string to int will cause an error:
# int("hello")  # This will raise a ValueError

# Practice: Try converting different types and see what happens!
# Integer division vs. float division

x = 10
y = 3

# Float division (returns a float)
float_div = x / y
print("Float division (x / y):", float_div)
print("Type of float_div:", type(float_div))

# Integer division (returns the floor of the division)
int_div = x // y
print("Integer division (x // y):", int_div)
print("Type of int_div:", type(int_div))
# 02_tuples.py
# Introduction to Tuples in Python

# What is a Tuple?
# A tuple is an ordered, immutable collection of items.
# Tuples are similar to lists, but you cannot change their contents after creation.

# Creating a tuple
my_tuple = (1, 2, 3)
print("my_tuple:", my_tuple)

# Tuples can contain different data types
mixed_tuple = (1, "hello", 3.14)
print("mixed_tuple:", mixed_tuple)

# Tuples can be nested
nested_tuple = (1, (2, 3), [4, 5])
print("nested_tuple:", nested_tuple)

# Creating a tuple with one item (note the comma)
single_item_tuple = (42,)
print("single_item_tuple:", single_item_tuple)

# Accessing tuple elements (indexing starts at 0)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Slice [1:]:", my_tuple[1:])

# Tuples are immutable: you cannot change their elements
# The following line would cause an error:
# my_tuple[0] = 10

# Tuple unpacking
a, b, c = my_tuple
print("Unpacked:", a, b, c)

# Using tuples to return multiple values from a function
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([3, 1, 4, 2])
print("Min and Max:", result)

# Tuple methods: count() and index()
sample = (1, 2, 2, 3)
print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# Why use tuples?
# - Tuples are faster than lists
# - Useful for fixed data
# - Can be used as dictionary keys

# Example: Using tuples as dictionary keys
locations = {
    (35.6895, 139.6917): "Tokyo",
    (51.5074, -0.1278): "London"
}
print("City at (35.6895, 139.6917):", locations[(35.6895, 139.6917)])
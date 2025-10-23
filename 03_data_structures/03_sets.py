# 03_sets.py
# Introduction to Sets in Python

# What is a set?
# A set is an unordered collection of unique elements.

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Numbers set (no duplicates):", numbers)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# Adding elements to a set
fruits.add("orange")
print("After adding orange:", fruits)

# Removing elements from a set
fruits.remove("banana")  # Raises KeyError if not found
print("After removing banana:", fruits)

# Discarding elements (no error if not found)
fruits.discard("pineapple")
print("After discarding pineapple (not present):", fruits)

# Checking membership
print("Is apple in fruits?", "apple" in fruits)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)

# Iterating through a set
for fruit in fruits:
    print("Fruit:", fruit)

# Sets are useful for removing duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("Unique list:", unique_list)
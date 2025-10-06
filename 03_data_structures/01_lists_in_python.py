# 01_lists_in_python.py

# Introduction to Lists in Python

# A list is a collection of items in a particular order.
# Lists are created by placing items inside square brackets [], separated by commas.

# Example of a list:
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits list:", fruits)

# Accessing elements in a list (indexing starts at 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative index counts from the end

# Modifying elements in a list
fruits[1] = "blueberry"
print("After modification:", fruits)

# Adding elements to a list
fruits.append("elderberry")  # Adds to the end
print("After appending:", fruits)

fruits.insert(1, "fig")  # Inserts at position 1
print("After inserting at index 1:", fruits)

# Removing elements from a list
fruits.remove("cherry")  # Removes first occurrence of "cherry"
print("After removing 'cherry':", fruits)

popped_fruit = fruits.pop()  # Removes and returns the last item
print("Popped fruit:", popped_fruit)
print("After popping:", fruits)

# List Methods
numbers = [3, 1, 4, 1, 5, 9, 2]
print("\nNumbers list:", numbers)

numbers.sort()  # Sorts the list in place
print("Sorted numbers:", numbers)

numbers.reverse()  # Reverses the list in place
print("Reversed numbers:", numbers)

count_ones = numbers.count(1)  # Counts occurrences of 1
print("Number of ones:", count_ones)

index_of_five = numbers.index(5)  # Finds the index of first occurrence of 5
print("Index of 5:", index_of_five)

numbers.extend([6, 7, 8])  # Adds multiple elements to the end
print("After extending:", numbers)

# Slicing lists
print("First three numbers:", numbers[:3])
print("Last two numbers:", numbers[-2:])

# Copying a list
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

# Clearing a list
numbers.clear()
print("Cleared numbers list:", numbers)

# Lists can hold any data type, even mixed types
mixed_list = [1, "hello", 3.14, True]
print("\nMixed list:", mixed_list)
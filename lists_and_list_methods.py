"""
🐍 Python Lists and List Methods - A Beginner's Guide
======================================================

This file teaches you everything you need to know about Lists in Python.
Lists are one of the most commonly used data structures in Python.
"""

print("=" * 60)
print("WELCOME TO PYTHON LISTS TUTORIAL")
print("=" * 60)
print()

# ============================================================================
# PART 1: WHAT ARE LISTS?
# ============================================================================
print("PART 1: What are Lists?")
print("-" * 60)
print("""
Lists are ordered collections that can store multiple items.
- Lists are mutable (can be changed after creation)
- Lists can contain different data types
- Lists are defined using square brackets []
- Items in a list are called elements
""")

# Creating empty lists
empty_list = []
print(f"Empty list: {empty_list}")

# Creating lists with elements
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits list: {fruits}")
print(f"Numbers list: {numbers}")
print(f"Mixed types list: {mixed}")
print()

# ============================================================================
# PART 2: ACCESSING LIST ELEMENTS
# ============================================================================
print("PART 2: Accessing List Elements")
print("-" * 60)

# Indexing (starts at 0)
print(f"First fruit (index 0): {fruits[0]}")
print(f"Second fruit (index 1): {fruits[1]}")
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second to last (index -2): {fruits[-2]}")
print()

# Slicing
print(f"First two fruits: {fruits[0:2]}")
print(f"All fruits from index 1: {fruits[1:]}")
print(f"All fruits up to index 2: {fruits[:2]}")
print()

# ============================================================================
# PART 3: MODIFYING LISTS
# ============================================================================
print("PART 3: Modifying Lists")
print("-" * 60)

# Changing elements
shopping_list = ["bread", "milk", "eggs"]
print(f"Original list: {shopping_list}")
shopping_list[0] = "whole wheat bread"
print(f"After changing first item: {shopping_list}")
print()

# ============================================================================
# PART 4: LIST METHODS
# ============================================================================
print("PART 4: List Methods")
print("-" * 60)
print()

# METHOD 1: append() - Adds an element to the end
print("1. append() - Adds an element to the end")
colors = ["red", "green", "blue"]
print(f"   Before: {colors}")
colors.append("yellow")
print(f"   After append('yellow'): {colors}")
print()

# METHOD 2: extend() - Adds all elements from another list
print("2. extend() - Adds all elements from another list")
primary_colors = ["red", "blue", "yellow"]
more_colors = ["green", "purple"]
print(f"   Before: {primary_colors}")
primary_colors.extend(more_colors)
print(f"   After extend({more_colors}): {primary_colors}")
print()

# METHOD 3: insert() - Adds an element at a specific position
print("3. insert() - Adds an element at a specific position")
animals = ["cat", "dog", "bird"]
print(f"   Before: {animals}")
animals.insert(1, "rabbit")  # Insert at index 1
print(f"   After insert(1, 'rabbit'): {animals}")
print()

# METHOD 4: remove() - Removes the first occurrence of a value
print("4. remove() - Removes the first occurrence of a value")
pets = ["dog", "cat", "fish", "cat"]
print(f"   Before: {pets}")
pets.remove("cat")  # Removes first 'cat'
print(f"   After remove('cat'): {pets}")
print()

# METHOD 5: pop() - Removes and returns element at index (default: last)
print("5. pop() - Removes and returns element at index")
numbers_list = [10, 20, 30, 40, 50]
print(f"   Before: {numbers_list}")
removed_item = numbers_list.pop()  # Removes last element
print(f"   After pop(): {numbers_list}")
print(f"   Removed item: {removed_item}")
removed_item = numbers_list.pop(1)  # Removes element at index 1
print(f"   After pop(1): {numbers_list}")
print(f"   Removed item: {removed_item}")
print()

# METHOD 6: clear() - Removes all elements
print("6. clear() - Removes all elements from the list")
temp_list = [1, 2, 3, 4, 5]
print(f"   Before: {temp_list}")
temp_list.clear()
print(f"   After clear(): {temp_list}")
print()

# METHOD 7: index() - Returns the index of first occurrence
print("7. index() - Returns the index of first occurrence")
letters = ["a", "b", "c", "d", "c"]
print(f"   List: {letters}")
position = letters.index("c")
print(f"   Index of 'c': {position}")
print()

# METHOD 8: count() - Returns the number of occurrences
print("8. count() - Returns the number of occurrences")
numbers_with_duplicates = [1, 2, 3, 2, 2, 4, 2]
print(f"   List: {numbers_with_duplicates}")
count_of_2 = numbers_with_duplicates.count(2)
print(f"   Count of 2: {count_of_2}")
print()

# METHOD 9: sort() - Sorts the list in ascending order
print("9. sort() - Sorts the list in ascending order")
unsorted_numbers = [5, 2, 8, 1, 9]
print(f"   Before: {unsorted_numbers}")
unsorted_numbers.sort()
print(f"   After sort(): {unsorted_numbers}")
# Sort in descending order
unsorted_numbers.sort(reverse=True)
print(f"   After sort(reverse=True): {unsorted_numbers}")
print()

# METHOD 10: reverse() - Reverses the order of elements
print("10. reverse() - Reverses the order of elements")
sequence = [1, 2, 3, 4, 5]
print(f"    Before: {sequence}")
sequence.reverse()
print(f"    After reverse(): {sequence}")
print()

# METHOD 11: copy() - Creates a shallow copy of the list
print("11. copy() - Creates a shallow copy of the list")
original = [1, 2, 3]
copied = original.copy()
print(f"    Original: {original}")
print(f"    Copy: {copied}")
copied.append(4)
print(f"    After modifying copy: Original={original}, Copy={copied}")
print()

# ============================================================================
# PART 5: USEFUL LIST OPERATIONS
# ============================================================================
print("PART 5: Useful List Operations")
print("-" * 60)

# Length of a list
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")
print(f"Length: {len(my_list)}")
print()

# Checking if an element exists
print(f"Is 3 in the list? {3 in my_list}")
print(f"Is 10 in the list? {10 in my_list}")
print()

# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Combined: {combined}")
print()

# Repeating lists
repeated = [1, 2] * 3
print(f"[1, 2] * 3 = {repeated}")
print()

# Min, Max, Sum (for numeric lists)
numbers_for_calc = [5, 2, 8, 1, 9, 3]
print(f"List: {numbers_for_calc}")
print(f"Minimum: {min(numbers_for_calc)}")
print(f"Maximum: {max(numbers_for_calc)}")
print(f"Sum: {sum(numbers_for_calc)}")
print()

# ============================================================================
# PART 6: LIST COMPREHENSION (BONUS)
# ============================================================================
print("PART 6: List Comprehension (Bonus)")
print("-" * 60)
print("""
List comprehension is a concise way to create lists.
Syntax: [expression for item in iterable if condition]
""")

# Creating a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

# Creating a list of even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")

# Converting to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase words: {uppercase}")
print()

# ============================================================================
# PART 7: PRACTICAL EXAMPLES
# ============================================================================
print("PART 7: Practical Examples")
print("-" * 60)

# Example 1: Managing a to-do list
print("Example 1: To-Do List Manager")
todo_list = []
todo_list.append("Buy groceries")
todo_list.append("Study Python")
todo_list.append("Exercise")
print(f"To-Do List: {todo_list}")
completed_task = todo_list.pop(0)
print(f"Completed: {completed_task}")
print(f"Remaining tasks: {todo_list}")
print()

# Example 2: Finding average of numbers
print("Example 2: Calculate Average")
scores = [85, 92, 78, 90, 88]
average = sum(scores) / len(scores)
print(f"Scores: {scores}")
print(f"Average score: {average:.2f}")
print()

# Example 3: Removing duplicates
print("Example 3: Remove Duplicates")
numbers_with_dupes = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers_with_dupes))
print(f"Original: {numbers_with_dupes}")
print(f"Unique: {unique_numbers}")
print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SUMMARY: Key Takeaways")
print("=" * 60)
print("""
✓ Lists store multiple items in an ordered collection
✓ Lists are mutable (can be changed)
✓ Lists are created with square brackets []
✓ Access elements using indices (starting from 0)
✓ Important methods:
  - append(): Add to end
  - extend(): Add multiple items
  - insert(): Add at specific position
  - remove(): Remove by value
  - pop(): Remove by index
  - sort(): Sort the list
  - reverse(): Reverse the list
  - count(): Count occurrences
  - index(): Find position
  - clear(): Remove all items
  - copy(): Create a copy

Keep practicing with lists - they're fundamental to Python!
""")
print("=" * 60)
print("Happy Learning! 🎉")
print("=" * 60)

# 04_dictionaries.py
# Introduction to Dictionaries in Python

# What is a dictionary?
# A dictionary is a collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be any data type.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Modifying an existing value
person["age"] = 26
print("After updating age:", person)

# Removing a key-value pair
del person["city"]
print("After removing city:", person)

# Checking if a key exists
if "name" in person:
    print("Name is present in the dictionary.")

# Iterating over keys and values
for key, value in person.items():
    print(key, ":", value)

# Getting all keys and values
keys = list(person.keys())
values = list(person.values())
print("Keys:", keys)
print("Values:", values)

# Dictionary methods
# .get() returns the value for a key, or a default if the key is not found
print("Phone:", person.get("phone", "Not available"))

# Clearing all items
person.clear()
print("After clearing:", person)
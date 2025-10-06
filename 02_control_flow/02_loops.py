# 02_loops.py
# Introduction to Loops in Python

# -------------------------------
# 1. The 'for' Loop
# -------------------------------
# Used to iterate over a sequence (like a list, tuple, string, or range).

print("For loop with a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nFor loop with a string:")
for letter in "hello":
    print(letter)

print("\nFor loop with range():")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

print("\nFor loop with custom start and end in range():")
for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

print("\nFor loop with step in range():")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# -------------------------------
# 2. The 'while' Loop
# -------------------------------
# Repeats as long as a condition is True.

print("\nWhile loop example:")
count = 0
while count < 5:
    print(count)
    count += 1

# -------------------------------
# 3. Loop Control Statements
# -------------------------------

# break: Exit the loop early
print("\nBreak statement in a loop:")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: Skip the current iteration
print("\nContinue statement in a loop:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# else with loops: Runs if the loop wasn't broken
print("\nElse with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break.")

print("\nElse with while loop:")
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("While loop finished without break.")

# -------------------------------
# 4. Nested Loops
# -------------------------------
# A loop inside another loop.

print("\nNested loops example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# -------------------------------
# 5. Infinite Loops (Be careful!)
# -------------------------------
# Uncomment the following lines to see an infinite loop (use Ctrl+C to stop)
# while True:
#     print("This will run forever!")

# -------------------------------
# Summary
# -------------------------------
# - Use 'for' loops to iterate over sequences.
# - Use 'while' loops when you need to repeat until a condition changes.
# - Use 'break' to exit a loop early, 'continue' to skip an iteration.
# - 'else' after a loop runs if the loop wasn't exited by 'break'.
# - Loops can be nested.
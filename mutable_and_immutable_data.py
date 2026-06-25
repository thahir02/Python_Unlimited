"""
Python Mutability and Immutability Guide
=========================================
A clean, educational guide demonstrating how memory handles different 
built-in data types in Python. Ideal for beginners and reference.

Concepts in Simple Words:
- MUTABLE: Like a whiteboard. You can change, add, or erase contents 
  without moving the board to a different room (Memory ID stays the same).
- IMMUTABLE: Like a printed book. You cannot erase its ink. To make a change, 
  you must print a brand-new book in a new location (Memory ID changes).
"""

# =====================================================================
# PART 1: IMMUTABLE TYPES (Numbers, Strings, Tuples)
# =====================================================================

# 1. Integers cannot be changed in place
x = 10
x = x + 5
print(x)  # Output: 15


# 2. Strings cannot be edited letter-by-letter
word = "Cat"
try:
    word[0] = "R"  # This will fail!
except TypeError:
    print("Cannot change string!")  # Output: Cannot change string!

# Combining strings creates a brand-new string
word = word + "s"
print(word)  # Output: Cats


# 3. Tuples are locked lists
my_tuple = (1, 2)
try:
    my_tuple[0] = 99  # This will fail!
except TypeError:
    print("Cannot change tuple!")  # Output: Cannot change tuple!


# =====================================================================
# PART 2: MUTABLE TYPES (Lists, Dictionaries, Sets)
# =====================================================================

# 1. Lists can be modified directly
my_list = ["Apple", "Banana"]
my_list.append("Cherry")
print(my_list)  # Output: ['Apple', 'Banana', 'Cherry']

my_list[0] = "Melon"
print(my_list)  # Output: ['Melon', 'Banana', 'Cherry']


# 2. Dictionaries can have values added or changed
user = {"name": "Alice", "age": 25}
user["age"] = 26  # Updates existing key
user["city"] = "Delhi"  # Adds a new key
print(user)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Delhi'}


# 3. Sets can have items added or removed dynamically
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(1)
print(numbers)  # Output: {2, 3, 4}

This code demonstrates how Python reuses memory addresses (id()) for immutable types to maximize efficiency.

# =====================================================================
# 1. INTEGER CACHING (REUSING MEMORY)
# =====================================================================

a = 100
b = 100
# Both point to the exact same cached integer object in memory
print(id(a) == id(b))  # Output: True

# =====================================================================
# 2. STRING INTERNING (REUSING TEXT MEMORY)
# =====================================================================

str1 = "hello"
str2 = "hello"
# Python automatically reuses identical short strings
print(id(str1) == id(str2))  # Output: True


# =====================================================================
# 3. CONTAINER EFFICIENCY (TUPLE VS LIST)
# =====================================================================

# Empty list vs Empty tuple
empty_list = []
empty_tuple = ()

# Tuples are strictly smaller because they don't hold extra empty buffer slots
print(sys.getsizeof(empty_list))   # Output: 56 (bytes used in memory)
print(sys.getsizeof(empty_tuple))  # Output: 40 (bytes used in memory)

# Populated list vs Populated tuple
items_list = [1, 2, 3]
items_tuple = (1, 2, 3)

print(sys.getsizeof(items_list))   # Output: 88 (bytes - contains extra padding slots for growth)
print(sys.getsizeof(items_tuple))  # Output: 64 (bytes - perfectly packed to fit 3 items)

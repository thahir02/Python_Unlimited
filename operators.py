'''
Operators in Python are special symbols used to perform operations on variables and values.
1.Arithmetic OperatorsUsed to perform common mathematical calculations.
  + (Addition) → x + y
  - (Subtraction) → x - y
  * (Multiplication) → x * y
  / (Division) → x / y (always returns a float)// (Floor Division) → x // y (rounds down to the nearest whole number)
  % (Modulus) → x % y (returns the remainder)** (Exponentiation) → x ** y (x to the power of y)

EXample
 ''''
x = 10
y = 3

print(x + y)   # 13  (Addition)
print(x - y)   # 7   (Subtraction)
print(x * y)   # 30  (Multiplication)
print(x / y)   # 3.3333333333333335 (Division always returns a float)
print(x // y)  # 3   (Floor Division rounds down)
print(x % y)   # 1   (Modulus returns the remainder)
print(x ** y)  # 1000 (10 to the power of 3)

'''
2.Assignment OperatorsUsed to assign values to variables, often combining an operation with assignment.
  = → x = 5
  += → x += 3 (same as x = x + 3)
  -= → x -= 3 (same as x = x - 3)
  *= → x *= 3 (same as x = x * 3)
  /= → x /= 3 (same as x = x / 3)

  Example
  '''
num = 5     # Assigns 5 to num
num += 3    # Same as: num = num + 3 (num is now 8)
num -= 2    # Same as: num = num - 2 (num is now 6)
num *= 2    # Same as: num = num * 2 (num is now 12)
print(num)  # Output: 12

'''
3.Comparison OperatorsUsed to compare two values, always returning a Boolean (True or False).
  == (Equal to) → x == y
  != (Not equal to) → x != y
  > (Greater than) → x > y
  < (Less than) → x < y
  >= (Greater than or equal to) → x >= y
  <= (Less than or equal to) → x <= y

  Example
  '''
a = 15
b = 20

print(a == b)  # False (Checks if equal)
print(a != b)  # True  (Checks if not equal)
print(a < b)   # True  (Checks if less than)
print(a >= b)  # False (Checks if greater than or equal to)

'''
4.Logical OperatorsUsed to combine conditional statements.
  and → Returns True if both statements are true (x < 5 and x < 10)
  or → Returns True if at least one statement is true (x < 5 or x < 4)
  not → Reverses the result, returning False if the result is true (not(x < 5))

  Example
  '''
age = 22
has_id = True
# 'and' requires BOTH conditions to be True
print(age >= 18 and has_id == True)  # Output: True
# 'or' requires AT LEAST ONE condition to be True
print(age > 30 or has_id == True)    # Output: True

# 'not' reverses the boolean value
print(not has_id)                    # Output: False

'''
5.Identity & Membership OperatorsUsed to test object identities and sequence presence.
  is → Returns True if both variables point to the same object (x is y)
  is not → Returns True if variables point to different objects (x is not y)
  in → Returns True if a sequence contains the specified value ("a" in "apple")
  not in → Returns True if a sequence does not contain the value ("z" not in "apple")

Example
'''
# Membership (in, not in)
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # Output: True
print("orange" not in fruits)  # Output: True

# Identity (is, is not)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)  # True (They have the same values)
print(list_a is list_b)  # False (They are different objects in memory)
print(list_a is list_c)  # True (They point to the exact same object)

   

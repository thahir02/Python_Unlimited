'''
String Formatting
String formatting is the process of injecting dynamic variables, values, or expressions into a static text template to create a customized final string.
Here is the evolution of string formatting in Python, from the oldest legacy method to the modern standard.

1. The Oldest Method: 
          % Formatting (C-Style)Introduced in Python 1.0, this legacy method uses placeholder tokens (like %s for strings or %d for integers) inside the text, followed by the % operator and a tuple of values.
Example :- 
'''
name = "Alice"
age = 30
# Oldest syntax
text = "My name is %s and I am %d years old." % (name, age)
print(text)
# Output: My name is Alice and I am 30 years old.

'''
2. The Intermediate Method: 
      str.format()Introduced in Python 2.6 to replace % formatting, this method uses curly braces {} as positional or keyword placeholders. The data is injected via the .format() method at the end of the string.
Example :-
'''
name = "Alice"
age = 30
# Intermediate syntax
text = "My name is {} and I am {} years old.".format(name, age)
print(text)
# Output: My name is Alice and I am 30 years old.

'''
3. The Latest Method: 
    F-Strings (Formatted String Literals)Introduced in Python 3.6 and enhanced in later versions, this is the modern standard. 
    By prefixing the string with the letter f, you can embed variables, math equations, or code expressions directly inside curly braces {}. 
    It is faster, cleaner, and the preferred way to write Python today.
Example:-
'''
name = "Alice"
age = 30
# Latest syntax
text = f"My name is {name} and I am {age} years old."
print(text)
# Output: My name is Alice and I am 30 years old.

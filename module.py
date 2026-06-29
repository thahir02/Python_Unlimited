'''
A Python module is a file containing Python code—including functions, classes, and variables—that you can reuse across different programs.
Types of Modules
  1.Built-in Modules: Pre-installed libraries included with Python (e.g., math, os, sys, random).
  2.User-Defined Modules: Custom .py files you write yourself to segment your project logic.
  3.Third-Party Modules: External code hosted on the Python Package Index (PyPI) and installed via a terminal using pip install module_name (e.g., requests, pandas, numpy).
Core Syntax and Importing MethodsYou can import code into your main file using a few variations of the import statement:
'''

# 1. Import the entire module (Requires dot notation to use components)
import math
print(math.sqrt(16))  # Outputs: 4.0

# 2. Import specific items (Bypasses the dot notation requirement)
from math import pi
print(pi)  # Outputs: 3.141592653589793

# 3. Import with an alias (Renames the module to shorten your code)
import random as rd
print(rd.randint(1, 10))

# 4. Import everything (Not recommended due to potential name clashes)
from math import *

#Creating Your Own Custom ModuleCreating a module is as simple as creating any basic Python script.

#1.Write the module file and name it
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

location = "Global Workspace"
#2.Import your module inside another script (e.g., main.py) located in the exact same directory:
# main.py
import mymodule
print(mymodule.greet("Alice"))  # Outputs: Hello, Alice!
print(mymodule.location)        # Outputs: Global Workspace

'''
Helpful Diagnostic Functions
  dir(): Returns a sorted list of all valid attributes and functions defined within an imported module.
  help('modules'): Type this inside your interactive Python shell to see an entire index of every module currently available on your local system.
'''

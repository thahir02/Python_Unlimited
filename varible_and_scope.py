'''
Varible in Python and there Scope :
In Python, variables are containers or symbolic labels that point to data values stored in memory
Variable scope determines where in your code a variable can be accessed or modified.
Python resolves variable names using the LEGB rule, which stands for Local, Enclosing, Global, and Built-in scopes.
The Four Scopes Explained
1. Local ScopeVariables created inside a function belong to that function's local scope. 
They only exist while the function is executing and cannot be accessed from outside.pythondef my_func(): '''
    x = 10  # Local variable
    print(x)

my_func()
# print(x)  # NameError: name 'x' is not defined

'''
2. Enclosing (Non-local) ScopeThis occurs in nested functions. 
The inner function can read variables defined in the outer (enclosing) function.pythondef outer_func(): '''
    x = "outer"

    def inner_func():
        print(x)  # Accesses x from the enclosing scope

    inner_func()
'''
3. Global ScopeVariables defined at the main, top-level of your Python script are global. 
They are accessible from anywhere in your file, including inside functions.pythonx = "global"  ''' 
# Global variable
def print_x():
    print(x)  # Reads the global x

print_x()
'''

4. Built-in ScopeThis is the widest scope. 
It contains Python’s built-in functions and exceptions that are always available without importing anything (e.g., len(), range(), str()). '''

'''
Recursive Function
A recursive function in Python is a function that calls itself to solve smaller instances of the same problem.
Every valid recursive function must have two main components to avoid infinite execution:
  Base Case: The condition under which the function stops calling itself and returns a direct value.
  Recursive Case: The part where the function breaks the problem down and calls itself with a new, smaller argument.
Standard Syntax and Visual ExampleThe most classic illustration of recursion is calculating a factorial (n!):
'''
def factorial(n):
    # 1. Base Case: stops the recursion
    if n == 1 or n == 0:
        return 1
    
    # 2. Recursive Case: function calls itself
    else:
        return n * factorial(n - 1)

print(factorial(4))  # Output: 24
'''
How the Call Stack WorksWhen factorial(4) executes, Python pushes each uncompleted function call onto an internal storage layer called the call stack:
factorial(4) -> waits for factorial(3)
  factorial(3) -> waits for factorial(2)
    factorial(2) -> waits for factorial(1)
      factorial(1) -> returns 1 (Base Case reached!)
'''

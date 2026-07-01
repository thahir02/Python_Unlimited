'''
In Python, there is no built-in "main" function required by the language interpreter.
Instead, Python executes script files sequentially from top to bottom. 
You use the main pattern in a Python module to control code execution.
Without this pattern, any code written outside of a function runs automatically the exact moment you import the module into another file.
The if __name__ == "__main__": guard ensures code only runs when you execute the file directly, not when you import it.
'''
# calculator.py

def add(a, b):
    """A reusable function to add two numbers."""
    return a + b

def main():
    """A test block that only runs during direct execution."""
    print("--- Running Calculator Module Directly ---")
    result = add(5, 3)
    print(f"Test Result (5 + 3): {result}")

# The guard condition
if __name__ == "__main__":
    main()
'''
Why This Matters (The Two Scenarios)
Scenario 1: Running the file directlyIf you run calculator.py in your terminal, Python sets __name__ to "__main__".
'''
#python calculator.py
#--- Running Calculator Module Directly ---
#Test Result (5 + 3): 8

'''
Scenario 2: Importing the file as a moduleIf you create a second file called app.py and import your calculator, Python sets __name__ inside calculator.py to "calculator".
The main() function is safely skipped, allowing you to use add() without triggering the test print statements.
'''

# app.py
import calculator

# You can use the function cleanly
total = calculator.add(10, 20)
print(f"Total in App: {total}")
$ python app.py
#Total in App: 30

'''
Core Reasons to Use This Pattern
Prevents Unwanted Output: It blocks test code, demo scripts, or scratchpad logic from running during an import.
Enables Module Reusability: It lets a single file serve a dual purpose: a runnable standalone script and an importable library.
Simplifies Debugging: You can leave functional test cases inside the main() block of your module to quickly verify changes later.

'''

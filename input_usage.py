'''
The input() function in Python can only collect user input during program execution. 
It cannot freeze time or accept data before the code starts running.
However, you can achieve the goal of providing data before execution by using alternative methods like command-line arguments or environment variables.

Scenario 1: During Program Execution (input())
  The input() function pauses your running program and waits for the user to type something into the terminal and press Enter.
'''
# The program starts, then pauses at this line
user_name = input("Enter your name: ")

# The program resumes after the user presses Enter
print(f"Hello, {user_name}!")

'''
Best for: Interactive scripts, forms, text games, or prompting users for confirmation midway through a task.

Scenario 2: 
  Before Program Execution (Alternatives)To feed data into your program before it actually starts executing, you must use tools that Python reads at launch.
  Method A: Command-Line Arguments (Recommended)You pass data into the terminal command itself when launching the script.
  Python reads this immediately using the sys.argv list.
'''
import sys

def main():
    # sys.argv[0] is always the script name itself
    # sys.argv[1] is the first argument passed
    if len(sys.argv) > 1:
        user_name = sys.argv[1]
    else:
        user_name = "Guest"

    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()
'''
Method B: 
  Environment VariablesYou set a variable in your operating system terminal right before running the script. Python reads it using the os module.
'''
import os

# Fetches the variable, or defaults to "Guest" if missing
user_name = os.getenv("USER_NAME", "Guest")

print(f"Hello, {user_name}!")


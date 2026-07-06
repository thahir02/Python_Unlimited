'''
Control Statement 
Control statements in Python are fundamental structural elements that alter the sequential execution flow of a program. 
This are also called as Conditional Statements (Selection), Iterative Statements (Loops), and Transfer Statements (Jumping).

1. Conditional Statements (Selection)These structures test logic via boolean expressions, executing specific code blocks only if conditions are met.
  if: Executes code only when a condition evaluates to True.
  else: Provides an alternate block if the preceding if condition evaluates to False.
  elif: Short for "else if"; tests sequential conditions without requiring deep indentation.
  match-case: Introduced in Python 3.10; offers pattern matching structural checks similar to switch-case statements in other programming languages.

Example of if-elif-else  '''
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")
'''
2. Iterative Statements (Loops)Loops let you repeat code blocks continuously based on designated bounds or evaluation limits.
  for: Iterates through elements of a sequence like lists, tuples, or strings.
  while: Continues execution indefinitely as long as its target condition evaluates to True. '''

# Example of a for loop
for i in range(3):
    print(f"Iteration {i}")
'''
3. Transfer Statements (Jumping)Transfer statements intercept structural repetition inside loops to modify processing patterns dynamically.
  break: Terminates the loop structure immediately, moving program execution to the next external code block.
  continue: Skips the remaining lines of code inside the current iteration and jumps directly to the next loop evaluation.
  pass: A null operator used purely as a placeholder when syntactic constraints require a statement block, but no execution logic is wanted yet. '''

# Example using break and continue
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num > 5:
        break  # Exit loop completely once number exceeds 5
    print(num)  # Outputs: 1, 3, 5

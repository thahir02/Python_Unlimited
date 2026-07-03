'''
The print() function in Python is a built-in function used to send data to the standard output device. 
It converts objects into text format before displaying them.
Syntax :
  print(object(s), sep=' ', end='\n', file=sys.stdout, flush=False)
Arguments :
  1.object(s): One or more values (strings, numbers, lists) to print, separated by commas.
  2.sep: The string inserted between multiple objects (defaults to a single space ' ').
  3.end: What gets printed at the very end of the line (defaults to a newline character '\n').
  4.file: An object with a write method, allowing you to redirect output to a file instead of the screen.
  5.flush: A boolean that forces Python to flush the output stream immediately when set to True.

Common Usage Examples '''
  #1.Basic String Output
      print("Hello, World!")  # Output: Hello, World!
  #2.Printing Multiple Items
      print("Python", 3.14, True)  # Output: Python 3.14 True
  #3.Customizing the Separator (sep)
      print("apple", "banana", "cherry", sep=", ")  # Output: apple, banana, cherry
  #4.Preventing a Newline (end)
      print("Hello", end=" ")
      print("World")  # Output: Hello World (on the same line)
  #5.Writing Direct to a File
      with open("output.txt", "w") as f:
      print("Save this text.", file=f)

#String Formatting with Print
  #For advanced variables output, you can use Python Documentation on F-strings:
      name = "Alice"
      print(f"Hello, {name}!")  # Output: Hello, Alice!



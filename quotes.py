'''
In Python, quotation marks are used to define string literals (text data).

Types of QuotesSingle Quotes (' '): Used for short, 
  single-line strings or identifier-like text.
  Double Quotes (" "): Functionally identical to single quotes, but preferred for text that naturally contains apostrophes.
  Triple Quotes (''' ''' or """ """): Used for multi-line blocks of text, preservation of formatting, and documentation.

Functional Comparison and Syntax Rules1. 
1.Single vs. Double Quotes (Single-Line Strings)There is no functional or performance difference between single and double quotes in Python. 
  Both must start and end on the same line. However, you can use them strategically to avoid syntax errors when nesting quotation marks:To include a single quote, wrap the string in double quotes:
  Ex :-  '''
    message = "Python's syntax is highly intuitive."
 #To include a double quote, wrap the string in single quotes:
  #Ex:-
    speech = 'He shouted, "Hello World!"'
  #If you use the same quote type externally and internally, Python throws a SyntaxError unless you escape it.
  #You can use a backslash (\) as an escape character to resolve this:
  #Ex:-
    # Escaping tells Python to treat the inner quote as plain text, not code
    error_fix = 'It\'s an excellent day to code.'
'''
2.Triple Quotes (Multi-Line and Documentation)Triple quotes allow strings to safely span across multiple lines without requiring the newline character (\n). 
  They also allow you to mix both single and double quotes freely inside without using escape backslashes.Multi-line Strings:
  Ex:-  '''
    poem = """Roses are red,
    Violets are blue,
    Python is clean,
    And easy to view."""
  #Use code with caution.Docstrings (Documentation Strings): When placed immediately at the beginning of a module, class, or function, triple double-quotes function as a docstring to document your code's purpose.
    pythondef calculate_area(radius):
    """Calculates and returns the area of a circle."""
    return 3.14159 * (radius ** 2)

# Python Functions: Modularity & Reusability

Functions are used to achieve **modularity** and **reusability** in code.
* **Modularity:** Breakdown of large code into small modules.
* **Reusability:** Code is reusable.

## Types of Functions
1. **User-defined functions:** Functions created by the programmer.
2. **Built-in functions:** Functions that are predefined in Python.
3. **Lambda functions:** Anonymous, single-line functions.
4. **Recursive functions:** Functions that call themselves.

## User-defined Functions

### Syntax
```python
def name(parameters):
    # Body of the function
    # ...
    return value
```
# Example 
def cal(ch, a, b):
    match ch:
        case '+':
            print(a,'+',b,'=',a + b)
        case '-':
            print(a,'-',b,'=',a - b)
        case '*':
            print(a,'*',b,'=',a * b)
        case '/':
            print(a,'/',b,'=',a / b)
        case _:
            print("Invalid choice")
    return ch
print('Enter 1st num')
a=int(input())
print('Enter 2nd number')
b=int(input())
print('Enter ur choice :')
ch = input()
cal(ch, a, b)

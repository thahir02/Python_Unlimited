## Types of User-Defined Functions

User-defined functions are classified into four types based on arguments (inputs) and return values (outputs):

### 1. Function with No Arguments and No Return Value
This type performs a static action and does not communicate data back to the caller.
```python
def greet():
    print("Hello, welcome to Python!")

# Call
greet()
```

### 2. Function with Arguments but No Return Value
This type accepts dynamic inputs to change its behavior but does not pass data back.
```python
def greet_user(name):
    print(f"Hello, {name}!")

# Call
greet_user("Alice")
```

### 3. Function with No Arguments but Returns a Value
This type generates or fetches data internally and passes it back to the caller.
```python
def get_pi_value():
    return 3.14159

# Call
radius = 5
area = get_pi_value() * (radius ** 2)
```

### 4. Function with Arguments and Returns a Value
The most common type. It takes inputs, processes them, and sends the result back.
```python
def add_numbers(a, b):
    return a + b

# Call
result = add_numbers(10, 20)
print(result)  # Outputs: 30
```
# TYPE 1: No arguments and No return value
# Everything happens entirely inside the function.
def type_one():
    x = 10
    y = 20
    print("Type 1 Result:", x + y)

type_one()
# print(x)  <-- Error! x only exists inside type_one


# TYPE 2: With arguments but No return value
# Inputs are sent in, but nothing comes back out.
def type_two(a, b):
    ans = a - b
    print("Type 2 Result:", a, "-", b, "=", ans)

type_two(50, 20)


# TYPE 3: No arguments but Returns a value
# No inputs are given, but it sends data out using 'return'.
def type_three():
    msg = "Hello from Type 3!"
    return msg

# We must catch the returned value in a variable to use it outside
result_three = type_three()
print(result_three)


# TYPE 4: With arguments and Returns a value
# Inputs are sent in, processed, and the final answer is sent back out.
def type_four(num1, num2):
    total = num1 * num2
    return total

# Catching the output in a variable
result_four = type_four(5, 6)
print("Type 4 Result:", result_four)

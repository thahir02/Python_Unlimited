# Define a function that takes an argument 'x'
def fun(x):
    # Return an anonymous (lambda) function that takes 'n' and multiplies it by 'x'
    # This creates a closure that "remembers" the value of 'x' even after fun() finishes executing
    return lambda n: n * x

# Prompt the user to enter a number
print('enter a number:')

# Read the user's input, convert it to an integer, and store it in 'num'
num = int(input())

# Call fun(num) and store the returned lambda function in the variable 'math_table'
# At this point, 'x' inside the lambda is permanently set to the user's number
math_table = fun(num)

# Loop 'i' through numbers 1 to 10 (inclusive) to generate the table rows
for i in range(1, 11):
    # math_table(i) passes 'i' into the lambda function (where 'n' = i)
    # The lambda function multiplies 'n' (i.e., i) by the remembered 'x' (i.e., num)
    # Print the equation and result in a formatted string style
    print(num, '*', i, '=', math_table(i))

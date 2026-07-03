# Define a list of integers from 1 to 10
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Define a function that returns the cube of a number
def fun(x):
    return x**3


# Apply the function to every item in the list
res = list(map(fun, lst))

# Print the original list and the result list on separate lines
print(lst, res, sep="\n")

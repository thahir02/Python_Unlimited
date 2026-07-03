# Define a list of integers
lst = [9, 4, 6, 8, 5, 2, 7]

# Create a lambda function to check for even numbers
even_num = lambda x: x % 2 == 0

# Filter the list and print the even numbers
print(list(filter(even_num, lst)))

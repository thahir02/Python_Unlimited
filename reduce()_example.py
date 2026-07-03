from functools import reduce

# Input list of integers
lst = [9, 1, 5]

# Lambda function that takes two arguments and returns their sum
even_num = lambda x, y: x + y

# reduce() applies even_num cumulatively to the items in lst
# Step 1: x = 9, y = 1 -> returns 9 + 1 = 10
# Step 2: x = 10 (previous result), y = 5 -> returns 10 + 5 = 15
print(reduce(even_num, lst))  # Outputs: 15



# or

from functools import reduce
lst=[9,1,5]
print(reduce(lambda x,y : x+y,lst))

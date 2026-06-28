'''
An argument in Python is the actual value passed to a function when it is called. It fills in the function's placeholders (parameters) with real data
In Python, there are 5 types of arguments you can use when calling functions
The 5 Types of Arguments
  1. Positional Arguments : Arguments passed to a function in the exact order they are defined.Position matters.If you swap the inputs, the data goes into the wrong variables.
  2. Keyword Arguments : Arguments passed by explicitly naming the parameter and assigning its value using an equals (=) sign.Order does not matter.Makes code highly readable.
  3. Default Arguments(also called as optional argumnts) : Parameters that have a pre-assigned backup value in the function definition.If you do not provide a value when calling the function, Python automatically uses this default value.
  4. Arbitrary Positional Arguments (*args) (also called as varible length argument) : Used when you do not know how many positional inputs a user will pass.Python collects all extra un-named inputs into a single tuple.Indicated by a single asterisk *.
  5. Arbitrary Keyword Arguments (**kwargs) (also called as variable length keyword argument) : Used when you do not know how many named inputs a user will pass.Python collects all extra named inputs into a single dictionary.Indicated by a double asterisk **.
some examples of each different type of argument
'''

# =====================================================================
# FUNCTION DEFINITIONS
# =====================================================================

# 1 & 2. Function used to show Positional and Keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# 3. Function with a Default Argument (country defaults to 'India')
def display_location(city, country="India"):
    print(f"City: {city}, Country: {country}")

# 4. Function using Arbitrary Positional Arguments (*args)
def sum_all_numbers(*args):
    total = sum(args)
    print(f"The sum of the numbers {args} is: {total}")

# 5. Function using Arbitrary Keyword Arguments (**kwargs)
def print_user_profile(**kwargs):
    print("\n--- User Profile Details ---")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# =====================================================================
# FUNCTION CALL EXAMPLES WITH EXPECTED OUTPUTS
# =====================================================================

print("--- 1. Positional Arguments (Order Matters) ---")
describe_pet("Dog", "Rex") 
# OUTPUT: I have a Dog named Rex.


print("\n--- 2. Keyword Arguments (Order Does Not Matter) ---")
describe_pet(pet_name="Whiskers", animal_type="Cat")
# OUTPUT: I have a Cat named Whiskers.


print("\n--- 3. Default Arguments (Optional inputs) ---")
# Case A: Missing the second argument -> uses default "India"
display_location("Mumbai")
# OUTPUT: City: Mumbai, Country: India

# Case B: Providing the second argument -> overrides the default
display_location("Tokyo", "Japan")
# OUTPUT: City: Tokyo, Country: Japan


print("\n--- 4. Arbitrary Positional Arguments (*args) ---")
sum_all_numbers(5, 12)
# OUTPUT: The sum of the numbers (5, 12) is: 17

sum_all_numbers(10, 20, 30, 40)
# OUTPUT: The sum of the numbers (10, 20, 30, 40) is: 100


print("\n--- 5. Arbitrary Keyword Arguments (**kwargs) ---")
print_user_profile(username="dev99", role="Admin")
# OUTPUT: 
# --- User Profile Details ---
# Username: dev99
# Role: Admin

print_user_profile(name="Amit", age=25, city="Delhi")
# OUTPUT: 
# --- User Profile Details ---
# Name: Amit
# Age: 25
# City: Delhi

# Number conversion into binary,octal,hexdecimal
# We can convert manually of using string formatting.In string formatting they are two types of conversion - 1.str.format() 2.f-string

# 1.str.format() it 2.7 version of python is slow than f-string
# Coversions using str.format()
s = int(input('Enter a number: '))
print('Choose which conversion to perform:\n "b" for binary\n "o" for octal\n "x" for hexadecimal')
ch = input("Enter your choice: ")

match ch:
    case "b":
        print("{0:b}".format(s))
    case "o":
        print("{0:o}".format(s))
    case "x":
        print("{0:x}".format(s))
    case _:
        print("This is invalid.")

#-------------------------------------------------or----------------------------------------------------------#

# 2.f-string it is 3.6 version of python it is latest version it is faster than format()
# Conversions using f-string
s = int(input('Enter a number: '))
print('Choose which conversion to perform:\n "b" for binary\n "o" for octal\n "x" for hexadecimal')
ch = input("Enter your choice: ")

match ch:
    case "b":
        print(f"{s:b}")
    case "o":
        print(f"{s:o}")
    case "x":
        print(f"{s:x}")
    case _:
        print("This is invalid.")

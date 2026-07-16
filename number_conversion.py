# Number conversion into binary,octal,hexdecimal
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

import re 
# module re(regular expression) is used to check in pattern matching
s=input("Enter the String : ")
check=input("Enter the String to Check : ")
choice=input("Enter your choice either match or search : ")
match choice:
    case 'match':
        mat=re.match(check,s)
        # Check if a match was actually found to avoid crashes
        if mat:
            print(f"Match found at:{mat.span()}")
        else:
             print("No match found at the beginning of the string.")
    case 'search':
        sea=re.search(check,s)
        # Check if a match was actually found to avoid crashes
        if sea:
            print(f"Match found at:{sea.span()}")
        else :
             print("No match found anywhere in the string.")
    case _:
        print("Invalid")

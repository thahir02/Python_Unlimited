#The example program for string translation
str=input("Enter the string : ")
table=str.maketrans('aeiou','12345','0123456789')
s_table=str.translate(table)
print(s_table)

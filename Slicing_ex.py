#write a program to reverse the input string and remove first and last characters from the reversed string

str1=input('Enter a string : ')
print(str1[::-1])
print(str1[len(str1)-2:0:-1])

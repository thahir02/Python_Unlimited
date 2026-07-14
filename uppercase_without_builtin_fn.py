# Conversion of input string into uppercase without using buitin function
str1=input('Enter a String : ')
str_upper=''
for i in str1:
    if ord(i)>=97 and ord(i)<=122:
        str_upper += chr(ord(i)-32)
    else:
        str_upper += i
print(str_upper)

#Program how many different type of string are there
str1=input('Enter a string : ')
up_count,low_count,num_count,sp_count=0,0,0,0
for i in str1:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    elif i.isnumeric():
        num_count += 1
    else:
        sp_count += 1
print('uppercase count=',up_count)
print('lowercase count=',low_count)
print('numericcase count=',num_count)
print('specialcase count=',sp_count)

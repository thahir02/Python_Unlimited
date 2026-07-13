str1=input('Enter the string:')
num=int(input('enter how many substring should done for given string:'))
if len(str1)<=num-1:
        print('Not Possible')
else:
    for i in range(0, len(str1) - 2):
        print(str1[i:i+3])

------------------------------------ OR -----------------------------------------

str1=input('Enter the string:')
num=int(input('enter how many substring should done for given string:'))
if len(str1)<=num-1:
        print('Not Possible')
else:
    p1=0
    p2=num 
    while(p2<=len(str1)):
        print(str1[p1:p2])
        p1+=1
        p2+=1

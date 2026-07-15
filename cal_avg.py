#program to calculate the average of taken input numbers as a string

from functools import reduce
nums=input('Enter the nums : \n') .split()
lst=list(map(int,nums))
res=reduce(lambda x,y:x+y,lst)
avg=res/len(lst)
print("{0:.4f}".format(avg))

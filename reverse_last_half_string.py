#Program to reverse the last half string 
'''
example
s=python
output : pytnoh
'''

s=input('enter the string')
s2=s[:len(s)//2:] +s[len(s)-1:(len(s)//2)-1:-1]
print(s2)

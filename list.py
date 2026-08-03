'''
List :-
  In Python, a List is a built-in, mutable, and ordered dynamic array that stores a collection of items. It is the most widely used data structure in the language due to its flexibility and built-in optimization.

1. Core Characteristics of a Python List
  Ordered: Elements maintain their specific insertion sequence. Indexing starts at 0.
  Mutable: You can add, remove, change, or reorder items after creation without changing the identity of the list.
  Heterogeneous: A single list can hold mixed data types simultaneously (integers, strings, floats, dicts, or other lists).
  Referential: It acts as a referential array, meaning it stores memory pointers to objects rather than storing the raw data values directly.
'''
#List 
lst =[10,[100,90],(1,6,7),{5,7,4},{'Name':"Thahir",'age':22}]
print(lst)
print(lst[0])
print(lst[1][0])
print(lst[2][0])
print(lst[4])
'''OUTPUT :
[10, [100, 90], (1, 6, 7), {4, 5, 7}, {'Name': 'Thahir', 'age': 22}]
10
100
1
{'Name': 'Thahir', 'age': 22}
'''
#Concatenation
lst1=[10,20,30]
lst2=[100,200,300]
print(lst1+lst2)
''' OUTPUT :
[10, 20, 30, 100, 200, 300]
'''
#Replication
lst=[0]*3
print(lst)
''' OUTPUT :
[0, 0, 0]
'''
#Accessing elements 
#Using index
lst=[1,2,3,4,5,6,7,8,9,0]
print(lst[0])
print(lst[1])
#using Silicing
print(lst[:])
print(lst[-1:-6:-1])
''' OUTPUT :
1
2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
[0, 9, 8, 7, 6]
'''
#list working with loop 
for i in lst:
    print(i,end = ' ')
print()
for i in range(0,len(lst)):
    print(lst[i],end = ' ')
''' OUTPUT :
1 2 3 4 5 6 7 8 9 0 
1 2 3 4 5 6 7 8 9 0 
'''

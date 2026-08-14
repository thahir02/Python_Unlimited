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
# Mutability of list -> add,modify,remove
lst=[]
for i in range(1,11):
    lst.append(i)
print(lst)
#using append()
print('using append()',end=" : ") 
lst.append(56)
print(lst)
#To add multiple elements once there are two ways 
#1.Using Concatenation which is old and slow 
print('using Concatenation',end=" : ")
lst = lst + [90,60,87]
print(lst)
#2.Using extend which is fast and easy 
print('using extend',end=" : ")
lst.extend([40,50,68])
print(lst)
#To insert elements whereever needed 
print('using insert',end=" : ")
lst.insert(1,23)
print(lst)
#To change the value of existing element
print("change the value of existing element" ,end=" : ")
lst[0]=2
print(lst)
#Multiple elements replaced with single element
print("Multiple elements replaced with single element" ,end=" : ")
lst[11:]=[11]
print(lst)
#Alternating replacing elements
print("Alternating replacing elements",end=" : ")
lst[0::2]=[2]*6
print(lst)
#remove any specific elements 
print("remove any specific elements",end=" : ")
lst.remove(5)
print(lst)
'''
Output :
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
using append() : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56]
using Concatenation : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56, 90, 60, 87]
using extend : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56, 90, 60, 87, 40, 50, 68]
using insert : [1, 23, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56, 90, 60, 87, 40, 50, 68]
change the value of existing element : [2, 23, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56, 90, 60, 87, 40, 50, 68]
Multiple elements replaced with single element : [2, 23, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Alternating replacing elements : [2, 23, 2, 3, 2, 5, 2, 7, 2, 9, 2, 11]
remove any specific elements : [2, 23, 2, 3, 2, 2, 7, 2, 9, 2, 11]
'''
# pop() and del in list
#Using pop()
lst=[1,3,5,7,9,8,11,12]
print(lst)
#default pop the last element
print("default pop the last element",end=" : ")
lst.pop()
print(lst)
#pop using index value
print("pop using index value",end=" : ")
lst.pop(5)
print(lst)
#Using del()
lst=[5,4,3,2,1,5,9,2]
print(lst)
# del() use to delete a single element
print("del() use to delete a single element",end=" : ")
del lst[1]
print(lst)
# del() use to delete a slice of elements
print("del() use to delete a slice of elements",end=" : ")
del lst[2:5]
print(lst)
lst=[1,2,3,4,5,6,7]
print(lst)
# del() use to delete the alternate elements
print("del() use to delete the alternate elements",end=" : ")
del lst[1::2]
print(lst)
'''
Output :-
[1, 3, 5, 7, 9, 8, 11, 12]
default pop the last element : [1, 3, 5, 7, 9, 8, 11]
pop using index value : [1, 3, 5, 7, 9, 11]
[5, 4, 3, 2, 1, 5, 9, 2]
del() use to delete a single element : [5, 3, 2, 1, 5, 9, 2]
del() use to delete a slice of elements : [5, 3, 9, 2]
[1, 2, 3, 4, 5, 6, 7]
del() use to delete the alternate elements : [1, 3, 5, 7]
'''

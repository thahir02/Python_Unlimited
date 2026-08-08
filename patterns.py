# Pattern 1
n=int(input("Enter the Size : "))
for i in range(0,n):
    for j in range(0,n):
        print('*',end=" ")
    print()
'''
Output :-
Enter the Size :  5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
# Pattern 2
n=int(input("Enter the Size : "))
for i in range(0,n):
    for j in range(0,n):
        print(i+1,end=" ")
    print()
'''
Output :-
Enter the Size :  5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
# Pattern 3
n=int(input("Enter the Size : "))
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ")
    print()
'''
Output :-
Enter the Size :  5
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
# Pattern 4
n=int(input("Enter the Size : "))
for i in range(0,n):
    for j in range(0,n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output :-
Enter the Size :  5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
# Pattern 5
n=int(input("Enter the Size : "))
count=1
for i in range(0,n):
    for j in range(0,n):
        if(count<10):
            print(0,end="")
        print(count,end=" ")
        count += 1
    print()
'''
Output :-
Enter the Size :  5
01 02 03 04 05 
06 07 08 09 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
'''
# pattern 6
n=int(input("Enter the size : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i*j<10):
            print(0,end="")
        print(i*j,end=" ")
    print()
'''
Output :-
Enter the size :  5
01 02 03 04 05 
02 04 06 08 10 
03 06 09 12 15 
04 08 12 16 20 
05 10 15 20 25 
'''
# Pattern 7
n=int(input("Enter the size : "))
count=0
for i in range(0,n):
    count=i+1
    for j in range(0,n):
        if count<10:
            print(0,end="")
        print(count,end=" ")
        count+=1
    print()
'''
Output :-
Enter the size :  5
01 02 03 04 05 
02 03 04 05 06 
03 04 05 06 07 
04 05 06 07 08 
05 06 07 08 09 
'''
# Pattern 8
n=int(input("Enter the size :"))
for i in range(0,n):
    for j in range(0,n):
        if i>=j:
            print("*",end=" ")
    print()
'''
Output :-
Enter the size : 5
* 
* * 
* * * 
* * * * 
* * * * * 
'''
# Pattern 9
n=int(input("Enter the size : "))
for i in range(0,n):
    for j in range(0,n):
        if i>=j :
            print(j+1,end=" ")
    print()
'''
Output :-
Enter the size :  5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
# Pattern 10
n=int(input("Enter the size : "))
for i in range(0,n):
    for j in range(0,n):
        if i>=j :
            print(f"{i+1:02d}", end=" ")
    print()
'''
Output :-
Enter the size :  5
01 
02 02 
03 03 03 
04 04 04 04 
05 05 05 05 05 
'''
# Pattern 11
n=int(input("Enter the size : "))
for i in range(0,n):
    for j in range(0,n):
        if j+i+1 >= n:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
#---------------- or ---------------#
'''
# Pattern 11
n=int(input("Enter the size : "))
for i in range(0,n):
    for k in range(0,(n-1)-i):
        print(" ",end = " ")
    for j in range(0,n):
        if(j<=i):
            print("*",end = " ")
    print()
    
Output :-
Enter the size :  5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
# Pattern 12 
n=int(input("Enter the size : "))
for i in range(0,n):
    for k in range(0,(n-1)-i):
        print(" ",end="")
    for j in range(0,n):
        if(j<=i):
            print("* ",end="")
    print()
#--------- or -------------#
'''
n=int(input("Enter the size : "))
for i in range(0,n):
    for j in range(0,n):
        if j+i+1 >= n:
            print("* ", end="")
        else:
            print(" ",end="")
    print()

Output :-
Enter the size :  5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
# Pattern 13 
n=int(input("Enter the size : "))
for i in range(0,n):
    for k in range(0,(n-1)-i):
        print(" ",end="")
    for j in range(0,n):
        if j==0 or j==i or i==n-1 :
            print("* ",end="")
        else :
            print("  ",end="")
    print()
'''
Output :-
Enter the size :  5
    *         
   * *       
  *   *     
 *     *   
* * * * * 
'''
# Pattern 14 
n=int(input("Enter the size : "))
for i in range(0,n):
    for k in range(0,(n-1)-i):
        print(" ",end="")
    for j in range(0,n):
        if j==0 or j==i or i==n-1 :
            print(j+1,end=" ")
        else :
            print(" ",end=" ")
    print()
'''
Output :-
Enter the size :  5
    1         
   1 2       
  1   3     
 1     4   
1 2 3 4 5 
'''

n=int(input())
odd_sum,even_sum=0,0
for i in range(1,n+1):
    if i%2==0:
        even_sum +=i
    else :
        odd_sum +=i

print('odd_sum = ',odd_sum)
print('even_sum =',even_sum)

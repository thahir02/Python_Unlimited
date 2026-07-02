n=int(input())
odd_sum,even_sum=0,0
for i in range(1,n+1):
    if i%2==0:
        even_sum +=i
    else :
        odd_sum +=i

print('odd_sum = ',odd_sum)
print('even_sum =',even_sum)

# The above same program can be written using contiue instead of else block i.e ;

n=int(input())
odd_sum,even_sum=0,0
for i in range(1,n+1):
    if i%2==0:
        even_sum +=i
        continue
    odd_sum +=i

print('odd_sum = ',odd_sum)
print('even_sum =',even_sum)

# 1. Accept user input, convert it to an integer, and store it in 'n'
n = int(input())

# 2. Loop through numbers starting from 2 up to and including 'n'
for i in range(2, n + 1):
    # 3. Check if 'n' is perfectly divisible by the current loop number 'i'
    if n % i == 0:
        # 4. Stop the loop early if a divisor (factor) is found
        break

# 5. If the loop finished only when 'i' reached 'n', it means 'n' is a prime number
if i == n:
    print(n, 'prime')
# 6. If the loop stopped early (i < n), it means 'n' has another factor and is not prime
else:
    print(n, 'not prime')

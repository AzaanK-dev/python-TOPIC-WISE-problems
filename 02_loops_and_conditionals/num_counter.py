# For a given integer N, count how many numbers from 1 to N:
# Are prime.
# Have an even sum of digits.
# Do not contain the divisible of 5.

n = 20
count = 0
check = True

for i in range(2,n+1):   # 1 is not a prime number, so we start from 2
    print(i, end=" ")
    check = True
    if i%5==0:
        continue

    for j in range(2,i): 
        if i%j==0 and not i==j:
            check = False
            break

    sum = 0
    x = i
    while x>0:
        r = x%10
        sum += r
        x //= 10
    if not sum%2==0:
        check = False
        
    if check:
        count += 1 

print("Count of prime numbers:", count)
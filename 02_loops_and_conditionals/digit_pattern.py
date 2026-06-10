# A number is special if:
# Digits alternate between odd and even.
# No digit ieats.
# Sum of digits is divisible by 7.

n = 3416
x = n
curr = prev = i = sum = 0
s = str(n)
valid = False

while(x>0):
    i += 1   # each iteration
    curr = x%10
    sum += curr
    if s.count(str(curr)) > 1:   # digit does not repeat (more than 1)
        valid = False
        break

    if i>1 and curr%2==prev%2:  # if curr & rev are same
        valid = False
        break
    else:   
        valid = True

    prev = curr    # stores prev digit
    x //= 10

if sum % 7 == 0 and valid:
    print("YES, this is special no.")
else: 
    print("NO, this is NOT special no.")


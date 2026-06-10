# A number is called a mirror number if:
# Reversing its digits produces a different number.
# Sum of original and reversed numbers is divisible by 11.

num = 12
i = num
rev = ""
while i > 0:
    r = i%10
    i //= 10
    rev += str(r)

if not num == int(rev) and (num + int(rev)) % 11 == 0:
    print("Mirror Numbers")
else:
    print("NOT Mirror Numbers")
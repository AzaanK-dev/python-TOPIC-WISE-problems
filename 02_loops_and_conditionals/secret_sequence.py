# Print only numbers satisfying all conditions:
# Divisible by 3 or 5.
# not divisible by both.
# Sum of digits is prime.
# Contains no repeated digit.


n = 100
result = []
count = 0

for i in range(1, n):

    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):

        temp = i
        digit_sum = 0

        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        if digit_sum > 1:
            is_prime = True
            for j in range(2, digit_sum):
                if digit_sum % j == 0:
                    is_prime = False
                    break
        else:
            is_prime = False

        num = str(i)
        freq = {}

        for ch in num:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        has_repeat = False
        for v in freq.values():
            if v > 1:
                has_repeat = True
                break

        if is_prime and not has_repeat:
            print(i)
            result.append(i)
            count += 1

print(count)
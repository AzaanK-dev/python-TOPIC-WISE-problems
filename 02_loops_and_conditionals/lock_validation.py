# A security lock accepts a number only if:
# It contains exactly 6 digits.
# Digits are in non-decreasing order from left to right.
# At least one digit appears exactly twice.
# No digit appears more than 3 times.


lock = "256679"
valid = False

if len(lock)==6:
    for i in range(len(lock)-1):  # to treat as 'lock[i]' not just 'i'
        if lock[i+1] < lock[i]:
            valid=True
    
    freq = [lock.count(d) for d in set(lock)]  # store frequency in list of each unique (set) char
    # freq = [1, 1, 2, 1, 1]  i.e 2->6

    if 2 in freq and valid and max(freq) <= 3:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
        

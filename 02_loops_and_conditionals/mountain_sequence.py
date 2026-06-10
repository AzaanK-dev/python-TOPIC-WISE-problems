# Given a sequence of numbers, determine whether it forms a valid mountain:
# Numbers must strictly increase.
# Then strictly decrease.
# Peak cannot be first or last element.
# Equal adjacent values are not allowed.


num = [1,3,5,4,6,2]
up = False
down = False
invalid = False

if num[0] < num[1]: 
    for i in range(len(num)-1):
        if not down and num[i] < num[i+1]: 
            up = True
        elif num[i] > num[i+1]: 
            down = True
        else: 
            invalid = True
            break

    if up and down and not invalid:
        print("YES, this is mountain sequence")
    else: 
        print("NO, this is NOT mountain sequence")
else: 
    print("NO, this is NOT mountain sequence")



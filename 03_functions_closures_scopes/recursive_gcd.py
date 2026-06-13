# Write a recursive function that:
# Performs a calculation.
# Tracks maximum recursion depth reached.
# Returns both result and depth information.
# No global variables allowed.


def gcd(n1,n2,depth):
    if n2==0:
        return n1,depth
    depth+=1
    return gcd(n2,n1%n2,depth)

res,dep = gcd(48,18,0)
print(res)
print(dep)
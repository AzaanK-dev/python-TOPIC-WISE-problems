# Given heights of blocks in a 1D landscape:
# Determine how many cells can hold water.
# Use loops and conditionals only.
# No built-in advanced libraries.


store = [3,0,2,0,4]
rmax = min_height = diff = sum = 0
lmax = store[0]

for i in range(len(store)):
    lmax = max(lmax,store[i])
    if i < len(store)-1:
        rmax = store[i+1]
        for j in range(i+1,len(store)):
            rmax = max(rmax,store[j])
    else:
        rmax = store[i]
    
    min_height = min(lmax,rmax)
    diff = min_height-store[i]
    if diff>=0:
        sum += diff 

print("Total water trapped:",sum)
    

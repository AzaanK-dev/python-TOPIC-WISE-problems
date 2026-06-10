# Given a sequence of daily temperatures:
# Find the longest consecutive streak where temperatures keep increasing.
# Print the starting index, ending index, and streak length.

temp = [5,4,3,2,1]
streak = 0
start = 0
end = 0
best_start = 0
best_end = 0
best = 0

for i in range(len(temp)-1):
    streak = 1
    start = i
    for j in range(i,len(temp)-1):
        if temp[j]<temp[j+1]:
            streak += 1
            end = j+1
        else: 
            break

    if best<streak:
        best_start = start
        best_end = end
        best = streak


print(best_start,best_end,best)
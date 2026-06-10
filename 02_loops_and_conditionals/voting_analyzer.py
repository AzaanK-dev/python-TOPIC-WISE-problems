# Given votes represented by integers:
# Ignore negative values.
# Stop processing if 999 appears.
# Count valid votes.
# Determine winner.
# Detect ties.


votes = [101,104,102,101,102,101,103,104,999,101,103,103]   # voter ids: 101,102,103 etc
valid = []
for v in votes:
    if v==999:
        break
    valid.append(v)

voter_ids = set(valid)
count = 0
res = {}

for i in voter_ids:
    if i<0:
        continue
    count = valid.count(i)
    res[i] = count

    print("Voter Id:",i,"; votes:",count)

max_votes = max(res.values())   # comparing all values only in key+value pair of res
winners = [k for k in res if res[k] == max_votes]   # finding key for that max value
print("Winners: ",winners)

if len(winners) > 1:
    print("Ties: ",winners)
else: 
    print("No Ties")





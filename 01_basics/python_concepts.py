# Create a function that receives a list and modify. Determine which changes affect the original objects and which do not.

# def swap_tracker(l1):
#     a1 = l1
#     a1.append(10)  # modifies original list also
#     print(l1,"\n",a1)
#     a2 = l1
#     a2 = [1,3,5]   # does not modify the original list. a2 points to a new list NOW
#     print(l1,"\n",a2)

# swap_tracker([2,4,6])

# ---------------------------------------------------------------------------------------
# Discover why old notes keep appearing unexpectedly.

# def collect_notes(note,notes=[]):      # default list
#     notes.append(note)
#     print(notes)

# collect_notes("maths")
# collect_notes("urdu")  
# collect_notes("english")    # still keeps old parameters

# ---------------------------------------------------------------------------------------
# Create a list containing nested lists. Make shallow and deep copies and observe which modifications propagate.

l1 = [1,[2,4],2,3,4]
l1_shallow = l1.copy()
print(l1_shallow)

import copy
l1_deep = copy.deepcopy(l1)
print(l1_deep)
# print("hello world!")

def my_func(n):
    print(n)
# my_func("hello")

# pizza = "pepperoni"
# qty = 4
# order = "{} slices of {} flavor"
# print(order.format(qty,pizza))  # output: 4 slices of pepperoni flavor

# x = 0.3
# y = 0.9
# print(x+x+x-y)  # -1.1102230246251565e-16

# from decimal import Decimal
# print(Decimal(0.3) + Decimal(0.3) + Decimal(0.3) - Decimal(0.9))   # -5.551115123130313080847263336E-17
# print(Decimal("0.3") + Decimal("0.3") + Decimal("0.3") - Decimal("0.9"))  # 0.0




#               LISTS (ARRAYS) IN PYTHON 

# pizza_flavours = ["pepperoni","max","spicy","tikka"]
# print(pizza_flavours[0])   # pepperoni
# print(pizza_flavours[-1])    # tikka
# print(pizza_flavours[1:3])    # ['max', 'spicy']
# print(pizza_flavours[2:])    # ['spicy', 'tikka']
# print(pizza_flavours[:2])    # ['pepperoni', 'max']

# print("".join(pizza_flavours))     # pepperonimaxspicy
# print(", ".join(pizza_flavours))

# pizza_flavours[2] = "creamy"
# print(pizza_flavours)  # ['pepperoni', 'max', 'creamy', 'tikka']

# print(pizza_flavours[1:2])  # ['max']
# pizza_flavours[1:2] = "mexican"
# print(pizza_flavours)  # ['pepperoni', 'm', 'e', 'x', 'i', 'c', 'a', 'n', 'creamy', 'tikka']

# pizza_flavours[1:2] = ["mexican"]
# print(pizza_flavours)  # ['pepperoni', 'mexican', 'creamy', 'tikka']

# if "tikka" in pizza_flavours:
    # print("We have tikka pizza")

# if "fajita" not in pizza_flavours:
    # print("We don't have fajita pizza")

# for i in pizza_flavours:
    # print(i,end="\n")

# pizza_flavours.append("fajita")
# if "fajita" in pizza_flavours:
    # print("NOW, We have added fajita pizza")

# pizza_flavours.pop()   # remove from last "tikka"
# print(pizza_flavours)   #  ['pepperoni', 'max', 'spicy'] 

# pizza_flavours.insert(2,"tikka")   # add "tikka" at 2
# print(pizza_flavours)   #  ['pepperoni', 'max', 'tikka', 'spicy']

# pizza_flavours.remove("max")
# print(pizza_flavours)   #  ['pepperoni', 'tikka', 'spicy']

# pizza_flavours_copy = pizza_flavours.copy()   # here seperate copy is created in memory for pizza_flavours_copy
# pizza_flavours_2 = pizza_flavours           # here same reference is pointed to both (pizza_flavours & pizza_flavours_2)

# squared_nums = [x**2 for x in range(10)]    # weird syntax in list
# print(squared_nums)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




#        DICTIONARIES (OBJECTS (BUT NOT HAVE OWN METHODS)) IN PYTHON

# pizza_order = {"size":"large", "flavor":"spicy", "qty":"4"}
# print(pizza_order)   
# print(pizza_order.__len__())  # 3

# print(pizza_order["flavor"])    # spicy
# pizza_order["flavor"] = "korean"
# print(pizza_order)       #  {'size': 'large', 'flavor': 'korean', 'qty': '4'}

# for key,value in pizza_order.items():
    # print(key,":",value)

# squared_nums = {x:x**2 for x in range(10)}
# print(squared_nums)

# pizza_flavours = ["pepperoni","max","spicy","tikka"]
# new_dict = dict.fromkeys(pizza_flavours,"medium")
# print(new_dict)  # {'pepperoni': 'medium', 'max': 'medium', 'spicy': 'medium', 'tikka': 'medium'}



#        TUPPLES (same as list, JUST IMMUTABLE DATA TYPE) IN PYTHON

pizza_flavours = ("pepperoni","max","spicy","tikka")
# pizza_flavours[1] = "creamy"    # TypeError: 'tuple' object does not support item assignment

trending = ("grilled","bbq","max")
all_flavours = pizza_flavours + trending
print(all_flavours)

print(all_flavours.count("max"))      # 2 (retuns frequency of item)


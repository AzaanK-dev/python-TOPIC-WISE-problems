# Create a function that receives a number and returns another function. That 
# returned function should again return another function. After three levels, 
# calling the final function should produce a result based on values remembered
# from all previous levels.


def f1(n1):
    def f2(n2):
        def f3(n3):
            return n1+n2+n3  # it will remember values from f1,f2
        return f3
    return f2

r1 = f1(4)
r2 = r1(5)
r3 = r2(10)
print(r3)
x=5 #global variable
def fun():
    x=7 #local varriable
    return x

print(fun())
print(x)


def fun1():
    global x
    x=9
    return x
print(x)
print(fun1())
print(x)


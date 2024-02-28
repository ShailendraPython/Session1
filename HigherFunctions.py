def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def Arith(fun):
    a=fun(20,10)
    print(a)

Arith(add)
Arith(sub)
def add(a,b):
    return a+b

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))

sum=add(a,b)
print(sum)


def sum(a,b=1,c=2):
    return a+b+c
sum1=sum(3)
sum2=sum(3,3,3)
print(sum1)
print(sum2)


def add1(a,b,c):
    return a+b+c
print(add1(1,2,3))
print(add1(10,c=20,b=30))


def add_num(*n):
    #return a+b+c+d
    print(sum(n))
add_num(1,2,3,4,5,6)
# print(n)
# print(1,2,3,4)
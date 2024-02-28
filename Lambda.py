def add(x, y):
    return x + y

# Equivalent lambda function
lambda_add = lambda x, y: x + y
lambda_sub = lambda x, y: x - y


# Example usage
a1 = add(3, 4)
a2 = lambda_add(3, 4)

print("Result from regular function:", a1)
print("Result from lambda function:", a2)



# li = [1,2,3,4,5,]
# print((lambda x : x+1)(li))


l2 = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, l2)
print(list(square))
# def func(a):
#     return a+5

func = lambda a : a+5 # In some functions, sometimes we need to pass a function as an argument. In those cases lambda function comes to picture.
square = lambda x : x*x
sum = lambda a, b, c : a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6
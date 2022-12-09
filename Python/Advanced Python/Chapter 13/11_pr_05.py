from functools import reduce
l = [3, 8, 455, 2, 5, 45]

# print(max(7, 34))

a = reduce(max, l)
print(a)


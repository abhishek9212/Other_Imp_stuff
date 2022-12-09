def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num: num > 10

l = [1, 2, 3, 43, 43, 7, 8, 54, 6]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))
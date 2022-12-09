def square(num):
    return num*num

l = [1, 2, 4]
# Now if we want to apply this square function for all the values of the list l, then:

# Method 1
# l2 = []
# for item in l:
#     l2.append(square(item))
# print(l2)

# Method 2
# print(map(square, l))  # This will give output as <map object at 0x0000022A53A5E230>. As, this returns a map object.
#  So, we have to typecast it into a list as shown below.
print(list(map(square, l)))
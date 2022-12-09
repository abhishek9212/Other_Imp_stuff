# enumerate --> to name a list of things separately, one by one

list1 = [43, 453, 23, False, 6.2, "Abhishek"]

# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

for index, item in enumerate(list1):  # instead of index, item we can write anything like (a, b) but the first one will be index and second will be item.
    # print(item, index)
    print(index, item)

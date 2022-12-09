l = [10, 5, 5432, 645, 6, 27]

# divby5 = lambda num : num%5==0

# divisible = list(filter(divby5, l))

# print(divisible)

######## ANOTHER WAY TO WRITE THE SAME ########

divisible = list(filter(lambda a : a%5 == 0, l))

print(divisible)
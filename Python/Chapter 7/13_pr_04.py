# num = int(input("Enter a number: "))
# x = (num/2)+1
# if(num == 2 or num == 3):
#     print("This is a prime number.")
# elif(num == 1):
#     print("This is not a prime number.")
# if(num != 1 and num != 2 and num != 3):

#     for i in range(2, int(x)):
#     # print(i)
#         if(num%(i)) == 0:
#             print("This is not a prime number.")
#             break
#     else:
#         print("This is a prime number.")



################## Second approach ###################

num2 = int(input("Enter a number: "))
prime = True

for i in range(2, num2):
    print(i)
    if(num2%i) == 0:
        prime = False
        break

if prime == True:
    print("The number is prime")
else:
    print("The number is not prime")
        
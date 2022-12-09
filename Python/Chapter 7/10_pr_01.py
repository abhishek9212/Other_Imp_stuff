num = int(input("Enter a number: "))

print("The multiplication table of the given number is\n")

for i in range(1, 11):
    # print(num*i)
    
    # print(f"{num}x{i}={num*i}") # f strings concept. 
                                # In these strings we just have to give that has to be converted to string inside curly braces.


# the above f string printf is same as
    print(str(num) + "x" + str(i) + "====" + str(num*i))
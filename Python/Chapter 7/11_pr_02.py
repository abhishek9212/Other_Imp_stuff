l1 = ['Harry', 'Sohan', 'Sachin', 'Rahul']

# for name in l1:
#     if(name[0] == 'S' or name[0] == 's'):
#         print("Hello " + name)
#     else:
#         print("No Greetings for you Mr." + name)

# Second way
for name in l1:
    if name.startswith("S"):
        print("Hello " + name)
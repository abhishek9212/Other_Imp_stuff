num = int(input("Enter a number: "))

print("The multiplication table of the given number in reverse order is\n")

for i in range(10, 0, -1):
    print(f"{num} x {i} = {num*i}")
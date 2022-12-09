lines = int(input("Enter any number of stars: "))

for i in range(lines):
    if(i == 0 or i == (lines-1)):
        print("* " * lines)
    else:
        print("* ", end = "")
        print("  " * (lines-2), end = "")
        print("*")


       
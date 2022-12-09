try:
    i = int(input("Enter a number: "))
    c = 1/i 
except Exception as e:
    print(e)
    exit()  # Even if we exit/terminate the program, finally will execute
finally:  
    print("We are Done")

print("Thanks for using the program")
try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
    
except ValueError as e:
    print("Please Enter a valid value")
    # print(e)  # the output which it throws is not an error, otherwise the program would stop here only if it was an error
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")
    # print(e) 

print("Thanks for using this code!")
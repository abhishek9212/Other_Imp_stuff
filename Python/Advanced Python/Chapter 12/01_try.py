while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying...") # the program will execute this statement and try to run this code even if exception occurs.
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your Input resulted in an error: {e}")  # program will not stop even if this error comes by accident, only that iteration will be killed and this error will be shown in that iteration

print("Thanks for playing this game")


# Now, this program is a command line application. But if it would have been a GUI then we would have coded
# in GUI and would have operated the GUI according to the code. Now, if someone doesn't know how to play 
# and enters his/her name, then the GUI would crash and the program would show a value error(ValueError: invalid literal for int() with base 10: 'Abhishek')
# But we don't want the GUI/software to crash and also don't want the user to see the error. Instead, we want
# to handle it somehow and show the user that what mistake he/she has done and what should they do to resolve it.
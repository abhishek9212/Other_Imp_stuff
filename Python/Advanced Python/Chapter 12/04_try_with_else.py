try:
    i = int(input("Enter a number: "))
    c = 1/i 
except Exception as e:
    print(e)
else:  # This else block will only run if the code written in try block runs successfully without any problem
    print("We were successfull!")
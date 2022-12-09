name = input("Enter name of the student:")
marks = input("Enter marks of the student:")
phone = input("Enter phone number of the student:")

formattedString1 = "The name of the student is {0}, his marks are {1} and the phone number is {2}".format(name, marks, phone)
formattedString2 = "The name of the student is {}, his marks are {} and the phone number is {}".format(name, marks, phone)
formattedString3 = f"The name of the student is {name}, his marks are {marks} and the phone number is {phone}"
print(formattedString1)
print(formattedString2)
print(formattedString3)

# All three are SAME
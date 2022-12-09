class Employee:
    company = 'Google'
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attributes salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45  # this will create a new instance variable
print(harry.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class
# print(rajni.address)

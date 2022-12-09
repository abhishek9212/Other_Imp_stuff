class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property    # this property decorator makes this function behave like a property(i.e. Attribute or variable) . This method with property decorator is also known as a getter method.
    def totalSalary(self):
        return self.salary + self.salarybonus  # internally this function will run and return the value but it will return like it's a property.

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
# print(e.totalSalary) # we can print it like a normal variable 

# Now, because it is behaving like a normal property, so we should be able to change it like a property.
# We can change totalSalary like a normal property for ex- e.totalSalary = 5800 but we have to set the values of salary and salarybonus accordingly and that's why we have to call setter function here.

e.totalSalary = 5800  # this 5800 is getting passed in the setter method as "val" argument.
print(e.salary)
print(e.salarybonus)

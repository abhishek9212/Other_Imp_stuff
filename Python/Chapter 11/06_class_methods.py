class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):   # This function will just create a new instance attribute salary and will make it equal to sal and will not change class attribute
    #     self.salary = sal       # One way is to write like this := self.__class__.salary = sal , where self.__class__ just gives the class name of the object self.

    # Second Alternative
    @classmethod  # This is a decorator which is a function which takes a function as an input and modifies it.
    def changeSalary(cls, sal):
        cls.salary = sal
        

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
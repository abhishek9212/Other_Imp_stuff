class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")   # this means company and salary of the object on which you are running


harry = Employee()
harry.salary = 100000
harry.getSalary()  # is same as Employee.getSalary(harry)




# if we remove self from getSalary() in the class definition then this error shows up 
# Employee.getSalary() takes 0 positional arguments but 1 was given because internally this call
# harry.getSalary() gets converted to Employee.getSalary(harry)
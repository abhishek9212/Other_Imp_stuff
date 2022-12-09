class Employee:
    company = "Google"

    def getSalary(self, signature):  # we can also give other arguments with self.
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")     # this means company and salary of the object on which you are running
    
    @staticmethod  # is used in methods in which we don't want to use it's attributes in any means. Like in the one shown below, we want to just print a line.
    def greet():    # now if we give self here then we have to pass harry(instance) in the function call manually otherwise it will give the error i.e. Employee.greet() missing 1 required positional argument: 'self'
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the Morning.")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!")  # is same as Employee.getSalary(harry)
harry.greet() #gets converted to this--> Employee.greet(harry) in backend but if we give static method decorator(@staticmethod) in the definition of the function then it converts it to Employee.greet()
harry.time()
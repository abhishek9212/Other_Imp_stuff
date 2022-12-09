class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am Breathing... ")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am luckily Breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am Breathing++")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()

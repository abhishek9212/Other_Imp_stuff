class Person:
    country = "India"

    def takeBreath(self):
        print("I am Breathing... ")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee so I am luckily Breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        print("I am an Programmer so I am Breathing++")


p = Person()
p.takeBreath()
# print(p.company)  # throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country) # Prints the variable/attribute value which is present in the nearest parent class. 


 
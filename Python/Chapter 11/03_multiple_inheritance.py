class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company)   # Visa will get printed because the one which is written first in argument list in Programmer will be given priority. 
print(p.level)
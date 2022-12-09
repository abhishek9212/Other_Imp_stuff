from ast import Num


class Number:
    def __init__(self, num):
        self.num = num 
    def __add__(self, num2):  # dunder add method(Dunder method is the one with __ at the start and end)
        print("Let's add")
        return self.num + num2.num
    def __mul__(self, num2):  # dunder mul method , these methods are given in Python documentation
        print("Let's multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
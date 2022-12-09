class Number:
    def __init__(self, num):
        self.num = num 
    def __add__(self, num2):  
        print("Let's add")
        return self.num + num2.num
    def __mul__(self, num2):  
        print("Let's multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal number: {self.num}"

    def __len__(self):
        return 1

n = Number(9)
print(n)  # this gives output like <__main__.Number object at 0x0000026496927CA0>, but if we want 
# different output to be displayed when we print it(an object), then we'll use __str__ dunder method.
print(len(n)) # if dunder method __len__ is not defined then it gives error like : TypeError: object of type 'Number' has no len() 
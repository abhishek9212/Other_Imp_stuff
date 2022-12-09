# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self, c):
        mulReal = (self.real * c.real) - (self.imaginary * c.imaginary)
        mulImaginary = (self.real * c.imaginary) + (self.imaginary * c.real)
        return Complex(mulReal, mulImaginary)

    def __str__(self):
        if self.imaginary < 0:
            return f"The Complex number is : {self.real} - {-self.imaginary}i"
        else:
            return f"The complex number is: {self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)  # This print calls both dunder methods, firstly because there are two objects inside it which 
#  are getting added directly that's why add method got called and then it returned an object of class
#  Complex only so after that on this print statement only the str dunder method got called as we are 
# printing an object. 
print(c1 * c2)
a = 54 # Global Variable
def func1():
    global a  # By this global keyword, we are saying use Global keyword "a". Do not create a local variable "a" of the function
    print(f"Print statement 1: {a}")
    a = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")
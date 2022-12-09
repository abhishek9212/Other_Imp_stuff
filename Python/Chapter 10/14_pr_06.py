class Sample:
    def __init__(kuchbhi, name):   # yes, we can change self parameter to any valid identifier. But, we does not change it usually as we want the code to be easily readable and understandable.
        kuchbhi.name = name

obj = Sample("Abhishek")
print(obj.name)
class Sample:
    a = 45

obj = Sample()
obj.a = 0    # this creates a new 'a' attribute of obj object and doesn't change the class attribute 
# Sample.a = 0   # this will change the class attribute

print(Sample.a)
print(obj.a) 
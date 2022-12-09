# Up until python 3.5 there was no f string, it was introduced in python 3.6. Before 3.6 people were using format methods.

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"

# a = f'This is {name}'
# a = "This is {}".format(name)
# a = "This is {} and his channel is {}".format(name, channel)
# a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
a = "This is {} and his {} channel is {}".format(name, channel, type)
print(a)


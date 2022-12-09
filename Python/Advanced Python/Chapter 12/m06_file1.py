def greet(name):
    print(f"Good Morning, {name}")

# print(__name__)  # if we run this from this file only then __name__ gives '__main__', but if we run from another file by importing that module file then it stores that file name in it.
if __name__ == '__main__':
    n = input("Enter a name\n")
    greet(n)
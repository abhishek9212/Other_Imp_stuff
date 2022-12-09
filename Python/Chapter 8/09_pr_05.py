import time

def recurstar(n):
    if n == 0:
        return 0
    print("*" * n)
    recurstar(n-1)

num = int(input("Enter a number: "))
recurstar(num)


def recurSum(n):
    if n == 0:
        return 0
    sum = n + recurSum(n-1)
    return sum

num = int(input("Enter a number: "))

print("The sum of the natural numbers upto this number is:", recurSum(num))
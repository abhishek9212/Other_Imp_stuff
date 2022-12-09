def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return (product)

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    fact = (n) * factorial_recursive(n-1)
    return fact

f = factorial_iter(5)
print(f)

print(factorial_recursive(5))

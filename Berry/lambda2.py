def factorial(n):
    if n == 0:
        return 1
    variable = n * factorial(n - 1)
    return variable
print(factorial(9))
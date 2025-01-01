def factorial(n):
    print(f"Calling factorial({n})") 
          
    if n == 0 :
        print(f"Base case reached: factorial(0) = 1")
        return 1

    result = n * factorial(n - 1)
    print(f"Returning: {n} * factorial ({n - 1}) = {result}")

    return result


print(factorial)
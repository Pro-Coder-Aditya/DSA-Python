def fact(n):
    # Base Case
    if (n == 1):
        return 1
    
    return n * fact(n - 1)

print(fact(10))
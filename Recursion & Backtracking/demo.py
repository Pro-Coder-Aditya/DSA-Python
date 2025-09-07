def abc(n):
    # Base Case
    if (n == 0):
        return print(0)

    print(n)
    return abc(n - 1)

abc(3)
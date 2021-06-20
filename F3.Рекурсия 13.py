def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return n * f(n-1) - 2 * f(n-2)


print(f(8))

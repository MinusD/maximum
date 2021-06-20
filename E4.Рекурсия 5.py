def f(n):
    if n <= 6:
        return n // 2
    elif n % 4 == 0:
        return f(n % 3) + 2 * g(n-1)
    else:
        return g(n-2) + g(n-3) - f(n-1)

def g(n):
    if n <= 6:
        return 64 - 2*n
    else:
        return f(n-2) + 3*g(n-2)


print(f(22))

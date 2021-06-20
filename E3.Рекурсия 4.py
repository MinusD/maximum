def f(n):
    if n < 3:
        return n + 9
    else:
        return 2*f(n-1) + 3 * g(n-2)

def g(n):
    if n < 4:
        return 25 - n
    else:
        return 4 * g(n-1) - f(n-2)

print(g(10))

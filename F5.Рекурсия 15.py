def f(n):
    if n == 1 or n == 2:
        return n
    else:
        return f(n-1) + 2 * g(n-2)

def g(n):
    if n == 1 or n == 2:
        return n
    else:
        return 2 * g(n-1) + f(n-2)


print(f(12))

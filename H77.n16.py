def f(n):
    if n < 3:
        return n
    if n%5 == 0:
        return f(n-3) + 3*f(n-4) + f(n-2)
    if n%10 == 3:
        return 10 + f(n-1)
    return 2*f(n-2) + f(n-1)
print(f(17))

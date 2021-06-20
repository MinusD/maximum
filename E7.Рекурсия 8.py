def f(n):
    if n == 1:
        return 2
    else:
        return f(n-1) + 3*n


print(f(38))

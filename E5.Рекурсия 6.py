def f(n):
    if n == 1:
        return 3
    else:
        return f(n-1) + 2*n

print(f(31))

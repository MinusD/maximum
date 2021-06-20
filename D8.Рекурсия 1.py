def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3*f(n-1) + 2*f(n-2) + (n - 1)


print(f(5))

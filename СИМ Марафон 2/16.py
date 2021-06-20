def f(n):
    if n == 1:
        return 1
    elif n %3 == 0:
        return 3*f(n-2) + 4
    elif n%3 == 1:
        return 1+ 8*f(n-1)
    else:
        return 2 * f(n-1) + 8

print(f(11))

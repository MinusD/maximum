def f(n):
    if n == 1:
        return 10
    elif n%5 == 0:
        return n * f(n-1)+1
    elif n %10 == 3:
        return 5 + f(n-2)
    else:
        return f(n-1) + 2

print(f(17))

def f(n):
    if n < 4:
        return n
    else:
        return f(n-3) + f(n-2)


print(f(21))

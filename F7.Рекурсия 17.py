def f(n):
    if n == 15:
        return n * n
    else:
        return n + f(n+1)

print(f(5))

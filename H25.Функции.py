def f(n):
    if n<3:
        return(n)
    else:
        return(f(n-1) + f(n-3))
print(f(18))

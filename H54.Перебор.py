for i in range(1000):
    s = i
    n = 0
    while s-n > 0:
        s -= 15
        n+=10
    if n == 50:
        print(i)

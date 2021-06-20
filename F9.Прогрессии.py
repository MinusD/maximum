for i in range(-50, 100):
    n = i
    s = 0
    while s-n <= 250:
        s = s + 25
        n+=1
    if n == 10:
        print(i)
    print(i, n)

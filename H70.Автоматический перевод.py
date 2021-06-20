for o in range(2, 100):
    n = 87
    nn = ''
    while n != 0:
        nn += str(n%o) + " "
        n//=o
    print(o, nn[::-1])

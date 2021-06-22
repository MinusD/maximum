for i in range(1, 355):
    x = i
    x1 = ''
    while x != 0:
        x1 += str(x%6)
        x//=6
    x1 = x1[::-1]
    x1 = int(x1 + x1[-1:])
    x2 = bin(x1)[2:]
    x2 = x2 + x2[-1:]
    print(i, int(x2, 2))

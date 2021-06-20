s = []
for o in range(2, 100):
    n = 56
    nn = ''
    while n != 0:
        nn += str(n%o) + " "
        n//=o
    print(o, nn[::-1])
    if int(nn[:2]) == 2:
        s.append(o)
print(s)

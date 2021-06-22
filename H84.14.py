n = 125 ** 200 +74
for x in range(1000):
    n -= 5 ** x 
    nn = ''
    while n != 0:
        nn +=str(int(n%5))
        n//=5
    if nn.count('4') == 100:
        print(x, nn.count('4'))
        break

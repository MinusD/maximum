n = (7 ** 80 - (10 - 3) ** 4 ) * 5/6*8
nn = ''
while n != 0:
    nn +=str(int(n%7))
    n//=7
print(nn.count('4'))

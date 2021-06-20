n = 16
nn = ''
while n != 0:
    nn += str(n%4)
    n//=4
print(nn[::-1])

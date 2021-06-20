n = 16
o = 3

nn = ''
while n != 0:
    nn += str(n%o) + ""
    n//=o
print(nn[::-1])

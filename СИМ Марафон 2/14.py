n  = 9 ** 40 + 3 ** 15 - 81
st = ''
while n != 0:
    st+= str(n%3)
    n//=3
print(st[::-1])
    

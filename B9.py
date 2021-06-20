for i in range(1000):
    n = 200
    s = i
    while 120 < s*s and s!= 11:
        s+=1
        n-=10
        print(i)
    if n == 120:
        print('Correct:', i)

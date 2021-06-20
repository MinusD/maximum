for i in range(1, 10000):
    a = i
    b = 0
    while a!= 256 and b<=10000:
        a*=2
        b+=a
    if b == 256:
        print("Correct", i)


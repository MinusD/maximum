for i in range(1000):
    s = i
    a = 0
    while a<=50:
        a+=10
        s+=a
    if s == 250:
        print(i)

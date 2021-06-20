for i in range(1000):
    s=0
    n=i
    while 2*s*s<127 and s <30:
        s+=1
        n+=2
    if n==20:
        print("Correct", i)

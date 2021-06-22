for i in range(1204300, 1204381):
    d = []
    for x in range(2, i//2+1):
        if x%2==0 and i%x == 0:
            d.append(x)
    if sum(d)%10 == 0 and sum(d)!=0:
        print(i, sum(d))

for i in range(20000):
    n = i
    s=0
    while s-n <=250:
        s+=25
        n+=1
    #print(i, n)
    if n == 10:
        print('Correct', i)

for a in range(1000):
    err = 0
    for x in range(100):
        for y in range(100):
            if (x*y >a) or x>y or 8>x:
                err+=0
            else:
                err+=1
                break
        if err != 0:
            break
    if err == 0:
        print(a)

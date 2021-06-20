for a in range(100):
    err = 0
    for x in range(1, 100):
        for y in range(1, 100):
            if y + 2*x != 36 or a < x or a < y:
                err = err
            else:
                err +=1
    if err == 0:
        print(a)
    else:
        print("not", a, err)
    

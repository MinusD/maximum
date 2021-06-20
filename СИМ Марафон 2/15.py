r = 100
for a in range(1, 500):
    err = 0
    for x in range(r):
        for y in range(r):
            if (x > 15 or x**2 <=a) and (y**2 <=a or y > 16):
                err +=0
            else:
                err +=1
    if err == 0:
        print(a)
    

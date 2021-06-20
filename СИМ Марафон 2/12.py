r = 100
for ii in range(50):
    for x1 in range(-r, r+1):
        for y1 in range(-r, r+1):
            x = -3
            y = -12
            for i in range(ii):
                x+=(x1+1)
                y+=(y1 - 2)
            x-=13
            y-=12
            if x == 0 and y == 0:
                print(ii, x1, y1)

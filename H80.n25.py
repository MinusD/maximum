for a in range(290, 301):
#for a in range(280555,255022, -1):
    dl = []
    for i in range(2, a//2+1):
        if i%2!=0:
            if a%i == 0:
                dl.append(i)
    if len(dl) == 5:
        print(a, (dl)[::-1])

    

m = 0
for d in range(1000):
    xx = d+1
    for a in range(100):
        for x in range(100):
            if not ((x>=3 and x<=15) == (x>=14 and x<=25)) or not(x>=a and x<=(a+d)):
                m = max(m, xx)
               

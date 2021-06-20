# not(x%6==0 and x%9==0) or x%a==0
for a in range(1, 500):
    err = 0
    for x in range(1, 200):
        if x%6!=0 or x%9!=0 or x%a==0:
            err +=1
    print(a, err)
    if err == 0:
        print(a)

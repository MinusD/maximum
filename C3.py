c = 0
for i in range(1000):
    s=i
    n=0
    while s != 0:
        s-=1
        n+=s
    if (n == 21):
        c+=1
        print(str(c)+". " + "Correct:", i)

for i in range(1000):
    x = i
    a=0
    b=0
    while x>0:
        b+=x%10
        if x%2==0:
            a+=1
        x//=10
    if a==3 and b == 14:
        print(i)

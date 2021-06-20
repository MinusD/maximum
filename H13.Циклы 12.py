for i in range(1000):
    x = i
    a=0
    b=1
    while x>0:
        a+=1
        b*=x%10
        x//=10
    if a==2 and b == 0:
        print(i)

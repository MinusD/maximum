a,b=map(int,input().split())
while a + b > 1000 :
    a -= 2
    b -= 20
print(a, b)

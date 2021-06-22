counter = 0
for i in range(100000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a+=1
        if x%2 != 0:
            b+=1
        x//=2
    if a == 16 and b == 14:
        counter+=1
print(counter)
        

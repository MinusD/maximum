for i in range(1000):
    co = 0
    for j in range(2,i):
        if i%j == 0:
            co+=1
    if co == 4:
        print(i,co, i ** 0.5)
            
